class Map(dict):
    """
    Mapper for common syntax use of dictionaries

    Args:
        *args (dict|Any): A dictionary of values that the object is initialized with. There can be multiple objects for concatenation.

        **kwargs (Any): Any named keyword argument to initialize the object with. Comes after the `args` param.

    Example:
        `m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])`
    """

    def __init__(self, *args, **kwargs):
        """Initializer"""
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        """Get attribute"""
        return self.get(attr)

    def __setattr__(self, key, value):
        """Set attribute"""
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        """Set key on Map object"""
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        """Delete attribute"""
        self.__delitem__(item)

    def __delitem__(self, key):
        """Delete key on Map object"""
        super(Map, self).__delitem__(key)
        del self.__dict__[key]
