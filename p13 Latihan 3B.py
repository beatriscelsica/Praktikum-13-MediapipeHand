import cv2
import mediapipe as mp
cap = cv2.VideoCapture(1)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            h, w, _ = img.shape

            index_x = int(hand_landmarks.landmark[5].x * w)
            pinky_x = int(hand_landmarks.landmark[17].x * w)

            if index_x < pinky_x:
                arah = "DEPAN"
                warna = (0, 225, 0)
            else:
                arah = "BELAKANG"
                warna = (0, 0, 225)
            cv2.putText(img, arah, (200, 50),
                        cv2.FONT_HERSHEY_PLAIN, 5, warna, 3)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("webcam", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()