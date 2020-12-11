from django.shortcuts import render


def main(request):
    return render(request, 'App_Customer/customer_login.html')