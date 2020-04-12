from django.shortcuts import render, redirect
from django.views import View

from .models import Parse

class IndexViews(View):

    def get(self, request, uniqid):
        req = Parse.objects.filter(parse__iexact=uniqid)
        if len(req) > 0:
            for i in req:
                return redirect(i.url)
        else:
            return render(request,'error.html')