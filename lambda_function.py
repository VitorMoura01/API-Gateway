import json

def lambda_handler(event, context):
    try:
        if 'headers' in event and 'Authorization' in event['headers']:
            token = event['headers']['Authorization']

            if token == "Bearer " + str(valid_token):
                if 'body' in event and event['body']:
                    input_data = json.loads(event['body'])
                    return {
                        'statusCode': 200,
                        'body': json.dumps({"status": "recebido com sucesso", "mensagem": input_data}),
                        'headers': {
                            'Content-Type': 'application/json'
                        }
                    }
                else:
                    return {
                        'statusCode': 400,
                        'body': json.dumps({'Error': 'Nenhum body presente na requisição'}),
                        'headers': {
                            'Content-Type': 'application/json'
                        }
                    }
            else:
                return {
                    'statusCode': 401,
                    'body': json.dumps({'Error': 'Token inválido'}),
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
        else:
            return {
                'statusCode': 401,
                'body': json.dumps({'Error': 'Token ausente no cabeçalho de autorização'}),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }

    except json.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'Error': 'JSON inválido: ' + str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'Error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
