import pygame
import pygame_gui
import math

pygame.init()

screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ряд Фурье для функции sin(x)')

gui_manager = pygame_gui.UIManager((screen_width, screen_height))

white = (255, 255, 255)  # индексы цветов белый и черный
black = (0, 0, 0)


def fourier_sin(x, n):  # фурье для функции синуса
    result = 0
    for i in range(1, n + 1):
        result += (1 / i) * math.sin(i * x)
    return result


# num_ins = 1  # настройки
animation_speed = 1
x = 0
dt = 0.05

pygame_gui.elements.UILabel(relative_rect=pygame.Rect((8, 10), (190, 20)),
                            text='Количество членов ряда')

num_terms_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 10), (50, 20)),
    manager=gui_manager,
    object_id='num_terms'
)
num_terms_input.set_text('1')

pygame_gui.elements.UILabel(relative_rect=pygame.Rect((8, 40), (150, 20)), text='Скорость анимации')
animation_speed_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 40), (50, 20)),
    manager=gui_manager,
    object_id='animation_speed'
)
animation_speed_input.set_text('1')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gui_manager.process_events(event)

    screen.fill(white)

    num_terms = int(num_terms_input.get_text())  # обновление n членов

    animation_speed = float(animation_speed_input.get_text())  # обновление скорости

    x_values = [x + i * dt * animation_speed for i in range(screen_width)]  # вычисление значений для графиков
    y_sin = [screen_height // 2 - int(50 * math.sin(x)) for x in x_values]
    y_fourier = [screen_height // 2 - int(50 * fourier_sin(x, num_terms)) for x in x_values]

    for i in range(screen_width - 1):  # отрисовка графиков
        pygame.draw.line(screen, black, (i, y_sin[i]), (i + 1, y_sin[i + 1]))
        pygame.draw.line(screen, (255, 0, 0), (i, y_fourier[i]), (i + 1, y_fourier[i + 1]))

    gui_manager.update(1 / 165)
    gui_manager.draw_ui(screen)

    pygame.display.flip()
    x += dt

pygame.quit()
