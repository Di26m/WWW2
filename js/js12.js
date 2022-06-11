var  text = document.getElementById('text');
text.title = "New text";
console.log(text.title);

text.style.color = "red";
text.style.backgroundColor = "blue";

text.innerHTML = "New<br>string";

// document.getElementById('text').style.color = "white";

//let spans = document.getElementsByTagName('span');
let spans = document.getElementsByClassName('simple-Text');
for (var i = 0; i < spans.length; i++) {
  console.log(spans[i].innerHTML);
}
