# # from reader import *
# # import pygame
# from my_model import raspoznavanie
#
# from random import randrange
# import numpy as np
#
# SCREEN_WIDTH = 1400
# SCREEN_HEIGHT = 840
# BLOCK_SIZE = int(SCREEN_HEIGHT / 28)
# KISTOCHKA_SIZE = 1
# KISTOCHKA_JEST = 255
# GLOBAL_FLAG = 0
#
# fps = 60
#
# # Пока не разобрался что это ниже
# pygame.init()
# sc = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# sc.fill(pygame.Color(54, 54, 54))
# clock = pygame.time.Clock()
#
# # Шрифт
# font = pygame.font.Font(None, 40)
#
# # Создаем массив, хранящий прямоугольники
# all_rects = []
# for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
#     row = []
#     for x in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
#         rect = pygame.Rect(x, y, BLOCK_SIZE - 0.5, BLOCK_SIZE - 0.5)
#         row.append([rect, [0, 0, 0]])
#     all_rects.append(row)
#
#
# # Преобразование в массив NUMPY
# def nparray_list(x: list):
#     y = np.zeros(shape=(28, 28))
#     for nomer_stroki in range(0, 28):
#         for nomer_kletki_v_stroke in range(0, 28):
#             y[nomer_stroki][nomer_kletki_v_stroke] = x[nomer_stroki][nomer_kletki_v_stroke][1][0]
#     return y
#
#
# # for x in range(0, 780, 28):
# #     for y in range(0, 780, 28):
# #         pygame.draw.rect(sc, (255, 255, 255), (x, y, 28, 28))
# #         # pygame.draw.rect(sc, (randrange(0, 255, 1), randrange(0, 255, 1), randrange(0, 255, 1)), (x, y, 28, 28))
# def collider_rect_mous(pos, arr):
#     x = pos[0] // BLOCK_SIZE
#     y = pos[1] // BLOCK_SIZE
#     res = arr[y][x]
#     return (res)
#
#
# while True:
#     if pygame.mouse.get_focused() and sum(pygame.mouse.get_pressed()) != 0:
#         pos = pygame.mouse.get_pos()
#         iventmouse = pygame.mouse.get_pressed()
#         if pos[0] <= 840 and pos[1] <= 840:
#             item = collider_rect_mous(pos, all_rects)
#             rect, color = item
#             if iventmouse[0] == 1:
#                 for i in range(3):
#                     item[1][i] = KISTOCHKA_JEST
#             elif iventmouse[2] == 1:
#                 item[1] = [0, 0, 0]
#
#     # Обновление массива с прямоугольниками на экране
#     for row in all_rects:
#         for item in row:
#             rect, color = item
#             pygame.draw.rect(sc, color, rect)
#
#     # Получение результата от НС
#     # if not pygame.mouse.get_focused():
#     #     arr = nparray_list(all_rects)
#     #     res = raspoznavanie(arr)
#     #     print(f"Цифра: {np.argmax(res)}")
#
#     pygame.display.flip()
#     clock.tick(fps)
#
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if pygame.key.get_pressed()[pygame.K_EQUALS] and KISTOCHKA_JEST != 255:
#                 KISTOCHKA_JEST += 51
#             if pygame.key.get_pressed()[pygame.K_MINUS] and KISTOCHKA_JEST != 0:
#                 KISTOCHKA_JEST -= 51
#             if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
#                 for row in all_rects:
#                     for item in row:
#                         item[1] = [0, 0, 0]
#             elif event.key == pygame.K_RETURN:
#                 # Получение результата от НС
#                 arr = nparray_list(all_rects)
#                 res = raspoznavanie(arr)
#                 print(f"Цифра: {np.argmax(res)}")
#
#         if event.type == pygame.QUIT:
#             # print(nparray_list(all_rects))
#             # print(type(nparray_list(all_rects)))
#             exit()
