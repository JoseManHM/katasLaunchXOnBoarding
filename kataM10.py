#Generación de primer traceback
def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()

#Try y Except
def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("No podemos encontrar dicho archivo!")

if __name__ == '__main__':
    main()

#Varios except
def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("No podemos encontrar el archivo")
    except IsADirectoryError:
        print("Encontramos config.txt pero es un directorio, no lo podemos abrir")
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivo bajo mucha carga, no podemos completar la lectura del archivo de configuración")

if __name__ == '__main__':
    main()

#Generación de excepciones
def water_left(astronautas, agua_rest, dias_rest):
    uso_diario = astronautas * 11
    uso_total = uso_diario * dias_rest
    agua_total_restante = agua_rest - uso_total
    if agua_total_restante < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronautas} astronautas despues de {dias_rest} dias!")
    return f"Agua total restante para {dias_rest} dias es: {agua_total_restante} litros"

water_left(4, 11, 3)

#Mejora de la funcion
def water_left2(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

water_left2(2,15,15)