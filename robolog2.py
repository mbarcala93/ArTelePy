"""
    Ejemplo 1 - Este programa escribe por Terminal el contenido del ultimo mensaje
            que ha recibido el chatbot junto con el nombre del autor y la ID del chat.

    Escrito por Transductor
    www.robologs.net
"""

#Importar librerias
import json
import requests

#Variables para el Token y la URL del chatbot
TOKEN = "1496253956:AAEmdff4DKn_i8yMeeBF4wWnvZdrCbpzmbA" #Cambialo por tu token
URL = "https://api.telegram.org/bot" + TOKEN + "/"



def update(offset):#La función update() ahora recibirá un parámetro offset, que se corresponderá al identificador del primer mensaje que queremos recibir.
    #Llamar al metodo getUpdates del bot haciendo una peticion HTTPS (se obtiene una respuesta codificada)
    respuesta = requests.get(URL + "getUpdates" + "?offset"+str(offset) + "$timeout=" + str(200))
    print(URL + "getUpdates" + "?offset"+str(offset) + "$timeout=" + str(100))
    #Decodificar la respuesta recibida a formato UTF8 (se obtiene un string JSON)
    mensajes_js = respuesta.content.decode("utf8")

    #Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)

    #Devolver este diccionario
    return mensajes_diccionario


def leer_mensaje(mensaje):#La función leer_mensaje() recibirá como parámetro un mensaje y devolverá la id del chat, id del mensaje, el nombre del remitente y el texto.

    #Llamar update() y guardar el diccionario con los mensajes recientes
    #mensajes = update()#llama al método getUpdates del chatbot y convierte en string JSON recibido a un diccionario python
    #print(mensajes)

    #Calcular el indice del ultimo mensaje recibido
    #indice = len(mensajes["result"])-1
    #print(str(indice))

    #Extraer el texto, nombre de la persona e id del último mensaje recibido
    texto = mensaje["message"]["text"]
    persona = mensaje["message"]["from"]["first_name"]
    id_chat = mensaje["message"]["chat"]["id"]

    #Calcular el ID único del mensaje para calcular el offset
    id_update=mensaje["update_id"]

    #Mostrar esta informacion por pantalla
    print(persona + " (id: " + str(id_chat) + ") ha escrito: " + texto + "///" + str(id_update))
    return id_chat, persona, texto, id_update
def enviar_mensaje(idchat, texto):
    #Llamar al método sendmessage del bot, pasado texto e idchat
    requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))



#Llamar a la funcion "leer_mensaje()"
#idchat, nombre, texto = leer_mensaje()

#Variable para almacenar la ID del último mensaje
ultima_id=0

while(True):#mantener conversacion
    mensajes_diccionario=update(ultima_id)
    for i in mensajes_diccionario["result"]:
        #Llamar a la funcion "leer_mensaje()"
        idchat, nombre, texto, id_update = leer_mensaje(i)

        #Si la ID del mensaje es mayor que el último, se guarda la ID + 1
        if id_update>(ultima_id-1):
            ultima_id=id_update+1


        #generar una respuesta a partir de la información del mensaje
        if "Hola" in texto:
                texto_respuesta="Hola, " + nombre + "!"
                #enviar_mensaje(idchat, texto_respuesta)
        elif "Adiós" in texto:
                texto_respuesta="Hasta pronto " + nombre + "!"
                #enviar_mensaje(idchat, texto_respuesta)
        else:
                texto_respuesta="Has escrito: <<" + texto + ">>"

        #enviar respuesta
        enviar_mensaje(idchat, texto_respuesta)
    #Vaciar_diccionario
    mensajes_diccionario=[]
