---
nav_title: Configurar la orquestación
article_title: Configurar la orquestación
page_order: 2
description: "Aprende a conectar BrazeAI Decisioning Studio Go a tu plataforma de interacción con los clientes para habilitar las comunicaciones personalizadas."
toc_headers: h2
---

# Configurar la orquestación

> BrazeAI Decisioning Studio™ Go necesita conectarse a tu plataforma de interacción con los clientes (CEP) para orquestar comunicaciones personalizadas. Este artículo explica cómo configurar la integración para cada CEP compatible.

## CEP compatibles

Decisioning Studio Go es compatible con las siguientes plataformas de interacción con los clientes:

| CEP | Tipo de integración | Características principales |
|-----|-----------------|--------------|
| **Braze** | Campañas desencadenadas por API | Integración nativa, desencadenamiento en tiempo real |
| **Salesforce Marketing Cloud** | Journey Builder con eventos API | Automatización de consultas SQL, extensiones de datos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecciona tu CEP a continuación para comenzar con la configuración de la integración.

{% tabs %}
{% tab Braze %}

## Configurar la integración con Braze

Para integrar Decisioning Studio Go con Braze, crearás una clave de API, configurarás una campaña desencadenada por API y proporcionarás los identificadores necesarios al portal de Decisioning Studio Go.

### Paso 1: Crear una clave de API REST

1. En el dashboard de Braze, ve a **Configuración** > **API e identificadores** > **Claves de API**.
2. Selecciona **Crear clave de API**.
3. Introduce un nombre para tu clave de API. Un ejemplo es "DecisioningStudioGoEmail".
4. Selecciona los permisos según las siguientes categorías:
    - **Datos de usuario:** selecciona `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Mensajes:** selecciona `messages.send`
    - **Campañas:** selecciona todos los permisos enumerados
    - **Canvas:** selecciona todos los permisos enumerados
    - **Segmentos:** selecciona todos los permisos enumerados
    - **Plantillas:** selecciona todos los permisos enumerados

{: start="5"}
5. Selecciona **Crear clave de API**.
6. Copia la clave de API y pégala en tu portal BrazeAI Decisioning Studio™ Go.

### Paso 2: Localiza tu nombre para mostrar de correo electrónico

1. En el dashboard de Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. Localiza el nombre para mostrar que se utilizará con BrazeAI Decisioning Studio™ Go.
3. Copia y pega el **nombre para mostrar del remitente** en el portal BrazeAI Decisioning Studio™ Go como **nombre para mostrar del correo electrónico**.
4. Copia y pega la dirección de correo electrónico asociada en tu portal BrazeAI Decisioning Studio™ Go como **dirección de correo electrónico del remitente**, que combina la parte local y el dominio.

### Paso 3: Encuentra tu URL de Braze y tu ID de aplicación

**Para encontrar tu URL de Braze:**
1. Ve al dashboard de Braze.
2. En la ventana de tu navegador, la URL de Braze comienza por `https://` y termina por `braze.com`. Un ejemplo de URL de Braze es `https://dashboard-01.braze.com`.

**Para encontrar tu ID de aplicación (clave de API):**

{% alert note %}
Braze ofrece ID de aplicaciones (denominados claves de API en el dashboard de Braze) que puedes utilizar con fines de seguimiento, por ejemplo, para asociar la actividad con una aplicación específica en tu espacio de trabajo. Si utilizas ID de aplicaciones, BrazeAI Decisioning Studio™ Go permite asociar un ID de aplicación con cada experimentador.<br><br>Si no utilizas ID de aplicaciones, puedes introducir cualquier cadena de caracteres como marcador de posición.
{% endalert %}

1. En el dashboard de Braze, ve a **Configuración** > **Configuración de la aplicación**.
2. Ve a la aplicación de la que deseas hacer seguimiento.
3. Copia y pega la **clave de API** en tu portal BrazeAI Decisioning Studio™ Go.

### Paso 4: Crear una campaña desencadenada por API

1. En el dashboard de Braze, ve a **Mensajería** > **Campañas**.
2. Selecciona **Crear campaña**.
3. Para el tipo de campaña, selecciona **Campaña de API**.
4. Introduce un nombre para tu campaña. Un ejemplo es "Decisioning Studio Go Email".

![Una campaña de API denominada "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. Para tu canal de mensajería, selecciona **Correo electrónico**.

![Opción para seleccionar tu canal de mensajería para la campaña de API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. En **Opciones adicionales**, selecciona la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña**.
7. Para el tiempo de reelegibilidad, introduce **1** y selecciona **Horas** en el menú desplegable.

![Reelegibilidad para la campaña de API seleccionada.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. Selecciona **Guardar campaña**.

### Paso 5: Copia los ID de tu campaña y mensaje

1. En tu campaña de API, copia el **ID de la campaña**. A continuación, ve al portal BrazeAI Decisioning Studio™ Go y pega el **ID de la campaña**.

![Un ejemplo de ID de variación de mensaje para copiar y pegar.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2. Copia el **ID de variación del mensaje**. A continuación, ve al portal BrazeAI Decisioning Studio™ Go y pega el **ID de variación del mensaje**.

### Paso 6: Localiza un ID de usuario de prueba

Para probar tu integración, necesitarás un ID de usuario:

Si tu espacio de trabajo utiliza [cifrado a nivel de campo de identificadores]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/), cualquier nuevo usuario de prueba que crees con el punto de conexión `/users/track` debe cumplir los requisitos de correo electrónico para espacios de trabajo cifrados. Envía el campo `email` como el hash HMAC-SHA256 codificado en Base64 del valor de correo electrónico en minúsculas, y envía `email_encrypted` como el valor de correo electrónico cifrado generado con tus claves de cifrado PII configuradas.

1. En el dashboard de Braze, ve a **Audiencia** > **Buscar usuarios**.
2. Busca al usuario por su ID de usuario externo, alias de usuario, correo electrónico, número de teléfono o token de notificaciones push.
3. Copia el ID de usuario para referenciarlo en tu configuración.

![Ejemplo de perfil de usuario obtenido al localizar un usuario con su ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurar la integración con SFMC

Para integrar Decisioning Studio Go con Salesforce Marketing Cloud, configurarás un paquete de aplicaciones, crearás una automatización de consultas de datos y construirás un recorrido para gestionar los envíos desencadenados.

### Parte 1: Configurar un paquete de aplicaciones SFMC

1. Ve a la página de inicio de Marketing Cloud.
2. Abre el menú en el encabezado global y selecciona **Configuración**.
3. Ve a **Aplicaciones** en **Herramientas de plataforma** en el panel de navegación lateral y, a continuación, selecciona **Paquetes instalados**.
4. Selecciona **Nuevo** para crear un paquete de aplicaciones.
5. Asigna un nombre y una descripción al paquete de aplicaciones.

![Un paquete de aplicaciones con el nombre "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. Selecciona **Añadir componente**.
7. En **Tipo de componente**, selecciona **Integración API**. A continuación, selecciona **Siguiente**.
8. Para el **tipo de integración**, selecciona **De servidor a servidor**. A continuación, selecciona **Siguiente**.
9. Selecciona los siguientes ámbitos recomendados solo para tu paquete de aplicaciones:
    - Canales > Correo electrónico > Leer, escribir, enviar
    - Canales > OTT > Leer
    - Canales > Push > Leer
    - Canales > SMS > Leer
    - Canales > Social > Leer
    - Canales > Web > Leer
    - Activos > Documentos e imágenes > Leer, escribir
    - Activos > Contenido guardado > Leer, escribir
    - Automatización > Automatizaciones > Leer, escribir, ejecutar
    - Automatización > Recorridos > Leer, escribir, ejecutar, activar/detener/pausar/enviar/programar
    - Contactos > Audiencias > Leer
    - Contactos > Lista y suscriptores > Leer, escribir
    - Plataforma Cross Cloud > Audiencia del mercado > Ver
    - Plataforma Cross Cloud > Miembro de la audiencia del mercado > Ver
    - Plataforma Cross Cloud > Marketing Cloud Connect > Leer
    - Datos > Extensiones de datos > Leer, escribir
    - Datos > Ubicaciones de archivos > Leer
    - Datos > Seguimiento de eventos > Leer, escribir
    - Notificaciones de eventos > Devoluciones de llamada > Leer
    - Notificaciones de eventos > Suscripciones > Leer

{% details Mostrar imagen de los ámbitos recomendados %}

![Los ámbitos recomendados para el paquete de aplicaciones de Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. Selecciona **Guardar**.
11. Copia y pega los siguientes campos en el portal BrazeAI Decisioning Studio™ Go: **Client Id**, **Client Secret**, **Authentication Base URI**, **REST Base URI**, **SOAP Base URI**.

### Parte 2: Configurar una automatización de consultas de datos

#### Paso 1: Crear una nueva automatización

1. Desde la página de inicio de Salesforce Marketing Cloud, ve a **Journey Builder** y selecciona **Automation Studio**.

![Opción de Automation Studio en la navegación de Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. Selecciona **Nueva automatización**.
3. Arrastra y suelta un nodo **Planificación** como **Origen inicial**.

!["Planificación" como origen inicial de un recorrido.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. En el nodo **Planificación**, selecciona **Configurar**.
5. Configura lo siguiente para la planificación:
    - **Fecha de inicio:** el día de mañana en el calendario
    - **Hora:** **12:00 AM**
    - **Zona horaria:** **(GMT-05:00) Este (EE. UU. y Canadá)**
6. Para **Repetir**, selecciona **Diario**.
7. Configura esta planificación para que nunca termine.
8. Selecciona **Hecho** para guardar la planificación.

![Un ejemplo de planificación definida para el 25 de enero de 2024 a las 12 AM ET, que se repite todos los días.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Paso 2: Crea tus consultas SQL

A continuación, crea 2 consultas SQL: una consulta de suscriptores y una consulta de interacción. Estas consultas permiten a BrazeAI Decisioning Studio™ Go recuperar datos para completar la audiencia e incorporar eventos de interacción.

**Consulta de suscriptores:**

1. Arrastra y suelta una **consulta SQL** en el canvas.
2. Selecciona **Elegir**.
3. Selecciona **Crear nueva actividad de consulta**.
4. Asigna un nombre y una clave externa a la consulta. Recomendamos utilizar el nombre y la clave externa sugeridos para la consulta de suscriptores que se proporcionan en tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo "OFE_Subscribers_query_Test5" y la clave externa.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. Selecciona **Siguiente**.
6. En tu portal BrazeAI Decisioning Studio™ Go, localiza la consulta SQL de datos del sistema en **Recursos de consulta de suscriptores**.
7. Copia y pega la consulta en el cuadro de texto y selecciona **Siguiente**.

![Un ejemplo de consulta en la sección Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. En tu portal BrazeAI Decisioning Studio™ Go, en la sección **Recursos para usar**, localiza la clave externa de la extensión de datos de destino. A continuación, pégala en la barra de búsqueda para buscar.

![Una clave externa pegada en la barra de búsqueda.]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. Selecciona la extensión de datos que coincida con la clave externa que buscaste. El nombre de la extensión de datos de destino también se proporciona en tu portal BrazeAI Decisioning Studio™ Go para que puedas consultarlo. La **extensión de datos** para la consulta de suscriptores debe terminar con el sufijo `BASE_AUDIENCE_DATA`.

![El nombre de la extensión de datos que coincide con la clave externa del ejemplo.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. Selecciona **Sobrescribir** y, a continuación, **Siguiente**.

**Consulta de interacción:**

1. Arrastra y suelta una **consulta SQL** en el canvas.

!["Consulta SQL" añadida como actividad en el recorrido.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. Selecciona **Elegir**.
3. Selecciona **Crear nueva actividad de consulta**.
4. Asigna un nombre y una clave externa a la consulta. Recomendamos utilizar el nombre y la clave externa sugeridos para la consulta de interacción que se proporcionan en tu portal BrazeAI Decisioning Studio™ Go.

![Un ejemplo "OFE_Engagement_query" y la clave externa.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. Selecciona **Siguiente**.
6. En tu portal BrazeAI Decisioning Studio™ Go, localiza la consulta SQL de datos del sistema en **Recursos de consulta de interacción**.
7. Copia y pega la consulta en el cuadro de texto y selecciona **Siguiente**.

![Un ejemplo de consulta en la sección Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. Localiza y selecciona la extensión de datos de destino para la consulta de interacción especificada en tu portal BrazeAI Decisioning Studio™ Go.

{% alert tip %}
El nombre de la extensión de datos de destino también se proporciona en tu portal BrazeAI Decisioning Studio™ Go para que puedas consultarlo. Asegúrate de que estás viendo la extensión de datos de destino para la consulta de interacción. La **extensión de datos** para la consulta de interacción debe terminar con el sufijo ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9. Selecciona **Sobrescribir** y, a continuación, **Siguiente**.

![El nombre de la extensión de datos que coincide con la clave externa del ejemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Paso 3: Ejecuta la automatización

1. Asigna un nombre a la automatización y selecciona **Guardar**.

![Un ejemplo de automatización "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. A continuación, selecciona **Ejecutar una vez** para confirmar que todo funciona según lo esperado.
3. Selecciona ambas consultas y selecciona **Ejecutar**.

![Una automatización "OFE_Experimenter_Test5_Automation" con una lista de actividades de consultas SQL seleccionadas para ejecutar.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. Selecciona **Ejecutar ahora**.

![Una actividad de consulta SQL seleccionada.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Ahora puedes comprobar que la automatización se está ejecutando correctamente. Ponte en contacto con soporte de Braze para obtener más ayuda si tu automatización no funciona como se esperaba.

### Parte 3: Crea tu recorrido SFMC

#### Paso 1: Configura el recorrido

1. En Salesforce Marketing Cloud, ve a **Journey Builder** > **Journey Builder**.
2. Selecciona **Crear nuevo recorrido**.
3. Para el tipo de recorrido, selecciona **Recorrido de varios pasos** y, a continuación, selecciona **Crear**.

![Una fuente de entrada de eventos API conectada a un nodo de división de decisiones y a varios nodos de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Paso 2: Construye el recorrido

**Crear una fuente de entrada:**

1. Para la fuente de entrada, arrastra **API Event** al Journey Builder.

!["API Event" seleccionado como fuente de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2. En el **API Event**, selecciona **Crear un evento**.

![La opción "crear un evento" en el API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. Selecciona **Extensión de datos**. Localiza y selecciona la extensión de datos en la que BrazeAI Decisioning Studio™ Go escribirá las recomendaciones.
4. Selecciona **Resumen** para guardar los cambios.
5. Selecciona **Hecho** para guardar el evento API.

![Resumen del evento API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Añadir una división de decisiones:**

1. Arrastra y suelta una **división de decisiones** después del **evento de entrada de API**.
2. En los detalles de la **división de decisiones**, selecciona **Editar** para la primera ruta.

![Detalles de la división de decisiones con el botón "Editar".]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. Actualiza la **división de decisiones** para utilizar el ID de plantilla pasado por la extensión de datos de recomendaciones. Localiza el campo correspondiente en **Datos del recorrido**.

![La sección Datos del recorrido en la ruta 1 de la división de decisiones.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. Selecciona tu evento de entrada y localiza el campo de ID de plantilla deseado, luego arrástralo al espacio de trabajo.

![El ID de la plantilla de correo electrónico que se va a incluir.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. Introduce el ID de la plantilla de tu primera plantilla de correo electrónico y, a continuación, selecciona **Hecho**.
6. Selecciona **Resumen** para guardar esta ruta.
7. Añade una ruta para cada una de tus plantillas de correo electrónico y, a continuación, repite los pasos 4 a 6 anteriores para establecer los criterios de filtrado de modo que el ID de la plantilla coincida con el valor de ID de cada plantilla.
8. Selecciona **Hecho** para guardar el nodo de **división de decisiones**.

![Dos rutas en una división de decisiones para cada ID de plantilla de correo electrónico.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Añadir un correo electrónico para cada división de decisiones:**

1. Arrastra un nodo de **correo electrónico** a cada ruta de la **división de decisiones**.
2. Selecciona **Correo electrónico** y, a continuación, selecciona la plantilla adecuada que debe ir en cada ruta (es decir, la plantilla con el valor de ID debe coincidir con la lógica de tu división de decisiones).

![Un nodo de correo electrónico añadido al recorrido.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Paso 3: Activa el recorrido

Después de configurar tu recorrido, actívalo y comparte los siguientes detalles con el equipo de BrazeAI Decisioning Studio™ Go:

* ID del recorrido
* Nombre del recorrido
* Clave de definición de evento API
* Clave externa de la extensión de datos de recomendaciones

{% alert note %}
El portal BrazeAI Decisioning Studio™ Go te muestra la automatización de SFMC que ha configurado para exportar los datos de suscriptores y de interacción una vez al día. Si abres esta automatización en SFMC, asegúrate de reanudarla y volver a ponerla en vivo.
{% endalert %}

1. En el portal BrazeAI Decisioning Studio™ Go, copia el **nombre del recorrido**.
2. A continuación, en Salesforce Marketing Cloud Journey Builder, pega el nombre del recorrido en la barra de búsqueda.
3. Selecciona el nombre del recorrido. Ten en cuenta que el recorrido se encuentra actualmente en estado de borrador.
4. Selecciona **Validar**.

![El recorrido completado para activar.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. A continuación, revisa los resultados de la validación y selecciona **Activar**.

![Recomendaciones enumeradas en la sección Reglas de validación.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. En el resumen **Activar recorrido**, selecciona **Activar** de nuevo.

![Resumen del recorrido.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

¡Ya está todo listo! Ahora puedes comenzar a desencadenar envíos a través de BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Próximos pasos

Ahora que has configurado la orquestación, continúa con el diseño de tu agente:

- [Diseña tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)