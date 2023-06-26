import unittest
from class_carrito import CarritoCompras

class carritodecompras(unittest.TestCase):
    def test_crear_carrito(self):
        carrito = CarritoCompras()
        self.assertEqual(carrito.obtener_cantidad(), 0)
        self.assertEqual(carrito.obtener_total_pagar(), 0)

    def test_crear_carrito2(self):
        carrito = CarritoCompras()
        self.assertFalse(carrito.obtener_cantidad(), 1)
        self.assertEqual(carrito.obtener_total_pagar(), 0)        
    
    def test_agregar_producto(self):
        carrito = CarritoCompras()
        carrito.agregar_producto("SKU001", 2, 150000)
        self.assertEqual(carrito.obtener_cantidad(), 2)
        self.assertEqual(carrito.obtener_total_pagar(), 300000)

    def test_agregar_producto2(self):
        carrito = CarritoCompras()
        carrito.agregar_producto("SKU001", 5, 600)
        carrito.agregar_producto("SKU002", 6, 1500)
        carrito.agregar_producto("SKU003", 1, 2400)
        self.assertEqual(carrito.obtener_cantidad(), 12)
        self.assertEqual(carrito.obtener_total_pagar(), 14400)       
    
    def test_eliminar_producto(self):
        carrito = CarritoCompras()
        carrito.agregar_producto("SKU001", 5, 600)
        carrito.agregar_producto("SKU002", 6, 1500)
        carrito.agregar_producto("SKU003", 1, 2400)
        carrito.eliminar_producto("SKU001", 5, 10)
        self.assertEqual(carrito.obtener_cantidad(), 7)
        self.assertEqual(carrito.obtener_total_pagar(), 11400)
    
    def test_producto_existe(self):
        carrito = CarritoCompras()
        carrito.agregar_producto("SKU001", 5, 600)
        carrito.agregar_producto("SKU002", 1, 1500)
        carrito.agregar_producto("SKU003", 7, 3200)
        self.assertTrue(carrito.producto_existe("SKU001"))
        self.assertTrue(carrito.producto_existe("SKU002"))
        self.assertFalse(carrito.producto_existe("SKU006"))
        self.assertTrue(carrito.producto_existe("SKU003"))
    
    def test_validar_pago_suficiente(self):
        carrito = CarritoCompras()
        carrito.agregar_producto("SKU001", 5, 600)
        self.assertTrue(carrito.validar_pago(3000))
    
    def test_validar_pago_insuficiente(self):
        carrito = CarritoCompras()
        carrito.agregar_producto("SKU001", 5, 600)
        with self.assertRaises(Exception) as context:
            carrito.validar_pago(2500)
            self.assertEqual(str(context.exception), "Error: no tienes dinero suficiente")

if __name__ == '__main__':
    unittest.main()
