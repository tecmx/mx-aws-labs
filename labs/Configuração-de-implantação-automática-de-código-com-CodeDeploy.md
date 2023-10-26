
## Criar uma instância do EC2


### Criar um IAM profile para permitir que a VM possa acessar o S3

1. Acessar a console do serviço IAM em https://console.aws.amazon.com/iam
2. Criar uma ova política de acesso:
3. Acessar a opção **Polices** no menu e depois criar no botão **Create policy**
4. Clicar na aba JSON e colar o seguinte conteúdo:

<pre>
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
</pre>

5. Depois, clicar em **Review policy**
6. Escolher o nome **CodeDeployDemo-EC2-Permissions** e clicar em **Create policy**  
7. Acessar a opção **Role** no menu lateral e depois criar no botão **Create role**
8. Escolher **AWS service** e, da lista **Choose the service that will use this role** escolher **EC2**
9. Clicar em **Next**
10. Na página **Attached permissions policy**, escolher o nome da política criada anteriormente
11. Clicar em **Next** até a etapa final, escolher o nome do role **CodeDeployDemo-EC2-Instance-Profile** e clicar em **Create role**

### Criar uma instância EC2

1. Acessar a console do serviço EC2
2. Iniciar o wizard através do botão "Launch Instance";
3. Escolher o sistema operacional Ubuntu Server 18.04 LTS e tipo t2.micro (Free-tier eligible);
4. Atribuir para a VM o IAM role criado anteriormente (CodeDeployDemo-EC2-Instance-Profile);
5. Atribuir uma **tag** para a VM (ex: usar key codeploy e value yes)
6. Baixar chave de acesso (criar uma nova com o seu nome);
7. Conectar via SSH na VM e realizar a instação do agente do CodeDeploy:

<pre>
sudo apt-get update
sudo apt-get install ruby wget
cd /home/ubuntu
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
</pre>

8. Verificar se o agente está executando:

<pre>
sudo service codedeploy-agent status
</pre>

## Referências:

* Create a Service Role for CodeDeploy: https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html
* Create an IAM Instance Profile for Your Amazon EC2 Instances (Console): https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-iam-instance-profile.html