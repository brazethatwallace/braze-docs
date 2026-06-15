---
nav_title: Generación dinámica de código
article_title: Generación dinámica de código Punchh
page_order: 2
description: "Este artículo de referencia describe cómo utilizar la generación dinámica de código Punchh en Braze."
page_type: partner
search_tag: Partner
---

# Generación dinámica de código con Punchh {#dynamic-code-generation-with-punchh}

> Un código de cupón es un código único que puede ser utilizado por un solo usuario (ya sea de uso único o múltiple). El marco Punchh genera códigos de cupón, que pueden procesarse dentro de una aplicación móvil o en el sistema de punto de venta (TPV).

_Esta integración está mantenida por Punchh._

## Sobre la integración {#about-the-integration}

Utilizando el marco de cupones Punchh y Braze, puedes lograr los siguientes escenarios:

- Generar un código de cupón cuando el invitado haga clic en un enlace de generación de cupón en un correo electrónico: el código del cupón se generará dinámicamente y se mostrará en una página web.
- Generar un código de cupón cuando el invitado abra un correo electrónico: el código del cupón se generará dinámicamente y se mostrará como una imagen dentro del correo electrónico.

## Integración de la generación dinámica de códigos de cupón {#integrating-dynamic-coupon-code-generation}

### Paso 1: Crear una campaña de cupones {#step-1-create-a-coupon-campaign}

1. Utilizando una campaña de cupones Punchh, crea una campaña de cupones de generación dinámica como se muestra en la siguiente imagen.
2. El marco de cupones Punchh generará los siguientes parámetros para permitir la generación dinámica de cupones:
    - Token dinámico de generación de cupones: se trata de un token de seguridad generado por el sistema para la encriptación.
    - URL de generación de cupones dinámicos: esta URL se incrustará en el correo electrónico como enlace o imagen, según requiera la empresa.

![El formulario para crear una campaña de cupones en Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Paso 2: Generar firma y construir URL {#step-2-generate-signature-and-construct-url}

La biblioteca JWT.IO descodifica, verifica y genera tokens web JSON, un método abierto RFC 7519 estándar del sector para representar reclamaciones de forma segura entre dos partes.

Los siguientes nombres `ClaimType` pueden utilizarse para garantizar la unicidad de los invitados y los cupones:

- `campaign_id`: representa el ID de Campaign Punchh generado por el sistema.
- `email`: representa la dirección de correo electrónico del usuario.
- `first_name`: captura el nombre del usuario.
- `last_name`: captura el apellido del usuario.

Para utilizar la API de código de cupón dinámico de Punchh, debe construirse un token JWT. Añade la siguiente plantilla Liquid al dashboard de Braze en el cuerpo del mensaje del canal que deseas utilizar:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


Sustituye lo siguiente:

| Marcador de posición | Descripción |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Tu token de generación de cupones dinámicos. |
| `CAMPAIGN_ID`                     | Tu ID de Campaign.                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Generar firma y construir URL" }

### Paso 3: Añadir el código del cupón al cuerpo del mensaje {#step-3-append-coupon-code-to-message-body}

#### Enlace a la página web de Punchh {#linking-to-punchh-web-page}

Para enlazar con una página web alojada en Punchh, añade `{% raw %}{{jwt}}{% endraw %}` a la URL de generación dinámica [que creaste anteriormente](#step-1-create-a-coupon-campaign-in-punchh). Tu enlace debe ser similar al siguiente:

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

Cuando un usuario haga clic en la URL del cupón, será redirigido a una página web alojada en Punchh, donde se mostrará el cupón generado.

![Ejemplo de mensaje de confirmación después de que un usuario genere con éxito un código de cupón.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Extracción de código mediante JSON como texto sin formato {#extracting-code-via-json-as-plain-text}

Para devolver una respuesta JSON, añade `{% raw %}{{jwt}}{% endraw %}` a la URL de generación dinámica [que creaste anteriormente](#step-1-create-a-coupon-campaign-in-punchh) y, a continuación, añade `.json` después del token en la cadena de URL. Tu enlace debe ser similar al siguiente:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

A continuación, puedes aprovechar el [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) para insertar el código como texto sin formato en el cuerpo de cualquier mensaje. Por ejemplo:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Enlazar una imagen dentro del contenido de un correo electrónico {#linking-an-image-inside-email-content}

Para enlazar el código del cupón dentro de una imagen:

1. Añade `{% raw %}{{jwt}}{% endraw %}` a la URL de generación dinámica [que creaste anteriormente](#step-1-create-a-coupon-campaign-in-punchh).
2. Añade `.png` después del token en la cadena de URL.
3. Inserta tu enlace en una etiqueta HTML {% raw %}`<img>`{% endraw %}.

{% tabs local %}
{% tab ejemplo de entrada %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab ejemplo de salida %}
![Salida renderizada de la etiqueta de imagen del código del cupón.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Mensajes de error {#error-messages}

| Código de error | Mensaje de error | Descripción |
| --- | --- | --- |
| `coupon_code_expired` | This promo code has expired | El código se utiliza después de su fecha de caducidad configurada. |
| `coupon_code_success` | Congratulations, Promo Code Applied Successfully. | El código se utiliza correctamente. |
| `coupon_code_error` | Please enter a valid promo code | El código utilizado no es válido. |
| `coupon_code_type_error` | Incorrect coupon type. This coupon can only be redeemed at `%{coupon_type}`. | Cuando un código que se supone que debe utilizarse en el TPV se utiliza en la aplicación móvil, se producirá este error. |
| `usage_exceeded` | The usage for this coupon code's campaign is full. Please try next time. | El uso del código supera el número de usuarios autorizados a utilizarlo. Por ejemplo, si la configuración del dashboard permite que un código sea utilizado por 3000 usuarios y el número de usuarios supera los 3000, se producirá este error. |
| `usage_exceeded_by_guest` | This promo code has already been processed. | El uso del código por un usuario supera el número de veces que un usuario puede utilizarlo. Por ejemplo, la configuración del dashboard permite que un mismo código sea utilizado tres veces por un usuario. Si se utiliza más veces, se producirá este error. |
| `already_used_by_other_guest` | This promo code has already been used by some other guest. | Otro usuario ya ha utilizado el código. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes de error" }