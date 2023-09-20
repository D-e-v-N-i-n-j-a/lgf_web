from django.http import HttpResponse
from django.shortcuts import  render,redirect
from django.core.mail import send_mail
from django.conf import settings
import paypalrestsdk
from home.models import Donation

paypalrestsdk.configure({
    "mode": "live",  
    "client_id": 'AWWbypiy6yDnYIlWs1E9Lao8rUR3k1yVgkLb3azj9IPJ2L9mRKs_kGehErA3rEpsSasRQLFm8YLXeG24',
    "client_secret": 'EDR2ox3hcvyu1qksrW_GdWGYsZz8HqUKbZ0Mg_YocW2r2HNvARu_dcaobvDlgilm7oL7SZIaf2O0Oscn',
})

def donate(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('donationAmount')
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
            donation = Donation(name=name, email=email, amount=total_amount)
            donation.save()
    
            send_mail(
                subject = 'Thank You for Your Donation',
                message = 'Thank you for your generous donation. We appreciate your support!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list = [email],
                fail_silently=False,
                )
            
            for link in payment.links:
                if link.method == "REDIRECT":
                    return redirect(link.href)
        else:
            return HttpResponse(f"Payment creation failed: {payment.error}")


    
    return render(request,'pages/donate.html') 