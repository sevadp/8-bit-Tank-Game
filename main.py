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
        pixmap = QPixmap('assets/background.jpg')
        label.setPixmap(pixmap)

        # Optional, resize window to image size
        self.resize(640, 640)
        self.timer = QBasicTimer()

        # Создание танка
        self.coords2 = QLabel(self)
        self.coords2.resize(48, 48)
        frist = "assets/64.png"
        pixmap = QPixmap(frist)
        self.coords2.setPixmap(pixmap)
        self.coords2.move(20, 430)

        # Второй танк
        # Создание танка
        self.coords = QLabel(self)
        self.coords.resize(48, 48)
        frist = "assets/64.png"
        pixmap = QPixmap(frist)
        self.coords.setPixmap(pixmap)
        self.coords.move(430, 430)

        # Направление движения танка 1
        self.move = "W"

        #Список активных пуль
        self.bullets = []
        self.life = []
        self.game_over = 0

        # Создаем игровой цикл
        self.timer.start(12, self)

        # Создание карты
        self.map = []
        self.bricks = []
        self.cant = []
        self.create_map()

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
                    frist = "assets/brick_comp.png"
                    pixmap = QPixmap(frist)
                    self.bricks.append(QLabel(self))
                    self.bricks[-1].resize(64, 64)
                    self.bricks[-1].setPixmap(pixmap)
                    self.bricks[-1].move(j * 64, i * 64)
                elif self.map[i][j] == "X":
                    frist = "assets/cant_lomatsa.png"
                    pixmap = QPixmap(frist)
                    self.cant.append(QLabel(self))
                    self.cant[-1].resize(64, 64)
                    self.cant[-1].setPixmap(pixmap)
                    self.cant[-1].move(j * 64, i * 64)



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
                frist = "assets/16x16bullet.png"
                pixmap = QPixmap(frist)
                self.bullets.append(QLabel(self))
                self.bullets[-1].resize(16, 16)
                self.bullets[-1].setPixmap(pixmap)
                self.bullets[-1].show()
                if self.move == "W":
                    self.life.append([self.move, 0])
                    self.bullets[-1].move(self.coords2.x() + 16,
                                          self.coords2.y() - 3)
                elif self.move == "A":
                    self.life.append([self.move, 0])
                    self.bullets[-1].move(self.coords2.x() - 3,
                                          self.coords2.y() + 16)

                elif self.move == "S":
                    self.life.append([self.move, 0])
                    self.bullets[-1].move(self.coords2.x() + 16,
                                          self.coords2.y() + 48)
                elif self.move == "D":
                    self.life.append([self.move, 0])
                    self.bullets[-1].move(self.coords2.x() + 48,
                                          self.coords2.y() + 16)

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

    def move_bullet(self, a, b):
        bullet = a
        c = (bullet.x(), bullet.y())
        life = b
        if life[0] == "W":
            bullet.move(bullet.x(), bullet.y() - 5)
            a = self.probitie(bullet.x(), bullet.y())
        elif life[0] == "A":
            bullet.move(bullet.x() - 5, bullet.y())
            a = self.probitie(bullet.x(), bullet.y())
        elif life[0] == "S":
            bullet.move(bullet.x(), bullet.y() + 5)
            a = self.probitie(bullet.x(), bullet.y())
        elif life[0] == "D":
            bullet.move(bullet.x() + 5, bullet.y())
            a = self.probitie(bullet.x(), bullet.y())
        if life[0] == "Up":
            bullet.move(bullet.x(), bullet.y() - 5)
            a = self.probitie(bullet.x(), bullet.y())
        elif life[0] == "Left":
            bullet.move(bullet.x() - 5, bullet.y())
            a = self.probitie(bullet.x(), bullet.y())
        elif life[0] == "Down":
            bullet.move(bullet.x(), bullet.y() + 5)
            a = self.probitie(bullet.x(), bullet.y())
        elif life[0] == "Right":
            bullet.move(bullet.x() + 5, bullet.y())
            a = self.probitie(bullet.x(), bullet.y())
        if a is not False:
            self.timer.stop()
            print("Конец игры!")
            self.game_over = 1

    def mousePressEvent(self, event):
            frist = "assets/16x16bullet.png"
            pixmap = QPixmap(frist)
            self.bullets.append(QLabel(self))
            self.bullets[-1].resize(16, 16)
            self.bullets[-1].setPixmap(pixmap)
            self.bullets[-1].show()
            if self.move2 == "Up":
                self.life.append([ self.move2, 0])
                self.bullets[-1].move(self.coords.x() + 16,
                                        self.coords.y() - 3)
            elif self.move2 == "Left":
                self.life.append([ self.move2, 0])
                self.bullets[-1].move(self.coords.x() - 3,
                                        self.coords.y() + 16)

            elif self.move2 == "Down":
                self.life.append([ self.move2, 0 ])
                self.bullets[-1].move(self.coords.x() + 16,
                                        self.coords.y() + 48)
            elif self.move2 == "Right":
                self.life.append([ self.move2, 0 ])
                self.bullets[-1].move(self.coords.x() + 48,
                                        self.coords.y() + 16)

    def check_move(self, x, y, c):
        if c == 1:
            tank_x, tank_y = self.coords2.x(), self.coords2.y()
        if c == 2:
            tank_x, tank_y = self.coords.x(), self.coords.y()
        if tank_x > x:
            return False
        if tank_y < y and tank_y + 48 > y and abs(tank_x - x) < 52:
            return 1
        elif tank_y < y + 64 and tank_y + 64 > y + 32 and abs(tank_x - x) < 52:
            return 2
        else:
            return False

    def check_move_2(self, x, y, c):
        if c == 1:
            tank_x, tank_y = self.coords2.x(), self.coords2.y()
        if c == 2:
            tank_x, tank_y = self.coords.x(), self.coords.y()
        if tank_x < x:
            return False
        if tank_y < y and tank_y + 48 > y and abs(tank_x - 16 - x) < 52:
            return 1
        elif tank_y < y + 64 and tank_y + 64 > y + 32 and abs(tank_x - 16 - x) < 52:
            return 2
        else:
            return False

    def check_move_3(self, x, y, c):
        if c == 1:
            tank_x, tank_y = self.coords2.x(), self.coords2.y()
        if c == 2:
            tank_x, tank_y = self.coords.x(), self.coords.y()
        if tank_y < y:
            return False
        if tank_x < x and tank_x + 48 > x and abs(tank_y - 16 - y) < 51:
            return 1
        elif tank_x < x + 64 and tank_x + 64 > x + 32 and abs(tank_y - 16 - y) < 51:
            return 2
        elif tank_x < x and tank_x + 48 > x and abs(tank_y - y) < 65:
            return 3
        else:
            return False

    def check_move_4(self, x, y, c):
        if c == 1:
            tank_x, tank_y = self.coords2.x(), self.coords2.y()
        if c == 2:
            tank_x, tank_y = self.coords.x(), self.coords.y()
        if tank_y > y:
            return False
        if tank_x < x and tank_x + 48 > x and abs(tank_y - y) < 51:
            return 1
        elif tank_x < x + 64 and tank_x + 64 > x + 32 and abs(tank_y - y) < 51:
            return 2
        elif tank_x < x and tank_x + 48 > x and abs(tank_y - y) < 50:
            return 3
        else:
            return False

    def check_brick(self, x, y):
        new_brick = []
        for i in self.bricks:
            if i.x() <= x <= i.x() + 64 and i.y() <= y <= i.y() + 64:
                i.move(-100, - 100)
                return True

        for i in self.cant:
            if i.x() <= x <= i.x() + 64 and i.y() <= y <= i.y() + 64:
                return True

    def timerEvent(self, e):
        # Движение танка
        if self.put == 1:
            if self.move == "D":
                frist = "assets/64_r.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.x()
                if a < 590:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move(i.x() + 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move(i.x() + 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(a + 1, self.coords2.y())
                elif 590 == a or a == 591:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move(i.x() + 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move(i.x() + 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(590, self.coords2.y())
            elif self.move == "A":
                frist = "assets/64_l.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.x()
                if a > 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_2(i.x() - 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_2(i.x() - 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(a - 1, self.coords2.y())
                elif 1 == a or a == 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_2(i.x() - 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_2(i.x() - 1, i.y(), 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(0, self.coords2.y())
            elif self.move == "W":
                frist = "assets/64.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.y()
                if a > 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_3(i.x(), i.y() - 1, 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_3(i.x(), i.y() - 1, 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(self.coords2.x(), a - 1)
                elif 1 == a or a == 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_3(i.x(), i.y() - 1, 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_3(i.x(), i.y() - 1, 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(self.coords2.x(), a - 1)
            elif self.move == "S":
                frist = "assets/64_d.png"
                pixmap = QPixmap(frist)
                self.coords2.setPixmap(pixmap)
                a = self.coords2.y()
                if a < 590:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_4(i.x(), i.y() + 1, 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_4(i.x(), i.y() + 1, 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(self.coords2.x(), a + 1)
                elif 590 == a or a == 591:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_4(i.x(), i.y() + 1, 1)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_4(i.x(), i.y() + 1, 1)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords2.move(self.coords2.x(), a + 1)

        # Второй танк. движение
        if self.put2 == 1:
            if self.move2 == "Right":
                frist = "assets/64_r.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.x()
                if a < 590:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move(i.x() + 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move(i.x() + 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(a + 1, self.coords.y())
                elif 590 == a or a == 591:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move(i.x() + 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move(i.x() + 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(590, self.coords.y())
            elif self.move2 == "Left":
                frist = "assets/64_l.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.x()
                if a > 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_2(i.x() - 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_2(i.x() - 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(a - 1, self.coords.y())
                elif 1 == a or a == 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_2(i.x() - 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_2(i.x() - 1, i.y(), 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(0, self.coords.y())
            elif self.move2 == "Up":
                frist = "assets/64.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.y()
                if a > 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_3(i.x(), i.y() - 1, 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_3(i.x(), i.y() - 1, 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(self.coords.x(), a - 1)
                elif 1 == a or a == 2:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_3(i.x(), i.y() - 1, 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_3(i.x(), i.y() - 1, 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(self.coords.x(), a - 1)
            elif self.move2 == "Down":
                frist = "assets/64_d.png"
                pixmap = QPixmap(frist)
                self.coords.setPixmap(pixmap)
                a = self.coords.y()
                if a < 590:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_4(i.x(), i.y() + 1, 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_4(i.x(), i.y() + 1, 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(self.coords.x(), a + 1)
                elif 590 == a or a == 591:
                    can = 1
                    for i in self.bricks:
                        b = self.check_move_4(i.x(), i.y() + 1, 2)
                        if b is not False:
                            can = 0
                    for i in self.cant:
                        b = self.check_move_4(i.x(), i.y() + 1, 2)
                        if b is not False:
                            can = 0
                    if can == 1:
                        self.coords.move(self.coords.x(), a + 1)

        # Обработка пуль
        new_bullet = []
        new_life = []
        if self.bullets != []:
            for i in range(len(self.bullets)):
                self.move_bullet(self.bullets[i], self.life[i])
                self.life[i][1] += 1
                # Удаление пули
                if self.life[i][1] < 150:
                    if self.bullets[i].x() < - 16 or self.bullets[i].x() > 640 or self.bullets[i].y() > 660 or self.bullets[i].y() < -16:
                        pass
                    elif self.check_brick(self.bullets[i].x(), self.bullets[i].y()):
                        self.bullets[i].move(-100, - 100)
                    else:
                        new_bullet.append(self.bullets[i])
                        new_life.append(self.life[i])


            self.bullets = new_bullet
            self.life = new_life



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
