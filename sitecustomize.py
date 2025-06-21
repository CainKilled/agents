import sys

try:
    import pydantic
except Exception:
    pydantic = None

if pydantic is not None:
    # Provide pydantic v2 compatibility shims if missing
    if not hasattr(pydantic, "TypeAdapter"):
        from pydantic import parse_obj_as

        class TypeAdapter:
            def __init__(self, typ):
                self.typ = typ

            def validate_python(self, obj):
                return parse_obj_as(self.typ, obj)

            def json_schema(self, *a, **kw):
                return {}

        pydantic.TypeAdapter = TypeAdapter

    if not hasattr(pydantic, "ConfigDict"):
        class ConfigDict(dict):
            pass

        pydantic.ConfigDict = ConfigDict

    if not hasattr(pydantic, "model_validator"):
        def model_validator(*args, **kwargs):
            def wrapper(fn):
                return fn

            return wrapper

        pydantic.model_validator = model_validator

    # Support `model_config` attribute for BaseModel on pydantic v1
    if hasattr(pydantic, "BaseModel") and not hasattr(pydantic.BaseModel, "model_config"):
        BaseModel = pydantic.BaseModel
        _orig_init_subclass = BaseModel.__init_subclass__

        def _init_subclass(cls, **kw):
            _orig_init_subclass(**kw)
            cfg = getattr(cls, "model_config", None)
            if isinstance(cfg, dict):
                class Config:
                    arbitrary_types_allowed = cfg.get("arbitrary_types_allowed", False)

                cls.Config = Config

        BaseModel.__init_subclass__ = classmethod(_init_subclass)

