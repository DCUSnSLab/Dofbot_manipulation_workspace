from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import math
import numpy

class DofbotApp(QWidget):

    def __init__(self):
        super().__init__()

        ## 창 전체를 구성하는 레이아웃을 선언합니다.
        self.window_layout = QGridLayout()

        ## 객체목록 구성요소를 선언합니다.
        self.group_box = QGroupBox('생성된 객체 목록')
        self.group_box_vbox = QVBoxLayout()
        self.obj_layers = {}
        self.cbs = []
        self.info_boxes = []
        self.labels_obj = []
        self.coord = []
        self.viz_objs = []  # 현재 활성화된 객체의 인덱스를 저장합니다.(int, 0 ~ 2)

        ## 버튼박스 구성요소를 선언합니다.
        self.btn_box = QGroupBox('조작 도구')
        self.btn_box_vbox = QVBoxLayout()
        self.obj_add_btn = QPushButton('객체 추가')
        self.obj_rm_btn = QPushButton('선택한 객체 삭제')
        self.play_box = QHBoxLayout()
        self.start_btn = QPushButton('시작')
        self.stop_btn = QPushButton('정지')

        ## 트래킹창 구성요소를 선언합니다.
        self.labels_trk_top = [QLabel('목표 객체: '), QLabel('객체 위치(2차원): '), QLabel('회전 각도(DE/RA): ')]
        self.obj_name_top = QLineEdit('-')
        self.tracking_box_top = QGroupBox('1번 서보모터(XY축)')
        self.tracking_box_top_hbox = QHBoxLayout()
        self.frame_XY = QFrame(self)
        self.coordXY_layout = QVBoxLayout(self.frame_XY)
        self.view_top = QGraphicsView()
        self.scene_top = QGraphicsScene()
        self.right_box_top = QVBoxLayout()
        self.man_info_top = [QGridLayout(), QGridLayout(), QGridLayout()]
        self.obj_coord_XY = QLineEdit('(0, 0)')
        self.angle_servo1 = QLineEdit('0 / 0')
        self.line_trk_top = [self.obj_name_top, self.obj_coord_XY, self.angle_servo1]

        self.labels_trk_bottom = [QLabel('목표 객체: '), QLabel('객체 위치(2차원): '), QLabel('회전 각도(DE/RA): ')]
        self.obj_name_bottom = QLineEdit('-')
        self.tracking_box_bottom = QGroupBox('2번 서보모터(XZ축)')
        self.tracking_box_bottom_hbox = QHBoxLayout()
        self.frame_XZ = QFrame(self)
        self.coordXZ_layout = QVBoxLayout(self.frame_XZ)
        self.view_bottom = QGraphicsView()
        self.scene_bottom = QGraphicsScene()
        self.right_box_bottom = QVBoxLayout()
        self.man_info_bottom = [QGridLayout(), QGridLayout(), QGridLayout()]
        self.obj_coord_XZ = QLineEdit('(0, 0)')
        self.angle_servo2 = QLineEdit('0 / 0')
        self.line_trk_bottom = [self.obj_name_bottom, self.obj_coord_XZ, self.angle_servo2]

        ## 프로그램 창을 엽니다.
        self.init_UI()

    def set_window_center(self):
        '''
        프로그램 창을 모니터 중앙으로 옮깁니다.
        :return: None
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    ## 객체의 움직임 매커니즘을 정의하고, 프로그램 창에 반영하는 기능을 구현합니다.
    def move_obj(self, index: int):
        '''
        (활성화된) 해당 객체의 위치를 임의로 조정합니다.
        :param index: 객체의 번호
        :return: None
        '''
    def set_group_box(self):
        '''
        현재 활성화된 객체를 객체목록에 표시합니다.
        :return: None
        '''
    def set_coords(self):
        '''
        트래킹창 내부의 좌표계에 객체와 직선을 표시합니다.
        :return: None
        '''

    ## 프로그램 창을 업데이트합니다. (한 프레임)
    def update_sim(self):
        '''
        move_obj > set_group_box > set_coords > set_right_box 순으로 프로그램의 한 프레임을 구성합니다.
        :return: None
        '''

    ## 버튼의 기능을 정의하고 각 버튼에 부여합니다.
    def del_this_obj(self, indexes: list):
        '''
        [선택한 객체 삭제] 버튼의 기능으로, 선택된 객체를 모두 비활성화한 후, 나머지 (활성화된) 객체의 인덱스를 앞으로 몰아 정리합니다.
        이 메서드는 viz_objs에서 해당 객체들을 모두 삭제한 후, 객체 인덱스를 앞으로 몹니다.
        비활성화된 객체는 바로 사라지지 않고, 업데이트(init_obj_bbox) 전까지 프로그램 창에 남아있습니다.
        :param indexes: 선택된 (삭제할) 객체의 번호
        :return: None
        '''
    def add_next_obj(self):
        '''
        [객체 추가] 버튼의 기능으로, 비활성화된 객체 중 가장 앞순서의 객체를 활성화합니다.
        이 메서드는 viz_objs에 객체만 추가합니다.
        객체는 활성화되더라도 업데이트(init_obj_bbox) 전까지 프로그램 창에 보이지 않습니다.
        :return: None
        '''
    def stop_timer(self):
        '''
        [정지] 버튼의 기능으로, 프로그램 창의 움직임을 멈춥니다.
        :return: None
        '''
    def start_timer(self):
        '''
        [시작] 버튼의 기능으로, 프로그램 창의 움직임을 재개합니다.
        :return: None
        '''

    ## 기본UI(고정)를 구현합니다.
    def set_obj_layers(self):
        '''
        객체 전체를 정의합니다.
        :return: None
        '''
    def set_trk_box_1(self):
        '''
        상단 트래킹창을 구성합니다.
        :return: None
        '''
        for i in range(3):  # right_box_top
            self.man_info_top[i].setColumnStretch(0, 1)
            self.man_info_top[i].setColumnStretch(1, 1)
            self.labels_trk_top[i].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.line_trk_top[i].setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.line_trk_top[i].setReadOnly(True)
            self.man_info_top[i].addWidget(self.labels_trk_top[i], i, 0)
            self.man_info_top[i].addWidget(self.line_trk_top[i], i, 1)
            self.right_box_top.addLayout(self.man_info_top[i])

        #self.frame_XY.setGeometry(0, 0, 500, 500)
        self.frame_XY.setLineWidth(1)
        self.frame_XY.setFrameShape(QFrame.Box)
        self.frame_XY.setFrameShadow(QFrame.Plain)
        line1_x = QGraphicsLineItem(-250, 0, 250, 0)
        line1_y = QGraphicsLineItem(0, -250, 0, 250)
        tx1 = QGraphicsTextItem('x축')
        tx1.setPos(275, -10)
        ty1 = QGraphicsTextItem('y축')
        ty1.setPos(-15, -285)
        base1 = QGraphicsRectItem(-50, -150, 100, 200)
        base1.setPen(QPen(Qt.gray, 5))
        servo1 = QGraphicsRectItem(-200, -10, 200, 20)
        servo1.setBrush(Qt.green)
        servo1.setPen(QPen(Qt.darkGreen, 3))
        self.scene_top.addItem(servo1)
        self.scene_top.addItem(base1)
        self.scene_top.addItem(line1_x)
        self.scene_top.addItem(tx1)
        self.scene_top.addItem(line1_y)
        self.scene_top.addItem(ty1)
        self.view_top = QGraphicsView(self.scene_top)
        self.coordXY_layout.addWidget(self.view_top)
        self.frame_XY.setLayout(self.coordXY_layout)
        self.tracking_box_top_hbox.addWidget(self.frame_XY)
        self.tracking_box_top_hbox.addLayout(self.right_box_top)
        self.tracking_box_top.setLayout(self.tracking_box_top_hbox)

    def set_trk_box_2(self):
        '''
        하단 트래킹창을 구성합니다.
        :return: None
        '''
        for i in range(3):  # right_box_bottom
            self.man_info_bottom[i].setColumnStretch(0, 1)
            self.man_info_bottom[i].setColumnStretch(1, 1)
            self.labels_trk_bottom[i].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.line_trk_bottom[i].setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.line_trk_bottom[i].setReadOnly(True)
            self.man_info_bottom[i].addWidget(self.labels_trk_bottom[i], i, 0)
            self.man_info_bottom[i].addWidget(self.line_trk_bottom[i], i, 1)
            self.right_box_bottom.addLayout(self.man_info_bottom[i])

        #self.frame_XZ.setGeometry(0, 0, 500, 500)
        self.frame_XZ.setLineWidth(1)
        self.frame_XZ.setFrameShape(QFrame.Box)
        self.frame_XZ.setFrameShadow(QFrame.Plain)
        line2_x = QGraphicsLineItem(-250, 250, 250, 250)
        line2_z = QGraphicsLineItem(0, -250, 0, 250)
        tx2 = QGraphicsTextItem('x축')
        tx2.setPos(275, 240)
        tz2 = QGraphicsTextItem('z축')
        tz2.setPos(-15, 270)
        base2 = QGraphicsRectItem(-50, 250, 100, 10)
        base2.setPen(QPen(Qt.gray, 5))
        servo2 = QGraphicsRectItem(-200, 230, 200, 20)
        servo2.setBrush(Qt.green)
        servo2.setPen(QPen(Qt.darkGreen, 3))
        self.scene_bottom.addItem(servo2)
        self.scene_bottom.addItem(base2)
        self.scene_bottom.addItem(line2_x)
        self.scene_bottom.addItem(tx2)
        self.scene_bottom.addItem(line2_z)
        self.scene_bottom.addItem(tz2)
        self.view_bottom = QGraphicsView(self.scene_bottom)
        self.coordXZ_layout.addWidget(self.view_bottom)
        self.frame_XZ.setLayout(self.coordXZ_layout)
        self.tracking_box_bottom_hbox.addWidget(self.frame_XZ)
        self.tracking_box_bottom_hbox.addLayout(self.right_box_bottom)
        self.tracking_box_bottom.setLayout(self.tracking_box_bottom_hbox)

    def set_btn_box(self):
        '''
        버튼박스를 구성합니다.
        :return: None
        '''
        self.obj_add_btn.setFixedHeight(150)
        self.obj_rm_btn.setFixedHeight(150)

        self.start_btn.setFixedHeight(150)
        self.stop_btn.setFixedHeight(150)
        self.play_box.addWidget(self.start_btn)
        self.play_box.addWidget(self.stop_btn)

        self.btn_box_vbox.addWidget(self.obj_add_btn)
        self.btn_box_vbox.addWidget(self.obj_rm_btn)
        self.btn_box_vbox.addLayout(self.play_box)

        self.btn_box.setLayout(self.btn_box_vbox)
    def init_UI(self):

        self.window_layout.setColumnStretch(0, 1000)
        self.window_layout.setColumnStretch(1, 500)
        ## 전체 레이아웃에 박스를 배치합니다.
        self.set_trk_box_1()
        self.set_trk_box_2()
        self.window_layout.addWidget(self.tracking_box_top, 0, 0)
        self.window_layout.addWidget(self.tracking_box_bottom, 1, 0)
        self.window_layout.addWidget(self.btn_box, 1, 1)
        self.window_layout.addWidget(self.group_box, 0, 1)

        ## 프로그램 창을 생성합니다.
        self.setLayout(self.window_layout)
        self.setWindowTitle('Dofbot Manipulation Simulator')
        self.setFixedSize(2000, 1500)
        self.set_window_center()
        self.setFont(QFont('SanSerif', 12))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = DofbotApp()
    sys.exit(app.exec_())