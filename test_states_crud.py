import requests
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api/states"
#body payload
def payload():
    return """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <state>
        <id></id>
        <id_zone xlink:href="http://164.92.218.36:8080/api/zones/1">1</id_zone>
        <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
        <iso_code>1</iso_code>
        <name>jojo</name>
        <active></active>  
    </state>
</prestashop>"""
#get states
def test_can_get_states():
    response = requests.get(ENDPOINT, auth=(key,""))
    assert response.status_code == 200
#find states id
def states_id(create_states_response):
    states_id = create_states_response.text.split('</id>')[0].split('<id>')[1][9:-3]
    return states_id
#create new states
def test_can_create_states():
    create_states_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_states_response.status_code == 201
    get_create_states_response = requests.get(ENDPOINT + f'/{states_id(create_states_response)}', auth=(key,""))
    assert get_create_states_response.status_code == 200
#update states
def test_can_update_states():
    create_states_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_states_response.status_code == 201
    new_states_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <state>
        <id>{states_id(create_states_response)}</id>
        <id_zone xlink:href="http://164.92.218.36:8080/api/zones/1">1</id_zone>
        <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
        <iso_code>1</iso_code>
        <name>jojo</name>
        <active></active>  
    </state>
</prestashop>"""
    update_states_response = requests.put(ENDPOINT + f'/{states_id(create_states_response)}', auth=(key,""), data=new_states_payload)
    assert update_states_response.status_code == 405
#delete states
def test_can_delete_states():
    create_states_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_states_response.status_code == 201
    get_create_states_response = requests.get(ENDPOINT + f'/{states_id(create_states_response)}', auth=(key,""))
    assert get_create_states_response.status_code == 200
    delete_states_response = requests.delete(ENDPOINT + f'/{states_id(create_states_response)}', auth=(key,""))
    assert delete_states_response.status_code == 405


