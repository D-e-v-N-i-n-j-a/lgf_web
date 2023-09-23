from django.shortcuts import render
from home.models import LibraryPictures  # Import your LibraryPicture model

def community_library(request):
    # Get all LibraryPicture objects from the database
    pictures = LibraryPictures.objects.all()

    return render(request, 'pages/commnunity_library.html', {'pictures': pictures})



