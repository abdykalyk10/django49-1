import datetime
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from . import models, forms

# book_list
def book_list_view(request):
    if request.method == "GET":
        query = models.BookModel.objects.all().order_by('-id')
        comtext_object_name = {
            'book':query
        }
        return render(request, template_name='book.html',
                      context=comtext_object_name)


#book detail
def book_detail_view(request, id):
    if request.method == "GET":
        form = forms.ReviwForm()
        query = get_object_or_404(models.BookModel, id=id)
        context_object_name = {
            'book_id':query,
            'form':form
        }
        return render(request, template_name='book_detail.html',
                      context=context_object_name)
    elif request.method == "POST":
        form = forms.ReviwForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.choice_book = get_object_or_404(models.BookModel, id=id)
            review.save()
            return redirect ('book_detail', id=id)
        else:
            return HttpResponse("Форма не валидна")





def about_me(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Абдыкалык <br> Мне 19 лет")


def text_and_photo(request):
    if request.method == "GET":
        return HttpResponse(
            "<h1>Море по ночьным небом</h1><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBF__6AaGPAMd4ha0VpqmSxwf8_XM6N_wWvQ&s'>")


def system_time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f"Текущее время: {current_time}")
