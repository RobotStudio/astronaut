class InvalidRequestObject(object):
    def __init__(self):
        self.errors = []  # type: dict

    def add_error(self, param, msg):
        self.errors.append({'parameter': param, 'message': msg})

    def has_errors(self):
        return len(self.errors) > 0

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__


class ValidRequestObject(object):
    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__
