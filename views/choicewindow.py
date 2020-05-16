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


from PyQt5 import QtWidgets, QtCore, uic

from views.aboutWindow import AboutWindow
from models.choices import Choices


class ChoiceWindow:
    choice = Choices.NOTHING
    window = 0
    clickCallback = 0
    coordPicker = 0

    def __init__(self, click_callback):
        self.clickCallback = click_callback
        self.window = uic.loadUi("views/choicewindow.ui")
        self.window.btnFish.clicked.connect(self.fishClicked)
        self.window.btnMine.clicked.connect(self.mineClicked)
        self.window.btnRapidFireLeft.clicked.connect(self.rapidFireLeftClicked)
        self.window.actAboutQT.triggered.connect(self.showAboutQt)
        self.window.actAbout.triggered.connect(self.showAbout)

    def showAboutQt(self):
        QtWidgets.QMessageBox.aboutQt(self.window)

    def showAbout(self):
        aboutWindow = AboutWindow(self.window)
        aboutWindow.exec()

    def clicked(self, choice):
        self.choice = choice
        self.clickCallback(self.choice)

    def fishClicked(self):
        self.clicked(Choices.FISH)

    def mineClicked(self):
        self.clicked(Choices.MINE)

    def rapidFireLeftClicked(self):
        self.clicked(Choices.RAPID_FIRE_BUTTON_LEFT)

    def rapidFireRightClicked(self):
        self.clicked(Choices.RAPID_FIRE_BUTTON_RIGHT)

    def show(self):
        self.window.show()
        self.window.activateWindow()

    def hide(self):
        self.window.hide()

    def minimize(self):
        self.window.setWindowState(self.window.windowState() | QtCore.Qt.WindowMinimized)

    def restore(self):
        self.window.raise_()
        self.window.activateWindow()
        self.window.setWindowState((self.window.windowState() & ~QtCore.Qt.WindowMinimized) | QtCore.Qt.WindowActive)
