import requests
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api/categories"
#body payload
def payload():
    return """<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id></id>
        <id_parent></id_parent>
        <active>0</active>
        <id_shop_default></id_shop_default>
        <is_root_category></is_root_category>
        <position>AAAAAAAA</position>
        <date_add></date_add>
        <date_upd></date_upd>
        <name><language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Maps</language></name>
        <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </link_rewrite>
        <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </description>
        <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_title>
        <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_description>
        <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_keywords>
        <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
        </associations>
    </category>
</prestashop>"""
#find categories id
def categories_id(create_categories_response):
    categories_id = create_categories_response.text.split('</id>')[0].split('<id>')[1][9:-3]
    return categories_id
#create new categories
def test_can_create_categories():
    create_categories_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_categories_response.status_code == 201
    get_create_categories_response = requests.get(ENDPOINT + f'/{categories_id(create_categories_response)}', auth=(key,""))
    assert get_create_categories_response.status_code == 200
#update categories
def test_can_update_categories():
    create_categories_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_categories_response.status_code == 201
    new_categories_payload = f"""<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id>{categories_id(create_categories_response)}</id>
        <id_parent></id_parent>
        <active>0</active>
        <id_shop_default></id_shop_default>
        <is_root_category></is_root_category>
        <position>AAAAAAA</position>
        <date_add></date_add>
        <date_upd></date_upd>
        <name><language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Maps</language></name>
        <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </link_rewrite>
        <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </description>
        <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_title>
        <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_description>
        <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_keywords>
        <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
        </associations>
    </category>
</prestashop>"""
    update_categories_response = requests.put(ENDPOINT + f'/{categories_id(create_categories_response)}', auth=(key,""), data=new_categories_payload)
    assert update_categories_response.status_code == 405
#delete categories
def test_can_delete_categories():
    create_categories_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_categories_response.status_code == 201
    get_create_categories_response = requests.get(ENDPOINT + f'/{categories_id(create_categories_response)}', auth=(key,""))
    assert get_create_categories_response.status_code == 200
    delete_categories_response = requests.delete(ENDPOINT + f'/{categories_id(create_categories_response)}', auth=(key,""))
    assert delete_categories_response.status_code == 405


