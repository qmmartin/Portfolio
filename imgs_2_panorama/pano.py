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

def bbox(img):
	h,w=img.shape[:2]
	points=np.float32([[0,0],[w,0],[w,h],[0,h]])
	return points    

def Translate_Gen (dx, dy):
	return np.float64([[1,0,dx],
						[0, 1, dy], 
						[0,0,1]])

image1=cv2.imread("input\piggly1.png")
image2=cv2.imread("input\piggly2.png")
image3=cv2.imread("input\piggly3.png")

image1=image1[::2,::2]
image2=image2[::2,::2]
image3=image3[::2,::2]


orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(image1,None)
kp2, des2 = orb.detectAndCompute(image2,None)
kp3, des3 = orb.detectAndCompute(image3,None)
# ~ print(len(kp1))
# ~ print(len(kp2))
# ~ input()
# out=cv2.drawKeypoints(image1,kp1,None, color=(0, 0, 0))
# show(out[::3,::3])
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
rc_matches = bf.knnMatch(des1,des2,k=2)
lc_matches = bf.knnMatch(des2,des3,k=2)
# ~ print(matches)
rc_good_matches=[]
for best_match,second_best_match in rc_matches:
	if best_match.distance<.75*second_best_match.distance:
		rc_good_matches.append(best_match)
		
lc_good_matches=[]
for best_match,second_best_match in lc_matches:
	if best_match.distance<.75*second_best_match.distance:
		lc_good_matches.append(best_match)
	



rc_match=cv2.drawMatches(image1,kp1,image2,kp2,rc_good_matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
lc_match=cv2.drawMatches(image2,kp2,image3,kp3,lc_good_matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

matched = np.vstack((lc_match, rc_match))

cv2.imwrite("output\matches.png", matched)

src_points=[]
dest_points=[]
for m in rc_good_matches:
	src_points.append(kp1[m.queryIdx].pt)
	dest_points.append(kp2[m.trainIdx].pt)

src_points=np.float32(src_points)
dest_points=np.float32(dest_points)

H1,_=cv2.findHomography(src_points,dest_points,method=cv2.RANSAC,ransacReprojThreshold=2,maxIters=10000000)

points=bbox(image1)
out_points=cv2.perspectiveTransform(points[:,None,:],H1) 
cut_x=int(out_points[1,0,0]/2)


all_points=np.vstack((points,out_points[:,0,:]))

X,Y=all_points.T

minx=X.min()
maxx=X.max()
miny=Y.min()
maxy=Y.max()
T=np.float32([[1,0,-minx],[0,1,-miny],[0,0,1]])


new_width=int(maxx-minx)
new_height=int(maxy-miny)
print(new_width, new_height)




out1=cv2.warpPerspective(image1,T@H1,(new_width,new_height))
out2=cv2.warpPerspective(image2,T,(new_width,new_height))


diff=np.uint8(abs(out1*1.0-out2))

cv2.imwrite("output\diff.png",diff[::2,::2])

mask=diff*0
mask[:,:cut_x-int(minx)]=255
mask=cv2.GaussianBlur(mask,(255,1),sigmaX=-1)

cv2.imwrite("output\mask.png",mask[::2,::2])

out=diff*0
percent=mask/255.0
out=np.uint8(out1*percent+out2*(1-percent))

image4=out
show(image4[::4,::4])
kp4, des4 = orb.detectAndCompute(image4,None)
stitch_matches = bf.knnMatch(des3,des4,k=2)

stitch_good_matches=[]
for best_match,second_best_match in stitch_matches:
	if best_match.distance<.75*second_best_match.distance:
		stitch_good_matches.append(best_match)

src_points2=[]
dest_points2=[]
for m in stitch_good_matches:
	src_points2.append(kp3[m.queryIdx].pt)
	dest_points2.append(kp4[m.trainIdx].pt)

src_points2=np.float32(src_points2)
dest_points2=np.float32(dest_points2)

H2,_=cv2.findHomography(src_points2,dest_points2,method=cv2.RANSAC,ransacReprojThreshold=2,maxIters=10000000)

points=bbox(image4)

out_points=cv2.perspectiveTransform(points[:,None,:], H2)
cut_x=int(out_points[1,0,0]/2.35)
all_points=np.vstack((points,out_points[:,0,:]))

X,Y=all_points.T

minx=X.min()
maxx=X.max()
miny=Y.min()
maxy=Y.max()
T=np.float32([[1,0,-minx],[0,1,-miny],[0,0,1]])



I=np.float32([[1,0,0], [0,1,0], [0,0,1]])
new_width=int(maxx-minx)
new_height=int(maxy-miny)


blank=np.zeros((new_width, new_height))

out1=cv2.warpPerspective(image1,T@H1,(new_width,new_height))
out2=cv2.warpPerspective(image2,T,(new_width,new_height))
out3=cv2.warpPerspective(image3, T@H2, (new_width,new_height))
out4=cv2.warpPerspective(image4, T, (new_width,new_height))

cv2.imwrite("output\out1.png",out1[::2,::2])
cv2.imwrite("output\out2.png",out2[::2,::2])
cv2.imwrite("output\out3.png",out3[::2,::2])
cv2.imwrite("output\out4.png",out4[::2,::2])


diff2=np.uint8(abs(out4*1.0-out3))
mask2=diff2*0
mask2[:,:cut_x-int(minx)]=255
mask2=cv2.GaussianBlur(mask2,(255,1),sigmaX=-1)

cv2.imwrite("output\mask2.png", mask2[::2,::2])

final=diff2*0
percent=mask2/255.0
final=np.uint8(out4*percent+out3*(1-percent))

cv2.imwrite("output\panoFinal.png", final[::2,::2])

panorama_image=final
gray = cv2.cvtColor(panorama_image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest_contour)
cropped_image = panorama_image[y:y+h, x:x+w]

cv2.imwrite("output\cropped_panoFinal.png", cropped_image)