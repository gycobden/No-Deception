# No-Deception
Our primary source of knowledge is rife with misinformation, and it can be difficult to verify sources and avoid confirmation bias. No Deception provides live fact-checking and bias readings of any post or article. It will back up statistics, link the related studies, and provide external sources for further exploration.

## Installation and Set Up
1) ```git clone https://github.com/gycobden/No-Deception/``` into your local machine, cd into the directory, then ```pip install -r requirements.txt```. It's recommended that a virtual environment be set up to download these dependencies.
2) Run ```python3 init_chroma.py --reset=True``` to set up the vector database
   - If this command doesn't work, use python instead of python3.
4) Add the Gemini API Key on Line 17 of src/backend/llm_integration/llm_query.py, then run ```python3 src/backend/endpoint.py``` in the No-Deception directory.
5) Go to the extensions page on Google Chrome, turn on developer mode, load in the contents by pressing the "Load unpacked" button in the top left and select the No-Deception folder
   - If you get an error message about pytest, type ```Get-ChildItem -Recurse -Directory -Filter "\_\_pycache\_\_" | Remove-Item -Recurse -Force``` into your terminal

This should add the extension to your page! 

## Usage
Simply go to a website, highlight a piece of text that you want fact-checked, then click on the No Deception google extension icon and see the magic!

## WIP Features
- Converting our binary accuracy score (good/bad) into a numerical one (0-100%)
- Simplifying installation for typical users through the main Google Extensions page
- Implementing a "Report Bugs" button on the extension's UI
- Moving the database to the Cloud (AWS EC2 or something)

## Bug Reporting
**IMPORTANT:** Please check the "Known Bugs" section below to make sure the bug you are encountering is not already being fixed by the developers before submitting.
Email ```evanmao@uw.edu``` to report any bugs encountered in installation or using the extension. Please use the following format in your email:
- Specify the exact steps needed to reproduce your bug
- Note down the version of the extension you are using
- Mention what operating system the bug is occurring on (Mac, Windows, Linux, etc.)
- Elaborate on the expected output and the actual output of the bug
- Any additional information relevant to the bug

## Known Bugs
n/a

## Developer Documentation
If you want to contribute to our project, please keep reading! Your work is greatly appreciated. :D

### Repository Layout
The Repository consists of a source code folder with directories for the front end and back end. The frontend contains the UI and interfaces with the Chrome extension. The backend contains databases, the LLM configuration, and Flask API configuration. There is a testing folder within each of these.

### Building and Testing

### Adding New Tests

### Documentation
