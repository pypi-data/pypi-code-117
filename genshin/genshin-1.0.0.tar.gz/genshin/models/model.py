"""Modified pydantic model."""
from __future__ import annotations

import abc
import datetime
import typing

import pydantic

__all__ = ["APIModel", "Aliased", "Unique"]

_SENTINEL = object()


def _get_init_fields(cls: typing.Type[APIModel]) -> typing.Tuple[typing.Set[str], typing.Set[str]]:
    api_init_fields: typing.Set[str] = set()
    model_init_fields: typing.Set[str] = set()

    for name, field in cls.__fields__.items():
        alias = field.field_info.extra.get("galias")
        if alias:
            api_init_fields.add(alias)
            model_init_fields.add(name)

    for name in dir(cls):
        obj = getattr(cls, name, None)
        if isinstance(obj, property):
            model_init_fields.add(name)

    return api_init_fields, model_init_fields


class APIModel(pydantic.BaseModel, abc.ABC):
    """Modified pydantic model."""

    __api_init_fields__: typing.ClassVar[typing.Set[str]]
    __model_init_fields__: typing.ClassVar[typing.Set[str]]

    # nasty pydantic bug fixed only on the master branch - waiting for pypi release
    if typing.TYPE_CHECKING:
        _mi18n: typing.ClassVar[typing.Dict[str, typing.Dict[str, str]]]
    else:
        _mi18n = {}

    def __init__(self, **data: typing.Any) -> None:
        """"""
        # clear the docstring for pdoc
        super().__init__(**data)

    def __init_subclass__(cls) -> None:
        cls.__api_init_fields__, cls.__model_init_fields__ = _get_init_fields(cls)

    @pydantic.root_validator(pre=True)
    def __parse_galias(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        """Due to alias being reserved for actual aliases we use a custom alias."""
        if cls.__model_init_fields__:
            # has all model init fields
            if cls.__model_init_fields__.issubset(set(values)):
                return values

            # has some model init fields but no api init fields
            if set(values) & cls.__model_init_fields__ and not set(values) & cls.__api_init_fields__:
                return values

        aliases: typing.Dict[str, str] = {}
        for name, field in cls.__fields__.items():
            alias = field.field_info.extra.get("galias")
            if alias is not None:
                aliases[alias] = name

        return {aliases.get(name, name): value for name, value in values.items()}

    @pydantic.root_validator()
    def __parse_timezones(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        """Timezones are a pain to deal with so we at least allow a plain hour offset."""
        for name, field in cls.__fields__.items():
            if isinstance(values.get(name), datetime.datetime) and values[name].tzinfo is None:
                timezone = field.field_info.extra.get("timezone", 0)
                if not isinstance(timezone, datetime.timezone):
                    timezone = datetime.timezone(datetime.timedelta(hours=timezone))

                values[name] = values[name].replace(tzinfo=timezone)

        return values

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        """Generate a dictionary representation of the model.

        Takes the liberty of also giving properties as fields.
        """
        for name in dir(type(self)):
            obj = getattr(type(self), name)
            if isinstance(obj, property):
                value = getattr(self, name, _SENTINEL)

                if name[0] == "_" or value is _SENTINEL or value == "":
                    continue

                self.__dict__[name] = value

        return super().dict(**kwargs)

    def _get_mi18n(
        self,
        field: typing.Union[pydantic.fields.ModelField, str],
        lang: str,
        *,
        default: typing.Optional[str] = None,
    ) -> str:
        """Get localized name of a field."""
        if isinstance(field, str):
            key = field.lower()
            default = default or key
        else:
            if not field.field_info.extra.get("mi18n"):
                raise TypeError(f"{field!r} does not have mi18n.")

            key = field.field_info.extra["mi18n"]
            default = default or field.name

        if key not in self._mi18n:
            return default

        if lang not in self._mi18n[key]:
            raise TypeError(f"mi18n not loaded for {lang}")

        return self._mi18n[key][lang]

    if not typing.TYPE_CHECKING:

        class Config:
            allow_mutation = False


class Unique(abc.ABC):
    """A hashable model with an id."""

    id: int

    def __int__(self) -> int:
        return self.id

    def __hash__(self) -> int:
        return hash(self.id)


def Aliased(
    galias: typing.Optional[str] = None,
    default: typing.Any = pydantic.main.Undefined,  # type: ignore
    *,
    timezone: typing.Optional[typing.Union[int, datetime.datetime]] = None,
    mi18n: typing.Optional[str] = None,
    **kwargs: typing.Any,
) -> typing.Any:
    """Create an aliased field."""
    if galias is not None:
        kwargs.update(galias=galias)
    if timezone is not None:
        kwargs.update(timezone=timezone)
    if mi18n is not None:
        kwargs.update(mi18n=mi18n)

    return pydantic.Field(default, **kwargs)
