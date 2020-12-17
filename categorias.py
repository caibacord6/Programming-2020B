import os
from logueo import *
Categorias = []

def categorias ():
  os.system('clear')
  print(":::: MENU CATEGORIAS ::::")
  print("[1.] INGRESAR NUEVA CATEGORIA")
  print("[2.] LISTAR CATEGORIAS")
  print("[3.] BUSCAR UNA CATEGORIA")
  print("[4.] MODIFICAR CATEGORIA")
  print("[5.] ELIMINAR CATEGORIA")
  print("[6.] VOLVER AL MENU")
  
  op = input(".:: DIGITE UNA OPCION: ")

  if op == '1' :
    ingresar_categoria()
  elif op == '2' :
    listar_categoria()
  elif op == '3' :
    buscar_categoria()
  elif op == '4' :
    modificar_categoria()
  elif op == '5' :
    eliminar_categoria()
    
  elif op == '6':
    categorias()
  else :
    print("::: Vuelve pronto :::")
    
def ingresar_categoria():
  os.system('clear')
  print("::: INGRESO NUEVA CATEGORIA ::: ")
  nomcategoria = (input(" DIGITE CATEGORIA A ALMACENAR: "))
  Categorias.append(nomcategoria)
  key = input(" LA CATEGORIA HA SIDO ALMACENADA CON EXITO. Presione cualquier tecla para volver al menú")
  categorias()

def listar_categoria():
  os.system('clear')
  print("::: LISTADO DE CATEGORIAS ::: ")
  if len(Categorias) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :  
    print(Categorias)
    
  key = input("Presione cualquier tecla para volver al menú") 
  categorias()

def buscar_categoria():
  os.system('clear')
  buscar = 0
  print("::: BÚSQUEDA DE CATEGORIAS ::: ")
  #Here we must to look for a number
  
  if len(Categorias) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CATEGORIA A BUSCAR: ")
    i = 0
    encontrado = False
    while i < len(Categorias) :#-1
      if buscar == Categorias[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      print("::: LA CATEGORIA FUE ENCONTRADA EN LA LISTA")
    else :
      print("::: LA CATEGORIA NO FUE ENCONTRADA EN LA LISTA")
          
  key = input("Presione cualquier tecla para volver al menú")
  categorias()

def modificar_categoria():
  os.system('clear')
  print("::: MODIFICACIÓN DE CATEGORIA ::: ")
  if len(Categorias) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CATEGORIA A MODIFICAR: ")
    i = 0
    encontrado = False
    while i < len(Categorias) :#-1
      if buscar == Categorias[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      #Categorias.remove = Categorias[i]
      modificar = input(" DIGITE NUEVA CATEGORIA")
      Categorias.insert(len(Categorias),modificar)
    else :
      print("::: LA CATEGORIA NO FUE ENCONTRADA EN LA LISTA")
  key = input("Presione cualquier tecla para volver al menú")
  categorias()

def eliminar_categoria():
	os.system('clear')
	print("::::::: ELIMINAR CATEGORIA :::::::")
	elim = input("DIGITE CATEGORIA A ELIMINAR")
	Categorias.remove(elim)
	key = input("	Persione cualquier tecla para volver al menu")
	categorias()