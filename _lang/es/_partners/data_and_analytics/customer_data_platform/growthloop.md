---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "Este artículo de referencia describe la asociación entre Braze y GrowthLoop, una plataforma que te permite segmentar los datos de los clientes directamente desde almacenes de datos y enviarlos a Braze."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) ayuda a los equipos de marketing a activar los datos de clientes desde el almacén de datos en la nube a Braze y otros canales. Automatiza, escala y mide los programas de marketing desde tu almacén de datos en la nube, manteniendo los datos en una ubicación única y centralizada.

_GrowthLoop se encarga del mantenimiento de esta integración._

## Sobre la integración {#about-the-integration}

La integración de Braze y GrowthLoop te permite segmentar los datos de clientes directamente desde el almacén de datos y enviarlos a Braze, garantizando que los usuarios puedan optimizar el amplio conjunto de características de Braze junto con su única fuente de verdad. Agiliza los esfuerzos de marketing para la segmentación y activación de clientes, reduciendo el tiempo que se tarda en segmentar, lanzar, probar y medir los resultados de las campañas dirigidas enviadas a Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta GrowthLoop Growth o Enterprise | Se necesita una cuenta GrowthLoop para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con todos los permisos.<br><br>Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze | La URL de tu endpoint REST or transferencia de estado representacional. Tu endpoint dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Envía listas de clientes desde tu almacén de datos a Braze para segmentar campañas de correo electrónico y notificaciones push en un clic, y mantenlas siempre sincronizadas.

- Correos electrónicos basados en la activación del registro: envía correos electrónicos para ayudar a los usuarios que abandonan tu flujo de registro y conviértelos en usuarios activos.
- Correos electrónicos basados en cualquier comportamiento del usuario: envía correos electrónicos basados en el comportamiento del usuario, como "Añadir al carrito".
- Correos electrónicos a clientes perdidos: reactiva a los clientes perdidos por correo electrónico con una oferta.

## Integración {#integration}

### Configurar la conexión de Braze en GrowthLoop {#configure-braze-connection-in-growthloop}

Cuando accedas a la plataforma de segmentación dentro de GrowthLoop, ve a la pestaña **Destinations** en la barra lateral de navegación y haz clic en **New Destination** en la barra de acciones.

Desplázate hasta que encuentres Braze y haz clic en **Add Braze**.

Aparecerá una ventana emergente para configurar la conexión con el destino.

- **Destination name**: así es como se denominará el destino y se hará referencia a él en la aplicación en adelante
- **Sync frequency**: selecciona Daily o Hourly; esto controlará la frecuencia con la que GrowthLoop exporta audiencias a Braze
- **API key**: clave de API creada en los requisitos, con los permisos necesarios
- **API URL**: URL como se define en los requisitos

Haz clic en **Create**, ¡y ya puedes exportar tu primera audiencia a Braze! Para crear una audiencia en GrowthLoop, visita [Crear una audiencia](https://www.growthloop.com/help-center-articles/create-an-audience).

### Posterior a la exportación {#post-export}

Una vez exportada tu audiencia, cada 15 minutos GrowthLoop generará una versión actualizada de tus listas de clientes y la enviará a Braze.

Al mismo tiempo, GrowthLoop eliminará de tu audiencia a los usuarios que ya no cumplan los requisitos y añadirá nuevos usuarios cualificados a tu audiencia.

Braze emparejará a los usuarios y creará una marca, indicando que forman parte de una audiencia de GrowthLoop.

Cuando crees una campaña en Braze, puedes seleccionar clientes en esa audiencia de GrowthLoop.

## Solución de problemas {#troubleshooting}

Ponte en contacto con el equipo de GrowthLoop en solutions@growthloop.com para obtener más información o ayuda.