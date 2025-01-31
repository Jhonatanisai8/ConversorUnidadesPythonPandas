import pandas as pd
def cm_a_pulgadas(cm):
    return cm / 2.54;

# leer el archivo excel 
df = pd.read_excel("muebles_medidas.xlsx")

#añadir una columna al dataFrame que sea de pulgadas y se rellana con el calculo de cm/2.54
df["pulgadas"] = df["centimetros"].apply(cm_a_pulgadas)
archivo = "muebles_medidas_convertidas.xlsx"

df.to_excel(archivo,index=False)
print("Conversor completado y guardado en un nuevo archivo llamado")