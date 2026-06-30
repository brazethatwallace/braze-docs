---
nav_title: Casos de uso
article_title: Casos de uso da Transformação de Dados Braze
page_order: 2
page_type: reference
description: "Este artigo de referência fornece alguns casos de uso da Transformação de Dados da Braze."
---

# Casos de uso de Transformação de Dados {#data-transformation-use-cases}

> Considere os seguintes casos de uso possíveis com a Transformação de Dados da Braze e uma combinação de webhooks das plataformas externas de exemplo.

## Geração de leads {#generating-leads}

Você hospeda um formulário Typeform de geração de leads em seu site. Quando novos usuários preenchem esse formulário, você pode:
- Criar novos usuários na Braze.
- Adicioná-los a uma de suas listas de e-mail da Braze.
- Sincronizar algumas de suas respostas como atributos personalizados na Braze, pois suas respostas são dados primários valiosos que podem alimentar experiências de mensagens personalizadas para uso futuro.

## Abertura de tickets de atendimento {#opening-service-tickets}

Quando os clientes abrem tickets de atendimento ao cliente em uma plataforma como o Zendesk, você pode:
- Registrar um evento personalizado na Braze quando um ticket do Zendesk for criado.
- Registrar um evento personalizado com propriedades de evento na Braze quando uma classificação CSAT negativa for fornecida ao Zendesk.

## Integração com a Braze {#integrating-with-braze}

A Braze tem uma integração com a [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate), uma plataforma de insights e pesquisas com clientes. Com a Transformação de Dados, é possível salvar várias respostas de pesquisa em um atributo personalizado aninhado, em vez de usar a integração existente que salva vários atributos personalizados.

## Exemplo de código de transformação {#example-transformation-code}

Considere esta carga útil de exemplo da Typeform, uma plataforma de pesquisa, que é enviada sempre que uma resposta de pesquisa é recebida.

![Captura de tela relacionada ao exemplo de código de transformação.]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Transformação básica %}

Este exemplo usa as respostas da pesquisa como atributos e registra um evento para indicar que a pesquisa foi concluída:

```
return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Transformação avançada %}

Vamos expandir o exemplo de transformação básica e introduzir uma declaração `if` para categorizar o usuário em uma das respostas.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}