from django.shortcuts import render, HttpResponse

name = "Евгений"
surname = "Юрченко"


def about(request):
    info = f"<h1>Автор: <i>{name} {surname}</i></h1>"
    return HttpResponse(info)


def home(request):
    return HttpResponse("Hello")
