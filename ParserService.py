import socket
import json
import os
import sys

import csv 
import time
import signal
import traceback

class Moneda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.compra = compra
        self.venta  = venta

class Parser:

    def leerArchivo(path):

        try:
            with open(path) as datafile:  # cargamos y luego leemos el archivo csv
                dfRead= csv.DictReader(datafile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                monedas = []

                for row in dfRead:
                    monedas.append(row) # los agregamos

                monedasJason = json.dumps(monedas) # lo pasamos a json

                return (monedasJason)

        except FileNotFoundError as e:
            print("Error al intentar cargar el archivo")
            print(e)
            return 0


class Main:

    def __init__(self):
        pass
    def handlerSigint(self,sig,frame):
        print("\nFin del servicio")

        self.s.close()
        exit()
    def main(self):
        periodo=30

        signal.signal(signal.SIGINT,self.handlerSigint)

        port = 10000

        try:
            port = int(sys.argv[1])
        #except ValueError as e:
        except:


            print("error en el puerto")
            exit(1)

        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.s.connect(("localhost",port))

        print("puerto" + str(port) + "...")

        while True:
            pathCsv = 'data.csv'
            if pathCsv == 0:

                print("saliendo...")
                return
            divisas = Parser.leerArchivo(pathCsv)

            if divisas == 0:
                print ("Errror en la ruta contenida en Config.txt")
                print ("Volviendo a intentar en %d segundos \n"%(periodo))
            else:
                try:
                    bytesEnviados = self.s.send(bytearray(divisas,'utf-8'))
                    (data,addr) = self.s.recvfrom(len("OK"))
                except:
                    print("error en el socket")
                    print("Volviendo a intentar en %d segundos\n"%(periodo))
                else:
                    print("datos enviandos con éxito")
                    print("volviendo a enviar datos en %d segundos\n"%(periodo))

            time.sleep(periodo)

m = Main()
m.main()
















