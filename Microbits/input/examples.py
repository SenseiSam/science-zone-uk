'''
The microbit has two buttons: A and B. 
These buttons can be used to send commands to the microbit. 
Here you will be learning how to make a number/string show when the buttons are pressed.
'''

#the code below is a function that lets you insert the commands you want to happen
#when a button is pressed

def on_button_pressed_a():
    #this shows the number 1 when the button is pressed
    basic.show_number(1)

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("Waffles")
input.on_button_pressed(button.B, on_button_pressed_b)


def on_button_pressed_ab():
    basic.show_number(30)
    
input.on_button_pressed(Button.B, on_button_pressed_ab)

