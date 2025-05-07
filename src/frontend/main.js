

function sendText() {
    fetch("https://jsonplaceholder.typicode.com/todos", {
        method: "POST",
        body: JSON.stringify({
          userId: 1,
          title: "Fix my bugs",
          completed: false
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      });
}

function getSelectionText() {
    let text = "";

    if (window.getSelection) {
        text = window.getSelection().toString();
    } else if (document.selection && document.selection.type != "Control") {
        text = document.selection.createRange().text;
    }

    return text;
}