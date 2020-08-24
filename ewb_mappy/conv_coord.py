# conv_coord.py
# EWB Mappy
# Tobias Eegholm
# 8/19/20

# -*- coding: utf-8 -*-
def conv_coord(deg_notation):
    degrees, rest = deg_notation.split('°', 1)
    minutes, rest = rest.split("'", 1)
    seconds, direction = rest.split('"', 1)

    dec_notation = float(degrees) + float(minutes)/60 + float(seconds)/3600
    
    if direction == 'S' or direction == 'W':
        dec_notation = -dec_notation

    return dec_notation
