# NoteBook

A simple and lightweight text editor built with Python and Tkinter.

## Features

- **Basic Text Editing**: Create, open, and save text files with customizable encoding
- **Customizable Interface**: 
  - Adjustable font colors and background colors
  - Configurable font sizes
  - Window transparency settings
- **Collaborator Management**: 
  - Add, remove, and view collaborator information
  - Store collaborator details (name, gender, IP address)
- **User-Friendly Interface**:
  - Intuitive menu system
  - Confirmation dialogs for important actions
  - Helpful about and help sections
  - Fun and creative window titles

## Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Running from Source
1. Clone or download this repository
2. Navigate to the source directory
3. Run the application:

```bash
python NoteBook.pyw
```

### Creating Executable
To create a standalone executable without console window:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile NoteBook.pyw
```

## Usage

### File Operations
- **Open**: Load existing text files with specified encoding
- **Save**: Save your work to a file with chosen encoding

### Settings
- **Font Color**: Change the text color from predefined options
- **Background Color**: Modify the editor's background color
- **Font Size**: Adjust text size from 8pt to 72pt
- **Window Transparency**: Control window opacity (10%-100%)

### Collaborator Management
- **Add**: Register new collaborators with name, gender, and IP
- **Delete**: Remove existing collaborators
- **View**: Display the list of all registered collaborators

## Configuration

The application uses JSON configuration files:
- Custom window titles with creative and fun messages
- Exit confirmation messages with various playful prompts
- Application version and author information
- Logging settings

Personal preferences are saved in the `../saves/` directory:
- [font.txt](saves\font.txt): Font color settings
- [back.txt](saves\back.txt): Background color settings
- [size.txt](saves\size.txt): Font size preferences
- [alpha.txt](saves\alpha.txt): Window transparency level
- [colluages.json](saves\colluages.json): Collaborator information

## Keyboard Shortcuts

### Basic Editing
- `Ctrl+C`: Copy selected text
- `Ctrl+V`: Paste clipboard content
- `Ctrl+X`: Cut selected text
- `Ctrl+Z`: Undo last operation
- `Ctrl+Y`: Redo undone operation
- `Ctrl+A`: Select all text

### Navigation
- `Ctrl+Home`: Move to document beginning
- `Ctrl+End`: Move to document end
- `Ctrl+Left/Right`: Move cursor by word
- `Ctrl+Up/Down`: Vertical scrolling

### Text Selection
- `Shift+Arrow keys`: Extend text selection
- `Ctrl+Shift+Left/Right`: Select by word
- `Ctrl+Shift+Home/End`: Select to document start/end

### Other Functions
- `Tab`: Insert tab character or indent selected text
- `Enter`: Insert new line
- `Delete/Backspace`: Delete characters

## Sample Window Titles

- "Why are there bite marks from FeSo4a here?"
- "This is just an ordinary notebook~"
- "Today's inspiration collector is online!"
- "The magical notebook that makes words work for you"
- "It's said that 99% of creative ideas are born here"

## Sample Exit Confirmation Messages

- "Really want to exit? qwq"
- "Don't exit! Are you sure? qwq"
- "The note isn't finished yet, are you sure you want to leave?"
- "Wait! Your inspiration might burst in the next second!"
- "Before closing, take another look, there might be surprises~"

## Author

FeSo4a - [GitHub Profile](https://github.com/FeSo4a)  
[bilibili](https://space.bilibili.com/3546674548967510)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
