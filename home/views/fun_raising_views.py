from django.shortcuts import render, redirect
from django.core.mail import send_mail
from home.models import Fundraiser  # Import the Fundraiser model you defined
from django.contrib import messages

def funRaising(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        area_of_interest = request.POST.get('areaOfInterest')
        summary = request.POST.get('summary_of_proposed_partnership')
        start_date = request.POST.get('start_date')
        finish_date = request.POST.get('finish_date')
        fundraising_amount = request.POST.get('fundraisingAmount')

        # Create a new Fundraiser object and save it to the database
        fundraiser = Fundraiser(
            email=email,
            firstname=firstname,
            lastname=lastname,
            country=country,
            area_of_interest=area_of_interest,
            summary_of_proposed_partnership=summary,
            start_date=start_date,
            finish_date=finish_date,
            fundraising_amount=fundraising_amount
        )
        fundraiser.save()

        # Send an email to the fundraiser
        subject = 'Thank You for Your Fundraising Efforts'
        message = f'Dear {firstname} {lastname},\n\n' \
                  'Thank you for your fundraising efforts. We appreciate your support!\n\n' \
                  'Sincerely,\n' \
                  'Your Organization Name'
        from_email = 'your@email.com'  # Replace with your organization's email
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Show a success message
        return render(request, 'pages/partnerforms.html', {'success_message': 'Form submitted successfully.'})


    return render(request, 'pages/fun_raising.html')
