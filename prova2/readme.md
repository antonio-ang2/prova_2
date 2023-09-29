# Revisão prova 2

## AWS

### RDS

O Amazon RDS (Relational Database Service) é um serviço de banco de dados gerenciado oferecido pela Amazon Web Services (AWS). Ele foi projetado para simplificar a configuração, operação e escalabilidade de bancos de dados relacionais na nuvem. O RDS é compatível com vários sistemas de gerenciamento de banco de dados (DBMS), incluindo:

1. MySQL
2. PostgreSQL
3. Oracle Database
4. Microsoft SQL Server
5. MariaDB

A principal finalidade do Amazon RDS é facilitar a implantação e a manutenção de bancos de dados relacionais, eliminando a necessidade de tarefas operacionais complicadas, como gerenciamento de servidor, aplicação de patches, backups e escalabilidade de hardware. Aqui estão algumas das principais funcionalidades e benefícios do Amazon RDS:

1. **Gerenciamento Automatizado:** O RDS gerencia automaticamente tarefas como backup, aplicação de patches de segurança e monitoramento do desempenho do banco de dados.

2. **Alta Disponibilidade:** Você pode configurar o RDS para funcionar em várias zonas de disponibilidade, garantindo alta disponibilidade e tolerância a falhas.

3. **Escalabilidade:** O RDS permite dimensionar verticalmente ou horizontalmente seu banco de dados para atender às necessidades de desempenho e capacidade em constante evolução.

4. **Segurança:** O serviço oferece recursos de segurança avançados, como criptografia de dados em repouso e em trânsito, grupos de segurança e integração com o AWS Identity and Access Management (IAM).

5. **Monitoramento e Métricas:** Você pode acompanhar o desempenho do seu banco de dados por meio de métricas e logs disponibilizados pelo RDS e integrá-los com outras ferramentas de monitoramento.

6. **Facilidade de Migração:** O RDS oferece ferramentas e recursos para ajudar na migração de bancos de dados locais para a AWS.

7. **Backup e Restauração:** O RDS realiza automaticamente backups regulares do seu banco de dados e permite restaurá-los a qualquer momento.

8. **Replicação:** É possível configurar réplicas de leitura para melhorar o desempenho de leitura do banco de dados.

9. **Compatibilidade com Aplicativos:** O RDS é compatível com muitos aplicativos e frameworks que usam bancos de dados relacionais.

No geral, o Amazon RDS torna mais fácil para as empresas implantar, gerenciar e dimensionar bancos de dados relacionais na nuvem, permitindo que se concentrem mais no desenvolvimento de aplicativos e menos na administração de infraestrutura de banco de dados.

### Apache
O Apache, em contexto de tecnologia, refere-se ao servidor web Apache HTTP Server, também conhecido como Apache. É um dos servidores web mais populares e amplamente utilizados no mundo. O Apache é um software de código aberto e gratuito, amplamente apoiado e mantido pela Apache Software Foundation.

Para que serve o Apache HTTP Server:

1. **Servir Páginas da Web:** O Apache é usado principalmente para servir páginas da web para clientes da Internet. Ele atende a solicitações HTTP de navegadores da web e entrega os arquivos HTML, imagens, CSS, JavaScript e outros recursos solicitados aos usuários.

2. **Hospedagem de Sites:** Empresas e indivíduos usam o Apache para hospedar seus sites e aplicativos da web. Ele pode ser configurado para acomodar vários domínios e sites em uma única instância.

3. **Execução de Aplicações Web:** Além de servir arquivos estáticos, o Apache pode ser configurado para executar aplicativos da web, como aplicativos baseados em PHP, Python, Ruby e outras linguagens de programação. Isso é possível com a ajuda de módulos e plugins específicos.

4. **Proxy Reverso:** O Apache pode ser configurado como um proxy reverso para encaminhar solicitações de clientes para outros servidores web ou aplicativos, geralmente para melhorar o desempenho, segurança ou escalabilidade.

5. **Segurança:** O Apache oferece recursos de segurança avançados, como SSL/TLS para criptografar a comunicação entre o servidor e o cliente, autenticação de usuário e controle de acesso baseado em diretivas.

6. **Extensibilidade:** Uma das principais vantagens do Apache é sua extensibilidade por meio de módulos. Você pode adicionar funcionalidades personalizadas ou de terceiros ao servidor, tornando-o altamente adaptável às suas necessidades.

7. **Configurabilidade:** O Apache é altamente configurável por meio de arquivos de configuração. Isso permite que os administradores personalizem o comportamento do servidor de acordo com as necessidades específicas do projeto.

8. **Controle de Acesso:** O Apache permite que os administradores controlem quem pode acessar os recursos do servidor com base em endereços IP, autenticação de usuário, entre outras regras.

9. **Logs e Monitoramento:** O Apache gera logs detalhados que podem ser usados para monitorar o tráfego, depurar problemas e avaliar o desempenho do servidor web.

Em resumo, o Apache HTTP Server é uma peça fundamental da infraestrutura da web e é usado para hospedar sites, aplicativos da web e serviços online, tornando-o essencial para a entrega de conteúdo e a execução de aplicativos na Internet.


## Construindo uma calculadora:

- Primeiro, devemos ter um arquivo fastapi:

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/somar/{numero1}/{numero2}")
async def somar(numero1: int, numero2: int):
    return {"resultado": numero1 + numero2}

@app.get("/subtrair/{numero1}/{numero2}")
async def subtrair(numero1: int, numero2: int):
    return {"resultado": numero1 - numero2}

@app.get("/multiplicar/{numero1}/{numero2}")
async def multiplicar(numero1: int, numero2: int):
    return {"resultado": numero1 * numero2}

@app.get("/dividir/{numero1}/{numero2}")
async def dividir(numero1: int, numero2: int):
    try:
        return {"resultado": numero1 / numero2}
    except:
        return {"resultado": "Não é possível dividir por zero."}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```