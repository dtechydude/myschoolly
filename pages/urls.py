
from django.urls import path
from pages import views as page_views

app_name ='pages'

urlpatterns = [

    # path('demoschool/', page_views.homepage, name='home'),
    path('', page_views.schoolly_home, name='schoolly_home'),
    path('about/', page_views.about, name='about'),
    path('contact/', page_views.contact_us, name='contact'),
    path('frequent-questions/', page_views.faqs, name='faqs'),
    # path('affiliate/', page_views.affiliate, name='affiliate'),
    # path('demo/', page_views.demo, name='demo'),
    # path('pages/', include('pages.urls')),
    
]
