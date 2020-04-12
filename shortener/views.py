from django.views import View
from django.shortcuts import render
#parse string
import random
import string
# model
import datetime
from parse.models import Parse


class IndexView(View):

    context = {}

    def get(self, request):
        return render(request,'index.html')

    def encode(self):
        N = 5
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        return res

    def post(self, request):
        param = request.POST
        if len(Parse.objects.all()) > 0:
            req = Parse.objects.filter(url=param["url"])
            if len(req) > 0:
                s = ''
                for i in req:
                    s = i.parse
                self.context['parse'] = s
                self.context['method'] = 'POST'
            else:
                p = self.encode()
                insert = Parse(url=param['url'], parse=p, tanggal= datetime.datetime.now())
                insert.save()
                self.context['parse'] = p
                self.context['method'] = 'POST'
        else:
            encode = self.encode()
            i = Parse(url=param['url'], parse=encode)
            i.save()
            self.context['parse'] = encode
            self.context['method'] = "POST"
        return render(request,'index.html', self.context)