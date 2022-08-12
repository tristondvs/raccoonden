var r, g, b;
var mic;

r = 255;
g = 0;
b = 0;

function setup() {
  createCanvas(500, 500);

  mic = new p5.AudioIn();
  mic.start();
}

function draw() {
  var micLevel = mic.getLevel();
  background(220);
  fill(r, g, b);
  ellipse(250, 250, 50 + micLevel * 2000);
}

function mousePressed() {
  r = random(256);
  g = random(256);
  b = random(256);
}