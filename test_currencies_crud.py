import requests
import string
import random
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api/currencies"

#generate iso_id
def iso_id():
    letters = string.ascii_uppercase
    iso_id =''.join(random.choice(letters) for i in range(3))
    return iso_id
    
#define payload
def payload():
    return f"""<prestashop>
        <currency>
        <id></id>
        <names>
            <language id="1">yevro</language>
        </names>
        <name notFilterable="true">Yevr</name>
        <symbol>
            <language id="1"></language>
        </symbol>
        <iso_code>{iso_id()}</iso_code>
        <numeric_iso_code>407</numeric_iso_code>
        <precision>2</precision>
        <conversion_rate>0.027072</conversion_rate>
        <deleted></deleted>
        <active>1</active>
        <unofficial></unofficial>
        <modified></modified>
        <pattern>
            <language id="1"></language>
        </pattern>
        </currency>
        </prestashop>"""

#find currency id        
def currency_id(create_currency_response):
    #pull text from the response, split it and slice to get id separated from the CDATA 
    currency_id = create_currency_response.text.split('</id>')[0].split('<id>')[1][9:-3]
    return currency_id
    
#get currencies
def test_can_get_currencies():
    response = requests.get(ENDPOINT, auth = (key,""))
    assert response.status_code == 200

#create new currency
def test_can_create_currency():
    create_currency_response = requests.post(ENDPOINT, auth = (key,""), data = f'{payload()}')
    assert create_currency_response.status_code == 201
    get_created_currency_response = requests.get(ENDPOINT + f'/{currency_id(create_currency_response)}', auth=(key,""))
    assert get_created_currency_response.status_code == 200
    print(get_created_currency_response.text)
 
#update currency 
def test_can_update_currency():
    create_currency_response = requests.post(ENDPOINT, auth = (key,""), data = f'{payload()}')
    assert create_currency_response.status_code == 201
    new_currency_payload = f"""<prestashop>
        <currency>
        <id>{currency_id(create_currency_response)}</id>
        <names>
            <language id="1">yevro</language>
        </names>
        <name notFilterable="true">Yevr</name>
        <symbol>
            <language id="1"></language>
        </symbol>
        <iso_code>{iso_id()}</iso_code>
        <numeric_iso_code>407</numeric_iso_code>
        <precision>2</precision>
        <conversion_rate>0.027072</conversion_rate>
        <deleted></deleted>
        <active>1</active>
        <unofficial></unofficial>
        <modified></modified>
        <pattern>
            <language id="1"></language>
        </pattern>
        </currency>
        </prestashop>"""
    update_currency_response = requests.put(ENDPOINT + f'/{currency_id(create_currency_response)}', auth=(key,""), data = new_currency_payload)
    assert update_currency_response.status_code == 405

#delete currency    
def test_can_delete_currency():
    create_currency_response = requests.post(ENDPOINT, auth = (key,""), data = f'{payload()}')
    assert create_currency_response.status_code == 201
    delete_currency_response = requests.delete(ENDPOINT + f'/{currency_id(create_currency_response)}', auth=(key,""))
    assert delete_currency_response.status_code == 405