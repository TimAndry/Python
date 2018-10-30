from django.shortcuts import render, redirect
from .models import Course

def index(request):
    course = Course.objects.all()
    context = {
        'courses': course
    }
    return render(request, 'courses_app/index.html', context, course)

def create(request):
    print('*' * 50)
    new_course = Course.objects.create(name = request.POST['name'], description = request.POST['desc'])

    return redirect('/')

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course
    }
    return render( request, 'courses_app/edit.html', context)


def delete(request, course_id):
    delete = Course.objects.get(id=course_id)
    delete.delete()
    return redirect('/')

def no(request):
    return redirect('/')
