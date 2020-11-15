import serial, time
arduino=serial.Serial("COM5", 9600)
time.sleep(2)
arduino.write(b'9')#la función write envía bytes, por eso se convierte el valor (9) a bytes antecediendolo de una "b" de binario.
arduino.close()
