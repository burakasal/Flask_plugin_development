//Initialize jquery for extension load
$(function(){
	// Debug
	console.log("WebExtloaded");

	//Simple txt label for misc info/debug
	$("#txtStatus").text("Extension is loaded!").css({"color": "green"});

			
	//Setup event listener on button
	$("#btnDo").click(function(e){

		chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
			let taburl = tabs[0].url;
			console.log("URL: "+taburl);

    		// make ajax request to our server
    		$.ajax({
        		url: "http://localhost:5000/api/fetch",
        		type: "post",
        		data: taburl,
        		contentType: "application/json",
        		success: function (response) {
           			// You will get response from your PHP page (what you echo or print)
           			console.log(response);
           			$("#txtStatus").text("Connection successful to backend!").css({ 'color': 'green'});
        			$("#txtResponse").text(response.detail).css({ 'color': 'blue'});
        		},
        		error: function(jqXHR, textStatus, errorThrown) {
           			console.log(textStatus, errorThrown);
           			$("#txtStatus").text("Connection failed to backend!").css({ 'color': 'red'});
        			$("#txtResponse").text("");
        		}
    		});

  		});		
	});
	$("#btnNer").click(function(e){

		chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
			let taburl = tabs[0].url;
			console.log("URL: "+taburl);
			
    		// make ajax request to our server
    		$.ajax({
        		url: "http://localhost:5000/api/fetch2",
        		type: "post",
        		data: taburl,
        		contentType: "application/json",
        		success: function (response) {
           			// You will get response from your PHP page (what you echo or print)
           			console.log(response);
           			$("#txtStatus").text("Connection successful to backend!").css({ 'color': 'green'});
        			$("#txtResponse").text(response.detail).css({ 'color': 'blue'});
        		},
        		error: function(jqXHR, textStatus, errorThrown) {
           			console.log(textStatus, errorThrown);
           			$("#txtStatus").text("Connection failed to backend!").css({ 'color': 'red'});
        			$("#txtResponse").text("");
        		}
    		});

  		});		
	});
});

