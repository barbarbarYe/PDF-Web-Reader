from django.shortcuts import render_to_response


def index(request):
    return render_to_response('../templates/viewer.html', {'title': 'This is Title', 'message': 'This is message'})

