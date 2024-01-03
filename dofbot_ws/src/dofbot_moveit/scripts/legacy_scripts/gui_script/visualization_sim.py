from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import math
import numpy


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.last_obj_index = int(-1)
        self.servo1_box = QGroupBox('1번 서보모터(XY축)')
        self.servo2_box = QGroupBox('2번 서보모터(XZ축)')
        self.frame_XY = QFrame(self)
        self.frame_XZ = QFrame(self)

        self.obj_add_btn = QPushButton('객체 추가', self)
        self.obj_rm_btn = QPushButton('선택한 객체 삭제', self)
        self.start_btn = QPushButton('시작', self)
        self.stop_btn = QPushButton('정지', self)

        self.group_box = QGroupBox('생성된 객체 목록')
        self.obj_layers = {}
        self.cbs = []
        self.info_boxes = []
        self.label = []
        self.coord = []
        self.setObjLayers()
        vbox = QVBoxLayout()
        for i in range(3):
            vbox.addLayout(self.obj_layers[i], 1)
        self.group_box.setLayout(vbox)

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 10))
        self.setToolTip('DOFBOT 매니퓰레이터의 움직임을 시뮬레이션하는 프로그램입니다.')

        # 1번 서보모터 좌표계 및 베이스 생성
        self.frame_XY.setGeometry(0, 0, 500, 500)
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
        scene1 = QGraphicsScene()
        scene1.addItem(servo1)
        scene1.addItem(base1)
        scene1.addItem(line1_x)
        scene1.addItem(tx1)
        scene1.addItem(line1_y)
        scene1.addItem(ty1)
        view1 = QGraphicsView(scene1)
        coordXY_layout = QVBoxLayout(self.frame_XY)
        coordXY_layout.addWidget(view1)

        # 2번 서보모터 좌표계 및 베이스 생성
        self.frame_XZ.setGeometry(0, 0, 500, 500)
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
        scene2 = QGraphicsScene()
        scene2.addItem(servo2)
        scene2.addItem(base2)
        scene2.addItem(line2_x)
        scene2.addItem(tx2)
        scene2.addItem(line2_z)
        scene2.addItem(tz2)
        view2 = QGraphicsView(scene2)
        coordXY_layout = QVBoxLayout(self.frame_XZ)
        coordXY_layout.addWidget(view2)

        grid = QGridLayout()

        grid.setColumnStretch(0, 1000)
        grid.setColumnStretch(1, 500)

        grid.addWidget(self.createServogroupbox(self.frame_XY, self.servo1_box), 0, 0)
        grid.addWidget(self.createServogroupbox(self.frame_XZ, self.servo2_box), 1, 0)
        grid.addWidget(self.createBtngroupbox(), 1, 1)
        grid.addWidget(self.group_box, 0, 1)

        self.setLayout(grid)
        self.setWindowTitle('2축 매니퓰레이터 트래킹 시뮬레이션')
        self.setFixedSize(2000, 1500)
        self.setWindowCenter()
        self.setFont(QFont('SanSerif', 13))
        self.show()

    # 객체 목록 3개 준비
    def setObjLayers(self):
        for i in range(3):
            self.label.append(QLabel('3차원 좌표: '))
            self.label[i].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.coord.append(QLineEdit('(0, 0, 0)'))
            self.coord[i].setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.coord[i].setReadOnly(True)
            self.cbs.append(QCheckBox('Object ' + str(i + 1)))

            self.info_boxes.append(QHBoxLayout())
            self.info_boxes[i].addWidget(self.label[i])
            self.info_boxes[i].addWidget(self.coord[i])

            self.obj_layers.update({int(i) : QVBoxLayout()})
            self.obj_layers[i].addWidget(self.cbs[i])
            self.obj_layers[i].addLayout(self.info_boxes[i])

    def setWindowCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    # 조작 도구
    def createBtngroupbox(self):
        groupBox = QGroupBox('조작 도구')

        self.obj_add_btn.setToolTip('움직이는 임의의 객체를 추가로 생성합니다.</br>(최대 3개)')
        self.obj_add_btn.resize(self.obj_add_btn.sizeHint())
        self.obj_add_btn.setFixedHeight(150)

        self.obj_rm_btn.setToolTip('상단의 리스트에서 선택한 객체를 삭제합니다.')
        self.obj_rm_btn.resize(self.obj_rm_btn.sizeHint())
        self.obj_rm_btn.setFixedHeight(150)

        self.start_btn.setToolTip('시뮬레이션을 시작합니다.')
        self.start_btn.resize(self.start_btn.sizeHint())
        self.start_btn.setFixedHeight(150)

        self.stop_btn.setToolTip('시뮬레이션을 정지합니다.')
        self.stop_btn.resize(self.stop_btn.sizeHint())
        self.stop_btn.setFixedHeight(150)

        play_box = QHBoxLayout()
        play_box.addWidget(self.start_btn)
        play_box.addWidget(self.stop_btn)

        btn_box = QVBoxLayout()
        btn_box.addWidget(self.obj_add_btn)
        btn_box.addWidget(self.obj_rm_btn)
        btn_box.addLayout(play_box)
        groupBox.setLayout(btn_box)

        return groupBox

    # n번 서보모터(OO축)
    def createServogroupbox(self, frame: QFrame, box: QGroupBox):

        label1 = QLabel('목표 객체: ')
        label1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        text1 = QLineEdit('Object 1')
        text1.setReadOnly(True)
        text1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label2 = QLabel('객체 위치(2차원): ')
        label2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        text2 = QLineEdit('(0, 0)')
        text2.setReadOnly(True)
        text2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label3 = QLabel('회전 각도: ')
        label3.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        text3 = QLineEdit('0(DE) / 0(RA)')
        text3.setReadOnly(True)
        text3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        right_box = QGridLayout()
        right_box.addWidget(label1, 0, 0)
        right_box.addWidget(text1, 0, 1)
        right_box.addWidget(label2, 1, 0)
        right_box.addWidget(text2, 1, 1)
        right_box.addWidget(label3, 2, 0)
        right_box.addWidget(text3, 2, 1)
        right_box.setColumnStretch(0, 1)
        right_box.setColumnStretch(1, 1)

        hbox = QHBoxLayout()
        hbox.addWidget(frame, 1)
        hbox.addLayout(right_box, 1)
        box.setLayout(hbox)

        return box

    # (좌표계)객체 상자 생성, (객체 목록)객체 추가 메소드
    #def makeObjBBox(self, coord: list):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
