---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Este artículo de referencia describe la asociación entre Braze y MyPostcard, que te permite utilizar el correo directo como un canal adicional para tu flujo de trabajo de CRM."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com), una aplicación de postales líder en el mundo, te permite realizar campañas de correo directo con facilidad, proporcionándote una forma sencilla y rentable de conectar con tus clientes.

Utiliza la integración de MyPostcard y Braze para enviar a tus clientes correos impresos sin esfuerzo.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta MyPostcard B2B | Es necesario registrarse en MyPostcard para beneficiarse de esta integración. |
| Clave de API B2B y credenciales | Puedes encontrar tu clave de API y las credenciales en la herramienta de administración MyPostcard B2B. |
| Campaña MyPostcard B2B aprobada | Para aprovechar esta integración, necesitas configurar una campaña de correo impreso en la herramienta MyPostcard B2B. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

Para elevar tus campañas de correo directo, es crucial ir más allá de los envíos masivos tradicionales e integrar fácilmente el correo impreso en tus flujos de trabajo. Este enfoque te permite llegar a clientes específicos que se han dado de baja de tus boletines por correo electrónico o cuyos correos electrónicos están marcados como correo no deseado. Con MyPostcard, puedes enviar sin esfuerzo campañas de correo impreso directamente a través de Braze.

- Construye flujos de trabajo intuitivos en Braze, incorporando el correo impreso como un nuevo y potente canal, sin necesidad de conocimientos técnicos.
- Libera el potencial de los envíos impresos personalizados con unos sencillos pasos.
- Benefíciate de una implementación sencilla respaldada por la asistencia personalizada de un equipo especializado.

## Integración {#integration}

Para integrarte con MyPostcard, [inicia sesión o regístrate](https://www.mypostcard.com/b2b/admin/) y crea tu primera campaña para utilizarla a través de [los webhooks de Braze]({{site.baseurl}}/user_guide/channels/webhooks/).

### Paso 1: Crea tu plantilla de webhook de Braze {#step-1-create-your-braze-webhook-template}

Para crear una plantilla de webhook de MyPostcard que puedas utilizar en futuras Campaigns o Canvas, ve a **Contenido** > **Webhook** en la plataforma Braze. Luego, selecciona **Crear plantilla de webhook**.

Si quieres crear una campaña única de webhook de MyPostcard o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña. Rellena los siguientes campos:

| Campo | Descripción |
|---|---|
| **Webhook URL** | La URL del webhook tal y como se muestra en la herramienta de administración B2B. |
| **Request Body** | Texto sin formato (formato JSON que se encuentra en la herramienta de administración B2B). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create your Braze webhook template" }

#### Método y encabezados de solicitud {#request-method-and-headers}

MyPostcard requiere que se incluya en la plantilla un método HTTP junto con los siguientes encabezados HTTP.

{% raw %}
<table aria-label="Request method and headers">
  <caption>Método y encabezados de solicitud</caption>
  <thead>
    <tr>
      <th><strong>Campo</strong></th>
      <th><strong>Detalles</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTP Method</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Username</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Password</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request method and headers" }

#### Cuerpo de la solicitud {#request-body}

Copia el cuerpo de la solicitud que aparece en la herramienta de administración B2B y, a continuación, rellena los marcadores de posición con contenido utilizando cualquier etiqueta de personalización de Liquid.

![Pestaña Redactar que muestra el cuerpo JSON y la información del webhook.]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### Paso 2: Previsualiza tu solicitud {#step-2-preview-your-request}

A continuación, previsualiza tu solicitud en el panel **vista previa** o ve a la pestaña **Test**, donde puedes elegir un usuario al azar, un usuario existente o crear un usuario personalizado para probar tu webhook. ¡No olvides guardar tu plantilla antes de salir de la página!

![Pestaña de prueba de webhook con diferentes campos para validar la implementación.]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas pueden encontrarse en la lista **Plantillas de Webhook guardadas** al crear una nueva [campaña de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}