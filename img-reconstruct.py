# 임포팅하는 패키지들은 평이하다 
import numpy as np
import numpy.fft as fft
import scipy.ndimage as nd
import scipy.misc as misc
from math import pi

#Read in source image
# 아슈타 할배 이미지 업로드, 하
source = nd.imread("einstein.bmp", flatten=True)

#Pad image to simulate oversampling
# w,h 만큼 상하좌우 검정색으로 패딩. 하
pad_len = len(source)
padded = np.pad(source, ((pad_len, pad_len),(pad_len, pad_len)), 'constant', 
                constant_values=((0,0),(0,0)))

# 2차원 푸리에변환. 하
ft = fft.fft2(padded)

#simulate diffraction pattern
# 코드는 걍 진폭영상 구하기인데..코멘트는 거창하군.
diffract = np.abs(ft)

# 패딩해 넣은 영상 크기 구하기
l = len(padded)

#keep track of where the image is vs the padding
# 제로패딩된 1값 마스크 생성, 위애서 생성한 패딩된 이미지와 비슷한 구조
mask = np.ones((pad_len+2,pad_len+2))
mask = np.pad(mask, ((pad_len-1, pad_len-1),(pad_len-1, pad_len-1)), 'constant', 
                constant_values=((0,0),(0,0)))

#Initial guess using random phase info
# 구해진 푸리에 진폭에 랜덤위상을 넣어서 랜덤 초기 푸리에신호 생성
guess = diffract * np.exp(1j * np.random.rand(l,l) * 2 * pi)

#number of iterations
# 800번만 반복.
r = 801

#step size parameter
# 학습율에 해당하는거 같음..
beta = 0.8

#previous result
# 800번 루프 s=0~800
prev = None
for s in range(0,r):
    #apply fourier domain constraints
    # 구해진 푸리에 진폭에 이전 위상을 넣어서 푸리에신호 생성후 갱신
    update = diffract * np.exp(1j * np.angle(guess)) 
    # 갱신 푸리에신호 역변환
    inv = fft.ifft2(update)
    # 진폭 취득
    inv = np.real(inv)
    # 이전 진폭 대치
    if prev is None:
        prev = inv
        
    #apply real-space constraints
    # ?? 약간 이해 안되는 대목
    # real 대신 abs()를 쓰면 이런거 안해도 될텐데..?
    temp = inv
    for i in range(0,l):
        for j in range(0,l):
            #image region must be positive
            if inv[i,j] < 0 and mask[i,j] == 1:
                inv[i,j] = prev[i,j] - beta*inv[i,j]
            #push support region intensity toward zero
            if mask[i,j] == 0:
                inv[i,j] = prev[i,j] - beta*inv[i,j]
    
    
    prev = temp
    
    # 역변환.
    guess = fft.fft2(inv)
        
    #save an image of the progress
    # 저장.
    if s % 10 == 0:
        misc.imsave("/Users/chasegoddard/Stuff/CDI/code/save/progress" + str(s) +
                    ".bmp", prev)
        print(s)


