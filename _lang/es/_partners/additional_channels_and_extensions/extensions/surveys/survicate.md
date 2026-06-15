---
nav_title: Survicate
article_title: Survicate
description: "Este artículo de referencia describe la asociación entre Braze y Survicate, una plataforma de opiniones de clientes que te ayuda a recopilar, analizar y actuar sobre la información de los clientes en múltiples canales y a lo largo del recorrido del usuario."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) es una plataforma de opiniones de clientes que recopila, analiza y actúa sobre la información de los clientes a través de múltiples canales y durante todo el recorrido del usuario. [Ver una demostración rápida](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Esta integración está mantenida por Survicate._

## Sobre la integración {#about-the-integration}

Utiliza la integración nativa de Survicate y Braze para sincronizar las respuestas de las encuestas por correo electrónico, dentro de la aplicación, móvil o web con los perfiles de cliente de Braze. Las respuestas a las encuestas se sincronizan automáticamente con los perfiles de usuario de Braze como atributos personalizados o eventos. La información sobre las opiniones en tiempo real facilita el seguimiento y el análisis de las opiniones junto con los datos de clientes y la creación de seguimientos específicos y segmentos hiperpersonalizados.

## Casos de uso {#use-cases}

Braze y Survicate trabajan juntos para cubrir una amplia gama de casos de uso de opiniones, ayudándote a recopilar información accionable de los usuarios y a mejorar la experiencia del cliente:

- Mejora las tasas de respuesta de las encuestas con encuestas incrustadas que pueden responderse desde un buzón de entrada de correo electrónico.
- Obtén información en las fases críticas del recorrido del cliente a través de mensajes dentro de la aplicación de Braze.
- Utiliza la información almacenada en Survicate para crear segmentos más inteligentes en Braze.
- Automatiza campañas de seguimiento basadas en las opiniones de los clientes.
- Utiliza la información de los clientes para desencadenar flujos de trabajo personalizados.
- Llega a una audiencia más amplia con encuestas traducidas automáticamente.
- Envía eventos a los perfiles de contacto de Braze cuando alguien responda a tu encuesta.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Survicate | Necesitas una cuenta de Survicate para activar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con el permiso `users.track`. <br><br> Se puede crear en el dashboard de Braze desde **Settings** > **APIs and Identifiers**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Características principales de la integración {#key-features-of-the-integration}

La integración de Survicate y Braze ofrece sincronización de datos en tiempo real, por lo que la información más actualizada de las encuestas de Survicate está disponible inmediatamente en Braze. Basándote en las respuestas a las encuestas, puedes utilizar estos datos para emprender acciones oportunas y personalizadas.

- **Envía las respuestas de las encuestas a Braze como atributos personalizados de usuario**: Enriquece los perfiles de usuario de Braze con datos procedentes de respuestas a encuestas.
- **Desencadena eventos personalizados en Braze**: Utiliza eventos basados en respuestas a encuestas para dirigirte a grupos específicos o iniciar campañas de seguimiento.
- **Construye segmentos detallados**: Crea segmentos en Braze utilizando los datos de las encuestas de Survicate para personalizar aún más tu alcance.

## Integración {#integration}

### Crea tus encuestas en Survicate {#creating-your-surveys-in-survicate}

#### Incrusta tu encuesta en un correo electrónico o crea una encuesta con un enlace que se pueda compartir {#embed-your-survey-in-an-email-or-create-a-shareable-link-survey}

1.  En Survicate, haz clic en **+ Create new survey**, selecciona cualquier método de creación (una plantilla, utilizar la creación de encuestas mediante IA o añadir tus propias preguntas) y el tipo de encuesta Email o Shareable link:
![Se selecciona Braze en el creador de encuestas.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2. En la pestaña Configure de la encuesta, selecciona **Braze** como herramienta para identificar a los encuestados:
![Se selecciona Braze en la pestaña Configure de la encuesta.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3. Después de configurar tu encuesta, ve a la pestaña Share y decide cómo enviar tu encuesta por correo electrónico. Hay dos opciones: puedes enviar tu **encuesta como un enlace** o **incrustar la primera pregunta en el correo electrónico** para que los encuestados empiecen a responder a la encuesta directamente desde el correo electrónico.

{% details Opción de enlace de encuesta %}

1. Obtén un enlace a tu encuesta desde el botón Copy survey link:

![Obtén un enlace a tu encuesta desde el botón Copy survey link.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2. Oculta el enlace de la encuesta detrás de un botón CTA o hipervínculo en tu correo electrónico de Braze.

![Oculta el enlace de la encuesta detrás de un botón CTA o hipervínculo en tu correo electrónico de Braze.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Opción de incrustación en correo electrónico %}

Muestra la primera pregunta directamente en el cuerpo del correo electrónico para iniciar la encuesta desde el correo electrónico. A continuación, se redirige a los encuestados a una página de destino para que completen el resto de la encuesta.

1. Haz clic en **Get email code** y, a continuación, **Copy the HTML code**:

![Get email code]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2. Ve a la campaña de Braze que quieras utilizar para la encuesta, haz clic en **Edit email body** y añade un bloque HTML a tu plantilla:

![Obtener código HTML de bloque]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3. Sustituye el código por el que copiaste de tu encuesta de Survicate. A continuación, verás la primera pregunta de la encuesta en la plantilla:

![Sustituye el código por el que copiaste de tu encuesta de Survicate]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. Programa el correo electrónico, elige tu grupo objetivo y tu campaña estará lista para enviar.

{% enddetails %}

### Encuesta de In-App Message de Braze {#braze-in-app-message-survey}

1. Haz clic en **+ Create new survey**, selecciona cualquier método de creación (una plantilla, utilizar la creación de encuestas mediante IA o añadir tus propias preguntas) y, a continuación, elige In-platform surveys y el tipo de encuesta Braze In-App Message:

![Haz clic en + Create new survey, selecciona cualquier método de creación]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2. Lanza tu encuesta de In-App Message de Braze accediendo a tu cuenta de Braze y, a continuación, a **Messaging** > **Campaigns** > **Create campaign** > **In-app message**:
![Lanza tu encuesta de In-App Message de Braze]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Lanza tu encuesta de In-App Message de Braze a través del editor tradicional {#launch-your-braze-in-app-messenger-survey-via-the-traditional-editor}

1. Si utilizas el editor tradicional, en el tipo de mensaje, elige **Custom code**:

![Elegir Custom code]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2. A continuación, pega el código de la pestaña Launch de tu encuesta en el campo HTML:

![Pega el código de la pestaña Launch de tu encuesta en el campo HTML]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze muestra los mensajes dentro de la aplicación en un iframe de forma predeterminada mientras el fondo de la aplicación está bloqueado. Para permitir la interacción con tu aplicación mientras aparecen las encuestas de Survicate, debes:<br><br>

- Añadir `opts.useBrazeIframeClipper = true` a tu fragmento de código Survicate-Braze.
- Instalar el [paquete](https://www.npmjs.com/package/@survicate/braze-bridge-npm) `@survicate/braze-bridge-npm` en el archivo donde inicialices Braze y utilizar la función `initBrazeBridge`.

Puedes encontrar un fragmento de código de muestra y una implementación de React [en el sitio de desarrolladores de Survicate](https://developers.survicate.com/javascript/installation/#braze).
{% endalert %}

{: start="3"}
3. En tu campaña de Braze, configura los pasos **Target** y **Assign**. Una vez completado, tu campaña estará lista para lanzarse. En el paso **Review**, puedes ver el aspecto de la campaña. La encuesta aparece en tu sitio web en el lugar especificado en el panel de Survicate, como se ha descrito anteriormente.

### Habilitación de la integración de Braze {#enabling-the-braze-integration}

1. Para habilitar la integración de Braze, ve a **Integrations**, busca y selecciona "Braze".

![Selecciona Braze]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2. Haz clic en **Connect** para configurar la autorización.

3. Introduce la clave de API del espacio de trabajo de tu cuenta de Braze y la URL de la instancia de Braze:

![Introduce la clave de API del espacio de trabajo de tu cuenta de Braze y la URL de la instancia de Braze]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Para conectar Survicate a Braze, la clave de API de Braze debe tener permisos `users.track`.
{% endalert %}

### Conectar tus encuestas a Braze {#connecting-your-surveys-to-braze}

Ahora que la integración de Braze está conectada, puedes establecer una configuración individual para cada encuesta. Ve a tu encuesta, selecciona la pestaña **Connect** y elige **Braze** de la lista de integraciones disponibles.

![Ve a tu encuesta, selecciona la pestaña Connect y elige Braze]({% image_buster /assets/img/survicate/survicate_14.png %})

### Envío de respuestas a Braze como atributos personalizados {#sending-responses-to-braze-as-custom-attributes}

Configura las respuestas de las encuestas para que fluyan hacia Braze como atributos personalizados, lo que enriquece tus perfiles de usuario de Braze con los datos recopilados.

1. En la pestaña Settings de la integración de Braze, busca la sección **Update fields**.

![Selecciona la sección Update fields]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2. Selecciona la pregunta de la que quieres actualizar los campos. Para evitar inundar de datos tus perfiles de usuario de Braze, puedes enviar respuestas solo a las preguntas elegidas.

![Selecciona la pregunta de la que quieres actualizar los campos]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
Las preguntas de clasificación y matriz no son compatibles con esta integración de Braze.
{% endalert %}

{: start="3"}
3. Añade el nombre del atributo personalizado que quieres actualizar en el campo **User**:

![Añade el nombre del atributo personalizado que quieres actualizar en el campo User]({% image_buster /assets/img/survicate/survicate_17.png %})

De forma predeterminada, Survicate envía el contenido de una respuesta a una encuesta como un valor de atributo. Puedes cambiar la etiqueta para hacerla más corta o ajustarla a tu estructura de datos haciendo clic en **Edit mapping** para modificar estos valores:

![La respuesta a la encuesta como valor de atributo]({% image_buster /assets/img/survicate/survicate_18.png %})

![Haz clic en Edit mapping para modificar estos valores]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Para NPS, Survicate envía valores mapeados basados en el grupo de respuesta de la pregunta NPS®. Sin embargo, si quieres recibir valores numéricos, puedes activar Send Answers as 0-10 values.
{% endalert %}

![Survicate envía valores mapeados en función del grupo de respuesta]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. Conecta más preguntas a tu integración haciendo clic en **+ Add new** y aplicando los mismos pasos.

![Conecta más preguntas a tu integración]({% image_buster /assets/img/survicate/survicate_21.png %})

### Enviar eventos a los perfiles de los contactos de Braze {#sending-events-to-braze-contacts-profiles}

Aparte de la configuración anterior, cada vez que un encuestado responde a una pregunta de la encuesta, Survicate puede enviar un evento personalizado en Braze denominado `survicate-question-answered`.
En el panel de Survicate, en Enviar respuestas como atributos personalizados, puedes elegir si quieres enviar el evento para todas las preguntas, las preguntas elegidas en la pestaña **Update fields**, o para ninguna:

![Puedes elegir si quieres enviar el evento para todas las preguntas]({% image_buster /assets/img/survicate/survicate_22.png %})

Si decides enviar los eventos, podrás ver en los perfiles de los usuarios cuántas veces han respondido a las encuestas de Survicate y cuándo lo hicieron por última vez:

![Respuestas]({% image_buster /assets/img/survicate/survicate_23.png %})

El evento contiene propiedades del evento con la respuesta a la pregunta e información sobre la encuesta, la pregunta y el encuestado. Puedes utilizar este evento para crear segmentos. Por ejemplo, crea un segmento de usuarios que hayan respondido a una encuesta después de una fecha concreta o un número determinado de veces:

![El evento contiene propiedades del evento con la respuesta]({% image_buster /assets/img/survicate/survicate_24.png %})

También puedes utilizar estos datos al crear una campaña en Braze.

![También puedes utilizar estos datos al crear una campaña en Braze]({% image_buster /assets/img/survicate/survicate_25.png %})

### Prueba la integración {#test-the-integration}

Cuando tengas tu encuesta lista y la integración configurada, puedes probarla sin salir de Survicate haciendo clic en el botón **Test Integration**, junto a cualquier atributo, etiqueta o configuración de nuevo contacto que hayas creado. Survicate crea un contacto de prueba (`braze-test@survicate.com`) en tu cuenta de Braze. El perfil del contacto incluye campos actualizados según la configuración.

![Haz clic en el botón Test Integration]({% image_buster /assets/img/survicate/survicate_26.png %})

En Braze, puedes ver datos de muestra de los campos mapeados en el contacto ficticio de Survicate:

![Datos de muestra de los campos mapeados en el contacto ficticio de Survicate]({% image_buster /assets/img/survicate/survicate_27.png %})

### Analizar los resultados de tu encuesta {#analyzing-your-survey-results}

Después de recopilar respuestas a través de tu encuesta de Braze, es hora de analizar los comentarios y la información que han compartido tus encuestados. Survicate te permite revisar fácilmente los resultados, las estadísticas y las tendencias para tomar nuevas medidas.

### Comentarios en Survicate {#feedback-in-survicate}

Cuando tu encuesta empiece a recoger respuestas, las verás inmediatamente en la pestaña Analyze de la encuesta.

![Respuestas en la pestaña Analyze]({% image_buster /assets/img/survicate/survicate_28.png %})

La pestaña Analyze te muestra los resultados globales con estadísticas y datos a lo largo del tiempo, así como respuestas individuales para examinar en detalle cada envío de encuesta.

### Comentarios en Braze {#feedback-in-braze}

Si actualizas los campos de usuario con las respuestas de la encuesta o envías las respuestas como eventos personalizados, podrás ver los datos de la encuesta sincronizados en tiempo real. En Braze, ve a un contacto concreto que haya respondido a tu encuesta. Verás tanto los datos basados en la respuesta como los eventos en la vista principal del contacto.

![Datos de la encuesta sincronizados en tiempo real]({% image_buster /assets/img/survicate/survicate_29.png %})