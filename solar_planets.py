import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.putText(img,"Mercury",(100,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(290,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Moon",(290,165),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Mars",(380,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(480,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(695,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(970,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("Solar_system",img)
cv2.waitKey(0)