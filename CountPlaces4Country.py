import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r'D:\LPA\Projects\Framework  Project\Framework  Project.gdb'

countryName = arcpy.GetParameterAsText(0)

countryName = 'Colombia'

arcpy.Select_analysis(r'D:\LPA\Data\ne_10m_admin_0_countries.shp',r'D:\LPA\Projects\Framework  Project\Framework  Project.gdb\SelCountry',"NAME = '{0}'".format(countryName))

arcpy.analysis.Buffer("SelCountry","SelCountry_Buffer","200 Kilometers", "FULL", "ROUND", "NONE", None, "PLANAR")

arcpy.analysis.Clip(r'D:\LPA\Data\ne_10m_populated_places.shp', "SelCountry_Buffer","Places_Clip",None)

arcpy.AddMessage('There are {0} populated places in or within 200 km of {1}'.format(arcpy.management.GetCount("Places_Clip"),countryName))