#   Heartbeat
#   Copyright (C) 2017 Matheus Cariús
#   Copyright (C) 2013 Ignacio M. Bataller

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import video
import processing

__version__ = 0.1

def main(): 
    print("Heartbeat v{}".format(__version__))
    if(len(sys.argv) < 2):
        print("Usage: '{} <path to video>'".format(sys.argv[0]))
        return 

    processing.process_video(sys.argv[1])

if __name__ == '__main__':
    main()
