from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def make_model(radius, texture, perimeter, area, smoothness, compactness,concavity, concave_points, symmetry, fractal_dimension):
    print("Hello")
    df = pd.read_csv('cancerpredictor\data.csv')
    Y = df['diagnosis']
    df = df.drop(columns=['id','diagnosis'])
    X = df[['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean','concave points_mean','symmetry_mean','fractal_dimension_mean']].values
    model = DecisionTreeClassifier()
    model.fit(X, Y)
    return model.predict([[float(radius), float(texture), float(perimeter), float(area), float(smoothness), float(compactness),float(concavity), float(concave_points), float(symmetry), float(fractal_dimension)]])


def hello(request):
    if not auth.SESSION_KEY in request.session:
        return redirect('login')
    return render(request, 'cancerpredictor/home.html')

def predict(request):
    if not auth.SESSION_KEY in request.session:
        return redirect('login')
    return render(request, 'cancerpredictor/prediction.html')

@csrf_exempt
def predict_web(request):
    if not auth.SESSION_KEY in request.session:
        return redirect('login')
    if request.method == 'POST':
        data = json.loads(request.body)
        username0 = data['username']
        radius = data['radius']
        texture = data['texture']
        perimeter = data['perimeter']
        area = data['area']
        smoothness = data['smoothness']
        compactness = data['compactness']
        concavity = data['concavity']
        concave_points = data['concave_points']
        symmetry = data['symmetry']
        fractal_dimension = data['fractal_dimension']
        res0 = make_model(radius, texture, perimeter, area, smoothness, compactness,concavity, concave_points, symmetry, fractal_dimension)
        user0 = User.objects.get(username=username0)
        np = PatientData(user=user0,res=res0[0])
        np.save()
        if res0[0] == 'M':
            return JsonResponse({"res":"Malignant Breast Cancer Detected","label": "true"}, safe=False)
        else:
            return JsonResponse({"res":"Benign Breast Cancer Detected", "label": "false"}, safe=False)
        
        

def contactus(request):
    if not auth.SESSION_KEY in request.session:
        return redirect('login')
    if request.method == "POST":
        name = request.POST['username']
        mess = request.POST['message']
        try:
            user0 = User.objects.get(username=name)
            new_message = Message.objects.create(user=user0, message=mess)
            new_message.save()
            messages.success(request, "Sent Successfully")
            return render(request, 'cancerpredictor/contactus.html')
        except:
            messages.error(request, "Internal Server Error")
            return render(request, 'cancerpredictor/contactus.html')
    return render(request, 'cancerpredictor/contactus.html')

def aboutus(request):
    if not auth.SESSION_KEY in request.session:
        return redirect('login')
    return render(request, 'cancerpredictor/aboutus.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, 'cancerpredictor/login.html')
    return render(request, "cancerpredictor/login.html")

def signup(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(username = username)
            messages.error(request, "Username already taken")
            return render(request, "cancerpredictor/signup.html", {
                "formValues": {
                    "firstName": firstName,
                    "lastName": lastName,
                    "email": email,
                }
            })
        except User.DoesNotExist:
            pass
        try:
            User.objects.get(email = email)
            messages.error(request, "Email already in use")
            return render(request, "cancerpredictor/signup.html", {
                "formValues": {
                    "firstName": firstName,
                    "lastName": lastName,
                    "username": username,
                }
            })
        except User.DoesNotExist:
            pass
        user = User.objects.create_user(username, email, password, first_name = firstName, last_name = lastName)
        user.save()
        messages.success(request, "Successfully Signed Up, Please Login")
        return redirect('login')
    return render(request, "cancerpredictor/signup.html",{
        "formValues": {}
    })

def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('login')