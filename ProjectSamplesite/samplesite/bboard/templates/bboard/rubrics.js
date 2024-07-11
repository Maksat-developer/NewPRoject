const domain = 'http://localhost:8000/';
let list = document.getElementById('list');

let listLoader = new XMLHttpRequest();

listLoader.addEventListener('readystatechange', () => {
    if (listLoader.readyState == 4) {
        if (listLoader.status == 200) {
            let data = JSON.parse(listLoader.responseText);
            let s = '<ul>';
            for (let i = 0; i < data.length; i++) {
                let d = data[i];
                s += `<li>${d.name} <a href="${domain}api/rubrics/${d.id}/" class="detail">Вывести</a></li>`; // Исправлено форматирование строки
            }
            s += '</ul>';
            list.innerHTML = s;

            // Исправлено получение ссылок и добавление слушателей
            let links = document.querySelectorAll('ul li a.detail');
            links.forEach((link) => {
                link.addEventListener('click', (event) => {
                    event.preventDefault(); // Предотвратить переход по ссылке
                    rubricLoad(event); // Вызов функции rubricLoad для обработки клика (предполагается, что эта функция существует)
                });
            });
        } else {
            window.alert(listLoader.statusText);
        }
    }
});

function listLoad() {
    listLoader.open('GET', domain + 'api/rubrics/', true);
    listLoader.send();
}

listLoad(); // Вызов функции для загрузки списка


let id = document.getElementById('id'); // Исправлено getElementByld на getElementById и исправлены типы кавычек
let name = document.getElementById('name'); // То же самое
let rubricLoader = new XMLHttpRequest();

rubricLoader.addEventListener('readystatechange', () => {
    if (rubricLoader.readyState == 4) {
        if (rubricLoader.status == 200) {
            let data = JSON.parse(rubricLoader.responseText);
            id.value = data.id;
            name.value = data.name;
        } else {
            window.alert(rubricLoader.statusText);
        }
    }
});

function rubricLoad(evt) {
    evt.preventDefault(); // Предотвратить действие по умолчанию (переход по ссылке)
    rubricLoader.open('GET', evt.target.href, true);
    rubricLoader.send();
}



let rubricUpdater = new XMLHttpRequest();

rubricUpdater.addEventListener('readystatechange', function() {
  if (rubricUpdater.readyState == 4) {
    if (rubricUpdater.status == 200 || rubricUpdater.status == 201) {
      listLoad();
      name.form.reset();
      id.value = ''; // Corrected the quotes
    } else {
      window.alert(rubricUpdater.statusText);
    }
  }
});

// Assuming 'name' and 'id' are defined elsewhere in your code as form input elements
name.form.addEventListener('submit', function(evt) { // Corrected the quote
  evt.preventDefault();
  let vid = id.value, url, method;
  if (vid) {
    url = 'api/rubrics/' + vid + '/'; // Corrected the quotes
    method = 'PUT';
  } else {
    url = 'api/rubrics/'; // Corrected the quotes
    method = 'POST';
  }
  let data = JSON.stringify({id: vid, name: name.value});
  rubricUpdater.open(method, domain + url, true); // Assuming 'domain' is defined
  rubricUpdater.setRequestHeader('Content-Type', 'application/json'); // Corrected the method call
  rubricUpdater.send(data);
});



listLoader.addEventListener('readystatechange', function() {
  if (listLoader.readyState == 4) {
    if (listLoader.status == 200) {
      // Assuming 'data' is fetched and parsed from the response. This part is not shown.
      let s = ''; // Initialize an empty string to accumulate HTML
      for (let i = 0; i < data.length; i++) {
        let d = data[i];
        s += '<li>' + d.name + ' <a href="' + domain + 'api/rubrics/' + d.id + '/" class="detail">Вывести</a> <a href="' + domain + 'api/rubrics/' + d.id + '/" class="delete">Удалить</a></li>';
      }
      // Assuming 'list' is a defined variable pointing to an element where the list should be displayed.
      list.innerHTML = s; // Append the accumulated HTML to the list element

      let links = document.querySelectorAll('ul li a.delete'); // Correct the querySelectorAll call
      links.forEach(function(link) {
        link.addEventListener('click', rubricDelete); // Ensure 'rubricDelete' is defined
      });
    } else {
      // Handle other statuses or errors
      console.error("Failed to load data: " + listLoader.statusText);
    }
  }
});
