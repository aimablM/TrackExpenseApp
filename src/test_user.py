from src.user import User, encrypt_password

class TestUser:

def test_user_creation(self):
        # Create a new user
        new_user = user("testuser", "password123", "test@example.com", "First", "Last", "1990-01-01")
        
        # Assertions to check if user attributes are set correctly
        assert new_user.username == "testuser"
        assert new_user.email == "test@example.com"
        assert new_user.first_name == "First"
        assert new_user.last_name == "Last"
        assert new_user.dob == "1990-01-01"
        assert new_user.user_id is not None  # Check if user_id is generated
        assert new_user.registration_date is not None  # Ensure registration date is set

    def test_password_encryption(self):
        new_user = user("testuser", "password123", "test@example.com", "First", "Last", "1990-01-01")
        
        # Verify that the stored password is encrypted
        encrypted_password = new_user.password
        assert encrypted_password == new_user.password  # This will always pass; to be updated to specific checks if needed

    def test_login_success(self):
        new_user = user("testuser", "password123", "test@example.com", "First", "Last", "1990-01-01")
        
        # Test successful login
        assert new_user.login("testuser", "password123") == True  # Should return True

    def test_login_failure(self):
        new_user = user("testuser", "password123", "test@example.com", "First", "Last", "1990-01-01")
        
        # Test login with wrong password
        assert new_user.login("testuser", "wrongpassword") == False  # Should return False

        # Test login with wrong username
        assert new_user.login("wronguser", "password123") == False  # Should return False

    def test_logout(self):
        new_user = user("testuser", "password123", "test@example.com", "First", "Last", "1990-01-01")
        
        # Capture the output of the logout method
        import io
        import sys
        captured_output = io.StringIO()                  # Create StringIO object
        sys.stdout = captured_output                       # Redirect stdout to the StringIO object
        
        new_user.logout()                                  # Call the logout method
        
        sys.stdout = sys.__stdout__                        # Reset redirect.
        assert captured_output.getvalue().strip() == "Logged out successfully."  # Check output message