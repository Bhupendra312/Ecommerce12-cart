from django.urls import path
from ecomapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('product',views.product),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cid>',views.catfilter),
    path('sort/<sid>',views.sort),
    path('pricefilter',views.pricefilter),
    path('search',views.search),
    path('product_detail/<pid>',views.product_detail),
    path('addtocart/<pid>',views.addtocart),
    path('cart',views.cart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('remove/<cid>',views.remove),
    path('place_order',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsucess',views.paymentsucess),

    

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)