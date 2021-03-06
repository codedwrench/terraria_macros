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
import pyautogui
from PyQt5 import QtCore
from models.hotbar import Hotbar


class Mining(QtCore.QThread):
    active = False
    executing = False
    hotbar = Hotbar()

    def run(self):
        pyautogui.keyDown(self.hotbar.pickaxeSlot)
        pyautogui.keyUp(self.hotbar.pickaxeSlot)
        while self.active:
            if not self.executing:
                self.executing = True
                mining_time = 0.4
                pyautogui.mouseDown(x=953, y=565)
                time.sleep(mining_time)
                pyautogui.mouseUp()
                pyautogui.mouseDown(x=973, y=565)
                time.sleep(mining_time)
                pyautogui.mouseUp()
                self.executing = False

