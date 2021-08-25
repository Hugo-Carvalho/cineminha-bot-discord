# cineminha-bot-discord

Bot para Discord que realiza a tranmissão da tela para o compartilhamento de video nos canais de voz.

## Inicie a aplicação

- Instale as bibliotecas necessárias com `pip install -r requirements.txt`
- Inicie a aplicação com `python main.py`

## Preparação do ambiente

- No servidor do Discord crie um canal de voz com o nome `Cineminha`
- Recomendamos criar um usuário segundário para a autenticação (para que seu usuário não seja não saia da sessão atual)

## Execução

Com a aplicação iniciada e o ambiente preparado, siga os comandos para iniciar o serviço:

`-start`

Inicia os principais serviços (deve aguardar)

Logo apos sera enviado um qrcode para autenticação

Faça o login com um dispositivo movel com o usuário criado

Aguarde a conexão

`-cine url`

Redireciona para a url

`-play`

Inicia a mídia visivel na pagina

`-fullscreen` (Somente Youtube)

Habilita a tela cheia do video
