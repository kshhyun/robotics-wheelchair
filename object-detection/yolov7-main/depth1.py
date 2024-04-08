import pyrealsense2 as rs
import cv2
import numpy as np
import torch
import time
from models.experimental import attempt_load
from utils.general import check_img_size, non_max_suppression, scale_coords
from utils.plots import plot_one_box
from utils.torch_utils import select_device

# YOLOv7 모델 로드
device = select_device('0')  # GPU 디바이스 선택
model = attempt_load('yolov7.pt', map_location=device)

# 깊이 카메라 설정
context = rs.context()
pipeline = rs.pipeline(context)
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 90)
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

time.sleep(2)

pipeline.start(config)

# 깊이 카메라에서 가져오기
while True:
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    if not depth_frame:
        continue

    depth_image = np.asanyarray(depth_frame.get_data())
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

    img_size = 640  # 입력 이미지 크기
    conf_thres = 0.5  # Confidence 임계값
    iou_thres = 0.5  # IoU 임계값

    # 모델 추론
    img = torch.zeros((1, 3, img_size, img_size), device=device)  # 모델 입력 형태에 맞게 데이터 생성
    pred = model(img)

    # 후처리
    pred = non_max_suppression(pred[0], conf_thres, iou_thres)
    for det in pred[0]:
        if det is not None and len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], depth_image.shape).round()
            for *xyxy, conf, cls in reversed(det):
                label = f'{cls} {conf:.2f}'
                xyxy = [int(x) for x in xyxy]
                plot_one_box(xyxy, depth_colormap, label=label)

    # 시각화
    cv2.imshow('Depth Camera', depth_colormap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pipeline.stop()
cv2.destroyAllWindows()
