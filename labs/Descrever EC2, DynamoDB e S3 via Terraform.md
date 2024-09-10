### Atividade 6: Descrever Instância EC2, DynamoDB e S3 via Terraform

Nesta atividade, você irá implementar, com o uso do Terraform, a infraestrutura usada no laboratório, incluindo uma instância EC2, uma tabela no DynamoDB e um bucket S3. Sua tarefa será descrever como esses componentes são configurados via código, criando um arquivo `main.tf`.

#### Passos:

1. **Instância EC2**:
   - Defina uma instância EC2 no Terraform utilizando o recurso `aws_instance`. Utilize o tipo de instância `t2.micro` ou outro especificado. 
   - Inclua a configuração de uma chave SSH para permitir acesso à instância.
   - Configure um `Security Group` para permitir o tráfego de entrada na porta 8080 (necessário para rodar o servidor Flask).

   Exemplo de configuração da instância EC2:
   ```hcl
   resource "aws_instance" "example" {
     ami           = "ami-0c55b159cbfafe1f0"  # Substitua pelo AMI correto
     instance_type = "t2.micro"
     key_name      = "nome-da-chave"
     
     security_groups = ["allow_http"]

     tags = {
       Name = "exemplo_ec2"
     }
   }
   ```

2. **Tabela DynamoDB**:
   - Defina a tabela DynamoDB utilizando o recurso `aws_dynamodb_table`.
   - Configure as chaves de partição e de ordenação conforme descrito no laboratório (Partition Key: `name` como `string` e Sort Key: `date` como `number`).

   Exemplo de configuração do DynamoDB:
   ```hcl
   resource "aws_dynamodb_table" "example_table" {
     name         = "minha_tabela"
     billing_mode = "PAY_PER_REQUEST"

     hash_key  = "name"
     range_key = "date"

     attribute {
       name = "name"
       type = "S"
     }

     attribute {
       name = "date"
       type = "N"
     }

     tags = {
       Name = "exemplo_tabela"
     }
   }
   ```

3. **Bucket S3**:
   - Defina o bucket S3 utilizando o recurso `aws_s3_bucket`.
   - Configure permissões para permitir a leitura e escrita do bucket pela instância EC2.

   Exemplo de configuração do bucket S3:
   ```hcl
   resource "aws_s3_bucket" "example_bucket" {
     bucket = "nome-do-seu-bucket"

     tags = {
       Name = "exemplo_bucket"
     }
   }
   ```

4. **Security Group**:
   - Defina um `Security Group` que permita o tráfego de entrada na porta 8080 de qualquer IP.
   
   Exemplo de configuração de `Security Group`:
   ```hcl
   resource "aws_security_group" "allow_http" {
     name        = "allow_http"
     description = "Permitir tráfego HTTP"
     vpc_id      = "vpc-id-aqui"

     ingress {
       from_port   = 8080
       to_port     = 8080
       protocol    = "tcp"
       cidr_blocks = ["0.0.0.0/0"]
     }

     egress {
       from_port   = 0
       to_port     = 0
       protocol    = "-1"
       cidr_blocks = ["0.0.0.0/0"]
     }
   }
   ```

5. **IAM Role e Política**:
   - Defina uma `IAM Role` para a instância EC2 que permita acesso ao DynamoDB e S3.
   - Crie uma política IAM com permissões de leitura e escrita para a tabela do DynamoDB e o bucket S3.
   
   Exemplo de configuração da IAM Role:
   ```hcl
   resource "aws_iam_role" "example_role" {
     name = "ec2_role"

     assume_role_policy = jsonencode({
       Version = "2012-10-17"
       Statement = [{
         Action    = "sts:AssumeRole"
         Effect    = "Allow"
         Principal = {
           Service = "ec2.amazonaws.com"
         }
       }]
     })
   }

   resource "aws_iam_role_policy" "example_policy" {
     name = "ec2_policy"
     role = aws_iam_role.example_role.id

     policy = jsonencode({
       Version = "2012-10-17"
       Statement = [
         {
           Action = [
             "dynamodb:*",
             "s3:*"
           ]
           Effect   = "Allow"
           Resource = "*"
         }
       ]
     })
   }
   ```

#### Referências Oficiais para Consulta:

1. **Documentação do Terraform**:
   - [AWS Provider para Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs): A documentação oficial do provedor AWS no Terraform contém exemplos e detalhes sobre a criação e configuração de recursos como EC2, DynamoDB e S3.

2. **Documentação do Amazon EC2**:
   - [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/): Use esta documentação para compreender como o Amazon EC2 funciona, incluindo detalhes sobre tipos de instância, segurança e acesso via SSH.

3. **Documentação do DynamoDB**:
   - [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/): Consulte para entender as configurações de tabelas, tipos de chave e políticas de acesso.

4. **Documentação do Amazon S3**:
   - [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/): Encontre informações detalhadas sobre como criar e gerenciar buckets, permissões e políticas de acesso.

5. **IAM e Segurança**:
   - [IAM Roles Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html): Use esta referência para aprender sobre a configuração de roles e políticas de segurança para conceder permissões aos serviços AWS.

- **Validação**:
  - Certifique-se de que os recursos são provisionados corretamente usando o comando `terraform apply`.
  - Verifique que a tabela DynamoDB está acessível e que o bucket S3 pode ser usado para upload de imagens.
