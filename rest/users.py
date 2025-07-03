import requests
api_url = "https://jsonplaceholder.typicode.com/users"

def list():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching users: {response.status_code} - {response.text}")

def create(dados):
    response = requests.post(api_url, json=dados)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Error creating user: {response.status_code} - {response.text}")
        
def read(user_id=None):
    if user_id:
        response = requests.get(f"{api_url}/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching user {user_id}: {response.status_code} - {response.text}")
    else:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching users: {response.status_code} - {response.text}")

def update(user_id, dados):
    response = requests.put(f"{api_url}/{user_id}", json=dados)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error updating user {user_id}: {response.status_code} - {response.text}")
def delete(user_id):   
    response = requests.delete(f"{api_url}/{user_id}")
    if response.status_code == 200:
        return {"message": "Usuario deletado com sucesso!"}
    elif response.status_code == 400:
        return {"message": "Erro ao deletar o usuário!"}
    elif response.status_code == 404:
        return {"message": "Usuario não encontrado!"}

    else:
        raise Exception(f"Error deleting user {user_id}: {response.status_code} - {response.text}")

