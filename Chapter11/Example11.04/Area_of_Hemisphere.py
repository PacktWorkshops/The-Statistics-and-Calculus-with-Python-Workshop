def sphere(x,y): 

    """Sphere of radius 1""" 

    return sqrt(1-x**2-y**2)  

 

def area(f,ax,bx,ay,by,num=10000): 

    """Returns area of parallelogram formed by 

        vectors with given partial derivs""" 

    running_sum = 0 

    dx = (bx-ax)/num 

    dy = (by-ay)/num 

    for i in range(num): 

        for j in range(num): 

            x = ax+i*dx 

            y = ay+j*dy 

            dz_dx=partial_d(f,'x',x,y,num) 

            dz_dy=partial_d(f,'y',x,y,num) 

            running_sum += mag(cross([1,0,dz_dx],[1,0,dz_dy]))*dx*dy 

    return running_sum 
