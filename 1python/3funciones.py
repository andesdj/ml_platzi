import turtle

def main():
    window= turtle.Screen()
    andes= turtle.Turtle()

    make_square(andes)
    turtle.mainloop()


def make_square(andes):
    length= int(input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(andes,length)


def make_line_and_turn(andes,length):
    andes.forward(length)
    andes.left(90)

if __name__ == '__main__':
    main()