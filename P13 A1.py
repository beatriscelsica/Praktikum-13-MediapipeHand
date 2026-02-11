import cv2 #import module opencv
import mediapipe
capture = cv2.VideoCapture(0) #video capture pada device kamera nomer 0
mediapipehand = mediapipe.solutions.hands #inisilisasi deteksi tangan
tangan = mediapipehand.Hands() #variable tangan untuk menyimpan konfigurasi deteksi tangan

while True:
    succes, img = capture.read() #menyimpan citra tangkap kamera ke img
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #merubah warna img ke RGB
    result = tangan.process(imgRGB) #melakukan pemrosesan dari citraimgRGB

    if result.multi_hand_landmarks:
        print("tangan") #ketika tangan terdeteksi menampilkan "tangan" pada terminal
    else:
        print("tidak ada") #ketika tangan terdeteksi menampilkan "tidak ada" pada teminal
    cv2.imshow("webcam", img)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
capture.release() #Tutup webcam dan jendela tampilan saat q ditekan
cv2.destroyAllWindows()




