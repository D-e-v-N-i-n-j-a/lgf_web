from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
import paypalrestsdk
# Create your views here.

paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})


def home(request):
    
    return render(request,'pages/index.html')



def aboutUs(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Send email
        try:
            send_mail(
                subject='New Contact Form Submission',
                message=f'From: {full_name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            success_message = "Your message has been sent successfully!"
            
            
        except:
            success_message = None
    else:
        success_message = None
    
    return render(request,'pages/about-us.html', {'success_message': success_message})




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
            for link in payment.links:
                if link.method == "REDIRECT":
                    return redirect(link.href)
        else:
            return HttpResponse(f"Payment creation failed: {payment.error}")


    
    return render(request,'pages/donate.html') 

