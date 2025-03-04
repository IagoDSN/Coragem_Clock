import pygame
import sys
import time
import threading
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Coragem's Clock")

clock = pygame.time.Clock()

icon = pygame.image.load("clock.png")
pygame.display.set_icon(icon)

fundofal = pygame.image.load("fundo.png")
fundo_rect = fundofal.get_rect()
screen_rect = screen.get_rect()
fundo_rect.center = screen_rect.center

screen_width, screen_height = screen.get_size()

alt = (screen_height - 600) // 2
lat = (screen_width - 80) // 2
quada = (screen_height - 250) // 2
quadl = (screen_width - 350) // 2

btn1 = pygame.Rect(20, 500, 150, 60)
btn2 = pygame.Rect(220, 500, 150, 60)
btn3 = pygame.Rect(420, 500, 150, 60)
btn4 = pygame.Rect(630, 500, 150, 60)
positivo = False
cont = 0
start_cps_time = None
contage = 0
duration = 0
mintus, second = " ", " "
secus, minus = 0, 0

input_box = pygame.Rect(300, 350, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
textes = ''
fonton = pygame.font.Font(None, 32)
negativo = True

principal = pygame.Rect((screen_width//2)-125, 350, 250, 60)
central = pygame.Rect(quadl, quada, 350, 150)

def draw_button(screen, rect, text, font):
    pygame.draw.rect(screen, (30, 30, 30), rect)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

pause_button_rect = pygame.Rect(420, 350, 150, 60)
reset_button_rect = pygame.Rect(220, 350, 150, 60)

# Função Alarme
def alarm():
    global duration, negativo, minus, secus, mintus, second
    mintus, second = " ", " "
    secus, minus = 0, 0
    for minus in range(duration-1, -1, -1):
        mintus = str(minus)
        for secus in range(59, -1 , -1):
            time.sleep(1)
            second = str(secus)
    print("Alarme!")
    pygame.mixer.init()
    pygame.mixer.music.load("alarme.mp3")
    pygame.mixer.music.play()
    time.sleep(40)
    negativo = True
def startar():
    global countdown_thread
    countdown_thread = threading.Thread(target=alarm)
    countdown_thread.start()

start_time = None
elapsed_time = 0
paused = True
#Função cronometro
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Loop 1
font = pygame.font.SysFont('arial', 80)
fontes = pygame.font.SysFont('arial', 40)
fontcq = pygame.font.SysFont('arial', 25)

def room1():
    global paused, start_time, elapsed_time
    runner = True
    while runner:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if btn2.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room2()
                elif btn4.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room4()
                elif btn3.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room3()

        now = datetime.now()
        data = now.strftime("%d/%m/%Y")
        agora = now.strftime("%H:%M:%S")

        # Função Draw:
        screen.fill((34, 45, 89))
        fundo = pygame.transform.scale(fundofal, (80, 80))
        screen.blit(fundo, (lat, alt))
        pygame.draw.rect(screen, (30, 30, 30), (quadl, quada, 350, 150))
        text1 = font.render(agora, 1, (255, 255, 255))
        screen.blit(text1, (240, 210))
        text2 = fontes.render(data, 1, (255, 255, 255))
        screen.blit(text2, (300, 330))

        pygame.draw.rect(screen, (30, 30, 30), btn1)
        pygame.draw.rect(screen, (30, 30, 30), btn2)
        pygame.draw.rect(screen, (30, 30, 30), btn3)
        pygame.draw.rect(screen, (30, 30, 30), btn4)
        text3 = fontcq.render("Relógio", 1, (255, 255, 255))
        screen.blit(text3, (50, 515))
        text4 = fontcq.render("Cronômetro", 1, (255, 255, 255))
        screen.blit(text4, (230, 515))
        text5 = fontcq.render("Alarme", 1, (255, 255, 255))
        screen.blit(text5, (455, 515))
        text6 = fontcq.render("CPS", 1, (255, 255, 255))
        screen.blit(text6, (680, 515))
        pygame.display.update()

# Loop 2
def room2():
    global paused, start_time, elapsed_time
    runner = True
    while runner:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if pause_button_rect.collidepoint(event.pos):
                    if paused:
                        paused = False
                        start_time = time.time() - elapsed_time
                    else:
                        paused = True
                        elapsed_time = time.time() - start_time
                elif btn1.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room1()
                elif btn4.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room4()
                elif btn3.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room3()
                elif reset_button_rect.collidepoint(event.pos):
                    start_time = None
                    elapsed_time = 0
                    paused = True

        if not paused:
            current_time = time.time()
            total_elapsed_time = current_time - start_time
        else:
            total_elapsed_time = elapsed_time

        # Função Draw:
        screen.fill((34, 45, 89))
        fundo = pygame.transform.scale(fundofal, (80, 80))
        screen.blit(fundo, (lat, alt))
        pygame.draw.rect(screen, (30, 30, 30), (quadl, quada, 350, 150))

        time_text = font.render(format_time(int(total_elapsed_time)), True, (255, 255, 255))
        screen.blit(time_text, (240, 210))
        draw_button(screen, pause_button_rect, "Continuar" if paused else "Pausar", fontcq)
        draw_button(screen, reset_button_rect, "Resetar", fontcq)

        pygame.draw.rect(screen, (30, 30, 30), btn1)
        pygame.draw.rect(screen, (30, 30, 30), btn2)
        pygame.draw.rect(screen, (30, 30, 30), btn3)
        pygame.draw.rect(screen, (30, 30, 30), btn4)
        text3 = fontcq.render("Relógio", 1, (255, 255, 255))
        screen.blit(text3, (50, 515))
        text4 = fontcq.render("Cronômetro", 1, (255, 255, 255))
        screen.blit(text4, (230, 515))
        text5 = fontcq.render("Alarme", 1, (255, 255, 255))
        screen.blit(text5, (455, 515))
        text6 = fontcq.render("CPS", 1, (255, 255, 255))
        screen.blit(text6, (680, 515))
        pygame.display.update()

#Loop 3
def room3():
    global paused, start_time, elapsed_time, active, textes, color, duration, negativo, minus, secus, mintus, second
    runner = True
    while runner:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if btn2.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room2()
                elif btn1.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room1()
                elif btn4.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room4()
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(textes)
                        duration = int(textes)
                        textes = ''
                        if negativo == True:
                            negativo = False
                            startar()
                    elif event.key == pygame.K_BACKSPACE:
                        textes = textes[:-1]
                    else:
                        if event.unicode.isdigit():
                            temp_text = textes + event.unicode
                            if int(temp_text) <= 600:
                                textes += event.unicode

        # Função Draw:
        screen.fill((34, 45, 89))

        txt_surface = fonton.render(textes, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        textx = fontcq.render("Digite os minutos", 1, (255, 255, 255))
        screen.blit(textx, (300, 385))
        
        fundo = pygame.transform.scale(fundofal, (80, 80))
        screen.blit(fundo, (lat, alt))
        pygame.draw.rect(screen, (30, 30, 30), (quadl, quada, 350, 150))

        textomin = font.render(mintus, 1, (255, 255, 255))
        screen.blit(textomin, (270, 210))
        textosec = font.render(second, 1, (255, 255, 255))
        screen.blit(textosec, (430, 210))

        pygame.draw.rect(screen, (30, 30, 30), btn1)
        pygame.draw.rect(screen, (30, 30, 30), btn2)
        pygame.draw.rect(screen, (30, 30, 30), btn3)
        pygame.draw.rect(screen, (30, 30, 30), btn4)
        text3 = fontcq.render("Relógio", 1, (255, 255, 255))
        screen.blit(text3, (50, 515))
        text4 = fontcq.render("Cronômetro", 1, (255, 255, 255))
        screen.blit(text4, (230, 515))
        text5 = fontcq.render("Alarme", 1, (255, 255, 255))
        screen.blit(text5, (455, 515))
        text6 = fontcq.render("CPS", 1, (255, 255, 255))
        screen.blit(text6, (680, 515))
        pygame.display.update()

# Loop 4 
def room4():
    global paused, start_time, elapsed_time, positivo, cont, start_cps_time, contage
    valor = "0.00"
    runner = True
    while runner:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if btn1.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room1()
                elif btn2.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room2()
                elif btn3.collidepoint(mouse_x, mouse_y):
                    runner = False
                    room3()
                elif principal.collidepoint(mouse_x, mouse_y):
                    if not positivo:
                        positivo = True
                        cont = 0
                        time.sleep(1)
                        start_cps_time = time.time()
                if central.collidepoint(mouse_x, mouse_y) and positivo:
                    cont += 1

        if positivo:
            elapsed_time = time.time() - start_cps_time
            if elapsed_time >= 5:
                positivo = False
                cps_value = cont / 5
                contage = cps_value
                valor = f"{cps_value:.2f}" 

        # Função Draw:
        screen.fill((34, 45, 89))
        fundo = pygame.transform.scale(fundofal, (80, 80))
        screen.blit(fundo, (lat, alt))
        pygame.draw.rect(screen, (30, 30, 30), central)
        pygame.draw.rect(screen, (30, 30, 30), principal)
        if positivo:
            centro = fontes.render(str(cont), 1, (255, 255, 255))
            screen.blit(centro, (375, 230))
            centro = fontes.render(str(int(5 - elapsed_time)), 1, (255, 255, 255))
            screen.blit(centro, (385, 360))
        else:
            centro = fontes.render("INICIAR", 1, (255, 255, 255))
            screen.blit(centro, (325, 360))
            centro = font.render(valor, 1, (255, 255, 255))
            screen.blit(centro, (325, 210))

        pygame.draw.rect(screen, (30, 30, 30), btn1)
        pygame.draw.rect(screen, (30, 30, 30), btn2)
        pygame.draw.rect(screen, (30, 30, 30), btn3)
        pygame.draw.rect(screen, (30, 30, 30), btn4)
        text3 = fontcq.render("Relógio", 1, (255, 255, 255))
        screen.blit(text3, (50, 515))
        text4 = fontcq.render("Cronômetro", 1, (255, 255, 255))
        screen.blit(text4, (230, 515))
        text5 = fontcq.render("Alarme", 1, (255, 255, 255))
        screen.blit(text5, (455, 515))
        text6 = fontcq.render("CPS", 1, (255, 255, 255))
        screen.blit(text6, (680, 515))
        pygame.display.update()

room1()

pygame.quit()
sys.exit()