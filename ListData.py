import arcpy

"""
arcpy.env.workspace = r"D:\LPA"

#Se define una variable donde se encuentran todas las carpetas que posee el workspace principal
wsList = arcpy.ListWorkspaces()

#Se define una lista vacia para almacenar las GDB encontradas
gdbListAll = []

#Se itera sobre cada carpeta buscando los elementos GDB y se almacenan en la lista gdb
for workspace in wsList:
    arcpy.env.workspace = workspace
    # Se listan todos los archivos que dan como resultado un tipo de extension GDB en este caso
    gdbList = arcpy.ListWorkspaces("", "FileGDB")
    # print("{0} contains {1}".format(workspace,gdbList))
    gdbListAll += gdbList
print("List of file geodatabases: \n{0}".format(gdbListAll))

#Se recorre cada GDB encontrada buscando inicialmente los FC, luego los Datasets y luego los FC de cada dataset
for gdb in gdbListAll:
    arcpy.env.workspace = gdb
    print("\nFeature classes in {0}:\n{1}".format(gdb,arcpy.ListFeatureClasses()))
    print("Feature datasets in {0}:\n{1}".format(gdb,arcpy.ListDatasets("","Feature")))
    fdList = arcpy.ListDatasets("","Feature")
    for fd in fdList:
        arcpy.env.workspace = r"{0}\{1}".format(gdb,fd)
        print("\nFeature classes in feature dataset {0} : \n{1}".format(
            arcpy.env.workspace,arcpy.ListFeatureClasses()))

## Se recorre cada gdb y se obtienen todos los archivos de tipo tabla
for gdb in gdbListAll:
    arcpy.env.workspace = gdb
    print("\nTables in {0}:\n{1}".format(gdb,arcpy.ListTables()))

"""

arcpy.env.workspace = r"D:\LPA\Data\Sample.gdb"

## Se recorre cada uno de los FC que estan en el workspace y se imprime cada campo de la tabla con su respectivo tipo de elemento
for tbl in arcpy.ListTables():
    fieldObjectList = arcpy.ListFields(tbl)
    #fieldNameList = [x.name for x in fieldObjectList]
    fieldNameTypeList = [[x.name,x.type] for x in fieldObjectList]
    print("\nFields in {0}\{1}:\n{2}".format(arcpy.env.workspace, tbl,fieldNameTypeList))

print("\nScript completed!")