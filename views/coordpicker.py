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


from PyQt5 import QtWidgets, QtGui, QtCore
import pyautogui

# This is a coordinate window picker, it allows you to click on the screen at a
# specific coordinate without disrupting the application behind it


class CoordPicker(QtWidgets.QDialog):
    instructionsText = "Please click on the bobber where you cast out the " \
                       "fishing line"

    acceptedSignal = QtCore.pyqtSignal(tuple)

    def initUI(self):
        desktop = QtWidgets.QApplication.desktop()
        desktopSize = desktop.screenGeometry()
        self.setGeometry(desktopSize)
        self.setWindowTitle("Coordinate Picker")
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Maximum)
        self.setWindowOpacity(0.5)

        self.lblInstructions.setText(self.instructionsText)
        self.lblInstructions.resize(self.lblInstructions.sizeHint())

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            coords = pyautogui.position()
            self.acceptedSignal.emit(coords)
            self.done(0)



