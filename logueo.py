import os
from categorias import *
from proveedores import *
from productos import *
from clientes import *
Datos = []
Email = []

def logueo():
 os.system("clear")
 print(":::: MENU ACCESO ::::")
 print("[1.] INGRESAR")
 print("[2.] CREAR CUENTA DE USUARIO")
 print("[3.] SALIR")
 op = input("SELECCIONA UNA OPCION: ")
 if op == '1' :
    ingresar()
 elif op == '2' :
     registrar()
 elif op == '3' :
      salir()
 else :
    print("::: Vuelve pronto :::")

def ingresar():
    os.system("clear")
    if len(Datos) == 0 :
       print("::: LA LISTA ESTÁ VACÍA :::")
       key = input("Presione cualquier tecla para volver al menú")
       logueo()
    else :
       i = 0
       encontrado = False
    while i < len(Datos)-1 :
      usuario = input("Digite Usuario: ")
      if usuario == Datos[i] :
        encontrado = True
      i += 1

    if encontrado == True :
       print("::: EL usuario ENCONTRADO EN LA LISTA")
    else :
     usuario = input("USUARIO: ")
     contraseña = input("CONTRESEÑA: ")
     print(":::: MENU ADMINISTRADOR ::::")
     print("[1.] CATEGORIAS")
     print("[2.] PROVEEDORES")
     print("[3.] PRODUCTOS")
     print("[4.] CLIENTES")
     print("[5.] REPORTES")
     print("[6.] SALIR")
     op = input("SELECCIONA UNA OPCION: ")
     if op == '1' :
        categorias()
     elif op == '2' :
        proveedores()
     elif op == '3' :
         productos()
     elif op == '4':
         clientes()
     elif op == '5':
         reportes()
     elif op == '6':
         salir()        
     else :
        print("::: Vuelve pronto :::")
    logueo()

def registrar ():
 os.system("clear")
 if len(Datos) == 0:
     nombres = input("DIGITE SUS NOMBRES: ")
     apellidos = input("DIGITE SUS APELLIDOS: ")
     celular = int(input("DIGITE NUMERO CELULAR: "))
     email = input("DIGITE SU E-MAIL: ")
     Email.append(email)
     usuario = input("DIGITE SU USUARIO: ")
     contraseña = input("DIGITE SU CONTRASEÑA: ")
     Datos.append([nombres, apellidos, celular, usuario, contraseña])
 else :
     nombres = input("DIGITE SUS NOMBRES: ")
     apellidos = input("DIGITE SUS APELLIDOS: ")
     celular = int(input("DIGITE NUMERO CELULAR: "))
     email = input("DIGITE SU E-MAIL: ")
     usuario = input("DIGITE SU USUARIO: ")
     contraseña = input("DIGITE SU CONTRASEÑA: ")
         
 i = 0
 encontrado = False
 while i < len(Datos)-1 :
      if email == Email[i] :
        encontrado = True
      i += 1
               #print("mail ya registrado")
      if encontrado == True :
            print("::: EMAIL FUE ENCONTRADO EN LA LISTA")
      else:
            Datos.append([nombres, apellidos, celular, email, usuario, contraseña])
 logueo()
def salir ():
	  print(Datos)
    #logueo()