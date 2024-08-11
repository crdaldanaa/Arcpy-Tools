import arcpy

workspace = r"D:\LPA\Data"

datalist = []

for dirpath, dirnames, filenames in arcpy.da.Walk(workspace, datatype="FeatureClass", type=["Point","Polygon"]):
    for filename in filenames:
        datalist.append(r"{0}\{1}".format(dirpath,filename))
print(datalist)
print("\nFound {0} data elements in {1}".format(len(datalist),workspace))
print("\nScript completed!")