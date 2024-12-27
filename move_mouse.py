import pyautogui
import time
import random


def generate_random_sleep_time(min_sleep_time=3, max_sleep_time=3):
    return random.randint(min_sleep_time, max_sleep_time)


def generate_random_movement_duration(min_movement_duration=5, max_movement_duration=30):
    return random.randint(min_movement_duration, max_movement_duration)


def generate_random_coordinates(
    top_left_x=0,
    top_left_y=0,
    bottom_right_x=pyautogui.size()[0] - 1,
    bottom_right_y=pyautogui.size()[1] - 1,
):
    random_x = random.randint(top_left_x, bottom_right_x)
    random_y = random.randint(top_left_y, bottom_right_y)
    return [random_x, random_y]


def moveMouse(time_to_sleep, x_coordinates, y_coordinates, movement_duration):
    time.sleep(time_to_sleep)
    pyautogui.moveTo(x_coordinates, y_coordinates, duration=movement_duration)


while True:
    moveMouse(
        generate_random_sleep_time(),
        generate_random_coordinates()[0],
        generate_random_coordinates()[1],
        generate_random_movement_duration(),
    )
