from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.db.models import Count

from .models import Boleta, Transaccion

from .forms import FormBoleta, FormTransaccion, FiltoFechaForm

def index(request):
    context = {}
    return render(request, 'super_pago_app/index.html', context)

def crear_boleta(request):
    if request.method == "POST":
        form = FormBoleta(request.POST)
        if form.is_valid():
            boleta = form.save(commit=False)
            boleta.save()
            return redirect('detalle_boleta', pk=boleta.pk)
    else:
        form = FormBoleta()
    context = { 'form': form }
    return render(request, 'super_pago_app/crear_boleta.html', context )


def detalle_boleta(request, pk):
    boleta = get_object_or_404(Boleta, pk=pk)

    context = { 'boleta': boleta }
    return render(request, 'super_pago_app/detalle_boleta.html', context )

def pagar_boleta(request):
    if request.method == "POST":
        form = FormTransaccion(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            codigo_barra = transaccion.codigo_barra
            boleta = get_object_or_404(Boleta, codigo_barra=codigo_barra)
            boleta.pago = True
            boleta.save()
            transaccion.save()
            return redirect('detalle_transaccion', pk=transaccion.pk)
    else:
        form = FormTransaccion()
    context = { 'form': form }
    return render(request, 'super_pago_app/crear_transaccion.html', context )
    
def detalle_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)

    context = { 'transaccion': transaccion }
    return render(request, 'super_pago_app/detalle_transaccion.html', context )

def boletas_impagas(request):
    boletas = Boleta.objects.filter(pago__exact=False)
    context = { 'boletas': boletas }
    return render(request, 'super_pago_app/boletas_impagas.html', context )

def boletas_impagas_filtro(request, tipo):
    boletas = Boleta.objects.filter(tipo__exact=tipo, pago__exact=False)
    context = { 'boletas': boletas }
    return render(request, 'super_pago_app/boletas_impagas.html', context )

def listar_pagos(request):
    if request.method == "POST":
        form = FiltoFechaForm(request.POST)
        if form.is_valid():
            fecha_desde = form.cleaned_data.get('fecha_desde')
            fecha_hasta = form.cleaned_data.get('fecha_hasta')

            transacciones = (Transaccion.objects.filter(fecha_pago__lte=fecha_hasta, fecha_pago__gte=fecha_desde)
                .values('fecha_pago')
                .annotate(cantidad=Count('fecha_pago'), suma=Sum('importe'))
                .order_by('fecha_pago')
            )
            context = { 'form': form, 'transacciones': transacciones }
            return render(request, 'super_pago_app/listar_pagos.html', context )
    else:
        form = FiltoFechaForm()
        transacciones = (Transaccion.objects
            .values('fecha_pago')
            .annotate(cantidad=Count('fecha_pago'), suma=Sum('importe'))
            .order_by('fecha_pago')
        )
        context = { 'form': form, 'transacciones': transacciones }
        return render(request, 'super_pago_app/listar_pagos.html', context )
