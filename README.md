# No Deception
Our primary source of knowledge is rife with misinformation, and it can be difficult to verify sources and avoid confirmation bias. No Deception provides live fact-checking and bias readings of any post or article. It will back up statistics, link the related studies, and provide external sources for further exploration.

## Installation and Set Up (Linux)
1) ```git clone https://github.com/gycobden/No-Deception/``` into your local machine, cd into the directory, then ```pip install -r requirements.txt```. It's recommended that a virtual environment be set up to download these dependencies.
2) Run ```python3 init_chroma.py --reset=True``` to set up the vector database
3) Add a Gemini API as an environment variable with the command ```export GENAI_API_KEY="your_value_here"``` (on Windows: ```$env:GENAI_API_KEY="your_value_here"```), then run ```python src/backend/endpoint.py``` in the No-Deception directory.
4) Go to the extensions page on Google Chrome, turn on developer mode, go to "manage extension" and press the "Load unpacked" button in the top left, and select the 'Frontend' folder

This should add the extension to your page!

## Usage
Simply go to a website, highlight a piece of text that you want fact-checked, then click on the No Deception Google extension icon and see the magic!

## WIP Features
- Converting our binary accuracy score (good/bad) into a numerical one (0-100%)
- Simplifying installation for typical users through the main Google Extensions page
- Implementing a "Report Bugs" button on the extension's UI
- Moving the database to the Cloud (AWS EC2 or something)
- Allowing users to download the extension without needing to access the backend

## Bug Reporting
**IMPORTANT:** Please check the "Known Bugs" section below to make sure the bug you are encountering is not already being fixed by the developers before submitting.
Email ```evanmao@uw.edu``` to report any bugs encountered in installation or using the extension. Please use the following format in your email:
- Specify the exact steps needed to reproduce your bug
- Note down the version of the extension you are using
- Mention what operating system the bug is occurring on (Mac, Windows, Linux, etc.)
- Elaborate on the expected output and the actual output of the bug
- Any additional information relevant to the bug

## Known Bugs
Documents don't display in pop-up - try rerunning ```python3 init_chroma.py --reset=True```

## Developer Documentation
If you want to contribute to our project, please keep reading! Your work is greatly appreciated. :D

### Obtaining Source Code
Simply run the ```git clone https://github.com/gycobden/No-Deception/``` command in your terminal and follow the same procedure as detailed in installation and setup

### Repository Layout
The Repository consists of a source code folder with directories for the front end and back end. The frontend contains the UI and interfaces with the Chrome extension. The backend contains databases, the LLM configuration, and Flask API configuration. Tests for the backend and frontend are in the respective backend and frontend folders.

### Hosting the database
There are two ways for the LLM backend services to connect to the database, and this behavior can be defined the ```config.py``` file.
 - Method 1: connect to a database locally. If you have a database stored locally on the machine though running the command ```python3 init_chroma.py --reset=True```, you can instruct the program to connect to this locally installed database by changing ```REMOTE_ACCESS = False``` in ```config.py``` and specify the ```CHROMA_PATH``` to be where the database is installed, which defaults to ```"src/backend/database/chroma_store"```.
 - Method 2: Remote connection. If you know the address of the host of the remost connection and the port to connect to, you can define that in ```config.py``` by setting the variables ```REMOTE_ADDRESS``` and ```REMOTE_PORT``` and setting ```REMOTE_ACCESS``` to be true. For simple test, if you have a locally stored database, you can host the database to your local server by running ```chroma run /path/to/your/local/database``` and set ```REMOTE_ADDRESS``` to be ```"localhost"``` and port to be ```8000``` to test that remote connection to local server is established.

### Building and Testing
Our CI builds on any push or pull request.

If you want to add some documents to be included in our dataset, import them into the ```./src/backend/articles``` folder. Then rerun the command ```python3 init_chroma.py --reset=True```.

Run ```pytest``` to run test files in src/backend/tests.

### Adding New Tests
#### LLM Integration Testing:
To add a new test, navigate to ```src/backend/llm_integration/tests.py```. To write a new test, follow the convention: test_testName. Ensure that testName is a simple, short description of the test. These tests must be focused on querying the LLM, including the prompts and return types.

#### Database Testing:
Navigate to ```src/backend/tests```, where you will see ```test_chromadb.py``` and ```test_docu_processing.py```. To add tests, put the ```@pytest.fixure``` above each test function, and each test should be preceded with ```test_```. These tests must be focused on verifying the database and document processing.

### Building a Release
For privacy and security reasons, you will need to generate your API key and add it as an environment variable.
Update the version number in the documentation before invoking the build system for clarity.

## Repository Structure
```
NoDeception/
├──.github/workflows/
├──_pycache_/
├──documents/
│  ├──requirements.pdf                  # class related documentation
├──src/
│   ├──backend/
│       ├──articles/                    #stores articles for DB
│        ├──database/                   #database initialization
│        ├──llm_integration/            #integration of gemini LLM
│       ├──tests/                       #DB and LLM tests
│        ├──__init__.py
│       ├──endpoint.py                  #backend endpoint to connect to frontend
│   ├──frontend/                        #establishing google extensions
├──.gitignore/
├──README.md
├──config.py
├──init_chroma.py
├──pytest.ini
└──requirements.txt

```
### Building a Release
For privacy and security reasons, you will need to generate your API key and add it as an environment variable.
Update the version number in the documentation before invoking the build system for clarity.
