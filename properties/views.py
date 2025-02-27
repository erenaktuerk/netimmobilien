from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.mail import EmailMultiAlternatives, BadHeaderError, EmailMessage, send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pages.forms import *



"""

def send_searchorder_email(firstname, lastname, email, tel, search_for_objecttype, searched_city, searched_postialcode, distance):
    # we enter the data that the form includes
    context = {
        'whichform': 'Neuer Suchauftrag',
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'search_for_objecttype': search_for_objecttype,
        'tel': tel,

        'searched_city': searched_city,
        'searched_postialcode': searched_postialcode,
        'distance': distance,
    }
    subject = "Neuer Suchauftrag"
    message = render_to_string(
        "mails/mail.html", context
    )
    striped_message = strip_tags(message)
    #print("we are here 2")
    # HERE IS THE PROBLEM
    print(settings.TUMURATAS_EMAIL)
    msg = EmailMultiAlternatives(subject, striped_message,
                                 from_email=settings.SERVER_EMAIL, to=[settings.TUMURATAS_EMAIL])
    msg.attach_alternative(message, "text/html")
    # if m == 1, than the message has been successfully sended
    m = msg.send(fail_silently=False)
    print('message is ', m)



"""


def properties(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    properties = Property.objects.all()
    filter_objecttype = Property.objects.values_list(
        'object_type', flat=True).distinct()
    filter_city = Property.objects.values_list('city', flat=True).distinct()
    filter_country = Property.objects.values_list(
        'country', flat=True).distinct()
    filter_propertyplan = Property.objects.values_list(
        'plan', flat=True).distinct()

    context['properties'] = properties
    context['filter_objecttype'] = filter_objecttype
    context['city'] = filter_city
    context['filter_country'] = filter_country
    context['filter_plan'] = filter_propertyplan
    # if the user wants to filter the properties
    if request.POST:
        objecttype_filterword = request.POST['objecttype']
        city_filterword = request.POST['city']
        country_filterword = request.POST['country']
        plan_filterword = request.POST['plan']

        print('objecttype is ', objecttype_filterword)
        print('city is ', city_filterword)
        print('country is ', country_filterword)

        all_properties = Property.objects.all()

        # filter after the objecttype
        if not objecttype_filterword == 'all':
            all_properties = all_properties.filter(
                object_type__iexact=objecttype_filterword)
        if not plan_filterword == 'all':
            all_properties = all_properties.filter(
                plan__iexact=plan_filterword)
        if not city_filterword == 'all':
            all_properties = all_properties.filter(
                city__iexact=city_filterword)
        if not country_filterword == 'all':
            all_properties = all_properties.filter(
                country__iexact=country_filterword)

        for i in all_properties:
            print('after property filter we got ', i)
        context['properties'] = all_properties
        if len(all_properties) > 0:
            context['properties_are_available'] = True

        return render(request, 'properties/properties.html', context)

    if len(properties) > 0:
        context['properties_are_available'] = True
    return render(request, 'properties/properties.html', context)


def property_detail(request, id):
    context = {}

    if request.method == 'POST':
        # we save the interest for the property, so that we contact back after a while
        form = DetailPropertyInterestForm(request.POST)
        print(form.errors)
        if form.is_valid():
            #captcha = request.POST.get('recaptcha_form')
            """
            if not captcha:
                #recaptcha_form = FormWithCaptcha()

                # we print the same site again
                property_item = get_object_or_404(Property, id=id)
                property_pics = Property_images.objects.filter(property__id=id)
                print('our property pics are: ', property_pics)
                context = {'property': property_item, 'pics': property_pics}
                form = DetailPropertyInterestForm(
                    initial={
                        'property': property_item
                    }
                )
                context['form'] = form
                context['recaptcha_form'] = recaptcha_form
                return render(request, 'pages/contact.html', context)
            """

            form.save()
            # here we send notification to employees
            return redirect("pages:anfrageerhalten")

        else:
            property_item = get_object_or_404(Property, id=id)
            property_pics = Property_images.objects.filter(property__id=id)
            print('our property pics are: ', property_pics)
            context = {'property': property_item, 'pics': property_pics}
            form = DetailPropertyInterestForm(
                initial={
                    'property': property_item,
                    'firstname': request.POST['firstname'],
                    'lastname': request.POST['lastname'],
                    'email': request.POST['email'],
                    'tel': request.POST['tel'],

                }
            )
            context['form'] = form
            errors = form.errors

            context['errors'] = "Sie haben leider falsche Buchstaben eingegeben."
            return render(request, 'properties/propertydetail.html', context)

    property_item = get_object_or_404(Property, id=id)
    property_pics = Property_images.objects.filter(property__id=id)
    context = {'property': property_item, 'pics': property_pics}
    form = DetailPropertyInterestForm(
        initial={
            'property': property_item
        }

    )
    print(form)
    context['form'] = form
    #context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    #recaptcha_form = FormWithCaptcha()
    #context['recaptcha_form'] = recaptcha_form

    return render(request, 'properties/propertydetail.html', context)

# how clients show interest for an specified property


"""
def property_interest_detail(request):
    if not request.method == 'POST':
        raise Http404
    else:
        form = DetailPropertyInterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:anfrageerhalten')
"""


def immoAnbieten(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    if request.method == 'POST':
        form = PropertyProviderForm(request.POST)

        if form.is_valid():
            #captcha = request.POST.get('recaptcha_form')
            """
            if not captcha:
                recaptcha_form = FormWithCaptcha()
                form = PropertyProviderForm()
                context['form'] = form
                context['recaptcha_form'] = recaptcha_form
                return render(request, 'pages/contact.html', context)
            """

            offer = form.save()
            # send an email here
            return redirect('pages:anfrageerhalten')
        else:
            #errors = form.errors
            form = PropertyProviderForm(
                initial={
                    'firstname': request.POST['firstname'],
                    'lastname': request.POST['lastname'],
                    'email': request.POST['email'],
                    'tel': request.POST['tel'],
                    'objecttype': request.POST['objecttype'],
                    'market_plan': request.POST['market_plan'],
                    'total_size': request.POST['total_size'],
                    'street': request.POST['street'],
                    'building_year': request.POST['building_year'],
                    'living_size': request.POST['living_size'],
                    'ground_size': request.POST['ground_size'],
                    'housenumber': request.POST['housenumber'],
                    'postialcode': request.POST['postialcode'],
                    'city': request.POST['city'],
                    'country': request.POST['country'],
                    'housenumber': request.POST['housenumber'],
                    'notification': request.POST['notification'],
                }
            )
            context['form'] = form

            context['errors'] = "Sie haben leider falsche Buchstaben eingegeben."
            return render(request, 'properties/immoAnbieten.html', context)

    context['form'] = PropertyProviderForm()
    #recaptcha_form = FormWithCaptcha()
    #context['recaptcha_form'] = recaptcha_form
    return render(request, 'properties/immoAnbieten.html', context)


def searchOrder(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    if request.method == 'POST':
        form = SearchOrderForm(request.POST)
        print("we are here p1")
        if form.is_valid():
            """

            captcha = request.POST.get('recaptcha_form')
            if not captcha:
                recaptcha_form = FormWithCaptcha()
                form = SearchOrderForm()
                context['form'] = form
                context['recaptcha_form'] = recaptcha_form
                return render(request, 'pages/contact.html', context)
                """
            form.save()
            return redirect('pages:anfrageerhalten')
        else:
            print("not valid")
            print(form.errors)
            #errors = form.errors
            context['form'] = SearchOrderForm(
                initial={
                    'firstname': request.POST['firstname'],
                    'lastname': request.POST['lastname'],
                    'email': request.POST['email'],
                    'tel': request.POST['tel'],
                    'search_for_objecttype': request.POST['search_for_objecttype'],
                    'searched_city': request.POST['searched_city'],
                    'searched_postialcode': request.POST['searched_postialcode'],
                    'distance': request.POST['distance'],

                }
            )
            context['errors'] = "Sie haben leider falsche Buchstaben eingegeben."
            return render(request, 'pages/searchorder.html', context)
    else:
        form = SearchOrderForm()
        #recaptcha_form = FormWithCaptcha()
        #context['recaptcha_form'] = recaptcha_form
        context['form'] = form
    return render(request, 'pages/searchorder.html', context)


def immobilienverrentung(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'properties/immobilienverrentung.html', context)


def immobilienpflege(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'properties/immobilienpflege.html', context)


def immoausland(request):
    context = {}
    context['cookie_accepted'] = request.session.get('cookie_accepted', '')

    return render(request, 'properties/immoausland.html', context)
