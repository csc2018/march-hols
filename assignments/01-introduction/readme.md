# Introduction

At this point, you should have been introduced to Python already. Regardless of whether you've written a single line of code, this assignment aims to get you started on writing Python code on your own computer.

**Prerequisites**: Know what Python is

# Task

Learn how to run Python code on your own computer.

## Instructions

### Python Installation
Install [Python 3.6](https://www.python.org/downloads/) - **remember to check "Install Python to PATH"**

Now, use your preferred command console, or follow the instructions below:

### Using the Console

**Windows**:

- Shift + right-click this folder on your computer and click "Open *PowerShell* window here"
- Alternatively, open *Command Prompt* and type `dir <path/to/this/folder>`
- For example:
```powershell
> dir C:\Users\Aaron\Documents\GitHub\march-hols\assignments\01-introduction
```

**Mac/Linux**:

- Open *Terminal* and type `cd <path/to/this/folder>`
- For example:
```bash
$ cd /Users/aaron/Documents/GitHub/march-hols/assignments/01-introduction
```

### Using Python in Console

Test your Python installation by typing this into your console:
```
python
```

You **should** see something like:
```
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Pay attention to the version, it should be **Python 3.6 and above**. If not, see the [FAQ](#FAQ).

### Running a Python file

Run the Python file `helloworld.py` that *should be in the same folder as this readme* by entering this into your command window:
```
python helloworld.py
```

Questions? See if the FAQ helps, or contact one of the exco members.

## FAQ

*When running `python`, my Python version is not Python 3.6 and above!*

- You either installed Python 2.7 (or below), or already have Python 2 installed on your computer previously. Remember to install the latest **Python 3** version (3.6.4 as of 11/3/2018) and replace the command with whichever works: `python3`, `py`, `python3.6`

*When running `helloworld.py`, an error appears: can't open file 'helloworld.py': [Errno 2] No such file or directory*

- Make sure you've navigated into the folder that contains the file. This is the `01-introductions` folder inside the `assignments` folder, i.e `march-hols/assignments/01-introductions`. Also check the spelling of the file - the Python file is **helloworld.py**.

*My question isn't on this list. Help?*

- Contact one of the exco members and we'll see what we can do.