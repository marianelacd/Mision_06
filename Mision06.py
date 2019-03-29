#Autor: Marianela Contreras
#Mision 06. Programa para dibujar con un espirógrafo.

import math
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

#función que dibujará la figura con el espirógrafo, mandando como parámetros r,R,l.
# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw



        k = r/R
        for angulo in range (0,360*r//math.gcd(r,R),1):
            theta=math.radians(angulo)
            x = int(R*(((1-k)* math.cos(theta))+((l*k)*math.cos(((1-k)/k)*theta))))
            y = int(R*(((1-k)* math.sin(theta))-((l*k)*math.sin(((1-k)/k)*theta))))
            pygame.draw.circle(ventana, ROJO, (x+ANCHO//2, ALTO//2 - y), 1)



            pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r= int(input("Introduzca r: "))
    R= int(input("Introduzca R: "))
    l= float(input("Introduzca l: "))
    dibujar(r,R,l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()