import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

# Sobrescribir los archivos salientes
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\LPA\Data\Sample.gdb"

# fc = r"D:\LPA\Data\ne_10m_admin_0_countries.shp"
fc = arcpy.GetParameterAsText(0)

if fc == "":
    fc = r"D:\LPA\Data\ne_10m_admin_0_countries.shp"

numFeats = arcpy.GetCount_management(fc)

print_message("{0} has {1} feature(s)".format(fc, numFeats))

##arcpy.CreateFileGDB_management(r"D:\LPA\Data", "Sample")

##arcpy.Select_analysis(fc, "Spain", "NAME = 'Spain'")

print("Script successful")
