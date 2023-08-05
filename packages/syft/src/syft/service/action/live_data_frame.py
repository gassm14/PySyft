# stdlib
from typing import Any
from typing import ClassVar
from typing import Type

# third party
from pandas import DataFrame

# relative
from ...serde.serializable import serializable
from ...types.syft_object import SYFT_OBJECT_VERSION_1
from .action_object import ActionObject
from .action_object import BASE_PASSTHROUGH_ATTRS
from .action_types import action_types


@serializable(attrs=["db_args", "df"])
class LiveDataFrame:
    def __init__(self, host=None, port=None, user=None, password=None, db=None, table=None, db_type=None):
        db_args = {"host": host, "port": port, "user": user, "password": password, "db": db, "table": table,
                   "db_type": db_type}
        self.db_args = None
        if None not in db_args.values():
            self.db_args = db_args
        self.df = DataFrame()

    def estimated_size(self):
        return self.df.memory_usage().nbytes

    def __len__(self):
        return len(self.df)

    def __getattribute__(self, name):
        if name in ["__class__", "estimated_size", "df", "db_args"]:
            return object.__getattribute__(self, name)
        return self.df.__getattribute__(name)

    def __getitem__(self, key):
        return self.df[key]

    def __copy__(self):
        if self.db_args is not None:
            return LiveDataFrame(**self.db_args.values())
        else:
            copy = LiveDataFrame()
            copy.df = self.df
            return copy


@serializable()
class LiveDataFrameObject(ActionObject):
    __canonical_name__ = "LiveDataFrameObject"
    __version__ = SYFT_OBJECT_VERSION_1

    syft_internal_type: ClassVar[Type[Any]] = LiveDataFrame
    syft_passthrough_attrs = BASE_PASSTHROUGH_ATTRS

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def syft_get_property(self, obj: Any, method: str) -> Any:
        return getattr(self.syft_action_data, method)

    def syft_is_property(self, obj: Any, method: str) -> bool:
        cols = self.syft_action_data.columns.values.tolist()
        if method in cols:
            return True
        return super().syft_is_property(obj, method)


action_types[LiveDataFrame] = LiveDataFrameObject
