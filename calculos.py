import numpy as np
import pandas as pd
from scipy.optimize import minimize


def agregarRetorno(df):
    # CREO LA LISTA DE RETORNOS
    retornos = [0]
    fechas = []
    precio = []

    # CREO BOOLEANOS PARA ITERAR
    bandera = False
    anterior = 0

    # ITERO SOBRE EL DATAFRAME VIEJO
    for index, value in df.items():
        if bandera == False:
            bandera = True
            anterior = value
            fechas.append(index)
            precio.append(value)
            continue
        else:
            retorno = (np.log(value) - np.log(anterior))
            retornos.append(retorno)
            anterior = value
            fechas.append(index)
            precio.append(value)

    # CREO UN NUEVO DATAFRAME Y AJUSTO LOS DATOS
    d = {'Date': fechas, 'Adj Close': precio, 'Retorno': retornos}
    df_final = pd.DataFrame(data=d)

    # RETORNO EL NUEVO NUEVO DATAFRAME
    return df_final


def promedioRetornos(df):
    # CALCULAR EL PROMEDIO DE LOS RETORNOS
    return df.mean()[1]


def varianzaRetornos(df):
    # CALCULAR LA VARIANZA DE LOS RETORNOS
    return df.var()[1]


def crearMatrizCovarianza(matrix):
    # CREA LA MATRIZ DE COVARIANZAS DE LOS ACTIVOS
    return np.cov(matrix)


def iterarRetornos(df):
    # SEPARA LA COLUMNA DE RETORNOS, LA ALMACENA EN UN ARRAY Y ME LA DEVUELVE
    array_aux = []
    for ind in df.index:
        retorno = df['Retorno'][ind]
        array_aux.append(retorno)
    return array_aux


def calcularREp(pesos, retornos):
    # CALCULAR EL RENDIMIENTO ESPERADO DEL PORTAFOLIO ANUAL
    matriz_1 = np.array(pesos)
    matriz_2 = np.array(retornos)

    resultado = matriz_1.dot(matriz_2.transpose())
    return resultado * 250


def calcularVARp(cov, pesos):
    # CALCULAMOS LA VARIANZA DEL PORTAFOLIO ANUAL
    mat_cov = np.array(cov)
    mat_pesos = np.array(pesos)

    resultado_1 = mat_cov.dot(mat_pesos)
    resultado_2 = resultado_1.dot(mat_pesos.transpose())

    return resultado_2 * 250


def calcularSDp(cov, pesos):
    #CALCULAMOS LA DESVIACION ESTANDAR
    return np.sqrt(calcularVARp(cov, pesos))


def generarPortafolios(w, prom_retornos_array, cov, menor_volatilidad, rend_esperado):
    #FUNCION PARA GENERAR MUCHOS PORTAFOLIOS DE DISTRIBUCION ALEATORIA PARA SELECCIONAR EL MEJOR
    pfolio_returns = []
    pfolio_volatilities = []

    mejores_pesos = []

    for x in range(50000):
        weights = np.random.random(len(w))
        weights /= np.sum(weights)

        REp = calcularREp(weights, prom_retornos_array)
        VOLp = calcularSDp(cov, weights)

        if REp >= rend_esperado and VOLp <= menor_volatilidad:
            mejores_pesos = weights
            menor_volatilidad = VOLp
            rend_esperado = REp



        pfolio_returns = np.append(pfolio_returns, REp)
        pfolio_volatilities = np.append(pfolio_volatilities, VOLp)

        pfolio_returns = np.array(pfolio_returns)
        pfolio_volatilities = np.array(pfolio_volatilities)

    return pfolio_returns, pfolio_volatilities, mejores_pesos, menor_volatilidad, rend_esperado