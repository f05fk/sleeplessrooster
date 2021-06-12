#!/usr/bin/python3
#########################################################################
# Copyright (C) Claus Schrammel <claus@f05fk.net>                       #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                       #
# SPDX-License-Identifier: GPL-3.0-or-later                             #
#########################################################################

import spidev
import time
from display import Display

display = Display()

try:
  while True:
    display.display([[0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                     [0x33, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                     [0x0f, 0xf0, 0x0f, 0xf0, 0x0f, 0xf0, 0x0f, 0xf0],
                     [0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00]])
    time.sleep(0.3)
    display.display([[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff],
                     [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xcc, 0xcc],
                     [0xf0, 0x0f, 0xf0, 0x0f, 0xf0, 0x0f, 0xf0, 0x0f],
                     [0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff]])
    time.sleep(0.3)
except:
  display.display([[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                   [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                   [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                   [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]])
