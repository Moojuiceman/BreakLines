# BreakLines
A plugin for [Sublime Text](http://www.sublimetext.com/) to break lines into groups of X lines.

## Installation

Install via [Package Control](https://packagecontrol.io/).

## Usage

There are shortcuts for creating groups of 10, 100, 1000, and X lines:

 - 10 lines: Ctrl+Alt+B, 1
 - 100 lines: Ctrl+Alt+B, 2
 - 1000 lines: Ctrl+Alt+B, 3
 - X lines: Ctrl+Alt+B, 4

These shortcuts should work on any platform. These commands are also available in the command palette and the Tools menu under "Break lines".

The X lines option will prompt for a number, and insert a newline after each group of this many lines within the selection/s. The 10, 100, and 1000 options behave the same without prompting. If nothing is selected (i.e. all selections are 0 characters) then the entire file will be grouped.

## Examples

No selections, break every 7 lines

| Before | After |
| :----- | :---- |
| ![no selection before](https://user-images.githubusercontent.com/7610940/42520324-de02eeaa-845d-11e8-8000-8c5a5ce91ff6.png) | ![no selection after](https://user-images.githubusercontent.com/7610940/42520177-8d1b6846-845d-11e8-8a45-fdc6c47306a3.png) |

Multiple selections, break every 2 lines

| Before | After |
| :----- | :---- |
| ![selection before](https://user-images.githubusercontent.com/7610940/42520182-8f452292-845d-11e8-81a3-d35aece49a42.png) | ![selection after](https://user-images.githubusercontent.com/7610940/42520184-910cdad4-845d-11e8-8cda-fafd1090acfb.png) |