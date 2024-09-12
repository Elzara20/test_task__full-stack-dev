# test_task__full-stack-dev
Тестовое задание на позицию "Full-stack разработчик" в компанию MYCEGO

## Установка и запуск
1. Клонирование репозитория
```bash
 git clone https://github.com/Elzara20/test_task__full-stack-dev.git 
```
2. Переход в директорию проекта 
```bash
 cd .\test_task__full-stack-dev\project\
```
3. Установка зависимостей
```bash
pip install -r requirements.txt
```
4. Миграции
```bash
python manage.py migrate
```
5. Запуск сервера
```bash
python manage.py runserver
```
Далее перейдите по адресу http://127.0.0.1:8000/

## Внешний вид

### Начальная страница (формы)
![start_page](https://github.com/Elzara20/test_task__full-stack-dev/blob/main/pictures/start.png)

Необходимо ввести OAuth-токен для авторизации в Яндексе и публичную ссылку (public_key) на Яндекс.Диск, где будут файлы и папки 

### Список файлов
![view_file](https://github.com/Elzara20/test_task__full-stack-dev/blob/main/pictures/view_file.png)


После выбора файла и нажатия кнопки "Скачать" на экране выводится сообщение ```файл имя_файла.jpg успешно скачан```
