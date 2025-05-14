# No-Deception
### Abstract
Our primary source of knowledge is rife with misinformation, and it can be difficult to verify sources and avoid confirmation bias. No Deception provides live fact-checking and bias readings of any post or article. It will back up statistics, link the related studies, and provide external sources for further exploration.
### Goal
We want to provide an easy way to navigate the internet by removing the overhead of fact-checking. We seek to provide the ability to see at a glance whether a site or post is biased, contains inaccuracies, or is malicious.
### Repository Layout
The Respository will consist of a source code folder with directories for the front end and back end. The front end will have the UI and assets, and the back end will have databases and API configuration. There will be a testing folder within each of these.

### Installation
```git clone https://github.com/gycobden/No-Deception/``` into your local machine, cd into the directory, then ```pip install -r requirements.txt```.

### Database Setup
run ```python3 init_chroma.py --reset=True``` to set up the vector database

### Fetch Server/Backend server
run the "endpoint.py" file. The easiest way we have found it to run "python src\backend\endpoint.py" if your terminal is open in the No-Deception directory.

### Google Chrome extension 
Go into the extensions page on google chrome
Turn on developer mode in the top right
Click the "Load unpacked" button in the top left - this should pull up your file manager
Find the "src" folder in the No-Deception directory and open in.
This should add the extension to your page! In order to use it we suggest pinning the extension to your chrome task bar, then select text and click on the extension to make it run!
