import copy
import data
import sender_stand_request

#Creación de un nuevo usuario
def get_kit_body(name):
    current_body = copy.deepcopy(data.kit_body)
    current_body["name"] = name
    return current_body

#Solicitud para verificar la respuesta exitosa al crear un nuevo kit
def positive_assert(kit_body):
    token = sender_stand_request.get_user_token()
    response = sender_stand_request.post_new_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def  negative_assert_code_400(kit_body):
    token = sender_stand_request.get_user_token()
    response = sender_stand_request.post_new_kit(kit_body, token)
    assert response.status_code == 400

#Prueba 1: Creación de un kit con nombre de un caracter
def test_create_kit_name_1char():
    positive_assert(get_kit_body('a'))

#Prueba 2: Creación de un kit con un nombre de 511 caracteres
def test_create_kit_name_511char():
    positive_assert(get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC'))

#Prueba 3: Creación de un kit con 0 caracteres
def test_create_kit_name_0char():
    negative_assert_code_400(get_kit_body(''))

#Prueba 4: Creación de un kit con 512 caracteres
def test_create_kit_name_512char():
    negative_assert_code_400(get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD'))

#Prueba 5: Creación de un kit con caracteres especiales
def test_create_kit_name_spchar():
    positive_assert(get_kit_body('#$"#$%%&&'))

#Prueba 6: Creación de un kit con un nombre con espacios
def test_create_kit_name_spacechar():
    positive_assert(get_kit_body('A Aaaa'))

#Prueba 7: Creación de un kit con números en el nombre
def test_create_kit_name_numchar():
    kit_body = get_kit_body('123')
    positive_assert(get_kit_body('123'))

#Prueba 8: Creación de un kit sin campo name
def test_create_kit_name_noname():
    token = sender_stand_request.get_user_token()
    response = sender_stand_request.post_new_kit({}, token)
    negative_assert_code_400(response.json())

#Prueba 9: Creación de un kit con un nombre con string
def test_create_kit_name_strname():
    kit_body = copy.deepcopy(data.kit_body)
    kit_body["name"] = '123'
    positive_assert(kit_body)
