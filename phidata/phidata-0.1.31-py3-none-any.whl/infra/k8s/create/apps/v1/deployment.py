from typing import Dict, List, Optional

from pydantic import BaseModel

from phidata.infra.k8s.create.core.v1.container import CreateContainer
from phidata.infra.k8s.create.core.v1.volume import CreateVolume
from phidata.infra.k8s.enums.api_version import ApiVersion
from phidata.infra.k8s.enums.kind import Kind
from phidata.infra.k8s.enums.restart_policy import RestartPolicy
from phidata.infra.k8s.resource.apps.v1.deployment import (
    Deployment,
    DeploymentSpec,
    LabelSelector,
    PodTemplateSpec,
)
from phidata.infra.k8s.resource.core.v1.container import Container
from phidata.infra.k8s.resource.core.v1.pod_spec import PodSpec
from phidata.infra.k8s.resource.core.v1.volume import Volume
from phidata.infra.k8s.create.common.labels import create_component_labels_dict
from phidata.infra.k8s.resource.meta.v1.object_meta import ObjectMeta
from phidata.utils.log import logger


class CreateDeployment(BaseModel):
    deploy_name: str
    pod_name: str
    app_name: str
    namespace: Optional[str] = None
    service_account_name: Optional[str] = None
    replicas: Optional[int] = 1
    containers: List[CreateContainer]
    init_containers: Optional[List[Container]] = None
    pod_node_selector: Optional[Dict[str, str]] = None
    restart_policy: RestartPolicy = RestartPolicy.ALWAYS
    termination_grace_period_seconds: Optional[int] = None
    volumes: Optional[List[CreateVolume]] = None
    labels: Optional[Dict[str, str]] = None
    pod_annotations: Optional[Dict[str, str]] = None

    def create(self) -> Optional[Deployment]:
        """Creates the Deployment resource"""

        deploy_name = self.deploy_name
        logger.debug(f"Init Deployment resource: {deploy_name}")

        deploy_labels = create_component_labels_dict(
            component_name=deploy_name,
            app_name=self.app_name,
            labels=self.labels,
        )

        pod_name = self.pod_name
        pod_labels = create_component_labels_dict(
            component_name=pod_name,
            app_name=self.app_name,
            labels=self.labels,
        )

        create_containers = self.containers
        containers: List[Container] = []
        for cc in create_containers:
            container = cc.create()
            if container is not None:
                containers.append(container)

        volumes: Optional[List[Volume]] = None
        if self.volumes:
            volumes = []
            for cv in self.volumes:
                volume = cv.create()
                if volume:
                    volumes.append(volume)

        deployment = Deployment(
            name=deploy_name,
            api_version=ApiVersion.APPS_V1,
            kind=Kind.DEPLOYMENT,
            metadata=ObjectMeta(
                name=deploy_name,
                namespace=self.namespace,
                labels=deploy_labels,
            ),
            spec=DeploymentSpec(
                replicas=self.replicas,
                selector=LabelSelector(match_labels=pod_labels),
                template=PodTemplateSpec(
                    # TODO: fix this
                    metadata=ObjectMeta(
                        name=pod_name,
                        namespace=self.namespace,
                        labels=pod_labels,
                        annotations=self.pod_annotations,
                    ),
                    spec=PodSpec(
                        init_containers=self.init_containers,
                        node_selector=self.pod_node_selector,
                        service_account_name=self.service_account_name,
                        restart_policy=self.restart_policy,
                        containers=containers,
                        termination_grace_period_seconds=self.termination_grace_period_seconds,
                        volumes=volumes,
                    ),
                ),
            ),
        )

        # logger.debug(
        #     f"Deployment {deploy_name}:\n{deployment.json(exclude_defaults=True, indent=2)}"
        # )
        return deployment
