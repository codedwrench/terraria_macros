#!/usr/bin/env python
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

import atexit
import keyboard
import pyautogui
import sys

from PyQt5 import QtWidgets

from controllers.maincontroller import MainController
from models.hotbar import Hotbar


hotbar = Hotbar()


def exitHandler():
    keyboard.unhook_all()


def useMagicMirror(arg):
    pyautogui.keyDown(hotbar.mirrorSlot)
    pyautogui.keyUp(hotbar.mirrorSlot)
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def main():
    atexit.register(exitHandler)
    app = QtWidgets.QApplication(sys.argv)
    mainController = MainController()

    pyautogui.FAILSAFE = True
    print("Starting")
    keyboard.on_press_key('num 7', mainController.showDialog)
    keyboard.on_press_key('num 8', useMagicMirror)
    keyboard.on_press_key('b', useMagicMirror)

    app.exec()


if __name__ == "__main__":
    main()
