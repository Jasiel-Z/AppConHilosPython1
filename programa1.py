import threading
import os

def task1():
    print("Tarea 1 asignada al thread: {}".format(threading.currentThread().name))
    print("ID del proceso corriendo la tarea 1:{}".format(os.getpid()))

def task2():
    print("Tarea 2 asignada al thread: {}".format(threading.currentThread().name))
    print("ID del proceso corriendo la tarea 2:{}".format(os.getpid()))

if __name__ == "__main__":
    print("ID del proceso corriendo el programa main: {}".format(os.getpid()))
    print("Nombre del main thread:{}".format(threading.current_thread().name))

    #crear hilos
    t1 = threading.Thread(target=task1,name="hilo 1")
    t2 = threading.Thread(target=task2,name="hilo 2")

    t1.start()
    t2.start()

    print("programa terminado")