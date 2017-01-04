var numRows = 100; //500;
var numCols = 250; //800;

function getInitState(numRows, numCols) {
   var state = [];
   for (var i = 0; i < numRows; i++) {
      var row = [];
      for (var j = 0; j < numCols; j++) {
         row.push(false);
      }
      state.push(row);
   }
   return state;
}

function drawInitHtml(state) {

   var contentData = '';

   for (var i in state) {
      var rowState = state[i];
      var rowHtml = "<div class='row'>";

      for (var j in rowState) {
         var pixStat = rowState[j];
         var pixId = 'pix-' + i + '-' + j;
         var pix = "<div class='pix' id='" + pixId + "'>&nbsp;</div>";
         rowHtml += pix;
      }
      rowHtml += '</div>';

      contentData += rowHtml;
   }

   //return contentData;
   $('#content').html(contentData);

}

function initMouseDown() {
   var mouseDown = 0;
   document.body.onmousedown = function() {
       mouseDown = 1;
   }
   document.body.onmouseup = function() {
       mouseDown = 0;
   }

}

function init() {

   var content = $('#content');

   var initState = getInitState(numRows, numCols);

   drawInitHtml(initState);


   $('.pix').each(function() {
      $(this).click(function() {
         $(this).css('background-color', 'white');
      });
   });

}

$(function() {
   init();
});

