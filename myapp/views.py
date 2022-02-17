from audioop import avg
from django.shortcuts import render
from .models import Musician,Album
from . import forms
# Create your views here.
def home(req):
    mp=Musician.objects.all()
    data={'mp':mp}


    return render(req,'home.html',data)
def post(req):

    return render(req,'post_success.html')

def add_musician(req):
    form=forms.MusicianForms()
    if req.method=="POST":
        form=forms.MusicianForms(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return post(req)
    
    data={'musicform':form,
          'successpost':'form submitted successfully!'}

    return render(req,'add_musician.html',data)

def list(req,idi):
    artist_info=Musician.objects.get(pk=idi)
    albumlist=Album.objects.filter(artist=idi)
    
    data={'album_list':albumlist,'artist_info':artist_info,}
    return render(req,'musician_list.html',data)

def new(req,idi):
    return render(req,'new.html')

def edit(req,idik):
    art_info=Musician.objects.get(pk=idik)
    art_form=forms.MusicianForms(instance=art_info)
    if req.method=="POST":
        art_form=forms.MusicianForms(req.POST,instance=art_info)
        if art_form.is_valid():
            art_form.save(commit=True)
            return update(req)
    data={'art_info':art_info,'art_form':art_form}

    return render(req,'edit.html',data)

def addartist(req):
    albumform=forms.AlbumForms()
    if req.method=="POST":
        albumform=forms.AlbumForms(req.POST)
        if albumform.is_valid():
            albumform.save(commit=True)
            return post(req)
    data={'albumform':albumform}
    return render(req,'add_artist.html',data)

def update(req):

    return render(req,'update.html')

def update2(req,idki):
    ark_info=Album.objects.get(pk=idki)
    ark_form=forms.AlbumForms(instance=ark_info)
    data={}
    if req.method=="POST":
        ark_form=forms.AlbumForms(req.POST,instance=ark_info)
        if ark_form.is_valid():
            ark_form.save(commit=True)
            return update(req)
    data.update({'ark_form':ark_form})
    data.update({'idki':idki})



    return render(req,'update2.html',context=data)
def delete(req,aid):

    artist_delete=Album.objects.get(pk=aid).delete(0)

    data={'artist_delete':artist_delete}

    return render(req,'delete.html',data)
