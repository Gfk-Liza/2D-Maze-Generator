# -*- coding: utf-8 -*-
# Generate a maze using the hole digging method.


# import-related
import random


# Positive and negative judgments.
def _sign(number, max_):
    if ((number > 0) and (max_ > number)) or (number == 0):
        return True
    return False


# Search for a place to move.
def search(map_, xco, yco, mode):
    # Resetting the candidates.
    xmolo = []
    ymolo = []
    xTmolo = []
    yTmolo = []
    if _sign((yco + 2), len(map_)):  # Down
        if map_[yco + 2][xco] == '1':
            xmolo.append(xco)
            ymolo.append(yco + 2)
            xTmolo.append(xco)
            yTmolo.append(yco + 1)
    if _sign((yco - 2), len(map_)):  # Up
        if map_[yco - 2][xco] == '1':
            xmolo.append(xco)
            ymolo.append(yco - 2)
            xTmolo.append(xco)
            yTmolo.append(yco - 1)
    if _sign((xco + 2), len(map_[0])):  # Right
        if map_[yco][xco + 2] == '1':
            xmolo.append(xco + 2)
            ymolo.append(yco)
            xTmolo.append(xco + 1)
            yTmolo.append(yco)
    if _sign((xco - 2), len(map_[0])):  # Left
        if map_[yco][xco - 2] == '1':
            xmolo.append(xco - 2)
            ymolo.append(yco)
            xTmolo.append(xco - 1)
            yTmolo.append(yco)
    # Output
    if mode == 1:
        return len(xmolo)
    if len(xmolo) == 0:
        return
    j = random.randint(0, (len(xmolo) - 1))
    return [xmolo[j], ymolo[j], xTmolo[j], yTmolo[j]]


# Generating function
def generation(width, height):  # The width and height must be natural numbers.
    # Generate a map that is all filled.
    world_map = []
    asd = ''
    for _ in range(width):
        asd = asd + '1'
    for _ in range(height):
        world_map.append(asd)
    asd = '0'
    for _ in range(width - 1):
        asd = asd + '1'
    world_map[0] = asd
    # Reset the coordinates.
    x_c = 0
    y_c = 0
    previously_on_x = [0]
    previously_on_y = [0]
    # Generating Main
    while not((x_c + y_c == 0) and (search(world_map, x_c, y_c, 1) == 0)):
        # Get the coordinates of the next move.
        _xy = search(world_map, x_c, y_c, 2)
        if _xy is None:
            previously_on_x.pop()
            previously_on_y.pop()
            # Update the coordinates.
            x_c = previously_on_x[-1]
            y_c = previously_on_y[-1]
        else:
            index_1 = world_map[_xy[1]][:_xy[0]] + \
                '0' + world_map[_xy[1]][(_xy[0] + 1):]
            world_map[_xy[1]] = index_1
            index_2 = world_map[_xy[3]][:_xy[2]] + \
                '0' + world_map[_xy[3]][(_xy[2] + 1):]
            world_map[_xy[3]] = index_2
            # Record the route you've taken.
            previously_on_x.append(_xy[0])
            previously_on_y.append(_xy[1])
            # Update the coordinates.
            x_c = _xy[0]
            y_c = _xy[1]
    # Output
    return world_map
