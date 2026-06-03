---
nav_title: Friendbuy
article_title: Friendbuy
description: "Aprende a integrar Friendbuy con Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Utiliza la integración entre [Friendbuy](https://www.friendbuy.com/) y Braze para ampliar tus capacidades de correo electrónico y SMS, a la vez que automatizas sin esfuerzo las comunicaciones de tus programas de referidos y fidelización. Braze generará perfiles de cliente para todos los números de teléfono de adhesión voluntaria recogidos a través de Friendbuy.

_Esta integración está mantenida por Friendbuy._

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito previo | Descripción |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta Friendbuy | Es necesario tener una [cuenta Friendbuy](https://retailer.friendbuy.io/) para beneficiarse de esta asociación. |
| Una clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Un punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende de la URL de tu instancia de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de Friendbuy {#integrating-friendbuy}

En [Friendbuy](https://retailer.friendbuy.io/), ve a **Developer Center** > **Integrations** y, en la tarjeta de integración de Braze, selecciona **Add integration**.

![La tarjeta de integración de Braze en Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

En el formulario, introduce tu punto de conexión REST y tu clave de API y, a continuación, selecciona **Install Integration**.

![El formulario de integración de Friendbuy.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Vuelve a tu [cuenta Friendbuy](https://retailer.friendbuy.io/) y actualiza la página. Si la integración se ha realizado correctamente, aparecerá un mensaje similar al siguiente:

![Integración instalada]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Atributos personalizados {#custom-attributes}

| Nombre de atributo personalizado | Definición | Tipo de datos |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status** | Los recomendantes se clasifican como *Advocate* y los recomendados como *Referred Friend*. | Cadena |
| **Friendbuy Customer Name** | El nombre que el cliente introdujo al enviar su información a través de un widget de referidos. | Cadena |
| **Friendbuy Referral Link** | Un enlace personal de referidos (PURL) generado para un Advocate. Por ejemplo, https://fbuy.io/EzcW | Cadena |
| **Friendbuy Date of Last Share** | La fecha y hora en que el Advocate compartió por última vez con un amigo a través de cualquier canal de compartición. Si el Advocate aún no ha compartido, la propiedad no será visible. | Tiempo |
| **Friendbuy Campaign ID** | El identificador de campaña asociado al enlace de referidos personal generado para un Advocate. | Cadena |
| **Friendbuy Campaign Name** | El nombre de campaña asociado al enlace de referidos personal generado para un Advocate. | Cadena |
| **Friendbuy Coupon Code** | El último código de cupón de referidos distribuido al cliente. Nota: solo se mostrará un código. | Cadena |
| **Friendbuy Coupon Value** | El valor monetario del último código de cupón distribuido al cliente. | Número |
| **Friendbuy Coupon Status** | El estado del último código de cupón distribuido al cliente. Nota: el estado será "distributed" o "redeemed". | Cadena |
| **Friendbuy Coupon Currency** | Código de moneda (USD, CAD, etc.) o porcentaje (%) asociado al último código de cupón distribuido al cliente. | Cadena |
| **Friendbuy Coupon Campaign ID** | El ID de campaña asociado al código de cupón generado para un cliente. | Cadena |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos personalizados" }

## Comportamiento predeterminado {#default-behavior}

Antes de que los datos de clientes puedan enviarse a Braze, los clientes deben dar su adhesión voluntaria a través del widget de referidos marcando una o más de las siguientes casillas:

![Widget de referidos]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy utiliza la norma internacional (E.164) para verificar los números de teléfono reales. Los números no válidos, como `555-555-5555`, no se enviarán a Braze.
{% endalert %}

### Comportamiento de las casillas de verificación {#checkbox-behavior}

| Casilla seleccionada | Comportamiento |
|-------------------|-----------------------------------------------------------------|
| Solo correo electrónico | Solo se envía a Braze la dirección de correo electrónico del cliente. |
| Solo teléfono | Solo se envía a Braze el número de teléfono del cliente. |
| Ninguna | No se envía ningún dato del cliente a Braze. |
| Ambas | La dirección de correo electrónico y el número de teléfono del cliente se envían a Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamiento de las casillas de verificación" }