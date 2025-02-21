from django.shortcuts import render
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
     # Load dataset
    dataset_path = os.path.join(settings.BASE_DIR, 'data', 'house_price_dataset.csv')

    
    data = pd.read_csv(dataset_path)
        

    
    # Encode categorical 'Location' column
    label_encoder = LabelEncoder()
    data["Location"] = label_encoder.fit_transform(data["Location"])
    
    # Select features and target variable
    x = data[['SquareFeet', 'Bedrooms', 'Bathrooms', 'Location']]
    y = data['Price ($)']
    
    # Split dataset into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    
    # Initialize and train the model
    model = LinearRegression()
    model.fit(x_train, y_train)
    
    # Get input values from request and ensure proper type
    var1 = float(request.GET.get('n1', 0))  # SquareFeet
    var2 = float(request.GET.get('n2', 0))  # Bedrooms
    var3 = float(request.GET.get('n3', 0))  # Bathrooms
    var4 = request.GET.get('n4', '')  # Location (Categorical)
    
    # Convert location input to encoded value
    if var4 in label_encoder.classes_:
        var4 = label_encoder.transform([var4])[0]
    else:
        var4 = -1  # Default value if location not in training data
    
    # Ensure input is 2D for model.predict()
    input_data = np.array([[var1, var2, var3, var4]])
    pred = model.predict(input_data)
    pred = round(pred[0])
    
    # Send result to the template
    price = f"The predicted price is ${pred}"
    return render(request, 'predict.html', {"result2": price})
