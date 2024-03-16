import concurrent.futures

def hilo1():
    print ("hilo 1 corriendo")
    for i in range (0,6):
        print(i) 


def hilo2():
    print("hilo 2 corriendo")
    for i in range (11,20):
        print(i) 

pool = concurrent.futures.ThreadPoolExecutor(max_workers= 2)
pool.submit(hilo1)
pool.submit(hilo2)

pool.shutdown(wait= True)
print("El hilo main termina aqui")        