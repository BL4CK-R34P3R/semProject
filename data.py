import pandas as pd


import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands





#df = pd.read_csv('data.csv') scope problem is used here use non local google if you dont remember stuff


def get_data(hand_landmarks):

	df = pd.read_csv('data.csv')
	print(len(df.columns))

	data_list =[
                        hand_landmarks.landmark[mp_hands.HandLandmark(0).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(1).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(2).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(3).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(4).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(5).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(6).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(7).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(8).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(9).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(10).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(11).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(12).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(13).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(14).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(15).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(16).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(17).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(18).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(19).value],
                        hand_landmarks.landmark[mp_hands.HandLandmark(20).value]                        

                ]

	series_data = pd.Series(data_list ,index=df.columns )
	df = df.append(  series_data,ignore_index=True)
	df.to_csv('data1.csv')
	
	
cap = cv2.VideoCapture(0)  # 2 for webcam
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference dont really know shit what this writable do.
    #image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)




    df = pd.read_csv('data.csv')
    # Draw the hand annotations on the image.
    #image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

        #print(type(f'{hand_landmarks.landmark[mp_hands.HandLandmark(5).value]}'))
        #print(f'{hand_landmarks.landmark[mp_hands.HandLandmark(5).value].x}')
        #print(f'{mp_hands.HandLandmark(5).name}')
        get_data(hand_landmarks)
                
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
