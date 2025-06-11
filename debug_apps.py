import os
import django
from pathlib import Path

# Set Django settings module for script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolhub.settings')

# Initialize Django
django.setup()

# This will print all installed apps as Django sees them
from django.apps import apps
print("Installed apps as seen by Django:")
for app in apps.get_app_configs():
    print(f" - {app.name} ({app.label})")

# Print settings.INSTALLED_APPS
from django.conf import settings
print("\nINSTALLED_APPS from settings:")
for app in settings.INSTALLED_APPS:
    print(f" - {app}")

# Print paths Django is looking at
print("\nPython paths:")
import sys
for path in sys.path:
    print(f" - {path}")

# Check the physical path of the apps
base_dir = Path(__file__).resolve().parent
print(f"\nBase directory: {base_dir}")
print("\nExisting app directories:")
for app_name in ['chat', 'students', 'teachers', 'announcements']:
    app_path = base_dir / app_name
    exists = app_path.exists()
    print(f" - {app_name}: {app_path} (exists: {exists})")
