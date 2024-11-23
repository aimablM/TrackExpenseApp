import sqlite3
from sqlite3 import Error


class DatabaseConnection:
    _instance = None

    # Singleton instance of connection because only one connection should exist

    # Private constructor (in Python we use double underscore)
    def __init__(self, db_name=None):
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def get_instance(cls, db_name=None):
        if cls._instance is None:
            if not db_name:
                raise ValueError("Database name must be provided")
            # Create new instance without calling __init__

            # Initialize instance attributes
            cls._instance = cls.__new__(cls)
            cls._instance.connection = None
            cls._instance.cursor = None
            cls._instance.db_name = db_name

            # Connect and initialize
            cls._instance.connect()
            cls._instance._initialize_database()

        else:
            if db_name and db_name != cls._instance.db_name:
                raise ValueError(
                    f"Database connection already exists for: {cls._instance.db_name}"
                )

        return cls._instance

    def connect(self):
        try:
            if self.connection:
                print("Connection already exists")
                return

            self.connection = sqlite3.connect(self.db_name)  # Connect to the database
            self.cursor = self.connection.cursor()
            print(f"Connected to: {self.db_name}")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def isConnected(self):
        if self.connection:
            return True

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
                self.cursor = None
                print(f"Disconnected from: {self.db_name}")
            else:
                print(f"No active connection to disconnect")
        except Error as e:
            print(f"Error disconnecting from database: {e}")

    def _initialize_database(self):
        try:
            # Define the database table for users if they do not exist
            create_tables = [
                """ CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            dob DATE,
            registration_date DATE)
            """,
                """ CREATE TABLE IF NOT EXISTS expenses (
                expense_id TEXT PRIMARY KEY,
                user_id TEXT,
                name TEXT NOT NULL,
                category TEXT,
                amount REAL NOT NULL,
                description TEXT,
                date TEXT,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
            """,
            ]

            for table in create_tables:
                self.cursor.execute(table)

            self.connection.commit()

        except Error as e:
            print(f"Error initializing database: {e}")

    def save(self):
        self.connection.commit()
