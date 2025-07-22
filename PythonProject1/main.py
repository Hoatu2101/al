import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def count_fingers(hand_landmarks, handedness):
    fingers = []
    # Ngón cái
    if handedness == "Right":
        fingers.append(hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x)
    else:
        fingers.append(hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x)

    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]

    for tip, pip in zip(tips, pips):
        fingers.append(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y)

    return sum(fingers)

cap = cv2.VideoCapture(2)  # chỉnh số 0 nếu bạn dùng webcam mặc định

with mp_hands.Hands(
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Không nhận được hình từ camera.")
            break

        image = cv2.flip(image, 1)  # lật ảnh để nhìn như gương
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False

        results = hands.process(image_rgb)

        image_rgb.flags.writeable = True
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                hand_label = hand_handedness.classification[0].label  # "Right" hoặc "Left"
                finger_count = count_fingers(hand_landmarks, hand_label)

                # Vẽ landmarks bàn tay
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                # Hiển thị số ngón tay đếm được
                cv2.putText(image, f'{hand_label} hand: {finger_count} fingers',
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                if finger_count == 1:
                    cv2.putText(image, "FUCK YOU ! ", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                if finger_count == 2:
                    cv2.putText(image,"CAI LON ",(10,70),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 0), 2)
        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:  # Nhấn ESC để thoát
            break

cap.release()
cv2.destroyAllWindows()
