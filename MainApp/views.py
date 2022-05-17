from django.shortcuts import render, HttpResponse

name = "Евгений"
surname = "Юрченко"
email = "eyurchenko@specialist.ru"


def about(request):
    info = f""" <div>Имя: <b>{name}</b> </div>
                Фамилия: <b>{surname}</b> <br>
                телефон: <b>8-923-600-01-02</b> <br>
                email: <b>{email}</b>"""
    return HttpResponse(info)


def home(request):
    text = f"""<h1> "Изучаем django" </h1>
    <strong> Автор </strong>: <i> {surname} Е.В. </i>"""
    return HttpResponse(text)
