HTML_MAIN = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>模块选择</title>
    <style>
        body {{
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }}

        h1 {{
            color: rgb(255, 173, 49);
            font-size: 40px;
            text-align: center;
            margin-top: 20px;
        }}

        p {{
            font-size: 20px;
            color: lightblue; /* 设置颜色为淡蓝色 */
        }}

        .container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            height: 60vh;
        }}

        .square {{
            width: 125px; /* 调整模块宽度 */
            height: 125px; /* 调整模块高度 */
            margin: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            border: 2px solid #fff;
            transition: background-color 0.3s ease;
        }}

        .square:hover, .square:active {{
            background-color: rgba(60, 255, 174, 0.558);
        }}
    </style>
</head>
<body>

<h1>模块选择</h1>

<div class="container">
    {items}
    <!-- Add more squares as needed -->
</div>

<script>
    function navigateToPage(pageUrl) {{
        window.location.href = pageUrl;
    }}
</script>

</body>
</html>

'''

HTML_ITME = '''
    <div class="square" onclick="navigateToPage('{url}')"><p>{name}</p></div>

'''

from config import active_modules


def generate_home_html(print_mod_info: bool = True) -> None:
    if print_mod_info:
        print('----------------------')
        print('已加载的MOD:')

    items = ''
    for each in active_modules:
        items += HTML_ITME.format(url = each.get_url_prefix(), name = each.get_name())

        if print_mod_info:
            print(each)
        
    if print_mod_info:
        print('----------------------')

    html = HTML_MAIN.format(items = items)
    with open('modules\\master\\templates\\home.html', 'w', encoding='utf-8') as f:
        f.write(html)