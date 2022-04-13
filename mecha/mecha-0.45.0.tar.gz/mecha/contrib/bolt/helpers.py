__all__ = [
    "get_bolt_helpers",
]


from dataclasses import dataclass, replace
from functools import partial, wraps
from importlib import import_module
from types import TracebackType
from typing import Any, Callable, ContextManager, Dict, Optional, Type
from uuid import UUID

from tokenstream import set_location

from mecha import (
    AstBool,
    AstChildren,
    AstColor,
    AstCoordinate,
    AstGamemode,
    AstGreedy,
    AstItemSlot,
    AstJson,
    AstMessage,
    AstNbt,
    AstNbtPath,
    AstNode,
    AstNumber,
    AstObjective,
    AstObjectiveCriteria,
    AstPlayerName,
    AstRange,
    AstResourceLocation,
    AstScoreboardSlot,
    AstSortOrder,
    AstString,
    AstSwizzle,
    AstTeam,
    AstTime,
    AstUUID,
    AstVector2,
    AstVector3,
    AstWord,
)

from .utils import internal


def get_bolt_helpers() -> Dict[str, Any]:
    """Return a collection of helpers used by the generated code."""
    return {
        "replace": replace,
        "missing": object(),
        "children": AstChildren,
        "operator_not": operator_not,
        "operator_in": operator_in,
        "operator_not_in": operator_not_in,
        "branch": BranchDriver,
        "get_rebind": get_rebind,
        "get_attribute": get_attribute,
        "import_module": python_import_module,
        "interpolate_bool": converter(AstBool.from_value),
        "interpolate_numeric": converter(AstNumber.from_value),
        "interpolate_coordinate": converter(AstCoordinate.from_value),
        "interpolate_time": converter(AstTime.from_value),
        "interpolate_word": converter(AstWord.from_value),
        "interpolate_phrase": converter(AstString.from_value),
        "interpolate_greedy": converter(AstGreedy.from_value),
        "interpolate_json": converter(AstJson.from_value),
        "interpolate_nbt": converter(AstNbt.from_value),
        "interpolate_nbt_path": converter(AstNbtPath.from_value),
        "interpolate_range": converter(AstRange.from_value),
        "interpolate_resource_location": converter(AstResourceLocation.from_value),
        "interpolate_item_slot": converter(AstItemSlot.from_value),
        "interpolate_objective": converter(AstObjective.from_value),
        "interpolate_objective_criteria": converter(AstObjectiveCriteria.from_value),
        "interpolate_scoreboard_slot": converter(AstScoreboardSlot.from_value),
        "interpolate_swizzle": converter(AstSwizzle.from_value),
        "interpolate_team": converter(AstTeam.from_value),
        "interpolate_color": converter(AstColor.from_value),
        "interpolate_sort_order": converter(AstSortOrder.from_value),
        "interpolate_gamemode": converter(AstGamemode.from_value),
        "interpolate_message": converter(AstMessage.from_value),
        "interpolate_vec2": converter(AstVector2.from_value),
        "interpolate_vec3": converter(AstVector3.from_value),
        "interpolate_entity": EntityConverter(
            uuid_converter=converter(AstUUID.from_value),
            player_name_converter=converter(AstPlayerName.from_value),
        ),
    }


@internal
def operator_not(obj: Any):
    if func := getattr(type(obj), "__not__", None):
        return func(obj)
    return not obj


@internal
def operator_in(item: Any, container: Any):
    if func := getattr(type(item), "__within__", None):
        return func(item, container)
    if func := getattr(type(container), "__contains__", None):
        return func(container, item)
    return item in container


@internal
def operator_not_in(item: Any, container: Any):
    return operator_not(operator_in(item, container))


class BranchDriver:
    obj: Any
    context_manager: Optional[ContextManager[Any]]

    @internal
    def __init__(self, obj: Any):
        self.obj = obj
        self.context_manager = None
        if func := getattr(type(obj), "__branch__", None):
            self.context_manager = func(obj)

    @internal
    def __enter__(self) -> Any:
        if self.context_manager is not None:
            return self.context_manager.__enter__()
        return self.obj

    @internal
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        if self.context_manager is not None:
            return self.context_manager.__exit__(exc_type, exc, traceback)


@internal
def get_rebind(obj: Any):
    if func := getattr(type(obj), "__rebind__", None):
        return partial(func, obj)
    return None


@internal
def get_attribute(obj: Any, attr: str):
    try:
        return getattr(obj, attr)
    except AttributeError as exc:
        try:
            return obj[attr]
        except (TypeError, LookupError):
            raise exc from None


@internal
def python_import_module(name: str):
    try:
        return import_module(name)
    except Exception as exc:
        tb = exc.__traceback__
        tb = tb.tb_next.tb_next  # type: ignore
        while tb and tb.tb_frame.f_code.co_filename.startswith("<frozen importlib"):
            tb = tb.tb_next
        raise exc.with_traceback(tb)


def converter(f: Callable[[Any], AstNode]) -> Callable[[Any, AstNode], AstNode]:
    internal(f)

    @internal
    @wraps(f)
    def wrapper(obj: Any, node: AstNode) -> AstNode:
        return set_location(f(obj), node)

    return wrapper


@dataclass
class EntityConverter:
    """Converter for entities."""

    uuid_converter: Callable[[Any, AstNode], AstNode]
    player_name_converter: Callable[[Any, AstNode], AstNode]

    @internal
    def __call__(self, obj: Any, node: AstNode) -> AstNode:
        if isinstance(obj, str):
            if obj.count("-") == 4:
                return self.uuid_converter(obj, node)
            return self.player_name_converter(obj, node)
        if isinstance(obj, UUID):
            return self.uuid_converter(obj, node)
        raise ValueError(f"Invalid entity value of type {type(obj)!r}.")
