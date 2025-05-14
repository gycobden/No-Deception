/*
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tab = tabs[0];
  
    chrome.scripting.executeScript(
      {
        target: { tabId: tab.id },
        func: () => window.getSelection().toString()
      },
      (results) => {
        if (chrome.runtime.lastError) {
          document.getElementById("code").textContent =
            "Error: " + chrome.runtime.lastError.message;
          return;
        }
  
        const selectedText = results?.[0]?.result || "No code selected.";
        document.getElementById("code").textContent = selectedText;
      }
    );
  });*/
/*document.getElementById('test').addEventListener('click', () => {
    console.log("Popup DOM fully loaded and parsed");
    const selection = document.title;
    console.log(selection);
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const tab = tabs[0];

        function printTitle() {
            const title = document.title;
            console.log(title);
            return title;
        };

        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            func: printTitle,
            //        files: ['contentScript.js'],  // To call external file instead
        }).then(injectionResults => { 
            for (const {frameId, result} of injectionResults) {
              selection = result;
              console.log(selection);
        }});
    });
});
*/
/*
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getSelectedCode") {
      chrome.scripting.executeScript({
        target: { tabId: sender.tab.id },
        func: () => {
          return window.getSelection().toString();
        }
      }, (results) => {
        const selectedText = results[0].result;
        sendResponse({ code: selectedText });
      });
    }
  });
*/