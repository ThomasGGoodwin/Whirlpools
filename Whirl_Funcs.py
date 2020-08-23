from turtle import *
from math import *

def circlecenter(pts): #see notebook for how I implemented
    x1=pts[0][0]
    y1=pts[0][1]
    x2=pts[1][0]
    y2=pts[1][1]
    x3=pts[2][0]
    y3=pts[2][1]
    #using y=mx+b
    c1x = (x1+x2)/2
    c1y = (y1+y2)/2
    m1 = -(x1-x2)/(y1-y2)
    b1 = c1y - m1*c1x
    c2x = (x2+x3)/2
    c2y = (y2+y3)/2
    m2 = -(x2-x3)/(y2-y3)
    b2 = c2y - m2*c2x
    xret = (b2-b1)/(m1-m2)
    yret = m1 * xret + b1
    return [xret,yret]

def colorless(n,rho,phi,base,iters,startx=600,starty=-300,lamp=False):
    reset()
    alp = ((n - 2) * 180 / n) / 2
    eta = 90 + rho / 2
    bet = eta - alp
    gam = 180 - phi - bet
    screen = Screen()
    screen.setup(width=1.0, height=1.0)
    hideturtle()
    penup()
    goto(startx,starty)
    pensize(1)
    pendown()
    speed(0)
    left(90)
    for j in range(0, iters):
        for i in range(0, n+1):
            forward(base)
            left(rho)
        right(rho)
        left(180 - gam)
        len1 = base * sin(radians(phi)) / sin(radians(bet))
        len2 = base * sin(radians(gam)) / sin(radians(bet))
        for i in range(0, n+1):
            forward(len1)
            right(bet + 180)
            color("orange")
            forward(len2)
            color("black")
            right(gam + rho + phi)
        forward(len1)
        a = 180 - gam - phi - rho
        base = sqrt(len1 ** 2 + len2 ** 2 - 2 * len1 * len2 * cos(radians(a)))
        right(degrees(asin(len2 * sin(radians(a)) / base)))
    toppoints = []
    for i in range(0, n+1):
        toppoints += [[position()[0], position()[1]]]
        forward(base)
        left(rho)
    if lamp:
        ctrpt = circlecenter(toppoints)
        toppoints.reverse()
        for i in range(len(toppoints)):
            goto(ctrpt[0], ctrpt[1])
            goto(toppoints[i][0], toppoints[i][1])
    #

def colored(n,rho,phi,base,iters,colors,backcol="#cccccc",startx=540,starty=315,lamp=False):
    reset()
    c=0
    if len(colors)!=n:
        mul = int(n/len(colors))
        colors = colors*mul
    colors = colors + [colors[0]]
    # creating alpha, beta, ga
    alp = ((n - 2) * 180 / n) / 2
    eta = 90 + rho / 2
    bet = eta - alp
    gam = 180 - phi - bet
    screen = Screen()
    screen.setup(width=1.0, height=1.0)
    bottompoints = [[]]
    toppoints = [[]]
    leftpoints = [[]]
    rightpoints = [[]]
    penup()
    goto(startx, starty)
    # pendown()
    speed(0)
    fillcolor(backcol)
    right(90)
    baselen = base
    for j in range(0, iters):
        if j == 0:
            bottompoints = [[position()[0], position()[1]]]
        for i in range(0, n + 1):
            forward(baselen)
            right(rho)
            if (j == 0):
                bottompoints += [[position()[0], position()[1]]]
        left(rho)
        right(180 - gam)
        len1 = baselen * sin(radians(phi)) / sin(radians(bet))
        len2 = baselen * sin(radians(gam)) / sin(radians(bet))
        for i in range(0, n + 1):
            forward(len1)
            if (i == 0 and j != iters - 1):
                leftpoints += [[position()[0], position()[1]]]
            left(bet + 180)
            forward(len2)
            left(gam + rho + phi)
        forward(len1)
        if j != iters - 1:
            rightpoints += [[position()[0], position()[1]]]
        a = 180 - gam - phi - rho
        baselen = sqrt(len1 ** 2 + len2 ** 2 - 2 * len1 * len2 * cos(radians(a)))
        left(degrees(asin(len2 * sin(radians(a)) / baselen)))
    toppoints = [[position()[0], position()[1]]]
    for i in range(0, n + 1):
        forward(baselen)
        right(rho)
        toppoints += [[position()[0], position()[1]]]
    leftpoints = leftpoints[1:]
    rightpoints = rightpoints[1:]
    penup()
    fillcolor(backcol)
    begin_fill()
    for i in range(0, len(bottompoints)):
        goto(bottompoints[i][0], bottompoints[i][1])
    for i in range(len(leftpoints)):
        goto(leftpoints[i][0], leftpoints[i][1])
    toppoints.reverse()
    for i in range(len(toppoints)):
        goto(toppoints[i][0], toppoints[i][1])
    rightpoints.reverse()
    for i in range(len(rightpoints)):
        goto(rightpoints[i][0], rightpoints[i][1])

    baselen = base
    penup()
    goto(startx, starty)
    end_fill()
    pensize(1)
    # pendown()
    speed(0)
    setheading(270)
    for j in range(0, iters):
        for i in range(0, n + 1):
            forward(baselen)
            right(rho)
        left(rho)
        right(180 - gam)
        len1 = baselen * sin(radians(phi)) / sin(radians(bet))
        len2 = baselen * sin(radians(gam)) / sin(radians(bet))
        for i in range(0, n + 1):
            fillcolor(colors[c % len(colors)])
            begin_fill()
            forward(len1)
            left(bet + 180)
            forward(len2)
            left(gam + rho + phi)
            end_fill()
            c += 1
        forward(len1)
        a = 180 - gam - phi - rho
        baselen = sqrt(len1 ** 2 + len2 ** 2 - 2 * len1 * len2 * cos(radians(a)))
        left(degrees(asin(len2 * sin(radians(a)) / baselen)))
    for i in range(0, n + 1):
        forward(baselen)
        right(rho)

    if lamp:
        ctrpt = circlecenter(toppoints)
        for i in range(len(toppoints) - 1):
            penup()
            goto(toppoints[i][0], toppoints[i][1])
            fillcolor(colors[c % len(colors)])
            begin_fill()
            goto(ctrpt[0], ctrpt[1])
            goto(toppoints[i + 1][0], toppoints[i + 1][1])
            end_fill()
            c += 1
    hideturtle()
    #

def preview(n,rho,phi,iters,colors,startx=-100,starty=-200,lamp=False,rad=350):
    reset()
    alp = ((n - 2) * 180 / n) / 2
    eta = 90 + rho / 2
    bet = eta - alp
    gam = 180 - phi - bet
    x = 180 - rho - phi - gam
    baselen = 100
    len2 = baselen * sin(radians(phi)) / sin(radians(gam))
    len3 = sqrt(baselen ** 2 + len2 ** 2 - 2 * baselen * len2 * cos(radians(x)))
    y = 180 - degrees(asin(baselen * sin(radians(x)) / len3))
    z = 180 - y - x

    screen = Screen()
    screen.setup(width=1.0, height=1.0)
    hideturtle()
    penup()
    speed(0)
    goto(startx, starty)
    c = 0
    rot = (n - 2) / n * 180
    setheading(90 - rot / 2)
    baselen = rad * sin(radians(360 / n)) / sin(radians(rot / 2))
    forward(baselen)
    right(180 - phi)
    forward(baselen * sin(radians(bet)) / sin(radians(gam)))
    right(180 - gam)
    pendown()
    for i in range(0, iters):
        len2 = baselen * sin(radians(phi)) / sin(radians(gam))
        len1 = baselen * sin(radians(bet)) / sin(radians(gam))
        len3 = sqrt(baselen ** 2 + len2 ** 2 - 2 * baselen * len2 * cos(radians(x)))
        for j in range(0, n):
            fillcolor(colors[c % len(colors)])
            begin_fill()
            forward(baselen * sin(radians(phi)) / sin(radians(gam)))
            right(180 - bet)
            forward(baselen)
            right(180 - phi)
            forward(baselen * sin(radians(bet)) / sin(radians(gam)))
            end_fill()
            backward(baselen * sin(radians(bet)) / sin(radians(gam)))
            left(180 - phi)
            right(180 - x)
            c = c + 1
        xpos, ypos = xcor(), ycor()
        head = heading()
        fillcolor(colors[0])
        begin_fill()
        forward(baselen * sin(radians(phi)) / sin(radians(gam)))
        right(180 - bet)
        forward(baselen / 2)
        penup()
        goto(xpos, ypos)
        setheading(head)
        end_fill()
        pendown()
        forward(baselen * sin(radians(phi)) / sin(radians(gam)))
        right(180 - (gam + bet - z))
        baselen = len3 * sin(radians(gam)) / sin(radians(bet))

    left(180 - (gam + bet - z))
    left(180 + bet - z)
    lamppoints = []
    for i in range(0, n):
        xpos, ypos = xcor(), ycor()
        head = heading()
        lamppoints = lamppoints + [(xcor(), ycor())]
        fillcolor("white")
        begin_fill()
        forward(len3)
        u = 180 - rot
        t = 180 - z - u
        d = len3 * sin(radians(t)) / sin(radians(u))
        e = len3 * sin(radians(z)) / sin(radians(u))
        left(180 - t)
        forward(e)
        left(rot)
        forward(d)
        end_fill()

        penup()
        goto(xpos, ypos)
        setheading(head)
        forward(len3)
        left(180 - rot)
        pendown()
    lamppoints = lamppoints + [lamppoints[0]]
    if lamp:
        ctr = circlecenter(lamppoints)
        goto(lamppoints[0])
        for i in range(0, len(lamppoints) - 1):
            fillcolor(colors[c % len(colors)])
            begin_fill()
            goto(ctr)
            goto(lamppoints[i + 1])
            end_fill()
            c += 1
            goto(lamppoints[i])
            goto(lamppoints[i + 1])
    #

def colorless_preview(n,rho,phi,iters,startx=-150,starty=-50,lamp=False,rad=350):
    reset()
    alp = ((n - 2) * 180 / n) / 2
    eta = 90 + rho / 2
    bet = eta - alp
    gam = 180 - phi - bet
    x = 180 - rho - phi - gam
    baselen = 100
    len2 = baselen * sin(radians(phi)) / sin(radians(gam))
    len3 = sqrt(baselen ** 2 + len2 ** 2 - 2 * baselen * len2 * cos(radians(x)))
    y = 180 - degrees(asin(baselen * sin(radians(x)) / len3))
    z = 180 - y - x

    screen = Screen()
    screen.setup(width=1.0, height=1.0)
    hideturtle()
    penup()
    speed(0)
    goto(startx, starty)
    c = 0
    rot = (n - 2) / n * 180
    setheading(90 - rot / 2)
    baselen = rad * sin(radians(360 / n)) / sin(radians(rot / 2))
    forward(baselen)
    left(180 - phi)
    forward(baselen * sin(radians(bet)) / sin(radians(gam)))
    left(180 - gam)
    pendown()
    for i in range(0, iters):
        len2 = baselen * sin(radians(phi)) / sin(radians(gam))
        len1 = baselen * sin(radians(bet)) / sin(radians(gam))
        len3 = sqrt(baselen ** 2 + len2 ** 2 - 2 * baselen * len2 * cos(radians(x)))
        for j in range(0, n):
            fillcolor("#ffffff")
            begin_fill()
            forward(baselen * sin(radians(phi)) / sin(radians(gam)))
            left(180 - bet)
            forward(baselen)
            left(180 - phi)
            forward(baselen * sin(radians(bet)) / sin(radians(gam)))
            end_fill()
            backward(baselen * sin(radians(bet)) / sin(radians(gam)))
            right(180 - phi)
            left(180 - x)
            c = c + 1
        xpos, ypos = xcor(), ycor()
        head = heading()
        fillcolor("#ffffff")
        begin_fill()
        forward(baselen * sin(radians(phi)) / sin(radians(gam)))
        left(180 - bet)
        forward(baselen / 2)
        penup()
        goto(xpos, ypos)
        setheading(head)
        end_fill()
        pendown()
        forward(baselen * sin(radians(phi)) / sin(radians(gam)))
        left(180 - (gam + bet - z))
        baselen = len3 * sin(radians(gam)) / sin(radians(bet))

    right(180 - (gam + bet - z))
    right(180 + bet - z)
    lamppoints = []
    for i in range(0, n):
        xpos, ypos = xcor(), ycor()
        head = heading()
        lamppoints = lamppoints + [(xcor(), ycor())]
        fillcolor("#ffffff")
        begin_fill()
        forward(len3)
        u = 180 - rot
        t = 180 - z - u
        d = len3 * sin(radians(t)) / sin(radians(u))
        e = len3 * sin(radians(z)) / sin(radians(u))
        right(180 - t)
        forward(e)
        right(rot)
        forward(d)
        end_fill()

        penup()
        goto(xpos, ypos)
        setheading(head)
        forward(len3)
        right(180 - rot)
        pendown()
    lamppoints = lamppoints + [lamppoints[0]]
    if lamp:
        ctr = circlecenter(lamppoints)
        goto(lamppoints[0])
        for i in range(0, len(lamppoints) - 1):
            fillcolor("#ffffff")
            begin_fill()
            goto(ctr)
            goto(lamppoints[i + 1])
            end_fill()
            c += 1
            goto(lamppoints[i])
            goto(lamppoints[i + 1])
    #
