import collections


class InvalidRequestObject(object):
    def __init__(self):
        self.errors = []  # type: dict

    def add_error(self, param, msg):
        self.errors.append({'parameter': param, 'message': msg})

    def has_errors(self):
        return bool(self.errors)


class ValidRequestObject(object):
    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class SpaceListRequestObject(object):
    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and \
                not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return SpaceListRequestObject(filters=adict.get('filters', None))
