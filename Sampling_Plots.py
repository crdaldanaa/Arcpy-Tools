"""
Script documentation
- Tool parameters are accessed using arcpy.GetParameter() or 
                                     arcpy.GetParameterAsText()
- Update derived parameter values using arcpy.SetParameter() or
                                        arcpy.SetParameterAsText()
"""
import arcpy
import random


def script_tool(param0, param1, param2, param3):
    # Obtener el tipo de muestreo del usuario (aleatorio o sistemático)
    muestreo = param3

    # Obtener la ruta de salida del shapefile
    out_file = param2

    # Obtener el número de muestras a seleccionar
    n_muestras = int(param1)

    # Obtener la capa de entrada (la capa de la que se realizará el muestreo)
    capa_entrada = param0

    # Definir la función para el muestreo aleatorio
    def muestreo_aleatorio(capa_entrada, n_muestras, out_file):
        # Realizar la selección aleatoria
        total_registros = int(
            arcpy.GetCount_management(capa_entrada).getOutput(0))
        # Generar una lista de números aleatorios únicos entre 1 y el número total de entidades
        indices_aleatorios = random.sample(
            range(1, total_registros + 1), n_muestras)

        # Convertir los índices aleatorios en una cadena separada por comas para usar en la expresión de selección
        indices_str = ','.join(map(str, indices_aleatorios))

        # Crear una expresión de selección basada en los índices aleatorios
        expresion_seleccion = "{} IN ({})".format(arcpy.AddFieldDelimiters(
            capa_entrada, arcpy.Describe(capa_entrada).OIDFieldName), indices_str)

        # Seleccionar las entidades en la capa de entrada basadas en la expresión de selección
        arcpy.Select_analysis(capa_entrada, out_file, expresion_seleccion)

    def seleccionar_punto_aleatorio(capa_entrada):
        # Obtener el número total de puntos
        total_puntos = int(arcpy.GetCount_management(
            capa_entrada).getOutput(0))
        # Seleccionar un índice aleatorio
        # Evita el primer punto que seleccionamos al azar
        indice_aleatorio = random.randint(0, total_puntos-1)
        # Seleccionar el punto aleatorio
        with arcpy.da.SearchCursor(capa_entrada, ["FID", "SHAPE@"], sql_clause=(None, f"ORDER BY FID")) as cursor:
            for i, row in enumerate(cursor):
                if i == indice_aleatorio:
                    punto_inicial = row[0]
                    break
        return punto_inicial

    def muestreo_sistematico(capa_entrada, n_muestras, out_file):
        # Seleccionar un punto aleatorio inicial
        punto_inicial = seleccionar_punto_aleatorio(capa_entrada)

        # Calcular el tamaño del intervalo para el muestreo sistemático
        total_registros = int(
            arcpy.GetCount_management(capa_entrada).getOutput(0))
        intervalo = (total_registros - 1) // n_muestras

        # Crear una consulta SQL para seleccionar los puntos sistemáticamente
        sql = "MOD(FID - {}, {}) = 0".format(punto_inicial, intervalo)

        # Realizar la selección sistemática
        arcpy.Select_analysis(capa_entrada, out_file, sql)

    # Realizar el muestreo según la selección del usuario
    if muestreo == 'Aleatorio':
        muestreo_aleatorio(capa_entrada, n_muestras, out_file)
    elif muestreo == 'Sistematico':
        muestreo_sistematico(capa_entrada, n_muestras, out_file)


if __name__ == "__main__":
    param0 = arcpy.GetParameter(0)
    param1 = arcpy.GetParameter(1)
    param2 = arcpy.GetParameter(2)
    param3 = arcpy.GetParameter(3)
    script_tool(param0, param1, param2, param3)
