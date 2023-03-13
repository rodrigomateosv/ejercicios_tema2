import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.a = db.Punto(2, 3)
        self.b = db.Punto(5, 5)
        self.c = db.Punto(-3, -1)
        self.d = db.Punto(0, 0)
        self.rectangulo = db.Rectangulo(self.a, self.b)

    def test_cuadrante(self):
        self.assertEqual(self.a.cuadrante(), "El punto (2,3) pertenece al primer cuadrante")
        self.assertEqual(self.b.cuadrante(), "El punto (5,5) pertenece al primer cuadrante")
        self.assertEqual(self.c.cuadrante(), "El punto (-3,-1) pertenece al tercer cuadrante")
        self.assertEqual(self.d.cuadrante(), "El punto (0,0) está sobre el origen de coordenadas")
    
    def test_vector(self):
        self.assertEqual(self.a.vector(self.b).x, db.Punto(3, 2).x)
        self.assertEqual(self.a.vector(self.b).y, db.Punto(3, 2).y)
        self.assertEqual(self.b.vector(self.a).x, db.Punto(-3, -2).x)
        self.assertEqual(self.b.vector(self.a).y, db.Punto(-3, -2).y)

    def test_vector_str(self):
        self.assertEqual(self.a.vector_str(self.b), "El vector resultante de (2,3) --> (5,5) = (3,2)")
        self.assertEqual(self.b.vector_str(self.a), "El vector resultante de (5,5) --> (2,3) = (-3,-2)")
        self.assertEqual(self.d.vector_str(self.a), "El vector resultante de (0,0) --> (2,3) = (2,3)")

    def test_distancia(self):
        self.assertEqual(self.a.distancia(self.b), 3.605551275463989)
        self.assertEqual(self.b.distancia(self.a), self.a.distancia(self.b))
        self.assertEqual(self.d.distancia(self.a), 3.605551275463989)

    def test_distancia_str(self):
        self.assertEqual(self.a.distancia_str(self.b), "La distancia entre (2,3) y (5,5) = 3.605551275463989")
        self.assertEqual(self.d.distancia_str(self.a), "La distancia entre (0,0) y (2,3) = 3.605551275463989")

    def test_rectangulo(self):
        self.assertEqual(self.rectangulo.base(), 3)
        self.assertEqual(self.rectangulo.altura(), 2)
        self.assertEqual(self.rectangulo.area(), 6)

    def test_rectangulo_str(self):
        self.assertEqual(self.rectangulo.base_str(), "La base del rectángulo formada por los puntos de su diagonal (2,3) y (5,5) es 3")
        self.assertEqual(self.rectangulo.altura_str(), "La altura del rectángulo formada por los puntos de su diagonal (2,3) y (5,5) es 2")
        self.assertEqual(self.rectangulo.area_str(), "El area del rectángulo formada por los puntos de su diagonal (2,3) y (5,5) es 6")

if __name__ == '__main__':
    unittest.main()
