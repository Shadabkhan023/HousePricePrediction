"""
ASGI config for web_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import pandas as pd

# Get the directory where the current script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the dataset
dataset_path = os.path.join(base_dir, 'data', 'house_price_dataset.csv')

# Load the dataset
df = pd.read_csv(dataset_path)


from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

application = get_asgi_application()
