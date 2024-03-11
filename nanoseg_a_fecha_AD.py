import arrow
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

timestamp_nanos = 133541300405678343
timestamp_seconds = timestamp_nanos / 1e7
timestamp_seconds -= 11644473600    # Desplazamiento (segundos entre la fecha 01/01/1601 y 1/01/1970)
#num_datapoints = 1000

datetime_np = np.datetime64(int(timestamp_seconds), 's')
df = pd.DataFrame({'Fecha': [datetime_np]})

#timestamps = np.arange(timestamp_seconds, timestamp_seconds + num_datapoints)

#df = pd.DataFrame({'Timestamp': timestamps})

#df['Fecha'] = pd.to_datetime(df['Timestamp'], unit='s', utc=True)

print(df)

#fecha = arrow.get(timestamp_seconds).to('UTC')

#print(fecha)

#cadena = "05/03/2024 17:34:00"
#fecha_hora = datetime.strptime(cadena, '%d/%m/%Y %H:%M:%S')
#timestamp = fecha_hora.timestamp()

#print(timestamp)