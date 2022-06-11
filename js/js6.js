var number = 15;
var isHasHouse = true;
// if (number == 15 && isHasHouse) - тоже самое if (number == 15 && isHasHouse == true )
// if (number == 15 && !isHasHouse) - тоже самое if (number == 15 && isHasHouse == false )
// && - и
// || - или
if (number == 15 && isHasHouse == true ) {
  // if (number == 15 && isHasHouse)
  console.log("Ok");
  console.log("Ok!");
} else if (number < 10) {
  console.log("Ok!");
} else if (number == 7) {
  console.log("7");
} else if (number > 15) {
  console.log(">= 15");
}
else {
  console.log("Else!");
}
