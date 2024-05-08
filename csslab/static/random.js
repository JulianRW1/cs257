function generateBigNumber() {
  generateNumber(1, 10); 
}

function generateSmallNumber() {
  generateNumber(1, 10);
}

function generateNumber(min, max) {
  let num = getRandomInt(min, max);
  document.getElementById("randomNumberText").innerHTML = "The random number is " + num;
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max-min)) + min;
}
  