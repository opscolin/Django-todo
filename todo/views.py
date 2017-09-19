#!/usr/bin/env python
# coding: utf-8
# Author: Colin
# Date:
# Desc:
#

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Todo

def index(request):
    todos = Todo.objects.all().order_by('finished', '-id')
    return render(request, 'todo/index.html', {"todos": todos})

def new(request):
	if request.method == "POST":
		title = request.POST.get('title')
		try:
			todo = Todo(title=title)
			todo.save()
			messages.info(request, u'新增成功')
		except:
			messages.info(request, u'新增失败')
		return HttpResponseRedirect(reverse("todo:index"))
	return render(request, 'todo/new.html')

def edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        todo = get_object_or_404(Todo, id=id)
        todo.title = title
        todo.save()
        return HttpResponseRedirect(reverse("todo:index"))
    return render(request, 'todo/edit.html', {'todo': todo})


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    messages.info(request, u'成功删除')
    return HttpResponseRedirect(reverse("todo:index"))


def finish(request, id):
    todo = get_object_or_404(Todo, id=id)
    status = request.GET.get('status', '')
    if status == 'yes':
        finished = 1
        todo.finished = finished
    elif status == 'no':
        finished = 0
    else:
        messages.info(request, u'非法请求')
        return HttpResponseRedirect(reverse("todo:index"))
    todo.finished = finished
    todo.save()
    messages.info(request, u'修改成功')
    return HttpResponseRedirect(reverse("todo:index"))
