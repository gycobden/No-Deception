# No-Deception
### Abstract
Our primary source of knowledge is rife with misinformation, and it can be difficult to verify sources and avoid confirmation bias. No Deception provides live fact-checking and bias readings of any post or article. It will back up statistics, link the related studies, and provide external sources for further exploration.
### Goal
We want to provide an easy way to navigate the internet by removing the overhead of fact-checking. We seek to provide the ability to see at a glance whether a site or post is biased, contains inaccuracies, or is malicious.
### Repository Layout
The Repository consists of a source code folder with directories for the front end and back end. The frontend contains the UI and interfaces with the Chrome extension. The backend contains databases, the LLM configuration, and Flask API configuration. There is a testing folder within each of these.

## Installation and Set Up
```git clone https://github.com/gycobden/No-Deception/``` into your local machine, cd into the directory, then ```pip install -r requirements.txt```. It's recommended that a virtual environment be set up to download these dependencies. 

### Database
Run ```python3 init_chroma.py --reset=True``` to set up the vector database
 - If this command doesn't work, use python instead of python3.

### Fetch Server/Backend server
Add the Gemini API in the designated line in endpoint.py. Run ```python3 src/backend/endpoint.py``` in the No-Deception directory.

### Google Chrome extension 
Go to the extensions page on Google Chrome
Turn on developer mode in the top right
Click the "Load unpacked" button in the top left - this should pull up your file manager
Select the No-Deception folder
 - If you get an error message about pytest, enter this command into the terminal: Get-ChildItem -Recurse -Directory -Filter "\_\_pycache\_\_" | Remove-Item -Recurse -Force

This should add the extension to your page! To use it, we suggest pinning the extension to your Chrome taskbar, then select text and click on the extension to make it run!
