from mimetypes import init
from multiprocessing import context
# html email required stuff
from django.core.mail import EmailMultiAlternatives, BadHeaderError, EmailMessage, send_mail
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# import the settings
from django.conf import settings
#from turtle import title
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from properties.models import *
from .forms import *


"""
this mail function is a notification to NetImmobilien, when someone has sended an form.
The function should tell which form has been send. That save time.



def send_mail_to_employees(whichform,subject, firstname, lastname, email, customerMessage=None, tel=None, market_plan=None, total_size=None, street=None, building_year=None, ground_size=None, living_size=None, housenumber=None, postialcode=None, city=None, objecttype=None, country=None, notification=None):
    # we enter the data that the form includes
    
    context = {
        'whichform': whichform,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'message': customerMessage,
        'tel': tel,
        'objecttype': objecttype,

        'market_plan': market_plan,
        'total_size': total_size,
        'street': street,
        'building_year': building_year,
        'ground_size': ground_size,
        'living_size': living_size,
        'housenumber': housenumber,
        'postialcode': postialcode,
        'city': city,
        'country': country,
        'notification': notification,

    }

    #subject = "Ein Kunde hat geschrieben! Tumuratas Group Website."
    message = render_to_string(
        "mails/mail.html", context
    )
    # print(message)
    striped_message = strip_tags(message)
    #print("we are here 2")
    # HERE IS THE PROBLEM
    #print(settings.TUMURATAS_EMAIL)
    msg = EmailMultiAlternatives(subject, striped_message,
                                 from_email=settings.SERVER_EMAIL, to=[settings.TUMURATAS_EMAIL])
    msg.attach_alternative(message, "text/html")
    # if m == 1, than the message has been successfully sended
    m = msg.send(fail_silently=False)
    print('message is ', m)



    ========================================

    



"""


def accept_cookie(request):
    if request.method == 'POST':
        context = {}
        request.session['cookie_accepted'] = True
        print("confirmed session ? ", request.session['cookie_accepted'])
        request.session.modified = True
        #response = render(request, 'pages/home.html', context)
        return redirect('pages:home')
    else:
        raise Http404







def testmail(request):
    return render(request, 'mails/mail.html')


def tippgeber(request):
    context = {}
    context['cookie_accepted'] = request.session['cookie_accepted']
    return render(request, 'pages/tippgeber.html', context)


def home(request):
    context = {}
    #context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    #print("Home session ? ", request.session.get('cookie_accepted', False))
    return render(request, 'pages/home.html', context)


def finance(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/financing.html', context)


def service(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/service.html', context)


def consulting(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/consulting.html', context)


def architekt(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/architect.html', context)


def career(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/career.html', context)


def aboutus(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/aboutus.html', context)


def contact(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    if request.method == 'POST':
        print("wir haben einen post !")
        contactform = ContactForm(request.POST)
        print("unser contactform", contactform)
        if contactform.is_valid():
            #captcha = contactform.get('captcha')
            print("captcha lautet")
            # request.POST.get('recaptcha_form')
            """

                    if not captcha:
                recaptcha_form = FormWithCaptcha()
                form = ContactForm()
                print("recaptcha error")
                print(captcha)
                context['form'] = form
                context['recaptcha_form'] = recaptcha_form
                context['error_captcha'] = "Du musst den Recaptcha Test bestehen"
                return render(request, 'pages/contact.html', context)
            
            
            """

            c = contactform.save()
            print("wir sind beim kontaktformular", c.id)
            print("wir sind beim kontaktformular", request.POST['firstname'])

            return redirect("pages:anfrageerhalten")
            # now send a mail to tumuratas, so that he can notice that there has arrived a mai
        else:
            errors = contactform.errors
            context['form'] = ContactForm(
                initial={
                    'topic': request.POST['topic'],
                    'firstname': request.POST['firstname'],
                    'lastname': request.POST['lastname'],
                    'email': request.POST['email'],
                    'tel': request.POST['tel'],
                    'street': request.POST['street'],
                    'postialcode': request.POST['postialcode'],
                    'city': request.POST['city'],
                    'message': request.POST['message'],

                }
            )
            context['errors'] = "Sie haben leider falsche Buchstaben eingegeben."
            return render(request, 'pages/contact.html', context)
    else:
        #recaptcha_form = FormWithCaptcha()
        form = ContactForm()
        print(form)
        context['form'] = form
        #context['recaptcha_form'] = recaptcha_form
    return render(request, 'pages/contact.html', context)


def build(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/bau.html', context)


def bewerten(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/bewerten.html', context)


def marketing(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/marketing.html', context)


def sanieren(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/sanieren.html', context)


def recherche(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/recherche.html', context)


def projektanbieten(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/projektanbieten.html', context)


def grundstuckanbieten(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/grundstuckanbieten.html', context)


def marketanalysis(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')
    return render(request, 'pages/marktanalyse.html', context)


def search(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    if 'keyword' in request.POST:
        keyword = request.POST['keyword']
        if keyword:
            pass
    if request.POST:
        searchword = request.POST.cleaned_data['searchword']
        properties = Property.objects.all()
        filtered_properties = properties.filter(title__iexact=searchword)
        context['searched_properties'] = properties
        return render(request, 'pages/search', context)
    else:
        return render(request, 'pages/search.html', context)


# we show this screen before we launch. This is the root url. Change that when we launch
def pause(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/pause.html', context)


def facilityManagement(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/facilitymanagement.html', context)


def winterdienst(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/winterdienst.html', context)


def reinigungsdienst(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/reinigungsdienst.html', context)


def hausmeisterservice(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/hausmeisterservice.html', context)


def ratenkredit(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/ratenkredit.html', context)


# error site


def error_404(request, exception):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/404.html', context)


# form has been send successfully
def anfrageerhalten(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/anfrageerhalten.html', context)


# law stuff
def datasecurity(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/datasecurity.html', context)


def impressum(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/impressum.html', context)


def agb(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/agb.html')


def widerrufsbelehrung(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'pages/widerrufsbelehrung.html')
