def saludar(nombre="Mundo"):
    return f"Hola, {nombre}!"

def test_saludar():
    assert saludar("Mundo") == "Hola, Mundo!"
