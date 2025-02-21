"""
ASGI config for web_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import pandas as pd

# Determine the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the dataset
dataset_path = os.path.join(base_dir, 'data', 'house_price_dataset.csv')

# Load the dataset
try:
    data = pd.read_csv(dataset_path)
except FileNotFoundError:
    print(f"Error: The file {dataset_path} does not exist.")



from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

application = get_asgi_application()
