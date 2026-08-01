---
nav_title: Objetos de cuenta
article_title: Objetos de cuenta
page_type: reference
permalink: /account_object/
hidden: true
description: "Aprende a usar objetos de cuenta para crear segmentos de usuarios según la cuenta a la que pertenecen y luego enviar mensajes personalizados usando etiquetas de Liquid."
---

# Objetos de cuenta {#account-objects}

> Aprende a usar objetos de cuenta para crear segmentos de usuarios según la cuenta a la que pertenecen y luego enviar mensajes personalizados usando etiquetas de Liquid.

Para importar datos de cuenta, usa un [archivo CSV](#using-a-csv-file) o la API de Braze. Usando la API de Braze, puedes [crear múltiples cuentas](#create-multiple-accounts), [crear una cuenta](#create-one-account), [eliminar múltiples cuentas](#delete-multiple-accounts) y [eliminar una cuenta](#delete-one-account).

| Audiencia | Cómo usarás este artículo |
|----------|----------------------------|
| Especialistas en marketing | Importar datos de usuarios y cuentas usando CSV, crear segmentos basados en atributos de cuenta y personalizar mensajes con información de cuenta en Braze. |
| Desarrolladores | Usar la REST API de Braze para crear, actualizar y eliminar registros de cuenta de forma programática y mantener Braze sincronizado con tus datos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Los objetos de cuenta están actualmente en beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en esta beta.
{% endalert %}

## Cómo funciona {#how-it-works}

Los objetos de cuenta son estructuras de datos personalizadas que representan la empresa de un usuario. Se conectan a los perfiles de usuario, para que puedas crear segmentos de estilo B2B y personalizar mensajes. Usa campos de cuenta como nombre de la empresa, sector, rol o estado de la operación con catálogos de Braze, filtros de segmentación y etiquetas de Liquid.

Por ejemplo, puedes dirigirte a usuarios que trabajan en el sector sanitario y enviar mensajes personalizados a médicos y administradores de hospitales para que tu mensaje sea aún más relevante.

Para usar objetos de cuenta, importas tres tipos de datos en Braze:

- **Datos de usuario:** Perfiles de usuario individuales que se usan para identificar a cada persona en Braze (por ejemplo, a través de `external_id`, correo electrónico, teléfono o alias de usuario). Importa datos de usuario a través de CSV.
- **Datos de relación usuario-cuenta:** La relación entre un usuario y una cuenta, incluyendo a qué empresa pertenece y el rol que tiene en esa cuenta. Importa estos datos de relación a través de CSV.
- **Datos de cuenta:** Los propios registros de la empresa, como nombre de la empresa, sector, ingresos anuales y otros detalles firmográficos. Estos son los registros que usas para segmentar y personalizar en Segments y mensajes. Importa datos de cuenta a través de CSV o la REST API de Braze.

Los tres tipos de datos deben importarse para que los objetos de cuenta funcionen. Los datos de usuario identifican a las personas en Braze, los datos de relación usuario-cuenta conectan a esos usuarios con cuentas y roles específicos, y los datos de cuenta proporcionan los atributos a nivel de empresa que se usan para la segmentación y la personalización.

## Requisitos previos {#prerequisites}

Antes de poder usar esta característica, ya debes tener usuarios en Braze.

## Importar datos a Braze {#import-data-to-braze}

Para usar objetos de cuenta dentro de tus mensajes, tus datos de usuario ya deben existir en Braze. A partir de ahí, completa dos importaciones: primero, importa los datos de relación usuario-cuenta para establecer las asociaciones y roles de cuenta (actualmente solo mediante CSV). Luego, importa los datos de cuenta con los detalles a nivel de empresa utilizados para la segmentación y personalización (mediante CSV o la REST API de Braze).

### Paso 1: Importar datos de relación usuario-cuenta {#step-1-import-user-account-relationship-data}

Primero, importa tus datos de relación usuario-cuenta a Braze como un archivo CSV con los siguientes campos. Esto ayuda a Braze a asociar los usuarios existentes con las cuentas y roles correctos.

<style>
table td {
    word-break: break-word;
}
</style>

| Nombre del campo | Tipo de campo | Obligatorio | Descripción |
|------------------|---------------|-------------|-------------|
| `account_id` | String | Sí | La cuenta a la que pertenece el usuario. Es el mismo que el campo `id` del objeto de cuenta (ID de CRM). |
| `external_id` | String | Sí | El [ID externo](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) del usuario en Braze. |
| `user_alias_name` | String | No* | El [nombre de alias](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases) del usuario en Braze. |
| `user_alias_label` | String | No* | La [etiqueta de alias](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users) del usuario en Braze. |
| `email` | String | No* | La dirección de correo electrónico del usuario. |
| `phone` | String | No* | El número de teléfono del usuario. |
| `user_role` | String | No | El rol que tiene el usuario en la cuenta, como "director" o "empleado". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
<sup>Se requiere uno de `external_id`, `email`, `phone` o `user_alias` para identificar a un usuario.</sup>

#### Usar un archivo CSV {#using-a-csv-file}

Sube tu CSV con las relaciones usuario-cuenta a Braze:

1. Ve a **Data Settings** > **Accounts**.
2. Selecciona **Update data**.
3. En **CSV upload**, selecciona **Users** y luego sube tu archivo a Braze.

![El menú desplegable "Upload data" en la página "Accounts" en Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Paso 2: Importar datos de cuenta {#step-2-import-account-data}

Las cuentas son empresas a las que pertenecen tus usuarios. Importa tus datos de cuenta a Braze como un archivo CSV con los siguientes campos. Ten en cuenta que a cada cuenta se le debe asignar un ID y un nombre.

<style>
table td {
    word-break: break-word;
}
</style>

| Nombre del campo | Tipo de campo | Obligatorio | Descripción |
|------------------|---------------|-------------|-------------|
| `id` | String | Sí | El ID de la cuenta en tu plataforma de administración de las relaciones con el cliente (CRM). |
| `name` | String | Sí | El nombre de la cuenta. |
| `type` | String | No | El tipo de cuenta, como cliente, partner o revendedor. |
| `annual_revenue` | String | No | Ingresos anuales de la cuenta. |
| `industry` | String | No | Industria en la que opera la cuenta. |
| `number_of_employees` | String | No | Número de empleados, admite rangos. |
| `address` | String | No | Dirección de la cuenta. |
| `city` | String | No | Ciudad donde se encuentra la cuenta. |
| `state` | String | No | Estado donde se encuentra la cuenta. |
| `postal_code` | String | No | Código postal de la dirección de la cuenta. |
| `country` | String | No | País donde se encuentra la cuenta. |
| `notes` | String | No | Notas adicionales sobre la cuenta. |
| `website` | String | No | URL del sitio web de la cuenta. |
| `main_phone` | String | No | Número de teléfono principal de la cuenta. |
| `created_date` | Time | No | Fecha en que se creó la cuenta. |
| `account_owner_email_address` | String | No | Un propietario interno de la cuenta (como "Tom del equipo de ventas de la Empresa A es propietario de la Empresa B"). |
| `parent_account_id` | String | No | ID de la cuenta principal, si aplica (como vincular al ID de una empresa matriz). |
| `sic_code` | String | No | Código de clasificación industrial estándar. |
| Campos personalizados | N/A | No | Campos personalizados que tú defines y administras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
{% alert note %}
Aunque algunos campos son opcionales, inclúyelos cuando sea posible porque son nombres de campo reservados y ayudan a mantener tus datos organizados.
{% endalert %}

A continuación, importa tus datos de cuenta a Braze subiendo un archivo CSV o usando la REST API de Braze. Puedes ver estos datos en **Data Settings**. No puedes editar estos datos en el editor del navegador.

#### Usar un archivo CSV

Para importar tus datos mediante CSV:

1. Ve a **Data Settings** > **Accounts**.
2. Selecciona **Update data**.
3. En **CSV upload**, selecciona **Account Data** y luego sube tu archivo a Braze.

![El menú desplegable "Upload data" en la página "Accounts" en Braze.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### Solución de problemas en importaciones CSV {#troubleshooting-csv-imports}

#### Filas vacías en importaciones CSV de objetos de cuenta {#empty-rows-in-account-objects-csv-imports}

Si importas datos de objetos de cuenta y ves filas vacías en la página **Accounts**, verifica si los valores de los campos de cuenta contienen comas.

En las importaciones CSV de objetos de cuenta, las comas en los valores pueden interpretarse como separadores. Esto puede causar que los valores se analicen incorrectamente y generen filas vacías en el panel.

Para solucionar este problema, elimina las comas del archivo CSV original y súbelo de nuevo. Por ejemplo, cambia `"$5,000,000"` a `"$5000000"` o `"$5 million"` antes de volver a subirlo.

## Usar la API de Braze {#using-the-braze-api}

Las API (interfaces de programación de aplicaciones) permiten que diferentes sistemas de software se comuniquen de forma programática. Cuando interactúas con la API de Braze, envías solicitudes HTTP a endpoints específicos. Los endpoints son URL estructuradas que aceptan instrucciones y devuelven respuestas. El método HTTP le indica a Braze qué acción realizar, y el cuerpo de la solicitud contiene los datos.

Para la administración de cuentas, la API de Braze usa estos métodos HTTP:

| Método | Propósito | Comportamiento |
|--------|---------|----------|
| `PUT` | Crear o actualizar recursos | Agrega un nuevo registro de cuenta si no existe. Actualiza el registro existente si ya existe. `PUT` está diseñado para ser idempotente, por lo que puedes sincronizar los mismos datos varias veces sin crear duplicados. |
| `DELETE` | Eliminar recursos | Elimina permanentemente el registro de cuenta especificado y sus asociaciones de Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

La API de Braze te da control programático sobre los datos de cuenta a escala. Puedes automatizar flujos de trabajo de administración de cuentas, sincronizar información de cuentas directamente desde tus orígenes de datos y mantener Braze alineado con tu fuente de verdad sin cargas ni ediciones manuales. Esto ayuda a reducir la carga operativa y mantener datos de cuenta precisos y oportunos para la segmentación y personalización.

Para más información sobre métodos HTTP y cómo funcionan las REST API, consulta los siguientes recursos:
- [Métodos de solicitud HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) en MDN Web Docs
- [Tutorial de REST API](https://restapitutorial.com/)
- [Resumen de la API de Braze]({{site.baseurl}}/api/basics)

{% alert note %}
Usa una clave de API con permisos de catálogos para autenticar solicitudes al endpoint `/business/accounts`.
{% endalert %}

Esta sección cubre cómo usar la API de Braze para:
- [Crear múltiples cuentas](#create-multiple-accounts)
- [Crear una cuenta](#create-one-account)
- [Eliminar múltiples cuentas](#delete-multiple-accounts)
- [Eliminar una cuenta](#delete-one-account)

### Crear múltiples cuentas {#create-multiple-accounts}

Dado que `PUT` es idempotente, puedes enviar la misma solicitud varias veces y Braze actualiza los registros existentes en lugar de crear duplicados. Esto lo convierte en una opción confiable para mantener los registros de cuenta en Braze actualizados.

El siguiente fragmento de código envía una solicitud `PUT` al endpoint `/business/accounts`. El arreglo `accounts` contiene múltiples objetos de empresa, cada uno mapeado a los campos de cuenta definidos en [Paso 2: Importar datos de cuenta](#step-2-import-account-data). Braze procesa cada objeto y crea o actualiza el registro correspondiente en tu página de **Accounts**. Esta operación es asíncrona. Braze pone la solicitud en cola y la procesa en segundo plano, lo que la hace adecuada para importaciones masivas donde no se requiere confirmación inmediata.

Para crear múltiples cuentas, envía una solicitud `PUT` a `/business/accounts`. Si una cuenta no existe, Braze agrega un nuevo elemento en la página de **Accounts**. Cada solicitud puede admitir hasta 50 cuentas. Ten en cuenta que esta operación es asíncrona.

Tu solicitud debería ser similar a la siguiente:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
          "accounts": [
              {
                  "id": "ACC001",
                  "name": "Acme Corporation",
                  "type": "Customer",
                  "annual_revenue": "$5,000,000",
                  "industry": "Manufacturing",
                  "number_of_employees": "150",
                  "address": "123 Industrial Way",
                  "city": "Metropolis",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA",
                  "notes": "Key client in the manufacturing sector",
                  "website": "http://www.acme.com",
                  "main_phone": "+1-212-555-1234",
                  "created_date": "2023-01-15T09:30:00Z",
                  "account_owner_email_address": "owner@example.com",
                  "parent_account_id": "",
                  "sic_code": "2011"
              },
              {
                  "id": "ACC002",
                  "name": "Global Solutions",
                  "type": "Partner",
                  "annual_revenue": "$10,000,000",
                  "industry": "Technology",
                  "number_of_employees": "500",
                  "address": "456 Tech Park",
                  "city": "Silicon Valley",
                  "state": "CA",
                  "postal_code": "94043",
                  "country": "USA",
                  "notes": "Important partner for software solutions",
                  "website": "http://www.globalsolutions.com",
                  "main_phone": "+1-650-555-5678",
                  "created_date": "2023-02-20T14:45:00Z",
                  "account_owner_email_address": "partner@example.com",
                  "parent_account_id": "ACC001",
                  "sic_code": "7372"
              },
              {
                  "id": "ACC003",
                  "name": "Oceanic Ventures",
                  "type": "Customer",
                  "annual_revenue": "$3,200,000",
                  "industry": "Retail",
                  "number_of_employees": "75",
                  "address": "789 Ocean Blvd",
                  "city": "Miami",
                  "state": "FL",
                  "postal_code": "33101",
                  "country": "USA",
                  "notes": "Expanding presence in retail markets",
                  "website": "http://www.oceanicventures.com",
                  "main_phone": "+1-305-555-6789",
                  "created_date": "2023-03-05T08:15:00Z",
                  "account_owner_email_address": "contact@example.com",
                  "parent_account_id": "",
                  "sic_code": "5941"
              }
          ]
      }'
```

### Crear una cuenta {#create-one-account}

Al igual que al crear múltiples cuentas, esta operación usa el método `PUT`. La diferencia es que el ID de la cuenta se incluye directamente en la URL del endpoint en lugar del cuerpo de la solicitud. Esto te da un control preciso sobre un solo registro.

El siguiente fragmento de código envía una solicitud `PUT` a `/business/accounts/ACC001`, donde `ACC001` es el identificador único de la cuenta. Esta operación es síncrona. Braze procesa la solicitud de inmediato y devuelve una respuesta tan pronto como se completa. Esto es adecuado para integraciones en tiempo real. Por ejemplo, cuando la información de la cuenta cambia en tu sistema, puedes reflejar esa actualización en Braze de inmediato para segmentación o personalización.

Para crear una cuenta, envía una solicitud `PUT` a `/business/accounts/:account_id`. Si la cuenta no existe, Braze crea un nuevo registro de cuenta. Esta operación es síncrona.

Tu solicitud debería ser similar a la siguiente:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "accounts": [
            {
                "name": "Braze",
                "type": "Customer",
                "annual_revenue": "$5,000,000",
                "industry": "Manufacturing",
                "number_of_employees": "150",
                "address": "123 Industrial Way",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "notes": "Key client in the manufacturing sector",
                "website": "http://www.acme.com",
                "main_phone": "+1-212-555-1234",
                "created_date": "2023-01-15T09:30:00Z",
                "account_owner_email_address": "owner@example.com",
                "parent_account_id": "",
                "sic_code": "2011"
            }
        ]
      }'
```

### Eliminar múltiples cuentas {#delete-multiple-accounts}

El método `DELETE` elimina registros de cuenta de Braze. A diferencia de `PUT`, las solicitudes `DELETE` no son reversibles. Una vez que se elimina una cuenta, la asociación entre los usuarios y esa cuenta también se elimina.

El siguiente fragmento de código envía una solicitud `DELETE` a `/business/accounts` con una lista de ID de cuenta en el cuerpo de la solicitud. Braze procesa cada ID y elimina el registro de cuenta correspondiente. Esta operación es asíncrona. Braze pone las eliminaciones en cola y las procesa en segundo plano. Usa esto para tareas de limpieza masiva, como cuando un grupo de cuentas ha cancelado, se ha consolidado o ya no es relevante para la segmentación en Braze.

Para eliminar múltiples cuentas, envía una solicitud `DELETE` a `/business/accounts` con un cuerpo que contenga una lista de ID de cuenta. Ten en cuenta que esta operación es asíncrona.

Tu solicitud debería ser similar a la siguiente:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "accounts": [
      { "id": "ACC001" },
      { "id": "ACC002" },
      { "id": "ACC003" }
    ]
  }'
```

### Eliminar una cuenta {#delete-one-account}

Al igual que al crear una cuenta, esta operación apunta a una cuenta específica incluyendo su ID directamente en la URL del endpoint. Esto te da un control preciso sobre un solo registro sin afectar a otros.

El siguiente fragmento de código envía una solicitud `DELETE` a `/business/accounts/ACC001`. Esta operación es síncrona. Braze procesa la solicitud de inmediato y devuelve una respuesta tan pronto como se completa. Usa esto cuando una cuenta individual se cierra, se fusiona o necesita ser eliminada de Braze por motivos de cumplimiento o higiene de datos.

Para eliminar una sola cuenta, envía una solicitud `DELETE` a `/business/accounts/:account_id`. Ten en cuenta que esta operación es síncrona.

Tu solicitud debería ser similar a la siguiente:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY"
```

## Uso de objetos en mensajes {#using-objects-in-messages}

Después de [importar tus datos a Braze](#importing-data-to-braze), puedes usar objetos de cuenta para crear un Segment y enviar mensajes personalizados a los usuarios mediante Liquid.

### Paso 1: Crear un Segment {#step-1-build-a-segment}

A continuación, crea un Segment que combine datos de usuario y datos de cuenta. En este ejemplo, te diriges a directores de empresas de salud para aumentar la inscripción a un nuevo webinar en tu empresa de promoción de la salud.

1. Ve a **Audiencia** > **Segments** y selecciona **Crear Segment**.
2. Asigna un nombre a tu Segment.
3. En el **Generador de Segments**, selecciona el filtro **Business** y configura los siguientes filtros de segmentación. Cuando hayas terminado, selecciona **Guardar**.

| Filtro                          | Descripción                                      |
|---------------------------------|--------------------------------------------------|
| `Role is exactly director`      | Se dirige a usuarios cuyo rol es específicamente Director |
| `Accounts industry matches regex healthcare` | Coincide con usuarios en cuentas con industrias relacionadas con la salud |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Actualmente, para usar múltiples filtros de cuenta, selecciona **Agregar criterios** en lugar de usar el desplegable **OR/AND**.
{% endalert %}

![Filtros de segmentación configurados para crear un segmento de usuarios que son directores en empresas de salud.]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/build_segment.png %})

{% alert note %}
La segmentación funciona solo en los primeros 1000 registros de cuenta que coincidan con los criterios. Puedes tener hasta un filtro de negocio por Segment, y todos los criterios deben estar en un solo filtro.
{% endalert %}

### Paso 2: Usar Liquid para personalizar {#step-2-use-liquid-to-personalize}

Ahora puedes personalizar tu mensaje para enviar a los usuarios información sobre oportunidades. En este ejemplo, redacta un mensaje para tus directores y vincúlalos al webinar. También puedes usar un catálogo de Braze para obtener imágenes específicas de la industria para la personalización.

#### Paso 2.1: Personalizar con información de cuenta {#step-21-personalize-with-account-information}

Selecciona **Business** como tipo de personalización y luego selecciona **Name** para personalizar el mensaje con el nombre de la empresa del usuario.

Lo siguiente se copia a tu portapapeles.

{% raw %}
```javascript
{% business %}
{{ business_accounts[0].name }}
```
{% endraw %}

Braze genera la etiqueta {% raw %}`{% business %}`{% endraw %}, que establece un arreglo llamado `business_accounts` que contiene información de cuenta para la cuenta asociada.

Ajusta la salida autogenerada para crear tu mensaje.

En el siguiente ejemplo, mueve la llamada a la etiqueta {% raw %}`{% business %}`{% endraw %} a la parte superior del mensaje y personaliza con el nombre del usuario. Usa el nombre de la cuenta para personalizar el mensaje. La salida de Liquid permanece igual, pero la colocas en diferentes partes del mensaje.

{% raw %}
```javascript
{% business %}

Hi {{${first_name}}},

We would love to invite you and your peers at {{ business_accounts[0].name }} to join our latest webinar named "Creating Optimal Health Outcomes for Patients".  Click the link below to register.
```
{% endraw %}

La salida es similar a lo siguiente:

{% raw %}
```javascript
Hi John,

We would love to invite you and your peers at Sunshine Health to join our latest webinar named "Creating Optimal Health Outcomes for Patients". Click the link below to register.
```
{% endraw %}

#### Paso 2.2: Conectar con catálogos {#step-22-connect-with-catalogs}

A continuación, personaliza aún más tu mensaje usando catálogos de Braze para agregar y almacenar una imagen que corresponda a la empresa de salud.

Para este ejemplo, supón que tienes lo siguiente:

- Un catálogo configurado llamado `industry_assets`
- El ID de cada entrada del catálogo es el nombre de una industria que corresponde a las industrias en tus cuentas
- Los enlaces de URL de imagen para una imagen principal y una secundaria.

El siguiente es un ejemplo del Liquid utilizado para esta personalización.
{% raw %}
```javascript
//Make a call to the business tag.  This sets the accounts array and prepares us to pull account data out.
{% business %}

//Assign the user's accounts industry to a variable called industry.  This step isn't required but it makes everything easier to read.
{% assign industry = {{business_accounts[0].industry}} %}

//Make a catalog_items call to the industry_assets catalog and ask for the industry item (in this case, it will ask for "healthcare")
{% catalog_items industry_assets industry %}

// Get the hero image for the "healthcare" industry
{{items[0].hero_image}}
```
{% endraw %}

## Preguntas frecuentes (FAQ) {#faq}

### ¿Puedo agregar campos personalizados? {#can-i-add-custom-fields}

Sí. Puedes agregar campos personalizados a las cuentas. Si tienes tu propio método de puntuación de leads, también puedes usar un campo personalizado en tu objeto de cuenta para rastrear esto.

### ¿Puede un usuario estar asociado con más de una cuenta? {#can-a-user-be-associated-with-more-than-one-account}

No. Actualmente, cada usuario solo puede tener una asociación de cuenta.

### ¿Puede un perfil de usuario contener múltiples correos electrónicos? {#can-one-user-profile-contain-multiple-emails}

No. Un perfil de usuario no puede tener más de un correo electrónico, como un correo personal y uno de trabajo.