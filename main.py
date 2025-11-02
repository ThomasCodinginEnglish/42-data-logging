def on_button_pressed_a():
    global start
    start = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global start
    start = False
input.on_button_pressed(Button.B, on_button_pressed_b)

start = False
datalogger.set_column_titles("ax", "ay", "az", "degree", "millis")
start = False

def on_every_interval():
    if start == True:
        datalogger.log(datalogger.create_cv("ax", input.acceleration(Dimension.X)),
            datalogger.create_cv("ay", input.acceleration(Dimension.Y)),
            datalogger.create_cv("az", input.acceleration(Dimension.Z)),
            datalogger.create_cv("degree", input.compass_heading()),
            datalogger.create_cv("millis", control.millis()))
loops.every_interval(100, on_every_interval)
