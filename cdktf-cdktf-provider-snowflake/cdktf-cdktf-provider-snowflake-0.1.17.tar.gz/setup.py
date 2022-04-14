import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-snowflake",
    "version": "0.1.17",
    "description": "Prebuilt snowflake Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/hashicorp/cdktf-provider-snowflake.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/hashicorp/cdktf-provider-snowflake.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_snowflake",
        "cdktf_cdktf_provider_snowflake._jsii"
    ],
    "package_data": {
        "cdktf_cdktf_provider_snowflake._jsii": [
            "provider-snowflake@0.1.17.jsii.tgz"
        ],
        "cdktf_cdktf_provider_snowflake": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "cdktf>=0.10.0, <0.11.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.56.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
