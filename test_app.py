from app import autenticar_usuario

#CP-01
def test_login_exitoso():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["success"] == True
    assert resultado["message"] == "Acceso concedido"
    assert resultado["response_time_ms"] > 0



#CP-04
def test_usuario_inexistente():
    resultado = autenticar_usuario("pedro", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"
