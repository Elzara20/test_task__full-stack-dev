import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
import yadisk
from .forms import AppForm
import re

def form(request): 
    """
    Обрабатывает запрос к странице формы. Форма содержит поле OAuth-токен и публичную ссылку public_key
    """
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data   
            token = cd['token'],
            public_key = cd['public_key']
          
            return redirect("view_file",  token=token[0], public_key=public_key)       
    else:
        context = {}
        context['form'] = AppForm
        return render(request, "form.html", context=context)


def view_file(request, token, public_key):
    """
    Обрабатывает запрос к странице со списком файлов и папок. На странице есть кнопка \"Cкачать\"
    """
    client = yadisk.Client(token=token)
    with client:
        # список файлов и папок
        items = client.listdir(public_key)  
    # токен также доступен в контексте для скачивания файлов
    return render(request, "view.html", {'token': token, 'items': items})  

def download_file(request):
    """
    Обрабатывает скачивание файла
    """
    if request.method == 'POST':
        
        token = request.POST.get('token')  # токен из POST-запроса
        file_path = request.POST.get('file_path')  # путь файла из POST-запроса

        # получение имя файла 
        match = re.search(r'disk:/(.*)', file_path)
        if match:
            filename = match.group(1)
            
        client = yadisk.Client(token=token)        
        with client:
            try:
                client.download(file_path, filename)
                return HttpResponse(f"файл {filename} успешно скачан")
            except Exception as e:
                return HttpResponse(f"Ошибка скачивания: {str(e)}", status=500)
    return HttpResponse("Метод не поддерживается", status=405)