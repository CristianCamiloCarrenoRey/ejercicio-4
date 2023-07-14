class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
        self.tareas_asignadas = []

    def asignar_tarea(self, tarea):
        self.tareas_asignadas.append(tarea)

    def calcular_salario(self):
        total_salario = self.salario_base
        for tarea in self.tareas_asignadas:
            total_salario += tarea.pago
        return total_salario

class Tarea:
    def __init__(self, nombre, descripcion, pago):
        self.nombre = nombre
        self.descripcion = descripcion
        self.pago = pago

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def generar_informe(self):
        print(f"Informe del departamento {self.nombre}:")
        for empleado in self.empleados:
            print(f"Empleado: {empleado.nombre}")
            print(f"Tareas asignadas: {len(empleado.tareas_asignadas)}")
            print(f"Salario: {empleado.calcular_salario()}")

# Crear empleados
empleado1 = Empleado("Juan", 2000)
empleado2 = Empleado("María", 2500)

# Crear tareas
tarea1 = Tarea("Desarrollo de software", "Desarrollar una aplicación web", 500)
tarea2 = Tarea("Diseño gráfico", "Diseñar un logotipo", 300)

# Asignar tareas a empleados
empleado1.asignar_tarea(tarea1)
empleado2.asignar_tarea(tarea2)

# Crear departamento
departamento = Departamento("Desarrollo")

# Agregar empleados al departamento
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)

# Generar informe del departamento
departamento.generar_informe()
