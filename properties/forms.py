
from django.forms import ModelForm
from captcha.fields import CaptchaField

from .models import *


class PropertyProviderForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = PropertyProviders
        fields = ['firstname', 'lastname', 'email', 'tel',
                  'objecttype', 'market_plan', 'total_size', 'street', 'building_year', 'ground_size', 'living_size',
                  'housenumber', 'postialcode', 'city', 'country', 'notification', 'captcha'
                  ]

# user has interest in a property ! We show this in property detail


class DetailPropertyInterestForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = DetailPropertyInteres
        fields = ['property', 'firstname',
                  'lastname', 'email', 'tel', 'captcha']

# kaufen oder mieten fehlt!


class SearchOrderForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = SearchOrder
        fields = ['firstname', 'lastname', 'email', 'tel', 'search_for_objecttype',
                  'searched_city', 'searched_postialcode', 'distance', 'captcha']
