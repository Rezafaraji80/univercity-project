import turtle

turtle.color("black")

adad = int(input("megedar ra vared konid : "))

if adad < 3:
    adad = int(input('adad bayad bozorgtar az 3 bashad'))

else:

    zavie = 360 / adad

    for i in range(adad):
        turtle.forward(100)
        turtle.left(zavie)

        for j in range(adad):
            turtle.forward(100)
            turtle.left(-zavie)

    turtle.done()
