import cv2

video= cv2.VideoCapture(0)

while True:
    state, img= video.read()
    if state:
        cv2.rectangle(img,(200,-10),(450,10),(0,255,0),-1)
        cv2.putText(img,"Made by Sakshi",(10,450), cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0),2)
        cv2.imshow("video output",img)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
video.release()
cv2.destroyAllWindows()
