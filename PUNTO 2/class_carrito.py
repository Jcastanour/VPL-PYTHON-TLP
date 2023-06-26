class CarritoCompras:
    def __init__(self):
        self.productos = {}
        self.total_pagar = 0
    
    def agregar_producto(self, sku, cantidad, precio):
        if sku in self.productos:
            self.productos[sku]['cantidad'] += cantidad
            self.productos[sku]['subtotal'] += cantidad * precio
        else:
            self.productos[sku] = {'cantidad': cantidad, 'subtotal': cantidad * precio}
        self.total_pagar += cantidad * precio
    
    def eliminar_producto(self, sku, cantidad, precio):
        if sku in self.productos:
            if cantidad >= self.productos[sku]['cantidad']:
                self.total_pagar -= self.productos[sku]['subtotal']
                del self.productos[sku]
            else:
                self.productos[sku]['cantidad'] -= cantidad
                self.productos[sku]['subtotal'] -= cantidad * precio
                self.total_pagar -= cantidad * precio
    
    def obtener_cantidad(self):
        return sum([producto['cantidad'] for producto in self.productos.values()])
    
    def obtener_total_pagar(self):
        return self.total_pagar
    
    def producto_existe(self, sku):
        return sku in self.productos
    
    def validar_pago(self, presupuesto):
        if presupuesto >= self.total_pagar:
            return True
        else:
            raise Exception("Error: no tienes dinero suficiente")





