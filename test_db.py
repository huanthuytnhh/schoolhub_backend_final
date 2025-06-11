"""
Simple script to test database connection in Django
"""
import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolhub.settings')
django.setup()

# Now we can import Django components
from django.db import connections
from django.db.utils import OperationalError

# Try to connect to the database
try:
    connection = connections['default']
    connection.cursor()
    print("Database connection successful!")
    print(f"Using database: {connection.settings_dict['ENGINE']}")
    print(f"Database name: {connection.settings_dict['NAME']}")
except OperationalError as e:
    print(f"Error connecting to database: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
    print(f"Database settings: {connections.databases}")
