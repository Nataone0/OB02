class User:
    def __init__(self, id, name, level="user"):
        self._id = id  # Используем защищенный атрибут
        self._name = name  # Защищенный атрибут
        self._level = level  # Защищенный атрибут

    # Методы для доступа к атрибутам
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name

    def set_level(self, level):
        if level in ["user", "admin"]:
            self._level = level
        else:
            raise ValueError("The level must be 'user' or 'admin'.")


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name, level="admin")
        self._users = {}  # Словарь для хранения пользователей

    def add_user(self, user):
        if user.get_id() not in self._users:
            self._users[user.get_id()] = user
        else:
            print(f"User with ID {user.get_id()} already exists.")

    def remove_user(self, user_id):
        if user_id in self._users:
            del self._users[user_id]
        else:
            print(f"User with ID {user_id} not found.")

    # Метод для вывода списка пользователей (для удобства)
    def list_users(self):
        for user_id, user in self._users.items():
            print(f"ID: {user_id}, Name: {user.get_name()}, Level: {user.get_level()}")


admin = Admin(1, "John")
user1 = User(2, "Alice")
user2 = User(3, "Bob")
user3 = User(4, "Eve")
user4 = User(5, "Dave")
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)
admin.list_users()
admin.remove_user(2)
admin.remove_user(2)
admin.list_users()