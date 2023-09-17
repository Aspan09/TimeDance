from django.shortcuts import render
from .forms import ContactFormOne, ContactFormTwo
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import (Actual, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,
                     ActualButtonOne, ActualButtonTwo, ActualButtonThird, ActualButtonFourth,
                     ActualButtonFifth
                     )


def homepage(request):
    context = {}
    posts_monday = Monday.objects.all()
    posts_tuesday = Tuesday.objects.all()
    posts_wednesday = Wednesday.objects.all()
    posts_thursday = Thursday.objects.all()
    posts_friday = Friday.objects.all()
    posts_saturday = Saturday.objects.all()
    posts_one = ActualButtonOne.objects.all()
    posts_two = ActualButtonTwo.objects.all()
    posts_three = ActualButtonThird.objects.all()
    posts_four = ActualButtonFourth.objects.all()
    posts_five = ActualButtonFifth.objects.all()

    posts_actual = Actual.objects.all()

    if request.method == 'POST':
        form_two = ContactFormTwo(request.POST)
        if form_two.is_valid():
            send_message(form_two.cleaned_data['first_name'],
                         form_two.cleaned_data['email_address'],
                         form_two.cleaned_data['phone'],
                         form_two.cleaned_data['message'],
                         )
            context = {'success': 1}
    else:
        form_two = ContactFormTwo()

    context['form_two'] = form_two

    template_name = 'index.html'
    print(posts_one)
    print(posts_five)
    return render(request, template_name,
                  {'posts_monday': posts_monday, 'posts_tuesday': posts_tuesday,
                   'posts_wednesday': posts_wednesday, 'posts_thursday': posts_thursday,
                   'posts_friday': posts_friday, 'posts_saturday': posts_saturday,
                   'posts_actual': posts_actual, 'posts_one': posts_one, 'posts_two': posts_two,
                   'posts_three': posts_three, 'posts_four': posts_four, 'posts_five': posts_five,
                   'form_two': form_two,
                   }
                  )


def send_message(first_name, email_address, phone, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'first_name': first_name, 'email_address': email_address, 'phone': phone, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'allavirc2@mail.ru'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [email_address])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def homepage_rus(request):
    template_name = 'index__rus.html'
    return render(request, template_name)

