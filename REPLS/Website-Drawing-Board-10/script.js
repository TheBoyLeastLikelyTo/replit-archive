// Retrieve the HTML elements
var canvas = document.getElementById("theCanvas");
var button = document.getElementById("clear");
// Create a reference to the canvas's context
var context = canvas.getContext("2d");

// Variable for keeping track if 
// "onmousemove" should be drawing.
var drawing = false;

// Set the canvas's dimensions 
// [Don't do this in CSS]
canvas.width = 500;
canvas.height = 300;

// Sets the color of the squares 
// that will be made
context.fillStyle = "red";

/////////////////////////////////

// onmousedown event; The 'e' parameter
// is a basic JQuery event 
// argument that let's it retrieve 
// the mouse position.
canvas.onmousedown = function(e) {
  // Setting 'drawing' to true allows
  // the onmousemove event to make rectangles
  drawing = true;
  
  // This makes the Rectangles
  // The first two parameters set the origin
  // The last two are the size
  context.fillRect(e.pageX - this.offsetLeft,
                   e.pageY - this.offsetTop, 
                   10, 
                   10
                  );
  // e.pageX is the mouse data from the
  // event argument parameter.
  
  // this.offsetLeft and Top need to be
  // subtracted from pageX and Y to account
  // for margins/scrollbars/etc.
}

canvas.onmousemove = function(e) {
  if (drawing) { 
    // Called every process loop
    // But only draws if the mouse was clicked
    context.fillRect(e.pageX - this.offsetLeft, 
                     e.pageY - this.offsetTop, 
                     10, 
                     10
                    );
  }
}

// The onmouseup event then resets the
// 'drawing' bool so squares stop being made
// once the mouse has been released
canvas.onmouseup = function(){
  drawing = false;
}

////////////////////////////////

// Button to clear the canvas. Haven't figured
// out how to make the canvas return to a transparent
// state
button.onclick = function(){
  context.clearRect(0, 0, canvas.width, canvas.height);
}



/*
  Fun fact: The gaps in between the squares
  depend on the speed of the mouse
  as well as the speed of your computer's
  processor. As the browser is creating a
  square where ever the mouse is at the
  start of the next process cycle.
  
  Your students will inevitably ask about this.
*/
