import cv2

img = cv2.imread('galapagos.jpg') 

cv2.imshow('Ventana', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
