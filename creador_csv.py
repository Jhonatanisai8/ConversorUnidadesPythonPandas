import pandas as pd
# DataFrame es la informacion basica con el nombre de las piezas basicas y centimetros para poder armar el excel
data = {
    "Piezas" : ["Pata","Tablero","Puerta","Estante","Panel Lateral"],
    "centimetros":[40,120,60,30,180]
}

df = pd.DataFrame(data)

#guardamos el dataFrame en un archivo excel 
df.to_excel("muebles_medidas.xlsx",index=False)