import pandas as pd
import pandas_datareader as web
import datetime as dt
import calculos as calculos
import os
from datetime import datetime

dirname=os.path.dirname(__file__)


def leerSimbolos():
    nombres = []

    # LEO EL ARCHIVO CON LOS SIMBOLOS YA CARGADOS
    df = pd.read_csv(dirname+'/datos/Simbolos.csv', parse_dates=True,
                     index_col=0)

    # ITERO SOBRE EL DataFrame PARA RECUPERAR LOS NOMBRES Y CARGARLOS EN UN ARREGLO
    for index, value in df.items():
        nombres.append(index)
    return nombres


def getData(nombre, inicio, fin):
    # DETERMINO CUAL VA A SER EL PERIODO DE OBTENCION DE DATOS
    # start = dt.datetime(2009, 1, 1)
    # end = dt.datetime(2010, 1, 1)

    start=datetime.strptime(inicio,"%y/%m/%d")
    end=datetime.strptime(fin,"%y/%m/%d")


    # OBTENGO LOS DATOS PARA EL PERIODO Y SIMBOLO SELECCIONADO
    df = web.DataReader(nombre, 'yahoo', start, end)

    # GUARDO LOS DATOS DEL ACTIVO COMO CSV
    guardarComoCSV(nombre, df)


def guardarComoCSV(nombre, df):
    # CONVIERTO LOS DATOS A UN CSV
    df.to_csv(dirname+'/datos/' + nombre + '.csv')


def limpiarDatos(nombre):
    # CARGO EL CSV CON EL NOMBRE QUE ME ENTRA POR PARAMETRO
    df = pd.read_csv(dirname+'/datos/' + nombre + '.csv',
                     parse_dates=True, index_col=0)

    # DESCARTO TODAS LAS COLUMNAS EXCEPTO LAS DE LA FECHA Y EL ADJ CLOSE
    df = df['Adj Close']

    # AGREGAR COLUMNA CON RETORNOS
    df_final = calculos.agregarRetorno(df)
    guardarComoCSV(nombre, df_final)
    return df_final


def dataFrame_retornos_varianzas():
    # CREA EL DATAFRAME EN EL QUE SE GUARDARAN LOS SIMBOLOS, PROMEDIO DE RETORNOS Y VARIANZAS DE LOS ACTIVOS
    data = []
    df_parcial = pd.DataFrame(data, columns=['Simbolo', 'Retorno', 'Varianza'])
    return df_parcial

def dataFrame_Portafolios(pf_r,pf_v):
    return pd.DataFrame({'Retornos':pf_r, 'Volatilidad':pf_v})