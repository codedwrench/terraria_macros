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

import time
from PyQt5 import QtWidgets, QtGui


from controllers.fishing import Fishing
from controllers.mining import Mining
from controllers.rapidfire import RapidFire
from models.choices import Choices
from models.fishpole import bobberColors
from views.choicewindow import ChoiceWindow
from views.coordpicker import CoordPicker



class MainController:
    choiceWindow = 0
    coordPicker = 0
    fishing = 0
    mining = 0
    rapidFire = 0

    def __init__(self):
        self.fishing = Fishing()
        self.mining = Mining()
        self.rapidFire = RapidFire()
        self.choiceWindow = ChoiceWindow(self.clicked)
        self.coordPicker = CoordPicker(self.choiceWindow.window)
        self.coordPicker.initUI()
        self.coordPicker.acceptedSignal.connect(self.coordPickerAccepted)
        self.choiceWindow.show()

    def clicked(self, choice, extraArgs=None):
        if choice == Choices.FISH:
            self.choiceWindow.hide()
            self.coordPicker.exec()
            self.choiceWindow.show()
        if choice == Choices.MINE:
            self.mining.active = True
            self.mining.start()
        if choice == Choices.RAPID_FIRE_BUTTON_LEFT:
            self.rapidFire.setButton('left')
            self.rapidFire.active = True
            self.rapidFire.start()
        if choice == Choices.RAPID_FIRE_BUTTON_RIGHT:
            self.rapidFire.setButton('right')
            self.rapidFire.active = True
            self.rapidFire.start()

        # minimize main window
        self.choiceWindow.minimize()

    # Once coordinates are accepted, show color picker for bobber color
    def coordPickerAccepted(self, coordTuple):
        self.coordPicker.close()
        self.fishing.setCursorXY(coordTuple)

        widget = QtWidgets.QColorDialog(self.choiceWindow.window)
        i = 0
        for key, value in bobberColors.items():
            widget.setCustomColor(i, QtGui.QColor(*value))
            i += 1

        widget.exec()
        selectedColor = widget.selectedColor()
        self.fishing.setBobberColor((selectedColor.red(), selectedColor.green(), selectedColor.blue()))
        self.fishing.active = True
        self.fishing.start()

    def restoreWindow(self, args=None):
        self.choiceWindow.restore()
        self.fishing.active = False
        self.mining.active = False
        self.rapidFire.active = False
        self.mining.exit()
        self.fishing.exit()
        self.rapidFire.exit()
