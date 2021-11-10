distance = 0

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    if distance <= 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
        """)
    elif distance <= 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # . . .
        """)
    elif distance <= 3:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # . .
        """)
    elif distance <= 4:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # .
        """)
    elif distance <= 5:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
        """)
    elif distance <= 6:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . #
                        # # # # #
        """)
    elif distance <= 7:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . # #
                        # # # # #
        """)
    elif distance <= 8:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . # # #
                        # # # # #
        """)
    elif distance <= 9:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # # # #
                        # # # # #
        """)
    elif distance <= 10:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
        """)
    elif distance <= 11:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . .
                        # # # # #
                        # # # # #
        """)
    elif distance <= 12:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # . . .
                        # # # # #
                        # # # # #
        """)
    elif distance <= 13:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # . .
                        # # # # #
                        # # # # #
        """)
    elif distance <= 14:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # .
                        # # # # #
                        # # # # #
        """)
    elif distance <= 15:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 16:
        basic.show_leds("""
            . . . . .
                        . . . . #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 17:
        basic.show_leds("""
            . . . . .
                        . . . # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 18:
        basic.show_leds("""
            . . . . .
                        . . # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 19:
        basic.show_leds("""
            . . . . .
                        . # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 20:
        basic.show_leds("""
            . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 21:
        basic.show_leds("""
            # . . . .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 22:
        basic.show_leds("""
            # # . . .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 23:
        basic.show_leds("""
            # # # . .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 24:
        basic.show_leds("""
            # # # # .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif distance <= 25:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
