from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def schoolly_home(request):
    return render(request, 'pages/schoolly-home.html')

def about(request):
    return render(request, 'pages/about.html')


def faqs(request):
    return render(request, 'pages/faqs.html')




def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        # message_subject = request.POST['subject']
        message = request.POST['message']
        # messages.success(request, f'New user account has been created. You can register another user.')


        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['contact@fizcos.com'] #to email
            ,
            )
   
        return render(request, 'pages/schoolly-home.html', {'message_name': message_name})
    else:
        return render(request, 'pages/schoolly-home.html', {})


def affiliate(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        messages.success(request, f'New user account has been created. You can register another user.')


        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['support@gmail.com'] #to email
            ,
            )
   
        return render(request, 'pages/affiliate.html', {'message_name': message_name})
    else:
        return render(request, 'pages/affiliate.html', {'title': 'Affiliate'})


def demo(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']
        messages.success(request, f'New user account has been created. You can register another user.')


        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['support@gmail.com'] #to email
            ,
            )
   
        return render(request, 'pages/demo.html', {'message_name': message_name})
    else:
        return render(request, 'pages/demo.html', {'title': 'Demo'})



def schoolly_home(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_phone = request.POST['phone']
        message_subject = request.POST['subject']
        message = request.POST['message']
    # messages.success(request, f'New user account has been created. You can register another user.')
        message = "Your name: " +  message_name  + " Your Email: " + message_email + " Your Phone: " + message_phone + " Subject: " + message_subject + " Content: " +  message

        send_mail(
            'Contact form detail', #subject
            message, #message
            message_email, #from email
            ['dtechydude@gmail.com', 'contact@schoolly.ng', 'solarrel@yahoo.co.uk'] #to email
            ,
            )

        return render(request, 'pages/schoolly-home.html', {'message_name': message_name})
    else:
        return render(request, 'pages/schoolly-home.html', {})
    # return render(request, 'pages/schoolly-home.html')



def contact_us(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_phone = request.POST['phone']
        message_subject = request.POST['subject']
        message = request.POST['message']
    # messages.success(request, f'New user account has been created. You can register another user.')
        message = "Your name: " +  message_name  + " Your Email: " + message_email + " Your Phone: " + message_phone + " Subject: " + message_subject + " Content: " +  message

        send_mail(
            'Contact form detail', #subject
            message, #message
            message_email, #from email
            ['dtechydude@gmail.com', 'contact@schoolly.ng', 'solarrel@yahoo.co.uk'] #to email
            ,
            )

        return render(request, 'pages/contact-demo.html', {'message_name': message_name})
    else:
        return render(request, 'pages/contact-demo.html', {})