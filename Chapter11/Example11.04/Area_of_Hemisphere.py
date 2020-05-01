def sphere(x,y):
    """Sphere of radius 1"""
    return sqrt(1-x**2-y**2)

def plane(x,y):
    """Plane 3x+2y+z=6"""
    return 1#6-3*x-2*y

def surface(x,y):
    return 10*numpy.sin(numpy.sqrt(x**2+y**2))#+numpy.cos(x*y/15.0)

def surface2(x,y):
    return numpy.sin(x+y)

def cross(u,v):
    """Returns the cross product of 2 3D vectors
    [[i,j,k],
     [1,0,dz/dx],
     [0,1,dz,dy]]
     
     cross([1,-1,2],[2,3,-5])
     >>> [-1, -9, 5]
     """
    return [u[1]*v[2]-v[1]*u[2],
            -u[0]*v[2]+v[0]*u[2],
            u[0]*v[1]-v[0]*u[1]]

print("Cross:",cross([2,3,4],[5,6,7]))

def mag(vec):
    """Returns the magnitude of a 3D vector"""
    return sqrt(vec[0]**2+vec[1]**2+vec[2]**2)

    
def partial_d(f,u,v,w,num):
    """returns the partial derivative of f
    with respect to u at (v,w)"""
    delta_u = 1/1000000
    try:
        if u == 'x':
            return (f(v+delta_u,w) - f(v,w))/delta_u
        else:
            return (f(v,w+delta_u) - f(v,w))/delta_u
    except ValueError:
        pass 

def area(f,ax,bx,ay,by,num=1000):
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
            try:
                running_sum += mag(cross([1,0,dz_dx],[0,1,dz_dy]))*dx*dy
            except:
                pass
    return running_sum

print("Area of hemisphere:",area(sphere,-1,1,-1,1)) 
