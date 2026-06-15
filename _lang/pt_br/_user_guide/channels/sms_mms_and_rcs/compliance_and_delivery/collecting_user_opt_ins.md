---
nav_title: "Coletar opt-ins de usuários"
article_title: Melhores práticas para coletar opt-ins de SMS dos usuários
page_order: 3
description: "Este artigo de referência aborda três melhores práticas para coletar opt-ins de usuários."
page_type: reference
channel:
  - SMS

---

# Coletar opt-ins de usuários {#collect-user-opt-ins}

> O artigo a seguir lista alguns métodos comuns de opt-in para SMS.

## Opção 1: Peça aos usuários que enviem uma mensagem de texto para seu código curto ou longo {#option-1-ask-users-to-text-your-short-or-long-code}

Peça aos usuários que enviem "START", "UNSTOP", "YES" ou uma palavra-chave de opt-in personalizada para o seu número, adicionando-os automaticamente ao seu grupo de inscrições. No seu site, app móvel ou até mesmo em publicidade, você pode solicitar que os usuários façam isso para realizar o opt-in, e pode oferecer um incentivo se for útil.

## Opção 2: Usuários fazem opt-in por mensagem no app {#option-2-users-opt-in-via-in-app-message}

Para permitir que os usuários façam opt-in para SMS a partir de uma mensagem no app, use o [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture/) fornecido pela Braze para criar um formulário personalizado que permite coletar números de telefone e expandir sua lista de SMS.

![Criador de mensagens no app com um modelo para captura de número de telefone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

A Braze recomenda que você também use o recurso de [double opt-in de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/). Esse recurso funciona automaticamente com o formulário de captura de número de telefone da mensagem no app, solicitando que os usuários confirmem sua intenção após enviar o número de telefone pelo formulário.

## Opção 3: Fluxo de cadastro {#option-3-sign-up-flow}

Quando um novo usuário se cadastra ou se registra no site ou app, peça o número de telefone e o e-mail. Inclua uma caixa de seleção para receber e-mails e SMS promocionais.

Após o cadastro do usuário, faça o seguinte:

1. Use o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) para criar o usuário e salvar seus atributos.

```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```

{: start="2"}
2. Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para inscrever o usuário em SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert tip %}
Para inserir os usuários no fluxo de [double opt-in de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/) ao inscrevê-los pela REST API, defina o parâmetro `use_double_opt_in_logic` como `true` na sua requisição. Se você omitir esse parâmetro, os usuários serão inscritos sem receber uma confirmação de double opt-in.

Esse parâmetro é compatível com os seguintes endpoints:<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}