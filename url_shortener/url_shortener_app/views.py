from django.shortcuts import render
from django.views import View


class MainPage(View):
    def get(self, request):
        return render(request, 'url_shortener_app/shortener_main.html')  # shortener_main.html
