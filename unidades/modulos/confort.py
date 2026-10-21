def clasificar_temperatura(temperatura: float) -> str:
    """Devuelve una categoría para una temperatura en grados Celsius."""
    if temperatura < 18:
        return "baja"
    if temperatura > 27:
        return "alta"
    return "adecuada"

def es_humedad_adecuada(humedad: float) -> bool:
    """Devuelve un valor dependiendo Informa de si la humedad es adecuada con los parametros 30/65"""
    return 30 <= humedad <= 65

def describir_confort(temperatura: float, humedad: float, sensor_activo: bool) -> str:
    """Comprueba que el sensor este activo para seguir con la funcion, si es así, muestra por pantalla el resultado de ambas funciones"""
    if not sensor_activo:
        return "revisar sensor"
    mensaje_clasificar =  clasificar_temperatura(temperatura)
    respuesta = es_humedad_adecuada(humedad)
    if respuesta:
        mensaje_humedad = "La humedad es adecuada"
    else:
        mensaje_humedad = "La humedad no es adecuada"

    return f"Temperatura: {mensaje_clasificar}\n{mensaje_humedad}"

if __name__ == "__main__":
    mensaje = describir_confort(22.5, 55, True)
    print(mensaje)


