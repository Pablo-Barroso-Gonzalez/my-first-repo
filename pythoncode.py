
idioma = input("What is your language?\n1- English\n2- Español\n")
if idioma == "1":
    mensaje = "Hello, I want to create this test file so I can upload my first file to GitHub."
elif idioma == "2":
    mensaje = "Hola, quiero crear este archivo de prueba para poder subir mi primer archivo a GitHub"
else:
    mensaje = "Invalid option"

print(mensaje)