"""

Developed By : sumit kumar
facebook : fb.com/sumit.luv
Youtube :youtube.com/lazycoders


"""
from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('search_phone', views.search_view_phone,name='search_phone'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin_products_phone', views.admin_products_view_phone,name='admin-products-phone'),
    path('admin_products_game', views.admin_products_view_game,name='admin-products-game'),
    path('admin_products_part', views.admin_products_view_part,name='admin-products-part'),
    path('admin_products_laptop', views.admin_products_view_laptop,name='admin-products-laptop'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('admin-add-product-phone', views.admin_add_product_view_phone,name='admin-add-product-view-phone'),
    path('admin-add-product-laptop', views.admin_add_product_view_laptop,name='admin-add-product-view-laptop'),
    path('admin-add-product-game', views.admin_add_product_view_game,name='admin-add-product-view-game'),
    path('admin-add-product-part', views.admin_add_product_view_part,name='admin-add-product-view-part'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('delete-product-phone/<int:pk>', views.delete_product_view_phone,name='delete-product-phone'),

    path('update-product/<int:pk>', views.update_product_view,name='update-product'),
    path('update-product-phone/<int:pk>', views.update_product_view_phone,name='update-product-phone'),

    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('admin-view-booking-phone', views.admin_view_booking_view_phone,name='admin-view-booking-phone'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),

    path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('customer-phone', views.customer_home_view_phone,name='customer-phone'),
    path('customer-game', views.customer_home_view_game,name='customer-game'),
    path('customer-laptop', views.customer_home_view_laptop,name='customer-laptop'),
    path('customer-part', views.customer_home_view_part,name='customer-part'),
    path('my-order', views.my_order_view,name='my-order'),
    # path('my-order', views.my_order_view2,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    #path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
   # path('add-to-cart-phone/<int:kk>', views.add_to_cart_view_phone,name='add-to-cart-phone'),
    path('cart', views.cart_view,name='cart'),
    path('cart-phone', views.cart_view_phone,name='cart-phone'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),


]
