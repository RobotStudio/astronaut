class SpaceListRequestObject(object):

    @classmethod
    def from_dict(cls, adict):
        return SpaceListRequestObject()

    def __bool__(self):
        return True
