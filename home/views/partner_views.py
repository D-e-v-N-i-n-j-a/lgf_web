from django.shortcuts import  render
from django.core.mail import send_mail
from django.conf import settings
from home.models import PartnershipForm
# Create your views here.



def partnership(request):
    
    return render(request,'pages/partner.html')
    



# PARTNERSHIP FORM
def partnerForm(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        organizations = request.POST.get('organizations')
        contact_number = request.POST.get('contact_number')
        country = request.POST.get('country')
        area_of_interest = request.POST.get('areaOfInterest')
        summary = request.POST.get('summary_of_proposed_partnership')
        start_date = request.POST.get('start_date')
        finish_date = request.POST.get('finish_date')
        fundraising_amount = request.POST.get('fundraisingAmount')
        
        form_instance = PartnershipForm(
            email=email,
            firstname=firstname,
            lastname=lastname,
            organizations=organizations,
            contact_number=contact_number,
            country=country,
            area_of_interest=area_of_interest,
            summary_of_proposed_partnership=summary,
            start_date=start_date,
            finish_date=finish_date,
            sponsorship_amount=fundraising_amount
        )
        form_instance.save()
        message = f"Email: {email}\nFirst Name: {firstname}\nLast Name: {lastname}\nOrganizations: {organizations}\n"
        message += f"Contact Number: {contact_number}\nCountry: {country}\nArea of Interest: {area_of_interest}\n"
        message += f"Summary: {summary}\nStart Date: {start_date}\nFinish Date: {finish_date}\n"
        message += f"Fundraising Amount: {fundraising_amount}"
        
        # SEND EMAIL TO VISITOR
        
        send_mail(
            subject='Partner Form Submission',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['Learnersgirlsfoundation@gmail.com'],  # Send confirmation email to the user
            fail_silently=False,
        )
        
        send_mail(
            subject = 'Thank You for Your Partnership Inquiry',
           message = f'''Dear {firstname} {lastname},

Thank you for your interest in fundraising for our cause. We appreciate your submission and dedication to making a positive impact.

We have received your fundraising proposal and will review it shortly. Our team will be in touch with you to discuss the details and next steps. If you have any immediate questions or concerns, please feel free to contact us.

Once again, thank you for your commitment to our cause. Together, we can make a difference.

Sincerely,
Your Organization Name
Founder : Kumuriwor Alira Bushiratu
''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],  # Send confirmation email to the user
            fail_silently=False,
        )
        
        return render(request, 'pages/partnerforms.html', {'success_message': 'Form submitted successfully.'})

    else:

        return render(request, 'pages/partnerforms.html')