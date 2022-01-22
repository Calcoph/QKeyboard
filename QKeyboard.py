import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QApplication
from PyQt5.QtCore import Qt, QSize

class QKeyboard(QWidget):
    def __init__(self, variant) -> None:
        super().__init__()
        self.setStyleSheet("QLabel { background: #0070a0 }")

        parts, vertical = self.parse_dotkeyb(variant)
        self.layout = QHBoxLayout(self)
        self.layout.addLayout(self.init_core(False, vertical, parts[0][1:]), 15)
        self.layout.addLayout(self.init_navigation(parts[1]), 3)
        self.layout.addLayout(self.init_numpad(parts[2]), 4)

    def init_core(self, ignore_fkeys, tall_return, labels):
        return_label = labels[-1]
        labels = labels[:-1]
        layout = QVBoxLayout()

        if not ignore_fkeys:
            flabels = [
                ["esc"],
                ["f1", "f2", "f3", "f4"],
                ["f5", "f6", "f7", "f8"],
                ["f9", "f10", "f11", "f12"]
            ]
            row = QHBoxLayout()
            for i, section in enumerate(flabels):
                for label in section:
                    l_widget = QLabel(label)
                    l_widget.setAlignment(Qt.AlignCenter)
                    row.addWidget(l_widget, 1)
                if i != 3:
                    row.addStretch(1)
            layout.addLayout(row, 2)
            layout.addStretch(1)

        """labels = [
            ["º", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "'", "¡", ("<-", 8)],
            [("tab", 6), "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "`", "+"],
            [("bloq\nmayús", 7), "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "´", "Ç"],
            [("mayús", 5), "<", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "-", ("mayús", 11)],
            [("ctrl", 6), "win", ("alt", 5), ("space", 26), ("alt gr", 5), "FN", "menu", ("ctrl", 6)]
        ]""" # TODO: delete
        row = QHBoxLayout()
        self.init_row(row, labels[0])
        layout.addLayout(row, 2)


        row1and2 = QHBoxLayout()
        
        r12 = QVBoxLayout()
        
        row = QHBoxLayout()
        self.init_row(row, labels[1])
        r12.addLayout(row)
        row = QHBoxLayout()
        self.init_row(row, labels[2])
        r12.addLayout(row)

        row1and2.addLayout(r12, 55)
        l_widget = QLabel("Enter")
        l_widget.setAlignment(Qt.AlignCenter)
        row1and2.addWidget(l_widget, 5)
        layout.addLayout(row1and2, 4)

        row = QHBoxLayout()
        self.init_row(row, labels[3])
        layout.addLayout(row, 2)
        row = QHBoxLayout()
        self.init_row(row, labels[4])
        layout.addLayout(row, 2)

        return layout

    def init_navigation(self, labels):
        print(labels)
        layout = QGridLayout()
        """labels = [
            ["print", "block", "pause"],
            [],
            ["insert", "inicio", "re\npág"],
            ["supr", "fin", "av\npág"],
            [],
            [None, "up"],
            ["left", "down", "right"],
        ]""" # TODO: delete

        self.init_grid(layout, labels)
        for i in range(7):
            layout.setRowStretch(i, 2)
        layout.setRowStretch(1, 1)

        return layout

    def init_numpad(self, labels):
        layout = QGridLayout()
        """labels = [
            [],
            [],
            ["bloq\nnum", "/", "-", "*"],
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, None, ","],
        ]""" # TODO: delete

        self.init_grid(layout, labels)

        l_widget = QLabel("+")
        l_widget.setAlignment(Qt.AlignCenter)
        layout.addWidget(l_widget, 3, 3, 2, 1)
        l_widget = QLabel("intro")
        l_widget.setAlignment(Qt.AlignCenter)
        layout.addWidget(l_widget, 5, 3, 2, 1)
        l_widget = QLabel("0")
        l_widget.setAlignment(Qt.AlignCenter)
        layout.addWidget(l_widget, 6, 0, 1, 2)
        
        for i in range(7):
            layout.setRowStretch(i, 2)
        layout.setRowStretch(0, 1)

        return layout

    def init_grid(self, layout, labels):
        for row, label_row in enumerate(labels):
            for col, label in enumerate(label_row):
                if label != None:
                    l_widget = QLabel(label)
                    l_widget.setAlignment(Qt.AlignCenter)
                    layout.addWidget(l_widget, row, col)

    def init_row(self, layout, labels):
        for item in labels:
            if isinstance(item, tuple):
                label, stretch_factor = item
            else:
                label = item
                stretch_factor = 4
            l_widget = QLabel(label)
            l_widget.setAlignment(Qt.AlignCenter)
            layout.addWidget(l_widget, stretch_factor)

    def parse_dotkeyb(self, filename):
        defaults = [
            [
                ["ESC", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"],
                ["º", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "'", "¡"],
                ["tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "`", "+", "Enter"],
                ["bloq\nmayús", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "´", "Ç", "Enter"],
                ["mayús", "<", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "-", "mayús"],
                ["ctrl", "win", "alt", "space", "alt gr", "FN", "menu", "ctrl"]
            ],
            [
                ["print", "block", "pause"],
                ["insert", "inicio", "re\npág"],
                ["supr", "fin", "av\npág"]
            ],
            [
                ["up"],
                ["left", "down", "right"]
            ],
            [
                ["bloq\nnum", "/", "-", "*"],
                ["7", "8", "9"],
                ["4", "5", "6"],
                ["1", "2", "3"],
                [","]
            ]
        ]

        if not filename.endswith(".keyb"):
            filename = filename + ".keyb"
        file = []
        with open("layouts/" + filename, "r", encoding="utf-8") as f:
            file = f.readlines()
        
        sizes = {}
        parts = ([], [], [], []) # core, navigation (upside), arrows, numpad
        current = 0
        for line in file:
            if line.strip() == "-":
                if current <= 3: # labels
                    parts[current].append([])
                    keys = line.split("##")
                    for key in keys:
                        new_key = key.strip().replace("\\n", "\n")
                        parts[current][-1].append(new_key)
                else: # key sizes
                    try:
                        key, size = line.split(":")
                    except ValueError:
                        print("That file is not compatible")
                    new_key = key.strip().replace("\\n", "\n")
                    sizes[new_key] = int(float(size.strip())*4)
            else:
                current+= 1

        for index, i in enumerate(parts):
            if len(i) == 0:
                parts[index].extend(defaults[index])
        
        for row in parts[0]:
            for index, key in enumerate(row):
                if key in sizes:
                    row[index] = (key, sizes[key])

        vertical = False
        try:
            return_label = parts[0][3][-1]
            if parts[0][3][-1] == parts[0][3][-2]: # horizontal return key
                parts[0][3].pop()
                parts[0][3].pop()
            elif parts[0][2][-1] == parts[0][3][-1]: # vertical return key
                parts[0][2].pop()
                parts[0][3].pop()
                vertical = True
            parts[0].append(return_label)
        except IndexError:
            print("That file is not compatible")

        row = [None]
        row.extend(parts[2][0])
        navigation = [
            parts[1][0],
            [],
            parts[1][1],
            parts[1][2],
            [],
            row,
            parts[2][1]
        ]
        
        row = [None, None]
        row.extend(parts[3][4])
        numpad = [
            [],
            [],
            parts[3][0],
            parts[3][1],
            parts[3][2],
            parts[3][3],
            row
        ]

        parts = (parts[0], navigation, numpad)

        return parts, vertical


if __name__ == "__main__":
    app = QApplication(sys.argv)

    keyboard = QKeyboard("QWERTY_es")
    keyboard.setMinimumSize(QSize(750, 275))
    keyboard.show()

    sys.exit(app.exec())
