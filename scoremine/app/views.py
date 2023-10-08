from django.shortcuts import render, redirect
from app.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def encode_string(input_str):
    encoded = []
    for char in input_str:
        ascii_value = ord(char)
        encoded.append(str(ascii_value))
    return '@'.join(encoded)

def decode_string(encoded_str):
    encoded_values = encoded_str.split("@")
    decoded = ''.join([chr(int(value)) for value in encoded_values])
    return decoded



def send_email(to_address, from_address, message, subject):
    try:
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = from_address
        msg["To"] = to_address
        body = MIMEText(message)
        msg.attach(body)

        smtp = smtplib.SMTP("smtp-relay.sendinblue.com", 587)
        smtp.starttls()  # Enable TLS encryption
        smtp.login("srameshbabu2004@gmail.com", "cUYEqWHFI8QyOSVT")
        smtp.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        print(e, "Ramesh")
        return False


def index(request):
    return render(request, "index.html")

def login_(request):
    return render(request, "login&reg.html")

def register_request(request):
    if request.method == "POST":
        username = request.POST['user']
        email = request.POST['email']
        pass1 = request.POST['passwd1']
        pass2 = request.POST['passwd2']
        
        if User.objects.filter(username=username):
            x = "Username already exist!"
            print(1)
            return render(request,'login&reg.html', {'x':x})
        
        if User.objects.filter(email=email).exists():
            x = "Email Already Registered!!"
            print(2)
            return render(request,'login&reg.html', {'x':x})
        
        if len(username)>20:
            x = "Username must be under 20 chars"
            print(3)
            return render(request,'login&reg.html', {'x':x})
        
        if pass1 != pass2:
            x = "Passwords didn't matched"
            print(4)
            return render(request,'login&reg.html', {'x':x})
        
        if not username.isalnum():
            x = "Username must be Alpha-Numeric"
            print(5)
            return render(request,'login&reg.html', {'x':x})
        
        x = "Please check your mail"
        
        newPass =encode_string(pass1)
        to_address = email
        from_address = "newUserReg@scoremine.in"
        subject = "Welcome to Scoremine Login!!"
        message = "Hello " + username + "!! \n" + "Welcome to Scoremine!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nRamesh Babu"        
        

        send_email(to_address, from_address, message, subject)
        
        subject = "Confirm your Email Scoremine Login!!"
        message = "Hello " + username + "Click on this link to confirm your account" + "\n" + "http://127.0.0.1:8000/activate/" + username+ "/" + email + "/" + newPass
        send_email(to_address, from_address, message, subject)
        return render(request,'login&reg.html', {'x':x})
        

def activate(request,username,email, pass1):
    print(username, email, pass1)
    newPass =decode_string(pass1)
    myuser = User.objects.create_user(username=username, email=email, password=newPass)
    myuser.save()
    print(myuser)
    x = "Your Account has been activated"
    return render(request,'login&reg.html', {'x':x})

def login_request(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['passwd']
        try:
            user = User.objects.get(username=username) 
        except:
            x = "bad credentials"
            return render(request, 'login&reg.html', {'x': x})
        print(user) 

        if user is not None and user.check_password(password):
            login(request, user)
            return render(request, "index.html", {"username": username})
        else:
            x = "Bad Credentials!!"
            print(x)
            return render(request, 'login&reg.html', {'x': x})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("app:index")

