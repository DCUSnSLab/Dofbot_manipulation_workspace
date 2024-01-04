# Yahboom사의 Dofbot Robotic Arm을 활용한<br/>자율주행 차량(SCV)의 보행자 트래킹 기술
> Dofbot 제품의 [공식 가이드](http://www.yahboom.net/study/Dofbot-Pi) 참고


## 리포지토리 및 작업공간
* 리포지토리 구조
```
Dofbot_manipulation_workspace/
├── Arm/
├── Dofbot/
├── catkin_ws/
├── dofbot_ws/
│   ├── src/
│   │   ├── dofbot_moveit/
│   │   │   ├── urdf/
│   │   │   │   └── dofbot.urdf
│   │   │   ├── meshes/
│   │   │   │   ├── base_link.STL
│   │   │   │   ├── link1.STL
│   │   │   │   ├── link2.STL
│   │   │   │   ├── link3.STL
│   │   │   │   ├── link4.STL
│   │   │   │   └── link5.STL
│   │   │   ├── launch/
│   │   │   │   ├── dofbot_moveit.launch
│   │   │   │   ├── vis_launch.launch
│   │   │   │   ├── bag_sim.launch
│   │   │   │   └── control_sim.launch
│   │   │   └── scripts/
│   │   │       ├── robot_manipulation.py
│   │   │       ├── tf_broadcaster_new.py
│   │   │       ├── bounding_box_design.py
│   │   │       ├── bbox_gui.py
│   │   │       ├── bbox_real.py
│   │   │       ├── bbox_rviz.py
│   │   │       ├── generate_random_objs.py
│   │   │       ├── generated_objs_gui.py
│   │   │       ├── generated_objs_real.py
│   │   │       ├── generated_objs_rviz.py
│   │   │       ├── Arm_Lib/
│   │   │       │   └── Arm_Lib.py
│   │   │       └── legacy_scripts/
│   │   │           ├── bbox_subscriber.py
│   │   │           ├── drawLine_new.py
│   │   │           └── pubsubcp.py
│   │   └── zed-ros-interfaces/
│   ├── devel/
│   └── build/
└── ubuntu20.04_library/
    └── libdofbot_kinemarics.so (Dofbot 라이브러리, 설치 필요)
```
* 주 작업공간 : [/dofbot_ws](./dofbot_ws)
  
| 패키지 | 설명 |
| --- | --- |
| [dofbot_moveit](./dofbot_ws/src/dofbot_moveit)  | Dofbot 로봇팔의 움직임을 Rviz에 시각화하는 패키지  |
| [zed-ros-interfaces](./dofbot_ws/src/zed-ros-interfaces)  | ZED 카메라의 Object Detection 토픽 활용을 위한 패키지(SDK로 설치 필요)  |

<br/>

## 매뉴얼

![image](https://github.com/DCUSnSLab/Dofbot_manipulation_workspace/assets/102202662/57fa9be3-a40b-48d8-aa98-5b57f8352420)

### 개발환경
* Manipulator
  * `ROBOT COM` : Raspberry 4 model B, Ubuntu 20.04 LTS, bash쉘 사용
  * Robotic Arm : Yahboom DOFBOT AI Vision Robotic Arm with ROS<br/>(https://category.yahboom.net/collections/r-robotics-arm/products/dofbot-pi)
    * 단, 로봇 팔의 서보모터 6개 중 **2개(1, 2번 서보모터)만 사용**함.<br/>나머지 4개의 서보모터를 떼어내는 개조 필요.
* `HOST COM` : Ubuntu 20.04 LTS, bash쉘 사용
* ROS : [ROS1 Noetic](https://wiki.ros.org/noetic/Installation/Ubuntu) - Python3 기반
* Sensor
  * LiDAR : Velodyne LiDAR VLP-32C
    * **/velodyne_points 토픽** 사용
  * CAMERA : ZED2i CAMERA
    * **/zed2i/zed_node/obj_det/objects 토픽** 사용

### 개발 준비
* `ROBOT COM` 세팅
  * 함께 배송되는 라즈베리파이4는 Ubuntu 20.04 LTS 기반의 ROS(Noetic)를 포함한 Dofbot 로봇팔과 관련된 패키지가 설치되어 있음. 추가적인 설정 불필요.
  * ROS 원격 연결 및 SSH 접속
    * `ifconfig` 명령어 이용해 IP 확인 ~~(2023.12.18 기준 XXX.XXX.X.3 사용)~~
    * `ROBOT COM`의 ~/.bashrc 파일에 내용 추가
      * `$ROS_MASTER_URI=http://{HOST IP}:11311`
      * `$ROS_HOSTNAME={ROBOT IP}`
    * SSH 접속 기본 암호(yahboom) 입력 필요
* `HOST COM` 세팅
  * Ubuntu 20.04 LTS 버전 설치
  * ROS1 Noetic 버전 설치
  * `HOST COM`의 로컬 경로(~)에 리포지토리 clone
  * ubuntu20.04_library 디렉토리 내의 라이브러리 설치
    * `HOST COM`의 로컬 경로(/usr/lib)로 [libdofbot_kinemarics.so](./ubuntu20.04_library) 파일 이동
  * ROS 원격 연결
    * `ifconfig` 명령어 이용해 IP 확인 ~~(2023.12.18 기준 XXX.XXX.X.2 사용)~~
    * `HOST COM`의 ~/.bashrc 파일에 내용 추가
      * `$ROS_MASTER_URI=http://{HOST IP}:11311`
      * `$ROS_HOSTNAME={HOST IP}`
        
### 개발 진행 중
dofbot_moveit 패키지 내부의 scripts 디렉토리에서 모든 코드 작업.
(작업 완료 후 트래킹 관련 파일들만 모아 새 패키지 생성할 예정)

하단은 작업 완료되었거나 작성 중인 코드 목록.
* `scripts/` : **로봇팔을 움직이는 모든 코드와 라이브러리가 포함된 디렉토리**
  * `legacy_scripts/` : 지금은 사용하지 않으나, 새로 작성하는 코드들의 근간이 되는 코드 레퍼런스가 저장된 디렉토리
    * bbox_subscriber.py - ROBOT COM에서 실행하던 코드로, 객체를 바라보도록 로봇팔을 움직인 뒤 로봇팔의 현재 각도를 Rviz로 전달하는 역할
    * drawLine_new.py - Rviz에서 로봇팔 모델이 정확히 객체의 정중앙을 가리키는지 확인하기 위한 코드
    * pubsubcp.py - bag 파일이 전달하는 데이터 중 객체 데이터를 기반으로 BoundingBox를 생성해 MarkerArray 형태로 뿌리는 코드로, bbox_subscriber.py가 받아서 사용했음
  * `Arm_Lib/` : Dofbot 로봇팔을 움직이는 함수들이 전부 들어있는 중요한 라이브러리
  * robot_manipulation.py - 로봇팔을 움직인 뒤 현재 각도를 Rviz로 전달하는 역할이며, 래거시 스크립트 중 bbox_subscriber.py의 경량화 코드로 지금은 메인 코드로써 사용하나, 시뮬레이션 파트로 넘어가면 래거시 스크립트로 보낼 예정
  * tf_broadcaster_new.py - TF를 담당하는 코드
  * bounding_box_design.py - bag 파일이 전달하는 데이터 중 객체 데이터를 기반으로 BoundingBox를 생성해 MarkerArray 형태로 뿌리는 코드로, 래거시 스크립트 중 pubsubcp.py의 경량화 코드이며, 8개의 LINE_STRIP으로 BoundingBox를 구성하던 이전의 방식을 CUBE 타입으로 변경
  * bbox_gui.py
  * bbox_real.py
  * bbox_rviz.py
  * generate_random_objs.py - bag 파일 없이 임의로 객체를 3개까지 생성하여 MarkerArray 형태로 뿌리는 코드, 해당 메시지는 BoundingBox와 동일한 역할을 함
  * generated_objs_gui.py
  * generated_objs_real.py
  * generated_objs_rviz.py
* `launch/` : **모든 런치 파일들이 포함된 디렉토리**
  * dofbot_moveit.launch - Dofbot 제품에 포함된 런치 파일 원본
  * vis_launch.launch - 래거시 코드
  * bag_sim.launch - bag 파일을 활용한 시뮬레이션에 쓰이는 런치 파일
  * control_sim.launch - 임의 객체를 활용한 시뮬레이션에 쓰이는 런치 파일
