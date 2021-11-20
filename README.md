# README #

* Resumen
    * Una aplicacion web en Django con bootstrap, para cargar y pagar boletas
* Version: 1.0
* [Author](https://www.linkedin.com/in/felipenavaslederhos)

### Como instalar la aplicacion? ###

* Instalacion
    * Instalar Python y Django - Se pueden seguir estas guias:
        * https://docs.djangoproject.com/en/3.2/intro/install/#install-python
        * https://developer.mozilla.org/es/docs/Learn/Server-side/Django/development_environment
    * Ingresar a una terminal y navegar hasta la carpeta del proyecto "super_pago", una vez dentro ejecutar:
        * ```py manage.py makemigrations``` -> Crea las migraciones pendientes
        * ```py manage.py migrate``` -> Impacta las migraciones en la base de datos
        * ```py manage.py createsuperuser``` -> Crear el usuario admin (si no funciona en windows ejecutar: ```winpty python manage.py createsuperuser```)

* Como ejecutar la aplicacion?
    * Ingresar a una terminal y navegar hasta la carpeta del proyecto "super_pago", una vez dentro ejecutar:
        * ```py manage.py runserver``` -> Primero tenemos que levantar el servidor
    * Ingresar con un navegador al siguiente URL:
        * http://localhost:8000/
