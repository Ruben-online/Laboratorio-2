from node import Node


class Appointment:
    def __init__(self, first_name, last_name, appointment_date, appointment_time, doctors_name, appointment_kind):
        self.first_name = first_name
        self.last_name = last_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.doctors_name = doctors_name
        self.appointment_kind = appointment_kind
        self.head = None


class Schedule:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def show_schedule(self):
        if self.is_empty():
            print("No hay citas programadas")
            return

        current = self.head
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break
        print()

    def add_appointment(self):
        data = input("Ingrese (# cita, Nombre, Apellido: ")
        first_name = input("Ingrese el nombre: ")
        last_name = input("Ingrese el apellido: ")
        appointment_date = input("Ingrese la fecha de la cita: ")
        appointment_time = input("Ingrese la hora de la cita: ")
        doctors_name = input("Ingrese el nombre del medico: ")
        consult_type = input("Ingrese el tipo de consulta: ")

        appointment = Appointment(first_name, last_name, appointment_date, appointment_time, doctors_name, consult_type)
        new_node = Node(data, appointment)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_appointment(self):
        if self.is_empty():
            print('No hay citas programadas')
            return

        data_to_delete = input("Ingrese la data de la cita a eliminar: ")


        if self.head.data == data_to_delete and self.head.next == self.head:
            self.head = None
            return

        current = self.head
        prev = None

        while True:
            if current.data == data_to_delete:
                if current == self.head:
                    prev.next = current.next
                    self.head = current.next
                else:
                    prev.next = current.next

                print(f'Cita con data {data_to_delete} eliminada.')
                break

            prev = current
            current = current.next

            if current == self.head:
                print(f'No se encontró la cita con la data {data_to_delete}')
                break