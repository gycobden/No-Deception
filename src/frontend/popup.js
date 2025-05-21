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
          document.getElementById("highlights").textContent =
            "Error: " + chrome.runtime.lastError.message;
          document.getElementById("truthy").textContent =
            "Error: " + chrome.runtime.lastError.message;
          document.getElementById("article").textContent =
            "Error: " + chrome.runtime.lastError.message;
          return;
        }
  
        const selectedText = results?.[0]?.result?.trim();
        if (!selectedText) {
          document.getElementById("highlights").textContent = "No code selected.";
          document.getElementById("truthy").textContent = "No code selected.";
          document.getElementById("article").textContent = "No code selected.";
          return;
        }
  
        // Display a loading message
        document.getElementById("highlights").textContent = "Sending to server...";
        document.getElementById("truthy").textContent = "Sending to server...";
        document.getElementById("article").textContent = "Sending to server...";
  
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
            console.log("Server response:", data);

            if (Array.isArray(data.highlights)) {
              document.getElementById("highlights").textContent =
                data.highlights.length > 0
                  ? data.highlights.join('\n\n')
                  : "No highlights found.";
            } else {
              document.getElementById("highlights").textContent =
                "No response from server.";
            }
            document.getElementById("truthy").textContent =
              data.truthy || "No response from server.";
            document.getElementById("article").textContent =
              data.article || "No response from server.";
          })
          .catch((error) => {
            document.getElementById("highlights").textContent =
              "Request failed: " + error.message;
            document.getElementById("truthy").textContent =
              "Request failed: " + error.message;
            document.getElementById("article").textContent =
              "Request failed: " + error.message;
          });
      }
    );
  });