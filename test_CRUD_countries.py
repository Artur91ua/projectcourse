import requests
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api/countries"


def payload():
    return """<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <country>
        <id_zone xlink:href="http://164.92.218.36:8080/api/zones/8">7</id_zone>
        <id_currency>5</id_currency>
        <call_prefix>3890</call_prefix>
        <iso_code>TES</iso_code>
        <active></active>
        <contains_states>0</contains_states>
        <need_identification_number>1</need_identification_number>
        <need_zip_code>0</need_zip_code>
        <zip_code_format>000</zip_code_format>
        <display_tax_label>0</display_tax_label>
        <name>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Test1</language>
        </name>
    </country>
</prestashop>"""


def country_id(create_country_response):
    body = create_country_response.text
    country_id00 = body.split('</id>')
    country_id0 = country_id00[0].split('<id>')
    country_id = country_id0[1][9:-3]
    return country_id

def test_can_create_country():
    create_country_response = requests.post(ENDPOINT, auth=(key, ""), data=f'{payload()}')
    assert create_country_response.status_code == 201
    get_created_country_response = requests.get(ENDPOINT + f'/{country_id(create_country_response)}', auth=(key, ""))
    assert get_created_country_response.status_code == 200


def test_can_update_country():
    create_country_response = requests.post(ENDPOINT, auth=(key, ""), data=f'{payload()}')
    assert create_country_response.status_code == 201
    new_country_payload = f"""
    <country>
        <id_zone xlink:href="http://164.92.218.36:8080/api/zones/8">7</id_zone>
        <id_currency>5</id_currency>
        <call_prefix>3890991</call_prefix>
        <iso_code>TES</iso_code>
        <active></active>
        <contains_states>0</contains_states>
        <need_identification_number>1</need_identification_number>
        <need_zip_code>0</need_zip_code>
        <zip_code_format>000</zip_code_format>
        <display_tax_label>0</display_tax_label>
        <name>
        <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Test_county_T</language>
        </name>
    </country>
</prestashop>"""
    update_country_response = requests.put(ENDPOINT + f'/{country_id(create_country_response)}', auth=(key, ""), data=new_country_payload)
    assert update_country_response.status_code == 405



def test_can_delete_country():
    create_country_response = requests.post(ENDPOINT, auth=(key, ""), data=f'{payload()}')
    assert create_country_response.status_code == 201
    get_created_country_response = requests.get(ENDPOINT + f'/{country_id(create_country_response)}', auth=(key, ""))
    assert get_created_country_response.status_code == 200
    delete_country_response = requests.delete(ENDPOINT + f'/{country_id(create_country_response)}', auth=(key, ""))
    assert delete_country_response.status_code == 405
    get_created_country_response = requests.get(ENDPOINT + f'/{country_id(create_country_response)}', auth=(key, ""))
    assert get_created_country_response.status_code == 200
