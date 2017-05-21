class ProjectErrors(Exception):
    pass

class ProjectNotFoundError(ProjectErrors):
    def __init__(self):
        super(ProjectNotFoundError, self).__init__("Project not found")

class ProjectAddError(ProjectErrors):
    def __init__(self):
        super(ProjectAddError, self).__init__("Project add error")

