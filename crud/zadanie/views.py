from django.shortcuts import render, redirect

from .forms import AddForm
from .models import News



def index(request):
    news = News.objects.all()
    return render(request, 'zadanie/main.html', context={'news': news})
#
# def makeMen():
#     p, try5lekuihr5jou = Person.objects.get_or_create(name='Tomeygdtrhj', surname='Tvhgfnhfsv', age=18, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom1', surname='fgv', age=28, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom2', surname='Tvhfjmdsv', age=38, gender=True, birthDay='2011-02-02')
#     p, _ = Person.objects.get_or_create(name='Tom3', surname='Tvhhmsv', age=19, gender=True, birthDay='2011-05-12')
#     p, _ = Person.objects.get_or_create(name='Tom4', surname='Tvhhfmnjsv', age=25, gender=True, birthDay='2011-12-05')
#



def create(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post_name = form.cleaned_data['post_name']
            post_description = form.cleaned_data['post_description']
            post_img = form.cleaned_data['post_img']
            men, _ = News.objects.get_or_create(post_img=post_img,post_name=post_name,post_description=post_description)

            return redirect('home')
        else:
            form = AddForm()
            return render(request, 'zadanie/create.html', context={'form': form})
    else:
        form = AddForm()
        return render(request, 'zadanie/create.html', context={'form': form})


def update(request, id):
    try:
        men = News.objects.get(id=id)
        if request.method == "POST":
            men.post_name = request.POST.get('post_name')
            men.post_description = request.POST.get('post_description')
            men.post_img = request.POST.get('post_img')
            men.save()
            return redirect('home')
        else:
            return render(request, 'zadanie/update.html', context={'men': men})
    except:
        return redirect('create')


def delete(request, id):
    try:
        men = News.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        return redirect('create')