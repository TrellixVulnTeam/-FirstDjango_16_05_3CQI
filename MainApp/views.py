from django.shortcuts import render, HttpResponse, Http404

name = "Евгений"
surname = "Юрченко"
email = "eyurchenko@specialist.ru"
phone = "8-923-600-01-02"

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]


def about(request):
    context = {
        "name": "Евгений",
        "surname": "Юрченко",
        "phone": 79008001012,
        "email": [2, 5, "6", 7.6, 8]
    }
    return render(request, "about.html", context)


def home(request):
    return render(request, "index.html")


def item_page(request, id):
    for item in items:
        if item["id"] == id:
            return render(request, "item_page.html", item)

    raise Http404(f"Товар c id={id} не найден")


def items_list(request):
    context = {
        "items": items
    }
    return render(request, "items.html", context)