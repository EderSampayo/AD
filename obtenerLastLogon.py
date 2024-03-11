import argparse
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import subprocess
import re

def convertir_timestamp(timestamp_100ns):
    timestamp_seconds = timestamp_100ns / 1e7
    timestamp_seconds -= 11644473600    # Desplazamiento (segundos entre la fecha 01/01/1601 y 1/01/1970)

    datetime_np = np.datetime64(int(timestamp_seconds), 's')
    df = pd.DataFrame({'Fecha': [datetime_np]})

    print(df)

def obtener_nanosegundos_lastLogon(distinguishedName):
    try:
        # Ejecuta el comando PowerShell para obtener lastLogon
        command = f"Get-ADUser -Filter {{DistinguishedName -eq '{distinguishedName}'}} -Properties lastLogon | Select-Object -ExpandProperty lastLogon"
        result = subprocess.check_output(["powershell", command], text=True)

        # Parsea el resultado y convierte a nanosegundos
        lastLogon = int(re.search(r'\d+', result).group())
        return lastLogon

    except Exception as e:
        print(f"Error al obtener lastLogon: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Obtener lastLogon de un usuario en AD")
    parser.add_argument('-u', '--DN', type=str, required=True, help="Valor")

    args = parser.parse_args()
    nanosegundos = obtener_nanosegundos_lastLogon(args.DN)
    convertir_timestamp(nanosegundos)

if __name__ == "__main__":
    main()