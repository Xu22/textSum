from django.shortcuts import render,render_to_response
# from dao.models import User
import json

import code
from manager.textsummary import TextSummary
from bs4 import BeautifulSoup
from urllib import request
import xlwt
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # username=request.COOKIES.get('username','')
    # blog_list = BlogsPost.objects.all()  # 获取所有数据
    # return render_to_response('index.html',{'username':username,'blog_list':blog_list,'form':BlogsPostForm()})
    return render_to_response('index.html')

def CalcSummary(request):
    data = request.body
    data = data.decode("utf-8",'ignore')
    content = json.loads(data, strict=False)
    # content=content.dict()
    # print(content)
    # code.interact()
    text = content['text']
    title = content['title']
    # print(text)
    textsummary = TextSummary()
    textsummary.SetText(title, text)
    summary = textsummary.CalcSummary()
    print(summary)
    return HttpResponse(summary)