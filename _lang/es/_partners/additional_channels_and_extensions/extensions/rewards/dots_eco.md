---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Este artículo de referencia describe la integración de Braze y DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) te permite recompensar a los usuarios con un impacto medioambiental real mediante certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL de certificado compartible y una URL de imagen, para que los usuarios puedan ver (y volver a ver) su prueba de impacto.

_Esta integración está mantenida por DOTS.ECO._

## Acerca de esta integración {#about-this-integration}

Braze y DOTS.ECO conectan los recorridos de interacción con los clientes con recompensas de impacto en el mundo real. Desde un paso en Canvas o Campaign de Braze, puedes desencadenar una solicitud de creación de certificado DOTS.ECO utilizando contenido conectado. DOTS.ECO devuelve metadatos de certificado (como `certificate_url` y `certificate_image_url`) que puedes almacenar en el perfil del usuario como atributos personalizados y reutilizar en canales como mensajes dentro de la aplicación, Content Cards y notificaciones push.

## Casos de uso {#use-cases}

- Desencadenar un certificado de impacto cuando un usuario completa un evento clave (compra, finalización de nivel, suscripción, referidos).
- Mostrar una imagen personalizada del certificado en un mensaje dentro de la aplicación después de que el paso de contenido conectado tenga éxito.
- Añadir una Content Card "Ver tu certificado" con la URL del certificado para acceder más tarde.
- Almacenar los metadatos del certificado (como `certificate_url`, `certificate_image_url`, `certificate_header` y `greeting`) como atributos personalizados para reutilizarlos en futuros mensajes.
- Asignar certificados utilizando un ID de usuario remoto para que los usuarios puedan reclamar y ver su impacto más tarde.
- Realizar pruebas A/B sobre la mensajería de impacto (diferentes textos/imágenes) manteniendo el mismo flujo de actualización de usuarios de DOTS.ECO.


## Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

| Requisito | Descripción |
|---|---|
| Cuenta DOTS.ECO | Acceso a la cuenta DOTS.ECO. |
| Credenciales DOTS.ECO | La solicitud de este artículo requiere un token de aplicación DOTS.ECO, una clave de API y un ID de asignación. Para recuperarlos, ponte en contacto con tu administrador del éxito del cliente en DOTS.ECO. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. Crea esta clave en el panel de Braze en **Configuración** > **Claves de API**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de DOTS.ECO {#integrating-dotseco}

### Paso 1: Crea un Canvas y añade un paso de Actualización de usuario {#step-1-create-a-canvas-and-add-a-user-update-step}

En el panel de Braze, crea un nuevo Canvas que se desencadene cuando un usuario complete un evento clave (como una compra, una suscripción o un hito).

Añade un paso de Actualización de usuario justo después del paso de entrada. Este paso se utilizará para llamar a la API de DOTS.ECO a través de contenido conectado y almacenar los datos de certificado devueltos en el perfil de usuario.

Utiliza este paso para llamar a la API de DOTS.ECO a través de contenido conectado y almacenar los datos de certificado devueltos en el perfil de usuario.

### Paso 2: Redactar JSON avanzado: haz una solicitud POST a DOTS.ECO utilizando contenido conectado {#step-2-compose-advanced-json-make-a-post-request-to-dotseco-using-connected-content}

En el paso **Actualización de usuario**, cambia al **Editor JSON avanzado** y utiliza contenido conectado para realizar una solicitud POST a la API de certificados DOTS.ECO.

Utiliza la etiqueta `capture` y una solicitud de contenido conectado para llamar al punto de conexión de certificados de DOTS.ECO. A continuación, guarda la respuesta en el perfil de usuario como atributos personalizados.

**Ejemplo de contenido conectado y Actualización de usuario**
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

Envía la solicitud a `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![Paso de Actualización de usuario de DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}
Esta integración utiliza contenido conectado dentro de un paso de **Actualización de usuario** en Canvas para llamar a la API de DOTS.ECO. Prueba primero las solicitudes con un cliente API (por ejemplo, Postman) para validar tu token y carga útil.
{% endalert %}

### Paso 3: Mostrar el certificado en mensajes {#step-3-display-the-certificate-in-messages}

Cuando los atributos del certificado se almacenan en el perfil de usuario, puedes hacer referencia a ellos en los pasos posteriores de mensaje en Canvas.

![Flujo de DOTS.ECO.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![Paso de mensaje de DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![Sección de redacción de mensajes de DOTS.ECO.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Por ejemplo:
- Mostrar la imagen del certificado en un mensaje dentro de la aplicación utilizando {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}
- Enlazar con el certificado alojado utilizando {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![Comportamiento de DOTS.ECO al hacer clic en el mensaje.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Esto te permite personalizar mensajes dentro de la aplicación, Content Cards o notificaciones push con confirmación de impacto.

## Solución de problemas {#troubleshooting}

Revisa los errores de contenido conectado en el panel de Braze en **Configuración** > **Registro de actividad de mensajes**.

- **El contenido conectado devuelve vacío**: Confirma que `:save result` está configurado y que estás haciendo referencia a los campos de respuesta esperados.
- **Los atributos no se muestran en el paso de mensaje**:
  - Confirma que los nombres de los atributos personalizados en Braze coinciden exactamente con los atributos que estableciste en el paso de Actualización de usuario.
  - En el paso de Actualización de usuario, utiliza la pestaña **Vista previa y prueba** para confirmar que los atributos se rellenan. A continuación, envía una prueba a un usuario y confirma que los atributos se guardan en su perfil de usuario.
- **Error `422` (entidad no procesable)**: Confirma que el token de tu aplicación y la cantidad de impacto son válidos.
- **Error `401`**: Confirma que el token de autenticación está presente y es correcto.
- **No hay vista previa de la imagen en el paso de mensaje**: Selecciona **Enviar prueba a usuario** en el paso de Actualización de usuario y, a continuación, obtén una vista previa del mensaje utilizando ese mismo usuario.