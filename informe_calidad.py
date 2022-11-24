import pandas as pd
import numpy as np
import seaborn as sns

df_order_details = pd.read_csv('order_details.csv', sep = ',')
df_order = pd.read_csv('orders.csv', sep = ',')
df_pizza_types = pd.read_csv('pizza_types.csv', encoding='latin-1')
#creo un nuevo data frame por cada data frame ya existente
calidad_df_order_details = pd.DataFrame()
calidad_df_order = pd.DataFrame()
calidad_df_pizza_types = pd.DataFrame()

# calculo número de nulls por cada columna del df_order_details
calidad_df_order_details['numero de nulls'] = df_order_details.isnull().sum()
# calculo número de nans por cada columna del df_order_details
calidad_df_order_details['numero de nan'] = df_order_details.isna().sum()
#calculo el tipo de objeto para cada columna del df_order_details
calidad_df_order_details['tipo columna'] = df_order_details.dtypes

# calculo número de nulls por cada columna del df_order
calidad_df_order['numero de nulls'] = df_order.isnull().sum()
# calculo número de nans por cada columna del df_order
calidad_df_order['numero de nan'] = df_order.isna().sum()
#calculo el tipo de objeto para cada columna del df_order
calidad_df_order['tipo columna'] = df_order.dtypes

# calculo número de nulls por cada columna del df_pizza_types
calidad_df_pizza_types['numero de nulls'] = df_pizza_types.isnull().sum()
# calculo número de nans por cada columna del df_pizza_types
calidad_df_pizza_types['numero de nan'] = df_pizza_types.isna().sum()
#calculo el tipo de objeto para cada columna del df_pizza_types
calidad_df_pizza_types['tipo columna'] = df_pizza_types.dtypes

print(calidad_df_order_details)
print(calidad_df_order)
print(calidad_df_pizza_types)