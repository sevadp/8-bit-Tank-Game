import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 400, 800, 800)
        self.setWindowTitle('8 BIT TANKS')

        label = QLabel(self)
        pixmap = QPixmap('background.jpg')
        label.setPixmap(pixmap)

        # Optional, resize window to image size
        self.resize(640, 640)

        # Кирпичики
        frist = "brick_comp.png"
        pixmap = QPixmap(frist)
        self.brick1 = QLabel(self)
        self.brick1.resize(32, 32)
        self.brick1.setPixmap(pixmap)
        self.brick1.move(-400, 0)

        self.brick2 = QLabel(self)
        self.brick2.resize(32, 32)
        self.brick2.setPixmap(pixmap)
        self.brick2.move(-400, 150)

        self.brick3 = QLabel(self)
        self.brick3.resize(32, 32)
        self.brick3.setPixmap(pixmap)
        self.brick3.move(-400, 300)

        self.brick4 = QLabel(self)
        self.brick4.resize(32, 32)
        self.brick4.setPixmap(pixmap)
        self.brick4.move(-400, 450)

        self.brick5 = QLabel(self)
        self.brick5.resize(32, 32)
        self.brick5.setPixmap(pixmap)
        self.brick5.move(-400, 600)

        self.timer = QBasicTimer()
        # Создание танка
        self.coords2 = QLabel(self)
        self.coords2.resize(48, 48)
        frist = "64.png"
        pixmap = QPixmap(frist)
        self.coords2.setPixmap(pixmap)
        self.coords2.move(20, 430)

        # Второй танк
        # Создание танка
        self.coords = QLabel(self)
        self.coords.resize(48, 48)
        frist = "64.png"
        pixmap = QPixmap(frist)
        self.coords.setPixmap(pixmap)
        self.coords.move(430, 430)

        # Максимум регистрируем 5 пуль
        frist = "16x16bullet.png"
        pixmap = QPixmap(frist)
        self.bullet1 = QLabel(self)
        self.bullet1.resize(16, 16)
        self.bullet1.setPixmap(pixmap)
        self.bullet1.move(-300, 300)

        self.bullet2 = QLabel(self)
        self.bullet2.resize(16, 16)
        self.bullet2.setPixmap(pixmap)
        self.bullet2.move(-300, 300)

        self.bullet3 = QLabel(self)
        self.bullet3.resize(16, 16)
        self.bullet3.setPixmap(pixmap)
        self.bullet3.move(-300, 300)

        self.bullet4 = QLabel(self)
        self.bullet4.resize(16, 16)
        self.bullet4.setPixmap(pixmap)
        self.bullet4.move(-300, 300)

        self.bullet5 = QLabel(self)
        self.bullet5.resize(16, 16)
        self.bullet5.setPixmap(pixmap)
        self.bullet5.move(-300, 300)

        # Направление движения танка 1
        self.move = "W"

        #Список активных пуль
        self.bullets = []

        # Создаем игровой цикл
        self.timer.start(33, self)

        # Создание карты
        self.map = []
        self.bricks = []
        self.create_map()


        # Пули, используются или нет
        self.used = [0, 0, 0, 0, 0]

        # Активное нажатие танка 1
        self.put = 0

        # Направление движения танка 2
        self.move2 = "Up"

        # Активное нажатие танка 2
        self.put2 = 0


        self.show()

    def create_map(self):
        with open("map.txt") as D:
            a = D.read()
            a = a.split("\n")
            for i in a:
                self.map.append(i)

        for i in range(10):
            for j in range(10):
                if self.map[i][j] == " ":
                    pass
                elif self.map[i][j] == "T":
                    frist = "brick_comp.png"
                    pixmap = QPixmap(frist)
                    self.bricks.append(QLabel(self))
                    self.bricks[-1].resize(64, 64)
                    self.bricks[-1].setPixmap(pixmap)
                    self.bricks[-1].move(j * 64, i * 64)
                elif self.map[i][j] == "X":
                    frist = "cant_lomatsa.png"
                    pixmap = QPixmap(frist)
                    self.bricks.append(QLabel(self))
                    self.bricks[-1].resize(64, 64)
                    self.bricks[-1].setPixmap(pixmap)
                    self.bricks[-1].move(j * 64, i * 64)



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.move = "D"
            self.put = 1
        elif event.key() == Qt.Key_A:
            self.move = "A"
            self.put = 1
        elif event.key() == Qt.Key_W:
            self.move = "W"
            self.put = 1
        elif event.key() == Qt.Key_S:
            self.move = "S"
            self.put = 1

        if event.key() == Qt.Key_Right:
            self.move2 = "Right"
            self.put2 = 1
        elif event.key() == Qt.Key_Left:
            self.move2 = "Left"
            self.put2 = 1
        elif event.key() == Qt.Key_Up:
            self.move2 = "Up"
            self.put2 = 1
        elif event.key() == Qt.Key_Down:
            self.move2 = "Down"
            self.put2 = 1

        if event.key() == Qt.Key_Space:
            if len(self.bullets) < 5:
                # Регистрируем пулю
                if self.move == "W":
                    self.bullets.append([self.coords2.x() + 16, self.coords2.y() - 3, self.move, 0, 0])
                elif self.move == "A":
                    self.bullets.append([self.coords2.x() - 3, self.coords2.y() + 16, self.move, 0, 0])
                elif self.move == "S":
                    self.bullets.append([self.coords2.x() + 16, self.coords2.y() + 48, self.move, 0, 0])
                elif self.move == "D":
                    self.bullets.append([self.coords2.x() + 48, self.coords2.y() + 16, self.move, 0, 0])

                self.register_bullet()

    def keyReleaseEvent(self, eventQKeyEvent):
        key = eventQKeyEvent.key()
        if key == Qt.Key_D and not eventQKeyEvent.isAutoRepeat() and self.move == "D":
            self.put = 0
        if key == Qt.Key_A and not eventQKeyEvent.isAutoRepeat() and self.move == "A":
            self.put = 0
        if key == Qt.Key_S and not eventQKeyEvent.isAutoRepeat() and self.move == "S":
            self.put = 0
        if key == Qt.Key_W and not eventQKeyEvent.isAutoRepeat() and self.move == "W":
            self.put = 0

        if key == Qt.Key_Right and not eventQKeyEvent.isAutoRepeat() and self.move2 == "Right":
            self.put2 = 0
        if key == Qt.Key_Left and not eventQKeyEvent.isAutoRepeat() and self.move2 == "Left":
            self.put2 = 0
        if key == Qt.Key_Down and not eventQKeyEvent.isAutoRepeat() and self.move2 == "Down":
            self.put2 = 0
        if key == Qt.Key_Up and not eventQKeyEvent.isAutoRepeat() and self.move2 == "Up":
            self.put2 = 0


    def find_no_use(self):
        for i in range(len(self.used)):
            if self.used[i] == 0:
                return i

    def register_bullet(self):
        no_use = self.find_no_use()
        self.used[no_use] = 1
        frist = "16x16bullet.png"
        pixmap = QPixmap(frist)
        self.bullets[len(self.bullets) - 1][4] = no_use

        if no_use == 0:
            self.bullet1.setPixmap(pixmap)
            self.bullet1.move(self.bullets[len(self.bullets) - 1][0], self.bullets[len(self.bullets) - 1][1])
        elif no_use == 1:
            self.bullet2.setPixmap(pixmap)
            self.bullet2.move(self.bullets[len(self.bullets) - 1][0], self.bullets[len(self.bullets) - 1][1])
        elif no_use == 2:
            self.bullet3.setPixmap(pixmap)
            self.bullet3.move(self.bullets[len(self.bullets) - 1][0], self.bullets[len(self.bullets) - 1][1])
        elif no_use == 3:
            self.bullet4.setPixmap(pixmap)
            self.bullet4.move(self.bullets[len(self.bullets) - 1][0], self.bullets[len(self.bullets) - 1][1])
        elif no_use == 4:
            self.bullet5.setPixmap(pixmap)
            self.bullet5.move(self.bullets[len(self.bullets) - 1][0], self.bullets[len(self.bullets) - 1][1])

    def probitie(self, x, y):
        tank_x, tank_y = self.coords2.x(), self.coords2.y()
        tank2_x, tank2_y = self.coords.x(), self.coords.y()

        # Проверка на попадание пули
        if tank_x <= x <= tank_x + 48 and tank_y <= y <= tank_y + 48:
            return 1
        elif tank2_x <= x <= tank2_x + 48 and tank2_y <= y <= tank2_y + 48:
            return 2
        else:
            return False

    def move_bullet(self, a):
        bullet = a
        if bullet[2] == "W":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x(), self.bullet1.y() - 10)
                a = self.probitie(self.bullet1.x(), self.bullet1.y())
            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x(), self.bullet2.y() - 10)
                a = self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x(), self.bullet3.y() - 10)
                a = self.probitie(self.bullet3.x(), self.bullet3.y())
            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x(), self.bullet4.y() - 10)
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x(), self.bullet5.y() - 10)
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        elif bullet[2] == "A":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x() - 10, self.bullet1.y())
                a = self.probitie(self.bullet1.x(), self.bullet1.y())
            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x() - 10, self.bullet2.y())
                a = self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x() - 10, self.bullet3.y())
                a = self.probitie(self.bullet3.x(), self.bullet3.y())
            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x() - 10, self.bullet4.y())
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x() - 10, self.bullet5.y())
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        elif bullet[2] == "S":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x(), self.bullet1.y() + 10)
                a = self.probitie(self.bullet1.x(), self.bullet1.y())
            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x(), self.bullet2.y() + 10)
                a =self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x(), self.bullet3.y() + 10)
                a = self.probitie(self.bullet3.x(), self.bullet3.y())
            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x(), self.bullet4.y() + 10)
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x(), self.bullet5.y() + 10)
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        elif bullet[2] == "D":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x() + 10, self.bullet1.y())
                a = self.probitie(self.bullet1.x(), self.bullet1.y())
            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x() + 10, self.bullet2.y())
                a = self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x() + 10, self.bullet3.y())
                a = self.probitie(self.bullet3.x(), self.bullet3.y())
            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x() + 10, self.bullet4.y())
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x() + 10, self.bullet5.y())
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        if bullet[2] == "Up":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x(), self.bullet1.y() - 10)
                a = self.probitie(self.bullet1.x(), self.bullet1.y())

            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x(), self.bullet2.y() - 10)
                a = self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x(), self.bullet3.y() - 10)
                a = self.probitie(self.bullet3.x(), self.bullet3.y())

            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x(), self.bullet4.y() - 10)
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x(), self.bullet5.y() - 10)
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        elif bullet[2] == "Left":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x() - 10, self.bullet1.y())
                a = self.probitie(self.bullet1.x(), self.bullet1.y())
            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x() - 10, self.bullet2.y())
                a = self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x() - 10, self.bullet3.y())
                a = self.probitie(self.bullet3.x(), self.bullet3.y())
            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x() - 10, self.bullet4.y())
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x() - 10, self.bullet5.y())
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        elif bullet[2] == "Down":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x(), self.bullet1.y() + 10)
                a = self.probitie(self.bullet1.x(), self.bullet1.y())
            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x(), self.bullet2.y() + 10)
                a = self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x(), self.bullet3.y() + 10)
                a = self.probitie(self.bullet3.x(), self.bullet3.y())
            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x(), self.bullet4.y() + 10)
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x(), self.bullet5.y() + 10)
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        elif bullet[2] == "Right":
            if bullet[4] == 0:
                self.bullet1.move(self.bullet1.x() + 10, self.bullet1.y())
                a = self.probitie(self.bullet1.x(), self.bullet1.y())
            elif bullet[4] == 1:
                self.bullet2.move(self.bullet2.x() + 10, self.bullet2.y())
                a = self.probitie(self.bullet2.x(), self.bullet2.y())
            elif bullet[4] == 2:
                self.bullet3.move(self.bullet3.x() + 10, self.bullet3.y())
                a = self.probitie(self.bullet3.x(), self.bullet3.y())
            elif bullet[4] == 3:
                self.bullet4.move(self.bullet4.x() + 10, self.bullet4.y())
                a = self.probitie(self.bullet4.x(), self.bullet4.y())
            elif bullet[4] == 4:
                self.bullet5.move(self.bullet5.x() + 10, self.bullet5.y())
                a = self.probitie(self.bullet5.x(), self.bullet5.y())
        if a is not False:
            self.timer.stop()
            print("Конец игры!")

    def mousePressEvent(self, event):
        if len(self.bullets) < 5:
            # Регистрируем пулю
            if self.move2 == "Up":
                self.bullets.append([self.coords.x() + 16, self.coords.y() - 3, self.move2, 0, 0])
            elif self.move2 == "Left":
                self.bullets.append([self.coords.x() - 3, self.coords.y() + 16, self.move2, 0, 0])
            elif self.move2 == "Down":
                self.bullets.append([self.coords.x() + 16, self.coords.y() + 48, self.move2, 0, 0])
            elif self.move2 == "Right":
                self.bullets.append([self.coords.x() + 48, self.coords.y() + 16, self.move2, 0, 0])

            self.register_bullet()

    def timerEvent(self, e):
        # Движение танка
        if self.put == 1:
            if self.move == "D":
                frist = "64_r.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.x()
                if a < 590:
                    self.coords2.move(a + 3, self.coords2.y())
                elif 590 == a or a == 591:
                    self.coords2.move(590, self.coords2.y())
            elif self.move == "A":
                frist = "64_l.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.x()
                if a > 2:
                    self.coords2.move(a - 3, self.coords2.y())
                elif 1 == a or a == 2:
                    self.coords2.move(0, self.coords2.y())
            elif self.move == "W":
                frist = "64.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.y()
                if a > 2:
                    self.coords2.move(self.coords2.x(), a - 3)
                elif 1 == a or a == 2:
                    self.coords2.move(self.coords2.x(), 0)
            elif self.move == "S":
                frist = "64_d.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.y()
                if a < 590:
                    self.coords2.move(self.coords2.x(), a + 3)
                elif 590 == a or a == 591:
                    self.coords2.move(self.coords2.x(), 592)

        # Второй танк. движение
        if self.put2 == 1:
            if self.move2 == "Right":
                frist = "64_r.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.x()
                if a < 590:
                    self.coords.move(a + 3, self.coords.y())
                elif 590 == a or a == 590:
                    self.coords.move(592, self.coords.y())
            elif self.move2 == "Left":
                frist = "64_l.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.x()
                if a > 2:
                    self.coords.move(a - 3, self.coords.y())
                elif 1 == a or a == 2:
                    self.coords.move(0, self.coords.y())
            elif self.move2 == "Up":
                frist = "64.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.y()
                if a > 2:
                    self.coords.move(self.coords.x(), a - 3)
                elif 1 == a or a == 2:
                    self.coords.move(self.coords2.x(), 0)
            elif self.move2 == "Down":
                frist = "64_d.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.y()
                if a < 590:
                    self.coords.move(self.coords.x(), a + 3)
                elif 590 == a or a == 591:
                    self.coords.move(self.coords.x(), 592)

        # Обработка пуль
        new_bullet = []
        if self.bullets != []:
            for i in range(len(self.bullets)):
                self.move_bullet(self.bullets[i])
                self.bullets[i][3] += 1
                # Удаление пули
                if self.bullets[i][3] < 100:
                    if self.bullets[i][4] == 0:
                        if self.bullet1.x() < -16 or self.bullet1.x() > 640 or self.bullet1.y() > 660 or\
                                self.bullet1.y() < -16:
                            self.used[self.bullets[i][4]] = 0
                        else:
                            new_bullet.append(self.bullets[i])
                    if self.bullets[i][4] == 1:
                        if self.bullet2.x() < -16 or self.bullet2.x() > 640 or self.bullet2.y() > 660 or\
                                self.bullet2.y() < -16:
                            self.used[self.bullets[i][4]] = 0
                        else:
                            new_bullet.append(self.bullets[i])
                    if self.bullets[i][4] == 2:
                        if self.bullet3.x() < -16 or self.bullet3.x() > 640 or self.bullet3.y() > 660 or\
                                self.bullet3.y() < -16:
                            self.used[self.bullets[i][4]] = 0
                        else:
                            new_bullet.append(self.bullets[i])
                    if self.bullets[i][4] == 3:
                        if self.bullet4.x() < -16 or self.bullet4.x() > 640 or self.bullet4.y() > 660 or\
                                self.bullet4.y() < -16:
                            self.used[self.bullets[i][4]] = 0
                        else:
                            new_bullet.append(self.bullets[i])
                    if self.bullets[i][4] == 4:
                        if self.bullet5.x() < -16 or self.bullet5.x() > 640 or self.bullet5.y() > 660 or\
                                self.bullet5.y() < -16:
                            self.used[self.bullets[i][4]] = 0
                        else:
                            new_bullet.append(self.bullets[i])
                else:
                    self.used[self.bullets[i][4]] = 0


            self.bullets = new_bullet




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())