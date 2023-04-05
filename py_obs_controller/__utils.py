def get_attributes_as_dict(obj):
    """ Returns a dictionary of all attributes of an object."""
    return {attr: getattr(obj, attr) for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")}