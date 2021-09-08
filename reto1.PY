print("Bienvenido al sistema de ubicación para zonas públicas WIFI ")
usuarioint=51659
claveint=95615
usuarioext=int(input("Dijite su usuario: "))
if (usuarioint == usuarioext):
  claveext=int(input("Digite su contraseña: "))
  if (claveint==claveext):
    c1=659
    c2=(5*2) - (5*1)
    captcha=int(input(f"El resultado de {c1} + {c2} es: "))
    if (captcha==c1+c2):
      print("Sesión iniciada")
    else:
      print("Error") 
  else:
    print("Error")
else:
  print("Error")