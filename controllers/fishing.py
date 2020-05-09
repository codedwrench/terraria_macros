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
from pyautogui import mouseDown, mouseUp, pixelMatchesColor
from PyQt5 import QtCore

from models.hotbar import Hotbar
from models.fishpole import FishPole


class Fishing(QtCore.QThread):
    active = False
    executing = False
    calibrated = False
    found = False

    fishingPole = FishPole()
    hotbar = Hotbar()

    # Initial search area, seen from the place where the cursor is at
    searchRangeX = 30
    searchRangeY = 4

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    # Sets cursor position to the right coordinates, also initializes the pos
    # of the bobber, the thing above the hook of the fishing rod.
    def setCursorXY(self, coordTuple):
        self.fishingPole.pointerXCoord = coordTuple[0]

        self.fishingPole.pointerYCoord = coordTuple[1]

        self.fishingPole.bobberXCoord = self.fishingPole.pointerXCoord
        self.fishingPole.bobberYCoord = self.fishingPole.pointerYCoord
        self.searchRangeX = 10
        self.searchRangeY = 3
        self.calibrated = False

    def run(self):
        fishingPole = self.fishingPole
        while self.active:
            if not self.executing:
                self.executing = True

                if not self.found:
                    mouseDown(x=fishingPole.pointerXCoord,
                              y=fishingPole.pointerYCoord)
                    mouseUp()
                    time.sleep(2)

                self.found = False

                # Search x and y range for a pixel of the color of the bobber
                for y in range(fishingPole.bobberYCoord -
                               self.searchRangeY,
                               fishingPole.bobberYCoord +
                               self.searchRangeY):

                    for x in range(fishingPole.bobberXCoord -
                                   self.searchRangeX,
                                   fishingPole.bobberXCoord +
                                   self.searchRangeX):

                        if pixelMatchesColor(x,
                                             y,
                                             fishingPole.bobberColor,
                                             fishingPole.bobberTolerance):
                            print(x, ",", y)
                            self.found = True

                            # This sets the position of the bobber and makes
                            # the range to find the bobber in small
                            if not self.calibrated:
                                self.calibrated = True
                                self.searchRangeX = 1
                                self.searchRangeY = 1
                                fishingPole.bobberXCoord = x
                                fishingPole.bobberYCoord = y

                # Add active here as well, so the program won't click one more
                # time if you're back in the main menu.
                if not self.found and self.active:
                    mouseDown(x=fishingPole.pointerXCoord,
                              y=fishingPole.pointerYCoord)
                    mouseUp()

                self.executing = False
