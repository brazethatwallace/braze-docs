---
nav_title: Resumen arquitectónico
article_title: Resumen arquitectónico
page_order: 3
description: "Este artículo trata de las diferentes partes y piezas del stack tecnológico de Braze, con enlaces a artículos relevantes."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# Para empezar: Resumen arquitectónico {#getting-started-architectural-overview}

> Este artículo trata de las diferentes partes y piezas del stack tecnológico de Braze, con enlaces a artículos relevantes.

A un alto nivel, Braze se ocupa de datos. La plataforma Braze, impulsada por el SDK or kit de desarrollo de software, la REST or transferencia de estado representacional API y las integraciones de partners, te permite agregar tus datos y actuar sobre ellos.

![Braze tiene diferentes capas. En total, consta del SDK, la API, el panel y las integraciones de partners. Cada una de ellas aporta partes de una capa de ingesta de datos, una capa de clasificación, una capa de orquestación, una capa de personalización y una capa de acción. La capa de acción tiene varios canales, como push, mensajes dentro de la aplicación, catálogo conectado, webhook, SMS y correo electrónico.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Ingesta de datos](#ingestion): Braze extrae datos de diversas fuentes.
* [Clasificación](#classification): Tu equipo de marketing segmenta dinámicamente tu base de usuarios utilizando estas métricas.
* [Orquestación](#orchestration): Braze coordina de forma inteligente los mensajes a diferentes segmentos de audiencia en el momento ideal.
* [Acción](#action): Tu equipo de marketing actúa a partir de los datos, creando contenidos a través de diversos canales de mensajería, como los servicio de mensajes cortos y el correo electrónico.
* [Personalización](#personalization): Los datos se transforman en tiempo real con información personalizada sobre tu audiencia.
* [Exportación](#exporting-data): Después, Braze hace un seguimiento de la interacción de tus usuarios con esta mensajería y la vuelve a introducir en la plataforma, creando un bucle. Obtendrás información sobre estos datos mediante informes y análisis en tiempo real.

Todo esto funciona conjuntamente para crear interacciones satisfactorias entre tu base de usuarios y tu marca, de modo que puedas alcanzar tus objetivos. Braze hace todo esto en el contexto de lo que llamamos nuestra pila integrada verticalmente. Profundicemos en cada capa, de una en una.

## Ingesta de datos {#ingestion}

Braze se basa en una arquitectura de datos de transmisión que aprovecha Snowflake, Kafka, MongoDB y Redis. Los datos de muchos orígenes se pueden cargar en Braze a través del SDK or kit de desarrollo de software y la API. La plataforma puede manejar cualquier dato en tiempo real, independientemente de cómo esté anidado o estructurado. Los datos en Braze se almacenan en el perfil de usuario.

{% alert tip %}
Braze puede hacer un seguimiento de los datos de un usuario a lo largo de su trayecto contigo, desde que es anónimo hasta que inicia sesión en tu aplicación y es conocido. Los ID de usuario, llamados `external_id`s en Braze, deben establecerse para cada uno de tus usuarios. Deben ser inmutables y accesibles cuando un usuario abra la aplicación, permitiéndote hacer un seguimiento de tus usuarios en todos los dispositivos y plataformas. Consulta el [artículo Ciclo de vida del usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) para conocer las mejores prácticas.
{% endalert %}

![Braze importa orígenes de datos backend desde la API, orígenes de datos frontend desde el SDK, datos de almacén de datos desde la ingesta de datos en la nube de Braze y desde las integraciones de partners. Estos datos se exportan a través de la API de Braze.]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
Esta base de datos de perfiles de usuario centrada en la persona permite una velocidad interactiva en tiempo real. Braze precalcula los valores cuando llegan los datos y almacena los resultados en nuestro formato de documento ligero para una rápida recuperación. Y como la plataforma se diseñó así desde el principio, es ideal para la mayoría de los casos de uso de la mensajería, especialmente combinada con otros conceptos de datos como el contenido conectado, los catálogos de productos y los atributos anidados.
{% endalert %}

### Desglose de los orígenes de datos {#data-source-breakdown}

Braze utiliza diferentes sistemas de almacenamiento de datos para diversas características. Comprender qué características utilizan qué orígenes de datos es importante para la gestión de datos y la solución de problemas.

#### Características basadas en MongoDB {#mongodb-powered-features}
- Eventos personalizados (rastreados por SDK or kit de desarrollo de software y API)
- Atributos personalizados
- Perfiles de usuario
- Eventos de compra
- La mayoría de las características de segmentación y orientación

#### Características basadas en Snowflake {#snowflake-powered-features}
- [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Línea de productos de predicción]({{site.baseurl}}/user_guide/brazeai)
- [Recomendaciones de artículos personalizadas mediante IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai)
- [Tasa de apertura real estimada]({{site.baseurl}}/user_guide/channels/email/reporting#estimated-real-open-rate) (no utiliza eventos personalizados)

{% alert important %}
**Consideraciones sobre la eliminación de datos:** Los eventos personalizados se almacenan en MongoDB y están separados de los datos de Snowflake. Si necesitas eliminar datos de eventos personalizados erróneos, debes hacerlo en MongoDB. Las características basadas en Snowflake (como las extensiones de segmento SQL y otras características basadas en Snowflake) utilizan datos de Snowflake, que se gestionan por separado. Eliminar datos de un sistema no los elimina automáticamente del otro.
{% endalert %}

### Orígenes de datos backend a través de la API de Braze {#backend-data-sources-through-the-braze-api}
Braze puede extraer datos de bases de datos de usuarios, transacciones offline y almacenes de datos a través de nuestra [REST or transferencia de estado representacional API]({{site.baseurl}}/api/endpoints/user_data).

### Orígenes de datos frontend a través del SDK or kit de desarrollo de software de Braze {#frontend-data-sources-through-braze-sdk}
Braze captura automáticamente datos propios de orígenes de datos frontend, como los dispositivos de los usuarios, mediante el [SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/user_guide/get_started/sdk_overview). El SDK or kit de desarrollo de software gestiona los usuarios nuevos (anónimos) y administra los datos de su perfil de usuario a lo largo de su ciclo de vida.

### Integraciones de partners {#partner-integrations}
Braze tiene más de 150 partners tecnológicos, a los que llamamos "Alloys". Puedes complementar tus fuentes de datos mediante una red significativamente sólida de [tecnologías interoperables y API de datos.]({{site.baseurl}}/partners/home)

### Conexión directa con el almacén a través de la ingesta de datos en la nube de Braze {#direct-warehouse-connection-through-braze-cloud-data-ingestion}
Puedes transmitir datos de clientes desde tu almacén de datos a la plataforma a través de la [ingesta de datos en la nube de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) en solo unos minutos, lo que te permitirá sincronizar los atributos, eventos y compras relevantes de los usuarios. La integración de la ingesta de datos en la nube admite estructuras de datos complejas, como JSON anidado y matrices de objetos.

La ingesta de datos en la nube puede sincronizar datos de Snowflake, Amazon Redshift, Databricks y Google BigQuery.

## Clasificación {#classification}
La capa de clasificación habilita a tu equipo para clasificar y construir dinámicamente audiencias, llamadas [segmentos]({{site.baseurl}}/user_guide/audience/segments), basándose en los datos que pasan por Braze.

{% alert note %}
En las capas de clasificación, orquestación y personalización es donde tu equipo de marketing realizará gran parte de su trabajo. La mayoría de las veces interactúan con estas capas a través del panel de Braze, nuestra interfaz web. Los desarrolladores tienen un papel en la configuración y personalización de estas capas.
{% endalert %}

Muchos tipos comunes de atributos de usuario, como el nombre, el correo electrónico, la fecha de nacimiento, el país y otros, son seguidos automáticamente por el SDK or kit de desarrollo de software de forma predeterminada. Como desarrollador, trabajarás con tu equipo para definir qué datos adicionales y personalizados tiene sentido seguir para tu caso de uso. Tus datos personalizados influirán en cómo se clasificará y segmentará tu base de usuarios. Configurarás este modelo de datos durante el proceso de implementación.

Más información sobre [datos recopilados automáticamente y datos personalizados]({{site.baseurl}}/developer_guide/analytics).

## Orquestación {#orchestration}
La capa de orquestación permite a tu equipo de marketing diseñar recorridos de usuario basados en los datos de usuario y la interacción previa. Este trabajo se realiza principalmente a través de la interfaz de nuestro panel, pero también tienes la opción de lanzar [campañas a través de la API]({{site.baseurl}}/api/api_campaigns). Por ejemplo, puedes hacer que tu backend le diga a Braze cuándo enviar los mensajes y las campañas que tus especialistas en marketing diseñaron en el panel, y desencadenarlos según la lógica de tu backend. Un ejemplo de mensaje desencadenado por la API podrían ser los restablecimientos de contraseña o las confirmaciones de envío.

{% alert note %}
Las campañas desencadenadas por la API son ideales para casos de uso transaccional más avanzados. Permiten a los especialistas en marketing gestionar el texto de la campaña, las pruebas multivariante y las reglas de reelegibilidad dentro del panel de Braze, a la vez que desencadenan la entrega de ese contenido desde tus servidores y sistemas. La solicitud de la API para desencadenar el mensaje también puede incluir datos adicionales que se incorporarán al mensaje en tiempo real.
{% endalert %}


### Conmutadores de características {#feature-flags}
Braze te permite habilitar o deshabilitar a distancia la funcionalidad de una selección de usuarios mediante [conmutadores de características]({{site.baseurl}}/developer_guide/feature_flags). Esto permite a tus especialistas en marketing dirigirse al segmento correcto de tu base de usuarios con mensajería para características que aún no has desplegado a toda tu audiencia. Pero, además, los conmutadores de características pueden utilizarse para activar y desactivar una característica en producción sin necesidad de desplegar código adicional ni actualizar la tienda de aplicaciones. Esto te permite desplegar nuevas características con seguridad y confianza.

## Personalización {#personalization}
La capa de personalización representa la capacidad de entregar contenido dinámico en tus mensajes. Utilizando Liquid, un lenguaje de personalización muy extendido, tu equipo puede extraer dinámicamente los datos existentes para mostrar el mensaje adaptado a cada destinatario. Además, puedes insertar cualquier información accesible en tu servidor web o a través de la API directamente en los mensajes que envías, como notificaciones push o correos electrónicos, utilizando [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). El contenido conectado se basa en Liquid y utiliza una sintaxis familiar.

Y como este contenido dinámico es programable, los especialistas en marketing pueden incluir valores calculados, respuestas de otras llamadas o elementos del catálogo de productos. Una vez que hayas configurado estos sistemas durante la implementación, tu equipo de marketing podrá hacerlo sin apenas ayuda de los equipos técnicos.

## Acción {#action}
La capa de acción habilita la mensajería real a tus usuarios. El objetivo de la capa de acción es enviar el mensaje adecuado al usuario adecuado en el momento adecuado, basándose en los datos disponibles a través de todas las capas comentadas anteriormente. La mensajería se realiza dentro de tu aplicación o sitio web (como el envío de mensajes dentro de la aplicación o a través de elementos gráficos como carruseles de Content Cards y banners) o fuera de tu experiencia de la aplicación (como el envío de notificaciones push o correos electrónicos).

### Canales de mensajería {#messaging-channels}
Braze se diseñó para gestionar un panorama tecnológico en evolución con su modelo de datos centrado en el usuario e independiente del canal. El panel gestiona la entrega de mensajes y los desencadenantes transaccionales. Por ejemplo, tus especialistas en marketing pueden desencadenar un mensaje servicio de mensajes cortos ofreciendo un cupón para uno de tus escaparates recién abiertos cuando un usuario entre en la geovalla establecida cerca de esta ubicación, o enviar a un usuario un correo electrónico para informarle de que su programa favorito tiene una nueva temporada.

El [SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/user_guide/get_started/sdk_overview) potencia canales de mensajería adicionales: push, mensajes dentro de la aplicación y Content Cards. Integras el SDK or kit de desarrollo de software con tu aplicación o sitio web para permitir que tu equipo de marketing utilice el panel de Braze para coordinar sus campañas en todos los canales de mensajería admitidos.

![Diagrama de los canales de mensajería de Braze disponibles a través del SDK.]({% image_buster /assets/img/getting_started/channels.png %})

## Exportación de datos {#exporting-data}
De manera fundamental, todas las interacciones de los usuarios finales con Braze se rastrean para que puedas medir tu participación y alcance. Y después de que Braze ha agregado tus datos de todas estas fuentes, se pueden exportar de vuelta a tu stack tecnológico utilizando una variedad de herramientas, cerrando el ciclo.

### Currents
[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) es un complemento opcional de Braze que proporciona una exportación granular de datos de transmisión que alimenta continuamente otros destinos de tu stack. Currents es una fuente de datos sin procesar por usuario y por evento que exporta datos cada cinco minutos, o cada 15.000 eventos, lo que ocurra primero. Algunos ejemplos de destinos posteriores para Currents serían Segment, S3, Redshift y Mixpanel, entre otros.

### Intercambio de datos con Snowflake {#snowflake-data-sharing}
La funcionalidad de [intercambio seguro de datos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) de Snowflake permite a Braze darte acceso seguro a los datos en nuestro portal de Snowflake sin preocuparte por fricciones en el flujo de trabajo, puntos de fallo y costes innecesarios que conllevan las relaciones típicas con proveedores de datos. Todo el intercambio se realiza a través de la capa de servicios única de Snowflake y su almacén de metadatos: no se copian ni transfieren datos realmente entre cuentas. Este es un concepto importante porque los datos compartidos no ocupan almacenamiento en la cuenta de un consumidor y, por lo tanto, no contribuyen a tus cargos mensuales por almacenamiento de datos. Los únicos cargos para los consumidores son por los recursos informáticos (es decir, almacenes virtuales) utilizados para consultar los datos compartidos.

### API de exportación de Braze {#braze-export-apis}
La API de Braze proporciona [endpoints]({{site.baseurl}}/api/endpoints/export) que te permiten exportar de manera programática análisis agregados, así como exportar datos de usuarios individuales. Estos datos se pueden exportar para audiencias y Segments de cualquier tamaño.

### CSV {#csvs}
Por último, existe la opción de descargar tus datos a nivel agregado directamente desde el panel como un [CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data). La opción de CSV permite fácilmente a los miembros de tu equipo exportar datos desde Braze.

{% alert tip %}
Si bien la exportación de CSV tiene un límite base de 500.000 filas, las API no tienen un límite en este aspecto.
{% endalert %}

## Uniendo todo {#putting-it-all-together}
Una de tus usuarias, llamémosla Mel, acaba de recibir tu anuncio de producto. Detrás de escena, todas las capas de la plataforma Braze trabajaron juntas para asegurar que este proceso funcionara sin problemas.

La información de Mel fue importada a Braze desde tu plataforma de interacción con los clientes heredada a través de una importación CSV. Cada vez que Mel interactuó con tu aplicación después de la integración, se añadieron más datos a su perfil de cliente.

Tu anuncio de producto se envió a todos los clientes que indicaron que les gustaba un artículo similar en tu aplicación. Definiste estos datos como un evento personalizado. El SDK or kit de desarrollo de software rastreó este evento y segmentó tu base de usuarios en consecuencia. Braze orquestó el mejor momento del día para enviar este anuncio y lo personalizó llamando a Mel por su nombre preferido.

Cuando Mel abre el anuncio, añade tu nuevo producto a su lista de deseos. Braze rastrea automáticamente que hizo clic en el correo electrónico. El SDK or kit de desarrollo de software rastrea que añadió tu nuevo producto a su lista de deseos. Cada vez que interactúan con tu marca, tú y tus usuarios aprenden más unos de otros.

![Diagrama que muestra cómo Braze rastrea las acciones de los usuarios a través de los canales de mensajería.]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})