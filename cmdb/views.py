import random
import time

from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from utils import db_mysql



def regist(request):
  if request.method == 'GET':
    return render(request, 'day6_regist.html')
  if request.method == 'POST':
    # 注册
    name = request.POST.get('name')
    password = request.POST.get('password')
    # 对密码进行加密
    password = make_password(password)
    # User.objects.create(u_name=name, u_password=password)
    sql = "INSERT INTO user (username,password) VALUES ('{name}','{password}')".format(name = name,password = password)
    hha = db_mysql.db.execute(sql)
    # return HttpResponseRedirect('index11.html')
    return render(request, 'index11.html')


def dgregist(request):
  if request.method == 'GET':
    return render(request, 'day6_regist.html')
  if request.method == 'POST':
    name = request.POST.get('name')
    password = request.POST.get('password')
    User.objects.create_user(username=name, password=password)
    return HttpResponseRedirect('/uauth/dglogin/')


def dglogin(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  if request.method == 'POST':
    name = request.POST.get('name')
    password = request.POST.get('password')
    # 验证用户名和密码，通过的话，返回User对象
    user = auth.authenticate(username=name, password=password)
    if user:

      auth.login(request, user)
      return HttpResponseRedirect('/stu/index/')
    else:
      return render(request, 'index11.html')


def dglogout(request):
  if request.method == 'GET':
    auth.logout(request)
    return HttpResponseRedirect('/uauth/dglogin')



def index(request):
  if request.method == 'GET':
    # 获取所有学生信息
    print(type(request))
    ticket = request.COOKIES.get('ticket')
    if not ticket:
      return HttpResponseRedirect('/login/')
    # if User.objects.filter(u_ticket=ticket).exists():
    #   stuinfos = StudentInfo.objects.all()
    #   return render(request, 'index11.html', {'stuinfos': stuinfos})
    else:
      return HttpResponseRedirect('/login/')