// let arr = [8, 90, 0, 5, 7, 8, 9, 22];
// // console.log(arr.join("|| "));
// // console.log(arr.sort());
// // console.log(arr.reverse().join(", "));
// let stroka = arr.reverse().join(", ");
//
// console.log(stroka.split(", "));
// ---------------------------------------

class Person {
    constructor(name, age, happiness) {
      this.name = name;
      this.age = age;
      this.happiness = happiness;

  }
  info() {
    console.log("Человек:" + this.name + ". Возраст: " + this.age);
  }
}

var alex = new Person('Alex', 45, true);
var bob = new Person('Bob', 25, false);

alex.name = 'alex2';
// console.log(alex.name);
// console.log(alex.age);
// console.log(bob.name);
alex.info();
bob.info();
