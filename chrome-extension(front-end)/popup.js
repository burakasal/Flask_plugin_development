//Initialize jquery for extension load
$(function(){
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
           			console.log(response);
					$("#txtResponse").text(response.detail).css({ 'color': 'red'});
					$("#txtResponse1").text(response.detail2).css({ 'color': 'black'});
					$("#txtResponse2").text(" ").css({ 'color': 'black'});
					$("#txtResponse3").text(" ").css({ 'color': 'black'});
					$("#txtResponse4").text(" ").css({ 'color': 'black'});
					$("#txtResponse5").text(" ").css({ 'color': 'black'});
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
           			console.log(response);
					$("#txtResponse").text(response.org).css({ 'color': 'red'});
					$("#txtResponse1").text(response.org2).css({ 'color': 'black'});
					$("#txtResponse2").text(response.per).css({ 'color': 'red'});
					$("#txtResponse3").text(response.per2).css({ 'color': 'black'});
					$("#txtResponse4").text(response.loc).css({ 'color': 'red'});
					$("#txtResponse5").text(response.loc2).css({ 'color': 'black'});
        		}
    		});
  		});		
	});

	$("#btnDo2").click(function(e){
		chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
			let taburl = tabs[0].url;
			console.log("URL: "+taburl);
			
    		// make ajax request to our server
    		$.ajax({
        		url: "http://localhost:5000/api/fetch3",
        		type: "post",
        		data: taburl,
        		contentType: "application/json",
        		success: function (response) {
           			console.log(response);
					$("#txtResponse").text(response.detail).css({ 'color': 'black'});
        		}
    		});
  		});		
	});

	$("#btnDo3").click(function(e){
		chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
			let taburl = tabs[0].url;
			console.log("URL: "+taburl);
			
    		// make ajax request to our server
    		$.ajax({
        		url: "http://localhost:5000/api/fetch4",
        		type: "post",
        		data: taburl,
        		contentType: "application/json",
        		success: function (response) {
           			console.log(response);
					$("#txtResponse").text(response.detail).css({ 'color': 'black'});
        		}
    		});
  		});		
	});
	$("#btnDo4").click(function(e){
		chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
			let taburl = tabs[0].url;
			console.log("URL: "+taburl);
			
    		// make ajax request to our server
    		$.ajax({
        		url: "http://localhost:5000/api/fetch5",
        		type: "post",
        		data: taburl,
        		contentType: "application/json",
        		success: function (response) {
           			console.log(response);
					$("#txtResponse").text(response.detail).css({ 'color': 'black'});
        		}
    		});
  		});		
	});
});

