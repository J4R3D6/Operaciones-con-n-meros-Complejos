import math
def sum(a, b):
    return (a[0]+b[0],a[1]+b[1])

def res(a, b):
    return (a[0]-b[0],a[1]-b[1])

def mult(a,b ):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+b[0]*a[1])

def div(a,b):
    return ((a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2),(a[1]*b[0]-a[0]*b[1])/(b[0]**2+b[1]**2))

def module(a):
    return (a[0]**2+a[1]**2)**(1/2)

def conjugado(a):
    return (a[0], -1*a[1])

def cartesiana_a_polar(a):
    return (module(a),math.atan2(a[1],a[0]))

def polar_a_cartesiana(a):
    return (a[0]*math.cos(a[1]),a[0]*math.sin(a[1]))

def operaciones():
    print(sum((3.5,6),(-6.7,2)))
    print(res((3.5,6),(-6.7,2)))
    print(mult((3.5,6),(-6.7,2)))
    print(div((3.5,6),(-6.7,2)))
    print(module((-6.7,2)))
    print(conjugado((-6.7,2)))
    print(cartesiana_a_polar((-6.7,2)))
    print(polar_a_cartesiana((6.992138442565336,2.851505721268765)))

if __name__ == "__main__":
    operaciones()