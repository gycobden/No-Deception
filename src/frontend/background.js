//  chrome.storage.local - for storing data on local machines.
//  service workers have no access to window.localStorage

const tldLocales = {
    'com.m': 'More Context',
    'com.l': 'Less Context'
  }
  
  chrome.runtime.onInstalled.addListener(async () => {
    for (let [tld, locale] of Object.entries(tldLocales)) {
      chrome.contextMenus.create({
        id: tld,
        title: locale,
        type: 'normal',
        contexts: ['selection'],
      });
    }
<<<<<<< HEAD
=======
  });

  chrome.action.onClicked.addListener((tab) => {
    chrome.action.setTitle({
      tabId: tab.id,
      title: `You are on tab: ${tab.id}`});
>>>>>>> b61fe74236403cf5095221792570fecd17aef6c1
  });