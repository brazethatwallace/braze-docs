---
nav_title: Mandarina
article_title: Tangerine
description: "Este artículo describe la asociación entre Braze y Tangerine Store360, una plataforma omnicanal que conecta las tiendas físicas con las tiendas en línea para ofrecer experiencias superiores en tienda a los consumidores y a los empleados de las tiendas. A través de esta integración, los datos brutos de campañas e impresiones de Braze están disponibles en Store360 a través de Snowflake Secure Data Sharing, y las marcas pueden medir cómo sus campañas afectan a la interacción en tienda y al tráfico en tienda."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine diseña, construye y opera una plataforma omnicanal llamada Store360. Store360 es una plataforma habilitadora omnicanal que conecta las tiendas físicas con las tiendas en línea para mejorar la experiencia del consumidor y del empleado en la tienda. Store360 rastrea y analiza el tráfico de visitas a las tiendas físicas, incluidos los usuarios de la aplicación móvil de los minoristas y su interacción en la tienda.

La integración de Braze y Tangerine te permite integrar datos brutos de campañas e impresiones de Braze en Store360 a través de Snowflake Secure Data Sharing. Ahora las marcas pueden medir el impacto de estas campañas en las visitas a las tiendas físicas y en la interacción en las mismas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Store360 | Se necesita una cuenta Store360 para beneficiarse de esta asociación. |
| ID de cuenta Braze | Tu ID de grupo de aplicaciones de Braze. |
| Coincidencia de ID de usuario | Los datos de tus clientes en Store360 y Braze deben tener ID de usuario coincidentes en las dos plataformas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

### Analizar el impacto de la campaña en la visita a la tienda física {#analyze-campaign-impact-on-physical-store-visit}

Las marcas utilizan Braze para enviar mensajes de campaña a los consumidores con el fin de aumentar las visitas a las tiendas. Durante la campaña, Store360 captura las visitas de usuarios de aplicaciones móviles identificados por ID de usuario.

Gracias a la capacidad analítica de Store360 Insight, las marcas pueden visualizar los detalles del impacto de la campaña, desde los mensajes enviados y leídos (datos de Braze) hasta quiénes y cuántos destinatarios visitaron las tiendas físicas (datos de Store360).

## Integración {#integration}

### Paso 1: Habilitar el uso compartido seguro de datos de Snowflake {#step-1-enable-snowflake-secure-data-share}

Trabaja con tu equipo de Braze para habilitar y configurar Snowflake Secure Data Share.

### Paso 2: Configurar Store360 para obtener datos de Braze {#step-2-configure-store360-to-get-braze-data}

Configura el ID de grupo de aplicaciones de Braze en tu cuenta de servicio Store360 mediante la consola web del administrador de Store360. Esto solicitará al equipo de administración de Tangerine que sincronice los datos de Braze con Store360 mediante el uso compartido de datos de Snowflake.

### Paso 3: Integrar los SDK de Store360 en la aplicación móvil {#step-3-integrate-store360-sdks-to-mobile-app}

Para realizar un seguimiento y analizar las visitas a la tienda de los usuarios de la aplicación móvil y las actividades en la tienda junto con los datos de campañas e impresiones de Braze, debes integrar el SDK de Store360 en tu aplicación móvil siguiendo los pasos que se indican en la documentación de instalación del SDK de Store360. Esta documentación te será facilitada tras la firma de un contrato de cliente con Tangerine Store 360.

## Analizar datos de Braze en Store360 {#analyze-braze-data-in-store360}

Aprovecha el uso compartido seguro de datos de Snowflake para compartir tus datos brutos de campañas e impresiones de Braze con los análisis de Store360 Insight, que proporcionan una imagen completa del ciclo de vida y las actividades de los usuarios, desde el entorno en línea hasta el fuera de línea.

Como referencia, aquí están todos los [campos de Braze](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) disponibles para ser incorporados en los análisis de Store360. Los detalles de este paso son muy específicos del cliente y requieren configuraciones especiales. Habla con tu director de cuentas de Store360 o con support@tangerine.io para obtener más información.

## Información importante y limitaciones {#important-information-and-limitations}

### Disponibilidad del servicio {#service-availability}

Actualmente, el servicio Store360 está disponible comercialmente en Japón e Indonesia.

Tangerine tiene previsto lanzar el producto Store360 en los siguientes países en 2023.
- Estados Unidos de América
- Tailandia
- Singapur
- Vietnam
- Corea

### Retención de datos {#data-retention}

Existe una política de retención de dos años para tus datos de Braze en el uso compartido de datos de Snowflake.

### Retraso en la carga de datos de eventos de Braze {#time-lag-in-populating-braze-event-data}

Los eventos de Braze se procesan con tecnología de streaming y están disponibles casi en tiempo real. Generalmente, los eventos están disponibles en los 30 minutos posteriores a haberse producido.