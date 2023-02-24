import requests
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api/zones"

#define payload
def payload():
    return """<prestashop>
            <zone>
                <name>Australia</name>
                <active></active>
            </zone>
        </prestashop>"""

#find zone id        
def zone_id(create_zone_response):
    #pull text from the response, split it and slice to get id separated from the CDATA 
    zone_id = create_zone_response.text.split('</id>')[0].split('<id>')[1][9:-3]
    return zone_id

#get zones
def test_can_get_zones():
    response = requests.get(ENDPOINT, auth=(key,""))
    assert response.status_code == 200
    
#create new zone
def test_can_create_zone():
    create_zone_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_zone_response.status_code == 201
    get_created_zone_response = requests.get(ENDPOINT + f'/{zone_id(create_zone_response)}', auth=(key,""))
    assert get_created_zone_response.status_code == 200


#update zone
def test_can_update_zone():
    create_zone_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_zone_response.status_code == 201
    new_zone_payload = f"""<prestashop>
            <zone>
                <id>{zone_id(create_zone_response)}</id>
                <name>Atlantis</name>
                <active></active>
            </zone>
        </prestashop>"""
    update_zone_response = requests.put(ENDPOINT + f'/{zone_id(create_zone_response)}', auth=(key,""), data = new_zone_payload)
    assert update_zone_response.status_code == 405

#delete zone    
def test_can_delete_zone():
    create_zone_response = requests.post(ENDPOINT, auth=(key,""), data = f'{payload()}')
    assert create_zone_response.status_code == 201
    delete_zone_response = requests.delete(ENDPOINT + f'/{zone_id(create_zone_response)}', auth=(key,""))
    assert delete_zone_response.status_code == 405
    
