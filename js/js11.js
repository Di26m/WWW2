var counter = 0
function onClickButton(el) {
  counter++;
  el.innerHTML = "вы нажали на кнопку:" + counter;
  el.style.background = "red";
  el.style.color = "blue";
  el.style.cssText = "border-radius: 5px; border: 10px; font-size: 20 px";
}
function onInput(el) {
  if (el.value=="Hello") {
    alert("И тебе привет!")
  }
  console.log(el.value);
}
