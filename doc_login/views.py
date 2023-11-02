from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import redirect_to_login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.utils.functional import wraps
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.cache import cache
from doc_login.models import *
from order_sys import settings
import random, jwt


def verify_required(login_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            token = request.COOKIES.get("cold_token", None)
            if token is not None:
                try:
                    email = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])['user_id']
                    state = cache.has_key(f"login:{email}")
                    if state:
                        return view_func(request, *args, **kwargs)
                except jwt.InvalidTokenError:
                    pass
            path = request.get_full_path()
            return redirect_to_login(path, login_url, "next")

        return _wrapped_view

    return decorator

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"] + "@htbi.com.tw"
        code = send_email_msg(email)
        cache.set(f"verify:{email}", code, 600)  # 10min
        request.session["code"] = code
        data = {
            "email": email,
        }
        return JsonResponse(data)
    else:
        return render(request, "login.html")


@csrf_exempt
def verify_code_view(request):
    if request.method == "POST":
        code = request.POST["code"]
        email = request.POST["email"]
        value = cache.get(f"verify:{email}")
        if value is None:
            return render(request, "login.html", {"error": "驗證碼已過期"})
        elif code == value:
            token = get_token(request)
            cache.set(f"login:{email}", "authenticated", 21600)  # 6hr
            next_url = request.GET.get('next', request.META["HTTP_REFERER"])
            response = redirect(next_url)
            response.set_cookie("cold_token", token)
            return response
        else:
            return render(request, "login.html", {"error": "驗證碼錯誤"})
    else:
        return render(request, "login.html")


def generate_code():
    return random.randint(0, 999999)


def get_token(request):
    user = request.POST["email"]
    return jwt.encode({"user_id": user}, settings.SECRET_KEY, algorithm="HS256")


def send_email_msg(email):
    rand_str = f"{generate_code():06d}"
    message = "您的驗證碼是" + rand_str + "，10分鐘內有效，請盡快填寫"
    emailBox = []
    emailBox.append(email)
    send_mail("驗證碼", message, "ernielin@htbi.com.tw", emailBox, fail_silently=False)
    return rand_str
