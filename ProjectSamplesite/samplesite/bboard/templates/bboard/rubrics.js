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
