from django.urls import path, include
from . import views


app_name = 'pages'
urlpatterns = [
    # search for properties and more
    path('search/', views.search, name='search'),

    # company profile / Unternehmensreiter
    path('kontakt/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('career/', views.career, name='career'),
    path('build/', views.build, name='build'),
    path('consulting/', views.consulting, name='consulting'),
    path('service/', views.service, name='service'),

    # service
    path('finanzierung/', views.finance, name='finance'),
    path('ratenkredit/', views.ratenkredit, name='ratenkredit'),

    path('bau/', views.build, name='bau'),
    path('architekt/', views.architekt,
         name='architekt'),
    path('facilitymanagement/', views.facilityManagement,
         name="facilitymanagement"),
    path('winterdienst/', views.winterdienst, name="winterdienst"),
    path('reinigungsdienst/', views.reinigungsdienst, name="reinigungsdienst"),
    path('hausmeisterservice/', views.hausmeisterservice,
         name="hausmeisterservice"),
    path('acceptcookies/', views.accept_cookie, name='acceptcookies'),

    path('tippgeber/', views.tippgeber, name='tippgeber'),
    path('marktanalyse/', views.marketanalysis, name="marktanalyse"),

    path('immobilienbewertung/', views.bewerten, name="bewerten"),
    path('recherche/', views.recherche, name='recherche'),
    path('marketing', views.marketing, name="marketing"),
    path('sanieren/', views.sanieren, name="sanieren"),
    path('bewerten/', views.bewerten, name="bewerten"),
    path('anfrageerhalten/', views.anfrageerhalten, name="anfrageerhalten"),

    # law stuff
    path('impressum/', views.impressum, name="impressum"),
    path('agb/', views.agb, name="agb"),
    path('datenschutz/', views.datasecurity, name="datenschutz"),
    path('widerrufsbelehrung/', views.widerrufsbelehrung,
         name="widerrufsbelehrung"),

    path('projektanbieten/', views.projektanbieten, name='projektanbieten'),
    path('grundstuckanbieten/', views.grundstuckanbieten,
         name='grundstuckanbieten'),
    path('pause/', views.pause, name='pause'),

    #path('404/', views.error_404, name="error404"),
    #path('mail/', views.testmail, name='testmail'),
    # Thats the homescreen
    path('', views.home, name='home'),

]
