let distance = 0
basic.forever(function () {
    distance = sonar.ping(
    DigitalPin.P0,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    if (distance <= 1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            `)
    } else if (distance <= 2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # . . .
            `)
    } else if (distance <= 3) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # . .
            `)
    } else if (distance <= 4) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # .
            `)
    } else if (distance <= 5) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
    } else if (distance <= 6) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            # # # # #
            `)
    } else if (distance <= 7) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . # #
            # # # # #
            `)
    } else if (distance <= 8) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            # # # # #
            `)
    } else if (distance <= 9) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # # # #
            # # # # #
            `)
    } else if (distance <= 10) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
    } else if (distance <= 11) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            # # # # #
            # # # # #
            `)
    } else if (distance <= 12) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # . . .
            # # # # #
            # # # # #
            `)
    } else if (distance <= 13) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # . .
            # # # # #
            # # # # #
            `)
    } else if (distance <= 14) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # .
            # # # # #
            # # # # #
            `)
    } else if (distance <= 15) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 16) {
        basic.showLeds(`
            . . . . .
            . . . . #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 17) {
        basic.showLeds(`
            . . . . .
            . . . # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 18) {
        basic.showLeds(`
            . . . . .
            . . # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 19) {
        basic.showLeds(`
            . . . . .
            . # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 20) {
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 21) {
        basic.showLeds(`
            # . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 22) {
        basic.showLeds(`
            # # . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 23) {
        basic.showLeds(`
            # # # . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 24) {
        basic.showLeds(`
            # # # # .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (distance <= 25) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        basic.showIcon(IconNames.No)
    }
})
