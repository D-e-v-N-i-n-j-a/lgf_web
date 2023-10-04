from django.shortcuts import redirect, render,get_object_or_404
from home.models import OurWork,Metrics
from django.shortcuts import  render
from django.core.mail import send_mail
from django.conf import settings
from home.models import ContactFormSubmission,Blog,Donation,Team,Testimonial,Cause
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.functions import Random
import paypalrestsdk
from django.http import HttpResponse


paypalrestsdk.configure({
    "mode": "live",  
    "client_id": 'AWWbypiy6yDnYIlWs1E9Lao8rUR3k1yVgkLb3azj9IPJ2L9mRKs_kGehErA3rEpsSasRQLFm8YLXeG24',
    "client_secret": 'EDR2ox3hcvyu1qksrW_GdWGYsZz8HqUKbZ0Mg_YocW2r2HNvARu_dcaobvDlgilm7oL7SZIaf2O0Oscn',
})

def home(request):
    works = OurWork.objects.all()
    team_members = Team.objects.all()
    statistics = Metrics.objects.first()
    testimonials = Testimonial.objects.all()
    causes = Cause.objects.all()
    success_message = None  # Initialize success_message
    
    # DISPLAY RANDOM BLOGS HERE
    random_blogs = Blog.objects.annotate(random_order=Random()).order_by('random_order')[:3]

    
    
    if request.method == 'POST':
        
        if 'contact_submit' in request.POST:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

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
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],  # Send thank-you email to the user
                fail_silently=False,
            )
                success_message = "Your message has been sent successfully!"
            except Exception as e:
                success_message = None
                
        
        if 'donation_submit' in request.POST:
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                amount = request.POST.get('amount')
                custom_amount = request.POST.get('customAmount')
            if amount:
                print(f"Amount: {amount}")
                total_amount = float(amount)
            elif custom_amount:
                print(f"Custom Amount: {custom_amount}")
                total_amount = float(custom_amount)
            else:
                return HttpResponse("Please provide a donation amount")
        
        
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
                donation = Donation(name=name, email=email, amount=total_amount)
                donation.save()
                message = f"A donation has been made through the website"
                message = f"Full Name: {name}\n"
                message += f"Email: {email}\n"
                message += f"Amount: {total_amount}\n"
           
                send_mail(
                subject = 'Donation Made',
                message = message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list = ['Learnersgirlsfoundation@gmail.com'],
                fail_silently=False,
                )
    
                send_mail(
                subject = 'Thank You for Your Donation',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list = [email],
                fail_silently=False,
                        message = f'''
Dear {name},

Thank you for your generous donation to Leaner's Girls Foundation. Your support is greatly appreciated and makes a significant difference in our mission.

Your contribution will help us [mention how the donation will be used, e.g., support a specific cause, project, or program]. We are truly grateful for your generosity and commitment to our cause.

We value your support and look forward to keeping you updated on how your donation is making an impact. If you have any questions or would like to learn more about our work, please feel free to contact us.

Once again, thank you for your kindness and support. Together, we can make a positive change in the lives of those we serve.

Sincerely,
Founder : Kumuriwor Alira Bushiratu
 Leaner's Girls Foundation
'''
            )
            
                for link in payment.links:
                    if link.method == "REDIRECT":
                        return redirect(link.href)
            else:
                return HttpResponse(f"Payment creation failed: {payment.error}")
        
    
    

    
    return render(request, 'pages/index.html', {'works': works, 'statistics': statistics, 'success_message': success_message,'random_blogs': random_blogs,'team_members': team_members, 'testimonials': testimonials, 'causes': causes,})



def home_details(request, id):
    works = get_object_or_404(OurWork, pk=id)
    return render(request, 'pages/work_details.html', {'works': works})



