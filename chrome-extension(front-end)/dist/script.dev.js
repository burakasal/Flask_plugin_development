"use strict";

var el = document.getElementById("myButton");

if (el) {
  el.addEventListener("click", myFunction);
}

function myFunction() {
  chrome.tabs.getSelected(null, function (tab) {
    chrome.tabs.detectLanguage(tab.id, function (language) {
      if (language == "en") {
        window.location.href = "en.html";
      } else if (language == "tr") {
        window.location.href = "tr.html";
      }
    });
  });
}