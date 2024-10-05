# test_user.py

from src.user import User, encrypt_password  # Adjust this import based on your project structure

def test_user_creation():
    new_user = User(
        "testuser",
        "password123",
        "test@example.com",
        "Test",
        "User",
        "2000-01-01"
    )
    assert new_user.username == "testuser"
    assert new_user.email == "test@example.com"
    assert new_user.password == encrypt_password("password123")
    print("User creation test passed.")

def test_user_login_success():
    new_user = User(
        "testuser",
        "password123",
        "test@example.com",
        "Test",
        "User",
        "2000-01-01"
    )
    assert new_user.login("testuser", "password123") == True
    print("User login success test passed.")

def test_user_login_failure():
    new_user = User(
        "testuser",
        "password123",
        "test@example.com",
        "Test",
        "User",
        "2000-01-01"
    )
    assert new_user.login("testuser", "wrongpassword") == False
    print("User login failure test passed.")

if __name__ == "__main__":
    test_user_creation()
    test_user_login_success()
    test_user_login_failure()
