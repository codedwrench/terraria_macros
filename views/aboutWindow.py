# -*- coding: utf-8 -*-
#
# This file is part of terraria_macros.
# A program that contains a bunch of macros for the videogame called Terraria.
# Copyright (C) 2020 Rick de Bondt
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from PyQt5 import QtWidgets, QtCore


class AboutWindow(QtWidgets.QDialog):
    aboutText = "<b>terraria_macros</b><br><br>" \
                "This program provides some macros you can use for the game: Terraria<br><br>" \
                "Copyright © 2020 Rick de Bondt<br><br>" \
                "This program is free software: you can redistribute it and/or modify<br>" \
                "it under the terms of the GNU General Public License as published by<br>" \
                "the Free Software Foundation, either version 3 of the License, or<br>" \
                "(at your option) any later version.<br><br>" \
                "This program is distributed in the hope that it will be useful,<br> " \
                "but WITHOUT ANY WARRANTY; without even the implied warranty of <br>" \
                "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br>" \
                "GNU General Public License for more details.<br><br>" \
                "You should have received a copy of the GNU General Public License<br>" \
                "along with this program.  If not, see " \
                "&lt;<a href='https://www.gnu.org/licenses/'>https://www.gnu.org/licenses/</a>&gt;."

    lblAboutTxt = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QGridLayout()
        self.lblAboutTxt = QtWidgets.QLabel()
        self.lblAboutTxt.setTextFormat(QtCore.Qt.RichText)
        self.lblAboutTxt.setText(self.aboutText)
        layout.addWidget(self.lblAboutTxt)
        self.setLayout(layout)
        self.setWindowTitle("About")

    def exec(self) -> int:
        return super().exec()
