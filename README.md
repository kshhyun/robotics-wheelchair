# 자율주행 휠체어 로봇 [데굴이]

## 1. 프로젝트 개요
복잡한 병원 환경에 실시간 대응하는 지능형 휠체어 로봇 제작하였습니다.
보호자의 도움없이 간단한 조작으로 환자의 편의성 및 병원 내 혼잡도 감소를 목표로 설정하였습니다.
<br/><br/>

## 2. 개발 스택
### OS
- Linux(Ubuntu 20.04 LTS)
- ROS2(melodic)

### 개발환경(IDE)
Visual Studio Code, Arduino

### H/W
- LiDAR 센서
- Turtlebot3 burger
- TTS 모듈

### S/W
- RViz
- Node-Red
- Cartographer
- Navigation2
  
### 개발언어
- Bash
- Python
  
### 알고리즘
- DWA (Dynamic Window Approach)
- slam (Simultaneous Localization And Mapping)
<br/><br/>

## 3. 프로젝트 구조
- ROS(Robot Operating System) : 로봇 개발을 위한 운영체제
- publisher, Subscriber를 통한 송수신
  #### 사용자 <-> 로봇
  ![image](https://github.com/user-attachments/assets/db22e2ab-003d-481d-9985-58d64e9261fe)

  #### 사용자 <-> 관리자
  ![image](https://github.com/user-attachments/assets/1e4a12f1-0255-4e56-ad3f-fe27facee1ab)


<br/><br/>

## 4. 주요 기능
- **병원 지도 작성** : LiDAR를 활용한 SLAM 기술로 병원 내 지도 작성 및 위치 파악.

  ![image](https://github.com/user-attachments/assets/0ef4160b-8d45-4bc4-8644-27d9e419415a)

- **자율주행 기능** : 설정된 목적지까지 경로 탐색 후 스스로 이동하며, 목적지 설정 기능을 제공.

  ![image](https://github.com/user-attachments/assets/51ef20dc-ee0f-4283-991f-06332525df5b)

- **장애물 회피** : DWA 알고리즘과 LiDAR 센서를 활용해 장애물을 인식하고 회피 경로를 탐색.

  ![image](https://github.com/user-attachments/assets/c7512429-e371-4006-b801-9314391e074b)
  
- **수동 조작 기능** : 방향키 조작으로 휠체어의 기본적인 수동 조작 가능.

  ![image](https://github.com/user-attachments/assets/1320ec1a-bf83-4093-966a-368cbf5769d3)

- **긴급 호출 및 주행 제어** :
  - **주행 권한 제어** : 긴급 호출 시 즉시 정지하고 음성 안내(TTS)를 통해 경고하며, 위급 상황이 종료될 때까지 조작이 제한.
  - **긴급 호출 알림** : 긴급 호출 시 관리자 페이지에 호출 알림창 표시 및 휠체어 조작 권한 부여.

    ![image](https://github.com/user-attachments/assets/ac0fe4d0-a9b4-45e3-baa3-2614bbad9f92)
