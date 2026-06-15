---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Este artículo de referencia describe la asociación entre Braze y Jacquard Dynamic Optimisation, que utiliza Braze Currents y contenido conectado para recopilar información de seguimiento de clics de tus suscriptores a través de webhooks. A continuación, Jacquard relaciona esos eventos con tus variantes lingüísticas para optimizar el lenguaje en tiempo real."
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> [Jacquard](https://www.jacquard.com/) aúna inteligencia artificial, lingüística computacional y un espíritu centrado en el cliente para ayudar a desplegar el lenguaje de la marca, a escala, a través de canales personalizados según la voz de tu marca.

Dynamic Optimisation, impulsada por Jacquard X, utiliza Braze Currents y contenido conectado para recopilar información de seguimiento de clics de tus suscriptores a través de webhooks. A continuación, Jacquard relaciona esos eventos con tus variantes lingüísticas para optimizar el lenguaje en tiempo real.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Jacquard | Es necesario tener una [cuenta Jacquard](https://www.jacquard.com/) para beneficiarse de esta asociación. |
| Token de servidor de conexión de Jacquard | Una larga cadena de caracteres que servirá como contraseña de tu Campaign en Braze para acceder a tu lenguaje de Jacquard.<br><br>Puedes solicitarlo a tu administrador del éxito del cliente de Jacquard si aún no te lo han proporcionado. |
| Currents | Para exportar datos a Currents, necesitas tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Solicitar credenciales de Jacquard Amazon S3 {#step-1-request-jacquard-amazon-s3-credentials}

Necesitarás que Jacquard configure un contenedor de Amazon S3 dedicado para recibir tus eventos de seguimiento de clics desde Braze. Ponte en contacto con tu administrador del éxito del cliente de Jacquard para iniciar este proceso. Cuando se cree el contenedor, se te proporcionarán credenciales únicas para crear tu Current.

### Paso 2: Crear un Current {#step-2-create-current}

1. En Braze, selecciona **Currents > Create New Current > Amazon S3 Data Export**.
2. A continuación, ponle un nombre a tu Current e introduce un correo electrónico de contacto.
3. Añade tu ID de clave de acceso de Jacquard AWS y tu clave de acceso secreta en el cuadro de credenciales. A continuación, añade "phrasee-braze-currents-exports" como nombre de contenedor de AWS S3.
4. Por último, añade la carpeta del contenedor de AWS S3 que recibiste de tu administrador del éxito del cliente de Jacquard. Probablemente será el nombre de tu empresa.
5. En **General Settings**, marca la casilla "Include events from anonymous users" y, en **Manage Engagement Events**, marca "Email Click".
6. Cuando hayas terminado, selecciona **Launch Current**.

### Paso 3: Solicitar la eliminación de información de identificación personal (PII) {#step-3-request-to-remove-personally-identifiable-information-pii}

A continuación, ponte en contacto con el equipo de tu cuenta de Braze para asegurarte de que no se transmite a Jacquard ninguna información de identificación personal.

De forma predeterminada, el Current incluirá ciertos atributos PII como el correo electrónico y la dirección. Jacquard no puede recibir ni recibirá PII, por lo que es fundamental que solicites al equipo de tu cuenta de Braze que desactive esta opción para cualquier dato de eventos que se transmita a Jacquard.

### Paso 4: Fragmentos de código de Jacquard X {#step-4-jacquard-x-code-snippets}

Ponte en contacto con el equipo de tu cuenta de Jacquard para obtener los fragmentos de código necesarios.

Estos fragmentos utilizan [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) y, una vez colocados en tus correos electrónicos, introducirán dinámicamente el lenguaje y un píxel de seguimiento para que Jacquard pueda optimizar tu lenguaje en tiempo real utilizando Jacquard X.