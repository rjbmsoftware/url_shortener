from django.shortcuts import render, redirect
from django.views import View


class MainPage(View):
    def get(self, request):
        return render(request, 'url_shortener_app/shortener_main.html')  # shortener_main.html

    def post(self, request, *args, **kwargs):
        """
        validate form
        check url is db
        if in db return that url + code
        redirect to link page to copy
        """
        return redirect('/new_url/', request)


class UrlOutput(View):
    def get(self, request):
        return render(request, 'url_shortener_app/url_output.html')