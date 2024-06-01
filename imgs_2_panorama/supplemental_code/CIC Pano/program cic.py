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
    
img1=cv2.imread("CIC Pano\cic1.jpg")
img2=cv2.imread("CIC Pano\cic2.jpg")
# ~ show(img1)
# ~ show(img2)
orb = cv2.ORB_create() #nfeatures=6 fastThreshold =70

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# ~ print(len(kp1))
# ~ print(len(kp2))
# ~ input()
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
# ~ cv2.imwrite("matches.png",img3)
# ~ input()
# ~ show(img3)

src_points=[]
dest_points=[]
for m in good_matches:
	src_points.append(kp1[m.queryIdx].pt)
	dest_points.append(kp2[m.trainIdx].pt)

src_points=np.float32(src_points)
dest_points=np.float32(dest_points)

H,_=cv2.findHomography(src_points,dest_points,method=cv2.RANSAC,ransacReprojThreshold=2,maxIters=10000000)
# ~ while 1:
	# ~ show(cv2.warpPerspective(img1,H,None)[::6,::6],100)
	# ~ show(img2[::6,::6],100)

def bbox(img):
	h,w=img1.shape[:2]
	points=np.float32([[0,0],[w,0],[w,h],[0,h]])
	return points


points=bbox(img1)
out_points=cv2.perspectiveTransform(points[:,None,:],H) #points needs to be of form [[[x1,y1]],[[x2,y2]],...]
cut_x=int(out_points[1,0,0]/2)
print(cut_x)
all_points=np.vstack((points,out_points[:,0,:]))
X,Y=all_points.T
minx=X.min()
maxx=X.max()
miny=Y.min()
maxy=Y.max()
T=np.float32([[1,0,-minx],[0,1,-miny],[0,0,1]]);
new_width=int(maxx-minx)
new_height=int(maxy-miny)
print(new_width,new_height)
out1=cv2.warpPerspective(img1,T@H,(new_width,new_height))
out2=cv2.warpPerspective(img2,T,(new_width,new_height))
cv2.imwrite("output\out1.png",out1)
cv2.imwrite("output\out2.png",out2)
diff=np.uint8(abs(out1*1.0-out2))
cv2.imwrite("diff.png",diff)
mask=diff*0
mask[:,:cut_x-int(minx)]=255
mask=cv2.GaussianBlur(mask,(255,1),sigmaX=-1)
cv2.imwrite("output\mask.png",mask)

out=diff*0
percent=mask/255.0
out=np.uint8(out1*percent+out2*(1-percent))
cv2.imwrite("output\out.png",out)


