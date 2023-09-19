from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Blog,Comment
import paypalrestsdk
from .models import ContactFormSubmission,Donation
from .form import CommentForm
# Create your views here.

paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})


def home(request):
    
    return render(request,'pages/index.html')





# CONTACT US FORM
def aboutUs(request):
    success_message = None

    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Save user information to the database
        submission = ContactFormSubmission(
            full_name=full_name,
            email=email,
            phone=phone,
            message=message,
        )
        submission.save()

        # Send email
        try:
            send_mail(
                subject='Thank You for Contacting Us',
                message='Thank you for contacting us. We will get back to you soon!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],  # Send thank-you email to the user
                fail_silently=False,
            )
            success_message = "Your message has been sent successfully!"
        except Exception as e:
            success_message = None

    return render(request, 'pages/about-us.html', {'success_message': success_message})


# DONATE FORM
def donate(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        custom_amount = request.POST.get('customAmount')

        print(f"Name: {name}")
        print(f"Email: {email}")

        if amount:
            print(f"Amount: {amount}")
            total_amount = float(amount)
        elif custom_amount:
            print(f"Custom Amount: {custom_amount}")
            total_amount = float(custom_amount)
        else:
            return HttpResponse("Please provide a donation amount")

        # Create a PayPal payment object
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
            },
            "transactions": [
                {
                    "amount": {
                        "total": str(total_amount),
                        "currency": "USD",
                    },
                    "description": f"Donation from {name}",
                }
            ],
            "redirect_urls": {
                "return_url": "http://127.0.0.1:8000/donation/success/",
                "cancel_url": "http://127.0.0.1:8000/donation/cancel/",
            }
        })

        # Create the payment on PayPal
        if payment.create():
            # Redirect the user to PayPal for payment approval
            donation = Donation(name=name, email=email, amount=total_amount)
            donation.save()
            subject = 'Thank You for Your Donation'
            message = 'Thank you for your generous donation. We appreciate your support!'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            for link in payment.links:
                if link.method == "REDIRECT":
                    return redirect(link.href)
        else:
            return HttpResponse(f"Payment creation failed: {payment.error}")


    
    return render(request,'pages/donate.html') 




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
    comments = Comment.objects.filter(blog=blog)  # Retrieve comments for the current blog

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('home:blog-details', blog_id=blog.id)

    else:
        form = CommentForm() 

    return render(request, 'pages/blog-details.html', {'blog': blog, 'comments': comments, 'form': form})





def join(request):
    
    return render(request,'pages/join-us.html')
    
    
















