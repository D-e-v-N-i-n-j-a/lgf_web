from django.shortcuts import render
from home.models import Volunteers  
from django.core.mail import send_mail
from django.conf import settings

def volunteer(request):
    if request.method == 'POST':
        # Get the form data from the request
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        contact_number = request.POST.get('contact_number')
        country = request.POST.get('country')
        summary_of_proposed_partnership = request.POST.get('summary_of_proposed_partnership')

        # Create a new PartnershipInquiry object and save it to the database
        partnership_inquiry = Volunteers(
            email=email,
            firstname=firstname,
            lastname=lastname,
            contact_number=contact_number,
            country=country,
            summary_of_proposed_partnership=summary_of_proposed_partnership
        )
        partnership_inquiry.save()

        # Send a confirmation email
        send_mail(
            subject='Thank You for Your Partnership Inquiry',
            message=f'''
                Dear {firstname} {lastname},

                Thank you for your partnership inquiry. We will contact you shortly to discuss the details.

                Sincerely,
                Your Organization Name
            ''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],  # Send confirmation email to the user
            fail_silently=False,
        )

        # Render a success message or redirect to a success page
        return render(request, 'pages/volunteer.html', {'success_message': 'Form submitted successfully.'})

    return render(request, 'pages/volunteer.html')
