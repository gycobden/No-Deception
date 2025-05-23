# No Deception

<img src="https://github.com/gycobden/No-Deception/blob/main/src/frontend/img/shield_logo.png" alt="Alt Text" width="200" height="auto"><br><br>

Our primary source of knowledge is rife with misinformation, and it can be difficult to verify sources and avoid confirmation bias. No Deception provides live fact-checking and bias readings of any post or article. 

### Overview
No Deception is a Chrome extension that allows you to analyze website text. When you highlight text and activate it, No Deception will list out misleading or inaccurate sentences, provide an overall text accuracy assessment, and provide referenced external sources for further exploration.

### Installation and Set Up (Linux)
1) ```git clone https://github.com/gycobden/No-Deception/``` into your local machine, cd into the directory, then ```pip install -r requirements.txt```. It's recommended that a virtual environment be set up to download these dependencies.
2) Run ```python3 init_chroma.py --reset=True``` to set up the vector database
3) Create a Gemini API key: follow instructions at https://aistudio.google.com/app/apikey.
4) Add your Gemini API key as an environment variable with the command ```export GENAI_API_KEY="your_value_here"``` (on Windows: ```$env:GENAI_API_KEY="your_value_here"```), then run ```python3 src/backend/endpoint.py``` in the No-Deception directory.

#### Adding Extension to Chrome
Open the three-dot menu, hover over extensions, and hit "manage extensions."

<img src="https://github.com/user-attachments/assets/70401681-fef4-4a5f-82b4-5e25cf4746a3" alt="Alt Text" width="800" height="auto"><br><br>

In the top right, flip the switch to turn on developer mode

<img src="https://github.com/user-attachments/assets/0eb33977-cacb-4eca-b618-9ba27e4816ff" alt="Alt Text" width="800" height="auto"><br><br>

Press the "Load unpacked" button in the top left

<img src="https://github.com/user-attachments/assets/54840102-654a-47b6-b2e1-4f77b509b564" alt="Alt Text" width="400" height="auto"><br><br>

Navigate to your No Deception directory, click into src, and select "frontend"

<img src="https://github.com/user-attachments/assets/589fde44-856c-42e3-a94a-b35eaddfba79" alt="Alt Text" width="400" height="auto"><br><br>

This will add the extension locally to Chrome.


### Usage
Go to a website and highlight a piece of text that you want fact-checked. Click the extension icon (puzzle piece) to the right of the search bar. Click on No Deception. This will create a pop-up that contains flagged sentences, an overall categorization, and referenced documents.

![Image](https://github.com/user-attachments/assets/1c50082f-9c6a-433c-a5a9-7e98dff8d601)<br><br>

### WIP Features
- Simplifying installation for typical users through the main Google Extensions page
- Implementing a "Report Bugs" button on the extension's UI
- Moving the database to the Cloud (AWS EC2 or something)

### Bug Reporting
**IMPORTANT:** Please check the "Known Bugs" section below to make sure the bug you are encountering is not already being fixed by the developers before submitting.
Email ```evanmao@uw.edu``` to report any bugs encountered in installation or using the extension. Please use the following format in your email:
- Specify the exact steps needed to reproduce your bug
- Note down the version of the extension you are using
- Mention what operating system the bug is occurring on (Mac, Windows, Linux, etc.)
- Elaborate on the expected output and the actual output of the bug
- Any additional information relevant to the bug

### Known Bugs
Documents don't display in pop-up - try rerunning ```python3 init_chroma.py --reset=True```

## Developer Documentation
If you want to contribute to our project, please keep reading! Your work is greatly appreciated. :D

### Obtaining Source Code
Follow the same procedure as detailed in the installation and setup
=======
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

### Repository Structure
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
