import arcpy

"""
dataElement = r"D:\LPA\Data\Sample.gdb"

desc = arcpy.Describe(dataElement)

print("Describing {0}...".format(dataElement))
print("Name:         "+ desc.name)
print("Datatype:     "+ desc.Datatype)
print("CatalogPath:  "+ desc.catalogPath)
print("Children:")
print()
for child in desc.children:
    if child.datatype == "FeatureDataset":
        pass
    else:
        if hasattr(child, "shapeType"):
            print("    {0} is a {1} of shapeType {2}".format(
                child.name, child.datatype,child.shapeType))
            print("    with Extent: {0}".format(child.extent))
        else:
            print("    {0} is a {1}".format(child.name,child.datatype))
        print("      and Fields:")
        for field in child.fields:
            print("      {0} of type {1}".format(field.name, field.type))
"""

dataElement = r"D:\LPA\Data\Sample.gdb"
descDictionary = arcpy.da.Describe(dataElement)

for i,key in enumerate(descDictionary):
    print("{0}.{1}:{2}".format(i+1, key,descDictionary[key]))
print(descDictionary)


print("\nScript completed")