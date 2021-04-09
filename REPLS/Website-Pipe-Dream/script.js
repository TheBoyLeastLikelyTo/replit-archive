$(function)() {

var levels = new Array {
  "map": [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]],
  "counts": [0,3,1,0,0,1],
  "starts": [2,0]
  "startDir": "R"
  "endSide":"right"
  }
}
var currentLvl = 1;
var levelName = "level"+currentLvl;
});

  initialize();

 function initialize(){
  $("#title").html("Connect the Pipes");
  // initialize the drop zone's size and position
  $("#drop-zone").empty();
  var width = levels[levelName].map[0].length * 4;
  var height = levels[levelName].map.length * 4;
 $("#drop-zone").css({
 "width": width+"rem",
 "height": height+"rem",
 "margin-left": (24-width)/2+"rem",
 "margin-top": (24-height)/2+"rem"
 });
 // create the grid
 for(var i = 0; i < levels[levelName].map.length;i++){
for(var j = 0; j < levels[levelName].map[i].length; j++){
 var id = i+"_"+j
 $("#drop-zone").append("<div id ='"+id+"'"+
 "class='pipe'>"+
 "<div class='p"+
levels[levelName].map[i][j]+
 "'></div></div>");
 }
 }
 // create the start wall
  var r = levels[levelName].start[0];
  var c = levels[levelName].start[1];
  $("#"+r+"_"+c).css("border-"+levels[levelName].startSide+"-color",
"blue");
  // create the end wall
  r = levels[levelName].end[0];
  c = levels[levelName].end[1];
  $("#"+r+"_"+c).css("border-"+levels[levelName].endSide+"-color",
"red");
 }
});





  