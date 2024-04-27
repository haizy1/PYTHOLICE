import urllib.request
import numpy as np
import cv2
url1="http://10.12.131.237:8080/shot.jpg"
url2="http://192.168.8.105:8080/shot.jpg"
while True:
    img_arr1=np.array(bytearray(urllib.request.urlopen(url1).read()),dtype=np.uint8)
    img1=cv2.imdecode(img_arr1,-1)
    #cv2.imshow("webcam1",img1)
    img_arr2=np.array(bytearray(urllib.request.urlopen(url2).read()),dtype=np.uint8)
    img2=cv2.imdecode(img_arr2,-1)
    #cv2.imshow("webcam2",img2)
    dim=(500,300)
    resized1=cv2.resize(img1,dim)
    resized2=cv2.resize(img2,dim)
    hori=np.concatenate((resized1,resized2),axis=0)
    cv2.imshow("Result",hori)
    if cv2.waitKey(1)==ord('q'):
        break;
cv2.destroyAllWindows()

    
    
       