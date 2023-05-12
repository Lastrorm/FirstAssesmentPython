from abc import ABC, abstractmethod


class Asignaturas(ABC):
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    @abstractmethod
    def descripcion(self):
        pass


class Matematicas(Asignaturas):
    def __init__(self, nombre, profesor, nivel):
        super().__init__(nombre, profesor)
        self.nivel = nivel

    def descripcion(self):
        return f"{self.nombre} es una asignatura de nivel {self.nivel}, impartida por el profesor {self.profesor}."


class Ciencias(Asignaturas):
    def __init__(self, nombre, profesor, laboratorio):
        super().__init__(nombre, profesor)
        self.laboratorio = laboratorio

    def descripcion(self):
        if self.laboratorio:
            return f"{self.nombre} es una asignatura con laboratorio, impartida por el profesor {self.profesor}."
        else:
            return f"{self.nombre} es una asignatura teórica, impartida por el profesor {self.profesor}."


class Historia(Asignaturas):
    def __init__(self, nombre, profesor, epoca):
        super().__init__(nombre, profesor)
        self.epoca = epoca

    def descripcion(self):
        return f"{self.nombre} es una asignatura que estudia la época {self.epoca}, impartida por el profesor {self.profesor}."
