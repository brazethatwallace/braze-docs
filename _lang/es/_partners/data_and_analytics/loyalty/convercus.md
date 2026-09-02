---
nav_title: Convercus
article_title: Convercus
description: "Este artículo de referencia describe la integración entre Braze y Convercus, una plataforma de fidelización y cupones que enriquece Braze con datos de fidelización en tiempo real y permite que las Campaigns de Braze desencadenen acciones de fidelización en Convercus."
page_type: partner
search_tag: Partner
---

# Convercus

> [Convercus](https://www.convercus.com/en) es una plataforma SaaS de fidelización y cupones que ayuda a marcas y comercios minoristas a aumentar la frecuencia de compra, el valor de la cesta y las tasas de recompra a través de programas de fidelización omnicanal y campañas de cupones personalizadas.

_Esta integración es mantenida por Convercus._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Convercus es bidireccional: los datos de fidelización fluyen hacia Braze en tiempo real como atributos personalizados, eventos personalizados y compras, y los Canvas y Campaigns de Braze pueden desencadenar acciones de fidelización en Convercus a través de webhooks. Usa el nivel de miembro sincronizado, el saldo de puntos, las compras y la actividad de cupones en Segments, Liquid y contenido conectado. Desde los recorridos de Braze, también puedes asignar cupones, registrar, acumular y canjear transacciones de puntos, y actualizar las preferencias de suscripción de correo electrónico en Convercus.

Convercus aloja la integración, por lo que no necesitas instalar infraestructura adicional. Mientras que la mayoría de los conectores de fidelización solo envían datos en una dirección, Convercus cierra el ciclo: reacciona en Braze a un evento de fidelización, ejecuta una acción en Convercus y mide el resultado de vuelta en Braze.

## Ejemplos {#use-cases}

* **Celebración de ascenso de nivel:** Cuando un miembro sube de nivel en un programa de fidelización en Convercus, desencadena un Canvas personalizado de Braze con un mensaje de bienvenida, un beneficio exclusivo del nivel y el nuevo nivel y saldo de puntos del miembro.
* **Bonificaciones de cumpleaños e hitos:** Desde un recorrido de Braze, registra puntos de bonificación en Convercus en el cumpleaños o aniversario de un miembro y luego envía un mensaje de celebración confirmando el nuevo saldo.
* **Recuperación de miembros inactivos:** Para miembros inactivos, haz que Braze asigne un cupón personalizado en Convercus a través de un webhook y entrégalo a través de correo electrónico, push y mensajes dentro de la aplicación.
* **Saldo de puntos en vivo en la mensajería:** Usa contenido conectado para obtener el saldo de puntos en tiempo real de un miembro en Braze Liquid, impulsando cadencias como "estás a X puntos de tu próxima recompensa".

## Requisitos previos {#prerequisites}

Antes de comenzar, necesitas lo siguiente:

| Requisito previo | Descripción |
| --- | --- |
| Una cuenta de Convercus | Un programa de Convercus activo. Contacta con tu director de cuentas de Convercus si aún no eres cliente. |
| Una clave de API REST de Braze | Una clave de API REST de Braze con el permiso `users.track`. Crea esta clave en el panel de Braze desde **Configuración** > **Claves de API**. |
| Un endpoint REST de Braze | [La URL de tu endpoint REST]({{site.baseurl}}/api/basics#endpoints). Tu endpoint depende de la URL de Braze para tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

Necesitas un identificador de usuario coherente entre los sistemas: el valor utilizado como `external_id` (o el tipo de identificador elegido) en Braze debe coincidir con el identificador de miembro correspondiente en Convercus. De lo contrario, los eventos no se atribuirán al perfil correcto.

## Integración {#integration}

### Paso 1: Configurar Braze en Convercus Selfservice {#step-1-configure-braze-in-convercus-selfservice}

En Convercus Selfservice (la interfaz de administración orientada al cliente; ábrela usando la URL que te proporcione tu director de cuentas de Convercus), abre el programa que deseas conectar a Braze y usa la **tarjeta de integración de Braze** para:

1. Configurar la conexión con Braze completando el formulario de integración:

   | Campo | Descripción |
   | --- | --- |
   | `apiKey` | Tu clave de API REST de Braze (con el permiso `users.track`). |
   | `apiEndpoint` | Tu endpoint REST de Braze, por ejemplo `https://rest.iad-01.braze.com`. |
   | Tipo de identificador | `external_id` o `user_alias`. Determina cómo se emparejan los miembros de Convercus con los perfiles de usuario de Braze. |
   | `defaultOptins` | Selección múltiple de los canales de adhesión voluntaria del programa (de `membershipOptins`). Se usa como valor predeterminado para el webhook de suscripción por correo electrónico cuando la solicitud omite `optins`. La configuración de Braze se considera incompleta hasta que se seleccione al menos uno. |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Configurar Braze en Convercus Selfservice" }

2. Crear una clave de API para las llamadas entrantes. Crea una credencial `X-Convercus-Key` por programa. La clave sin procesar se muestra una sola vez en el momento de la creación, con el prefijo `cvc_` (formato: `cvc_<base64url>`). Almacénala en Braze cuando configures las Campaigns de webhook y los bloques de contenido conectado en el paso 2. Las claves pueden revocarse en cualquier momento desde la misma tarjeta; la revocación surte efecto de inmediato.

Después de guardar la conexión con Braze, Convercus comienza a transmitir de inmediato los eventos de fidelización de ese programa a Braze. No se requiere configuración de infraestructura adicional.

{% alert note %}
Cada programa de Convercus se configura de forma independiente. Un único inquilino de Convercus puede conectar diferentes programas a diferentes espacios de trabajo de Braze, cada uno con su propia clave de API.
{% endalert %}

### Paso 2: Configurar webhooks en Braze {#step-2-configure-webhooks-in-braze}

Para activar acciones de Convercus desde un Canvas o una Campaign, crea acciones de webhook en Braze que llamen al servicio de integración de Convercus. Todas las solicitudes deben incluir los siguientes encabezados:

- `X-Convercus-Key: cvc_…` — la clave de API generada en el paso 1.
- `Content-Type: application/json`

Todos los endpoints se encuentran bajo la URL base `<SERVICE_HOST>/v1/programs/{programId}`. Reemplaza `<SERVICE_HOST>` con el host proporcionado por tu director de cuentas de Convercus y `{programId}` con tu ID de programa de Convercus.

| Acción | Endpoint |
| --- | --- |
| Asignar un cupón a un miembro | `POST /campaigns/{couponId}/assign` — devuelve `{ "couponCode": "..." }`. |
| Asignar un cupón a varios miembros | `POST /campaigns/{couponId}/assign/batch` — hasta 500 miembros en una sola llamada; el cuerpo acepta opcionalmente `valid_from` / `valid_to`. Devuelve `{ "batchId": "..." }`. |
| Registrar puntos ganados / canjeados | `POST /members/{accountId}/bookings` — crea un `EARNBOOKING` o `BURNBOOKING` en la cuenta de un miembro. Devuelve `{ "bookingId": "..." }`. |
| Sincronizar preferencias de suscripción por correo electrónico | `POST /subscriptions/email` — establece las adhesiones voluntarias del miembro en `allowed` o `declined`. Los canales de adhesión voluntaria se resuelven como solicitud `optins` > `defaultOptins`. Devuelve `200` (todo correcto), `207` (parcial — consulta `succeeded` / `failed`) o `400` (adhesiones voluntarias desconocidas o ninguna configurada). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Configurar webhooks en Braze" }

Ejemplo — asignar un cupón a un miembro:

{% raw %}
```text
POST <SERVICE_HOST>/v1/programs/{programId}/campaigns/{couponId}/assign
X-Convercus-Key: cvc_…
Content-Type: application/json

{
  "account_id": "{{custom_attribute.${convercus_account_id}}}",
  "braze_campaign_id": "{{campaign.${api_id}}}"
}
```
{% endraw %}

Las demás acciones siguen el mismo patrón, cambiando solo el endpoint y el cuerpo. Por ejemplo, un registro de puntos se envía a `/members/{accountId}/bookings` con `booking_type` (`EARNBOOKING` o `BURNBOOKING`), `booking_type_code`, `points` y `reason`; el webhook de suscripción por correo electrónico se envía a `/subscriptions/email` con `account_id` y `status` (`allowed` o `declined`).

#### Respuestas de error y reintentos {#error-responses-and-retries}

| Estado | Significado |
| --- | --- |
| `200` | Éxito. |
| `207` | Multi-Estado — solo para el webhook de suscripción por correo electrónico, cuando algunas membresías se actualizaron y otras fallaron. |
| `400` | El cuerpo de la solicitud no pasó la validación. |
| `401` | `X-Convercus-Key` falta o no es válida. |
| `5xx` | La llamada ascendente a Convercus falló. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Respuestas de error y reintentos" }

{% alert warning %}
Las respuestas 5xx no son seguras para reintentar sin confirmar el éxito; estas operaciones no son idempotentes, y los reintentos pueden asignar cupones duplicados o acreditar puntos por duplicado. Desactiva el reintento automático de Braze en 5xx para estos webhooks, o configura un recuento máximo de reintentos muy bajo.
{% endalert %}

### Paso 3: Verificar los datos en Braze {#step-3-verify-data-in-braze}

1. Activa un evento de fidelización en Convercus; por ejemplo, un cambio de nivel de estado, una transacción de puntos o un canje de cupón.
2. Abre el usuario correspondiente en Braze y confirma que el atributo personalizado, el evento personalizado o la compra esperada aparezcan en el perfil. Los usuarios se emparejan por `external_id` (o el tipo de identificador elegido en el paso 1).
3. Para verificar la dirección opuesta, ejecuta un envío de prueba en Braze que llame a uno de los webhooks del paso 2 y confirma la acción en Convercus (cupón asignado, puntos registrados o suscripción actualizada).

## Usar Convercus con Braze {#use-convercus-with-braze}

### Paso 1: Personaliza mensajes con datos de fidelización sincronizados {#step-1-personalize-messages-with-synced-loyalty-data}

Una vez que la integración esté en vivo, los eventos de Convercus llegan a cada perfil de usuario en Braze a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) y se pueden utilizar como cualquier otro dato nativo:

1. Usa atributos personalizados de fidelización (por ejemplo, `convercus_status_level`, `convercus_balance`) en **Segments** para dirigirte a titulares de nivel, miembros con saldo alto o usuarios recientemente degradados.
2. Usa eventos personalizados (por ejemplo, `convercus_status_level_changed`, eventos de cupones y membresías) como **pasos desencadenantes** en Canvas o como filtros en campañas de reactivación.
3. Referencia cualquiera de estos campos en **Liquid** para personalización dentro del mensaje (líneas del asunto, cuerpo del texto, títulos push).
4. Usa eventos `purchase` transmitidos desde Convercus para impulsar recorridos orientados a productos (reposición, venta cruzada de categoría, solicitudes de reseña posteriores a la compra).

#### Atributos personalizados {#custom-attributes}

| Atributo | Descripción |
| --- | --- |
| `convercus_account_id` | El ID de cuenta de Convercus del miembro, único dentro de un programa de Convercus / espacio de trabajo de Braze. |
| `convercus_user_id` | El ID de usuario de Convercus que identifica a la persona subyacente en múltiples programas de Convercus. |
| `convercus_partner_id` | Identificador del partner de Convercus (comerciante/marca) a través del cual se inscribió este miembro. Útil para segmentación en programas de coalición. |
| `convercus_member_role` | El rol del miembro dentro del programa de fidelización. |
| `convercus_status_level` | El nivel o categoría actual del miembro. |
| `convercus_balance` | Objeto con los `points`, `lockedPoints` y `statusPoints` actuales del miembro. |
| `email_subscribe` | Estado de suscripción de correo electrónico derivado de las adhesiones voluntarias de Convercus (`opted_in`, `subscribed` o `unsubscribed`). |
| `push_subscribe` | Estado de suscripción push derivado de los eventos de token de notificaciones push de Convercus (`opted_in` o `unsubscribed`). |
| Campos de perfil estándar | `email`, `phone`, `first_name`, `last_name`, `dob`, `gender`, `home_city`, `country`. |
| Propiedades de usuario personalizadas | Cualquier propiedad personalizada definida en el objeto de usuario de Convercus se reenvía como atributo personalizado de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

{% alert note %}
Dentro de un espacio de trabajo de Braze, los miembros se identifican de forma única mediante `convercus_account_id`. `convercus_user_id` identifica a la persona subyacente en múltiples programas de Convercus y se proporciona para análisis entre programas; para segmentación dentro de Braze, usa `convercus_account_id`.
{% endalert %}

**Mapeado de `email_subscribe`**

| Estado de Convercus | `email_subscribe` de Braze |
| --- | --- |
| Entrada de `allowedOptins` para `email consent` o `newsletter` | `opted_in` |
| Entrada de `declinedOptIns` para esos canales (y sin entrada permitida) | `unsubscribed` |
| Sin registro en ningún sentido | `subscribed` (valor predeterminado neutral de Braze) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

#### Eventos personalizados {#custom-events}

| Evento | Se desencadena cuando |
| --- | --- |
| `convercus_account_created` | Se crea una cuenta nueva en Convercus. |
| `convercus_membership_added` | Una cuenta existente se une a un programa de fidelización. |
| `convercus_membership_created` | Se crea una nueva membresía. |
| `convercus_membership_changed` | Los datos de una membresía cambian. |
| `convercus_membership_optins_changed` | Las preferencias de adhesión voluntaria de un miembro cambian. |
| `convercus_membership_terminated` | Una membresía finaliza. |
| `convercus_status_level_changed` | El nivel o categoría de un miembro cambia. |
| `convercus_balance_changed` | El saldo de puntos de un miembro cambia. |
| `convercus_account_transaction` | Se califica una transacción de fidelización. |
| `convercus_coupon_assigned` | Se asigna un cupón al miembro. |
| `convercus_coupon_redeemed` | El miembro canjea un cupón. |
| `convercus_user_logged_in` | El miembro inicia sesión en una interfaz impulsada por Convercus. |
| `convercus_user_logged_out` | El miembro cierra sesión. |
| `convercus_user_created` | Se crea un nuevo usuario. |
| `convercus_user_changed` | Los datos del perfil de un usuario cambian. |
| `convercus_push_token_created` | Se registra un token de notificaciones push para el miembro. |
| `convercus_push_token_deleted` | Se elimina un token de notificaciones push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos personalizados" }

#### Compras {#purchases}

Las transacciones de Convercus de tipo `EARNTRANSACTION` (puntos ganados por gasto del cliente) se reportan a Braze como [compras]({{site.baseurl}}/api/objects_filters/purchase_object) y se contabilizan en los análisis de ingresos de Braze, segmentación RFM y características predictivas, utilizando el ID de transacción como identificador de producto y el monto y la moneda de la transacción como precio y moneda.

Las transacciones de tipo `PAYWITHPOINTSTRANSACTION` (quema de puntos) **no** se reportan como compras; fluyen como el evento personalizado `convercus_account_transaction` para que permanezcan disponibles para segmentación. Las reversiones y cancelaciones de transacciones de ganancia se reportan como compras con precio negativo, manteniendo los ingresos de Braze alineados con Convercus.

### Paso 2: Obtén datos de fidelización en vivo con contenido conectado {#step-2-fetch-live-loyalty-data-with-connected-content}

Para valores que deben estar actualizados en el momento del envío —saldo de puntos actual, cupones activos, nivel más reciente— llama a Convercus desde Braze usando [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) en lugar de depender del atributo sincronizado más recientemente. Ambos endpoints se encuentran bajo la misma URL base que los webhooks y requieren el encabezado `X-Convercus-Key`.

| Datos | Endpoint | Devuelve |
| --- | --- | --- |
| Perfil del miembro | `GET /members/{accountId}/profile` | `member_id`, `first_name`, `last_name`, `email`, `tier_name`, `tier_id`, `points_balance`, `enrollment_date`. |
| Cupones del miembro | `GET /members/{accountId}/coupons` | Lista de cupones activos y canjeables (estado, valor, ventana de validez, título, descripción). Agrega `?lang=<code>` (por ejemplo, `?lang=de`) para localizar `title`/`description`; el valor predeterminado es `en`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Obtén datos de fidelización en vivo con contenido conectado" }

Los endpoints de contenido conectado siempre devuelven HTTP 200 en fallos esperados para que las plantillas de Liquid puedan ramificarse según el campo `error`:

| Respuesta | Significado |
| --- | --- |
| `200` + carga útil | Éxito. |
| `200 { "error": "member_not_found" }` | La cuenta no existe en este programa. |
| `200 { "error": "internal_error" }` | Fallo upstream o inesperado. |
| `401` | `X-Convercus-Key` falta o es inválido (manéjalo en el momento de la integración, no en Liquid). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Obtén datos de fidelización en vivo con contenido conectado" }

Ejemplo — renderiza el estado de fidelización de un miembro (nivel, puntos y ofertas activas):

{% raw %}
```liquid
{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/profile
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 300
  :retry
  :save member
%}

{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/coupons?lang=en
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 0
  :retry
  :save coupon_data
%}

{% unless member.error %}
  <h2>Your Loyalty Status</h2>
  <p>Hi {{member.first_name}}, you're a <strong>{{member.tier_name}}</strong> member.</p>
  <p>Points balance: <strong>{{member.points_balance}}</strong></p>

  {% if coupon_data.coupons.size > 0 %}
    <h3>Your Active Offers</h3>
    {% for coupon in coupon_data.coupons %}
      <p><strong>{{coupon.title}}</strong> — valid until {{coupon.valid_to}}</p>
    {% endfor %}
  {% endif %}
{% endunless %}
```
{% endraw %}

Envuelve siempre el contenido conectado en condicionales (verifica `member.error` y `coupons` vacío) para que un fallo temporal de búsqueda nunca envíe un mensaje roto. Almacena en caché el perfil (`cache_max_age 300`) pero no los cupones (`cache_max_age 0`), ya que el estado de los cupones puede cambiar entre envíos.

## Consideraciones {#considerations}

- **Latencia:** Los eventos de Convercus a Braze se propagan a través de Kafka y llegan a Braze en segundos bajo carga normal.
- **Límites de velocidad de Braze:** La integración reintenta automáticamente ante respuestas `429`, respetando el encabezado `x-ratelimit-retry-after` de Braze con retirada exponencial.
- **Caché de contenido conectado:** Braze almacena en caché las respuestas de contenido conectado durante varios minutos de forma predeterminada. Para valores que deben ser exactos en el momento del envío (como el saldo de puntos), reduce o evita la ventana de caché en la llamada de contenido conectado.
- **Una configuración por programa:** Cada programa de fidelización se mapea a un único espacio de trabajo de Braze. Para conectar un segundo espacio de trabajo, configúralo en un programa independiente.
- **Observabilidad:** Las estadísticas de llamadas a la API por programa y el historial de errores (en ambas direcciones) se conservan durante 90 días y están disponibles desde la tarjeta de integración de Braze en Selfservice.

## Solución de problemas {#troubleshooting}

- **Los eventos no aparecen en Braze:** Verifica que el valor utilizado como identificador (seleccionado en el paso 1) coincida con el `external_id` del usuario (o el tipo de identificador elegido) en Braze. Los identificadores que no coinciden hacen que los eventos se atribuyan al perfil incorrecto o se descarten.
- **El webhook devuelve `401`:** Falta el encabezado `X-Convercus-Key` o la clave de API `cvc_…` ha sido revocada. Regenera la clave en Selfservice y actualiza la acción del webhook en Braze.
- **El webhook devuelve `400`:** Falta `Content-Type: application/json` en la solicitud, o la carga útil no coincide con el esquema documentado. Para el webhook de suscripción por correo electrónico, un `400` también significa que las adhesiones voluntarias solicitadas son desconocidas para el programa o no hay ninguna configurada.
- **Depuración más profunda:** Revisa las estadísticas de llamadas a la API por programa y el historial de errores en la tarjeta de integración de Braze en Selfservice, o contacta a tu representante de Convercus.