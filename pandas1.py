import pandas as pd
import numpy as np
datos={'Nombre':[np.nan,'Yenny','Nicole'],
       'Calificaciones':['70','90','80'],
       'Materias': ['Cálculo','Física','Materiales II'] }
df=pd.DataFrame(datos)
print (df)
print ('\n'*2) #Deja dos espacios
#Para datos no válidos uso pd.nan o ‘N/A’
#Muestra la inf. general de la tabla
print (df.info()) 
print ('\n'*2)
#Reemplaza variables
nuevo=df.replace('Yenny',"nadie")
print (nuevo)
print ('\n'*3)
#Estadística básica
print (df.describe())
print ('\n')
#Eliminar filas que no tienen datos (np.nan)
filas=pd.DataFrame(datos)
filas.dropna(how='any',inplace=True)
print(filas)
print ('\n')
#Eliminar registro buscando por columna 
columna=df[df['Calificaciones']!='80']
print(columna)
print ('\n')
#Llenar con 0 valores NAN
df.fillna(0,inplace=True)
print(df)
#Convertir a números enteros
df['Calificaciones']=df.Calificaciones.astype(int)
print(df.describe())
print ('\n')
#Estadísticas individuales
print("Promedio=",df['Calificaciones'].mean())
