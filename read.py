import serial, time #importar librería pyserial
arduino=serial.Serial('COM5', 9600) #instanciar un objeto Pyserial "arduino", pasando como parámetros el puerto del ARDUINO
time.sleep(2)
mensaje=arduino.readline()#orden readline()para leer una linea enviada por arduino
print(mensaje)
arduino.write(b'9')#imprimir en consola la linea leída
arduino.close()#cerrar puerto serie
