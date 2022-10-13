import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)    # 모델로드

img = cv2.imread('image.jpeg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()    # 판다스 -> 넘파이배열
result = [item for item in result if item[6]=='person']

tmp_img = cv2.imread('image.jpeg')
print(tmp_img.shape)

for i in range(len(result)):
    cv2.rectangle(tmp_img, (int(results.xyxy[0][i][0].item()), int(results.xyxy[0][i][1].item())), (int(results.xyxy[0][i][2].item()), int(results.xyxy[0][i][3].item())), (255,255,255))
    cv2.imwrite('result1.png', tmp_img)

