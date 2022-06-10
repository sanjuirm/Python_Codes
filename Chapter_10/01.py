from projectile import Projectile

def main():
    angle = eval(input("Enter the launch angle: "))
    vel = eval(input("Enter the initial velocity: "))
    h0 = eval(input("Enter the initial height: "))
    time  = eval(input("Enter the time interval: "))
    
    ball=Projectile(angle,vel,h0)
    Y_max=0
    while ball.getY()>=0:
        ball.update(time)
        if ball.getY() > Y_max:
            Y_max=ball.getY()

    print('\nDistance travelled: {0:0.1f} meters.'.format(ball.getX()),'\nmaximun Height achieved: {0:0.1f} meters.'.format(Y_max))
    
main()
        
    

     

       

        
