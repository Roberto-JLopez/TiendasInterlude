import pyautogui
import subprocess
import time
import keyboard
import sys
import os


# Función para obtener la ruta correcta de los recursos (imágenes) en el ejecutable
def resource_path(relative_path):
    try:
        # Para el caso del ejecutable
        base_path = sys._MEIPASS
    except Exception:
        # Para el caso del script original
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ruta del juego
game = r"C:\Program Files (x86)\L2 Tienda 1\system\L2.exe"


# Imágenes (ahora usando resource_path para obtener las rutas correctas)
starlog = resource_path("imagenes/Starlog.png")
star = resource_path("imagenes/star.png")
ok = resource_path("imagenes/ok.png")
sepu = resource_path("imagenes/sepu.png")
message = resource_path("imagenes/message.png")
login = resource_path("imagenes/login.png")
log = resource_path("imagenes/Log.png")
inicio = resource_path("imagenes/inicio.png")
buy = resource_path("imagenes/buy.png")
agree = resource_path("imagenes/Agree.png")


# Función para hacer clic
def click(buscar_elemento):
    pyautogui.click(buscar_elemento)  # Simular un clic izquierdo del ratón
    pyautogui.mouseDown()  # Presiona el botón izquierdo del ratón
    time.sleep(0.01)  # Espera 0.01 segundos
    pyautogui.mouseUp()  # Suelta el botón izquierdo del ratón


# Función para hacer doble clic
def dobleclick(buscar_elemento):
    pyautogui.doubleClick(buscar_elemento)  # Simular un clic izquierdo del ratón
    pyautogui.mouseDown()  # Presiona el botón izquierdo del ratón
    time.sleep(0.01)  # Espera 0.01 segundos
    pyautogui.mouseUp()  # Suelta el botón izquierdo del ratón


# Función para buscar elementos
def buscar_elemento(imagen, nombre_elemento, certeza, intentos=10):
    for _ in range(intentos):
        try:
            localizacion = pyautogui.locateCenterOnScreen(image=imagen, minSearchTime=2, confidence=certeza)
            if localizacion:
                click(localizacion)
                print(f"Elemento {nombre_elemento} encontrado")
                return True
        except pyautogui.ImageNotFoundException:
            print(f"Error: Imagen de '{nombre_elemento}' no encontrada. Intentando nuevamente...")
            time.sleep(5)
    print(f"No se pudo localizar el elemento {nombre_elemento} después de varios intentos.")
    exit()  # Terminar el programa


# Función para comenzar la compra
def comenzar_compra(imagen, certeza, intentos=10):
    for _ in range(intentos):
        try:
            localizacion = pyautogui.locateCenterOnScreen(image=imagen, minSearchTime=2, confidence=certeza)
            if localizacion:
                click(localizacion)
                print("comprando listo")
                return True
        except pyautogui.ImageNotFoundException:
            print("Error: Imagen no encontrada. Intentando nuevamente...")
            time.sleep(5)
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa


# Función para poner el mensaje
def mensaje(imagen, certeza, intentos=10):
    for _ in range(intentos):
        try:
            localizacion = pyautogui.locateCenterOnScreen(image=imagen, minSearchTime=2, confidence=certeza)
            if localizacion:
                click(localizacion)
                keyboard.write(">>Entrance Sepulcher<<")
                pyautogui.press('enter')
                print("mensaje listo")
                return True
        except pyautogui.ImageNotFoundException:
            print("Error: Imagen no encontrada. Intentando nuevamente...")
            time.sleep(5)
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa


# Función para compra de ítem
def compra_iten(imagenIten, certeza=0.8, intentos=5):
    for _ in range(intentos):
        try:
            localizacion = pyautogui.locateOnScreen(image=imagenIten, minSearchTime=2, confidence=certeza)
            if localizacion:
                dobleclick(localizacion)
                time.sleep(1)
                pyautogui.write("100000000")
                pyautogui.press('enter')
                pyautogui.write("2")
                pyautogui.press('enter')
                print("comprando sepu")
                return True
        except pyautogui.ImageNotFoundException:
            pyautogui.press("enter")
            pyautogui.write("/buy")
            pyautogui.press("enter")
            print("Error: Imagen no encontrada. Intentando nuevamente...")
            time.sleep(5)
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa


# Función para loguear la cuenta
def loguenado_cuenta(imagen, username, password, certeza=0.8, intentos=10):
    for _ in range(intentos):
        try:
            localizacion = pyautogui.locateOnScreen(image=imagen, minSearchTime=2, confidence=certeza)
            if localizacion:
                click(localizacion)
                pyautogui.write(username)
                pyautogui.press("tab")
                pyautogui.write(password)
                print("Cuenta logueada exitosamente")
                return True
        except pyautogui.ImageNotFoundException:
            print("Error: Imagen no encontrada. Intentando nuevamente...")
            time.sleep(5)
    print("No se pudo localizar la imagen después de varios intentos.")
    exit()  # Terminar el programa



# Información de la cuenta
username = ["ventas0011","ventas0012","ventas0013","ventas0014",
           "ventas0015","ventas0016","ventas0017","ventas0018",
           "ventas0019","ventas0020"]
password = "1234"
for i in username:
    print(f"logueando {i}")
    # Paso 1: Abrir el juego
    subprocess.Popen(game)
    print("abriendo el juego")
    time.sleep(10)

    # Logueo
    logueo_exitoso = loguenado_cuenta(login, i, password, 0.8, 5)
    time.sleep(2)
    buscar_login = buscar_elemento(log, "Loguin", 0.8, 5)
    time.sleep(2)
    buscar_agree = buscar_elemento(agree, "Agree", 0.8, 5)
    time.sleep(2)
    buscar_ok = buscar_elemento(ok, "Boton OK", 0.8, 5)
    time.sleep(2)
    buscar_starlog = buscar_elemento(starlog, "Boton Star", 0.8, 5)
    time.sleep(10)

    # Enviar mensaje y comprar
    pyautogui.write("/buy")
    pyautogui.press("enter")
    time.sleep(2)
    comprar_sepu = compra_iten(sepu)
    poner_mensaje = mensaje(message, 0.8, 5)
    time.sleep(2)
    compra = comenzar_compra(star, 0.8, 5)

    # Minimizar la ventana activa
    pyautogui.hotkey('alt', 'h')
    pyautogui.hotkey('win', 'down')




