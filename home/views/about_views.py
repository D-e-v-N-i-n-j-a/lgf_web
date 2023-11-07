from django.shortcuts import  render
from django.core.mail import send_mail
from django.conf import settings

from home.models import ContactFormSubmission,Team,Testimonial,BoardMembers



# CONTACT US FORM
def aboutUs(request):
    success_message = None
    teams = Team.objects.all()
    testimonial = Testimonial.objects.all()
    board_members = BoardMembers.objects.all()

    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

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

    return render(request, 'pages/about.html', {'success_message': success_message,'teams': teams,'testimonials':testimonial,'board_members':board_members})



