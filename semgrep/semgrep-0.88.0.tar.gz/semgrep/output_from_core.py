"""Generated by atdpy from type definitions in Output_from_core.atd.

This implements classes for the types defined in 'Output_from_core.atd', providing
methods and functions to convert data from/to JSON.
"""
# Disable flake8 entirely on this file:
# flake8: noqa
import json
from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import NoReturn
from typing import Optional
from typing import Tuple
from typing import Union

############################################################################
# Private functions
############################################################################


def _atd_missing_json_field(type_name: str, json_field_name: str) -> NoReturn:
    raise ValueError(
        f"missing field '{json_field_name}'" f" in JSON object of type '{type_name}'"
    )


def _atd_bad_json(expected_type: str, json_value: Any) -> NoReturn:
    value_str = str(json_value)
    if len(value_str) > 200:
        value_str = value_str[:200] + "…"

    raise ValueError(
        f"incompatible JSON value where"
        f" type '{expected_type}' was expected: '{value_str}'"
    )


def _atd_bad_python(expected_type: str, json_value: Any) -> NoReturn:
    value_str = str(json_value)
    if len(value_str) > 200:
        value_str = value_str[:200] + "…"

    raise ValueError(
        f"incompatible Python value where"
        f" type '{expected_type}' was expected: '{value_str}'"
    )


def _atd_read_unit(x: Any) -> None:
    if x is None:
        return x
    else:
        _atd_bad_json("unit", x)


def _atd_read_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    else:
        _atd_bad_json("bool", x)


def _atd_read_int(x: Any) -> int:
    if isinstance(x, int):
        return x
    else:
        _atd_bad_json("int", x)


def _atd_read_float(x: Any) -> float:
    if isinstance(x, (int, float)):
        return x
    else:
        _atd_bad_json("float", x)


def _atd_read_string(x: Any) -> str:
    if isinstance(x, str):
        return x
    else:
        _atd_bad_json("str", x)


def _atd_read_list(read_elt: Callable[[Any], Any]) -> Callable[[List[Any]], List[Any]]:
    def read_list(elts: List[Any]) -> List[Any]:
        if isinstance(elts, list):
            return [read_elt(elt) for elt in elts]
        else:
            _atd_bad_json("array", elts)

    return read_list


def _atd_read_assoc_array_into_dict(
    read_key: Callable[[Any], Any],
    read_value: Callable[[Any], Any],
) -> Callable[[List[Any]], Dict[Any, Any]]:
    def read_assoc(elts: List[List[Any]]) -> Dict[str, Any]:
        if isinstance(elts, list):
            return {read_key(elt[0]): read_value(elt[1]) for elt in elts}
        else:
            _atd_bad_json("array", elts)
            raise AssertionError("impossible")  # keep mypy happy

    return read_assoc


def _atd_read_assoc_object_into_dict(
    read_value: Callable[[Any], Any]
) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
    def read_assoc(elts: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(elts, dict):
            return {_atd_read_string(k): read_value(v) for k, v in elts.items()}
        else:
            _atd_bad_json("object", elts)
            raise AssertionError("impossible")  # keep mypy happy

    return read_assoc


def _atd_read_assoc_object_into_list(
    read_value: Callable[[Any], Any]
) -> Callable[[Dict[str, Any]], List[Tuple[str, Any]]]:
    def read_assoc(elts: Dict[str, Any]) -> List[Tuple[str, Any]]:
        if isinstance(elts, dict):
            return [(_atd_read_string(k), read_value(v)) for k, v in elts.items()]
        else:
            _atd_bad_json("object", elts)
            raise AssertionError("impossible")  # keep mypy happy

    return read_assoc


def _atd_read_nullable(
    read_elt: Callable[[Any], Any]
) -> Callable[[Optional[Any]], Optional[Any]]:
    def read_nullable(x: Any) -> Any:
        if x is None:
            return None
        else:
            return read_elt(x)

    return read_nullable


def _atd_write_unit(x: Any) -> None:
    if x is None:
        return x
    else:
        _atd_bad_python("unit", x)


def _atd_write_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    else:
        _atd_bad_python("bool", x)


def _atd_write_int(x: Any) -> int:
    if isinstance(x, int):
        return x
    else:
        _atd_bad_python("int", x)


def _atd_write_float(x: Any) -> float:
    if isinstance(x, (int, float)):
        return x
    else:
        _atd_bad_python("float", x)


def _atd_write_string(x: Any) -> str:
    if isinstance(x, str):
        return x
    else:
        _atd_bad_python("str", x)


def _atd_write_list(
    write_elt: Callable[[Any], Any]
) -> Callable[[List[Any]], List[Any]]:
    def write_list(elts: List[Any]) -> List[Any]:
        if isinstance(elts, list):
            return [write_elt(elt) for elt in elts]
        else:
            _atd_bad_python("list", elts)

    return write_list


def _atd_write_assoc_dict_to_array(
    write_key: Callable[[Any], Any], write_value: Callable[[Any], Any]
) -> Callable[[Dict[Any, Any]], List[Tuple[Any, Any]]]:
    def write_assoc(elts: Dict[str, Any]) -> List[Tuple[str, Any]]:
        if isinstance(elts, dict):
            return [(write_key(k), write_value(v)) for k, v in elts.items()]
        else:
            _atd_bad_python("Dict[str, <value type>]]", elts)
            raise AssertionError("impossible")  # keep mypy happy

    return write_assoc


def _atd_write_assoc_dict_to_object(
    write_value: Callable[[Any], Any]
) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
    def write_assoc(elts: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(elts, dict):
            return {_atd_write_string(k): write_value(v) for k, v in elts.items()}
        else:
            _atd_bad_python("Dict[str, <value type>]", elts)
            raise AssertionError("impossible")  # keep mypy happy

    return write_assoc


def _atd_write_assoc_list_to_object(
    write_value: Callable[[Any], Any],
) -> Callable[[List[Any]], Dict[str, Any]]:
    def write_assoc(elts: List[List[Any]]) -> Dict[str, Any]:
        if isinstance(elts, list):
            return {_atd_write_string(elt[0]): write_value(elt[1]) for elt in elts}
        else:
            _atd_bad_python("List[Tuple[<key type>, <value type>]]", elts)
            raise AssertionError("impossible")  # keep mypy happy

    return write_assoc


def _atd_write_nullable(
    write_elt: Callable[[Any], Any]
) -> Callable[[Optional[Any]], Optional[Any]]:
    def write_nullable(x: Any) -> Any:
        if x is None:
            return None
        else:
            return write_elt(x)

    return write_nullable


############################################################################
# Public classes
############################################################################


@dataclass
class ID:
    """Original type: unique_id_type = [ ... | ID | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "ID"

    @staticmethod
    def to_json() -> Any:
        return "id"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class AST:
    """Original type: unique_id_type = [ ... | AST | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "AST"

    @staticmethod
    def to_json() -> Any:
        return "AST"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class UniqueIdType:
    """Original type: unique_id_type = [ ... ]"""

    value: Union[ID, AST]

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return self.value.kind

    @classmethod
    def from_json(cls, x: Any) -> "UniqueIdType":
        if isinstance(x, str):
            if x == "id":
                return cls(ID())
            if x == "AST":
                return cls(AST())
            _atd_bad_json("UniqueIdType", x)
        _atd_bad_json("UniqueIdType", x)

    def to_json(self) -> Any:
        return self.value.to_json()

    @classmethod
    def from_json_string(cls, x: str) -> "UniqueIdType":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class UniqueId:
    """Original type: unique_id = { ... }"""

    type_: UniqueIdType
    md5sum: Optional[str] = None
    sid: Optional[int] = None

    @classmethod
    def from_json(cls, x: Any) -> "UniqueId":
        if isinstance(x, dict):
            return cls(
                type_=UniqueIdType.from_json(x["type"])
                if "type" in x
                else _atd_missing_json_field("UniqueId", "type"),
                md5sum=_atd_read_string(x["md5sum"]) if "md5sum" in x else None,
                sid=_atd_read_int(x["sid"]) if "sid" in x else None,
            )
        else:
            _atd_bad_json("UniqueId", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["type"] = (lambda x: x.to_json())(self.type_)
        if self.md5sum is not None:
            res["md5sum"] = _atd_write_string(self.md5sum)
        if self.sid is not None:
            res["sid"] = _atd_write_int(self.sid)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "UniqueId":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class RuleTimes:
    """Original type: rule_times = { ... }"""

    rule_id: str
    parse_time: float
    match_time: float

    @classmethod
    def from_json(cls, x: Any) -> "RuleTimes":
        if isinstance(x, dict):
            return cls(
                rule_id=_atd_read_string(x["rule_id"])
                if "rule_id" in x
                else _atd_missing_json_field("RuleTimes", "rule_id"),
                parse_time=_atd_read_float(x["parse_time"])
                if "parse_time" in x
                else _atd_missing_json_field("RuleTimes", "parse_time"),
                match_time=_atd_read_float(x["match_time"])
                if "match_time" in x
                else _atd_missing_json_field("RuleTimes", "match_time"),
            )
        else:
            _atd_bad_json("RuleTimes", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["rule_id"] = _atd_write_string(self.rule_id)
        res["parse_time"] = _atd_write_float(self.parse_time)
        res["match_time"] = _atd_write_float(self.match_time)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "RuleTimes":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class TargetTime:
    """Original type: target_time = { ... }"""

    path: str
    rule_times: List[RuleTimes]
    run_time: float

    @classmethod
    def from_json(cls, x: Any) -> "TargetTime":
        if isinstance(x, dict):
            return cls(
                path=_atd_read_string(x["path"])
                if "path" in x
                else _atd_missing_json_field("TargetTime", "path"),
                rule_times=_atd_read_list(RuleTimes.from_json)(x["rule_times"])
                if "rule_times" in x
                else _atd_missing_json_field("TargetTime", "rule_times"),
                run_time=_atd_read_float(x["run_time"])
                if "run_time" in x
                else _atd_missing_json_field("TargetTime", "run_time"),
            )
        else:
            _atd_bad_json("TargetTime", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["path"] = _atd_write_string(self.path)
        res["rule_times"] = _atd_write_list(lambda x: x.to_json())(self.rule_times)
        res["run_time"] = _atd_write_float(self.run_time)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "TargetTime":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class Time:
    """Original type: time = { ... }"""

    targets: List[TargetTime]
    rules: List[str]
    rules_parse_time: Optional[float] = None

    @classmethod
    def from_json(cls, x: Any) -> "Time":
        if isinstance(x, dict):
            return cls(
                targets=_atd_read_list(TargetTime.from_json)(x["targets"])
                if "targets" in x
                else _atd_missing_json_field("Time", "targets"),
                rules=_atd_read_list(_atd_read_string)(x["rules"])
                if "rules" in x
                else _atd_missing_json_field("Time", "rules"),
                rules_parse_time=_atd_read_float(x["rules_parse_time"])
                if "rules_parse_time" in x
                else None,
            )
        else:
            _atd_bad_json("Time", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["targets"] = _atd_write_list(lambda x: x.to_json())(self.targets)
        res["rules"] = _atd_write_list(_atd_write_string)(self.rules)
        if self.rules_parse_time is not None:
            res["rules_parse_time"] = _atd_write_float(self.rules_parse_time)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "Time":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class Stats:
    """Original type: stats = { ... }"""

    okfiles: int
    errorfiles: int

    @classmethod
    def from_json(cls, x: Any) -> "Stats":
        if isinstance(x, dict):
            return cls(
                okfiles=_atd_read_int(x["okfiles"])
                if "okfiles" in x
                else _atd_missing_json_field("Stats", "okfiles"),
                errorfiles=_atd_read_int(x["errorfiles"])
                if "errorfiles" in x
                else _atd_missing_json_field("Stats", "errorfiles"),
            )
        else:
            _atd_bad_json("Stats", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["okfiles"] = _atd_write_int(self.okfiles)
        res["errorfiles"] = _atd_write_int(self.errorfiles)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "Stats":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class ExcludedByConfig:
    """Original type: skip_reason = [ ... | Excluded_by_config | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "ExcludedByConfig"

    @staticmethod
    def to_json() -> Any:
        return "excluded_by_config"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class WrongLanguage:
    """Original type: skip_reason = [ ... | Wrong_language | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "WrongLanguage"

    @staticmethod
    def to_json() -> Any:
        return "wrong_language"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class TooBig:
    """Original type: skip_reason = [ ... | Too_big | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "TooBig"

    @staticmethod
    def to_json() -> Any:
        return "too_big"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Minified:
    """Original type: skip_reason = [ ... | Minified | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "Minified"

    @staticmethod
    def to_json() -> Any:
        return "minified"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Binary:
    """Original type: skip_reason = [ ... | Binary | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "Binary"

    @staticmethod
    def to_json() -> Any:
        return "binary"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class IrrelevantRule:
    """Original type: skip_reason = [ ... | Irrelevant_rule | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "IrrelevantRule"

    @staticmethod
    def to_json() -> Any:
        return "irrelevant_rule"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class TooManyMatches:
    """Original type: skip_reason = [ ... | Too_many_matches | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "TooManyMatches"

    @staticmethod
    def to_json() -> Any:
        return "too_many_matches"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class SkipReason:
    """Original type: skip_reason = [ ... ]"""

    value: Union[
        ExcludedByConfig,
        WrongLanguage,
        TooBig,
        Minified,
        Binary,
        IrrelevantRule,
        TooManyMatches,
    ]

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return self.value.kind

    @classmethod
    def from_json(cls, x: Any) -> "SkipReason":
        if isinstance(x, str):
            if x == "excluded_by_config":
                return cls(ExcludedByConfig())
            if x == "wrong_language":
                return cls(WrongLanguage())
            if x == "too_big":
                return cls(TooBig())
            if x == "minified":
                return cls(Minified())
            if x == "binary":
                return cls(Binary())
            if x == "irrelevant_rule":
                return cls(IrrelevantRule())
            if x == "too_many_matches":
                return cls(TooManyMatches())
            _atd_bad_json("SkipReason", x)
        _atd_bad_json("SkipReason", x)

    def to_json(self) -> Any:
        return self.value.to_json()

    @classmethod
    def from_json_string(cls, x: str) -> "SkipReason":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class RuleId:
    """Original type: rule_id"""

    value: str

    @classmethod
    def from_json(cls, x: Any) -> "RuleId":
        return cls(_atd_read_string(x))

    def to_json(self) -> Any:
        return _atd_write_string(self.value)

    @classmethod
    def from_json_string(cls, x: str) -> "RuleId":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class SkippedTarget:
    """Original type: skipped_target = { ... }"""

    path: str
    reason: SkipReason
    details: str
    rule_id: Optional[RuleId] = None

    @classmethod
    def from_json(cls, x: Any) -> "SkippedTarget":
        if isinstance(x, dict):
            return cls(
                path=_atd_read_string(x["path"])
                if "path" in x
                else _atd_missing_json_field("SkippedTarget", "path"),
                reason=SkipReason.from_json(x["reason"])
                if "reason" in x
                else _atd_missing_json_field("SkippedTarget", "reason"),
                details=_atd_read_string(x["details"])
                if "details" in x
                else _atd_missing_json_field("SkippedTarget", "details"),
                rule_id=RuleId.from_json(x["rule_id"]) if "rule_id" in x else None,
            )
        else:
            _atd_bad_json("SkippedTarget", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["path"] = _atd_write_string(self.path)
        res["reason"] = (lambda x: x.to_json())(self.reason)
        res["details"] = _atd_write_string(self.details)
        if self.rule_id is not None:
            res["rule_id"] = (lambda x: x.to_json())(self.rule_id)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "SkippedTarget":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True, order=True)
class Position:
    """Original type: position = { ... }"""

    line: int
    col: int
    offset: int

    @classmethod
    def from_json(cls, x: Any) -> "Position":
        if isinstance(x, dict):
            return cls(
                line=_atd_read_int(x["line"])
                if "line" in x
                else _atd_missing_json_field("Position", "line"),
                col=_atd_read_int(x["col"])
                if "col" in x
                else _atd_missing_json_field("Position", "col"),
                offset=_atd_read_int(x["offset"])
                if "offset" in x
                else _atd_missing_json_field("Position", "offset"),
            )
        else:
            _atd_bad_json("Position", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["line"] = _atd_write_int(self.line)
        res["col"] = _atd_write_int(self.col)
        res["offset"] = _atd_write_int(self.offset)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "Position":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class SkippedRule:
    """Original type: skipped_rule = { ... }"""

    rule_id: RuleId
    details: str
    position: Position

    @classmethod
    def from_json(cls, x: Any) -> "SkippedRule":
        if isinstance(x, dict):
            return cls(
                rule_id=RuleId.from_json(x["rule_id"])
                if "rule_id" in x
                else _atd_missing_json_field("SkippedRule", "rule_id"),
                details=_atd_read_string(x["details"])
                if "details" in x
                else _atd_missing_json_field("SkippedRule", "details"),
                position=Position.from_json(x["position"])
                if "position" in x
                else _atd_missing_json_field("SkippedRule", "position"),
            )
        else:
            _atd_bad_json("SkippedRule", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["rule_id"] = (lambda x: x.to_json())(self.rule_id)
        res["details"] = _atd_write_string(self.details)
        res["position"] = (lambda x: x.to_json())(self.position)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "SkippedRule":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Error_:
    """Original type: severity = [ ... | Error | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "Error_"

    @staticmethod
    def to_json() -> Any:
        return "error"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Warning:
    """Original type: severity = [ ... | Warning | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return "Warning"

    @staticmethod
    def to_json() -> Any:
        return "warning"

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class Severity:
    """Original type: severity = [ ... ]"""

    value: Union[Error_, Warning]

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return self.value.kind

    @classmethod
    def from_json(cls, x: Any) -> "Severity":
        if isinstance(x, str):
            if x == "error":
                return cls(Error_())
            if x == "warning":
                return cls(Warning())
            _atd_bad_json("Severity", x)
        _atd_bad_json("Severity", x)

    def to_json(self) -> Any:
        return self.value.to_json()

    @classmethod
    def from_json_string(cls, x: str) -> "Severity":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class MetavarValue:
    """Original type: metavar_value = { ... }"""

    start: Position
    end: Position
    abstract_content: str
    unique_id: UniqueId

    @classmethod
    def from_json(cls, x: Any) -> "MetavarValue":
        if isinstance(x, dict):
            return cls(
                start=Position.from_json(x["start"])
                if "start" in x
                else _atd_missing_json_field("MetavarValue", "start"),
                end=Position.from_json(x["end"])
                if "end" in x
                else _atd_missing_json_field("MetavarValue", "end"),
                abstract_content=_atd_read_string(x["abstract_content"])
                if "abstract_content" in x
                else _atd_missing_json_field("MetavarValue", "abstract_content"),
                unique_id=UniqueId.from_json(x["unique_id"])
                if "unique_id" in x
                else _atd_missing_json_field("MetavarValue", "unique_id"),
            )
        else:
            _atd_bad_json("MetavarValue", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["start"] = (lambda x: x.to_json())(self.start)
        res["end"] = (lambda x: x.to_json())(self.end)
        res["abstract_content"] = _atd_write_string(self.abstract_content)
        res["unique_id"] = (lambda x: x.to_json())(self.unique_id)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "MetavarValue":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class MatchExtra:
    """Original type: match_extra = { ... }"""

    metavars: Dict[str, MetavarValue]
    message: Optional[str] = None

    @classmethod
    def from_json(cls, x: Any) -> "MatchExtra":
        if isinstance(x, dict):
            return cls(
                metavars=_atd_read_assoc_object_into_dict(MetavarValue.from_json)(
                    x["metavars"]
                )
                if "metavars" in x
                else _atd_missing_json_field("MatchExtra", "metavars"),
                message=_atd_read_string(x["message"]) if "message" in x else None,
            )
        else:
            _atd_bad_json("MatchExtra", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["metavars"] = _atd_write_assoc_dict_to_object(lambda x: x.to_json())(
            self.metavars
        )
        if self.message is not None:
            res["message"] = _atd_write_string(self.message)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "MatchExtra":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class Location:
    """Original type: location = { ... }"""

    path: str
    start: Position
    end: Position
    lines: List[str]

    @classmethod
    def from_json(cls, x: Any) -> "Location":
        if isinstance(x, dict):
            return cls(
                path=_atd_read_string(x["path"])
                if "path" in x
                else _atd_missing_json_field("Location", "path"),
                start=Position.from_json(x["start"])
                if "start" in x
                else _atd_missing_json_field("Location", "start"),
                end=Position.from_json(x["end"])
                if "end" in x
                else _atd_missing_json_field("Location", "end"),
                lines=_atd_read_list(_atd_read_string)(x["lines"])
                if "lines" in x
                else _atd_missing_json_field("Location", "lines"),
            )
        else:
            _atd_bad_json("Location", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["path"] = _atd_write_string(self.path)
        res["start"] = (lambda x: x.to_json())(self.start)
        res["end"] = (lambda x: x.to_json())(self.end)
        res["lines"] = _atd_write_list(_atd_write_string)(self.lines)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "Location":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class Match:
    """Original type: match_ = { ... }"""

    location: Location
    extra: MatchExtra
    rule_id: Optional[RuleId] = None

    @classmethod
    def from_json(cls, x: Any) -> "Match":
        if isinstance(x, dict):
            return cls(
                location=Location.from_json(x["location"])
                if "location" in x
                else _atd_missing_json_field("Match", "location"),
                extra=MatchExtra.from_json(x["extra"])
                if "extra" in x
                else _atd_missing_json_field("Match", "extra"),
                rule_id=RuleId.from_json(x["rule_id"]) if "rule_id" in x else None,
            )
        else:
            _atd_bad_json("Match", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["location"] = (lambda x: x.to_json())(self.location)
        res["extra"] = (lambda x: x.to_json())(self.extra)
        if self.rule_id is not None:
            res["rule_id"] = (lambda x: x.to_json())(self.rule_id)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "Match":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class Error:
    """Original type: error = { ... }"""

    error_type: str
    severity: Severity
    location: Location
    message: str
    rule_id: Optional[RuleId] = None
    details: Optional[str] = None
    yaml_path: Optional[List[str]] = None

    @classmethod
    def from_json(cls, x: Any) -> "Error":
        if isinstance(x, dict):
            return cls(
                error_type=_atd_read_string(x["error_type"])
                if "error_type" in x
                else _atd_missing_json_field("Error", "error_type"),
                severity=Severity.from_json(x["severity"])
                if "severity" in x
                else _atd_missing_json_field("Error", "severity"),
                location=Location.from_json(x["location"])
                if "location" in x
                else _atd_missing_json_field("Error", "location"),
                message=_atd_read_string(x["message"])
                if "message" in x
                else _atd_missing_json_field("Error", "message"),
                rule_id=RuleId.from_json(x["rule_id"]) if "rule_id" in x else None,
                details=_atd_read_string(x["details"]) if "details" in x else None,
                yaml_path=_atd_read_list(_atd_read_string)(x["yaml_path"])
                if "yaml_path" in x
                else None,
            )
        else:
            _atd_bad_json("Error", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["error_type"] = _atd_write_string(self.error_type)
        res["severity"] = (lambda x: x.to_json())(self.severity)
        res["location"] = (lambda x: x.to_json())(self.location)
        res["message"] = _atd_write_string(self.message)
        if self.rule_id is not None:
            res["rule_id"] = (lambda x: x.to_json())(self.rule_id)
        if self.details is not None:
            res["details"] = _atd_write_string(self.details)
        if self.yaml_path is not None:
            res["yaml_path"] = _atd_write_list(_atd_write_string)(self.yaml_path)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "Error":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class MatchResults:
    """Original type: match_results = { ... }"""

    matches: List[Match]
    errors: List[Error]
    skipped_targets: List[SkippedTarget]
    stats: Stats
    skipped_rules: Optional[List[SkippedRule]] = None
    time: Optional[Time] = None

    @classmethod
    def from_json(cls, x: Any) -> "MatchResults":
        if isinstance(x, dict):
            return cls(
                matches=_atd_read_list(Match.from_json)(x["matches"])
                if "matches" in x
                else _atd_missing_json_field("MatchResults", "matches"),
                errors=_atd_read_list(Error.from_json)(x["errors"])
                if "errors" in x
                else _atd_missing_json_field("MatchResults", "errors"),
                skipped_targets=_atd_read_list(SkippedTarget.from_json)(x["skipped"])
                if "skipped" in x
                else _atd_missing_json_field("MatchResults", "skipped"),
                stats=Stats.from_json(x["stats"])
                if "stats" in x
                else _atd_missing_json_field("MatchResults", "stats"),
                skipped_rules=_atd_read_list(SkippedRule.from_json)(x["skipped_rules"])
                if "skipped_rules" in x
                else None,
                time=Time.from_json(x["time"]) if "time" in x else None,
            )
        else:
            _atd_bad_json("MatchResults", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["matches"] = _atd_write_list(lambda x: x.to_json())(self.matches)
        res["errors"] = _atd_write_list(lambda x: x.to_json())(self.errors)
        res["skipped"] = _atd_write_list(lambda x: x.to_json())(self.skipped_targets)
        res["stats"] = (lambda x: x.to_json())(self.stats)
        if self.skipped_rules is not None:
            res["skipped_rules"] = _atd_write_list(lambda x: x.to_json())(
                self.skipped_rules
            )
        if self.time is not None:
            res["time"] = (lambda x: x.to_json())(self.time)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "MatchResults":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class CveResult:
    """Original type: cve_result = { ... }"""

    url: str
    filename: str
    funcnames: List[str]

    @classmethod
    def from_json(cls, x: Any) -> "CveResult":
        if isinstance(x, dict):
            return cls(
                url=_atd_read_string(x["url"])
                if "url" in x
                else _atd_missing_json_field("CveResult", "url"),
                filename=_atd_read_string(x["filename"])
                if "filename" in x
                else _atd_missing_json_field("CveResult", "filename"),
                funcnames=_atd_read_list(_atd_read_string)(x["funcnames"])
                if "funcnames" in x
                else _atd_missing_json_field("CveResult", "funcnames"),
            )
        else:
            _atd_bad_json("CveResult", x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res["url"] = _atd_write_string(self.url)
        res["filename"] = _atd_write_string(self.filename)
        res["funcnames"] = _atd_write_list(_atd_write_string)(self.funcnames)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> "CveResult":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class CveResults:
    """Original type: cve_results"""

    value: List[CveResult]

    @classmethod
    def from_json(cls, x: Any) -> "CveResults":
        return cls(_atd_read_list(CveResult.from_json)(x))

    def to_json(self) -> Any:
        return _atd_write_list(lambda x: x.to_json())(self.value)

    @classmethod
    def from_json_string(cls, x: str) -> "CveResults":
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)
