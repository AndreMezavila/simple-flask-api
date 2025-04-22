import requests

data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'message': 'Hello world!'
}

response = requests.post(' http://127.0.0.1:5000/students', json=data)

print(response.status_code)
print(response.json())