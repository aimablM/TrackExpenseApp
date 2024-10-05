import uuid
from hashlib import sha256
from datetime import datetime

def generate_unique_id():
        return str(uuid.uuid4())
def encrypt_password(password):
        return sha256(password.encode()).hexdigest()

def save_user(self):
        print(f"User {user.username} registered successfully!")
        
class user:
     
        
    def __init__(self, username, password, email, first_name, last_name, dob):
        self.user_id = generate_unique_id()
        self.username = username
        self.password = encrypt_password(password)
        self.email = email 
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.registration_date = datetime.now()
        self.profile_picture_url = None
        self.expense = []
        self.budget = None

        save_user(self) 

    def register(self, username, password, email, first_name, last_name, dob):
        # Logic to save user details to database
        self.username = username
        self.password = encrypt_password(password)
        self.email = email 
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        pass

   

   

    def login(self, username, password):
        try:
         if(self.username == username and self.password == encrypt_password(password)):
            print("Login Successful!")
            return True
         else:
            raise ValueError("Login failed. Please check your username and password.")
            return False
        except Exception as e:
            print(f"Login failed: {e}")
            return False
            