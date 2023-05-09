from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Links
from .forms import AddLinks

def home(request):
    return render(request, 'links/home.html', {'title': 'Главная страница'})

def contacts(request):
    return render(request, 'links/contacts.html', {'title': 'О нас'})

@login_required
def links(request):
    form = AddLinks(request.POST)
    err = False
    if request.method == "POST":
        if form.is_valid():
            new_short = '127.0.0.1:8000/go_link/' + form.cleaned_data.get('short_url')
            if not Links.objects.filter(short_url=new_short).first():
                new_link = form.save()
                new_link.short_url = new_short
                new_link.user = request.user
                new_link.save()
                form = AddLinks()
            else:
                err = True

    data ={
        'err': err,
        'links': Links.objects.filter(user=request.user), 
        'form': form,
        'title': 'Создание ссылок'
    }
    return render(request, 'links/ssyl.html', data)

def goLink(request, slug):
    url = '127.0.0.1:8000' + request.path
    re_url = Links.objects.filter(short_url=url).first()
    return redirect(re_url.full_url)

