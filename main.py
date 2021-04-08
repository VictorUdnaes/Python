import turtle
import random
import winsound
#setup

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("green")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pensize(3)
border_pen.pendown()
for sides in range(4):
    border_pen.forward(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("yellow")
score_pen.penup()
score_pen.setposition(-290, 277)
scoreString = "Score: {}".format(score)
score_pen.write(scoreString, False, align="left", font=("Arial", 12, "normal"))
score_pen.hideturtle()

#sprite setups
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Window")
wn.setup(700, 700)
wn.bgpic("background.gif")

wn.register_shape("invader.gif")
wn.register_shape("player.gif")
wn.register_shape("longBullet.gif")
#-----------------------------------------------------------------------------------------------------------------------
#Player creation

player = turtle.Turtle()
player.color("green")
player.shape("player.gif")
player.pu()
player.speed(0)
player.setposition(0, -280)
player.setheading(90)

playerSpeed = 15


def move_left():
    x = player.xcor() - playerSpeed
    if x < - 285:
        x = -285
    player.setx(x)


def move_right():
    x = player.xcor() + playerSpeed
    if x > 285:
        x = 285
    player.setx(x)


#-----------------------------------------------------------------------------------------------------------------------
#create player weapon

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("longBullet.gif")
bullet.pu()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 25

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletState = "ready"


def fire_bullet():
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)


def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 15:
        return True
    else:
        return False


#-----------------------------------------------------------------------------------------------------------------------
# Enemy creation

enemySpeed = 1
number_of_enemies = 30
rows = int(number_of_enemies/10)
enemies = []
for i in range(int(number_of_enemies)):
    enemies.append(turtle.Turtle())

enemy_start_x = -200
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.pu()
    enemy.speed(0)
    x = enemy_start_x + 50 * enemy_number
    if enemy_number > 10:
        enemy_start_y -= 50
        enemy_number = 0

    y = enemy_start_y
    enemy.setposition(x, y)
    enemy_number += 1


#-----------------------------------------------------------------------------------------------------------------------
# keyboard bindings

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "Up")


#-----------------------------------------------------------------------------------------------------------------------
# main game loop

while True:
    for enemy in enemies:
        x = enemy.xcor() + enemySpeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor() - 40
                e.sety(y)
            enemySpeed *= -1

        if enemy.xcor() < - 280:
            for e in enemies:
                y = e.ycor() - 40
                e.sety(y)
            enemySpeed *= -1

        if is_collision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scoreString = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scoreString, False, align="left", font=("Arial", 12, "normal"))

        if is_collision(player, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            gameOver = "GAME OVER"
            gameOver_pen = turtle.Turtle()
            gameOver_pen.color("yellow")
            gameOver_pen.write(gameOver, False, align="center", font=("Anton", 30, "normal"))

            break

    if bulletState == "fire":
        b_y = bullet.ycor() + bulletSpeed
        bullet.sety(b_y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"





