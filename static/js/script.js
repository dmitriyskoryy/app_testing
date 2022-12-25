

function checkType(node) {
    const input = document.querySelector('.list_answer input').value = node.value;
}

//    num_page = document.querySelector('.push_back input');
//    result_answer[num_page.value] = node.value
//
//
//    localStorage.setItem('result_test', result_answer);
//
//    key_storage = localStorage.getItem('result_test');
//    console.log('localStorage: ', JSON.stringify(key_storage));
//
//    let jso = JSON.stringify(key_storage);
//    alert(jso);



//const input = document.querySelector('.input-container input');
//const radio = document.querySelector('.list_answer input');
//radio.addEventListener('click', function(e)) {
//    console.log("asdfasdfasdf");
//});

//
//const btn = document.querySelector('.push_back');
//btn.addEventListener('click', () => {
//
//    const options = {
//    // Будем использовать метод POST
//    method: 'POST',
//    // Добавим тело запроса
//    body: JSON.stringify({
//      answerajax: 'foo',
//    }),
//    // Дополнительный заголовое с описанием типа данных,
//    // которые мы отправляем серверу. В данном случае
//    // сервер jsonplaceholder будет знать, как ему
//    // обрабатывать запрос
//    headers: {
//      "Content-type": "application/json; charset=UTF-8",
//      "X-CSRFToken": {{csrf_token}},
//    }
//  }
//  // Делаем запрос за данными
//  fetch('/', options)
//    .then(response => response.json())
//    .then(json => console.log(json))
//});