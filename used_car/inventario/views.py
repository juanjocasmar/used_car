from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo
from django.db.models import Sum

# Create your views here.
def lista_vehiculos(request):
    marca_filtro = request.GET.get('marca', '')
    vehiculos = Vehiculo.objects.all()
    if marca_filtro:
        vehiculos = vehiculos.filter(marca__icontains=marca_filtro)
    return render(request, 'inventario/lista_vehiculos.html', {'vehiculos': vehiculos})

def registrar_vehiculo(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        anio = request.POST.get('anio')
        precio_compra = request.POST.get('precio_compra')

        # Verificar que los valores no estén vacíos
        if not marca or not modelo or not anio or not precio_compra:
            return render(request, 'inventario/registrar_vehiculo.html', {'error': 'Todos los campos son obligatorios'})

        # Guardar el vehículo en la base de datos
        Vehiculo.objects.create(
            marca=marca,
            modelo=modelo,
            anio=int(anio),
            precio_compra=float(precio_compra)
        )

        return redirect('lista_vehiculos')

    return render(request, 'inventario/registrar_vehiculo.html')

def cambiar_estado(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.estado = 'Vendido'
    vehiculo.save()
    return redirect('lista_vehiculos')

def reporte_ventas(request):
    # Filtrar solo los vehículos vendidos
    vehiculos_vendidos = Vehiculo.objects.filter(estado="Vendido")

    # Calcular compras y ventas solo sobre los vendidos
    total_compras = vehiculos_vendidos.aggregate(total=Sum("precio_compra"))["total"] or 0
    total_ventas = vehiculos_vendidos.aggregate(total=Sum("precio_venta"))["total"] or 0
    total_utilidad = total_ventas - total_compras  # La utilidad es la diferencia

    return render(request, 'inventario/reporte.html', {
        "total_compras": total_compras,
        "total_ventas": total_ventas,
        "total_utilidad": total_utilidad
    })

def home(request):
    return render(request, 'inventario/base.html')