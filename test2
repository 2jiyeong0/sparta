import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)    # 모델로드

# 이미지 저장
img = cv2.imread('image.jpeg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()    # 판다스 -> 넘파이배열
result = [item for item in result if item[6]=='person']


tmp_img = cv2.imread('image.jpeg')
print(tmp_img.shape)
cropped = tmp_img[int(result[0][1]):int(result[0][3]), int(result[0][0]):int(result[0][2])]
print(cropped.shape)
cv2.imwrite('people1.png', cropped)
cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (255,255,255))
cv2.imwrite('result.png', tmp_img)
