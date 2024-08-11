import arcpy

def formatSQLIN(dataList, sqlTemplate):
    'a function to generate a SQL statement'
    sql = sqlTemplate #"OBJECTID IN "
    step = "("
    for data in dataList:
        step += str(data)
    sql += step + ")"
    return sql

def formatSQL(dataList, sqlTemplate):
    'a function to generate a SQL statement'
    sql = ''
    for count, data in enumerate(dataList):
        if count != len(dataList)-1:
            sql += sqlTemplate.format(data) + ' OR '
        else:
            sql += sqlTemplate.format(data)
    return sql

## Función para obtener un listado de caracteristicas con una condición SQL
def formatSQL2(dataList, sqlTemplate, operator=" OR "):
    'a function to generate a SQL statement'
    sql = ''
    for count, data in enumerate(dataList):
        if count != len(dataList)-1:
            sql += sqlTemplate.format(data) + operator
        else:
            sql += sqlTemplate.format(data)
    return sql
'''
El asterisco entra en una tupla

## SQL con múltiples condiciones
def formatSQLMultiple(dataList, sqlTemplate, operator=" OR "):
    'a function to generate a SQL statement'
    sql = ''
    for count, data in enumerate(dataList):
        if count != len(dataList)-1:
            sql += sqlTemplate.format(*data) + operator
        else:
            sql += sqlTemplate.format(*data)
    return sql

sqlTemplate = "(NAME = '{0}' AND BUS_SIGNAG = '{1}')"
lineNames = [('71 IB', 'Ferry Plaza'),('71 OB','48th Avenue')]
sql = formatSQLMultiple(lineNames, sqlTemplate)
'''