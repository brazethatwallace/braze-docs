---
nav_title: Merkury
article_title: Merkury
description: "Este artículo de referencia describe la asociación entre Braze y Merkury, una plataforma de identidad empresarial para tus aplicaciones, que te permite aprovechar el `MerkuryID` para aumentar las tasas de reconocimiento de los visitantes del sitio de los clientes de Braze."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) es la plataforma de identidad empresarial de Merkle que ayuda a las marcas a maximizar la interacción, la experiencia y los ingresos de los consumidores a través de funciones de identidad de primera mano sin cookies. `MerkuryID` unifica los registros de clientes y clientes potenciales conocidos y desconocidos de una marca, las visitas a sitios o aplicaciones y los datos de los consumidores en un único y persistente identificador de persona.

_Esta integración está mantenida por Merkury._

## Sobre la integración {#about-the-integration}

La integración de Braze y Merkury te permite aprovechar `MerkuryID` para aumentar las tasas de reconocimiento de los visitantes del sitio para los clientes de Braze. Al reconocer a los visitantes que son suscriptores de correo electrónico de la marca, Merkury actualiza el perfil de Braze para incluir la dirección de correo electrónico del suscriptor. La mayor capacidad de reconocimiento de `MerkuryID` mejora la interacción y las oportunidades de personalización, y aumenta inmediatamente las cantidades de envíos de correo electrónico por abandono del sitio y los ingresos asociados.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Merkle | Se necesita una cuenta de Merkle para beneficiarse de esta asociación. |
| ID de cliente de Merkle | Obtén tu ID de cliente de tu representante de Merkle. |
| Etiqueta Merkury | Coloca la etiqueta Merkury de Merkle en tu sitio web. |
| Punto de conexión REST y SDK de Braze | La URL de tu punto de conexión REST o SDK. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Se puede crear en **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert important %}
Las solicitudes del conector de identidad Merkury a Braze operan dentro de las especificaciones de límite de velocidad de la API de Braze. Ponte en contacto con Braze o con tu director de cuentas de Merkle si tienes alguna pregunta.<br><br>Merkury envía al menos una solicitud al final de una sesión cualificada.
{% endalert %}

## Integración en paralelo del SDK {#side-by-side-sdk-integration}

Utiliza la etiqueta Merkury del lado del cliente de Merkle para capturar dispositivos de Braze y reenviarlos al punto de conexión del conector de identidad Merkury para su identificación.

### Paso 1: Configurar la etiqueta del SDK web de Braze {#step-1-setup-braze-web-sdk-tag}

Debes tener el [SDK web de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) desplegado en tu sitio web para utilizar esta integración.

### Paso 2: Desplegar la etiqueta Merkury de Merkle {#step-2-deploy-merkles-merkury-tag}

Despliega la etiqueta Merkury en tu sitio web para que el conector de identidad Merkury esté disponible en tu sitio web. Tu director de cuentas de Merkle te proporcionará una guía detallada con instrucciones.

### Paso 3: Crear atributos personalizados {#step-3-create-custom-attributes}

El conector de identidad Merkury rellena los siguientes campos, que debes crear en Braze como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes).

| Nombre del atributo | Tipo de datos | Descripción |
| --- | --- | --- |
| `hmid` | Cadena | ID de Merkury de Merkle |
| `confidence_score` | Número | Nivel de confianza con el que Merkury pudo identificar (1-8, cuanto más bajo mejor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 3: Create custom attributes" }

### Paso 4: Proporcionar a Merkle el universo de correos electrónicos de los usuarios {#step-4-provide-merkle-with-user-email-universe}

Merkle recomienda una exportación de segmentación de tu universo de correo electrónico permitido. Esto puede complementarse con exportaciones diarias de usuarios activos permitidos.

Los siguientes campos son obligatorios:

- `braze_id`
- `external_id`
- dirección de correo electrónico

Consulta a tu representante de Braze para más información.