import numpy as np

def scramble_img(original_img, key_stream_scramblingR):

    
    M,N,dimension = original_img.shape
    n = M*N*dimension;
    scrambled_img = original_img;
    
    vector = np.vectorize(np.int_)

    red_stream_scrambling = vector(np.remainder(np.floor(key_stream_scramblingR), n));

    
    red_img1 = original_img.flatten()

    
    for i in range(M*N*dimension):
        t = red_img1[i];
        red_img1[i] = red_img1[red_stream_scrambling[i]];
        red_img1[red_stream_scrambling[i]] = t;
        
        
        
    red_img = red_img1.reshape(M, N,dimension)
    return red_img
    
def diffuse_img(original_img ,key_stream_diffusionR):
    
    M, N, dimension = original_img.shape;
    n = M*N*dimension;
    diffused_img = original_img
    
    vector = np.vectorize(np.int_)
    red_stream_diffusion = vector(np.remainder(key_stream_diffusionR, 255));

    red_img1 = original_img.flatten()

    for i in range(n):
        red_img1[i] = (int(red_img1[i]) ^ int(red_stream_diffusion[i]));
    
    red_img = red_img1.reshape(M, N,dimension)

    return red_img
        