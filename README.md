## Django-ESP32-CAM-Stream ##

Цей проект є веб-додатком, створеним з використанням фреймворку Django, який відображає відеопотік з камери мікроконтролеру ESP32-CAM на веб-сторінці.

**Структура проекту**

Проект складається з кількох частин Django проект (testing_project) та Django додаток (sensor_app).

**Django проект (testing_project)**

* settings.py: Містить параметри проекту, такі як база даних, підключені програми та інші параметри.
* urls.py: Опис маршрутів для проекту.
* wsgi.py та asgi.py: Для запуску програми в різних середовищах.
* manage.py: Основний скрипт для управління проектом (запуск сервера, міграції, створення суперкористувачів тощо).

**Django додаток (sensor_app)**

* views.py: Визначає логіку відображення відеопотоку з камери.
* urls.py: Визначає маршрути, пов'язані з відображенням відеопотоку.
* templates/video_stream.html: Шаблон HTML, який відображає відеопотік з камери.



**Підключення камери ESP32-CAM**

У проекті передбачається використання камери ESP32-CAM, яка передає відеопотік через IP-адресу. У програмі Django необхідно вказати IP-адресу камери, наприклад, http://192.168.0.105:81/stream.
Програма дозволяє відобразити реальний відеопотік з камери мікроконтролера на веб-сторінці. Проект демонструє базову роботу з Django, налаштування програми, шаблони та маршрути, а також використання зовнішніх пристроїв (камер) для відображення даних у реальному часі.
