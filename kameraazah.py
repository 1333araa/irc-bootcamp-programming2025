import cv2

nama_peserta = "Azahra Salsabila"

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    if not ret:
        break


    cv2.putText(frame, f"Nama: {nama_peserta}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    
    cv2.imshow("Kamera", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 
kamera.release()
cv2.destroyAllWindows()
