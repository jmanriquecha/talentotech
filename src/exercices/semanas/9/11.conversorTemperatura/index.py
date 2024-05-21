""" 
Conversor de Temperatura
Enunciado
Conversor de Temperatura: Escribe un programa que permita convertir temperaturas entre Celsius y Fahrenheit. El programa debe mostrar un menú con las opciones: convertir de Celsius a Fahrenheit, convertir de Fahrenheit a Celsius y salir.
Dificultad
Media

Instrucciones
"""
def conversorTemperatura():
    print('PROGRAMA DE CONVERSIÓN DE TEMPERATURA')
    print('(1) Convertir de Celsius a Fahrenheit')
    print('(2) Convertir de Fahrenheit a Celsius')
    print('(3) Salir')

    while True:
        option = int(input('\nSeleccione un número entre 1 - 3: \n'))
        if option == 1:
            grados = float(input('\nIngrese °C: '))
            result = celsiusAFahrenheit(grados)
            print(f'Resultado: {grados} °C = {result} °F')
        elif option == 2:
            grados = float(input('\nIngrese °F: '))
            result = fahrenheitACelsius(grados)
            print(f'Resultado: {grados} °F = {result} °C')
        elif option == 3:
            print('Finalizando aplicación: ')
            break
        else:
            print('No ha seleccionado una opción valida! ')

def celsiusAFahrenheit(grados):
    return (grados * 9 / 5) + 32

def fahrenheitACelsius(grados):
    return (grados - 32) * 5 / 9

if __name__ == "__main__":
    conversorTemperatura()
    
    
    
