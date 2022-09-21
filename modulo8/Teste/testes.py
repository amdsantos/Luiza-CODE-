import json

def exception_example():
    string_json = '{"message": "Olá Mundo!""}'
    
    try:
        object = json.loads(string_json)
        print(json.dumps(object))
    except Exception as err:
        print(f"Erro capturado: {err}")
        
exception_example()