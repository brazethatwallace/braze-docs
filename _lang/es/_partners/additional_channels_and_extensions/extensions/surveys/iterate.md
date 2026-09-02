---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Este artículo de referencia describe la asociación entre Braze e Iterate, que te permite enriquecer los datos de clientes utilizando cuestionarios para añadir información adicional."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) proporciona herramientas de cuestionarios y comentarios para ayudarte a aprender de tus clientes, ofreciendo experiencias de investigación fáciles de usar que se adaptan a tu marca.

_Esta integración la mantiene Iterate._

## Sobre la integración {#about-the-integration}

La integración de Iterate con Braze te permite entregar cuestionarios de Iterate de forma nativa y fácilmente dentro de tu producto o campañas. Las respuestas a los cuestionarios pueden registrarse como atributos de usuario personalizados en Braze, lo que te permite construir una imagen completa de tus usuarios o crear nuevas y potentes audiencias y segmentos.

Con el SDK de Braze instalado en tu aplicación o sitio web, puedes utilizar las herramientas de segmentación y orientación disponibles en Braze para enviar cuestionarios a través de mensajes dentro de la aplicación a una parte específica de tu audiencia en función de cualquier desencadenante o segmento personalizado. Los cuestionarios de Iterate también pueden incrustarse directamente en tus campañas de correo electrónico o incluirse como enlaces en tus campañas push o de otro tipo.

## Requisitos previos {#prerequisites}

| Requisito | Origen |
|---|---|
| Cuenta Iterate | Se necesita una [cuenta de Iterate](https://iteratehq.com) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. Para enviar cuestionarios a través de mensajes dentro de la aplicación de Braze, también necesitarás el permiso `kpi.mau.data_series`.<br><br> Puede crearse en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Con Iterate, puedes recopilar casi cualquier tipo de datos. Desde información personal (nombre, edad, correo electrónico), datos de rendimiento (NPS, satisfacción del cliente, puntuaciones con estrellas), preferencias (dispositivo preferido, frecuencia de comunicación preferida) o personalidad (libro, perro o gato favoritos). Lo que preguntes depende enteramente de ti, y del tipo de datos que quieras recopilar o de audiencias que quieras crear.

## Integración {#integration}

### Para empezar: conectar Braze con Iterate {#getting-started-connect-braze-with-iterate}

Inicia sesión en tu cuenta de Iterate y añade tu punto de conexión REST de Braze y tu clave de API REST en la página **Company Settings**.

### Enviar cuestionarios como mensaje dentro de la aplicación {#deliver-surveys-as-an-in-app-message}

#### Paso 1: Crea tu cuestionario {#step-1-create-your-survey}

Antes de crear tu cuestionario, activa la opción **Enable in-app message surveys** en la configuración de Iterate.

A continuación, crea un nuevo cuestionario en Iterate y añade las preguntas pertinentes. Si lo consideras oportuno, también puedes incluir un mensaje de aviso que se mostrará antes del cuestionario. Selecciona **Send via Braze In-App Message** como tipo de cuestionario.

Una vez completado tu cuestionario, en la pestaña **Publish**, copia el fragmento de código que aparece en **Copy and paste your embed code**.

#### Paso 2: Comparte tu cuestionario {#step-2-share-your-survey}

En Braze, crea una nueva campaña de mensajería dentro de la aplicación, selecciona **Custom Code** como tipo de mensajería y pega tu fragmento de código en el mensaje. A continuación, selecciona **Wait for User to Dismiss** como comportamiento del mensaje al hacer clic.

Continúa configurando tu campaña como lo harías con cualquier otra campaña de mensajería dentro de la aplicación, eligiendo un método de entrega y dirigiéndote a una audiencia.

### Enviar cuestionarios por correo electrónico o push {#deliver-surveys-through-email-or-push}

#### Paso 1: Crea tu cuestionario

Crea un nuevo cuestionario por correo electrónico o enlace en Iterate y añade las preguntas pertinentes. Una vez redactadas las preguntas y personalizado el diseño, selecciona **Send survey** > **Integrations** > **Braze**.

A continuación, verás las opciones de configuración para enviar respuestas a Braze. Activa la integración para poder enviar las respuestas de ese cuestionario a Braze.

#### Paso 2: Comparte tu cuestionario

Tu cuestionario puede compartirse de dos maneras: incrustando la primera pregunta en tu mensaje o incluyendo un enlace directo al cuestionario en la plataforma Iterate.

![Opciones de enlace de Iterate]({% image_buster /assets/img/iterate.png %})

- **Incrustar el código**
  - Copia el fragmento de código en **Email embed code** dentro de la sección de integración de Braze de la pestaña **Send survey**. Inserta el código en el HTML de tu correo electrónico de Braze donde desees que aparezca el comienzo del cuestionario.
  - Si tienes dificultades para mostrar las preguntas del cuestionario o si no tienen el formato correcto, deberás ir a la pestaña **Sending Info** en el creador de mensajes y desmarcar **Inline CSS**.
- **Incluir un enlace**
  - Copia el enlace que aparece en **Survey Link** en la sección de integración de Braze de la pestaña **Send survey**. Ten en cuenta que el Liquid incluido en el enlace {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} se sustituirá automáticamente para cada usuario al enviarlo.

### Próximos pasos: crea campañas de seguimiento {#next-steps-build-follow-up-campaigns}

A medida que los usuarios respondan, verás cómo sus perfiles se llenan de datos en tiempo real. Estos datos pueden utilizarse para segmentar a los usuarios y enviar campañas de seguimiento personalizadas. Por ejemplo, si envías la pregunta "¿Te gustan nuestros productos?", puedes crear segmentos de usuarios que tengan el atributo de usuario personalizado `Do you enjoy our products?` que hayan respondido "Sí" o "No" y dirigirte a estos usuarios.

## Eventos personalizados de Braze {#braze-custom-events}

Cuando un usuario responde a una pregunta del cuestionario, Iterate desencadena un evento personalizado dentro de Braze denominado `survey-question-response`. Los eventos personalizados te permiten desencadenar cualquier número y tipo de campañas de seguimiento.

## Personalizar los nombres de los atributos de usuario {#customize-user-attribute-names}

Por defecto, el atributo de usuario creado para una pregunta es el mismo que el prompt.
En algunos casos, es posible que desees personalizarlo. Para ello, haz clic en el menú desplegable **Customize user attribute names** en el paso **Create your Survey** e introduce los nombres personalizados que desees.