---
nav_title: Parceria Twilio
alias: /partners/twilio/

description: "Este artigo descreve a parceria entre a Braze e a Twilio."
page_type: update
channel:
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Observe que o suporte para a integração de webhook da Twilio será descontinuado em 31 de janeiro de 2020. Se você deseja continuar acessando os serviços de SMS com a Braze, consulte nossa [documentação de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/).
{% endalert %}

Para este exemplo, configuraremos o canal de webhook da Braze para enviar SMS e MMS aos seus usuários, por meio da [API or interface de programação do aplicativo (API) de envio de mensagens](https://www.twilio.com/docs/api/rest/sending-messages) da Twilio. Para sua conveniência, um modelo de webhook da Twilio está incluído no dashboard.

## URL HTTP {#http-url}

A URL do webhook é fornecida pela Twilio no seu dashboard. Essa URL é única para sua conta Twilio, pois contém seu ID de conta Twilio (`TWILIO_ACCOUNT_SID`).

No nosso exemplo da Twilio, a URL do webhook é `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Você pode encontrar essa URL na seção *Getting Started* do console da Twilio.

![Console da Twilio]({% image_buster /assets/img_archive/Twilio_Console.png %})

## Corpo da solicitação {#request-body}

A API or interface de programação do aplicativo (API) da Twilio espera que o corpo da solicitação seja codificado em URL, então precisamos começar alterando o tipo de solicitação no criador de webhook da Braze para `Raw Text`. Os parâmetros obrigatórios para o corpo da solicitação são *To*, *From* e *Body*.

A captura de tela a seguir é um exemplo de como sua solicitação pode ficar se você estiver enviando um SMS para o número de telefone de cada usuário, com o corpo "Hello from Braze!".

- Você precisará ter números de telefone válidos em cada perfil de usuário no seu público-alvo.
- Para atender ao formato de solicitação da Twilio, use o filtro Liquid `url_param_escape` no conteúdo da sua mensagem. Esse filtro codifica uma string para que todos os caracteres sejam permitidos em uma solicitação HTML. Por exemplo, o caractere de mais (`+`) no número de telefone `+12125551212` é proibido em dados codificados em URL e será convertido para `%2B12125551212`.

![Corpo do webhook]({% image_buster /assets/img_archive/Webhook_Body.png %})

## Cabeçalhos e método da solicitação {#request-headers-and-method}

A Twilio requer dois cabeçalhos de solicitação: o Content-Type da solicitação e um cabeçalho de [autenticação básica HTTP](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side). Adicione-os ao seu webhook clicando no ícone de engrenagem ao lado do criador de webhook e, em seguida, clicando em *Add New Pair* duas vezes.

Nome do cabeçalho | Valor do cabeçalho
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Authorization | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Substitua `TWILIO_ACCOUNT_SID` e `TWILIO_AUTH_TOKEN` pelos valores do seu dashboard da Twilio. Por fim, o endpoint da API or interface de programação do aplicativo (API) da Twilio espera uma solicitação HTTP POST, então escolha essa opção no menu suspenso de *HTTP Method*.

![Método do webhook]({% image_buster /assets/img_archive/Webhook_Method.png %})

## Pré-visualize sua solicitação {#preview-your-request}

Use o criador de webhook para pré-visualizar a solicitação de um usuário aleatório ou de um usuário com credenciais específicas, para garantir que a solicitação esteja sendo renderizada corretamente.

![Pré-visualização do webhook]({% image_buster /assets/img_archive/Webhook_Preview.png %})