from django.shortcuts import render
from home.models import OurWork,Metrics

def home(request):
    works = OurWork.objects.all()
    statistics = Metrics.objects.first()
    
    return render(request, 'pages/index.html', {'works': works,'statistics': statistics})



