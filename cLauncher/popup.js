chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      console.log("The color is green.");
    });
  });



let runBoa = document.getElementById('boaCall');

var value = 1;

runBoa.onclick = function(element) {

	chrome.storage.local.get(['key'], function(result) {
          console.log('Value currently is ' + result.key);
        });


	console.log("test")
	chrome.storage.local.set({key: value}, function() {
          console.log('Value is set to ' + value);
        });
  };