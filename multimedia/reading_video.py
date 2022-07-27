import cv2

video= cv2.VideoCapture(r'C:\Users\ASPIRE 3\Documents\Python digipodium\sample_video.mkv')

while True:
    state, img= video.read()
    if state:
        cv2.imshow("video output",img)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
video.release()
cv2.destroyAllWindows()