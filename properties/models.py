#from email.mime import image
#from random import choices
#from tabnanny import verbose
#from turtle import distance, turtlesize
#from unittest.util import _MAX_LENGTH
from django.db import models
#from ckeditor.fields import RichTextField
#from multiselectfield import MultiSelectField


class Property(models.Model):

    # gesamtfläche, wohnfläche, nutzfläche, gewerbefläche, anzahl zimmer, hat stellplatz, abstellraum, terrasse, garten, gästewc,

    SALE = 'Verkaufen'
    RENT = 'Vermieten'
    countries = (
        ('Deutschland', 'Deutschland'),
        ('Türkei', 'Türkei'),
    )
    property_types = (
        ('Grundstück', 'Grundstück'),
        ('Einfamilienhaus/Rheinhaus', 'Einfamilienhaus/Rheinhaus'),
        ('Mehrfamilienhaus', 'Mehrfamilienhaus'),
        #('Doppelhauskälfte', 'Doppelhauskälfte'),
        ('Gewerbeobjekt', 'Gewerbeobjekt'),
        ('Gewerbegrundstück', 'Gewerbegrundstück'),
        ('Kapitalanlage', 'Kapitalanlage'),
        ('Neubau', 'Neubau'),
        ('Lagerhallen', 'Lagerhallen'),
    )

    property_plan = (
        (SALE, 'Kaufen'),
        (RENT, 'Mieten')
    )

    # is this property only for business customers ?
    is_gewerblich = models.BooleanField(default=False)

    property_title = models.CharField(
        max_length=220, verbose_name="Titel der Immobilie")
    plan = models.CharField(
        max_length=30, choices=property_plan, default=SALE)
    street = models.CharField(max_length=120, verbose_name="Straße")
    housenumber = models.CharField(max_length=70, verbose_name="Hausnummer")
    postialcode = models.CharField(max_length=70, verbose_name="Postleihzahl")
    city = models.CharField(max_length=120, verbose_name="Stadt")
    country = models.CharField(
        choices=countries, max_length=220, default='Deutschland', verbose_name="Land")
    title_picture = models.ImageField(upload_to='fotos/immo')
    total_area = models.CharField(max_length=60, verbose_name="Gesamtfläche")

    # properties brutto price
    price = models.IntegerField(verbose_name="Preis der Immobilie")
    object_type = models.CharField(
        max_length=60, choices=property_types, verbose_name="Objekttyp")
    # Wohnfläche
    area_to_live = models.CharField(
        max_length=60, verbose_name="Wohnfläche", null=True, blank=True)
    total_ground_size = models.CharField(
        max_length=60, verbose_name="Grundstückgröße", null=True, blank=True)
    area_of_use = models.CharField(
        max_length=60, verbose_name="Nutzfläche", null=True, blank=True)

    amount_of_bedrooms = models.IntegerField(
        null=True, blank=True, verbose_name='Anzahl Schlafzimmer')
    amount_of_rooms = models.IntegerField(
        null=True, blank=True, verbose_name='Anzahl Zimmer')
    amount_of_bathrooms = models.IntegerField(
        null=True, blank=True, verbose_name='Anzahl Badezimmer')
    # Bezugsfrei ab
    available_date = models.DateField(
        null=True, blank=True, verbose_name="Bezugsfrei ab")
    build_in_year = models.CharField(
        max_length=7, blank=True, null=True, verbose_name="Baujahr")
    energypass_available = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Energypass vorhanden")
    # here we should add choices
    energypass_type = models.CharField(max_length=40, null=True, blank=True)

    # some descriptions
    object_description = models.CharField(max_length=2200,
        blank=True, null=True, verbose_name="Objektbeschreibung")
    equipment_description = models.CharField(
        max_length=2200, blank=True, null=True, verbose_name="Beschreibung der Ausstattung")
    location_description = models.CharField(
        max_length=2200,blank=True, null=True, verbose_name="Lagebeschreibung")
    other_description = models.CharField(
        max_length=2200,blank=True, null=True, verbose_name="Sonstige Beschreibung")

    # Some checks, some booleans of the property
    has_keller = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Keller vorhanden?")
    has_balkon = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Balkon vorhanden?")
    has_garage = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Garage/Abstellplatz vorhanden?")

    # What is our purpose with this object
    is_for_selling = models.BooleanField(
        default=True, verbose_name="Ist Objekt zu verkaufen?")
    is_for_renting = models.BooleanField(
        default=False, verbose_name="Ist Objekt zu vermieten?")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Wurde hinzugefügt am")
    is_available = models.BooleanField(
        default=True, verbose_name="Ist Objekt verfügbar?")

    def __str__(self):
        return self.property_title


class Property_images(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fotos/immo')

    def __str__(self):
        return f'Picture number{self.id}'


# for customer who wants to sell their properties. This is anbieten
class PropertyProviders(models.Model):
    #
    GERMANY = 'Deutschland'
    TURKEY = 'Türkei'
    countries = (
        (GERMANY, 'Deutschland'),
        (TURKEY, 'Türkei'),
    )

    FOR_SELLING = "Verkauf"
    FOR_RENT = "Vermieten"

    market_plans = (
        (FOR_SELLING, 'Zum Verkauf'),
        (FOR_RENT, 'Zum Vermieten')
    )

    property_types = (
        ('Grundstück', 'Grundstück'),
        ('Einfamilienhaus', 'Einfamilienhaus'),
        ('Mehrfamilienhaus', 'Mehrfamilienhaus'),
        ('Gewerbeobjekt', 'Gewerbeobjekt'),
        ('Anlageobjekt', 'Anlageobjekt'),
        ('Wohnung', 'Wohnung'),
        ('Lagerhallen', 'Lagerhallen'),
        ('Neubau', 'Neubau'),
        ('Kapitalanlage', 'Kapitalanlage'),

    )

    firstname = models.CharField(max_length=50, verbose_name='Vorname*')
    lastname = models.CharField(max_length=50, verbose_name='Nachname*')
    email = models.EmailField(verbose_name='Email*')
    tel = models.CharField(max_length=50, verbose_name='Telefonnummer*',
                           help_text='Gib deine Telefonnummer hier ein.')
    objecttype = models.CharField(
        max_length=50, choices=property_types, verbose_name='Objektart*')
    market_plan = models.CharField(
        max_length=50, choices=market_plans, default=FOR_SELLING, verbose_name='Objektvorhaben*', blank=True, null=True)
    total_size = models.CharField(
        max_length=30, verbose_name='Wohnfläche in qm', null=True, blank=True)
    living_size = models.CharField(
        max_length=30, verbose_name='Nutzfläche in qm', null=True, blank=True)
    ground_size = models.CharField(
        max_length=30, verbose_name='Grundstückgröße in qm', null=True, blank=True)
    building_year = models.CharField(
        max_length=30, verbose_name='Baujahr')
    street = models.CharField(max_length=90, verbose_name='Straße*')
    housenumber = models.CharField(max_length=50, verbose_name='Hausnummer*')
    postialcode = models.CharField(max_length=50, verbose_name='Postleizahl*')
    city = models.CharField(max_length=90, verbose_name='Stadt*')
    country = models.CharField(
        max_length=70, choices=countries, default=GERMANY, verbose_name='Land')
    notification = models.TextField(
        null=True, blank=True, verbose_name='Sonstiges')

    class Meta:
        db_table = 'neue_immobilien_angebote'
        verbose_name = "Neue Immobilieangebot"
        verbose_name_plural = 'Neue Immobilienangebote'

    def __str__(self):
        return f'{self.firstname}s Immoangebot'


class DetailPropertyInteres(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, verbose_name='Immobilie')
    firstname = models.CharField(max_length=80, verbose_name='Vorname')
    lastname = models.CharField(max_length=80, verbose_name='Nachname')
    email = models.CharField(max_length=80, verbose_name='Email')
    tel = models.CharField(
        max_length=80, verbose_name='Telefonnummer', null=True, blank=True)

    class Meta:
        db_table = 'immobilien_anfragen'

    def __str__(self):
        return f'{self.firstname}s Immo Anfrage'


class SearchOrder(models.Model):
    property_types = (
        ('Grundstück', 'Grundstück'),
        ('Einfamilienhaus', 'Einfamilienhaus'),
        ('Doppelhauskälfte', 'Doppelhauskälfte'),
        ('Gewerbegrundstück', 'Gewerbegrundstück'),
        ('Gewerblich', 'Gewerblich'),
        ('Wohnung', 'Wohnung'),
    )

    DISTANCE_CHOICES = [(i, str(i)) for i in range(0, 100, 10)]

    firstname = models.CharField(max_length=60, verbose_name='Vorname')
    lastname = models.CharField(max_length=60, verbose_name='Nachname')
    email = models.EmailField(verbose_name='Email*')
    tel = models.CharField(max_length=60, verbose_name='Telefon')
    search_for_objecttype = models.CharField(
        choices=property_types, max_length=70, verbose_name='Objekttyp')
    searched_city = models.CharField(max_length=60, verbose_name='Stadt')
    searched_postialcode = models.CharField(
        max_length=60, verbose_name='Postleizahl')
    distance = models.IntegerField(
        choices=DISTANCE_CHOICES, default=DISTANCE_CHOICES[1], verbose_name="Distanzraum in Km")
