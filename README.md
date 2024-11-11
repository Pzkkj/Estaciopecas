# Sistema de Gerenciamento de Autopeças

Este é um sistema de gerenciamento de autopeças desenvolvido em Python, utilizando a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados. O sistema permite o cadastro, atualização, exclusão e listagem de registros de **Fornecedores**, **Peças** e **Veículos**.

## Funcionalidades

O sistema está dividido em módulos que oferecem funcionalidades específicas para cada tipo de dado:

### Módulo Fornecedores
- **Cadastrar Fornecedor**: Registra novos fornecedores, com validação de campos obrigatórios.
- **Atualizar Fornecedor**: Atualiza informações de fornecedores existentes, garantindo unicidade do CNPJ.
- **Excluir Fornecedor**: Solicita confirmação antes de excluir um fornecedor.
- **Listar Fornecedores**: Facilita a busca e visualização de fornecedores usando critérios como Razão Social e CNPJ.

### Módulo Peças
- **Cadastrar Peça**: Adiciona novas peças ao sistema, com validação dos campos obrigatórios.
- **Atualizar Peça**: Permite atualizar informações de peças, garantindo unicidade do código da peça.
- **Excluir Peça**: Solicita confirmação antes de excluir uma peça.
- **Listar Peças**: Permite busca por código, descrição, fabricante e fornecedor.

### Módulo Veículos
- **Cadastrar Veículo**: Registra novos modelos de veículos com validação dos campos obrigatórios.
- **Atualizar Veículo**: Garante a atualização correta dos dados do veículo.
- **Excluir Veículo**: Solicita confirmação antes de excluir um veículo.
- **Listar Veículos**: Facilita a busca por fabricante, modelo e tipo do veículo.

## Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas: Tkinter (inclusa na instalação padrão do Python) e SQLite (banco de dados embutido)


## Instruções de Instalação e Execução

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/gerenciamento-autopecas.git
    ```
2. **Navegue até o diretório do projeto**:
    ```bash
    cd gerenciamento-autopecas
    ```
3. **Instale as dependências** (caso use bibliotecas adicionais):
    ```bash
    pip install -r requirements.txt
    ```
4. **Inicie o sistema**:
    Execute o arquivo `main.py` para iniciar a aplicação:
    ```bash
    python main.py
    ```

## Uso

1. **Cadastro**: Preencha os campos obrigatórios e clique em "Salvar" para registrar um novo fornecedor, peça ou veículo.
2. **Atualização**: Selecione um registro na lista e edite os campos desejados. Salve para confirmar as alterações.
3. **Exclusão**: Selecione um registro na lista e clique em "Deletar". Uma confirmação será solicitada.
4. **Listagem**: Use as listas para visualizar e buscar informações de fornecedores, peças e veículos por critérios específicos.

## Banco de Dados

O banco de dados SQLite (`autopecas.db`) é criado automaticamente pelo sistema ao executar pela primeira vez. Caso precise reiniciar o banco de dados, basta deletar o arquivo `autopecas.db` e reiniciar a aplicação.

## Contribuição

Se deseja contribuir para o projeto, siga estas etapas:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature-nova-funcionalidade`).
3. Faça commit de suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o branch (`git push origin feature-nova-funcionalidade`).
5. Crie um Pull Request.



