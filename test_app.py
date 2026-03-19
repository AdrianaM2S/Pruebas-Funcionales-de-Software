import time
from app import autenticar_usuario

#CP-01
def test_login_exitoso():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["success"] == True
    assert resultado["message"] == "Acceso concedido"
    assert resultado["response_time_ms"] > 0
    
#CP-02
def test_usuario_vacio():
    resultado = autenticar_usuario("", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"
    assert resultado["response_time_ms"] > 0

#CP-03
def test_contrasena_vacia():
    resultado = autenticar_usuario("admin", "")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"
    assert resultado["response_time_ms"] > 0

#CP-04
def test_usuario_inexistente():
    resultado = autenticar_usuario("pedro", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"
    assert resultado["response_time_ms"] > 0

#CP-05
def test_contrasena_incorrecta():
    resultado = autenticar_usuario("admin", "9999")
    assert resultado["success"] == False
    assert resultado["message"] == "Contraseña incorrecta"
    assert resultado["response_time_ms"] > 0

#CP-06
def test_tiempo_respuesta_login_exitoso():
    inicio = time.perf_counter()
    resultado = autenticar_usuario("admin", "1234")
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    assert resultado["success"] == True
    assert tiempo_ms < 500

#CP-07
def test_estructura_salida():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["success"] == True
    assert resultado["message"] == "Acceso concedido"
    assert resultado["response_time_ms"] > 0

#CP-Extra-01
def test_usuario_contrasena_vacia():
    resultado = autenticar_usuario("", "")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"
    assert resultado["response_time_ms"] > 0

#CP-Extra-02
def test_usuario_mayuscula():
    resultado = autenticar_usuario("Admin", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"
    assert resultado["response_time_ms"] > 0

#CP-Extra-03
def test_usuario_caracter_especial():
    resultado = autenticar_usuario("@dm!n", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"
    assert resultado["response_time_ms"] > 0

#CP-Extra-04
def test_contrasena_caracter_especial():
    resultado = autenticar_usuario("admin", "!23?")
    assert resultado["success"] == False
    assert resultado["message"] == "Contraseña incorrecta"
    assert resultado["response_time_ms"] > 0

#CP-Extra-05
def test_usuario_contrasena_caracter_especial():
    resultado = autenticar_usuario("@dm!n", "!23?")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"
    assert resultado["response_time_ms"] > 0

#Prueba adicional de tiempo reportado por el sistema
def test_tiempo_reportado():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["response_time_ms"] < 500
