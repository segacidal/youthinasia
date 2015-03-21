from django.shortcuts import render
from django.http import HttpResponse, Http404
from gallery.models import Gallery, Image
from gallery.forms import GalleryForm

from utils import gallery_fuctions as gfunc

def home(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery/home.html', {'galleries': galleries})

def addgallery(request):

    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            gallery = form.save()
            gfunc.create_folder(gallery.slug)

    else:
        form = GalleryForm()
    return render(request, 'gallery/addgallery.html', {'form': form})

def gallery(request, slug):
    g = Gallery.objects.get(slug = slug)
    images = g.image_set.all()

    if len(images) == 0:
        return render(request, 'gallery/gallery.html', {'images': images, 'warning': "No Images!"})
    else:
        return render(request, 'gallery/gallery.html', {'images': images})