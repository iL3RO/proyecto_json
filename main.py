from funciones import listar_disponibles, contar_tipos, buscar_moto, filtrar_motos, mas_alquiladas

while True:
    print("\n=== MENÚ MOTOS ===")
    print("1. Ver motos disponibles")
    print("2. Contar tipos de motos")
    print("3. Buscar moto")
    print("4. Filtrar por cilindrada")
    print("5. Ver más alquiladas")
    print("6. Salir")
    
    opcion = input("Elige opción (1-6): ")
    
    if opcion == "1":
        listar_disponibles()
    elif opcion == "2":
        contar_tipos()
    elif opcion == "3":
        buscar_moto()
    elif opcion == "4":
        filtrar_motos()
    elif opcion == "5":
        mas_alquiladas()
    elif opcion == "6":
        print("Hasta luego miarma")
    else:
        print("Opción no válida")
