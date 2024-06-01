import numpy as np
import cv2




def show(img,wait=0):
    if img.dtype!=np.uint8:
        img=normalize(img)
    img=np.uint8(img)
    cv2.imshow("img",img)
    cv2.waitKey(wait)

def normalize(img):
    img=img*1.0
    img=img-img.min()
    img=img/img.max()
    return np.uint8(255*img)
    
img1=cv2.imread("image1.png")
img2=cv2.imread("image2.png")
# ~ show(img1)
# ~ show(img2)
orb = cv2.ORB_create() #nfeatures=6 fastThreshold =70

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# ~ print(len(kp1))
# ~ print(len(kp2))
# ~ out=cv2.drawKeypoints(img1,kp1,None)
# ~ show(out)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.knnMatch(des1,des2,k=2)
# ~ print(matches)
good_matches=[]
for best_match,second_best_match in matches:
	if best_match.distance<.75*second_best_match.distance:
		good_matches.append(best_match)
	
print(len(good_matches))
# ~ match=matches[0]
# ~ print(match.queryIdx,match.trainIdx)
# ~ print(des1[match.queryIdx])
# ~ print(des2[match.trainIdx])
img3 = cv2.drawMatches(img1,kp1,img2,kp2,good_matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# ~ show(img3)

src_points=[]
dest_points=[]
for m in good_matches:
	src_points.append(kp1[m.queryIdx].pt)
	dest_points.append(kp2[m.trainIdx].pt)

src_points=np.float32(src_points)
dest_points=np.float32(dest_points)

H,_=cv2.findHomography(src_points,dest_points,method=cv2.RANSAC,ransacReprojThreshold=2,maxIters=10000000)
while 1:
	show(cv2.warpPerspective(img1,H,None),100)
	show(img2,100)
# ~ print(H)
