## Exemplos de aplicações com banco de dados não relacional

# Use root/example as user/password credentials
Neste exemplo ele está criando um banco de dados não relacional Mongo e um mongo express: 
version: '3.1'

services:

  mongo:
    image: mongo
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    ports:
      - 27017:27017

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
      ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/


#### O que é mongo express
Mongo Express, também conhecido como "mongo-express" ou "mongo-expressjs", é uma interface de usuário web de código aberto para gerenciar bancos de dados MongoDB. É uma ferramenta que facilita a visualização, edição e administração de dados armazenados em um banco de dados MongoDB, por meio de uma interface gráfica intuitiva e amigável, acessível diretamente em um navegador da web.

Algumas das principais funcionalidades do Mongo Express incluem:

1. **Visualização de Dados:** O Mongo Express permite visualizar e explorar os dados armazenados no seu banco de dados MongoDB, exibindo coleções e documentos em formatos legíveis.

2. **Edição de Dados:** Você pode editar e atualizar documentos diretamente pela interface do Mongo Express, tornando a edição de dados mais rápida e conveniente.

3. **Inserção de Dados:** Você pode criar novos documentos e inserir dados no banco de dados usando formulários interativos.

4. **Exclusão de Dados:** O Mongo Express permite excluir documentos individuais ou coleções inteiras, com confirmação para evitar exclusões acidentais.

5. **Gerenciamento de Índices:** Você pode criar e gerenciar índices para otimizar consultas e melhorar o desempenho das buscas.

6. **Consultas Personalizadas:** Além de visualizar os dados, você pode executar consultas personalizadas usando uma interface de consulta visual ou expressões de consulta no estilo JSON.

7. **Administração de Usuários e Permissões:** O Mongo Express pode ser usado para gerenciar usuários e permissões no banco de dados MongoDB.

O Mongo Express é útil para desenvolvedores, administradores de banco de dados e qualquer pessoa que precise interagir com um banco de dados MongoDB sem a necessidade de linha de comando ou ferramentas de linha de comando mais complexas.

Vale mencionar que o Mongo Express deve ser usado com cautela em ambientes de produção, uma vez que expor interfaces de gerenciamento a partir da web pode apresentar riscos de segurança. Portanto, é importante configurar corretamente as autenticações e autorizações para proteger os dados armazenados no MongoDB.