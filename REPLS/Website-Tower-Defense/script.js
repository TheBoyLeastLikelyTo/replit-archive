var canvas = document.getElementById("main");
var ctx = canvas.getContext("2d");
var ranges = document.getElementById("toggleRanges");
var colors = ["#ff0000", '#00ffff', "#00ff00", "#ffa31a", "#ffb3ff"];
var enemies = [];
var towers = [];
var shots = [];
var health = 200;
var score = 0;
var level = 1;
var showRange = true;
var time = 0;
var timeout = 200;
var count = 0;
var roundMobs = 2; // To the level power


var turns = [[220,120],[220,420],[390,420],[390,120],[canvas.width+10,120]];
var spawntime = 20;

var roundMobs = Math.pow(2,level);
setInterval(updateGame,30);

function getDistance(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
}

function getXYSpeed(speed, startX, startY, endX, endY) {
    var distance = getDistance(startX, startY, endX, endY);
    var xDiff = endX - startX;
    var yDiff = endY - startY;
    return [speed * (xDiff / distance), speed * (yDiff / distance)];
}

function enemy(hits) {
    this.x = -20;
    this.y = 120;
    this.dx = 2 + hits;
    this.dy = 0;
    this.hits = hits;
    this.progress = 0;
    this.nextTurn = 0;

    this.updatePosition = function () {
        this.progress += Math.abs(this.dx) + Math.abs(this.dy);
        this.draw();
        if(this.checkTurn()){
            health -= this.hits+1;
            return true;
        }
        this.x += this.dx;
        this.y += this.dy;
    };

    this.draw = function() {
        ctx.beginPath();
        ctx.fillStyle = colors[this.hits];
        ctx.arc(this.x, this.y, 10, 0, 2*Math.PI);
        ctx.fill();
        ctx.lineWidth = 1;
        ctx.strokeStyle = "black";
        ctx.stroke();
        ctx.closePath();
    };

    this.checkTurn = function() {
        var distance = getDistance(this.x, this.y, turns[this.nextTurn][0], turns[this.nextTurn][1]);
        if (distance <= 5) {
            this.nextTurn++
            if (this.nextTurn == turns.length) {
              return true
            }
            this.changeSpeed{}            }
        }
    };
    this.changeSpeed == function({
      var newSpeed = 
    })
}
