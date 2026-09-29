import requests
#testing the connection
def test_clickhouse_is_running():
    response = requests.get('http://localhost:8123/')    
    assert response.status_code == 200
    assert 'Ok.' in response.text

# creating a table in clickhouse database
def test_create_table():
    headers = {
        'X-ClickHouse-User': 'default',
        'X-ClickHouse-Key': 'qa_password'
    }

    drop_query = 'DROP TABLE IF EXISTS users'
    response = requests.post('http://localhost:8123/', data=drop_query, headers=headers)    
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id UInt32,
        name String,
        age UInt8
    ) ENGINE = MergeTree()
    ORDER BY id;
    '''
    response = requests.post('http://localhost:8123/', data=query, headers=headers)
    if response.status_code != 200:
        print(f"Database Error: {response.text}")
        
    assert response.status_code == 200

def test_insert_data():
    query = '''
    INSERT INTO users (id, name, age) VALUES 
    (1, 'Alice', 25),
    (2, 'Bob', 30);
    '''
    headers = {
        'X-ClickHouse-User': 'default',
        'X-ClickHouse-Key': 'qa_password'
    }
    
    response = requests.post('http://localhost:8123/', data=query, headers=headers)
    
    if response.status_code != 200:
        print(f"Database Error: {response.text}")
    assert response.status_code == 200

def test_retrieve_data():
    query = 'SELECT * FROM users ORDER BY id FORMAT JSON'    
    headers = {
        'X-ClickHouse-User': 'default',
        'X-ClickHouse-Key': 'qa_password'
    }    
    response = requests.post('http://localhost:8123/', data=query, headers=headers)
    assert response.status_code == 200
 
    response_data = response.json()

    #asserting if the table has 2 rows only.
    assert response_data['rows'] == 2

    # asserting the first user and its details
    first_user = response_data['data'][0]
    assert first_user['id'] == 1
    assert first_user['name'] == 'Alice'
    assert first_user['age'] == 25

    # asserting second user to be bob
    second_user = response_data['data'][1]
    assert second_user['name'] == 'Bob'