from client.models import MainCarousel
from django.shortcuts import render, redirect
import os
from django.http import HttpResponseRedirect

def main_carousel_control(request):
    images = MainCarousel.objects.all()

    return render(request,'backend/pages/page_control/carousel/carousel.html',{'images': images} )

def add_main_carousel(request):

    if request.method == "POST":
         image = request.FILES.get('image1')
        
         title = request.POST.get('title')


         if not image:
             return  render(request,'backend/pages/page_control/carousel/add.html',{'error': 'Upload the images first'} )
         elif not title:
             return  render(request,'backend/pages/page_control/carousel/add.html',{'error': 'Title is required'} )
         else:
             carousel_item = MainCarousel(image=image)
             carousel_item.title = title
             carousel_item.save()

             
             return redirect('main_carousel_control')

    return render(request,'backend/pages/page_control/carousel/add.html')

def delete_image(request, image_id):
    image = MainCarousel.objects.get(id=image_id)
    # Delete the image file from the file system
    if image.image:
        if os.path.isfile(image.image.path):
            os.remove(image.image.path)

    image.delete()
    return redirect('main_carousel_control')
