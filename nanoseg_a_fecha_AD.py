import arrow
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

timestamp_nanos = 133541300405678343
timestamp_seconds = timestamp_nanos / 1e7
timestamp_seconds -= 11644473600    # Desplazamiento (segundos entre la fecha 01/01/1601 y 1/01/1970)

datetime_np = np.datetime64(int(timestamp_seconds), 's')
df = pd.DataFrame({'Fecha': [datetime_np]})

print(df)