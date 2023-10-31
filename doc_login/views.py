from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import JsonResponse
from redis import Redis
from doc_login.models import *
from order_sys import settings
import random, jwt


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"] + "@htbi.com.tw"
        code = send_email_msg(email=email)
        redis = Redis(connection_pool=settings.CACHES["default"]["LOCATION"])
        redis.setex(f"email:{email}", 600, code)
        request.session["code"] = code
        data = {
            "code": code,
        }
        return JsonResponse(data)
    else:
        return render(request, "login.html")


def verify_code_view(request):
    if request.method == "POST":
        code = request.POST["code"]
        redis = Redis(connection_pool=settings.CACHES["default"]["LOCATION"])
        value = redis.get(f"email:{request.email}")
        if value is None:
            return render(request, "login.html", {"error": "驗證碼已過期"})
        elif code == value.decode("utf-8"):
            request.session["csrf_token"] = get_token(request)
            return redirect(request.META["HTTP_REFERER"])
        else:
            return render(request, "login.html", {"error": "驗證碼錯誤"})
    else:
        return render(request, "login.html")


def generate_code():
    return random.randint(0, 999999)


def get_token(request):
    user = request.POST["user"]
    return jwt.encode({"user_id": user}, settings.SECRET_KEY, algorithm="HS256")


def send_email_msg(email):
    rand_str = f"{generate_code():06d}"
    message = "您的驗證碼是" + rand_str + "，10分鐘內有效，請盡快填寫"
    emailBox = []
    emailBox.append(email)
    send_mail("驗證碼", message, "ernielin@htbi.com.tw", emailBox, fail_silently=False)
    return rand_str
