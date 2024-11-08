from database import Database

class User:
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email
        self.age = age
        
class UserSrvice:
    def __init__(self, db_name = "user.db"):
        self.db = Database(db_name)
        
    def add_user(self, user):
        if self.find_user_by_email(user.email):
            print("Пользователь с такеим емаил уже существует")
            return
        self.db.add_user(user)
        
        print("Пользователь успешно добавлен")
        
    def find_user_by_email(self, email):
        user_data = self.db.get_user(email)
        if user_data:
            return User(name=user_data[1], email=user_data[2], age=user_data[3])
        else:
            print("Не найдено!")
            
    def close(self):
        self.db.close()       
    
            
# user - UserSrvice()

# user = User(name="isko", email="adv1218@gmail.com", age=20)
# User.add_user(user)