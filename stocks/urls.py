from django.urls import path

from .views import (
    home_view,
    about_view,
    avatar_view,
    detail_product_view,
    list_product_view,
    search_product_with_form_view,
    create_product_with_form_view,
    create_client_with_form_view,
    detail_client_view,
    client_list_view,
    client_delete_view,
    client_update_view,
    search_client_view,
    office_list_view,
    create_office_with_form_view,
    detail_office_view,
    search_office_view,
    office_delete_view,
    delete_product_view,
    office_update_view,
    update_product_view,
    user_login_view,
    user_logout_view,
    user_creation_view,
    error_page,
    
    
    
)

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path('avatar/create/', avatar_view, name='avatar_create'),
    path("login/", user_login_view, name= "login"),
    path("logout/", user_logout_view, name= "logout"),
    path("registro/", user_creation_view, name="user-create"),
    path("list/", list_product_view, name="product-list"),
    path("buscar-con-formulario/", search_product_with_form_view, name="product-search"),
    path("crear-producto-con-formulario/", create_product_with_form_view, name="product-create"),
    path("producto/detail/<producto_id>", detail_product_view, name="product-detail"),
    path("producto/delete/<producto_id>", delete_product_view, name="product-delete"),
    path("producto/update/<producto_id>", update_product_view, name="product-update"),
    path("cliente/create/", create_client_with_form_view, name="client-create"),
    path("cliente/detail/<cliente_id>", detail_client_view, name="client-detail"),
    path("cliente/list/", client_list_view, name="client-list"),
    path("cliente/delete/<cliente_id>", client_delete_view, name="client-delete"),
    path("cliente/update/<cliente_id>", client_update_view, name="client-update"),
    path("cliente/buscar/", search_client_view, name="client-search"),
    path("sucursal/list/", office_list_view, name="office-list"),
    path("sucursal/create/", create_office_with_form_view, name="office-create"),
    path("sucursal/detail/<sucursal_id>", detail_office_view, name="office-detail"),
    path("sucursal/buscar/", search_office_view, name="office-search"),
    path("sucursal/delete/<sucursal_id>", office_delete_view, name="office-delete"),
    path("sucursal/update/<sucursal_id>", office_update_view, name="office-update"),
    path('error/', error_page, name='error_page'),
    

]