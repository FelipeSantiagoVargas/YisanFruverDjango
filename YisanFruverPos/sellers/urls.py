# Django
from django.urls import path

# View
from sellers import views


urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='',
        view=views.HomeView.as_view(),
        name='home'
    ),
    path(
        route='sell/',
        view= views.SellView.as_view(),
        name='sell'
    ),
    path(
        route='add/<int:product_id>/',
        view= views.add_product,
        name='add'
    ),
    path(
        route='delete/<int:product_id>/',
        view= views.delete_product,
        name='delete'
    ),
    path(
        route='save/',
        view= views.save_purchase,
        name='save'
    ),
    path(
        route='ticket/',
        view= views.save_purchase,
        name='ticket'
    ),

]