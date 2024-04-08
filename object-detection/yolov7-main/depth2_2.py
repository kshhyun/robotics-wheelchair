import pyrealsense2 as rs
import cv2
import numpy as np
import torch
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords
from utils.plots import plot_one_box
from utils.torch_utils import select_device

# YOLOv7 모델 로드
device = select_device('0')  # 첫번째(0) GPU 디바이스 선택
model = attempt_load('yolov7.pt', map_location=device) # 선택한 디바이스에 yolov7 모델 옮기기

# 깊이 카메라 설정
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

profile = pipeline.start(config)

# 깊이 카메라에서 가져오기
while True:
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()
    
    if not depth_frame or not color_frame:
        continue

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    
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
                plot_one_box(xyxy, color_image, label=label)

    color_height, color_width, _ = color_image.shape
    depth_height, depth_width, _ = depth_colormap.shape

    color_image_resized = cv2.resize(color_image, (depth_width, depth_height))

    # 시각화
    stacked_images = np.hstack((color_image_resized, depth_colormap))
    cv2.imshow('Depth Camera with YOLOv7', stacked_images)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):  # 's' 키를 누르면 이미지 저장
        cv2.imwrite('output.jpg', stacked_images)