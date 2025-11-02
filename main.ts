input.onButtonPressed(Button.A, function () {
    start = true
})
input.onButtonPressed(Button.B, function () {
    start = false
})
let start = false
datalogger.setColumnTitles(
"ax",
"ay",
"az",
"degree",
"millis"
)
start = false
loops.everyInterval(100, function () {
    if (start == true) {
        datalogger.log(
        datalogger.createCV("ax", input.acceleration(Dimension.X)),
        datalogger.createCV("ay", input.acceleration(Dimension.Y)),
        datalogger.createCV("az", input.acceleration(Dimension.Z)),
        datalogger.createCV("degree", input.compassHeading()),
        datalogger.createCV("millis", control.millis())
        )
    }
})
