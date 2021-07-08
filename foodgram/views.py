from django.shortcuts import render

def page_not_found(request, exception):
    """
    Обработка ошибок 404. Работает только при DEBUG = False
    """

    return render(request, 'base/message.html', {
        'title': 'Ошибка 404',
        'message': 'Страница не найдена'
    },
        status=404)


def server_error(request):
    """
    Обработка ошибок 500. Работает только при DEBUG = False
    """
    return render(request, 'base/message.html', {
        'title': 'Ошибка 500',
        'message': 'Ошибка сервера'
    },
        status=500)
