from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render,redirect
from django.core.mail import send_mail
from django.conf import settings
from home.models import Blog,Comment
from django.contrib import messages
from home.form import CommentForm





# BLOG HERE
def blogs(request):
    all_blogs = Blog.objects.all()
    paginator = Paginator(all_blogs, 4)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    
    context = {
        'blogs': blogs,
    }


    return render(request,'pages/blog.html',context)






def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            
            full_name = form.cleaned_data['full_name'],
            
            send_mail(
                subject = 'New Blog Comment',
                message = f"New Comment from {full_name}:\n\n",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list = ['skyhightech93@gmail.com'],
                fail_silently=False,
            )
            
            print("email sent")
            return redirect('home:blog-details', blog_id=blog.id)

    else:
        form = CommentForm() 

    return render(request, 'pages/single.html', {'blog': blog, 'comments': comments, 'form': form})


