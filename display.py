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

modules = 4

class Display:

  def __init__(self):
    self.spi = spidev.SpiDev()
    self.spi.open(0, 0)

    self.spi.max_speed_hz = 5000000
    #spi.mode = 0b01

    # enable
    self.spi.xfer([0x0c, 0x01, 0x0c, 0x01, 0x0c, 0x01, 0x0c, 0x01])
    # decode mode: raw; no BCD
    self.spi.xfer([0x09, 0x00, 0x09, 0x00, 0x09, 0x00, 0x09, 0x00])
    # intensity
    self.spi.xfer([0x0a, 0x03, 0x0a, 0x03, 0x0a, 0x03, 0x0a, 0x03])
    # scan limit: display all
    self.spi.xfer([0x0b, 0x07, 0x0b, 0x07, 0x0b, 0x07, 0x0b, 0x07])

  def display(self, screen):
    for i in range(8):
      data = []
      for block in screen:
        data.extend([i + 1, block[i]])
      self.spi.xfer(data)
