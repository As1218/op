from lesson_3 import UserSrvice, User


user = UserSrvice()

user_service = User(name="isko", email="isko1@gmail.com", age=20)

user.add_user(user_service)

find = user.find_user_by_email("isko1@gmail.com")
if find:
    print(f"Пользователь найден: {find.name}, {find.email}, {find.age}")