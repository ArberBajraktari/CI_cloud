from app import app # Flask instance of the API

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'No request is made' in response.data


def test_output_var():
    response = app.test_client().get('/<output>')
    assert response.status_code == 200
    assert b'output' in response.data