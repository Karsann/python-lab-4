import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QLineEdit, QComboBox, QCheckBox, QSlider, QProgressBar,
    QSpinBox, QVBoxLayout, QHBoxLayout, QTabWidget,
    QMessageBox, QInputDialog, QDialog, QDialogButtonBox, QFormLayout,
    QMenuBar, QMenu, QStatusBar
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction


class SenderBox(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введіть текст...")
        self.send_button = QPushButton("Надіслати сигнал")
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_data)

    def send_data(self):
        self.my_signal.emit(self.input_field.text())


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Власний діалог")
        layout = QFormLayout()
        self.name_field = QLineEdit()
        layout.addRow("Ваше ім'я:", self.name_field)

        dialog_buttons = QDialogButtonBox()
        dialog_buttons.addButton(QDialogButtonBox.StandardButton.Ok)
        dialog_buttons.addButton(QDialogButtonBox.StandardButton.Cancel)

        dialog_buttons.accepted.connect(self.accept)
        dialog_buttons.rejected.connect(self.reject)
        layout.addRow(dialog_buttons)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторна 4")
        self.resize(500, 420)

        self.t2_name = QLineEdit()
        self.t2_chk = QCheckBox("Погоджуюсь з умовами")
        self.t2_lbl = QLabel("Значення повзунка: 0")
        self.t2_slider = QSlider(Qt.Orientation.Horizontal)
        self.t2_btn = QPushButton("Перевірити")
        self.t2_reset = QPushButton("Скинути")
        self.t2_res = QLabel("Результат...")

        self.sender_box = SenderBox()
        self.t4_lbl = QLabel("Тут з'явиться текст із сигналу...")
        self.block_chk = QCheckBox("Блокувати сигнал")

        self.t5_lbl = QLabel("Результат діалогу...")

        self.setStyleSheet("""
            QWidget { font-size: 13px; }
            QPushButton { background-color: #3498db; color: white; padding: 5px; border-radius: 3px; }
            QPushButton:hover { background-color: #2980b9; }
        """)

        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        file_menu = QMenu("Файл", self)
        help_menu = QMenu("Довідка", self)
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(help_menu)

        exit_act = QAction("Вихід", self)
        exit_act.setShortcut("Ctrl+Q")
        exit_act.triggered.connect(self.close)
        file_menu.addAction(exit_act)

        about_act = QAction("Про програму", self)
        about_act.triggered.connect(self.show_about)
        help_menu.addAction(about_act)

        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)
        status_bar.showMessage("Готово")

        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        tabs.addTab(self.build_tab1(), "Завдання 1")
        tabs.addTab(self.build_tab2(), "Завдання 2")
        tabs.addTab(self.build_tab4(), "Завдання 4")
        tabs.addTab(self.build_tab5(), "Завдання 5")

    def show_about(self):
        QMessageBox.about(self, "Інфо", "Проста програма на PyQt6")

    def build_tab1(self):
        tab = QWidget(self)
        layout = QVBoxLayout()

        lbl = QLabel("Текстова мітка")
        lbl.setToolTip("Це підказка")
        inp = QLineEdit()
        inp.setPlaceholderText("Введіть щось...")
        combo = QComboBox()
        combo.addItems(["Київ", "Львів", "Одеса"])
        spin = QSpinBox()
        spin.setValue(20)
        chk = QCheckBox("Активний пункт")
        chk.setChecked(True)
        slider = QSlider(Qt.Orientation.Horizontal)
        progress = QProgressBar()
        progress.setValue(50)

        h_box = QHBoxLayout()
        h_box.addWidget(slider)
        h_box.addWidget(progress)

        layout.addWidget(lbl)
        layout.addWidget(inp)
        layout.addWidget(combo)
        layout.addWidget(spin)
        layout.addWidget(chk)
        layout.addLayout(h_box)

        tab.setLayout(layout)
        return tab

    def build_tab2(self):
        tab = QWidget(self)
        layout = QVBoxLayout()

        self.t2_name.setPlaceholderText("Введіть ім'я...")
        self.t2_btn.setEnabled(False)

        layout.addWidget(self.t2_name)
        layout.addWidget(self.t2_chk)
        layout.addWidget(self.t2_lbl)
        layout.addWidget(self.t2_slider)
        layout.addWidget(self.t2_btn)
        layout.addWidget(self.t2_reset)
        layout.addWidget(self.t2_res)

        self.t2_slider.valueChanged.connect(self.on_slider_change)
        self.t2_chk.toggled.connect(self.t2_btn.setEnabled)
        self.t2_btn.clicked.connect(self.check_t2)
        self.t2_reset.clicked.connect(self.reset_t2)

        tab.setLayout(layout)
        return tab

    def on_slider_change(self, value):
        self.t2_lbl.setText(f"Значення повзунка: {value}")

    def check_t2(self):
        txt = self.t2_name.text().strip()
        if not txt:
            self.t2_res.setText("Помилка: ім'я порожнє!")
        else:
            self.t2_res.setText(f"Успіх! Вітаємо, {txt}")

    def reset_t2(self):
        self.t2_name.clear()
        self.t2_chk.setChecked(False)
        self.t2_slider.setValue(0)
        self.t2_res.setText("Форму скинуто")

    def build_tab4(self):
        tab = QWidget(self)
        layout = QVBoxLayout()

        layout.addWidget(self.sender_box)
        layout.addWidget(self.t4_lbl)
        layout.addWidget(self.block_chk)

        self.sender_box.my_signal.connect(self.t4_lbl.setText)
        self.block_chk.toggled.connect(self.sender_box.blockSignals)

        tab.setLayout(layout)
        return tab

    def build_tab5(self):
        tab = QWidget(self)
        layout = QVBoxLayout()

        b1 = QPushButton("Діалог QMessageBox")
        b2 = QPushButton("Діалог QInputDialog")
        b3 = QPushButton("Власний діалог QDialog")

        b1.clicked.connect(self.open_msg)
        b2.clicked.connect(self.open_input)
        b3.clicked.connect(self.open_custom)

        layout.addWidget(b1)
        layout.addWidget(b2)
        layout.addWidget(b3)
        layout.addWidget(self.t5_lbl)

        tab.setLayout(layout)
        return tab

    def open_msg(self):
        ans = QMessageBox.question(self, "Питання", "Видалити дані?")
        if ans == QMessageBox.StandardButton.Yes:
            self.t5_lbl.setText("Натиснуто: Так")
        else:
            self.t5_lbl.setText("Натиснуто: Ні")

    def open_input(self):
        txt, ok = QInputDialog.getText(self, "Ввід", "Введіть ваше місто:")
        if ok and txt:
            self.t5_lbl.setText(f"Місто: {txt}")

    def open_custom(self):
        d = MyDialog()
        if d.exec() == QDialog.DialogCode.Accepted:
            self.t5_lbl.setText(f"Введено у власному діалозі: {d.name_field.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
