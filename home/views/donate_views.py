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
        
        name = request.POST.get('full_name')
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
            message = f"A donation has been made through the website"
            message = f"Full Name: {name}\n"
            message += f"Email: {email}\n"
            message += f"Amount: {total_amount}\n"
            message += f"Message: {message}\n"
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


    
    return render(request,'pages/donate.html') 