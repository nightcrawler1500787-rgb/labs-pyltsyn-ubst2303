import os

def create_files_with_encoding():
    # Создаем папки если их нет
    os.makedirs('flatpages/templates', exist_ok=True)
    os.makedirs('flatpages/static/css', exist_ok=True)
    
    # HTML для index.html
    index_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Главная страница</title>
</head>
<body>
    <h1>Привет, Мир!</h1>
    <h2>Это учебный сайт, с его помощью будут изучены технологии python/django, html/css.</h2>
    <h3>Как видите, здесь используются заголовки различных уровней.</h3>
    
    <p>Здесь есть маркированный список:</p>
    <h4>
        <ul>
            <li>Элемент 1;</li>
            <li>элемент 2;</li>
            <li>элемент 3;</li>
            <li>последний элемент.</li>
        </ul>
    </h4>
    
    <p>И нумерованный список:</p>
    <h4>
        <ol>
            <li>Элемент 1;</li>
            <li>элемент 2;</li>
            <li>элемент 3;</li>
            <li>последний элемент.</li>
        </ol>
    </h4>
    
    <p>И даже таблица:</p>
    <table style="border: 1px solid black; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="border: 1px solid black; padding: 5px;">Столбик 1</th>
                <th style="border: 1px solid black; padding: 5px;">Столбик 2</th>
                <th style="border: 1px solid black; padding: 5px;">Столбик 3</th>
                <th style="border: 1px solid black; padding: 5px;">Столбик 4</th>
                <th style="border: 1px solid black; padding: 5px;">Столбик 5</th>
                <th style="border: 1px solid black; padding: 5px;">Столбик 6</th>
            </tr>
        </thead>
        <tr>
            <td style="border: 1px solid black; padding: 5px;">Строка 1 Столбец 1</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 1 Столбец 2</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 1 Столбец 3</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 1 Столбец 4</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 1 Столбец 5</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 1 Столбец 6</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 5px;">Строка 2 Столбец 1</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 2 Столбец 2</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 2 Столбец 3</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 2 Столбец 4</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 2 Столбец 5</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 2 Столбец 6</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 5px;">Строка 3 Столбец 1</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 3 Столбец 2</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 3 Столбец 3</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 3 Столбец 4</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 3 Столбец 5</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 3 Столбец 6</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 5px;">Строка 4 Столбец 1</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 4 Столбец 2</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 4 Столбец 3</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 4 Столбец 4</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 4 Столбец 5</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 4 Столбец 6</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 5px;">Строка 5 Столбец 1</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 5 Столбец 2</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 5 Столбец 3</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 5 Столбец 4</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 5 Столбец 5</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 5 Столбец 6</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 5px;">Строка 6 Столбец 1</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 6 Столбец 2</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 6 Столбец 3</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 6 Столбец 4</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 6 Столбец 5</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 6 Столбец 6</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 5px;">Строка 7 Столбец 1</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 7 Столбец 2</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 7 Столбец 3</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 7 Столбец 4</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 7 Столбец 5</td>
            <td style="border: 1px solid black; padding: 5px;">Строка 7 Столбец 6</td>
        </tr>
    </table>
    
    <a href="/hello/">Перейти на страницу со стилями</a>
</body>
</html>'''
    
    # HTML для static_handler.html
    static_handler_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Страница со стилями</title>
    <link rel="stylesheet" href="/static/css/index.css">
</head>
<body>
    <h1>Привет, Мир!</h1>
    <h2>Это учебный сайт, с его помощью будут изучены технологии python/django, html/css.</h2>
    <h3>Как видите, здесь используются заголовки различных уровней.</h3>
    
    <p>Здесь есть маркированный список:</p>
    <h4>
        <ul>
            <li>Элемент 1;</li>
            <li>элемент 2;</li>
            <li>элемент 3;</li>
            <li>последний элемент.</li>
        </ul>
    </h4>
    
    <p>И нумерованный список:</p>
    <h4>
        <ol>
            <li>Элемент 1;</li>
            <li>элемент 2;</li>
            <li>элемент 3;</li>
            <li>последний элемент.</li>
        </ol>
    </h4>
    
    <p>И даже таблица:</p>
    <table>
        <thead>
            <tr>
                <th>Столбик 1</th>
                <th>Столбик 2</th>
                <th>Столбик 3</th>
                <th>Столбик 4</th>
                <th>Столбик 5</th>
                <th>Столбик 6</th>
            </tr>
        </thead>
        <tr>
            <td>Строка 1 Столбец 1</td>
            <td>Строка 1 Столбец 2</td>
            <td>Строка 1 Столбец 3</td>
            <td>Строка 1 Столбец 4</td>
            <td>Строка 1 Столбец 5</td>
            <td>Строка 1 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 2 Столбец 1</td>
            <td>Строка 2 Столбец 2</td>
            <td>Строка 2 Столбец 3</td>
            <td>Строка 2 Столбец 4</td>
            <td>Строка 2 Столбец 5</td>
            <td>Строка 2 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 3 Столбец 1</td>
            <td>Строка 3 Столбец 2</td>
            <td>Строка 3 Столбец 3</td>
            <td>Строка 3 Столбец 4</td>
            <td>Строка 3 Столбец 5</td>
            <td>Строка 3 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 4 Столбец 1</td>
            <td>Строка 4 Столбец 2</td>
            <td>Строка 4 Столбец 3</td>
            <td>Строка 4 Столбец 4</td>
            <td>Строка 4 Столбец 5</td>
            <td>Строка 4 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 5 Столбец 1</td>
            <td>Строка 5 Столбец 2</td>
            <td>Строка 5 Столбец 3</td>
            <td>Строка 5 Столбец 4</td>
            <td>Строка 5 Столбец 5</td>
            <td>Строка 5 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 6 Столбец 1</td>
            <td>Строка 6 Столбец 2</td>
            <td>Строка 6 Столбец 3</td>
            <td>Строка 6 Столбец 4</td>
            <td>Строка 6 Столбец 5</td>
            <td>Строка 6 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 7 Столбец 1</td>
            <td>Строка 7 Столбец 2</td>
            <td>Строка 7 Столбец 3</td>
            <td>Строка 7 Столбец 4</td>
            <td>Строка 7 Столбец 5</td>
            <td>Строка 7 Столбец 6</td>
        </tr>
    </table>
    
    <img src="/static/img/sample-image.jpg" alt="Пример изображения">
    
    <a href="/">Вернуться на главную</a>
</body>
</html>'''
    
    # CSS для index.css
    css_content = '''body {
    background: #1abc9c;
    font-family: Tahoma, Arial, sans-serif;
    color: #333;
    margin: 20px;
    line-height: 1.6;
}

h1 {
    font-family: "Times New Roman", Times, serif;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 30px;
}

h2 {
    color: #34495e;
    margin-top: 25px;
}

h3 {
    color: #16a085;
    font-style: italic;
}

h4 {
    font-size: 16px;
    color: #34495e;
    margin: 15px 0;
}

p {
    font-size: 18px;
    margin-bottom: 15px;
    font-weight: bold;
}

ul, ol {
    margin: 10px 0;
    padding-left: 30px;
}

li {
    margin-bottom: 5px;
}

table {
    border-collapse: collapse;
    width: 100%;
    border: 2px solid #2c3e50;
    margin: 20px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

table th {
    background-color: #34495e;
    color: white;
    padding: 12px;
    text-align: center;
    border: 1px solid #2c3e50;
    font-weight: bold;
}

table td {
    border: 1px solid #2c3e50;
    padding: 10px;
    text-align: center;
}

table tr:nth-child(even) {
    background-color: #ecf0f1;
}

table tr:nth-child(odd) {
    background-color: #ffffff;
}

table tr:hover {
    background-color: #d5dbdb;
}

img {
    height: 30px;
    width: auto;
    margin: 20px 0;
    display: block;
    border: 2px solid #34495e;
    border-radius: 5px;
}

a {
    color: #2c3e50;
    text-decoration: none;
    font-weight: bold;
}

a:hover {
    color: #e74c3c;
    text-decoration: underline;
}'''
    
    # Сохраняем файлы с UTF-8 кодировкой
    with open('flatpages/templates/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    with open('flatpages/templates/static_handler.html', 'w', encoding='utf-8') as f:
        f.write(static_handler_html)
    
    with open('flatpages/static/css/index.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print("✅ Все файлы созданы с кодировкой UTF-8")
    print("✅ index.html создан")
    print("✅ static_handler.html создан") 
    print("✅ index.css создан")

if __name__ == "__main__":
    create_files_with_encoding()
