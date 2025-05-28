import numpy as np

def lorenz_map(shape,n0):
    
    a = 10; 
    b = 8/3;
    c = 28; 
    x0 = 0.3;
    y0=n0

    z0 = 0;
    threshold = 700;
    disturbance = 0.02;
    primer_number = 982451653;
    x1=0
    x2=0
    x3=0
    n = shape[0];
    red_stream_scrambling = np.zeros(n);
    green_stream_scrambling = np.zeros(n);
    blue_stream_scrambling = np.zeros(n);

    for i in range(n):
        x1 = a * (y0 - x0) 
        x2 = x0 * (c - z0) - y0
        x3 = x0 * y0 - b * z0
        
        x0 = x1; y0 = x2;
        z0 = x3;
        if (i > threshold):
            if(((i-threshold)% 3541) ==0):
                x0 = x0 + disturbance*np.sin(x0)
        x0 = (x0% primer_number);
        y0 = (y0%primer_number); 
        z0 = (z0%primer_number);
       
        red_stream_scrambling[(i%n)] = x1/pow(10,9);
        green_stream_scrambling[(i%n)] = x2/pow(10,9);
        blue_stream_scrambling[(i%n)] = x3/pow(10,9);
        
    return red_stream_scrambling, green_stream_scrambling, blue_stream_scrambling
    
def rossler_map(shape,n0):
    a = 0.2; 
    b = 0.2;
    c = 5.7; 
    p0 = 1;
    q0=n0

    r0 = 1;
    threshold = 700;
    disturbance = 0.02;
    primer_number = 982451653;
    p1=0
    q2=0
    r3=0
#     M, N, dimension = img.shape;
    n = shape[0]*shape[1]*shape[2];
    red_stream_scrambling = np.zeros(n);
    green_stream_scrambling = np.zeros(n);
    blue_stream_scrambling = np.zeros(n);

    for i in range(n):
        p1 = -(q0+r0)
        q1 = p0 + (a * q0)
        r1 = b + r0*(p0-c)
        p0 = p1; 
        q0 = q1;
        r0 = r1;
#         if (i > threshold):
#             if(((i-threshold)% 3541) ==0):
#                 p0 = p0 + disturbance*np.sin(p0)
        p0 = (p0% primer_number);
        q0 = (q0%primer_number); 
        r0 = (r0%primer_number);
       
        red_stream_scrambling[(i%n)] = p1*pow(10,9);
        green_stream_scrambling[(i%n)] = q1*pow(10,9);
        blue_stream_scrambling[(i%n)] = r1;
        
    return red_stream_scrambling, green_stream_scrambling, blue_stream_scrambling


def logistic_map(shape,n0):    
    a = 10; 
    b = 8/3;
    c = 28; 
    x0 = 1
    y0= n0
    z0=0

    threshold = 700;
    disturbance = 0.02;
    primer_number = 982451653;
    x1=0
    x2=0
    x3=0
    n = shape[0]*shape[1]*shape[2];
    red_stream_diff = np.zeros(n);
    green_stream_diff = np.zeros(n);
    blue_stream_diff = np.zeros(n);

    for i in range(n):
        x1 = c*x0*(1-x0) + b*pow(y0,2)*x0+ a * pow(z0,3)
        x2 = c*y0*(1-y0) + b*pow(z0,2)*y0+ a * pow(z0,3)
        x3 = c*z0*(1-z0) + b*pow(x0,2)*z0+ a * pow(y0,2)
        
        x0 = x1; y0 = x2;
        z0 = x3;
        if (i > threshold):
            if(((i-threshold)% 3541) ==0):
                x0 = x0 + disturbance*np.sin(x0)
        x0 = (x0% primer_number);
        y0 = (y0%primer_number); 
        z0 = (z0%primer_number);
       
        red_stream_diff[(i%n)] = x1;
        green_stream_diff[(i%n)] = x2;
        blue_stream_diff[(i%n)] = x3;
        
    return red_stream_diff, green_stream_diff, blue_stream_diff