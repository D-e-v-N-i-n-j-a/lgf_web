from django.shortcuts import render,get_object_or_404
from home.models import OurWork,Metrics

def home(request):
    works = OurWork.objects.all()
    statistics = Metrics.objects.first()
    
    return render(request, 'pages/index.html', {'works': works,'statistics': statistics})




def home_details(request, id):
    works = get_object_or_404(OurWork, pk=id)
    return render(request, 'pages/work_details.html', {'works': works})



