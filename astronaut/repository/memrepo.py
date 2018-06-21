from astronaut.domain import space


class MemRepo:
    def __init__(self, entries=None):
        self._entries = []  # type: list
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        if key in ['size', 'price']:
            return getattr(element[key], operator)(int(value))
        elif key in ['lattitude', 'longitude']:
            return getattr(element[key], operator)(float(value))

        return getattr(element[key], operator)(value)

    def list(self, filters=None):
        if not filters:
            return self._entries

        result = []  # type: list
        result.extend(self._entries)

        for key, val in filters.items():
            result = [e for e in result if self._check(e, key, val)]

        return [space.Space.from_dict(r) for r in result]
