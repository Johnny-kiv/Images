import cv2
import face_recognition

# Включаем первую камеру
cap = cv2.VideoCapture(0)

# "Прогреваем" камеру, чтобы снимок не был тёмным
for i in range(30):
    cap.read()

# Делаем снимок
ret, frame = cap.read()

# Записываем в файл
cv2.imwrite('imgs/input.png', frame)

# Отключаем камеру
cap.release()
def compare_faces(img_path):
    ves_j = face_recognition.load_image_file("imgs/ves_j.png")
    ves_j_encoding = face_recognition.face_encodings(ves_j)[0]
    ves_v = face_recognition.load_image_file("imgs/ves_v.jpg")
    ves_v_encoding = face_recognition.face_encodings(ves_v)[0]
    img = face_recognition.load_image_file("imgs/input.png")
    img_encoding = face_recognition.face_encodings(img)[0]
    result_j = face_recognition.compare_faces([ves_j_encoding],img_encoding)
    result_v = face_recognition.compare_faces([ves_v_encoding],img_encoding)
    if result_j==[True]: return "Привет, Ваня"
    elif result_v==[True]: return "Здравствуйте, Владимир!"
    else: return "Привет! Ты кто?"
#    print(result)


def main():
   # face_rec()
   print(compare_faces(img_path="imgs/input.png"))


if __name__ == '__main__':
    main()