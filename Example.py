def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

yen_rate = 0.0063
peso_mexicano_rate = 0.056
peso_colombiano_rate = 0.00027

try:
    budget = float(input("Ingrese su presupuesto en USD: "))
    print("Seleccione el país:")
    print("1) Japón")
    print("2) México")
    print("3) Colombia")

    option = int(input("Ingrese una opción: "))
    if option == 1:
        result = exchange_money(budget, yen_rate)
        print("Recibirás", result, "yenes")

    elif option == 2:
        result = exchange_money(budget, peso_mexicano_rate)
        print("Recibirás", result, "pesos mexicanos")

    elif option == 3:
        result = exchange_money(budget, peso_colombiano_rate)
        print("Recibirás", result, "pesos colombianos")

    else:
        print("Opción no válida")

except ValueError:
    print("Por favor ingrese solo números.")