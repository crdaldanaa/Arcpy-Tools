import arcpy
import math

# Configurar el entorno de trabajo
arcpy.env.workspace = r"D:\OneDrive\02_Carbon Market\03_Work\01_ALLCOT\07_Sembrando Futuro\Capas"
arcpy.env.overwriteOutput = True

points = arcpy.management.FeatureToPoint(
    in_features= r"AP_Finales.shp",
    out_feature_class= "CenterPoints_AP",
    point_location="CENTROID"
)

# Obtener los puntos como una lista de coordenadas
puntos_list = []
with arcpy.da.SearchCursor(points, ["OID@", "SHAPE@XY"]) as cursor:
    for row in cursor:
        puntos_list.append((row[0], row[1]))

# Crear la tabla de salida
output_table = arcpy.management.CreateTable(arcpy.env.workspace, "distancias.dbf")

# Agregar campos a la tabla de salida
arcpy.management.AddField(output_table, "FromID", "LONG")
arcpy.management.AddField(output_table, "ToID", "LONG")
arcpy.management.AddField(output_table, "Distance", "DOUBLE")

# Insertar los cálculos de distancia en la tabla de salida
with arcpy.da.InsertCursor(output_table, ["FromID", "ToID", "Distance"]) as cursor:
    for i, (from_id, (x1, y1)) in enumerate(puntos_list):
        for j, (to_id, (x2, y2)) in enumerate(puntos_list):
            if from_id != to_id:
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                cursor.insertRow((from_id, to_id, distance))

print("Distancias calculadas y guardadas en", output_table)