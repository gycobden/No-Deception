// Saves options to chrome.storage
const saveOptions = () => {
  const darkMode = document.getElementById('dark').checked;

  chrome.storage.sync.set(
    { darkMode: darkMode },
    () => {
      // Update status to let user know options were saved.
      const status = document.getElementById('status');
      status.textContent = 'Options saved.';
      setTimeout(() => {
        status.textContent = '';
      }, 750);
    }
  );
};

// Restores select box and checkbox state using the preferences
// stored in chrome.storage.
const restoreOptions = () => {
  chrome.storage.sync.get(
    { darkMode: false },
    (items) => {
      document.getElementById('dark').checked = items.darkMode;
    }
  );
};

document.addEventListener('DOMContentLoaded', restoreOptions);
document.getElementById('save').addEventListener('click', saveOptions);

chrome.storage.sync.get({ darkMode: false }, (items) => {
  if (items.darkMode) {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
});