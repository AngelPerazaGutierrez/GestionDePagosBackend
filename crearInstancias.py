from sqlalchemy import Date, func
from GestionDePagosBackend.models.banco_model import Banco
from GestionDePagosBackend.models.cp_model import Cp
from GestionDePagosBackend.models.empresa_model import Empresa
from GestionDePagosBackend.models.usuario_model import Usuario

#instancias para ser llamadas en la sesion y estas a si vez se crearan en la db segun la tabla.

nuevo_usuario = Usuario(
    cedula=808080800,
    nombre="creado desde Test",
    apellido="Test",
    email="test@gmail.com",
    password="1234567890",
    fecha_creacion=func.now(),
    proceso="Nomina"
)


nueva_empresa = Empresa(
    nit=909080809,
    nombre_empresa="empresaTest",
    tipo_cuenta1="Ahorros",
    nombre_banco1="Banco Test",
    numero_cuenta1=78906543211,
    ciudad="Bogota"
)


nuevo_comprobante = Cp(
    adjuntos="text.txt",
    fecha=func.now(),
    ciudad="Bogota",
    nit=808080800,
    tercero="testEmpresa",
    concepto="TestConcepto",
    banco="TestBanco",
    tipo_cuenta="Ahorros",
    numero_cuenta=123456789,
    valor=1234567890
)


nuevo_banco = Banco(
    nit=909090909,
    tipo_cuenta="Corriente",
    nombre_banco="BancoTest"
)