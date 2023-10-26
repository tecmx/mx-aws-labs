
## Criar um bucket no serviço S3

1. Entrar na console do AWS;
2. Entrar na opção S3 na lista de serviços;
3. Criar um novo bucket no S3 com o seu nome;
   * Habilitar ACLs (marcar a opção ACLs enabled)
   * Desabilitar o bloqueio público (desmarcar a opção Block all public access)  
4. Fazer o upload de um arquivo nesse bucket (sugestão: utilize um arquivo de imagem qualquer);
5. Configurar esse arquivo para ser acessível publicamente;
   * Selecionar o objeto e clicar na opção Make public using ACL do menu Actions
6. Obter a URL do arquivo e abrir através do browser em uma nova aba para validar o acesso publico.

## Utilizar o serviço S3 via API Python

1. Conectar via SSH na instância do EC2 criada anteriormente;
2. Entrar no Virtualenv criado anteriormente:
```
source venv/bin/activate
```

3. Clonar repositório e executar o servidor:
```
git clone https://github.com/mvneves/Flask-AWS-Example.git
cd Flask-AWS-Example
pip install -r requirements.txt
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port 8080
```

4. Editar os fontes (ver arquivo config.py) para enviar arquivos para o bucket do S3 criado na etapa anterior (Parte 3); 
    * Observação: nesse ponto será necessário obter credenciais de acesso para a API do AWS. Para usuário AWS Educate, essas credenciais podem ser obtidas no botão Account Details;
5. Testar o acesso ao serviço via browser do computador local:

http://[ip-publico-vm]:8080

Obs: necessário liberar a porta TCP 8080 no Security Group (firewall) da máquina virtual.

6. Adicionar o servidor na inicialização do sistema (Opcional):
```
sudo cp etc/rc.local /etc/
./run.sh
```

7. Reiniciar a VM e testar novamente para validar que o serviço está subindo automaticamente (Opcional).