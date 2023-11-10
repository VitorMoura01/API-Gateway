# API-Gateway
## Criação de uma função Lambda em Python integrado com API Gateway
![image](https://github.com/VitorMoura01/API-Gateway/assets/99188092/58ef34dd-ba9f-4338-93f7-952b31655c70)
## 1.0 Como criar o ambiente na AWS
1. Acesse a página inicial do console.
2. Procure por Lambda entre os serviços na barra de pesquisa.
3. Clique em criar função.
   * Criar do zero.
   * Insira o nome da função.
   * Escolha python como o idioma a ser usado.
   * Arquitetura x86_64.
   * Alterar a função de execução padrão > Usar uma função existente.
   * Selecione LabRole para o nosso ambiente de dev (não será esse usado em produção).
4. Crie a função e no editor de código coloque o código.
5. Adicione um gatilho e escolha o API Gateway.
6. Escolha o tipo de requisição REST e a segurança aberta.
7. Realize deploy.

## 2.0 Como usar
No Postman, ou qualquer outra plataforma de APIs, envie seu JSON com Bearer Token e o body desejado no Endpoint do API Gateway. Exemplo:
   * "afonsomeda10"
   * {"body": "{\"name\": \"Vitor\", \"age\": 19, \"enrolment\": \"System Information\"}"}
### Endpoint: https://63p1hn5hoc.execute-api.us-east-1.amazonaws.com/default/flaskTestFunction
### Exemplo de body
```json
{
    "{\"name\": \"Vitor\", \"age\": 19, \"enrolment\": \"System Information\"}"
}
````

## 3.0 Testes de unidade
Foram realizados testes de unidade a fim de garantir a funcionalidade da função Lambda em casos de requisições não autorizadas ou mal estruturadas. A partir desses testes podemos saber se cumprimos ou não com as regras de negócio estabelecidas no projeto.

### 3.1 Não foi enviado o token
resultado esperado: Token ausente no header da requisição 
body:
![image](https://github.com/VitorMoura01/API-Gateway/assets/99188092/74b41588-053b-4b71-8af7-0f68878a56a8)
resultado obtido:
![image](https://github.com/VitorMoura01/API-Gateway/assets/99188092/cc089ce0-fabe-4b9d-bbbf-417c646db7cf)
**Passou no teste.**

### 3.2 Foi enviado o token, porém não condiz com o esperado
resultado esperado: Token inválido
resultado obtido:
![image](https://github.com/VitorMoura01/API-Gateway/assets/99188092/9db824ef-e2c1-4c39-96a7-c0a0877fe7e5)
**Passou no teste.**


### 3.3 Não foi enviado um body na estrutura do JSON
resultado esperado: Nenhum body presente na requisição (Bad Request)
resultado obtido:
![image](https://github.com/VitorMoura01/API-Gateway/assets/99188092/6918f65e-ca9b-44ff-986b-ec19591448c2)
**Passou no teste.**

### 3.3 Foi enviado o body de forma correta
resultado esperado: body enviado foi retornado
resultado obtido:
![image](https://github.com/VitorMoura01/API-Gateway/assets/99188092/e62b996f-cdfb-46d2-8363-cd70987f2fbd)
**Passou no teste.**


