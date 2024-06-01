import numpy as np
import cv2

def show(img,wait=0, window="img"):
    if img.dtype!=np.uint8:
        img=normalize(img)
    img=np.uint8(img)
    cv2.imshow(window,img)
    cv2.waitKey(wait)

def normalize(img):
    img=img-img.min()
    img=img/img.max()
    return np.uint8(255*img)

image1=cv2.imread("image1.png")
image2=np.flipud(image1)
orb = cv2.ORB_create(nfeatures= 1000)

kp1, des1 = orb.detectAndCompute(image1,None)
kp2, des2 = orb.detectAndCompute(image2,None)

# print(len(kp1))
# print(len(kp2))
out = cv2.drawKeypoints(image1, kp1, None)
show(out)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

matches = bf.knnMatch(des1,des2,k=2)

good_matches=[]

for best_match,second_best_match in matches:
    if best_match.distance<0.75*second_best_match.distance:
        good_matches.append(best_match)
print(len(good_matches))
image3 = cv2.drawMatches(image1,kp1,image2,kp2,good_matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imwrite("matches.png",image3)
show(image3)

src_points=[]
dest_points=[]
for m in good_matches:
    src_points.append(kp1[m.queryIdx].pt)
    dest_points.append(kp2[m.trainIdx].pt)

src_points=np.float32(src_points)
dest_points=np.float32(dest_points)
H,_=cv2.findHomography(src_points,dest_points, method=cv2.RANSAC)
# show(cv2.warpPerspective(image1, H, None))    

def bbox(img):
    h,w=img.shape[:2]
    points=np.float32([[0,0],[w,0],[w,h],[0,h]])
    return(points)

points = bbox(image1)
cv2.perspectiveTransform(points[:,None,:],H) # points need to be of form [[[x1,y1]],[[x2,y2]]]
print(H@points.T)
out_points=cv2.perspectiveTransform(points[:,None,:],H) 
all_points=np.vstack((points,out_points[:,0,:1]))
X,Y=all_points.T
minx=X.min()
miny=Y.min()
maxx=X.max()
maxy=Y.max()
T=np.float32([[1,0,-minx],[0,1,-miny],[0,0,1]])
new_width=int(maxx-minx)
new_height=int(maxy-miny)
print(new_width,new_height)
out1=cv2.warpPerspective(image1,H,(new_width,new_height))
cv2.imwrite("out1.png",out1)

# First input in filter2D must be float
