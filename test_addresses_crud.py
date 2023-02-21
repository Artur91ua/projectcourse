import requests
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api/addresses"

#define payload
def payload():
    return """<prestashop>
            <address>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country>1</id_country>
                <id_state></id_state>
                <alias>ksionz</alias>
                <company></company>
                <lastname>Shliakhta</lastname>
                <firstname>Olena</firstname>
                <vat_number></vat_number>
                <address1>Zalyvnyi 20</address1>
                <address2></address2>
                <postcode>37600</postcode>
                <city>Myrhorod</city>
                <other></other>
                <phone>661763661</phone>
                <phone_mobile>661763661</phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>"""

#find address id        
def address_id(create_address_response):
    #pull text from the response, split it and slice to get id separated from the CDATA 
    address_id = create_address_response.text.split('</id>')[0].split('<id>')[1][9:-3]
    return address_id

#create new address
def test_can_create_address():
    create_address_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_address_response.status_code == 201
    get_created_address_response = requests.get(ENDPOINT + f'/{address_id(create_address_response)}', auth=(key,""))
    assert get_created_address_response.status_code == 200

#update address
def test_can_update_address():
    create_address_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_address_response.status_code == 201
    new_address_payload = f"""<prestashop>
            <address>
                <id>{address_id(create_address_response)}</id>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country>1</id_country>
                <id_state></id_state>
                <alias>ksionz</alias>
                <company></company>
                <lastname>Shliakhta</lastname>
                <firstname>Olena</firstname>
                <vat_number></vat_number>
                <address1>Zalyvnyi 20</address1>
                <address2></address2>
                <postcode>37600</postcode>
                <city>Kharkiv</city>
                <other></other>
                <phone>661763661</phone>
                <phone_mobile>661763661</phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>"""
    update_address_response = requests.put(ENDPOINT + f'/{address_id(create_address_response)}', auth=(key,""), data = new_address_payload)
    assert update_address_response.status_code == 200
    get_updated_address_response = requests.get(ENDPOINT + f'/{address_id(create_address_response)}', auth=(key,""))
    assert get_updated_address_response.status_code == 200
    #find updated data in the body of the request
    new_body_city = new_address_payload.split('city>')[1][:-2]
    #find updated data in the body of the response
    updated_body_city = update_address_response.text.split('city>')[1][9:-5]
    assert updated_body_city == new_body_city

#delete address    
def test_can_delete_address():
    create_address_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_address_response.status_code == 201
    delete_address_response = requests.delete(ENDPOINT + f'/{address_id(create_address_response)}', auth=(key,""))
    assert delete_address_response.status_code == 200
    get_deleted_address_response = requests.get(ENDPOINT + f'/{address_id(create_address_response)}', auth=(key,""))
    assert get_deleted_address_response.status_code == 404