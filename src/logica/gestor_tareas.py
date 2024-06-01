import tkinter as tk
from tkinter import ttk, messagebox

class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, indice):
        if indice < 0 or indice >= len(self.tareas):
            raise IndexError("Índice fuera de rango")
        self.tareas[indice].completada = True

    def eliminar_tarea(self, indice):
        if indice < 0 or indice >= len(self.tareas):
            raise IndexError("Índice fuera de rango")
        del self.tareas[indice]

    def ver_tareas(self):
        return self.tareas
