# generate training images
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import math

PI = 3.14159

img_size = 28 #512
img_num = 20
random.seed()
f = open("./labels.txt",'a')
obj_num = 1
radius = 3 #30
width = 4 #8

def cal_dis(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def cal_angle(x1,y1,x2,y2): #angle between x axis and the vertice (x1<x2.)
    if x1==x2:
        return 0.5 #90/180
    if y1==y2 :
        return 0
    if y1<y2:
        return math.atan((y2-y1)/(x2-x1))/PI  #Normalize
    return (PI - math.atan((y1-y2)/(x2-x1)))/PI  #Normalize



for i in range(img_num):
    
    img = np.zeros((img_size,img_size,3),np.uint8)#empty image
    
    nodes = []
    for j in range(obj_num):
        
        x = random.randint(radius,img_size-radius)
        #y = random.randint(radius,img_size-radius)
        #-----------------------
        y = int(0.5* img_size) # y is set to 0.5*img_size 
        #-----------------------
    
        cv2.circle(img,(x,y),radius,(255,255,255),width)# center,radius,color,width

        nodes.append( (float(x)/img_size, float(y)/img_size) ) #(x,y)

    nodes = sorted(nodes, key=lambda node: node[1])
    nodes = sorted(nodes, key=lambda node: node[0])
    '''
    #write to a text

    for j in range(obj_num):
        if j==obj_num -1:
            end = ""
        else:
            end = ","

        f.write(str(round(nodes[j][0],2))+" "+str(round(nodes[j][1],2)) + end)
    '''
    

    for node_i in range(obj_num):

        
        x1,y1 = nodes[node_i][0],nodes[node_i][1]
            #dis = cal_dis(x1,x2,y1,y2)

            #ang = cal_angle(x1,x2,y1,y2)

        print("img"+str(i)+" "+str(round(x1,2))+" "+str(round(y1,2))+"\n")
           
        f.write(str(round(x1,2)))#label : distance + angle 



            #label : distance + angle 
            #used for vector

    f.write("\n")
    cv2.imwrite("./imgs/"+str(i)+".png", img)

