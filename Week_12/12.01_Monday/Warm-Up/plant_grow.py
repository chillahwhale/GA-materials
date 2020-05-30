'''
Problem from Codewars (https://www.codewars.com/kata/58941fec8afa3618c9000184)

Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level. Return the number of days that it will take for the plant to reach/pass desiredHeight (including the last day in the total count).

Example
For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.
     After day 1 --> 100
     After night 1 --> 90
     After day 2 --> 190
     After night 2 --> 180
     After day 3 --> 280
     After night 3 --> 270
     After day 4 --> 370
     After night 4 --> 360
     After day 5 --> 460
     After night 5 --> 450
     After day 6 --> 550
     After night 6 --> 540
     After day 7 --> 640
     After night 7 --> 630
     After day 8 --> 730
     After night 8 --> 720
     After day 9 --> 820
     After night 9 --> 810
     After day 10 --> 910

For upSpeed = 10, downSpeed = 9 and desiredHeight = 4, the output should be 1. Because the plant reach to the desired height at day 1(10 meters).

>>> plant_grow(100, 10, 910)
10

>>> plant_grow(10, 9, 4)
1

>>> plant_grow(5, 2, 50)
16

'''

def plant_grow(upSpeed, downSpeed, desiredHeight):

    # Replace the line below with all your code.
    pass


plant_grow(100, 10, 910)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
