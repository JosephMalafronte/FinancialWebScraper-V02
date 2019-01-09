chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      console.log("The color is green.");
    });
  });



//Read op number from spreadsheet?s
var opNumber = 6;

var triggerString;



document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('link');
    // onClick's logic below:
    link.addEventListener('click', function() {
        runBoa();
    });
});

runBoa = function(){
  chrome.storage.local.get(['key'], function(result) {
          console.log('Value currently is ' + result.key);
          opNumber = result.key;
        });

  triggerString = "Trigger"
  localStorage.setItem("secret message" + opNumber.toString(), triggerString);

  opNumber += 1;
  chrome.storage.local.set({key: opNumber}, function() {
          console.log('Value is set to ' + opNumber);
        });
};



  
