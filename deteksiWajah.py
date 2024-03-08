import cv2

# Import webcam
cam = cv2.VideoCapture(0)
cam.set(3, 640) #ubah lebar
cam.set(4, 480) #ubah tinggi

# Import file xml
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Menangkap Gambar per FPS
while True :
    retV, frame = cam.read()
    abuabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Program face Detection dengan Algoritma Hear-Cascade
    faces = faceDetector.detectMultiScale(abuabu, 1.3, 5)
    for (x, y, w, h) in faces :
        frame = cv2.rectangle( frame, (x,y), (x+w, y+h), (0,0,255), 2)
        abuabu = cv2.rectangle(abuabu, (x,y), (x+w, y+h), (0,0,255), 2)

    # Menampilkan ke webcam
    cv2.imshow("Webcamku" , frame)
    cv2.imshow("Webcam 2 - Gray" , abuabu)

    # Tombol Stop
    k = cv2.waitKey(1) & 0xFF 
    if k == 27 or k == ord('q'):
       break

# Menghapus Memori
cam.release()
cv2.destroyAllWindows()


