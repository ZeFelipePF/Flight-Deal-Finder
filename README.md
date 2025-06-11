# Alerta de Voos Baratos ✈️

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)

Este projeto é um bot automatizado que monitora os preços de voos para destinos de interesse e envia um alerta por SMS ou WhatsApp quando encontra uma passagem abaixo do preço-alvo. Os destinos e preços são gerenciados através de uma simples planilha do Google Sheets.

## Funcionalidades Principais

-   **Gerenciamento via Planilha**: Lê a lista de destinos e preços-alvo diretamente de uma planilha do Google Sheets.
-   **Busca Automática de IATA**: Preenche automaticamente os códigos IATA para as cidades listadas na planilha.
-   **Monitoramento de Preços**: Pesquisa os voos mais baratos (ida e volta, diretos) para os próximos 6 meses.
-   **Alertas por SMS/WhatsApp**: Se um voo é encontrado com preço inferior ao definido na planilha, um alerta detalhado é enviado via Twilio.

---

## Tecnologias Utilizadas

-   **Linguagem**: Python
-   **APIs**:
    -   [**Sheety**](https://sheety.co/): Para interagir com a Google Sheet como se fosse uma API REST.
    -   [**Amadeus Self-Service API**](https://developers.amadeus.com/): Para busca de códigos de cidades (IATA) e pesquisa de ofertas de voos.
    -   [**Twilio API**](https://www.twilio.com/): Para o envio de notificações via SMS/WhatsApp.
-   **Bibliotecas Python**:
    -   `requests`: Para realizar as chamadas HTTP para as APIs.
    -   `python-dotenv`: Para gerenciar as chaves de API e segredos de forma segura.
    -   `twilio`: Para interagir com a API da Twilio.

---

## Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Pré-requisitos

-   Python 3.11 ou superior.
-   Contas ativas e chaves de API para **Sheety**, **Amadeus for Developers** e **Twilio**.
-   Uma planilha no Google Sheets com as colunas: `city`, `iataCode`, `lowestPrice`.

### 2. Instalação

Primeiro, clone o repositório:
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
Crie e ative um ambiente virtual:

Bash

# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
Instale as dependências a partir do arquivo requirements.txt:

Bash

pip install -r requirements.txt
(Nota: Se o arquivo requirements.txt não existir, crie-o com o comando pip freeze > requirements.txt após instalar as bibliotecas requests, python-dotenv e twilio).

3. Configuração das Variáveis de Ambiente
Este projeto utiliza um arquivo .env para armazenar suas credenciais de forma segura.

a. Crie um arquivo chamado .env na raiz do projeto.

b. Copie o conteúdo abaixo para o seu arquivo .env e substitua os valores pelos seus.

Snippet de código

# Sheety API
SHEETY_ENDPOINT="[https://api.sheety.co/seu/endpoint/prices](https://api.sheety.co/seu/endpoint/prices)"

# Amadeus API
AMADEUS_API_KEY="SUA_CHAVE_DE_API_AMADEUS"
AMADEUS_API_SECRET="SEU_SEGREDO_DE_API_AMADEUS"

# Twilio API
TWILIO_SID="SEU_TWILIO_ACCOUNT_SID"
TWILIO_TOKEN="SEU_TWILIO_AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER="SEU_NUMERO_VIRTUAL_TWILIO"
MY_PHONE_NUMBER="SEU_NUMERO_DE_TELEFONE_PARA_RECEBER_ALERTA"
4. Configuração da Planilha (Sheety)
Crie sua planilha no Google Sheets.
Acesse sua conta no Sheety e crie um novo projeto linkando a sua planilha.
Na configuração do seu endpoint no Sheety, certifique-se de que os métodos GET, POST e PUT estejam habilitados.
Como Usar
Com tudo configurado, basta executar o script principal a partir do seu terminal (com o ambiente virtual ativado):

Bash

python main.py
O script irá percorrer a sua planilha, buscar os voos e enviar notificações se as condições forem atendidas.

Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
