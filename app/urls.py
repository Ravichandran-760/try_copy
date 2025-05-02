from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,products,cart, login ,details,register,order,submit_order
from . import views

app_name='app'
urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),   
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('detail/<int:Shirtid>/', details, name='details'),
    path("register/", register, name="register"),
    path('order/', views.order, name='order'),
    path('submit-order/', views.submit_order, name='submit_order'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)