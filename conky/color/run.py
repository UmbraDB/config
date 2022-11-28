#!/usr/bin/env python

"""The script replaces colors contained in output from
`curl -s wttr.in/$Location` with conky-compatible color codes.
Use it like this:
```
conky.text = [[
${execpi 1800 curl -s wttr.in/Hamburg | head -7 | tail -5 | /path/to/run.py}
]]
```

Obviously, replace `Hamburg` with your location, and `1800` with your desired
interval.
"""

import sys


WHITE = "${color white}"
LIGHTGREY = "${color lightgrey}"
GREY = "${color grey}"
TEAL = "${color teal}"
LIGHTBLUE = "${color lightblue}"
BLUE = "${color blue}"
LIGHTGREEN = "${color lightgreen}"
GREEN = "${color green}"
YELLOW = "${color yellow}"
ORANGE = "${color orange}"
RED = "${color red}"


color_mapping = {
    # color reset
    "[0m": "$color",

    # white
    "[38;5;255m": WHITE,

    # lightgrey
    "[38;5;7m": LIGHTGREY,
    "[38;5;250m": LIGHTGREY,
    "[38;5;251m": LIGHTGREY,

    # grey
    "[38;5;8m": GREY,
    "[38;5;240;1m": GREY,

    # multiple teal shades
    "[38;5;050m": TEAL,
    "[38;5;051m": TEAL,

    # light blue
    "[38;5;045m": LIGHTBLUE,
    "[38;5;069m": LIGHTBLUE,
    "[38;5;081m": LIGHTBLUE,
    "[38;5;111m": LIGHTBLUE,
    "[38;5;117m": LIGHTBLUE,
    "[38;5;153m": LIGHTBLUE,

    # blue
    "[38;5;018m": BLUE,
    "[38;5;019m": BLUE,
    "[38;5;020m": BLUE,
    "[38;5;021m": BLUE,
    "[38;5;026m": BLUE,
    "[38;5;027m": BLUE,
    "[38;5;032m": BLUE,
    "[38;5;033m": BLUE,
    "[38;5;039m": BLUE,
    "[38;5;21;1m": BLUE,
    "[38;5;21;25m": BLUE,

    # light green
    "[38;5;154m": LIGHTGREEN,
    "[38;5;049m": LIGHTGREEN,  # more like a teal-green
    "[38;5;118m": LIGHTGREEN,
    "[38;5;190m": LIGHTGREEN,
    "[38;5;082m": LIGHTGREEN,
    "[38;5;083m": LIGHTGREEN,

    # green
    "[38;5;040m": GREEN,
    "[38;5;041m": GREEN,
    "[38;5;046m": GREEN,
    "[38;5;047m": GREEN,
    "[38;5;048m": GREEN,

    # yellow
    "[38;5;220m": YELLOW,
    "[38;5;226m": YELLOW,
    "[38;5;227m": YELLOW,
    "[38;5;228m": YELLOW,
    "[38;5;228;5m": YELLOW,

    # orange
    "[38;5;166m": ORANGE,
    "[38;5;167m": ORANGE,
    "[38;5;202m": ORANGE,
    "[38;5;203m": ORANGE,
    "[38;5;208m": ORANGE,
    "[38;5;214m": ORANGE,

    # red
    "[38;5;160m": RED,
    "[38;5;161m": RED,
    "[38;5;196m": RED,
    "[38;5;197m": RED,

    # bold is not supported; so no color reset
    # is broken, we just replace it with white
    "[1m": WHITE,
}


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    output = []

    for line in lines:
        output_line = line

        for color in color_mapping.keys():
            output_line = output_line.replace(color, color_mapping[color])

        output.append(output_line)

    print("".join(output))
