df = pd.read_csv('./park_uda_cam1.csv')
# print(df.info())
# Cambio el guion (-) por (:) de la columna hora para pasarle
# a tipo time
df['hora'] = df['hora'].str.replace('-', ':')

# Para convertir un registro a tipo time
time_str = '09:50:26'
time_object = datetime.strptime(time_str, '%H:%M:%S').time()

# Se concatena la fecha con la hora para tratarlos posteriormente en intervalos
# users['full_name'] = users.last_name.str.cat(users.first_name, sep=', ')
df['fecha_hora'] = df['fecha'].str.cat(df['hora'], sep=' ')

# Si se quiere pasar la columna fecha a tipo date
df['fecha_hora'] = pd.to_datetime(df['fecha_hora'], dayfirst=True)
# df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True)
# print(df.info())


# Ver el número de autos detectados por YOLOv8 large, con un tamaño de imagen [1920, 1080]
# por día, en la CAM1, agrupando por dias
df_day_grouped = df.groupby(['fecha']).size().reset_index(name='autos')

# Ver el número de autos por dia, agrupando por fecha y hora
df_day_hour_grouped = df.groupby(['fecha', 'hora']).size().reset_index(name='autos')

# Número de autos detectados en intervalos de tiempo
# Aquí se puede sacar cualquier gráfico de las detecciones de los autos en cualquier intervalo
# de días o de horas, incluso minutos
inicio_dia = '2023-06-23 10:00:00'
fin_dia = '2023-06-23 10:59:59'

mask = (df['fecha_hora'] > inicio_dia) & \
       (df['fecha_hora'] <= fin_dia)

masked_df = df.loc[mask]
masked_df_grouped = masked_df.groupby(['fecha_hora', 'hora', 'fecha']).size().reset_index(name='autos')
