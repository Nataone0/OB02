class User:
    def __init__(self, id, name, level="user"):
        self.id = id
        self.name = name
        self.level = level


class Admin(User):
    def __init__(self, id, name, level="admin"):
        super().__init__(id, name, level)