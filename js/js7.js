// Одномерный массив
var arr = [5, true, "stroka", 5.7, 0, -100];
// [] - массив
arr[3] = "word";
console.log(arr.length);

// Многомерный массив
var matrix = [
  [4,6,8],["stroka", 5.7],[0, -100]
];

matrix[1][0] = 90;
console.log(matrix);
