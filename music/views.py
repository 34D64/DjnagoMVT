from django.shortcuts import render
from django.http import HttpResponse
from .models import Music
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import musicForm

# def UserWithoutSingin(request):
#     qs = Music.objects.all()

#     return HttpResponse(qs)


# def ArtistMusic(request):
#     user =request.user
#     print(user)
#     qs = Music.objects.filter(Artist__name=3)
#     qs = qs.filter(rank=1000)
#     print(qs)

#     return HttpResponse(qs)


# class MusicList(ListView):
#     model = Music



def MusicList(request):
    context ={}
    qs = Music.objects.all()

    form = musicForm(request.POST or None )
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    # qs = qs.filter(Artist__name = request.user)
    context['form']= form
    return render(request,template_name='music/index.html',context=context)


def music(request):
    context ={"ali":20,
              "sina":21}
    qs = Music.objects.all()

    # qs = qs.filter(Artist__name = request.user)
    context['form']= qs
    return render(request,template_name='music/music.html',context=context)