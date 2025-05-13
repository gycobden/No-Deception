//THIS IS RUNNING

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
  
        const selectedText = results?.[0]?.result?.trim();
        if (!selectedText) {
          document.getElementById("code").textContent = "No code selected.";
          return;
        }
  
        // Display a loading message
        document.getElementById("code").textContent = "Sending to server...";
  
        // Send POST request
        fetch("http://127.0.0.1:5000/backend/endpoint", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ code: selectedText })
        })
          .then((response) => {
            if (!response.ok) throw new Error("Server error");
            return response.json();
          })
          .then((data) => {
            document.getElementById("code").textContent =
              data.result || "No response from server.";
          })
          .catch((error) => {
            document.getElementById("code").textContent =
              "Request failed: " + error.message;
          });
      }
    );
  });
  

/*
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "getSelectedCode" }, (response) => {
    if (chrome.runtime.lastError) {
        document.getElementById("code").textContent = "Error: " + chrome.runtime.lastError.message;
      } else {
        document.getElementById("code").textContent = response.code || "No code selected.";
      }
    });
  });

*/