from circular_list import Appointment, Schedule

clinic_schedule = Schedule()


while True:
    print("Menu principal\n")
    print("1. Agregar una nueva cita ")
    print("2. Eliminar una cita existente")
    print("3. Mostrar todas las citas programadas")
    print("4. Salir del programa")

    main_menu = input("Ingrese una opcion (1-4): ")

    if main_menu == "1":
        clinic_schedule.add_appointment()

    elif main_menu == "2":
        clinic_schedule.delete_appointment()

    elif main_menu == "3":
        print("Citas programadas")
        clinic_schedule.show_schedule()

    elif main_menu == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo")