#!/bin/python3

'''
Amirhosein Abutalebi
This program show gradient in window that you set measurement
'''

import cv2
import numpy as np

COLOR = {
    "red":(0, 0, 255),
    "green":(0, 255, 0),
    "blue":(255, 0, 0),
    "black":(0, 0, 0),
    "white":(255, 255, 255),
    "yellow":(0, 255, 255)
}

def check_input_int(input_int):
    '''
    This def check input is numeric or not
    '''
    true = input_int.isnumeric()
    if true:
        return False
    else:
        print("Value Error.\nPlease Enter just number.")
        return True

def check_input_str(input_str):
    '''
    This def check input is str or not
    '''
    if len(input_str) == 1:
        true = input_str[0].isnumeric()
        if true:
            print("Value Error.\nPlease Enter just String or RGB code.")
            return True
        else:
            return False
    else:
        for i in range(len(input_str)):
            true = input_str[i].isnumeric()
            if true:
                pass
            else:
                return False
        return True

def get_size():
    '''
    This def get size for show window and return x and y.
    '''
    true1 = True
    true2 = True
    while true1:
        x_window = input("Please Enter a number for Lenght : ")
        true1 = check_input_int(x_window)
    while true2:
        y_window = input("Please Enter a number for Width : ")
        true2 = check_input_int(y_window)
    x_window = int(x_window)
    y_window = int(y_window)
    return x_window, y_window

def get_number_of_color():
    '''
    This def get number of color use in gradient and return it.
    '''
    true = True
    while  true:
        number_of_color = input("Enter a number for number of color : ")
        true = check_input_int(number_of_color)
    number_of_color = int(number_of_color)
    return number_of_color

def check_tuple(tuple_case):
    '''
    This function check tuple is correct or no
    '''
    if len(tuple_case) == 3:
        blue, green, red = tuple_case
        blue = int(blue)
        green = int(green)
        red = int(red)
        if blue <= 255 and blue >= 0:
            if green <= 255 and green >= 0:
                if red <= 255 and red >= 0:
                    return True
    return False

def color_input_to_rgb(color_input):
    '''
    This def change name color to rgb code
    '''
    for count in range(len(color_input)):
        for check_color, value in COLOR.items():
            if [check_color] == color_input[count]:
                color_input[count] = value

    for count in range(len(color_input)):
        is_tuple = type(color_input[count])
        if is_tuple != tuple:
            for i in range(3):
                color_input[count][i] = int(color_input[count][i])

    for count in range(len(color_input)):
        is_tuple = type(color_input[count])
        if  is_tuple != tuple:
            color_input[count] = tuple(color_input[count])
    return color_input

def get_color(number_of_color):
    '''
    This def get color base number of color and color input should
    exist in color list or get code rgb and return list of input colors
    '''
    print("Color exist is : {}".format(COLOR.keys()))
    color_input = []
    number_of_color_list = len(COLOR)
    for i in range(number_of_color):
        true = True
        while true:
            color = input("Enter a name of color exist or Enter a code rgb {} : ".format(i+1))
            color_input.insert(i, color)
            color_input[i] = color_input[i].split(",")
            true = check_input_str(color_input[i])
            if true:
                tuple_case = tuple(color_input[i])
                check = check_tuple(tuple_case)
                if check:
                    break
                else:
                    print("Enter correct RGB code For example input = 125,125,125.")
                    print("This tuple is wrong value. value of tuple is between 0 and 255.")
                    del color_input[i]
            else:
                count = 0
                for check_color in COLOR:
                    count += 1
                    if [check_color] == color_input[i]:
                        break
                    if count == number_of_color_list:
                        print("Value Error.\nColor input is not exist in list Of color.")
                        del color_input[i]
                        true = True
                        break
    return color_input

def create_gradient_lwf(size_x, size_y, color_input, number_of_color, animation, time):
    '''
    This def create gradient linear by opencv with feather
    '''
    canvas = np.zeros((size_x, size_y, 3), dtype="uint8")

    part_of_size = int(size_y/(number_of_color-1))

    count = -1
    for i in range(number_of_color-1):
        b_color1, g_color1, r_color1 = color_input[i]
        if i != number_of_color-1:
            b_color2, g_color2, r_color2 = color_input[i+1]

        diff_r = (r_color1/255) * part_of_size
        diff_g = (g_color1/255) * part_of_size
        diff_b = (b_color1/255) * part_of_size

        if b_color1 < b_color2:
            b_color1 = b_color2

        if g_color1 < g_color2:
            g_color1 = g_color2

        if r_color1 < r_color2:
            r_color1 = r_color2
        for row in range(part_of_size, 0, -1):
            count += 1
            # RED
            red = diff_r / part_of_size * r_color1
            if r_color1 > r_color2:
                diff_r -= 1
                if diff_r <= 0:
                    diff_r = 0
            if r_color1 == r_color2:
                diff_r += 1
                if diff_r >= part_of_size:
                    diff_r = part_of_size
            # GREEN
            green = diff_g / part_of_size * g_color1
            if g_color1 > g_color2:
                diff_g -= 1
                if diff_g <= 0:
                    diff_g = 0
            if g_color1 == g_color2:
                diff_g += 1
                if diff_g >= part_of_size:
                    diff_g = part_of_size
            # BLUE
            blue = diff_b / part_of_size * b_color1
            if b_color1 > b_color2:
                diff_b -= 1
                if diff_b <= 0:
                    diff_b = 0
            if b_color1 == b_color2:
                diff_b += 1
                if diff_b >= part_of_size:
                    diff_b = part_of_size
            color = (int(blue), int(green), int(red))
            cv2.line(canvas, (count, 0), (count, size_y), color)
            if animation == 'yes':
                cv2.waitKey(time)
                cv2.imshow("Gradient", canvas)

    cv2.imshow("Gradient", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def create_gradient_rwf(size_x, size_y, color_input, number_of_color, animation, time):
    '''
    This def create gradient radial by opencv with feather
    '''
    canvas = np.zeros((size_x, size_y, 3), dtype="uint8")

    center_x, center_y = int(size_x/2), int(size_y/2)
    radius = size_x - center_x
    part_of_size = int(radius/number_of_color)
    cv2.rectangle(canvas, (0, 0), (size_x, size_y), color_input[0], -1)

    count = -1
    for i in range(number_of_color-1):
        b_color1, g_color1, r_color1 = color_input[i]
        if i != number_of_color-1:
            b_color2, g_color2, r_color2 = color_input[i+1]

        diff_r = (r_color1/255) * part_of_size
        diff_g = (g_color1/255) * part_of_size
        diff_b = (b_color1/255) * part_of_size

        if b_color1 < b_color2:
            b_color1 = b_color2

        if g_color1 < g_color2:
            g_color1 = g_color2

        if r_color1 < r_color2:
            r_color1 = r_color2

        for row in range(part_of_size, 0, -1):
            count += 1
            # RED
            red = diff_r / part_of_size * r_color1
            if r_color1 > r_color2:
                diff_r -= 1
                if diff_r <= 0:
                    diff_r = 0
            if r_color1 == r_color2:
                diff_r += 1
                if diff_r >= part_of_size:
                    diff_r = part_of_size
            # GREEN
            green = diff_g / part_of_size * g_color1
            if g_color1 > g_color2:
                diff_g -= 1
                if diff_g <= 0:
                    diff_g = 0
            if g_color1 == g_color2:
                diff_g += 1
                if diff_g >= part_of_size:
                    diff_g = part_of_size
            # BLUE
            blue = diff_b / part_of_size * b_color1
            if b_color1 > b_color2:
                diff_b -= 1
                if diff_b <= 0:
                    diff_b = 0
            if b_color1 == b_color2:
                diff_b += 1
                if diff_b >= part_of_size:
                    diff_b = part_of_size
            color = (int(blue), int(green), int(red))
            cv2.circle(canvas, (center_x, center_y), radius-count, color, -1)
            if animation == 'yes':
                cv2.waitKey(time)
                cv2.imshow("Gradient", canvas)

    cv2.imshow("Gradient", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def create_gradient_lwof(size_x, size_y, color_input, number_of_color):
    '''
    This def create gradient linear by opencv without feather
    '''
    canvas = np.zeros((size_x, size_y, 3), dtype="uint8")

    part_of_size = int(size_y/number_of_color)

    for count in range(number_of_color):
        cv2.rectangle(canvas, (count*part_of_size, 0), ((count+1)*part_of_size, size_y), color_input[count], -1)
    cv2.imshow("Gradient", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def create_gradient_rwof(size_x, size_y, color_input, number_of_color):
    '''
    This def create gradient radial by opencv without feather
    '''
    canvas = np.zeros((size_x, size_y, 3), dtype="uint8")

    center_x, center_y = int(size_x/2), int(size_y/2)
    radius = size_x - center_x
    part_of_size = int(radius/number_of_color)

    for count in range(number_of_color):
        if count == 0:
            radius = int(1.2*size_x - center_x)
        else:
            radius = size_x - center_x
        cv2.circle(canvas, (center_x, center_y), radius-(count*part_of_size), color_input[count], -1)
    cv2.imshow("Gradient", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def question_gradient():
    '''
    This def question that gradient is linear or radial
    '''
    true = True
    while true:
        question = input("This gradient is linear or radial : ")
        if question == 'linear' or question == 'radial':
            return question
        else:
            print("Value Error.\nPlease Enter linear or radial.")

def question_feather():
    '''
    This def question that gradient have feather or have not
    '''
    true = True
    while true:
        question = input("This gradient have feather : ")
        if question == 'yes' or question == 'no':
            return question
        else:
            print("Value Error.\nPlease yes or no.")

def question_animation():
    '''
    This def question that gradient have animation or not
    '''
    true = True
    while true:
        question = input("This gradient have animation : ")
        if question == 'yes' or question == 'no':
            while true:
                if question == 'yes':
                    time = input("Time for delay : ")
                    true = check_input_int(time)
            return question, time
        else:
            print("Value Error.\nPlease yes or no.")

def main():
    '''
    This def is main
    '''

    question_a, time = 'no', 0
    question_g = question_gradient()
    question_f = question_feather()
    if question_f == 'yes':
        question_a, time = question_animation()
        time = int(time)
    size_x, size_y = get_size()
    number_of_color = get_number_of_color()
    color_input = get_color(number_of_color)
    color_input = color_input_to_rgb(color_input)
    if question_g == 'linear' and question_f == 'yes':
        create_gradient_lwf(size_x, size_y, color_input, number_of_color, question_a, time)
    if question_g == 'linear' and question_f == 'no':
        create_gradient_lwof(size_x, size_y, color_input, number_of_color)
    if question_g == 'radial' and question_f == 'yes':
        create_gradient_rwf(size_x, size_y, color_input, number_of_color, question_a, time)
    if question_g == 'radial' and question_f == 'no':
        create_gradient_rwof(size_x, size_y, color_input, number_of_color)

if __name__ == "__main__":
    main()
