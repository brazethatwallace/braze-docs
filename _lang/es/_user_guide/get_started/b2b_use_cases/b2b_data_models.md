---
nav_title: Modelos de datos
article_title: Crear un modelo de datos B2B
page_order: 0
page_type: reference
description: "Aprende a utilizar las herramientas de datos de Braze para crear modelos B2B."
---

# Crear un modelo de datos B2B {#create-a-b2b-data-model}

> Este caso de uso demuestra cómo puedes utilizar las herramientas de datos de Braze para crear un modelo de datos B2B eficaz y eficiente que te ayude a segmentar, desencadenar, personalizar y enviar mensajes a los usuarios de tu empresa.

{% alert note %}
Estas recomendaciones pueden cambiar con el tiempo a medida que Braze desarrolle sus capacidades B2B.
{% endalert %}

Antes de entrar en cómo puedes configurar tu modelo de datos B2B, repasemos varios conceptos y términos que debes conocer.

Hay cuatro objetos B2B principales que necesitas para ejecutar campañas B2B.

| Objeto | Descripción |
| --- | --- |
| Clientes potenciales | Un registro de clientes potenciales que han mostrado interés por un producto o servicio, pero que aún no han sido calificados como una oportunidad. |
| Contactos | Normalmente, personas que han sido cualificadas y convertidas de cliente potencial a contacto para buscar una oportunidad de venta. |
| Oportunidades | Un registro que hace seguimiento de los detalles de una venta potencial o un acuerdo en curso. |
| Cuentas | Un registro de una organización que es un cliente potencial cualificado, un cliente existente, un socio o un competidor que mantiene una relación de importancia similar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Crear un modelo de datos B2B" }

En Braze, estos cuatro objetos se combinan y reducen a dos objetos: perfiles de usuario y objetos empresariales.

| Objeto Braze B2B | Descripción | Objetos B2B originales  |
| --- | --- | --- |
| Perfiles de usuario | Se mapean directamente con clientes potenciales y contactos en tu sistema CRM de ventas. Como Braze capta los clientes potenciales, se crean automáticamente como clientes potenciales en tu sistema CRM de ventas. A medida que se convierten en contactos, los ID y detalles de los contactos se sincronizan de nuevo con Braze. | Clientes potenciales<br> Contactos |
| Objetos empresariales | Se mapean con cualquier objeto que no sea de usuario en tu sistema CRM de ventas. Esto incluye tus objetos específicos de ventas, como objetos de cuenta y objetos de oportunidad. | Cuentas<br> Oportunidades |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Crear un modelo de datos B2B" }

## Paso 1: Crea tus objetos empresariales en Braze {#step-1-create-your-business-objects-in-braze}

Los objetos empresariales son cualquier conjunto de datos no centrado en el usuario. En un contexto B2B, estos incluyen tus datos de cuentas y oportunidades, y cualquier otro conjunto de datos pertinente no centrado en el usuario que tu empresa rastree.

Existen dos métodos para crear y gestionar tus objetos empresariales en Braze: catálogos y fuentes conectadas.

| Método | Descripción |
| --- | --- |
| [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) | Son objetos de datos independientes (objetos de datos complementarios) del perfil de usuario principal en Braze. En un contexto B2B, probablemente tendrías catálogos para tus cuentas y oportunidades. |
| [Fuentes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) | Permiten a Braze consultar directamente tu almacén de datos. Es probable que ya estés sincronizando regularmente tus objetos de clientes potenciales, contactos, oportunidades y cuentas con tu almacén de datos, así que puedes dirigir la segmentación de Braze directamente a ese almacén y activarla en un entorno de copia cero. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Crea tus objetos empresariales en Braze" }

{% tabs %}
{% tab Catálogos %}

### Opción 1: Usa catálogos para cuentas y oportunidades {#option-1-use-catalogs-for-accounts-and-opportunities}

Los catálogos son tablas de datos que se alojan y gestionan en Braze. Aunque los datos de cuentas y oportunidades proceden del sistema CRM de ventas que hayas elegido, los duplicarías en Braze para utilizarlos con fines de marketing: segmentación basada en cuentas, marketing basado en cuentas, gestión de clientes potenciales, y más.

Para esta opción, recomendamos crear un catálogo para tus cuentas y otro para tus oportunidades, y actualizarlos con frecuencia enviando actualizaciones a Braze a través de nuestra [API de catálogos]({{site.baseurl}}/api/endpoints/catalogs/) o de la [Ingesta de datos de Cloud (CDI) de catálogos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/). Al crear estos catálogos, asegúrate de que el `id` (primera columna) de tu catálogo coincida con el `id` de tu sistema CRM de ventas.

#### Mapea los campos de tu CRM {#map-over-your-crm-fields}

Las tablas siguientes incluyen algunos ejemplos de campos que puedes mapear desde los objetos de cuenta y oportunidad de tu CRM.

{% subtabs %}
{% subtab Catálogo de cuentas %}

En este caso de uso, Salesforce es el sistema CRM de ejemplo. Puedes mapear cualquier campo incluido en los objetos de tu CRM.

<table aria-label="Mapea los campos de tu CRM" border="1">
  <caption>Mapea los campos de tu CRM</caption>
  <thead>
  <tr>
    <th><b>Objeto Braze</b></th>
    <th><b>Campo de Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo CRM (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Catálogo &gt; Catálogo de cuentas</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tbody>
</table>

##### Ejemplo de tabla de campos de cuenta mapeados {#example-table-of-mapped-account-fields}

![Tabla de cuentas de Salesforce con la información correspondiente, como la dirección de facturación y el titular de la cuenta.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Catálogo de oportunidades %}

En este caso de uso, Salesforce es el sistema CRM de ejemplo. Puedes mapear cualquier campo incluido en los objetos de tu CRM.

<table aria-label="Ejemplo de tabla de campos de cuenta mapeados" border="1">
  <caption>Ejemplo de tabla de campos de cuenta mapeados</caption>
  <thead>
  <tr>
    <th><b>Objeto Braze</b></th>
    <th><b>Campo de Braze</b></th>
    <th><b>Objeto CRM (Salesforce)</b></th>
    <th><b>Campo CRM (Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">Catálogo &gt; Catálogo de oportunidades</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
  </tbody>
</table>

##### Ejemplo de tabla de campos de oportunidad mapeados {#example-table-of-mapped-opportunity-fields}

![Tabla de oportunidades de Salesforce con la información correspondiente, como la dirección de facturación y el titular de la cuenta.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Fuentes conectadas %}

### Opción 2: Usa fuentes conectadas para cuentas y oportunidades {#option-2-use-connected-sources-for-accounts-and-opportunities}

Las fuentes conectadas son tablas de datos alojadas por ti en tu propio almacén de datos y consultadas por las [Extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/) de Braze. A diferencia de los catálogos, en lugar de duplicar tus objetos empresariales (cuentas y oportunidades) en Braze, los mantendrías en tu almacén de datos y usarías tu almacén como fuente de verdad.

Para configurar las fuentes conectadas, consulta [Integrar fuentes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Paso 2: Relaciona tus objetos empresariales con los perfiles de usuario {#step-2-relate-your-business-objects-to-user-profiles}

Los perfiles de usuario son el objeto principal en Braze, que impulsa la mayor parte de tu segmentación demográfica, desencadenamiento y personalización. Los perfiles de usuario incluyen [datos de usuario predeterminados]({{site.baseurl}}/user_guide/data/unification/user_data/) recopilados por nuestro SDK y otras fuentes, incluidos [datos personalizados]({{site.baseurl}}/user_guide/data/activation/), que adoptan la forma de atributos (datos demográficos), eventos (datos de comportamiento) o compras (datos de transacciones).

### Paso 2.1: Mapea los ID del CRM de ventas a Braze {#step-21-map-sales-crm-ids-to-braze}

En primer lugar, asegúrate de que Braze y el CRM que elijas tengan un identificador común para compartir datos. Te sugerimos que utilices la siguiente tabla para mapear los campos de ID de tu CRM de ventas al objeto de usuario de Braze. La tabla siguiente usa Salesforce como sistema CRM, pero esto se puede hacer con cualquier CRM.

#### Objeto Braze: usuario {#braze-object-user}

| Campo de Braze | Objeto CRM (Salesforce) | Campo CRM (Salesforce) | Información adicional |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` | - Etiqueta de alias de usuario: `salesforce_lead_id` <br>- Nombre del alias de usuario: `lead_id` |
| `Aliases.salesforce_contact_id` | Contact | `id` | - Etiqueta de alias de usuario: `salesforce_contact_id` <br>- Nombre del alias de usuario: `contact_id` |
| `AccountId` | Contact | `AccountId` |
| `OpportunityId` (opcional, escalar) <br>o<br> `Opportunities` (opcional, matriz) | Opportunity | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objeto Braze: usuario" }

{% alert note %}
Recomendamos usar [alias]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases) en lugar de `external_id` para mapear los identificadores de leads y contactos de Salesforce a Braze. Esto se debe a que reduce la cantidad de búsquedas necesarias a la hora de identificar y ejecutar tus iniciativas de crecimiento basadas en producto.
{% endalert %}

Una vez que tengas tus ID sincronizados, necesitas relacionar tus perfiles de usuario de Braze con tus objetos empresariales.

### Paso 2.2: Crea una relación entre los perfiles de usuario y tus objetos empresariales {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab Catálogos %}

#### Opción 1: Al usar catálogos {#option-1-when-using-catalogs}

Ahora que los detalles de tus oportunidades y cuentas están registrados como catálogos de Braze, necesitas crear una relación entre esos catálogos y los perfiles de usuario a los que quieres enviar mensajes. Actualmente, esto requiere dos pasos:

1. Incluye la cuenta (como `account_id (string)`), el ID de oportunidad (como `opportunity_ids (array)`), o ambos en el perfil de usuario como atributos.
2. Registra un evento (como `account_linked`) que incluya el ID de la cuenta como propiedad del evento.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Fuentes conectadas %}

#### Opción 2: Al usar fuentes conectadas {#option-2-when-using-connected-sources}

Una de las tablas de tu fuente conectada debe incluir un `user_id` que coincida con el `external_user_id` configurado en Braze para tus usuarios. La configuración del perfil de usuario anterior utiliza tus lead y `contact_ids` como tu `external_id`, por lo que debes asegurarte de que tus tablas de lead/contacto incluyan estos ID.

Además de asegurarte de que los ID coincidan, recomendamos escribir datos básicos a nivel de cuenta, como `account_id`, `opportunity_id`, e incluso atributos firmográficos comunes como `industry`, en los perfiles de usuario para una segmentación y personalización eficientes.

{% endtab %}
{% endtabs %}