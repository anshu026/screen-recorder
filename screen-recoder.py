import numpy as np
import cv2
import pyscreenshot as pys
#pyscreenchot library is used to take screenshot in this project
forcc = cv2.VideoWriter_fourcc(*'XVID')
o = cv2.VideoWriter('output.avi', forcc, 8, (1920,1080))
while True:
    img= pys.grab()
    img_np=np.array(img)

    #frame= cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Screen', img_np)
    out.write(img_np)


    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

o.release()
cv2.destroyAllWindows()
