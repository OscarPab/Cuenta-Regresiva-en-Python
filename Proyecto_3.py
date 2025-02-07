import time

def cuenta_regresiva(tiempo):
    # Convertimos el tiempo en segundos
    while tiempo:
        # Calculamos los minutos y segundos
        minutos, segundos = divmod(tiempo, 60)
        # Formateamos el tiempo
        tiempo_formateado = '{:02d}:{:02d}'.format(minutos, segundos)
        print(tiempo_formateado, end='\r')
        # Esperamos un segundo
        time.sleep(1)
        # Reducimos el tiempo en un segundo
        tiempo -= 1

    print("¡Tiempo terminado!")

# Solicitamos al usuario el tiempo en segundos
tiempo = int(input("Introduce el tiempo en segundos: "))
# Iniciamos la cuenta regresiva
cuenta_regresiva(tiempo)
