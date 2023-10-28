import db
import pass_handling

class User:
    def __init__(self, username="", password="", salt="", id = -1):
        self._id = id
        self.username = username
        self._hashed_password = pass_handling.hash_password(password, salt)

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt=""):
        self._hashed_password = pass_handling.hash_password(password, salt)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)

    def load_user_by_username(self,cursor):

        query = f"SELECT * FROM users WHERE username = '{self.username}';"
        print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            self._id, self.username, self.hashed_password = row
            print("User loaded")
        else:
            print("User not exist")


    def load_user_by_id(self,cursor):

        query = f"SELECT * FROM users WHERE id = '{self._id}';"
        print(query)
        cursor.execute(query)
        row = cursor.fetchone()  # check if user exist
        if row is not None:
            self._id, self.username, self.hashed_password = row
            print("User loaded")
        else:
            print("User not exist")


    def load_all_users(self,cursor):

        query = f"SELECT * FROM users;"
        cursor.execute(query)
        for row in cursor:
            print(f"ID:{row[0]}, username:{row[1]}")

    def delete(self,cursor):

        query = f"SELECT * FROM users WHERE id = '{self._id}';"
        cursor.execute(query)
        row = cursor.fetchone()  # check if user exist
        if row is not None:
            ans = input(f"DO YOU WANT TO DELETE {self.username}? Y/N ")
            if ans == "Y":
                query = f"DELETE FROM users WHERE id = '{self._id}' RETURNING id;"
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    print(f"User {self.username} deleted")
                    self._id = -1

    def save_to_database(self,cursor):

            query = f"SELECT * FROM users WHERE id = {self._id};"
            cursor.execute(query)
            row = cursor.fetchone()  # check if user exist
            if row is not None:
                query = f"UPDATE users SET username = '{self.username}', hashed_password = '{self._hashed_password}' WHERE id = {self._id};"
                cursor.execute(query)
                print(f"Database updated")
            else:
                query = f"INSERT INTO users (username,hashed_password) VALUES ('{self.username}', '{self._hashed_password}') RETURNING id;"
                cursor.execute(query)
                self._id = cursor.fetchone()[0]
                print(f"User created, id: {self._id}")

class Message:
    def __init__(self):
        self._id = -1
        self.from_id = 10
        self.to_id = 2
        self.creation_date = None
        self.text = " "

    @property
    def id(self):
        return self._id

    def send_to_database(self,cursor):
            query = f"SELECT * FROM messages WHERE id = {self._id};"
            cursor.execute(query)
            row = cursor.fetchone()  # check if mess exist
            if row is not None:
                print(f"Error - message id exist")
            else:
                query = f"INSERT INTO messages (from_id,to_id,text) VALUES ('{self.from_id}', '{self.to_id}', '{self.text}') RETURNING creation_date;"
                cursor.execute(query)
                self.creation_date = cursor.fetchone()[0]
                print(f"Message send at {self.creation_date}")

    def load_all_messages(self,cursor):

        query = f"SELECT * FROM messages;"
        cursor.execute(query)
        for row in cursor:
            print(f"From:{row[1]}, to: {row[2]} || {row[4]} at {row[3]}")
cursor = db.cursor

mess = Message()
mess.send_to_database(cursor)
mess.load_all_messages(cursor)



