//very crude pitch detection
// created by datramnt https://editor.p5js.org/datramt/sketches/rkC5INGBQ

// source mic audio from browser source
let mic;
let fft;
let energies = [];
// adding vars for chroma key value and mousePressed Function
let r, g, b;
let chroma = "0,177,64";

function setup() {
  createCanvas(800, 400);
  mic = new p5.AudioIn();
  mic.start();
  fft = new p5.FFT();
  fft.setInput(mic);
  noStroke();
  fill("red");
}

// changes color of spectrum on mouse-click
function mousePressed() {
  r = random(255);
  g = random(255);
  b = random(255);
}

function draw() {
  background(chroma);
  fill(r, g, b);
  let spectrum = fft.analyze();

  for (let i = 0; i < 127; i++) {
    energies[i] = fft.getEnergy(midiToFreq(i));
  }

  //at what index of energies is the max?
  let indexOfMaxValue = indexOfMax(energies);

  // console.log(indexOfMaxValue)

  beginShape();
  vertex(0, height);
  for (let i = 0; i < energies.length; i++) {
    vertex((i * width) / energies.length, height - energies[i]);
  }
  vertex(width, height);
  endShape();

  let micLevel = mic.getLevel();
  // hiding mic audio circle reference
  //fill('red');-
  //ellipse(indexOfMaxValue*width/127, constrain(height-micLevel*height*5, 0, height), 30);
}

function indexOfMax(arr) {
  if (arr.length === 0) {
    return -1;
  }

  var max = arr[0];
  var maxIndex = 0;

  for (var i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      maxIndex = i;
      max = arr[i];
    }
  }

  return maxIndex;
}
