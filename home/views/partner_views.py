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

I wanted to take a moment to express our heartfelt gratitude for your incredible efforts in organizing and leading the recent fundraising campaign for {organizations}. Your dedication and hard work have made a significant impact, and we are truly thankful for your generosity and commitment to our cause.

Your passion and enthusiasm have not only inspired those around you but have also brought us closer to our fundraising goals. Thanks to your tireless efforts, we have been able to [mention specific achievements or milestones reached].

We believe that it's people like you who make a real difference in the world. Your willingness to give your time, energy, and resources to support our cause is remarkable, and we are fortunate to have you as a part of our community.

Please accept our deepest thanks and know that your contributions are making a positive change in the lives of those we serve. We look forward to continuing this journey together and achieving even greater successes in the future.

Once again, thank you for your outstanding dedication to our cause. Your commitment to making the world a better place is truly inspiring.

With gratitude,
Learner's Girls Foundation''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],  # Send confirmation email to the user
            fail_silently=False,
        )
        
        return render(request, 'pages/partnerforms.html', {'success_message': 'Form submitted successfully.'})

    else:

        return render(request, 'pages/partnerforms.html')