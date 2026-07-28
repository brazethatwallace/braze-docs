---
nav_title: Centro de preferencias de correo electrónico con API
article_title: Centro de preferencias de correo electrónico con API
page_order: 1
description: "Este artículo describe el centro de preferencias de correo electrónico con API y cómo personalizarlo."
channel:
  - email
---

# Centro de preferencias de correo electrónico con API {#api-email-preference-center}

> Configurar un centro de preferencias proporciona un lugar centralizado para que tus usuarios editen y administren sus preferencias de notificación para tu [mensajería de correo electrónico]({{site.baseurl}}/user_guide/channels/email). Este artículo incluye los pasos para crear un centro de preferencias generado por API, pero también puedes crear un centro de preferencias usando el [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

En el panel de Braze, ve a **Audiencia** > **Centros de preferencias de correo electrónico**.

Aquí es donde puedes administrar y ver cada grupo de suscripción. Cada grupo de suscripción que crees se añade a esta lista del centro de preferencias. Puedes crear múltiples centros de preferencias.

{% alert important %}
El centro de preferencias está diseñado para usarse dentro del canal de correo electrónico de Braze. Los enlaces del centro de preferencias son dinámicos y se basan en cada usuario, por lo que no pueden alojarse externamente.
{% endalert %}

## Crear un centro de preferencias con API {#create-a-preference-center-with-api}

Usando los [endpoints del centro de preferencias de Braze]({{site.baseurl}}/api/endpoints/preference_center), puedes crear un centro de preferencias, un sitio web alojado por Braze, que puede mostrar el estado de suscripción y los estados de los grupos de suscripción de tus usuarios. Usando HTML y CSS, tu equipo de desarrolladores puede crear el centro de preferencias para que el estilo de la página coincida con tus directrices de marca.

Usar Liquid te permite recuperar los nombres de tus grupos de suscripción y el estado de cada usuario. De esta manera, Braze almacena y recupera estos datos cuando se carga la página.

### Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Centro de preferencias habilitado | Tu panel de Braze tiene permisos para usar la característica del centro de preferencias. |
| Espacio de trabajo válido con un grupo de suscripción de correo electrónico, SMS o WhatsApp | Un espacio de trabajo funcional con usuarios válidos y un grupo de suscripción de correo electrónico, SMS o WhatsApp. |
| Usuario válido | Un usuario con una dirección de correo electrónico y un ID externo. |
| Clave de API generada con permisos del centro de preferencias | En el panel de Braze, ve a **Configuración** > **Claves de API** para confirmar que tienes acceso a una clave de API con permisos del centro de preferencias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

### Paso 1: Usa el endpoint Crear centro de preferencias {#step-1-use-the-create-preference-center-endpoint}

Comencemos a crear un centro de preferencias usando el [endpoint Crear centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center). Para personalizar tu centro de preferencias, puedes incluir HTML que se alinee con tu marca en el campo `preference_center_page_html` y el campo `confirmation_page_html`.

El [endpoint Generar URL del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) te permite obtener la URL del centro de preferencias para un usuario específico fuera de un correo electrónico enviado a través de Braze.

{% alert note %}
Braze renderiza `confirmation_page_html` en un iframe que usa una URL `data:`. Los navegadores tratan las URL `data:` como orígenes opacos. Como resultado, los scripts en ese iframe no pueden cargar recursos externos adicionales, y la navegación de la ventana principal o la comunicación entre marcos desde esa página falla.<br><br>En su lugar, puedes enlazar a contenido externo, como una URL de cuestionario alojada, en lugar de incrustar scripts. Si necesitas incrustar una herramienta de terceros y el proveedor lo permite, usa un `<iframe title="Descripción del contenido incrustado" src="https://example.com/...">` que apunte a la URL HTTPS alojada de la herramienta.
{% endalert %}

### Paso 2: Incluir en tu campaña de correo electrónico {#step-2-include-in-your-email-campaign}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar un enlace al centro de preferencias en tus correos electrónicos, usa la siguiente etiqueta de Liquid en el lugar deseado de tu correo electrónico, de manera similar a como insertarías las URL de cancelación de suscripción.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

También puedes usar una combinación de HTML que incluya Liquid. Por ejemplo, puedes pegar lo siguiente como la URL en el editor HTML o en el editor de arrastrar y soltar. Esto muestra el diseño básico del centro de preferencias que lista todos los grupos de suscripción de correo electrónico automáticamente. Si usas [aliasing de enlaces]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing), añade un signo de interrogación final (`?`) después de la etiqueta de Liquid para que Braze pueda añadir parámetros de seguimiento.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

El centro de preferencias tiene una casilla de verificación que permite a tus usuarios cancelar la suscripción de todos los correos electrónicos.

{% multi_lang_include preference_center/testing.md section="api" %}

#### Editar un centro de preferencias {#edit-a-preference-center}

Puedes editar y actualizar tu centro de preferencias usando el [endpoint Actualizar centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center).

#### Identificar centros de preferencias y detalles {#identify-preference-centers-and-details}

Para identificar tus centros de preferencias, usa el [endpoint Ver detalles del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) para devolver información relacionada, como la marca de tiempo de la última actualización, el ID del centro de preferencias y más.

## Personalizar un centro de preferencias {#customize-a-preference-center}

Braze administra las actualizaciones del estado de suscripción desde el centro de preferencias, lo que mantiene el centro de preferencias sincronizado. Sin embargo, también puedes crear y alojar tu propio centro de preferencias usando las [API de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups) con las siguientes opciones.

### Opción 1: Enlace con parámetros de cadena de consulta {#option-1-link-with-string-query-parameters}

Usa pares de campo-valor de cadena de consulta en el cuerpo de la URL para pasar el ID de usuario y la categoría de correo electrónico a la página, de modo que los usuarios solo necesiten confirmar su elección para cancelar la suscripción. Esta opción es buena para quienes almacenan un identificador de usuario en un formato hash y no tienen ya un centro de suscripción.

Para esta opción, cada categoría de correo electrónico requiere su propio enlace de cancelación de suscripción específico:<br>
`http://mycompany.com/query-string-form-fill?field_id=Alex&field_category=offers`

{% alert tip %}
También es posible aplicar un hash al ID externo del usuario en el momento del envío usando un filtro de Liquid. Esto convertirá el `user_id` en un valor hash MD5, por ejemplo:
{% raw %}
```liquid
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Opción 2: Autenticar con JSON web token {#option-2-authenticate-with-json-web-token}

Usa un [JSON web token](https://auth0.com/learn/json-web-tokens/) para autenticar a los usuarios en una parte de tu servidor web (por ejemplo, preferencias de cuenta) que normalmente está detrás de una capa de autenticación como nombre de usuario e inicio de sesión con contraseña.

Este enfoque no requiere pares de valor de cadena de consulta incrustados en la URL, ya que estos pueden pasarse en la carga útil del JSON web token, por ejemplo:

```json
{
    "user_id": "1234567890",
    "name": "Alex Smith",
    "category": "offers"
}
```

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué mi centro de preferencias no funciona en un envío de prueba? {#why-doesnt-my-preference-center-work-in-a-test-send}

Los enlaces del centro de preferencias requieren un contexto de envío en vivo. Los envíos de prueba no generan URL válidas del centro de preferencias, y el botón **Guardar preferencias** se deshabilita si la página se carga. Este es el comportamiento esperado. Para probar de extremo a extremo, lanza una Campaign o un paso en Canvas a un usuario de prueba o un segmento interno pequeño, o usa el [endpoint Generar URL del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center). Para más detalles, consulta [Probar centros de preferencias](#testing-preference-centers).

### No he creado un centro de preferencias. ¿Por qué veo "PreferenceCenterBrazeDefault" en mi panel? {#i-havent-created-a-preference-center-why-am-i-seeing-preferencecenterbrazedefault-on-my-dashboard}

Esto se usa para renderizar el centro de preferencias cuando se usa el Liquid heredado {%raw%}`${preference_center_url}`{%endraw%}, lo que significa que los pasos en Canvas o las plantillas que hacen referencia a {%raw%}`${preference_center_url}` o `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} no funcionarán. Esto también se aplica a los mensajes enviados anteriormente que incluían el Liquid heredado o "PreferenceCenterBrazeDefault" como parte del mensaje.

Si haces referencia a {%raw%}`${preference_center_url}`{%endraw%} en un nuevo mensaje, se creará de nuevo un centro de preferencias llamado "PreferenceCenterBrazeDefault".

### ¿Los centros de preferencias admiten múltiples idiomas? {#do-preference-centers-support-multiple-languages}

No. Sin embargo, puedes aprovechar Liquid al escribir el HTML para páginas personalizadas de adhesión voluntaria y cancelación de suscripción. Si usas enlaces dinámicos para administrar las cancelaciones de suscripción, este es un enlace único.

Por ejemplo, si estás rastreando la tasa de cancelaciones para usuarios de habla hispana, necesitarías usar Campaigns separadas o aprovechar los análisis de Currents (como verificar cuándo un usuario cancela la suscripción y comprobar el idioma preferido de ese usuario).

Como otro ejemplo, para rastrear las tasas de cancelación de suscripción para usuarios de habla hispana, podrías añadir una cadena de parámetro de consulta como `?Spanish=true` a la URL de cancelación de suscripción si el idioma del usuario es español y usar un enlace de cancelación de suscripción regular si no lo es:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Luego, a través de Currents, podrías identificar qué usuarios hablan español y cuántos eventos de clic hubo para ese enlace de cancelación de suscripción.

### ¿Se requieren tanto los enlaces de cancelación de suscripción como los centros de preferencias de correo electrónico para el envío? {#are-both-unsubscribe-links-and-email-preference-centers-required-for-sending}

No. Si ves el mensaje "Your Email Body does not include an unsubscribe link" al redactar una campaña de correo electrónico, esta advertencia es esperada si tu enlace de cancelación de suscripción está en un bloque de contenido.

### ¿Cómo actualizo el icono predeterminado del navegador? {#how-do-i-update-the-default-browser-icon}

De forma predeterminada, el icono junto al nombre de la pestaña del navegador (favicon) usa el logotipo de Braze. Para añadir un favicon personalizado, lo configuras a través del atributo `links-tags` en tu llamada a la API de Crear o Actualizar [centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center). Braze luego inyecta la etiqueta {% raw %}`<link rel="icon" ...>`{% endraw %} en la página alojada por ti.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}