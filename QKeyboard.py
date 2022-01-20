class QKeyboard(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("QLabel { background: #0070a0 }")

        self.layout = QHBoxLayout(self)
        self.layout.addLayout(self.init_core(False), 15)
        self.layout.addLayout(self.init_navigation(), 3)
        self.layout.addLayout(self.init_numpad(), 4)

    def init_core(self, ignoreFkeys):
        layout = QVBoxLayout()

        if not ignoreFkeys:
            labels = [
                ["esc"],
                ["f1", "f2", "f3", "f4"],
                ["f5", "f6", "f7", "f8"],
                ["f9", "f10", "f11", "f12"]
            ]
            row = QHBoxLayout()
            for i, section in enumerate(labels):
                for label in section:
                    l_widget = QLabel(label)
                    l_widget.setAlignment(Qt.AlignCenter)
                    row.addWidget(l_widget, 1)
                if i != 3:
                    row.addStretch(1)
            layout.addLayout(row, 2)
            layout.addStretch(1)

        labels = [
            ["º", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "'", "¡", ("<-", 8)],
            [("tab", 6), "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "`", "+"],
            [("bloq\nmayús", 7), "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "´", "Ç"],
            [("mayús", 5), "<", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "-", ("mayús", 11)],
            [("ctrl", 6), "win", ("alt", 5), ("space", 26), ("alt gr", 5), "FN", "menu", ("ctrl", 6)]
        ]
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
        row1and2.addWidget(l_widget, 4)
        layout.addLayout(row1and2, 4)

        row = QHBoxLayout()
        self.init_row(row, labels[3])
        layout.addLayout(row, 2)
        row = QHBoxLayout()
        self.init_row(row, labels[4])
        layout.addLayout(row, 2)

        return layout

    def init_navigation(self):
        layout = QGridLayout()
        labels = [
            ["print", "block", "pause"],
            [],
            ["insert", "inicio", "re\npág"],
            ["supr", "fin", "av\npág"],
            [],
            [None, "up"],
            ["left", "down", "right"],
        ]

        self.init_grid(layout, labels)
        for i in range(7):
            layout.setRowStretch(i, 2)
        layout.setRowStretch(1, 1)

        return layout

    def init_numpad(self):
        layout = QGridLayout()
        labels = [
            [],
            [],
            ["bloq\nnum", "/", "-", "*"],
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, None, ","],
        ]

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
            if isinstance(item, Tuple):
                label, stretch_factor = item
            else:
                label = item
                stretch_factor = 4
            l_widget = QLabel(label)
            l_widget.setAlignment(Qt.AlignCenter)
            layout.addWidget(l_widget, stretch_factor)
