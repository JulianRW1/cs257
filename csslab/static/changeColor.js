function changeColor() {
  the_heading = document.getElementById("textToChange");

  let colors = ["red", "orange", "yellow", "green", "blue", "purple"];
  let color = colors[Math.floor(Math.random()*colors.length)];
  the_heading.style.color = "red";

  console.log("I just changed the color to: " + the_heading.style.color); 
}
