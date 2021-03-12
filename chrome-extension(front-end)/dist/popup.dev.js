"use strict";

//Initialize jquery for extension load
$(function () {
  //Setup event listener on button
  $("#btnTerm").click(function (e) {
    chrome.tabs.query({
      active: true,
      lastFocusedWindow: true
    }, function (tabs) {
      var taburl = tabs[0].url;
      $.ajax({
        url: "http://localhost:5000/api/fetch",
        type: "post",
        data: taburl,
        contentType: "application/json",
        success: function success(response) {
          console.log(response);
          $("#txtResponse").text(response.detail).css({
            'color': "maroon"
          });
          $("#txtResponse1").text(response.detail2).css({
            'color': 'black'
          });
          $("#txtResponse2").text(" ");
          $("#txtResponse3").text(" ");
          $("#txtResponse4").text(" ");
          $("#txtResponse5").text(" ");
        }
      });
    });
  });
  $("#btnNer").click(function (e) {
    chrome.tabs.query({
      active: true,
      lastFocusedWindow: true
    }, function (tabs) {
      var taburl = tabs[0].url;
      $.ajax({
        url: "http://localhost:5000/api/fetch2",
        type: "post",
        data: taburl,
        contentType: "application/json",
        success: function success(response) {
          console.log(response);
          $("#txtResponse").text(response.org).css({
            'color': 'maroon'
          });
          $("#txtResponse1").text(response.org2).css({
            'color': 'black'
          });
          $("#txtResponse2").text(response.per).css({
            'color': 'maroon'
          });
          $("#txtResponse3").text(response.per2).css({
            'color': 'black'
          });
          $("#txtResponse4").text(response.loc).css({
            'color': 'maroon'
          });
          $("#txtResponse5").text(response.loc2).css({
            'color': 'black'
          });
        }
      });
    });
  });
  $("#btnHeap").click(function (e) {
    chrome.tabs.query({
      active: true,
      lastFocusedWindow: true
    }, function (tabs) {
      var taburl = tabs[0].url;
      $.ajax({
        url: "http://localhost:5000/api/fetch3",
        type: "post",
        data: taburl,
        contentType: "application/json",
        success: function success(response) {
          console.log(response);
          $("#txtResponse").text(response.detail).css({
            'color': 'black'
          });
        }
      });
    });
  });
  $("#btnCon").click(function (e) {
    chrome.tabs.query({
      active: true,
      lastFocusedWindow: true
    }, function (tabs) {
      var taburl = tabs[0].url;
      $.ajax({
        url: "http://localhost:5000/api/fetch4",
        type: "post",
        data: taburl,
        contentType: "application/json",
        success: function success(response) {
          console.log(response);
          $("#txtResponse").text(response.detail).css({
            'color': 'black'
          });
          $("#txtResponse1").text(" ");
          $("#txtResponse2").text(" ");
          $("#txtResponse3").text(" ");
          $("#txtResponse4").text(" ");
          $("#txtResponse5").text(" ");
        }
      });
    });
  });
  $("#btnWord").click(function (e) {
    chrome.tabs.query({
      active: true,
      lastFocusedWindow: true
    }, function (tabs) {
      var taburl = tabs[0].url;
      $.ajax({
        url: "http://localhost:5000/api/fetch5",
        type: "post",
        data: taburl,
        contentType: "application/json",
        success: function success(response) {
          console.log(response);
          $("#txtResponse").text(response.detail).css({
            'color': 'black'
          });
        }
      });
    });
  });
  $("#btnSum").click(function (e) {
    SentNum = prompt("How many sentences do you want? (Please wait while it loads)");
    chrome.tabs.query({
      active: true,
      lastFocusedWindow: true
    }, function (tabs) {
      var taburl = tabs[0].url;
      dict2 = {
        taburl: taburl,
        SentNum: SentNum
      };
      $.ajax({
        url: "http://localhost:5000/api/fetch6",
        type: "post",
        data: JSON.stringify(dict2),
        contentType: "application/json",
        success: function success(response) {
          $("#txtResponse").text("");
          $("#txtResponse1").text(response.detail).css({
            'color': 'black'
          });
        }
      });
    });
  });
});