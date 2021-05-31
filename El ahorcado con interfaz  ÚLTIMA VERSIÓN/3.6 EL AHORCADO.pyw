import sys
import pygame
from pygame.locals import *
import os
#----------------------EL AHORCADO ------------------------------------------------------- 
listaIntentos = None
men = None
op1 = None
op2 = None
op3 = None
lista = None
Let = None
p1 = None
PxL = None
tam = None
p2 = None
y = None
listaP1 = None
listaInt = None
listaPalabra1 = None
opci_C3_B3n = None
OpV_C3_A1lida = None
repetir = None
i = None
igual = None
palabra2 = None
Letra = None
ListaDeResultados = None
J = None
h = None
adivin_C3_B3 = None
repite = None
seJuega = None
n1 = None
x = None
palabra1 = None
contador = None
termin_C3_B3 = None
listaLetra = None
letraEnPal1 = None
n2 = None
contarRegistros = None
z = None
primeraEntrada = None
elementoListaPal = None
ResultadosOrdenados = None
intentosPend = None
elementoListaInt = None
listaP2 = None
uni_C3_B3n = None
tamP1 = None
acert_C3_B3 = None
aux1 = None
axu2 = None
mensaje = None
opci_C3_B3n1 = None
opci_C3_B3n2 = None
opci_C3_B3n3 = None
primeraEleccion = None
k = None
elije = None
#---------------------- FIN EL AHORCADO -------------------------------------------------------
#---------------------------------- COMUN A VARIOS------------------------
pygame.init()


anchoVentana=1254
altoVentana=636
cantLetrasLimite=25


azul=(0,0,255)
blanco=(255,255,255)
rojo=(255,0,0)
amarillo=(255,255,0)
celeste=(178,255,255)
naranjado=(255,128,0)
negro=(0,0,0)
gris=(155,155,155)
verdeClaro=(119,221,119)
verdeFluor=(0,255,0)
azulClaro=(0,170,228)

ventana=pygame.display.set_mode((anchoVentana,altoVentana))
pygame.display.set_caption("El ahorcado")
#----------------------------------COMUN A VARIOS------------------------

#********************** 13.2.2 Menú de opciones - clic tecla K************************

def creaUnBoton(mensaje,colorBot1,colorBot2,posIniX,posIniY,anchoRect, altoRect,tamLetra,tipoFuente):
    boton = pygame.Rect(posIniX,posIniY,anchoRect,altoRect)
    pygame.draw.rect(ventana,colorBot1,boton)
    textoBoton(tipoFuente,mensaje,colorBot2,posIniX,posIniY,anchoRect,altoRect,tamLetra)
    return boton

def huboColisionConPuntero(area):
    huboColi=False
    rectMouse=pygame.Rect(0,0,2,2)
    rectMouse.left,rectMouse.top=pygame.mouse.get_pos()
    if area.colliderect(rectMouse):
        huboColi=True
    return huboColi
def huboClikeo():
    huboClic=False
    click=pygame.mouse.get_pressed()
    if click[0]==1:
        huboClic=True 
    return huboClic


def huboClik_K():
    huboClicN=False
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key==K_k:
                huboClicN=True

    return huboClicN


def seDebeCerrarLaVentana():
    cerramos=False
    for evento in pygame.event.get():
        if evento.type == QUIT:
           cerramos=True
    return cerramos


def posicionamientoBoton(anchoVentana,area):
  pos=(anchoVentana-area[0])/2
  return pos


def textoBoton(tipoFuente,mensaje,color,BotonX,BotonY,Ancho,Alto,tamFuente):
  fuente=pygame.font.SysFont(tipoFuente,tamFuente)
  texto=fuente.render(mensaje,0,color)
  textoRect = texto.get_rect()
  textoRect.center=(BotonX+(Ancho/2),BotonY+(Alto/2))
  ventana.blit(texto,textoRect)


def mostrarMensaje(tipoFuente,tamFuente,posIniX,posIniY,mensaje,color):
    fuente=pygame.font.SysFont(tipoFuente,tamFuente)
    texto=fuente.render(mensaje,0,color)
    ventana.blit(texto,(posIniX,posIniY))


#********************** fin 13.2.2 Menú de opciones - clic tecla K************************
#----------------------------------2.2 INGRESAR PALABRAS------------------------



def cargarImagenesSimuAnimacion():
    listaImgenesHomero=[]
    i=3
    while i< 49: 
        nombreImag = 'Animacion/'+str(i)+'.png'
        imagHomero = pygame.image.load(nombreImag)
        imagHomero = pygame.transform.scale(imagHomero,(1254,636))
        listaImgenesHomero.append(imagHomero)
        i+=1
    return listaImgenesHomero

def mostrarImagenesSimuAnimacion(listaImgenesHomero,i,j,limite):
    posX = 0 
    posY = 0
    if i>limite : # por cada vuelta de j "i" va hasta 160 (espera mostrando la que está la posicion j)
          ventana.blit(listaImgenesHomero[j],(posX,posY))
          i=0 # i vuelve a 0 cuando llega al limite+1
          if j==40:
            pygame.mixer.music.load("musica/OUUCH.mp3")
            pygame.mixer.music.play(0,0)
            pygame.mixer.music.set_volume(1) 
          if j<45: # solo si j es menor al tamaño del vector
              j+=1 # j asmenta 1
    i+=1 # aumenta i en 1    
    return i,j               


def mostrarFondoHomeroFeliz():
    imagHomeroFeliz = pygame.image.load("ImagenesHomeroPartes/homeroFeliz.jpeg")
    imagHomeroFeliz = pygame.transform.scale(imagHomeroFeliz,(1254,636))
    ventana.blit(imagHomeroFeliz,(0,0))

def mostrarFondoHomeroEspera():
    imagHomeroEspera = pygame.image.load("ImagenesHomeroPartes/homeroEspera.jpeg")
    imagHomeroEspera = pygame.transform.scale(imagHomeroEspera,(1254,636))
    ventana.blit(imagHomeroEspera,(0,0))

def mostrarFondoVacio():
    imagFondoVacio = pygame.image.load("ImagenesHomeroPartes/fondoVacio.png")
    imagFondoVacio = pygame.transform.scale(imagFondoVacio,(1254,636))
    ventana.blit(imagFondoVacio,(0,0))

def cargarYmostrarImegenParteHomero(num):
    nombreImagPartes = 'ImagenesHomeroPartes/'+str(num)+'.png'
    imagHomeroPartes = pygame.image.load(nombreImagPartes)
    imagHomeroPartes = pygame.transform.scale(imagHomeroPartes,(1254,636))
    ventana.blit(imagHomeroPartes,(0,0))
#--nube 
nubeImagen= pygame.image.load("imagenesnubes/nube.png")
posXImagen=anchoVentana*6/100
posYImagen=altoVentana*-1/100
nubeImagen = pygame.transform.scale(nubeImagen,(283,150)) # tamaño origiinal de la immagen /4*3
posX1Imagen=50
posY1Imagen=40

velocidad=1
derecha=True

limiteMoverImagen=anchoVentana*81/100

#-- fin nube
def derteminarPosYLetra(posIniY,anVent,cantLs):
  pos=posIniY-determinarLargoGuion(anVent,cantLs) # tiene que quedar un poquito mas arriba que el guion
  if cantLs<=3: 
     pos+=8 #para bajar debe ser mas grande
  if cantLs==4:     
     pos+=5   
  if cantLs==5:
     pos+=7          
  if cantLs==6:
     pos+=4          
  if cantLs==7:
     pos+=7
  if cantLs==8:
     pos+=6
  if cantLs==9:     
     pos+=4   
  if cantLs>=10 and cantLs==11:
     pos+=7          
  if cantLs==12:
     pos+=6
  if cantLs==13:
     pos+=5          
  if cantLs==14:
     pos+=4
  if cantLs==15:
     pos+=3
  if cantLs>=16 and cantLs<=18:     
     pos+=7
  if cantLs==19:
     pos+=5  
  if cantLs>=20 and cantLs<=25:     
     pos+=7
  return pos


def determinarLargoGuion(anVent,cantLs):
  tam=0
  if cantLs==1: 
    tam= (anVent/cantLs)*4/100
  if cantLs==2:     
     tam= (anVent/cantLs)*8/100 
  if cantLs>=3 and cantLs<=4:     
     tam= (anVent/cantLs)*13/100 
  if cantLs>=5 and cantLs<=6:     
     tam= (anVent/cantLs)*18/100 
  if cantLs>6 and cantLs<=9:
     tam= (anVent/cantLs)*27/100
  if cantLs>=10 and cantLs<=15:     
     tam= (anVent/cantLs)*40/100
  if cantLs>=16 and cantLs<=19:     
     tam= (anVent/cantLs)*60/100 
  if cantLs>=20 and cantLs<=25:     
     tam= (anVent/cantLs)*80/100   
  return tam

tamFuLetra= determinarLargoGuion(anchoVentana,cantLetrasLimite)+4
fuente_letra=pygame.font.SysFont("Comic Sans",int(float(tamFuLetra)))

colorDeLaLetra=amarillo
letra_a=fuente_letra.render("A",0,colorDeLaLetra)
letra_b=fuente_letra.render("B",0,colorDeLaLetra)
letra_c=fuente_letra.render("C",0,colorDeLaLetra)
letra_d=fuente_letra.render("D",0,colorDeLaLetra)
letra_e=fuente_letra.render("E",0,colorDeLaLetra)
letra_f=fuente_letra.render("F",0,colorDeLaLetra)
letra_g=fuente_letra.render("G",0,colorDeLaLetra)
letra_h=fuente_letra.render("H",0,colorDeLaLetra)
letra_i=fuente_letra.render("I",0,colorDeLaLetra)
letra_j=fuente_letra.render("J",0,colorDeLaLetra)
letra_k=fuente_letra.render("K",0,colorDeLaLetra)
letra_l=fuente_letra.render("L",0,colorDeLaLetra)
letra_m=fuente_letra.render("M",0,colorDeLaLetra)
letra_n=fuente_letra.render("N",0,colorDeLaLetra)
letra_ñ=fuente_letra.render("Ñ",0,colorDeLaLetra)
letra_o=fuente_letra.render("O",0,colorDeLaLetra)
letra_p=fuente_letra.render("P",0,colorDeLaLetra)
letra_q=fuente_letra.render("Q",0,colorDeLaLetra)
letra_r=fuente_letra.render("R",0,colorDeLaLetra)
letra_s=fuente_letra.render("S",0,colorDeLaLetra)
letra_t=fuente_letra.render("T",0,colorDeLaLetra)
letra_u=fuente_letra.render("U",0,colorDeLaLetra)
letra_v=fuente_letra.render("V",0,colorDeLaLetra)
letra_w=fuente_letra.render("W",0,colorDeLaLetra)
letra_x=fuente_letra.render("X",0,colorDeLaLetra)
letra_y=fuente_letra.render("Y",0,colorDeLaLetra)
letra_z=fuente_letra.render("Z",0,colorDeLaLetra)

pygame.mixer.music.load("musica/los-simpson-intro (mp3cut.net).mp3")
pygame.mixer.music.play(0,0)
pygame.mixer.music.set_volume(0.5) 

lugarLetra=fuente_letra.render("",0,negro)

def creaListaVaciaLetras(cantLs,lstLet):
    i=0
    while i<cantLs:
      lstLet.insert(i,lugarLetra)
      i+=1

def ubicarLetra(lstLet,pos, letra):
    lstLet[pos]=letra
    pos+=1
    return lstLet,pos

def culcularAreaGuiones(anchoRect,altoRect,cantLs):
    area=(anchoRect+altoRect)*cantLs # le sumo el altoRect que es el espacio entre guiones
    return area

def posInicialEnX(anVent,anchoRect,altoRect,cantLs):
  anchoACubrir=culcularAreaGuiones(anchoRect,altoRect,cantLs)
  pos=(anVent-anchoACubrir)/2
  return pos

def dimencionesDelGuion(anVent,alVent,cantLs):
  altoRect = alVent*1/100
  anchoRect=determinarLargoGuion(anVent,cantLs)
  anchoRect-= altoRect # le resto el altoRect que va a ser el espacio entre guiones   
  return anchoRect,altoRect

def ubicacionDelPrimerGuion(anVent,alVent,cantLs):
  anchoRect, altoRect = dimencionesDelGuion(anVent,alVent,cantLs)
  posIniX= posInicialEnX(anVent,anchoRect,altoRect,cantLs)
  posIniY= alVent*56/100
  return anchoRect, altoRect,posIniX,posIniY


def crearYMostrarGuiones(vent,colorGuion,anVent,alVent,posicion,cantLs):
  anchoRect,altoRect,posIniX,posIniY=ubicacionDelPrimerGuion(anVent,alVent,cantLs)
  i=posicion
  while i<cantLs: 
     posDeX= posIniX+(i)*(anchoRect+altoRect)# 4 es la CANTIDAD y le sumo el altoRect que es el espacio entre guiones
     posDeY=posIniY+225
     guion = pygame.Rect(posDeX,posDeY,anchoRect,altoRect)
     pygame.draw.rect(vent,colorGuion,guion)
     i+=1



def derteminarPosXLetra(i,posIniX,anchoRect,altoRect):
  pos=posIniX+(i)*(anchoRect+altoRect)#  le sumo el altoRect que es el espacio entre guiones 
  return pos

def mostrarLetras(colorLetras,anVent,alVent,cantLs,lstLet):
  anchoRect,altoRect,posIniX,posIniY=ubicacionDelPrimerGuion(anVent,alVent,cantLs)
  i=0
  while i<cantLs: 
     posDeX=derteminarPosXLetra(i,posIniX,anchoRect,altoRect) 
     posDeY=derteminarPosYLetra(posIniY,alVent,cantLs) + 225
     ventana.blit(lstLet[i],(posDeX,posDeY))     
     i+=1
 

def movimientoDeImagen(der,posX,limMovImagen,vel):
  if der==True:
    if posX<limMovImagen:
      posX+=vel
    else:
      der=False
  else:
    if posX>0:
      posX-=vel
    else:
      der=True
  return der,posX,limMovImagen,vel



def pulsasionesDeTeclado(evento,posi,cantLetras,listaLetra,bandEnter,listaL):
  if evento.type == pygame.KEYDOWN:
     if posi<cantLetras or evento.key==K_BACKSPACE or evento.key==K_RETURN: #se accede hasta la catidad de letras de la palaba (de lo contraario se pasa del array), para dar enter o para borrar (si no estuviese así no me deja borrar la última letra)
        if evento.key==K_a:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_a)
          listaL.append('A')
        if evento.key==K_b:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_b)
          listaL.append('B')
        if evento.key==K_c:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_c)
          listaL.append('C')
        if evento.key==K_d:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_d)
          listaL.append('D')
        if evento.key==K_e:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_e)
          listaL.append('E')
        if evento.key==K_f:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_f)
          listaL.append('F')
        if evento.key==K_g:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_g)
          listaL.append('G')
        if evento.key==K_h:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_h)
          listaL.append('H')
        if evento.key==K_i:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_i)
          listaL.append('I')
        if evento.key==K_j:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_j)
          listaL.append('J')
        if evento.key==K_k:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_k)
          listaL.append('K')
        if evento.key==K_l:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_l)
          listaL.append('L')
        if evento.key==K_m:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_m)
          listaL.append('M')
        if evento.key==K_n:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_n)
          listaL.append('N')
        if evento.key==K_2:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_ñ)
          listaL.append('Ñ')
        if evento.key==K_o:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_o)
          listaL.append('O')
        if evento.key==K_p:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_p)
          listaL.append('P')
        if evento.key==K_q:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_q)
          listaL.append('Q')
        if evento.key==K_r:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_r)
          listaL.append('R')
        if evento.key==K_s:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_s)
          listaL.append('S')
        if evento.key==K_t:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_t)
          listaL.append('T')
        if evento.key==K_u:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_u)
          listaL.append('U')
        if evento.key==K_v:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_v)
          listaL.append('V')
        if evento.key==K_w:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_w)
          listaL.append('W')
        if evento.key==K_x:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_x)
          listaL.append('X')
        if evento.key==K_y:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_y)
          listaL.append('Y')  
        if evento.key==K_z:
          listaLetra,posi=ubicarLetra(listaLetra,posi,letra_z)
          listaL.append('Z')
        if evento.key==K_BACKSPACE:
            if posi>0: # es para que no agregue guiones a la izquierda
              posi-=1 # para borrar la ultima ingresada (ya que despues de ubicar la letra se suma 1 a posi)
              listaLetra,posi=ubicarLetra(listaLetra,posi,lugarLetra) # lugarletra es un espacio vacio
              listaL.pop()
              posi-=1 #aunque 2 lineas arriba reste 1 dentro de "ubicarLetra" se le suma 1 y como yo quiero que posi retroceda vuelvo a restar 1
              band=posi
        if evento.key==K_RETURN:
          bandEnter=1
  return posi,cantLetras,listaLetra,bandEnter,listaL

def capturarEventoYAccionar(posi,cantLetras,listaLetra,bandEnter,listaL):
    for evento in pygame.event.get():
        if evento.type == QUIT:
          pygame.quit()
          sys.exit()
        else:
          posi,cantLetras,listaLetra,bandEnter,listaL=pulsasionesDeTeclado(evento,posi,cantLetras,listaLetra,bandEnter,listaL)
    return posi,cantLetras,listaLetra,bandEnter,listaL     


def mostrarImagenEnMoviento(nube,posX,posY,posX1,posY1):
  ventana.blit(nube,(posX,posY))
  


#----------------------------------FIN 2.2 INGRESAR PALABRAS------------------------
#---------------------------------- 13.2.4 menu pricipal... ------------------------
                  
def mostrarReglas():
    amarillo=(255,255,0)
    celeste=(178,255,255)
    negro=(0,0,0)
    tipoFuenteR='Comic Sans MS'
    tamF=30
    posiX=10
    comensarAjugar='no'
    colorTexto = amarillo
    while True and comensarAjugar=='no':
      mostrarFondoVacio()
      mensaje='REGLAS: '
      mensaje2='a- Es para 2 jugadores,después de cada intento puede elegir seguir arriesgando por'
      mensaje3='   letra o arriesgar la palabra; si en el noveno intento no descifró la palabra, pierde.'
      mensaje4='b- El jugador 1 ingresa una palabra'
      mensaje5='c- El jugador 2 puede elegir arriesgar la palabra completa o arriesgar por letra'
      mensaje6='d- si arriesga palabra, gana (si acierta) o pierde (si no acierta)'
      mensaje7='e- si arriesga letra tiene 9 intentos (la letra que se repita no se cuenta)'
      mensaje8='f- después del noveno intento o de arriesgar la palabra pueden elegir seguir jugando'
      mensaje9='g- si salen del juego se mostrará todas las palabras descifradas y en cuantos intentos' 
      mensaje10='  se lograron cada una, o si no hay partidas ganadas que mostrar, se informará.'
      mensaje11='NOTA: para escribrir la letra Ñ debe usar el número 2.'
      mostrarMensaje("Arial Black",28,10,15,mensaje,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,55,mensaje2,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,95,mensaje3,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,135,mensaje4,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,175,mensaje5,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,215,mensaje6,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,255,mensaje7,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,295,mensaje8,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,335,mensaje9,colorTexto)
      mostrarMensaje(tipoFuenteR,tamF,posiX,375,mensaje10,colorTexto)
      mostrarMensaje("Arial Black",26,200,500,mensaje11,colorTexto)
      mensaje1 = 'Volver al menù'
      botVoverAlMenu=creaUnBoton(mensaje1,celeste,negro,40,570,200,55,25,"Comic Sans MS")
      if huboColisionConPuntero(botVoverAlMenu)==True:
          if huboClikeo()==True or huboClik_K()== True:
                comensarAjugar='si' # si acá llamaba a menuPrincipal al salir del menú volvia acá
      if seDebeCerrarLaVentana() == True:
          pygame.quit()
          sys.exit() # cerramos la ventana        
      pygame.display.update() # la ventana se va a estar actualizando

                                                                                                                                                        
def creaBotMenuIniYAcionar(tamP1,listaLetrasPalabra_1,cantLetrasLimite,palabra1,palabra2,listaP1,altoVentana,Letra, anchoVentana,ventana,color,color1,Posicionamiento,tam,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,limiteMoverImagen,velocidad):
     azul=(0,0,255)
     rojo=(255,0,0)
     amarillo=(255,255,0)
     celeste=(178,255,255)
     negro=(0,0,0)
     verdeFluor=(0,255,0)    
     boton = pygame.draw.rect(ventana,color,(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))
     if huboColisionConPuntero(boton)==True:
       boton = pygame.draw.rect(ventana,color1,(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))
       if huboClikeo()==True or huboClik_K()== True:
            pygame.mixer.music.stop()
            if color==rojo: # desarrollo del juego en si (antes era el main)
                palabra1,palabra2,tamP1,listaP1=turnoJugador1(palabra1,palabra2,tamP1,listaP1,ventana,blanco,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad,negro,anchoVentana,altoVentana,cantLetrasLimite,listaLetrasPalabra_1)
            if color==azul:                       
                mostrarReglas()
                pygame.mixer.music.load("musica/los-simpson-intro (mp3cut.net).mp3")
                pygame.mixer.music.play(0,0)
                pygame.mixer.music.set_volume(0.5)
                if seDebeCerrarLaVentana() == True:
                        pygame.quit()
                        sys.exit()
                        pygame.display.update()
            if color==amarillo:
                pygame.quit() 
                sys.exit()

     return palabra1,palabra2,tamP1,listaP1



def menuPrincipal(tamP1,listaLetrasPalabra_1,cantLetrasLimite,palabra1,palabra2,listaP1,altoVentana,Letra,anchoVentana,ventana,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,limiteMoverImagen,velocidad):
        azul=(0,0,255)
        blanco=(255,255,255)
        rojo=(255,0,0)
        amarillo=(255,255,0)
        celeste=(178,255,255)
        naranjado=(255,128,0)
        negro=(0,0,0)
        gris=(155,155,155)
        verdeFluor=(0,255,0)
        tamBoton=[220,55]
        xDboton=posicionamientoBoton(anchoVentana,tamBoton)-300
        Boton1= [xDboton,300]
        Boton2= [xDboton,360]
        Boton3= [xDboton,420]
        velocidad+=0.3
        while tamP1==0:
          mostrarFondoHomeroFeliz()
          mostrarImagenEnMoviento(nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen) #+++++++++++++++ 15.1
          derecha,posXImagen,limiteMoverImagen,velocidad=movimientoDeImagen(derecha,posXImagen,limiteMoverImagen,velocidad) #+++++++++++++++ 15.1
          palabra1,palabra2,tamP1,listaP1=creaBotMenuIniYAcionar(tamP1,listaLetrasPalabra_1,cantLetrasLimite,palabra1,palabra2,listaP1,altoVentana,Letra,anchoVentana,ventana,rojo,gris,Boton1,tamBoton,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,limiteMoverImagen,velocidad)
          palabra1,palabra2,tamP1,listaP1=creaBotMenuIniYAcionar(tamP1,listaLetrasPalabra_1,cantLetrasLimite,palabra1,palabra2,listaP1,altoVentana,Letra,anchoVentana,ventana,azul,gris,Boton2,tamBoton,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,limiteMoverImagen,velocidad)
          palabra1,palabra2,tamP1,listaP1=creaBotMenuIniYAcionar(tamP1,listaLetrasPalabra_1,cantLetrasLimite,palabra1,palabra2,listaP1,altoVentana,Letra,anchoVentana,ventana,amarillo,gris,Boton3,tamBoton,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,limiteMoverImagen,velocidad)
          textoBoton("Comic Sans MS","Iniciar",negro,Boton1[0],Boton1[1],tamBoton[0],tamBoton[1],30)
          textoBoton("Comic Sans MS","Reglas",negro,Boton2[0],Boton2[1],tamBoton[0],tamBoton[1],30)
          textoBoton("Comic Sans MS","Salir",negro,Boton3[0],Boton3[1],tamBoton[0],tamBoton[1],30)
          for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
              if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT  
                 pygame.quit() # detengo todos los módulos de pygame
                 sys.exit()
          pygame.display.update() # la ventana se va a estar actualizando
        return palabra1,palabra2,tamP1,listaP1          
#-------------------------------FIN 13.2.4 menu pricipal... ------------------------
#----------------------EL AHORCADO ------------------------------------------------
"""Describe esta función...
"""
def cifrarPalabra(lstP1):
  p2aux=''
  h=1
  tmP1 = len(lstP1)
  while h <= tmP1: # WHILE 2---------******************
    listaP2.insert(int(h - 1), '-')
    h = h + 1
        # CIERRA WHILE 2 -----------******************
  p2aux = ''.join(listaP2)
  return p2aux
"""Describe esta función...
"""
def Opciones(men, op1, op2, op3):
  global opci_C3_B3n, OpV_C3_A1lida
  opci_C3_B3n = input(str(men)).upper()
  if opci_C3_B3n == op1 or opci_C3_B3n == op2 or opci_C3_B3n == op3:
    OpV_C3_A1lida = opci_C3_B3n
  else:
    print()
    print(' Opción incorrecta')
    OpV_C3_A1lida = Opciones(men, op1, op2, op3)
  return OpV_C3_A1lida

"""Describe esta función...
"""
def est_C3_A1LaLetra(lista, Let): #arreglado*******************-----------
  global repetir, i
  repetir = False
  b = 1
  while b <= len(lista) and repetir == False:
      for i in lista:
        if i == Let:
         repetir = True
      b = b + 1
  return repetir

"""Describe esta función...
"""
def BuscarXletra(p1, Let, PxL, tam):
  global h, palabra1
  p1=list(p1) 
  PxL=list(PxL)
  h=0
  while h < tam:
       
       if p1[h]==Let:
          PxL[h]=palabra1 = ''.join(p1[h])

       h=h+1 
    # sale ['S', '-', '-', '-','-', '-']
  return PxL

"""Describe esta función...
"""
def compararPalabras(p1, p2):
  global igual 
  igual = 'no'
  if p1 == p2:
    igual = 'si'
  return igual



""" igual que la funcion "ingresoDeTexto(...)" pero muestra guiones (objetos de pygame) por ende lleva màs parametros solo de una letra
"""
def pedirIngresoUnaLetra(contador,palabra2,listaLetP2Pygame,vent,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel,anVent,alVent):
  azul=(0,0,255)
  blanco=(255,255,255)
  rojo=(255,0,0)
  amarillo=(255,255,0)
  celeste=(178,255,255)
  naranjado=(255,128,0)
  negro=(0,0,0)
  gris=(155,155,155)
  verdeClaro=(119,221,119)
  verdeFluor=(0,255,0)
  pos=0
  bandEnter=0
  derecha=True
  cantLs=1
  listaP2=[]
  while bandEnter==0:
    mostrarImagenEnMoviento(nube,posXIm,posYIm,posX1Im,posY1Im)
    if contador==0:
      mostrarFondoHomeroEspera()
    else:
      cargarYmostrarImegenParteHomero(contador)
    mensajeJ2_7_1(palabra2)
    mensajeJ2_7()
    crearYMostrarGuiones(vent,negro,anVent,alVent,pos,cantLs)
    mostrarLetras(negro,anVent,alVent,cantLs,listaLetP2Pygame)
    pos,cantLs,listaLetP2Pygame,bandEnter,listaP2=capturarEventoYAccionar(pos,cantLs,listaLetP2Pygame,bandEnter,listaP2)
    derecha,posXIm,limMovIm,vel=movimientoDeImagen(derecha,posXIm,limMovIm,vel)
    pygame.display.update()
  return listaP2,listaLetP2Pygame



"""Describe esta función...
"""

def Juega_x_Letra(vent,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel,anVent,alVent):
  global listaIntentos, men, listaP1, listaPalabra1, palabra2, Letra, repite, palabra1, contador, termin_C3_B3, listaLetra,letraEnPal1, contarRegistros, intentosPend, listaP2, tamP1, acert_C3_B3,  k
  listaP1 = ''.join(listaP1)
  """ si el jugador 1 ingresa la palabra "SOL", las variables llegan con estos valores 
   (listaP1)    guarda SOL
   (palabra2)   guarda ---
   (Letra)      guarda None
   (repite)     guarda None
   (palabra1)   guarda SOL
   (listaLetra) guarda [] ... acá va a guardar las latras que se ingresan pero NO están en la palabra
  """
  men='v'
  listaLetP2Pygame=[]
  cantLs=1
  creaListaVaciaLetras(cantLs,listaLetP2Pygame)
  Letra,listaLetP2Pygame=pedirIngresoUnaLetra(contador,palabra2,listaLetP2Pygame,vent,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel,anVent,alVent)# se pide una letra por vez
  Letra = ''.join(Letra)
  repite = est_C3_A1LaLetra(listaLetra, Letra)# busca en la lista la ultima letra ingresada e informa si ya se habia ingresado
  if repite==False: # si la letra inggresada NO estaba en la lista         
   listaLetra.insert(int(len(listaLetra)), Letra) # guardo la letra en la posisión "int(len(listaLetra)" es decir un entero que es el tamño de la listaLetra, también prodría haber usado el método append ()
  letraEnPal1 = est_C3_A1LaLetra(listaP1, Letra)
  if letraEnPal1 == False: # IF SI LA LETRA NO ESTÁ EN LA PALABRA
      men='N'
    #CIERRA IF SI LA LETRA NO ESTÁ EN LA PALABRA
    #si no se cumple "letraEnPal1+ == False" como la letra no está en la palabra, continuó
  if repite == False: # IF SI LA LETRA NUNCA SE INGRESÓ (es la primera vez, por ende no está repetida) modifica contadores
   contador = contador + 1 
   intentosPend = intentosPend - 1# hasta acá va bien
   listaP2 = BuscarXletra(listaP1, Letra, palabra2, tamP1)
   palabra1 = ''.join(listaP1)
   palabra2 = ''.join(listaP2) # hasta acá va bien
   acert_C3_B3 = compararPalabras(palabra1, palabra2)
   if acert_C3_B3 == 'si': # IF ACERTÓ LA PALABRA (LA COMPLETÓ)
    contarRegistros = contarRegistros + 1
    men='G' # ganó
    listaIntentos.append(contador)
    listaPalabra1.append(palabra1)
    termin_C3_B3 = 'si' # cierra IF ACERTÓ LA PALABRA (LA COMPLETÓ)
   else: # ELSE IF ACERTÓ LA PALABRA (LA COMPLETÓ)
       if men=='v': # if si la letra está en la palabra
        men='L' #muestra el logro
       else: #  si no la letra está en la palabra
        men='N' # informa que no está         
        # cierra ELSE IF ACERTÓ LA PALABRA (LA COMPLETÓ)
      # cierra IF SI LA LETRA NUNCA SE INGRESÓ
  else:  # ELSE IF SI LA LETRA NUNCA SE INGRESÓ
   men='R' #repite ingreso de letra (no modifica contadores)
        #CIERRA ELSE IF SI LA LETRA NUNCA SE INGRESÓ
  return men


"""Describe esta función...
"""
def formarY_OrdenarResultados(y, listaP1, listaInt):
  ListaDeResultados = []
  z = 0
  while z < y:
    elementoListaPal = listaP1[int(z)]
    elementoListaInt = listaInt[int(z)]
    uni_C3_B3n = 'La palabra  "'+elementoListaPal+'" se acertó en '+str(elementoListaInt)+' intento/s.   '
    ListaDeResultados.append(uni_C3_B3n)# El método append () agrega un elemento al final de la lista.  
    z = z + 1

  for i in range(1,len(listaInt)):
    for j in range(0,len(listaInt)-i):
        if(listaInt[j] > listaInt[j+1]):
            aux=listaInt[j]
            listaInt[j]=listaInt[j+1]
            listaInt[j+1]=aux
            aux=ListaDeResultados[j]
            ListaDeResultados[j]=ListaDeResultados[j+1]
            ListaDeResultados[j+1]=aux

  return ListaDeResultados


"""crea los botones menú permite al jugador 2 elejir arriesgar 
Palabra, ariesgar Letra o salir, y acciona según lo que elije  LINEA 129
"""
def botPalabLetOsalir(superficie,color,color1,Posicionamiento,tam,elije):
     azul=(0,0,255)
     rojo=(255,0,0)
     amarillo=(255,255,0)
     celeste=(178,255,255)
     negro=(0,0,0)
    
     boton = pygame.draw.rect(superficie,color,(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))
     if huboColisionConPuntero(boton)==True:
       boton = pygame.draw.rect(superficie,color1,(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))
       if huboClikeo()==True or huboClik_K()== True:
            if color==rojo:
                  elije='P'
            if color==celeste:
                  elije='L'
            if color==amarillo:
                  elije='F'
 
     return elije


"""arma un menú que me permite al jugador 2 elejir arriesgar Palabra, ariesgar Letra o salir y da mensajes mostrando la palabra a decifra
   muestra los distintos mensajes segun cada resultado de ingresar una letra y devuelve "termin_C3_B3 = 'si'" en caso de que gane jugando x letra...
"""
def menuPalabLetOsalir(mensBndera,Letra,palabra2,intentosPend,tamP1,ventana,elije,tamX,nubeImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,posXImagen,limiteMoverImagen,velo):
    global contador
    azul=(0,0,255)
    blanco=(255,255,255)
    rojo=(255,0,0)
    amarillo=(255,255,0)
    celeste=(178,255,255)
    naranjado=(255,128,0)
    negro=(0,0,0)
    gris=(155,155,155)
    verdeFluor=(0,255,0)
    tamBoton=[220,55]
    xDboton=posicionamientoBoton(anchoVentana,tamBoton)+200
    Boton1= [xDboton,300]
    Boton2= [xDboton,360]
    Boton3= [xDboton,420]
    elije=None
    velo+=0.4
    if mensBndera == 'N':
      pygame.mixer.music.load("musica/OUUCH.mp3")
      pygame.mixer.music.play(0,0)
      pygame.mixer.music.set_volume(1)
    if mensBndera != 'N' and contador>0 and mensBndera != 'R':
      contador -=1
      intentosPend +=1
      pygame.mixer.music.load("musica/Exacto.mp3")
      pygame.mixer.music.play(0,0)
      pygame.mixer.music.set_volume(1)
    while elije==None:
      if contador==0:
          mostrarFondoVacio()
      if contador> 0 and mensBndera=='L':
          mostrarFondoHomeroFeliz()
      if contador >0 and mensBndera!='L' and mensBndera!='primera':
          cargarYmostrarImegenParteHomero(contador)
      if mensBndera == 'primera':
         mensajeJ2_1()
         mensajeMostrarPalabra(palabra2,tamP1)
         xDboton=posicionamientoBoton(anchoVentana,tamBoton)+225
         Boton1= [xDboton,300]
         Boton2= [xDboton,360]
         Boton3= [xDboton,420]
      if mensBndera=='N':
         mensajeNoEstaLaLetra(Letra,palabra2,intentosPend)
      if mensBndera=='L':
         mensajeLogro(palabra2,intentosPend)
      if mensBndera=='R':
         mensajeRepiteIngresoLetra(Letra,palabra2,intentosPend)
      mostrarImagenEnMoviento(nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen)
      derecha,posXImagen,limiteMoverImagen,velo=movimientoDeImagen(derecha,posXImagen,limiteMoverImagen,velo)
      elije=botPalabLetOsalir(ventana,rojo,gris,Boton1,tamBoton,elije)
      elije=botPalabLetOsalir(ventana,celeste,gris,Boton2,tamBoton,elije)
      elije=botPalabLetOsalir(ventana,amarillo,gris,Boton3,tamBoton,elije)
      textoBoton("Arial Black","Arriesgar PALABRA",negro,Boton1[0],Boton1[1],tamBoton[0],tamBoton[1],20)
      textoBoton("Arial Black","Arriesgar LETRA",negro,Boton2[0],Boton2[1],tamBoton[0],tamBoton[1],20)
      textoBoton("Comic Sans MS","Salir del juego",negro,Boton3[0],Boton3[1],tamBoton[0],tamBoton[1],20)
      for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
          if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT  
             pygame.quit() # detengo todos los módulos de pygame
             sys.exit() # cerramos la ventana
      pygame.display.update() # la ventana se va a estar actualizando
    return elije,contador,intentosPend


"""Describe esta función...
"""
def mostrarResultadosOrdenados(ResultadosOrdenados,contarRegistros):
    azul=(0,0,255)
    blanco=(255,255,255)
    rojo=(255,0,0)
    amarillo=(255,255,0)
    celeste=(178,255,255)
    naranjado=(255,128,0)
    negro=(0,0,0)
    gris=(155,155,155)
    verdeFluor=(0,255,0)
    tamF=23
    posiX=10 
    tipoFuenteR='Comic Sans MS'
    nuevaPartida='NO'    
    while nuevaPartida=='NO':
      mostrarFondoVacio()
      mensajeTitulo1='RESULTADOS:'     
      mostrarMensaje("Arial Black",30,10,10,mensajeTitulo1,negro)
      mensajeTitulo2='('+str(contarRegistros)+' partidas ganadas ordenadas por intentos)'     
      mostrarMensaje("Arial Black",24,400,10,mensajeTitulo2,negro)
      i=0
      yDelMensaje=33
      while i<contarRegistros:
          mensaje1=str(i+1)+') ' + str(ResultadosOrdenados[i])
          yDelMensaje+=30                        
          mostrarMensaje(tipoFuenteR,tamF,posiX,yDelMensaje,mensaje1,verdeFluor)
          i+=1
      mensajeSal = 'Salir del Juego'          
      botSalirJ=creaUnBoton(mensajeSal,celeste,negro,50,500,220,55,28,"Comic Sans MS")
      if huboColisionConPuntero(botSalirJ)==True:
          if huboClikeo()==True or huboClik_K()== True:
                  pygame.quit()
                  sys.exit() # SE SALE DEL JUEGO     ....    anchoVentana=1254     altoVentana=636 
      mensajeV = 'Nueva partida'  # mensaje,colorBot1,colorBot2,posIniX,posIniY,anchoRect, altoRect,tamLetra,tipoFuente
      botVoverAlMenu=creaUnBoton(mensajeV,verdeFluor,negro,980,500,220,55,28,"Comic Sans MS")
      if huboColisionConPuntero(botVoverAlMenu)==True:
          if huboClikeo()==True or huboClik_K()== True:
                  nuevaPartida='si'
      if seDebeCerrarLaVentana() == True:
          pygame.quit()
          sys.exit() # cerramos la ventana        
      pygame.display.update() # la ventana se va a estar actualizando
    return nuevaPartida 
  
#-------------------------------------FIN EL AHORCADO ----------------------------------------

#-------------------------------------13.2.3 menú de opciones - clic K 2 botones ----------------------------------------
"""esta funcion crea los botenes y permite el caambio de color, elegir y acciona en consecuencia
"""
def botPartidaOsalir(ResultadosOrdenados,contarRegistros,terminaJuego,superficie,color,color1,Posicionamiento,tam):
    azul=(0,0,255)
    rojo=(255,0,0)
    amarillo=(255,255,0)
    celeste=(178,255,255)
    negro=(0,0,0)
    azul=(0,0,255)
    naranjado=(255,128,0)
    boton = pygame.draw.rect(superficie,color,(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))
    if huboColisionConPuntero(boton)==True:
      boton = pygame.draw.rect(superficie,color1,(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))
      if huboClikeo()==True or huboClik_K()== True:
           if color==naranjado:
               terminaJuego='si'
           if color==verdeFluor:
               terminaJuego=mostrarResultadosOrdenados(ResultadosOrdenados,contarRegistros)  
           if color==amarillo:
               pygame.quit() 
               sys.exit()
    return terminaJuego

"""esta función da opciones para continuar y muestra los distintos mensajes segun cada resultado de jugar por palabra...
"""
def resultadosYmenuPartidaOsalir(ResultadosOrdenados,contarRegistros,palabra2,resp,vent,anVent,alVent,cantLs,listaLetra,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel):
    vel+=0.5
    azul=(0,0,255)
    azulClaro=(0,170,228)
    blanco=(255,255,255)
    rojo=(255,0,0)
    amarillo=(255,255,0)
    celeste=(178,255,255)
    naranjado=(255,128,0)
    negro=(0,0,0)
    gris=(155,155,155)
    verdeClaro=(119,221,119)
    verdeFluor=(0,255,0)
    tamBoton=[220,55]
    xDboton=posicionamientoBoton(anVent,tamBoton)+325
    Boton2= [xDboton,280]
    Boton3= [xDboton,340]
    tamBoton4=[300,35]
    xDboton4=anVent-(tamBoton4[0]+30)
    yDboton4=alVent-(tamBoton4[1]+45)
    Boton4= [xDboton4,yDboton4]
    derecha=True
    terminaJuego='no'
    i=0
    j=0
    demora=10
    listaImgenesHomero=[]
    listaImgenesHomero = cargarImagenesSimuAnimacion()
    banderaCagaFondo=0

    if resp=='G' or resp=='GL' or resp =='pierdIntentos':
                      banderaCagaFondo=1
    if resp!='G' and resp!='GL' and resp!='pierdIntentos': # es cuando pierde por palabra
                      banderaCagaFondo=1
    if resp=='G' or resp=='GL':
      pygame.mixer.music.load("musica/UIii.mp3")
      pygame.mixer.music.play(0,0)
      pygame.mixer.music.set_volume(1)

    while terminaJuego=='no':
      if resp=='G' or resp=='GL':
           derecha,posXIm,limMovIm,vel=movimientoDeImagen(derecha,posXIm,limMovIm,vel)
           mostrarImagenEnMoviento(nube,posXIm,posYIm,posX1Im,posY1Im)
      if banderaCagaFondo==0:  # si no hay que una pantalla que tenga ver con algún resultado en particular
           vent.fill(azulClaro) # pone esto
      if contarRegistros==0:
         mensajeNoHayPartidasGanadas()
      if resp=='pierdIntentos':
         i,j=mostrarImagenesSimuAnimacion(listaImgenesHomero,i,j,demora)
         mensajePierdePorIntentos()
      if resp=='GL':
         mostrarFondoHomeroFeliz()
         mensajeGanaPorLetra()
      if resp=='G':
         mostrarFondoHomeroFeliz()
         mensajeGanaPorPal()
      if resp!='G' and resp!='GL' and resp!='pierdIntentos':
         i,j=mostrarImagenesSimuAnimacion(listaImgenesHomero,i,j,demora)
         mensajePierdePorPal(palabra2)
      mostrarLetras(negro,anVent,alVent,cantLs,listaLetra)
      terminaJuego=botPartidaOsalir(ResultadosOrdenados,contarRegistros,terminaJuego,vent,naranjado,gris,Boton2,tamBoton)
      terminaJuego=botPartidaOsalir(ResultadosOrdenados,contarRegistros,terminaJuego,vent,amarillo,gris,Boton3,tamBoton)
      textoBoton("Arial Black","Nueva Partida",negro,Boton2[0],Boton2[1],tamBoton[0],tamBoton[1],20)
      textoBoton("Comic Sans MS","Salir del Juego",negro,Boton3[0],Boton3[1],tamBoton[0],tamBoton[1],20)
      if contarRegistros>0:
            terminaJuego=botPartidaOsalir(ResultadosOrdenados,contarRegistros,terminaJuego,vent,verdeFluor,gris,Boton4,tamBoton4)
            textoBoton("Arial Black","Ver las partidas ganadas",negro,Boton4[0],Boton4[1],tamBoton4[0],tamBoton4[1],19)
      for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
          if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT  
             pygame.quit() # detengo todos los módulos de pygame
             sys.exit() # cerramos la ventana
      pygame.display.update() # la ventana se va a estar actualizando
    return terminaJuego
#-------------------------------------fin 13.2.3 menú de opciones - clic K 2 botones ----------------------------------------
#------------------------------MEZCLA------------------------------------------------------


def texto_mensaje(tipoFuente,tamFuente,color,mensaje):
  fuente=pygame.font.SysFont(tipoFuente,tamFuente)
  texto=fuente.render(mensaje,0,color)
  return texto

def mensajeJ1_1():
  ventana.blit(texto_mensaje('Comic Sans',45,verdeFluor,"Jugador 1 ingrese una palabra: "),(12,175))

def mensajeJ2_1():
  ventana.blit(texto_mensaje("Comic Sans",45,negro,"Jugador 2, elija una opción"),(230,240))

def mensajeJ2_2(cantLs):
  ventana.blit(texto_mensaje('Comic Sans',45,negro,'Jugador 2 ingrese una palabra de '+str(cantLs)+' letras'),(100,130))

def mensajeMostrarPalabra(palabraCifrada,tamP1):
  ventana.blit(texto_mensaje("Comic Sans",45,negro,' La palabra a descifrar es:  '+ palabraCifrada+' (y tiene '+ str(tamP1)+' letras)'),(165,200))

def mensajeGanaPorPal():
  ventana.blit(texto_mensaje('Arial Black',35,verdeFluor," *** Ganó el jugador 2, acertó la palabra ***"),(120,100))

def mensajePierdePorPal(palabra2):
  ventana.blit(texto_mensaje("Arial Black",26,verdeFluor,' Perdió, usted ingresó  "'+palabra2+'" y la palabra correcta era la que se muestra'),(10,510))

def mensajeJ2_7():
  ventana.blit(texto_mensaje('Comic Sans',40,negro,"Jugador 2 ingrese una letra: "),(70,190))

def mensajeJ2_7_1(palabra2):
  ventana.blit(texto_mensaje("Comic Sans",45,negro,' Logró descifrar esto '+palabra2),(70,160))

def mensajeJ2_8(Letra):
  ventana.blit(texto_mensaje('Comic Sans',45,negro,'La letra  ->"'+Letra+'"<-  no está en la palabra'),(20,180))

def mensajeLogro(palabra2,intentosPend):
  ventana.blit(texto_mensaje("Comic Sans",40,negro,' Logró descifrar '+palabra2+' le quedan '+ str(intentosPend)+' intentos'),(20,210))

def mensajeNoEstaLaLetra(Letra,palabra2,intentosPend):
    mensajeJ2_8(Letra)
    mensajeLogro(palabra2,intentosPend)

def mensajeJ2_10(Letra):
  ventana.blit(texto_mensaje('Comic Sans',40,negro,'La letra  ->"'+Letra+'"<- ya se había ingresado'),(20,180))

def mensajeRepiteIngresoLetra(Letra,palabra2,intentosPend):
    mensajeJ2_10(Letra)
    mensajeLogro(palabra2,intentosPend)  

def mensajeJ2_11():
  ventana.blit(texto_mensaje('Arial Black',32,verdeFluor," Perdió por agotar los 9 intentos posibles"),(30,445))

def mensajeJ2_12():
  ventana.blit(texto_mensaje("Arial Black",32,verdeFluor," y la palabra correcta era la que se muestra "),(30,470))

def mensajeGanaPorLetra():
  ventana.blit(texto_mensaje('Arial Black',35,verdeFluor," *** Ganó el jugador 2, completó la palabra ***"),(120,100))

def mensajePierdePorIntentos():
    mensajeJ2_11()
    mensajeJ2_12()

def mensajeNoHayPartidasGanadas():
    ventana.blit(texto_mensaje('Arial Black',23,negro," No hay partidas ganadas"),(900,570))
      
""" esta función permite ingresar texto (lista de letras) como obeto de pygame y como caracter común tambien me da el tamaño de la lista 
"""
def ingresoDeTexto(vent,colorVent,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel,colorLet,anVent,alVent,cantLs,listaLetra,listaP1):
  pos=0
  bandEnter=0
  derecha=True
  while bandEnter==0:
    mostrarImagenEnMoviento(nube,posXIm,posYIm,posX1Im,posY1Im)
    mostrarFondoHomeroEspera()
    mensajeJ1_1()
    mostrarLetras(colorLet,anVent,alVent,cantLs,listaLetra)
    pos,cantLs,listaLetra,bandEnter,listaP1=capturarEventoYAccionar(pos,cantLs,listaLetra,bandEnter,listaP1)
    derecha,posXIm,limMovIm,vel=movimientoDeImagen(derecha,posXIm,limMovIm,vel)
    pygame.display.update()
  return pos,listaLetra,bandEnter,listaP1


""" igual que la funcion "ingresoDeTexto(...)" pero muestra guiones (objetos de pygame) por ende lleva màs parametros
"""
def ingresoDeTexto_J2_palabra(vent,colorVent,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel,colorLet,anVent,alVent,cantLs,listaLetra,listaP2):
  global palabra2,tamP1
  pos=0
  bandEnter=0
  derecha=True
  while bandEnter==0:
    mostrarFondoHomeroEspera()
    mostrarImagenEnMoviento(nube,posXIm,posYIm,posX1Im,posY1Im)
    mensajeJ2_2(cantLs)
    mensajeMostrarPalabra(palabra2,tamP1)
    crearYMostrarGuiones(vent,colorLet,anVent,alVent,pos,cantLs)
    mostrarLetras(colorLet,anVent,alVent,cantLs,listaLetra)
    pos,cantLs,listaLetra,bandEnter,listaP2=capturarEventoYAccionar(pos,cantLs,listaLetra,bandEnter,listaP2)
    derecha,posXIm,limMovIm,vel=movimientoDeImagen(derecha,posXIm,limMovIm,vel)
    pygame.display.update()
  return pos,listaLetra,bandEnter,listaP2


"""Describe esta función... Linea 497
"""
def Juega_x_Palabra(vent,colorVent,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel,colorLet,anVent,alVent,cantLs,listaLetra):
  global listaIntentos, listaPalabra1, palabra2, adivin_C3_B3, palabra1, contador, contarRegistros
  listaPalab2=[]
  tamP1,listaLetrasPalabra_2,NoUsoLoDevulto,listaPalab2=ingresoDeTexto_J2_palabra(vent,colorVent,nube,posXIm,posYIm,posX1Im,posY1Im,limMovIm,vel,colorLet,anVent,alVent,cantLs,listaLetra,listaPalab2)
  palabra2 = ''.join(listaPalab2)
  gana_J2='N'
  adivin_C3_B3 = compararPalabras(palabra1, palabra2)
  if adivin_C3_B3 == 'si':
    contador = contador + 1
    contarRegistros = contarRegistros + 1
    gana_J2='G'
    listaIntentos.append(contador)
    listaPalabra1.append(palabra1)
  return gana_J2

"""Describe esta función...
"""
def turnoJugador1(palabra1,palabra2,tamP1,listaP1,ventana,blanco,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad,negro,anchoVentana,altoVentana,cantLetrasLimite,listaLetrasPalabra_1):
    listaP1=[]
    tamP1,listaLetrasPalabra_1,jugadaDelJugador_1,listaP1=ingresoDeTexto(ventana,blanco,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad,negro,anchoVentana,altoVentana,cantLetrasLimite,listaLetrasPalabra_1,listaP1)
    palabra1 = ''.join(listaP1)
    palabra2=cifrarPalabra(listaP1)
    return palabra1,palabra2,tamP1,listaP1


#-------------------------------------------------FIN MEZCLA------------------------------------------------------

#-----------------------
# MAIN----------------------------------------------------------------*************************
#----------------------
listaIntentos = []
listaPalabra1 = []
seJuega = 'S'
x = 1
contarRegistros = 0
primeraEntrada = 'siPrimera'
while seJuega == 'S': # WHILE 1--------------+++++++++++++++++
  listaLetra = []
  limiteDeIntentos=9 #  SI SE CAMBIA SE ALTERARÁ EL ORDEN DE MOSTRAR LAS IMAGENES DE CADA RESULTADO (ver en menuPalabLetOsalir  numeroDeImagen = 9 intentosPend)
  intentosPend = limiteDeIntentos
  contador = 0
  termin_C3_B3 = 'no'
  tamP1 = 0
  verdeFluor=(0,255,0)
  azul=(0,0,255)
  blanco=(255,255,255)
  rojo=(255,0,0)
  amarillo=(255,255,0)
  celeste=(178,255,255)
  negro=(0,0,0)
  gris=(155,155,155)
  listaLetrasPalabra_1=[]
  creaListaVaciaLetras(cantLetrasLimite,listaLetrasPalabra_1)
  listaLetrasPalabra_2=[]
  listaP2 = []
  mostrarImagenEnMoviento(nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen)
  derecha,posXImagen,limiteMoverImagen,velocidad=movimientoDeImagen(derecha,posXImagen,limiteMoverImagen,velocidad)
  mostrarFondoHomeroEspera()
  if primeraEntrada == 'siPrimera':
     palabra1,palabra2,tamP1,listaP1=menuPrincipal(tamP1,listaLetrasPalabra_1,cantLetrasLimite,palabra1,palabra2,listaP1,altoVentana,Letra,anchoVentana,ventana,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,limiteMoverImagen,velocidad)
     primeraEntrada = 'NOP'   
  else:
     palabra1,palabra2,tamP1,listaP1=turnoJugador1(palabra1,palabra2,tamP1,listaP1,ventana,blanco,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad,negro,anchoVentana,altoVentana,cantLetrasLimite,listaLetrasPalabra_1)
  gana='N'
  mensajeBnderaPLS='primera' # podia ser cualquier cosa excepto N, R, L 
  while termin_C3_B3 == 'no': # WHILE 3 -------*********** 
    elije,contador,intentosPend = menuPalabLetOsalir(mensajeBnderaPLS,Letra,palabra2,intentosPend,tamP1,ventana,elije,anchoVentana,nubeImagen,posYImagen,posX1Imagen,posY1Imagen,derecha,posXImagen,limiteMoverImagen,velocidad)
    if elije != 'F': #IF 3 (SI NO elige finalizar el juego)
     if elije == 'L': #IF 3.1 (elige jugar por letra)
      res = Juega_x_Letra(ventana,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad,anchoVentana,altoVentana)
      gana=res
      ResultadosOrdenados = formarY_OrdenarResultados(contarRegistros, listaPalabra1, listaIntentos)
      mensajeBnderaPLS=res # res es lo que se obtiene como respesta de ingresar una letra y mensajeBnderaPLS la uso para los distintos mensajes en menuPalabLetOsalir
      if res=='G':
         respuesta='GL'
         termin_C3_B3= resultadosYmenuPartidaOsalir(ResultadosOrdenados,contarRegistros,palabra2,respuesta,ventana,anchoVentana,altoVentana,tamP1,listaLetrasPalabra_1,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad)         
          # si el jugador 2 gana sale del while (termina)
               #CIERRA IF 3.1
     else:# ELSE if 3.1 (elige jugar por palabra)
      creaListaVaciaLetras(tamP1,listaLetrasPalabra_2)
      resultadoP=Juega_x_Palabra(ventana,blanco,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad,negro,anchoVentana,altoVentana,tamP1,listaLetrasPalabra_2)
      gana=resultadoP
      ResultadosOrdenados = formarY_OrdenarResultados(contarRegistros, listaPalabra1, listaIntentos)
      termin_C3_B3 =resultadosYmenuPartidaOsalir(ResultadosOrdenados,contarRegistros,palabra2,resultadoP,ventana,anchoVentana,altoVentana,tamP1,listaLetrasPalabra_1,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad)
      # CIERRA ELSE if 3.1
     if contador == limiteDeIntentos: #IF 4 si el jugador llega al limite de intentos (contador=9)
          if gana!='G': # si no ganó al llegar al limite de intentos (contador=9)
               menPierdeXIntentos='pierdIntentos'
               ResultadosOrdenados = formarY_OrdenarResultados(contarRegistros, listaPalabra1, listaIntentos)
               termin_C3_B3 = resultadosYmenuPartidaOsalir(ResultadosOrdenados,contarRegistros,palabra2,menPierdeXIntentos,ventana,anchoVentana,altoVentana,tamP1,listaLetrasPalabra_1,nubeImagen,posXImagen,posYImagen,posX1Imagen,posY1Imagen,limiteMoverImagen,velocidad)
          termin_C3_B3 ='Si' #gane o pierda si llega a limite sale del WHILE (cierra while 3)       
             #CIERRA IF 4
    else: # ELSE IF 3 (SI elige finalizar el juego)
      termin_C3_B3 = 'si'
      pygame.quit() # detengo todos los módulos de pygame
      sys.exit() # cerramos la ventana
  if seDebeCerrarLaVentana()==True:
       pygame.quit() # detengo todos los módulos de pygame
       sys.exit() # cerramos la ventana
   # CIERRA WHILE 3 -------***********
  pygame.display.update()
 # CIERRA WHILE 1 ----------+++++++++++++++++++++++++++