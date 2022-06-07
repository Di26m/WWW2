// function info(word1) {
//   console.log(word1 + "!");
//   // console.log("!");
// }
//
// function summa(a, b) {
//   var res = a + b;
//   info(res);
// }
// summa(5,7);

// function summa(arr) {
//   var sum = 0;
//   for (var i = 0; i < arr.length; i++)
//     sum += arr[i]
// return sum;
// }
// var array = [6, 8, 1];
// var array_2 = [6, 8, 1, 7];
// var array_3 = [6, 8, 1, 90];
//
// var res = summa(array);
// res *= 2;
// console.log("Результат: " + res);
// summa(array_2);
// summa(array_3);

var num = 10; // - глобальная переменная

function info() {
  var num = 20; // - локальна переменная (работает только внутри функции)
  console.log(num);
}

info();
console.log(num);
