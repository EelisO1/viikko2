from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user
    
    def contains_letters_and_numbers(self, password):
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
        return bool(re.match(pattern, password))
    
    def valid_username_format(self, username):
        pattern = r'^[a-zA-Z]+$'
        return bool(re.match(pattern, username))

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if len(username) < 3:
            raise UserInputError("Username must contain atleast 3 characters")
        
        if len(password) < 8:
            raise UserInputError("Password must contain atleast 8 characters")
        
        if not self.contains_letters_and_numbers(password):
            raise UserInputError("Password must contain characters and numbers")
        
        if not self.valid_username_format(username):
            raise UserInputError("Username must only contain characters a-z")