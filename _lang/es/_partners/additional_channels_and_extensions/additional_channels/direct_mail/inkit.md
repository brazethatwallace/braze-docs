---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Este artículo de referencia describe la asociación entre Braze e Inkit, que te permite ahorrar tiempo y esfuerzo automatizando tus campañas de correo directo y hacer que los clientes que no están conectados vuelvan a estarlo."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com) y Braze permiten a las organizaciones generar y distribuir documentos de forma segura, tanto digitalmente como por correo directo.

_Esta integración está mantenida por Inkit._

## Sobre la integración {#about-the-integration}

La integración de Braze e Inkit te permite generar documentos y enviarlos por correo directamente a los usuarios de Braze con los webhooks de Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta Inkit | Se necesita una [cuenta Inkit](https://www.inkit.com/) para beneficiarse de esta asociación. |
| Clave de API de Inkit<br><br>`<INKIT_API_TOKEN>` | Esta clave se encuentra en tu [dashboard de Inkit](https://app.inkit.io/#/account/integrations), en la pestaña **Development**, y te permitirá conectar tus cuentas de Braze e Inkit.|
| ID de la plantilla Inkit<br><br>`<INKIT_TEMPLATE_ID>` | Después de crear una plantilla, puedes copiar el ID de plantilla de la pestaña **Templates** para utilizarlo en tu plantilla en Braze.<br><br>Por ejemplo, podrías crear una plantilla llamada `invoice_template` en el entorno Inkit con el ID de plantilla: `tmpl_3bDScFl9cwr3OAVR1RSdEC`.
| Encabezado HTTP | El encabezado HTTP forma parte de la solicitud de API que envías desde Braze a Inkit. En él, incluirás tu clave de API de Inkit para autenticar y autorizar las llamadas a la API de Inkit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

### Paso 1: Crear una plantilla Inkit {#step-1-create-an-inkit-template}

En la plataforma Inkit, crea una plantilla para utilizarla en tu campaña de Braze en HTML, Word, PowerPoint, Excel o PDF. Consulta la [documentación de Inkit](https://docs.inkit.com/docs/create-a-template) para obtener más información.

### Paso 2: Crea tu plantilla de webhook de Braze {#step-2-create-your-braze-webhook-template}

Para crear una plantilla de webhook de Inkit y utilizarla en futuras campañas o Canvas, ve a **Contenido** > **Webhook** en la plataforma Braze. Luego, selecciona **Crear plantilla de webhook**.

Si deseas crear una campaña de webhook de Inkit única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña.

![Una selección de plantillas de webhook prediseñadas disponibles en la pestaña Plantillas de Webhook de la sección Plantillas y medios.]({% image_buster /assets/img/inkit-webhook-template.png %})

Una vez que hayas seleccionado la plantilla de webhook de Inkit, deberías ver lo siguiente:
- **Webhook URL**: En blanco
- **Request Body**: Texto sin procesar

En el campo URL del webhook, [crea](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) e introduce una URL de webhook de Inkit.

![Código del cuerpo de la solicitud y URL del webhook mostrados en la pestaña de redacción del creador de webhooks de Braze.]({% image_buster /assets/img/inkit-integration.png %})

#### Encabezados de solicitud y método {#request-headers-and-method}

Inkit requiere un `HTTP Header` para la autorización, incluida tu clave de API de Inkit codificada en base 64. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Settings**, debes reemplazar el `<INKIT_API_TOKEN>` con tu clave de API de Inkit.

{% raw %}
- **Método HTTP**: POST
- **Encabezado de solicitud**:
  - **Authorization**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud {#request-body}

Asegúrate de que tu Liquid coincide con los atributos personalizados adecuados asociados a los siguientes campos obligatorios y opcionales. También puedes añadir campos de datos personalizados a cualquier solicitud.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Paso 3: Vista previa de tu solicitud {#step-3-preview-your-request}

El texto sin formato se resaltará automáticamente si se trata de una etiqueta de Braze aplicable. `street`, `unit`, `state` y `zip` deben configurarse como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) para enviar este webhook.

Previsualiza tu solicitud en el panel de **vista previa** o ve a la pestaña de **Test**, donde puedes seleccionar un usuario al azar, un usuario existente o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas pueden encontrarse en la lista **Plantillas de Webhook guardadas** al crear una nueva [campaña de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}