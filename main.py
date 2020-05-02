# IMPORTACIONES DE PAQUETES
import datos as datos
import calculos as calculos
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import pandas as pd

style = 'MacOSX'

def main(rend_esp,men_vol,inicio,fin):
    # CREO ARRAY PARA ALMACENAR OTROS ARRAYS QUE CONTIENE LOS TODOS LOS RETORNOS DE CADA SIMBOLO
    
    array = []


    # CREAR DATAFRAME QUE CONTIENE LOS RETORNOS Y LAS VARIANZAS DE LOS ACTIVOS
    df_retorno_varianza = datos.dataFrame_retornos_varianzas()

    # CREO UNA LISTA DE NOMBRES BURSATILES
    nombres = datos.leerSimbolos()

    # CREO MATRIZ CON PESOS ARBITRARIOS
    pesos = []

    # ITERO SOBRE ESA LISTA PARA OBTENER LOS DATOS
    for nombre in nombres:
        # OBTENGO LOS DATOS Y LOS FACTOREO
        datos.getData(nombre, inicio, fin)
        df = datos.limpiarDatos(nombre)

        # OBTENGO LOS VECTORES QUE CONTIENEN TODOS LOS RETORNOS DE CADA SIMBOLO Y LOS ALMACENO ADENTRO DE OTRO VECTOR (ARRAY)
        array.append(calculos.iterarRetornos(df))

        # CALCULAR EL PROMEDIO DE LOS RETORNOS
        promedio = calculos.promedioRetornos(df)
        varianza = calculos.varianzaRetornos(df)

        # AGREGA AL DF_RETORNO_VARIANZA LOS DATOS DEL SIMBOLO, RETORNO Y VARIANZA PARA CADA SIMBOLO CARGADO EN EL SISTEMA
        df_retorno_varianza = df_retorno_varianza.append({'Simbolo': nombre, 'Retorno': promedio, 'Varianza': varianza},
                                                         ignore_index=True)

        # OBTENGO LOS PESOS ARBITRARIOS DE LOS ACTIVOS
        pesos.append(1 / len(nombres))

    # print(df_retorno_varianza)

    # SEPARAMOS LA COLUMNA DE RETORNOS PARA CALCULAR EL RETORNO ESPERADO DEL PORTAFOLIO
    prom_ret_array = calculos.iterarRetornos(df_retorno_varianza)

    # CALCULAMOS EL RENDIMIENTO ESPERADO DEL PORTAFOLIO ANUAL
    REp = calculos.calcularREp(pesos, prom_ret_array)
    # print(REp)

    # CON EL VECTOR DE VECTORES (ARRAY) CALCULO LA MATRIZ DE COVARIANZAS
    mat_cov = calculos.crearMatrizCovarianza(array)

    # CALCULAMOS LA VARIANZA DEL PORTAFOLIO
    VARP = calculos.calcularVARp(mat_cov, pesos)
    # print(VARP)

    # GENERAMOS PORTAFOLIOS ALEATORIOS
    pf_r, pf_v, mejores_pesos, menor_volatilidad, rendimiento_esperado = calculos.generarPortafolios(pesos, prom_ret_array, mat_cov, men_vol, rend_esp)
    #CREO EL DATAFRAME CON LOS RESULTADOS DEL MEJOR PORTAFOLIO
    df_p = datos.dataFrame_Portafolios(pf_r, pf_v)

    # CREO EL GRAFICO CON LA FRONTERA EFICIENTE
    df_p.plot(x='Volatilidad', y='Retornos', kind='scatter', figsize=(10, 6))

    plt.xlabel('Volatilidad Esperada')
    plt.ylabel('Retorno Esperado')

    # IMPRIMO LOS RESULTADOS
    print('-------  RESULTADOS  -------')

    print('Menor volatilidad: ', round(menor_volatilidad,4))
    print('Mejor Rendimiento esperado: ', round(rendimiento_esperado*100, 3), '%')
    print('-------  PESOS  -------')


    f=[]
    porcentaje=[]
    for i in range(len(nombres)):
        porcentaje.append(round(mejores_pesos[i] * 100,1))
        f.append([nombres[i], porcentaje[i]])
    


    final=pd.DataFrame(f)

    # MUESTRO EL GRAFICO
    plt.show()
    return final, round(rendimiento_esperado*100, 3), round(menor_volatilidad,4)
