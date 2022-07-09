from django.urls import path
from .views import index, login, carrito, pagoapropiado, registrarusuario, contacto, menusemanal,form_del_menu, modificar_menu, repartidores, FichaEnsalada, FichaInternacional, FichaMariscos, FichaPlatilloDia, FichaPlatillosPrincipales, FichaPostres, FichaSopas, FichaVeganos, Ensalada, Internacional, Mariscos, PlatilloDia, PlatillosPrincipales, Postres, Sopas, Veganos

urlpatterns = [
    path('', index,name="index"),
    path('login',login,name="login"),
    path('carrito',carrito,name="carrito"),
    path('pago-apropiado',pagoapropiado,name="pagoapropiado"),
    path('registrar-usuario',registrarusuario,name="registrarusuario"),
    path('contacto',contacto,name="contacto"),
    path('menu-semanal',menusemanal,name="menusemanal"),
    path('form-del-menu/<id>', form_del_menu,name="form_del_menu"),
    path('modificar-menu/<id>',modificar_menu,name="modificar_menu"),
    path('repartidores',repartidores,name="repartidores"),
    path('Ficha-Ensalada',FichaEnsalada,name="fichaEnsalada"),
    path('Ficha-Internacional',FichaInternacional,name="fichaInternacional"),
    path('Ficha-Mariscos',FichaMariscos,name="FichaMariscos"),
    path('Ficha-Platillo_Dia',FichaPlatilloDia,name=("FichaDia")),
    path('Ficha-Platillos_Principales',FichaPlatillosPrincipales,name="FichaPrincipales"),
    path('Ficha-Postres',FichaPostres,name=("FichaPostre")),
    path('Ficha-Sopas',FichaSopas,name="FichaSopa"),
    path('Ficha-Veganos',FichaVeganos,name="FichaVegano"),
    path('Ensalada',Ensalada,name="Ensalada"),
    path('Internacional',Internacional,name="Internacional"),
    path('Mariscos',Mariscos,name="Mariscos"),
    path('Platillo-Dia',PlatilloDia,name="PlatilloDia"),
    path('Platillo-Principales',PlatillosPrincipales,name="Principales"),
    path('Postres',Postres,name="Postres"),
    path('Sopas',Sopas,name="Sopas"),
    path('Veganos',Veganos,name="Veganos"),
]