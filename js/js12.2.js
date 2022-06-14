document.getElementById('main-form').addEventListener("submit", checkForm);

function checkForm(event) {
  event.preventDefault();
  var el = document.getElementById('main-form');

  // var name = document.getElementById('name').value;
  var name = el.name.value;
  var pass = el.pass.value;
  var repass = el.repass.value;
  var state = el.state.value;

  var fail = "";
  // console.log(state  + " - " + pass + " - " + repass);
  if (name == "" || pass == "" || state == "")
    fail = "Заполните все поля";
  else if (name.length <= 1 || name.length > 20)
    fail = "Введите корректное имя";
  else if (pass != repass)
    fail = "Пароли не совпадают";
  else if (pass.split("&").length > 1)
    fail = "Не корректный пароль";

  if(fail != "")
    document.getElementById('error').innerHTML = fail;

    // return false;
   else {
    alert("Все данные корректно заполнены");
    window.location = 'https://itproger.com';
    // return true;
    // return false;
  }
  // return false;
}
