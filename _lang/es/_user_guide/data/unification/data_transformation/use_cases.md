---
nav_title: Casos de uso
article_title: Casos de uso de Transformación de datos de Braze
page_order: 2
page_type: reference
description: "Este artículo de referencia proporciona algunos casos de uso de Transformación de datos de Braze."
---

# Casos de uso de Transformación de datos {#data-transformation-use-cases}

> Considera los siguientes casos de uso posibles con Transformación de datos de Braze y una combinación de webhooks de las plataformas externas de ejemplo.

## Generación de clientes potenciales {#generating-leads}

Alojas un formulario Typeform de generación de clientes potenciales en tu sitio web. Cuando los nuevos usuarios rellenan este formulario, puedes:
- Crear nuevos usuarios en Braze.
- Añadirlos a una de tus listas de correo electrónico de Braze.
- Sincronizar algunas de sus respuestas como atributos personalizados en Braze, ya que sus respuestas son valiosos datos propios que pueden impulsar experiencias de mensajería personalizada en el futuro.

## Apertura de tickets de servicio {#opening-service-tickets}

Cuando los clientes abren tickets de servicio al cliente en una plataforma como Zendesk, puedes:
- Escribir un evento personalizado en Braze cuando se crea un ticket de Zendesk.
- Escribir un evento personalizado con propiedades del evento en Braze cuando se proporciona una calificación CSAT negativa en Zendesk.

## Integración con Braze {#integrating-with-braze}

Braze tiene una integración con [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate), una plataforma de información y cuestionarios para clientes. Con Transformación de datos, puedes guardar varias respuestas de cuestionario en un atributo personalizado anidado, en lugar de usar la integración existente que guarda varios atributos personalizados.

## Ejemplo de código de transformación {#example-transformation-code}

Considera esta carga útil de muestra de Typeform, una plataforma de cuestionarios, que se envía cada vez que se recibe una respuesta a un cuestionario.

![Captura de pantalla relacionada con el ejemplo de código de transformación.]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Transformación básica %}

Este ejemplo toma las respuestas del cuestionario como atributos y escribe un evento para indicar que se ha completado el cuestionario:

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
{% tab Transformación avanzada %}

Desarrollemos aún más el ejemplo de transformación básica e introduzcamos una declaración `if` para categorizar al usuario en una de las respuestas.

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