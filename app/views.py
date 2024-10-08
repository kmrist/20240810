from django.shortcuts import render, redirect

from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def index(request):
    return render(request, "index.html")


def tab1(request):
    return render(request, "tab1.html")


def tab2(request):
    return render(request, "tab2.html")


def tab3(request):
    return render(request, "tab3.html")


# from django.shortcuts import render
from .models import Location


def tab1(request):
    locations = Location.objects.all()  # データベースからすべての情報を取得
    return render(request, "tab1.html", {"locations": locations})


def register_data(request):
    if request.method == "POST":
        try:
            location = Location(
                prefecture=request.POST["prefecture"],
                city_district=request.POST["city_district"],
                title=request.POST["title"],
                date=request.POST["date"],
                image=request.FILES["image"],
                description=request.POST["description"],
                external_url=request.POST["external_url"],
            )
            location.save()
            return redirect("index")  # 登録後にインデックスページにリダイレクト
        except MultiValueDictKeyError as e:
            print(f"Error: {e}")
            # エラーメッセージを表示するために、タブ1のテンプレートを再表示
            return render(request, "tab1.html", {"error": "必要な情報が不足しています。"})
    else:
        return redirect("index")  # GETリクエストの場合はインデックスページにリダイレクト
