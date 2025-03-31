import time
import numpy as np
start_time = time.time()
def quadratic_func(x):
    return x**2
def sine_func(x):
    return np.sin(x)
def exponential_func(x):
    return np.exp(x)
def linear_approximation(func,center,tolerance):
    dx=1e-8
    derivative = (func(center+dx) - func(center - dx))/(2*dx)
    offset=tolerance/abs(derivative)
    left_bound=center-offset
    right_bound=center+offset
    while abs(func(left_bound)-func(center)-(derivative*(left_bound-center)))>tolerance:
        left_bound-=dx
    while abs(func(right_bound) - func(center) - derivative *(right_bound - center))> tolerance:
        right_bound+=dx
    return float (left_bound), float(right_bound)
print(linear_approximation(quadratic_func, 1,0.1))
print(linear_approximation(sine_func,np.pi/4,0.05))
print(linear_approximation(exponential_func,0,0.01))
print("--- %s seconds ---" % (time.time() - start_time))

