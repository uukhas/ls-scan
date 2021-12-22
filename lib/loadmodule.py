from importlib.util import spec_from_file_location, module_from_spec

def load_module(module_name, file_name):
    spec = spec_from_file_location(module_name, file_name)
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, module_name)
