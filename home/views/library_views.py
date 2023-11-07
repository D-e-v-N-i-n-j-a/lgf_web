from django.shortcuts import render
from home.models import LibraryPictures  # Import your LibraryPicture model

def community_library(request):
    

    return render(request, 'pages/library.html')





def gallery(request):
    
    # Get all LibraryPicture objects from the database
    pictures = LibraryPictures.objects.all()
    return render(request,'pages/gallery.html',{'gallery':pictures})



