# we will add tippgeber as "contact-reason" in the regular contactform.
# the Reasons in contactform: "Tippgeber",


from django.forms import ModelForm, forms
from .models import *
from captcha.fields import CaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

# this is the GOOGLE RECAPTCHA Form !


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['topic', 'firstname', 'lastname', 'email',
                  'tel', 'street', 'postialcode', 'city', 'message']
