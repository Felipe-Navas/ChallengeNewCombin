from django.contrib import admin

from .models import Boleta, Transaccion

admin.site.register(Boleta)
admin.site.register(Transaccion)