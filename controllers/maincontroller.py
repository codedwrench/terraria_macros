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


from controllers.fishing import Fishing
from controllers.mining import Mining
from controllers.rapidfire import RapidFire
from models.choices import Choices
from views.choicedialog import ChoiceDialog
from views.coordpicker import CoordPicker


class MainController:
    choiceDialog = 0
    coordPicker = 0
    fishing = 0
    mining = 0
    rapidFire = 0

    def __init__(self):
        self.fishing = Fishing()
        self.mining = Mining()
        self.rapidFire = RapidFire()
        self.choiceDialog = ChoiceDialog(self.clicked)
        self.coordPicker = CoordPicker()
        self.coordPicker.initUI()
        self.coordPicker.acceptedSignal.connect(self.coordPickerAccepted)
        self.choiceDialog.show()

    def clicked(self, choice):
        if choice == Choices.FISH:
            self.coordPicker.show()
        if choice == Choices.MINE:
            self.mining.active = True
            self.mining.start()
        if choice == Choices.RAPID_FIRE_BUTTON_LEFT:
            self.rapidFire.active = True
            self.rapidFire.start()

    def coordPickerAccepted(self, coordTuple):
        self.fishing.setCursorXY(coordTuple)
        self.fishing.active = True
        self.fishing.start()

    def showDialog(self, args=None):
        self.choiceDialog.show()
        self.fishing.active = False
        self.mining.active = False
        self.rapidFire.active = False
        self.mining.exit()
        self.fishing.exit()
        self.rapidFire.exit()

    def hideDialog(self):
        self.choiceDialog.hide()
