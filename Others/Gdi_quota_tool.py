import winreg

KEY_PATH = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows"
KEY_NAME = "GDIProcessHandleQuota"

def get_gdi_quota():
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, KEY_PATH, 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, KEY_NAME)
        return value
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"❌ Error al leer el valor: {e}")
        return None

def set_gdi_quota(value):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, KEY_PATH, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, KEY_NAME, 0, winreg.REG_DWORD, value)
        print(f"✅ GDIProcessHandleQuota actualizado a {value}")
    except PermissionError:
        print("❌ No tienes permisos suficientes. Ejecuta este script como administrador.")
    except Exception as e:
        print(f"❌ Error al escribir el valor: {e}")

def main():
    actual = get_gdi_quota()
    if actual is not None:
        print(f"🔎 Valor actual de GDIProcessHandleQuota: {actual}")
    else:
        print("⚠️ La clave no existe aún.")

    print("\n¿Qué quieres hacer?")
    print("1. Aumentar a 65536 (máximo recomendado)")
    print("2. Restaurar a 10000 (valor por defecto de Windows)")
    print("3. Salir")

    opcion = input("Selecciona una opción (1/2/3): ").strip()

    if opcion == "1":
        set_gdi_quota(65536)
    elif opcion == "2":
        set_gdi_quota(10000)
    elif opcion == "3":
        print("👋 Cancelado por el usuario.")
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
