import sys
import pygame
import requests
import os

api_server = "http://static-maps.yandex.ru/1.x/"


class Map:
    def __init__(self):
        self.lon = "-74.000166"
        self.lat = "40.712524"
        self.z = "16"

    def create_map(self, z1):
        self.z = eval(f"{self.z}+{z1}")
        if self.z < 0:
            self.z = 0
        elif self.z > 17:
            self.z = 17

        params = {
            "ll": ",".join([self.lon, self.lat]),
            "l": "map",
            "z": self.z
        }

        response = requests.get(api_server, params=params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(api_server)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True
map = Map()
map.create_map("0")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                map.create_map("1")
            elif event.key == pygame.K_PAGEDOWN:
                map.create_map("-1")
        screen.blit(pygame.image.load("map.png"), (0, 0))
        pygame.display.flip()
pygame.quit()

os.remove("map.png")
