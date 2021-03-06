import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while(cap.isOpened()):
   ret, frame = cap.read()
   cv2.imshow('frame', frame)
   if cv2.waitKey(1) & 0xFF == ord(' '):
       out.write(frame)
   elif cv2.waitKey(1) & 0xFF == ord('q'):
       break
cap.release()
out.release()
cv2.destroyAllWindows()