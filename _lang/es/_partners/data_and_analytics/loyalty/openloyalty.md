---
nav_title: Open Loyalty
article_title: Open Loyalty
description: "La integración de Braze y Open Loyalty te permite sincronizar datos de fidelización —como saldo de puntos, cambios de nivel y advertencias de caducidad— directamente en Braze en tiempo real."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Open Loyalty

> [Open Loyalty](https://www.openloyalty.io/) es una plataforma de programas de fidelización basada en la nube que te permite crear y gestionar programas de recompensas y fidelización de clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización —como el saldo de puntos, los cambios de nivel y las advertencias de caducidad— directamente en Braze en tiempo real. Esto te permite desencadenar mensajes personalizados (correo electrónico, push, servicio de mensajes cortos) cuando cambia el estado de fidelización de un usuario.

_Esta integración la mantiene Open Loyalty_

## Sobre la integración {#about-the-integration}

Esta integración utiliza Transformación de datos de Braze para capturar webhooks de Open Loyalty y mapearlos a perfiles de usuario de Braze.

* **Actualizaciones en tiempo real**: Envía eventos de fidelización (puntos ganados, subidas de nivel) a Braze.
* **Personalización**: Utiliza atributos de fidelización (saldo actual, nombre del siguiente nivel) en tus plantillas de Braze.
* **Bidireccional**: Actualiza los atributos personalizados de los clientes de Open Loyalty basándote en los datos de participación de Braze.

## Ejemplos {#use-cases}

Esta integración abarca los siguientes flujos de datos:

1. **Sincronizar eventos con Braze (de entrada)**: Realiza un seguimiento de los cambios de puntos, las subidas de nivel o los canjes de recompensas enviando datos de Open Loyalty a Braze. La Transformación de datos convierte estos datos en un evento de usuario.
2. **Modificar miembros de Open Loyalty (de salida)**: Actualiza automáticamente los datos de los miembros en Open Loyalty en función del comportamiento del usuario en Braze, como añadir etiquetas "VIP" o actualizar atributos personalizados.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitas lo siguiente:

| Requisito | Descripción |
| :--- | :--- |
| Cuenta de Open Loyalty | Necesitas una cuenta de administrador en un tenant de Open Loyalty para aprovechar esta asociación. |
| Clave de API REST or transferencia de estado representacional de Open Loyalty | Una clave de API REST or transferencia de estado representacional de Open Loyalty (para integraciones que envían datos de Braze a Open Loyalty). <br><br> Créala en **Settings > Admins > API Keys**. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. <br><br> Crea esta clave en el panel de Braze desde **Configuración** > **Claves de API**. |
| Transformación de datos de Braze | Necesitas acceder a la pestaña "Data Settings" en Braze para configurar los listeners de webhook. |
| ID coincidentes | El `external_id` del usuario en Braze debe coincidir con su `loyaltyCardNumber` (u otro identificador predeterminado) en Open Loyalty. |
| ID de tenant | Tu ID de tenant de Open Loyalty (necesario para las actualizaciones de salida). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

La integración principal sincroniza los eventos webhook de Open Loyalty con Braze mediante Transformación de datos.

### Paso 1: Generar la URL del webhook en Braze {#step-1-generate-the-webhook-url-in-braze}

Primero, crea una transformación de datos en Braze para generar una URL única para recibir datos.

1.  En Braze, abre **Data Settings > Data Transformation**.
2.  Haz clic en **Create Transformation**.
3.  Completa los siguientes campos:
     * **Transformation name**: Proporciona un nombre descriptivo (por ejemplo, "Open Loyalty Point Update Events").
     * **Select destination**: Elige **POST: Track users**.
4.  Haz clic en **Create Transformation**.
5.  Localiza la **Webhook URL** en el panel de detalles y haz clic en **Copy**.

{% alert important %}
Guarda bien esta URL; la necesitas para el siguiente paso.
{% endalert %}

### Paso 2: Crear la suscripción al webhook en Open Loyalty {#step-2-create-the-webhook-subscription-in-open-loyalty}

Indica a Open Loyalty que envíe eventos específicos a la URL que acabas de generar.

1.  Inicia sesión en tu panel de administración de Open Loyalty.
2.  Ve a **General > Webhooks**.
3.  Haz clic en **Add new webhook** y configura la suscripción:
    * **eventName**: Selecciona el evento del que quieres hacer un seguimiento (por ejemplo, `AvailablePointsAmountChanged`, `CustomerLevelChanged` o `CampaignEffectWasApplied`).
    * **url**: Pega la URL del webhook de Braze del paso 1.
    * Añade los siguientes encabezados:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Guarda la suscripción al webhook.

### Paso 3: Configurar la transformación de datos {#step-3-configure-the-data-transformation}

Escribe la lógica JavaScript en Braze para mapear la carga útil entrante de Open Loyalty a propiedades de Braze.

1.  En Braze, abre la transformación de datos que creaste en el paso 1.
2.  Desencadena el evento en Open Loyalty (por ejemplo, cambia los puntos de un miembro o asigna un nivel) para generar una carga útil de muestra en el panel de **Webhook details**.
3.  En el editor de **Transformation code**, escribe un script para mapear los datos entrantes. Utiliza el siguiente ejemplo como guía:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,

      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",

      // timestamp
      "time": new Date().toISOString(),

      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. Haz clic en **Validate** para asegurarte de que el código se ejecuta con tu carga útil de muestra y, a continuación, haz clic en **Activate**.


## Usar Open Loyalty con Braze {#using-open-loyalty-with-braze}

Una vez completada la integración de entrada, configura las **actualizaciones de salida** para modificar los miembros de Open Loyalty en función del comportamiento en Braze.

### Paso 1: Configurar una Campaign de webhook en Braze {#step-1-configure-braze-webhook-campaign}

Este proceso utiliza webhooks de Braze para enviar una solicitud `PATCH` a la API de miembros de Open Loyalty (por ejemplo, para añadir una etiqueta "VIP").

1.  En Braze, crea una nueva **Campaign de webhook** (o utiliza un webhook dentro de un Canvas).
2.  Haz clic en **Compose Webhook**.
3.  **Webhook URL**: Construye la URL utilizando tu instancia de Open Loyalty, el ID de tenant y la variable Liquid de Braze para el ID de usuario.
    * Formato:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Completa los siguientes campos:
    * **Request Method**: `PATCH`
    * **Request Headers**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Request Body**: Selecciona `Raw text` y pega la carga útil:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Paso 2: Configurar el desencadenador {#step-2-configure-the-trigger}

1.  Ve a la pestaña **Delivery** o **Entry Schedule**.
2.  Completa los siguientes campos:
    * **Delivery Method**: Action-Based.
    * **Trigger**: Define el desencadenador correspondiente (por ejemplo, un usuario entra en un Segment específico en Braze).
    * **Launch**: Activa la Campaign.

## Solución de problemas {#troubleshooting}

### Verificar eventos de entrada {#verify-inbound-events}
Cuando la transformación de datos está activa, los datos aparecen en Braze como un evento personalizado. Compruébalo creando una Campaign con un desencadenador **Perform Custom Event** y verificando si el evento que definiste (por ejemplo, `Loyalty Event Triggered`) está disponible.

### Verificar webhooks de salida {#verify-outbound-webhooks}
Comprueba el registro de actividad de mensajes en Braze para asegurarte de que el webhook devolvió un estado `200 OK`.
* **Error 401**: Comprueba tu token de la API de Open Loyalty.
* **Error 404**: El ID de usuario en Braze no existe en Open Loyalty.