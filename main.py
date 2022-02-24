import cv2 
import numpy as np 

def on_mouse(event, x, y, flags, param):
    if flags==cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),16,(0.0),-1)
    else:
        return 

def tomoire(img):
    array=np.array(img)
    output=np.zeros((img.shape[0],img.shape[1]))
    pitch=10
    for j in range(img.shape[0]):
        #rint("Progress : "+str(100*j//img.shape[0])+"%")
        for i in range(0,img.shape[1],2*pitch):
            t=array[j][i]
            if i>=img.shape[1]-(2*pitch):
                p=0
                while p+i<img.shape[1]:
                    output[j][p+i]=array[j][p+i]
                    p=p+1
                break
            if t>120:
                for k in range(pitch):
                    output[j][i+k]=255
                    output[j][i+pitch+k]=0
            else:
                for k in range(pitch):
                    output[j][i+k]=0
                    output[j][i+pitch+k]=255
    return output

if __name__=="__main__":
    width=640
    height=640
    pitch=10

    img=np.zeros((height,width))
    img.fill(255)
    initimg=img.copy()

    winName = 'Initial Image'
    cv2.imshow(winName,img)
    cv2.moveWindow(winName,20,20)
    
    cv2.setMouseCallback(winName, on_mouse)
    m_img=tomoire(img)

    #画面遷移2の時のカーソル調整コード
    while True:
        img_0 = img.copy()

        m_img=tomoire(img)
        cv2.imshow(winName,m_img)
        
        if cv2.waitKey(100) == 27:      # Esc Key
            break
        elif cv2.waitKey(100)==32:      # Space Key
            img=initimg.copy()
        elif cv2.waitKey(100)==13:      # Enter Key
            cv2.imwrite("./moire.png",m_img)
        
    cv2.destroyAllWindows()