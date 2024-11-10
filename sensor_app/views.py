from django.shortcuts import render

def video_stream(request):
    # Передаем URL видеопотока в шаблон
    camera_url = "http://192.168.0.108:81/stream"  # IP-адрес вашей камеры
    return render(request, 'video_stream.html', {'camera_url': camera_url})
