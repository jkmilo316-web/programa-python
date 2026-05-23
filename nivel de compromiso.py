# =====================================================================
# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Solución Básica: Problema 1 - Nivel de Compromiso de Clientes
# =====================================================================

def calcular_compromiso(duracion, clics):
    """
    Módulo (función) encargado de la lógica de negocio para clasificar 
    el nivel de compromiso de una sesión basado en su duración y clics.
    """
    # ✓ Clasificar como "Alto" (si Duración > 180s y Clics > 8)
    if duracion > 180 and clics > 8:
        return "Alto"
    
    # ✓ Clasificar como "Bajo" (si Duración < 60s o Clics < 3)
    elif duracion < 60 or clics < 3:
        return "Bajo"
    
    # ✓ Clasificar como "Medio" en todos los demás casos
    else:
        return "Medio"


def generar_informe_sesiones(matriz_sesiones):
    """
    Módulo encargado de recorrer la matriz de datos, invocar la función
    de cálculo e imprimir el reporte final estructurado.
    """
    print("\n=============================================")
    print("      INFORME DE COMPROMISO DE SESIONES      ")
    print("=============================================")
    print(f"{'ID Cliente':<15}{'Clasificación':<15}")
    print("---------------------------------------------")
    
    # Recorrido de la matriz fila por fila
    for fila in matriz_sesiones:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]
        
        # Invocación del módulo de lógica de negocio
        clasificacion = calcular_compromiso(duracion, clics)
        
        # Salida formateada
        print(f"{id_cliente:<15}{clasificacion:<15}")
        
    print("=============================================\n")


def main():
    """
    Función principal que actúa como punto de entrada del programa.
    Inicializa los datos requeridos.
    """
    # REQ-01: Matriz con datos iniciales (mínimo 5 filas de prueba)
    # Formato: [ID Cliente, Duración (segundos), Eventos Clics]
    banco_datos_sesiones = [
        ["CLI-001", 200, 10],  # Alto (Duración > 180 Y Clics > 8)
        ["CLI-002", 45, 5],    # Bajo (Duración < 60)
        ["CLI-003", 120, 5],   # Medio (Casos restantes)
        ["CLI-004", 150, 1],   # Bajo (Clics < 3)
        ["CLI-005", 300, 9],   # Alto (Duración > 180 Y Clics > 8)
        ["CLI-006", 60, 3]     # Medio (Límite exacto de exclusión)
    ]
    
    # Ejecución del reporte
    generar_informe_sesiones(banco_datos_sesiones)


# Validar que el archivo se ejecute de manera directa
if __name__ == "__main__":
    main()