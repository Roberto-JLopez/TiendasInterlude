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
game = r"D:\Lineage II Elite - Interlude\system\l2.exe"
# ruta del juego
gameDos = r"C:\Program Files (x86)\L2 Tienda 2\system\L2.exe"

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
offlineShop = resource_path("imagenes/offlineShop.png")
confirm = resource_path("imagenes/confirm.png")

# Función para hacer clic
def click(buscar_elemento):
    pyautogui.click(buscar_elemento)  # Simular un clic izquierdo del ratón
    pyautogui.mouseDown()  # Presiona el botón izquierdo del ratón
    time.sleep(0.05)  # Espera 0.01 segundos
    pyautogui.mouseUp()  # Suelta el botón izquierdo del ratón


# Función para hacer doble clic
def dobleclick(buscar_elemento):
    pyautogui.doubleClick(buscar_elemento)  # Simular un clic izquierdo del ratón
    pyautogui.mouseDown()  # Presiona el botón izquierdo del ratón
    time.sleep(0.07)  # Espera 0.01 segundos
    pyautogui.mouseUp()  # Suelta el botón izquierdo del ratón

def click_derecha_del_centro(imagen, certeza=0.8, offset_x=80):
    try:
        localizacion = pyautogui.locateCenterOnScreen(imagen, confidence=certeza)
        if localizacion:
            x, y = localizacion
            coordenadas = (x + offset_x, y)  # click a la derecha
            click(coordenadas)
            print("Clic en botón 'Enable'")
            return True
    except Exception as e:
        print(f"Error al buscar imagen: {imagen}")
        time.sleep(5)
    print("No se encontró la imagen para click a la derecha.")
    return False

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
    return False  # Terminar el programa


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
                time.sleep(2)
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
username = ["ventas0001","ventas0002","ventas0003","ventas0004",
           "ventas0005","ventas0006","ventas0007","ventas0008",
           "ventas0009","ventas0010","ventas0011","ventas0012","ventas0013","ventas0014",
           "ventas0015","ventas0016","ventas0017","ventas0018",
           "ventas0019","ventas0020"]
password = "1234"
for i in username:
    print(f"logueando {i}")
    # Paso 1: Abrir el juego
    subprocess.Popen(game, shell=True)
    print("abriendo el juego")
    time.sleep(10)

    # Logueo}
    logueo_exitoso = loguenado_cuenta(login, i, password, 0.8, 5)
    time.sleep(2)
    for intento_reintento in range(5):  # Máximo 5 reintentos
        buscar_login = buscar_elemento(log, "Loguin", 0.8, 2)
        time.sleep(2)

        buscar_agree = buscar_elemento(agree, "Agree", 0.8, 2)
        if not buscar_agree:
            print(f"Intento #{intento_reintento + 1}: No se encontró el botón 'Agree'. Reintentando login...")
            continue  # Reintenta desde el login
        else:
            break  # Salir del for si encontró 'Agree'

    else:
        print("Error: No se pudo encontrar el botón 'Agree' después de 5 intentos.")
        continue  # Salta al siguiente usuario del for principal
    buscar_ok = buscar_elemento(ok, "Boton OK", 0.8, 5)
    time.sleep(2)
    buscar_starlog = buscar_elemento(starlog, "Boton Star", 0.8, 5)
    time.sleep(10)

    # Enviar mensaje y comprar
    pyautogui.write("/buy")
    pyautogui.press("enter")
    time.sleep(2)
    intentos_compra = 5
    for intento in range(intentos_compra):
        print(f"Intento de compra #{intento + 1}")
        if compra_iten(sepu):
            time.sleep(2)
            pyautogui.write("100000")
            time.sleep(2)
            if buscar_elemento(confirm, "Boton Confirm", 0.8, 5):
                break
        else:
            print("Fallo al intentar comprar el ítem.")
        if intento < intentos_compra - 1:
            print("Reintentando proceso de compra...")
        else:
            print("Error: No se pudo completar la compra después de varios intentos.")
            exit()
    pyautogui.write("50")
    time.sleep(2)
    buscar_confirm = buscar_elemento(confirm, "Boton Confirm", 0.8, 5)
    time.sleep(2)
    poner_mensaje = mensaje(message, 0.8, 5)
    time.sleep(2)
    buscar_confirm = buscar_elemento(confirm, "Boton Confirm", 0.8, 5)
    time.sleep(2)
    compra = comenzar_compra(star, 0.8, 5)
    time.sleep(2)
    pyautogui.write(".menu")
    pyautogui.press("enter")
    time.sleep(2)
    buscar_tiendaoffline = click_derecha_del_centro(offlineShop, 0.8, 95)
