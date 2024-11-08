import sqlite3

class Database:
    def __init__(self, db_name='users.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS user(
                   id INTEGER PRIMARY KEY AUTOINCRLEMENT
                   name VACHAR (40) NOT NOY NULL,
                   email TEXT UNIQUE NOT NULL,
                   age INTEGER
                )             
        """)
        self.connection.commit()
        
    def add_user(self,user):
        self.cursor.execute("INSERT INTO user (name,email,age) VALUES (?,?,?)", (user.name , user.email, user.age))
        
        self.connection.commit()
        
    def get_user(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,)) 
        return self.cursor.fetchone() 
    
    def close(self):
        self.connection.close()    