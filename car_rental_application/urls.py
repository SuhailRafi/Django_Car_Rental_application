from django.contrib import admin
from django.urls import path, include
from systems import urls
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('home', include('systems.urls')), #redirects to systems/url.py
    path ('base/', include('systems.urls')),
    path ('carList/', include('systems.urls')),
    path ('popularCar/', include('systems.urls')),
    path ('availableCar/', include('systems.urls')),
    path ('orderCreate/', include('systems.urls')),
    path ('orderDetails/', include('systems.urls')),
    path ('orderList/', include('systems.urls')),
    path ('forms/', include('systems.urls')),
    path ('carCreate/', include('systems.urls')),
    path ('carDetails/', include('systems.urls')),
    path ('newCar/', include('systems.urls')),
    path ('adminIndex/', include('systems.urls')),
    path ('adminMessage/', include('systems.urls')),
    path ('contact/', include('systems.urls')),
    path ('login/', views.UserLoginForm, name='login'),
    path ('registration/', views.UserRegistrationForm, name='registration')
]