# Image-Reconstruction
Image reconstruction from a diffraction pattern, as in Coherent Diffraction Imaging (CDI)

This is an implementation of the hybrid input-output (HIO) algorithm, done in python using the numpy and scipy libraries. 
The algorithm works by iteratively transforming an image between real space and Fourier space, applying constraints at each step. 
In this implementation, the real space image is constrained to be positive, real, and required to have compact support (this is valid since the diffraction pattern is taken with oversampling). 
The Fourier constraint is that the intensity of the transformed image must be the measured intensity given as input. 

For example, given a diffraction pattern: 

![Diffract](https://raw.githubusercontent.com/cwg45/Image-Reconstruction/master/transform.png)

We can reconstruct the original image:

![Progress](https://raw.githubusercontent.com/cwg45/Image-Reconstruction/master/progress.gif)

![Results](https://raw.githubusercontent.com/bemoregt/Image-Reconstruction/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-04-01%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%201.33.01.png)

Citations:

J. R. Fienup, "Phase retrieval algorithms: a comparison," Appl. Opt. 21, 2758-2769 (1982)

