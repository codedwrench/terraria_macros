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


class RapidFire(QtCore.QThread):
    active = False
    executing = False
    button = 'left'

    def setButton(self, button):
        self.button = button

    def run(self):
        while self.active:
            if not self.executing:
                self.executing = True
                rapid_fire_delay = 0.01
                pyautogui.mouseDown(button=self.button)
                pyautogui.mouseUp(button=self.button)
                time.sleep(rapid_fire_delay)
                self.executing = False


