import unittest
import app

class TestApp(unittest.TestCase):

    def test_add_interesado(self):
        json_test = {"nombres": "jose", "correo": "joseguzman@upeu.edu.pe",
                    "status": 200, "mensaje": "Gracias por registrarse"}
        self.assertDictEqual(app.validarDatos("jose", "joseguzman@upeu.edu.pe"), json_test)

    def test_validated_name(self):
        json_test = {"nombres": "", "correo": "joseguzman@upeu.edu.pe",
                    "status": 400, "mensaje": "Ingrese su nombre"}
        self.assertDictEqual(app.validarDatos("", "joseguzman@upeu.edu.pe"), json_test)

    def test_validated_mail(self):
        json_test = {"nombres": "jose", "correo": "",
                    "status": 400, "mensaje": "Ingrese su correo"}
        self.assertDictEqual(app.validarDatos("jose", ""), json_test)

    def test_validated_send_mail(self):
        json_test = {"nombres": "jose", "correo": "",
                    "status": 400, "mensaje": "Ingrese su correo12"}
        self.assertDictEqual(app.validarDatos("jose", ""), json_test)

    if __name__ == "__main__":
        unittest.main()