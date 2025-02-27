from django.db import models


class Contact(models.Model):
    IMMOBILIEN_ANBIETEN = 0
    IMMOBILIEN = 1
    BAU = 2
    FINANZIERUNG = 3
    PROJEKTENTWICKLUNG = 4
    CONSULTING = 5
    TIPPGEBER_VERTRAG = 6
    KARRIERE = 7
    SUCHAUFTRAG = 8
    SONSTIGES = 9

    topics = (
        (IMMOBILIEN_ANBIETEN, 'Immobilien anbieten'),
        (IMMOBILIEN, 'Immobilien'),
        (BAU, 'Bau'),
        (FINANZIERUNG, 'Finanzierung'),
        (PROJEKTENTWICKLUNG, 'Projektentwicklung'),
        (CONSULTING, 'Consulting'),
        (TIPPGEBER_VERTRAG, 'Tippgeber werden bei der Tumuratas Group'),
        (KARRIERE, 'Karriere'),
        (SUCHAUFTRAG, 'Suchauftrag für Immobilien und Projekte'),
        (SONSTIGES, 'Sonstiges')
    )

    topic = models.IntegerField(
        default=0, choices=topics, verbose_name='Anliegen')
    firstname = models.CharField(max_length=100, verbose_name='Vorname*')
    lastname = models.CharField(max_length=100, verbose_name='Nachname*')
    email = models.EmailField(verbose_name='Email*')
    tel = models.CharField(max_length=26, null=True,
                           blank=True, verbose_name='Telefonnummer*')
    street = models.CharField(max_length=80, null=True,
                              blank=True, verbose_name="Straße")
    postialcode = models.CharField(
        max_length=80, null=True, blank=True, verbose_name="Postleizahl")
    city = models.CharField(max_length=80, null=True,
                            blank=True, verbose_name="Stadt")

    message = models.TextField(verbose_name='Nachricht')
    inquiry_send_at_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Datum')
    checked = models.BooleanField(default=False, verbose_name='Bearbeitet?')

    def __str__():
        return f'{self.firstname}s contact'
