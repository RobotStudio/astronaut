from astronaut.shared import response_object as ro


class SpaceListUseCase(object):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object):
        space = self.repo.list()
        return ro.ResponseSuccess(space)
