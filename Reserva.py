# Clase para representar una habitación en el hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo      # Tipo de habitación (simple, doble, suite, etc.)
        self.precio = precio  # Precio por noche
        self.disponible = True  # Estado de disponibilidad de la habitación

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}): ${self.precio} por noche"

# Clase para representar un cliente del hotel
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Nombre del cliente
        self.email = email    # Email del cliente

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

# Clase para representar una reserva en el hotel
class Reserva:
    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente    # Cliente que hace la reserva
        self.habitacion = habitacion  # Habitación reservada
        self.noches = noches      # Número de noches de la reserva
        self.costo_total = self.calcular_costo_total()  # Costo total de la reserva

        # Marcar la habitación como no disponible
        self.habitacion.disponible = False

    def calcular_costo_total(self):
        # Calcula el costo total de la reserva
        return self.habitacion.precio * self.noches

    def __str__(self):
        return f"Reserva para {self.cliente.nombre} en {self.habitacion} por {self.noches} noches. Costo total: ${self.costo_total}"

# Ejemplo de uso del sistema de reservas

# Crear algunas habitaciones
habitacion1 = Habitacion(501, "Simple", 75)
habitacion2 = Habitacion(502, "Doble", 175)
habitacion3 = Habitacion(503, "Suite", 200)

# Crear un cliente
cliente1 = Cliente("Ronny Melo", "ronnyemp1988@hotmail.com")

# Realizar una reserva
reserva1 = Reserva(cliente1, habitacion2, 3)

# Mostrar la reserva
print(reserva1)

# Intentar hacer otra reserva en la misma habitación
cliente2 = Cliente("Margarita Reyes", "margaraR@gmail.com")
if habitacion2.disponible:
    reserva2 = Reserva(cliente2, habitacion2, 2)
else:
    print(f"Lo siento, ya está reservada por {cliente1} la {habitacion2} .")

# Crear una nueva reserva en una habitación disponible
reserva3 = Reserva(cliente2, habitacion1, 2)

# Mostrar todas las reservas
print("\nRESERVAS:\n")
print(reserva1)
print(reserva3)