# Lift Algorithm Implementation
This lift implementation uses a GUI to visualise the lifts movements across a range of floors, whilst comparing two competing algorithms on speed and efficiency.

## File Structure
```
├── sources/
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── look_algorithm.py
│   │   ├── scan_algorithm.py
│   │   └── stack.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── building.py
│   │   ├── floor.py
│   │   └── lift.py
│   ├── input_files/
│   │   └── input_.txt * 300
│   ├── generate_input.py
│   └── main.py
└── README.md
```

## Usage
```python
import main

main.main_loop()
```

Select the start simulation button located at the top of the screen on the GUI to run the algorithms.

Select the time complexity button located under the start button to visualise the time complexity.

## Licence
MIT License

Copyright (c) 2025 Edward Owen Allman, Benjamin Brodie Parker, Marcos Ashton Iglesias, Charlie Joseph Winders, Caspar Rex Rider Hadley

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.