import pandas as pd
from datetime import datetime
import numpy as np

# abro los csv que me interesan
def extract():
    df_order_details = pd.read_csv('order_details.csv', sep = ',')
    df_order = pd.read_csv('orders.csv', sep = ',')
    df_pizza_types = pd.read_csv('pizza_types.csv', encoding='latin-1')
    return df_order_details, df_order, df_pizza_types


def transform(df_order_details, df_order, df_pizza_types):
    df_order_details['fechas'] = '' # creo una nueva columna vacía en el dataframe de order_details a la que iré añadiendo las fechas de los pedidos 
    df_order_details['semana'] = '' # creo una nueva columna vacía a la que le asignaré el número de semana del año usando la librería datetime
    df_order_details['ingredientes'] = '' # creo una nueva columna vacía a a que le voy a añadir los ingredientes de cada pizza
    for i in range(len(df_order_details)):
        num_order_id = df_order_details['order_id'][i]
        fecha = df_order['date'][num_order_id - 1]
        fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y')
        semana = fecha_datetime.strftime('%W')
        # añado a la columna 'fecha' en el dataframe 
        df_order_details['fechas'][i] = fecha_datetime
        # añado a la columna 'semana' en el dataframe
        df_order_details['semana'][i] = semana
        tipo_pizza = df_order_details['pizza_id'][i]
        #utilizo este bucle para que me busque los ingredientes que tiene cada pizza en el dataframe df_pizza_types
        for j in range(len(df_pizza_types)): 
            if tipo_pizza[:-2] == df_pizza_types['pizza_type_id'][j]:
                ingredientes = df_pizza_types['ingredients'][j]
                df_order_details['ingredientes'][i] = ingredientes

    #creo una lista a la que añadiré todos los ingredientes de cada pizza
    lista_ingredientes = [] 
    for i in range(len(df_pizza_types)):
        ingredientes = df_pizza_types['ingredients'].iloc[i].split(',')
        for ing in ingredientes:
            ing = ing.strip()
            if ing not in lista_ingredientes:
                lista_ingredientes.append(ing)

    #creo una columna por cada ingrediente no repetido usando lista_ingredientes previamente creada
    for ing in lista_ingredientes:
        df_order_details[ing] = df_order_details['ingredientes'].str.contains(ing)

    # sumo todos los ingredientes por semanas en un nuevo data frame llamado df_semana
    df_semana = pd.DataFrame()
    df_semana['semana'] = df_order_details['semana'].copy()
    df_order_details['Barbecued Chicken']
    for i in range(len(lista_ingredientes)):
        df_semana[lista_ingredientes[i]] = df_order_details[lista_ingredientes[i]]
    print(df_semana)
    df_semana = df_semana.groupby('semana').sum()
    #quito la primera fila ya que la semana 0 empieza en jueves y por lo tanto está incompleta
    df_semana = df_semana.drop(df_semana.index[0])
    #calculo la media de todas las semanas: 
    df_final = df_semana.mean() 
    #aproximo hacia abajo para no tener decimales:
    df_final = df_final.apply(np.floor)
    #dataset final:
    return df_final
        
def load(df_final):
    csv_final = df_final.to_csv('prediccion_final.csv')
    return csv_final

if __name__ == '__main__':
    df1, df2, df3 = extract()
    df_final = transform(df1, df2, df3)
    print(df_final)
    prediccion_final = load(df_final)
    
