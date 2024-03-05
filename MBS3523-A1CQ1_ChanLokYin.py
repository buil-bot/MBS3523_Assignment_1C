import cv2
import serial

# Create a serial object
ser = serial.Serial("com5", 9600)

# Create a video capture object for the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    sensor_value = ser.readline().decode().strip()
    cv2.putText(frame, f"Sensor Value: {sensor_value}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
ser.close()

cv2.destroyAllWindows()