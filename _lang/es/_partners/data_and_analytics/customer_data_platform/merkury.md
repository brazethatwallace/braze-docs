---
nav_title: Merkury
article_title: Merkury
description: "Este artículo de referencia describe la asociación entre Braze y Merkury, una plataforma de identidad empresarial para tus aplicaciones, que te permite aprovechar el `MerkuryID` para aumentar las tasas de reconocimiento de los visitantes del sitio de los clientes de Braze."
page_type: partner
search_tag: Partner
---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) es la plataforma de identidad empresarial de Merkle que ayuda a las marcas a maximizar la participación, la experiencia y los ingresos de los consumidores a través de funciones de identidad de primera parte sin cookies. `MerkuryID` unifica los registros de clientes y clientes potenciales conocidos y desconocidos de una marca, las visitas a sitios o aplicaciones y los datos de los consumidores en un único y persistente identificador de persona.

_Esta integración está mantenida por Merkury._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Merkury te permite aprovechar el `MerkuryID` para aumentar las tasas de reconocimiento de visitantes del sitio para los clientes de Braze. Al reconocer a los visitantes que son suscriptores de correo electrónico de la marca, Merkury actualiza el perfil de Braze para incluir la dirección de correo electrónico del suscriptor. Las capacidades de reconocimiento mejoradas de `MerkuryID` mejoran las oportunidades de participación y personalización, y aumentan de inmediato las cantidades de envío de correos electrónicos de abandono del sitio y los ingresos asociados.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Merkle | Se requiere una cuenta de Merkle para aprovechar esta integración. |
| ID de cliente de Merkle | Obtén tu ID de cliente de tu representante de Merkle. |
| Etiqueta Merkury | Coloca la etiqueta Merkury de Merkle en tu sitio web. |
| Endpoint REST or transferencia de estado representacional y SDK or kit de desarrollo de software de Braze | La URL de tu endpoint REST or transferencia de estado representacional o SDK or kit de desarrollo de software. Tu endpoint dependerá de la [URL de Braze para tu instancia]({{site.baseurl}}/api/basics#endpoints). |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Se puede crear en **Panel de Braze > Consola para desarrolladores > Clave de API REST or transferencia de estado representacional > Crear nueva clave de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% alert important %}
Las solicitudes del conector de identidad Merkury a Braze operan dentro de las especificaciones de límite de velocidad de la API de Braze. Ponte en contacto con Braze o con tu director de cuentas de Merkle si tienes alguna pregunta.<br><br>Merkury envía al menos una solicitud al final de una sesión cualificada.
{% endalert %}

## Integración de SDK or kit de desarrollo de software en paralelo {#side-by-side-sdk-integration}

Utiliza la etiqueta Merkury del lado del cliente de Merkle para capturar dispositivos de Braze y los reenvía al endpoint del conector de identidad de Merkury para su identificación.

### Paso 1: Configurar la etiqueta del SDK or kit de desarrollo de software Web de Braze {#step-1-setup-braze-web-sdk-tag}

Debes tener el [SDK or kit de desarrollo de software Web de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-gtm) implementado en tu sitio web para usar esta integración.

### Paso 2: Implementar la etiqueta Merkury de Merkle {#step-2-deploy-merkles-merkury-tag}

Implementa la etiqueta Merkury en tu sitio web para que el conector de identidad de Merkury esté disponible en tu sitio web. Tu director de cuentas de Merkle te proporcionará una guía detallada con instrucciones.

### Paso 3: Crear atributos personalizados {#step-3-create-custom-attributes}

El conector de identidad de Merkury completa los siguientes campos, que debes crear en Braze como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Nombre del atributo | Tipo de datos | Descripción |
| --- | --- | --- |
| `hmid` | Cadena | ID de Merkury de Merkle |
| `confidence_score` | Número | Nivel de confianza con el que Merkury pudo identificar (1-8, menor es mejor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 3: Crear atributos personalizados" }

### Paso 4: Proporcionar a Merkle el universo de correo electrónico de usuarios {#step-4-provide-merkle-with-user-email-universe}

Merkle recomienda una exportación de segmentación de tu universo de correo electrónico con permisos. Esto se puede complementar con exportaciones diarias de usuarios activos con permisos.

Los siguientes campos son obligatorios:

- `braze_id`
- `external_id`
- dirección de correo electrónico

Consulta a tu representante de Braze para obtener más información.