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


from PyQt5 import QtWidgets, uic

from models.choices import Choices


class ChoiceDialog:
    choice = Choices.NOTHING
    window = 0
    clickCallback = 0
    coordPicker = 0

    def __init__(self, click_callback):
        self.clickCallback = click_callback
        self.window = uic.loadUi("views/choicedialog.ui")
        self.window.btnFish.clicked.connect(self.fishClicked)
        self.window.btnMine.clicked.connect(self.mineClicked)
        self.window.btnRapidFireLeft.clicked.connect(self.rapidFireLeftClicked)

    def clicked(self, choice):
        self.choice = choice
        self.window.hide()
        self.clickCallback(self.choice)

    def fishClicked(self):
        self.clicked(Choices.FISH)

    def mineClicked(self):
        self.clicked(Choices.MINE)

    def rapidFireLeftClicked(self):
        self.clicked(Choices.RAPID_FIRE_BUTTON_LEFT)

    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
