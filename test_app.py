from app import app

def test_hello():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert 'Hello from CI/CD' in str(resp.data)

def test_health():
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    assert b'ok' in resp.data
