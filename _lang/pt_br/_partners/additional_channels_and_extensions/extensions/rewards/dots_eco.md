---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Este artigo de referência descreve a integração da Braze com o DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) permite recompensar os usuários com impacto ambiental real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados, como uma URL de certificado compartilhável e uma URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

_Essa integração é mantida pelo DOTS.ECO._

## Sobre essa integração {#about-this-integration}

A Braze e o DOTS.ECO conectam as jornadas de engajamento do cliente a recompensas de impacto no mundo real. A partir de uma etapa de Canvas ou Campaign da Braze, você pode disparar uma solicitação de criação de certificado DOTS.ECO usando Conteúdo conectado. O DOTS.ECO retorna metadados do certificado (como `certificate_url` e `certificate_image_url`) que podem ser armazenados no perfil do usuário como atributos personalizados e reutilizados em canais como mensagens no app, Content Cards e notificações por push.

## Casos de uso {#use-cases}

- Dispare um certificado de impacto quando um usuário concluir um evento-chave (compra, conclusão de nível, inscrição, indicação).
- Mostre uma imagem de certificado personalizada em uma mensagem no app depois que a etapa de Conteúdo conectado for bem-sucedida.
- Adicione um Content Card "Veja seu certificado" com a URL do certificado para acesso posterior.
- Armazene metadados de certificados (como `certificate_url`, `certificate_image_url`, `certificate_header` e `greeting`) como atributos personalizados para reutilização em futuros envios de mensagens.
- Atribua certificados usando um ID de usuário remoto para que os usuários possam reivindicar e visualizar seu impacto posteriormente.
- Execute testes A/B no envio de mensagens de impacto (textos/imagens diferentes), mantendo o mesmo fluxo de atualização de usuário do DOTS.ECO.


## Pré-requisitos {#prerequisites}

Antes de começar, você precisa dos seguintes itens:

| Pré-requisito | Descrição |
|---|---|
| Conta DOTS.ECO | Acesso à conta DOTS.ECO. |
| Credenciais DOTS.ECO | A solicitação deste artigo requer um token de aplicativo DOTS.ECO, uma chave de API e um ID de alocação. Para obtê-los, entre em contato com o seu CSM DOTS.ECO. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. Crie essa chave no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração com o DOTS.ECO {#integrating-dotseco}

### Etapa 1: Crie um Canvas e adicione uma etapa de Atualização de usuário {#step-1-create-a-canvas-and-add-a-user-update-step}

No dashboard da Braze, crie um novo Canvas que dispara quando um usuário conclui um evento-chave (como uma compra, inscrição ou marco).

Adicione uma etapa de Atualização de usuário logo após a etapa de entrada. Essa etapa será usada para chamar a API do DOTS.ECO via Conteúdo conectado e armazenar os dados de certificado retornados no perfil do usuário.

Use essa etapa para chamar a API do DOTS.ECO via Conteúdo conectado e armazenar os dados de certificado retornados no perfil do usuário.

### Etapa 2: Crie JSON avançado: faça uma solicitação POST para o DOTS.ECO usando Conteúdo conectado {#step-2-compose-advanced-json-make-a-post-request-to-dotseco-using-connected-content}

Na etapa **Atualização de usuário**, mude para o **Advanced JSON Editor** e use o Conteúdo conectado para fazer uma solicitação POST para a API de certificado do DOTS.ECO.

Use a tag `capture` e uma solicitação de Conteúdo conectado para chamar o endpoint de certificado do DOTS.ECO. Em seguida, salve a resposta no perfil do usuário como atributos personalizados.

**Exemplo de Conteúdo conectado e Atualização de usuário**
{% raw %}
```
{% capture post_body %}
{
  "remote_user_email": "{{${email_address} | default: 'braze+user@example.com'}}",
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",
  "impact_qty": 1,
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"
}
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk
  :method post
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }
  :body {{post_body}}
  :content_type application/json
  :save result
%}

{
  "attributes": [
    {
      "certificate_image_url": "{{result.certificate_image_url}}",
      "certificate_url": "{{result.certificate_url}}",
      "certificate_id": "{{result.certificate_id}}"
    }
  ]
}
```
{% endraw %}

Envie a solicitação para `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![Etapa de Atualização de usuário do DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}
Essa integração usa o Conteúdo conectado dentro de uma etapa de **Atualização de usuário** do Canvas para chamar a API do DOTS.ECO. Teste as solicitações com um cliente de API (por exemplo, Postman) primeiro para validar o token e a carga útil.
{% endalert %}

### Etapa 3: Exiba o certificado nas mensagens {#step-3-display-the-certificate-in-messages}

Quando os atributos do certificado estão armazenados no perfil do usuário, eles podem ser referenciados nas etapas de mensagem posteriores do Canvas.

![Fluxo do DOTS.ECO.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![Etapa de mensagem do DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![Seção de composição de mensagem do DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Por exemplo:
- Mostre a imagem do certificado em uma mensagem no app usando {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}
- Crie um link para o certificado hospedado usando {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![Comportamento ao clicar na mensagem do DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Isso permite que você personalize mensagens no app, Content Cards ou notificações por push com confirmação de impacto.

## Solução de problemas {#troubleshooting}

Revise os erros de Conteúdo conectado no dashboard da Braze em **Configurações** > **Registro de atividades de envio de mensagem**.

- **Conteúdo conectado retorna vazio**: Confirme que `:save result` está definido e que você está referenciando os campos de resposta esperados.
- **Os atributos não estão sendo exibidos na etapa de mensagem**:
  - Confirme se os nomes dos atributos personalizados na Braze correspondem exatamente aos atributos definidos na etapa de Atualização de usuário.
  - Na etapa de Atualização de usuário, use a guia **Pré-visualização e teste** para confirmar o preenchimento dos atributos. Em seguida, envie um teste para um usuário e confirme se os atributos estão salvos no perfil do usuário.
- **Erro `422` (entidade não processável)**: Confirme se o token do app e a quantidade de impacto são válidos.
- **Erro `401`**: Confirme se o token de autenticação está presente e correto.
- **Sem pré-visualização da imagem na etapa de mensagem**: Selecione **Enviar teste para o usuário** na etapa de Atualização de usuário e, em seguida, faça a pré-visualização da mensagem usando esse mesmo usuário.