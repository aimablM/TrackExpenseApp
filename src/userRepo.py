from databaseConnection import DatabaseConnection
from user import User
from user import encrypt_password


class UserRepo:

    def __init__(self, database_name):
        self.db = DatabaseConnection.get_instance(database_name)
        self.cursor = self.db.cursor
        self.connetion = self.db.connection
        self.current_user = None

    def authenticateUser(self, username, password):

        encrypted_password = encrypt_password(password)
        self.cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, encrypted_password),
        )
        record = self.cursor.fetchone()
        if record:
            user = User(
                record[1],
                record[2],
                record[3],
                record[4],
                record[5],
                record[6],
            )
            return user
        else:
            return None

    def addUser(self, user: User):
        self.cursor.execute(
            "INSERT INTO users (user_id, username, password, email, first_name, last_name, dob, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                user.user_id,
                user.username,
                user.password,
                user.email,
                user.first_name,
                user.last_name,
                user.dob,
                user.registration_date,
            ),
        )
        self.db.connection.commit()

    def removeUser(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        self.db.connection.commit()

    def editUser(self, user):
        self.cursor.execute(
            "UPDATE users SET username = ?, password = ?, email = ?, first_name = ?, last_name = ?, dob = ? WHERE user_id = ?",
            (
                user.username,
                user.password,
                user.email,
                user.first_name,
                user.last_name,
                user.dob,
                user.user_id,
            ),
        )

    def getUser(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return self.cursor.fetchone()

    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def __del__(self):
        self.db.disconnect()


if __name__ == "__main__":

    userRepo = UserRepo("expense_tracker.db")
    print(userRepo.getAllUsers())
    user1 = User(
        username="john_doe",
        password="securepassword123",
        email="john_doe",
        first_name="John",
        last_name="Doe",
        dob="1990-01-01",
    )
    userRepo.addUser(user1)
    print(userRepo.getAllUsers())
    # userRepo.__del__()
