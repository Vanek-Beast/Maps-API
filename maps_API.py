import sys
import pygame
import requests
import os

api_server = "http://static-maps.yandex.ru/1.x/"

lon = "-74.000166"
lat = "40.712524"
delta = "0.02"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": "map"
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
while pygame.event.wait().type != pygame.QUIT:
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()

os.remove(map_file)
