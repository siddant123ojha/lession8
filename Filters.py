import cv2
import numpy as np
def apply_filter(filter_type, img_path, gray_img_path):
    if filter_type=="original":
        return img_path
    elif filter_type=="sobel":
        sobelx=cv2.Sobel(gray_img_path,cv2.CV_64F,1,0,ksize=3)
        sobely=cv2.Sobel(gray_img_path,cv2.CV_64F,0,1,ksize=3)
        combined_sobel=cv2.bitwise_or(sobelx.astype("uint8"), sobely.astype("uint8"))
        return cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type =="canny":
            edges=cv2.Canny(gray_img_path,100,200)
            return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif filter_type=="black_white":
            bw_img_path=cv2.threshold(gray_img_path,127,255,cv2.THRESH_BINARY)
            return cv2.cvtColor(bw_img_path, cv2.COLOR_GRAY2BGR)
    elif filter_type=="median":
            return cv2.medianBlur(img_path,5)
    elif filter_type == "gaussian":
            return cv2.GaussianBlur(img_path,(5,5),0)
    elif filter_type == "sepia":
            sepia_filter=np.array([[0.272,0.534,0.131],
                                   [0.349,0.686,0.163],
                                   [0.393,0.769,0.189]])
            sepia_img_path=cv2.transform(img_path,sepia_filter)
            sepia_img_path=np.clip(sepia_img_path,0,255)
            return sepia_img_path.astype("uint8")
    elif filter_type=="red_tint":
           red_tint=img_path.copy()
           red_tint[:,:,1]=0
           red_tint[:,:,0]=0
           return red_tint
    elif filter_type=="blue_tint":
           blue_tint=img_path.copy()
           blue_tint[:,:,1]=0
           blue_tint[:,:,2]=0
           return blue_tint
    else: return img_path

img_path=cv2.imread("3x3 logo.png")
if img_path==None:
       print("Error: img_path not found")
else:
       gray_img_path=cv2.cvtColor(img_path,cv2.COLOR_BGR2RGB)
       filter_type="original"

       print("press the following keys to apply filters:")
       print("O = Original img_path")
       print("S = Sobel Edge Detection")
       print("C = Canny Edge Detection")
       print("G = Gaussian Blur")
       print("M = Median Filtering")
       print("B = Black and White")
       print("P = Sepia Effect")
       print("R = Red tint")
       print("BT = Blue tint")
       print("q = Quit")
       while True:
             filteredimg_path=apply_filter(filter_type,img_path,gray_img_path)
             cv2.imshow("Filtered Image",filteredimg_path)
             key=cv2.waitKey(0) & 0xFF
             if key==ord("o"):
                    filter_type="original"
             elif key==ord("s"):
                    filter_type="sobel"
             elif key==ord("c"):
                    filter_type="canny"
             elif key==ord("g"):
                    filter_type="gaussian"
             elif key==ord("m"):
                    filter_type="median"
             elif key==ord("b"):
                    filter_type="black and white"
             elif key==ord("p"):
                    filter_type="sepia"
             elif key==ord("r"):
                    filter_type="red_tint"
             elif key==ord("bt"):
                    filter_type="blue_tint"
             elif key==ord("q"):
                    print("EXITING...")
                    break
             else:print("Invalid Key")
cv2.destroyAllWindows()