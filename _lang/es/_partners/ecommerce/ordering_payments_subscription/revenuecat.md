---
nav_title: RevenueCat
article_title: RevenueCat
description: "La integración de RevenueCat y Braze te permite sincronizar automáticamente los eventos del ciclo de vida de compra y suscripción de tus clientes en todas las plataformas. Esto te permite crear campañas que reaccionen a la etapa del ciclo de vida de suscripción de tus clientes, como interactuar con clientes que cancelaron durante su prueba gratuita o enviar recordatorios a clientes con problemas de facturación."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) es la única fuente de verdad para el estado de tu suscripción en iOS, Android y web. Tanto si estás creando una nueva aplicación como si ya tienes millones de suscriptores, puedes usar RevenueCat para crear compras dentro de la aplicación multiplataforma, gestionar tus productos y suscriptores, y analizar tus datos, sin necesidad de código de servidor.

_Esta integración está mantenida por RevenueCat._

## Sobre la integración {#about-the-integration}

La integración de RevenueCat y Braze te permite sincronizar automáticamente los eventos del ciclo de vida de compra y suscripción de tus clientes en todas las plataformas. Esto te permite crear campañas que reaccionen a la etapa del ciclo de vida de suscripción de tus clientes, como interactuar con clientes que cancelaron durante su prueba gratuita o enviar recordatorios a clientes con problemas de facturación.

## Requisitos previos {#prerequisites}

Como mínimo, necesitarás habilitar la integración desde el dashboard de RevenueCat para conectar RevenueCat con Braze. Si estás usando el SDK de Braze, puedes usar los SDK de RevenueCat y Braze juntos para mejorar la integración asegurándote de que se utiliza el mismo identificador de cliente en ambos sistemas.

| Requisito | Descripción |
|---|---|
| Cuenta y aplicación de RevenueCat | Se necesita una [cuenta de RevenueCat](https://app.revenuecat.com/login) para aprovechar esta asociación. También debes tener una aplicación de RevenueCat configurada. |
| SDK de RevenueCat | Además del SDK de Braze requerido, recomendamos instalar el [SDK de RevenueCat](https://docs.revenuecat.com/docs/configuring-sdk) para proporcionar alias de usuario a RevenueCat. |
| Instancia de Braze | Tu instancia de Braze puede obtenerse a través de tu administrador de incorporación de Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat requiere la instancia de Braze para enviar desde el servidor al punto de conexión REST de Braze correcto. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Clave de API REST de prueba de Braze (opcional) | Se puede usar una clave de API de prueba para compras de prueba y producción si deseas que estas solicitudes se envíen a instancias de Braze independientes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

- Activa una Campaign de incorporación que destaque tus funciones premium cuando un cliente inicie una prueba gratuita.
- Envía un recordatorio para actualizar la información de facturación cuando se reciba un evento de "Problema de facturación".
- Envía un cuestionario de opinión después de que un cliente cancele una prueba gratuita.

## Integración {#integration}

### Paso 1: Establecer la identidad de usuario de Braze {#step-1-set-braze-user-identity}

En el SDK de Braze, puedes configurar el ID de usuario de Braze para que coincida con el ID de usuario de la aplicación RevenueCat, lo que garantiza que los eventos enviados desde Braze y RevenueCat puedan sincronizarse con el mismo usuario.

Configura el SDK de Braze con el mismo ID de usuario de la aplicación que RevenueCat o usa el método `.changeUser()` del SDK de Braze.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name",
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Enviar objeto alias de usuario a Braze (opcional) {#send-user-alias-object-to-braze-optional}

Si deseas enviar un identificador de usuario único alternativo distinto del ID de usuario de la aplicación RevenueCat, actualiza los usuarios con los siguientes datos como atributos de suscriptor de RevenueCat.

| Clave | Descripción |
|---|---|
| `$brazeAliasName` | El `alias_name` de Braze en el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
| `$brazeAliasLabel` | El `alias_label` de Braze en el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Send user alias object to Braze (optional)" }

Ambos atributos son necesarios para que el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/) se envíe junto con los datos del evento. Estas propiedades pueden configurarse manualmente, como cualquier otro [atributo de suscriptor de RevenueCat](https://docs.revenuecat.com/docs/subscriber-attributes). En el paso uno se muestran fragmentos de código de ejemplo.

### Paso 2: Enviar eventos de RevenueCat a Braze {#step-2-send-revenuecat-events-to-braze}

Después de configurar el SDK de compras de RevenueCat y el SDK de Braze para que tengan la misma identidad de usuario, puedes activar la integración y configurar los nombres de los eventos desde el dashboard de RevenueCat.

1. Navega hasta tu proyecto en el dashboard de RevenueCat y busca la tarjeta **Integrations** en el menú de la izquierda. Selecciona **+ New**.
2. A continuación, selecciona **Braze** entre las integraciones disponibles y añade tu instancia de Braze y tu clave de API REST de Braze.
3. Introduce los nombres de eventos que RevenueCat enviará o elige los nombres de eventos predeterminados. Encontrarás más información sobre los eventos disponibles en el [paso 3](#configure-event-names).
4. Selecciona si deseas que RevenueCat informe de los ingresos netos (después del corte de la tienda de aplicaciones) o de los ingresos brutos (ventas brutas).

![Configuración de Braze en RevenueCat con campos para la instancia de Braze, el identificador de la clave de API y el identificador del sandbox.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Paso 3: Configurar los nombres de los eventos {#configure-event-names}

Introduce los nombres de eventos que RevenueCat enviará o selecciona entre los nombres de eventos predeterminados seleccionando **Use Default Event Names**. Los eventos que RevenueCat admite enviar se describen en el siguiente cuadro.

| Evento | Descripción |
|---|---|
| Compra inicial | La primera compra de un producto de suscripción con renovación automática que no contenga una prueba gratuita. |
| Prueba iniciada | El inicio de una prueba gratuita de un producto de suscripción con renovación automática. |
| Prueba convertida | Cuando un producto de suscripción con renovación automática pasa de un periodo de prueba gratuito a un periodo normal de pago. |
| Prueba cancelada | Cuando un usuario desactiva las renovaciones de un producto de suscripción con renovación automática durante un periodo de prueba gratuito. |
| Renovación | Cuando se renueva un producto de suscripción con renovación automática, o un usuario vuelve a comprar el producto de suscripción con renovación automática tras un lapso en su suscripción. |
| Cancelación | Cuando un usuario desactiva las renovaciones de un producto de suscripción con renovación automática durante el periodo de pago normal. |
| Compra sin suscripción | La compra de cualquier producto que no sea una suscripción con renovación automática. |
| Caducidad | Cuando caduca una suscripción. |
| Problema de facturación | Cuando ha habido un problema al intentar cobrar al usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Configure event names #configure-event-names" }

Para los eventos que incluyan ingresos, RevenueCat registrará automáticamente este importe junto con el evento en Braze, como las conversiones de prueba y las renovaciones.

## Uso de esta integración {#using-this-integration}

Después de configurar los ajustes de Braze en RevenueCat, los eventos comenzarán a fluir automáticamente de RevenueCat a Braze sin ninguna otra acción de tu parte.

## Personalización {#customization}

### Añadir una clave de API de sandbox para pruebas {#add-a-sandbox-api-key-for-testing}

Si solo proporcionas una clave de API REST de Braze a RevenueCat, solo se enviarán los eventos de producción. Si también quieres enviar eventos de prueba de sandbox, [crea otra clave de API REST de Braze]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) y añádela a tu configuración de Braze en RevenueCat.