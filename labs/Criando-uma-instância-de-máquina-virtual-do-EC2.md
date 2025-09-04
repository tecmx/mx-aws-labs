
## Criar uma nova instância

**ATENÇÃO:** antes de acessar a console, é necessário iniciar o lab no [AWS Academy](https://www.awsacademy.com/vforcesite/LMS_Login).

1. Acessar a [console do AWS](https://console.aws.amazon.com);
2. Escolher a região us-east-1 (N. Virginia);
3. Entrar na opção EC2 na lista de serviços e iniciar o wizard através do botão "Launch Instance";
4. Escolher o sistema operacional Ubuntu Server 22.04 LTS e tipo t2.micro (Free-tier eligible);
5. Habilitar a opção "Auto-assign public IP" na seção de "Network settings";
5. Baixar chave de acesso (criar uma nova com o seu nome) e conectar via SSH na instância criada; Voltar até a lista de instâncias e localizar a instância recém criada (dica: colocar um nome para instância); Clicar no botão "Connect" para ler as instruções para conectar-se via SSH;
8. Testar o acesso a instância criada através via SSH.

Exemplo:
```
ssh -i chave.pem ubuntu@ip-publico-vm
```

## Iniciar um servidor usando Flask na instância (Opcional)

1. Instalar Virtual Environment:

```
sudo apt-get update
sudo apt-get install virtualenv python3 python3-pip
```

2. Criar um novo environment e instalar dependências:
```
mkdir venv
virtualenv -ppython3 venv
source venv/bin/activate
pip install Flask
```

3. Criar um arquivo hello.py com o seguinte conteúdo

```
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
```

4. Executar o servidor criado:

```
export FLASK_APP=hello.py
flask run --host=0.0.0.0 --port 8080
```

5. Liberar a porta TCP 8080 no Security Group (firewall) da máquina virtual.

6. Testar o acesso ao serviço via browser do computador local.

http://[ip-publico-vm]:8080

Obs: O IP publico da VM pode ser obitido na interface Web do serviço EC2.

7. Para encerrar a execução, pressione Control+C e depois digite o comando:

```
deactivate
```

