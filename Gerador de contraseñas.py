import random
import time
caracteres = "1234567890abcdefghijklmnopqrstxywzñ!?¿¡*ABCDEFGHIJKLMNOPQRSTOXYZÑ"
longitud = int(input("Di la cantidad de caracteres"))

password = ""
for i in range(longitud):
    password += random.choice(caracteres)

print(password)
