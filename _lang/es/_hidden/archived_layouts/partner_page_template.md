---
nav_title: Página del socio

page_order: 4

#Required
description: "Esta es la descripción de la Búsqueda de Google. Los caracteres que pasan de 160 se truncan, sé breve."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks


noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Nombre del socio] {#partner-name}

> ¡Te damos la bienvenida a la plantilla de la página del socio! Aquí encontrarás todo lo que necesitas para crear tu propia página del socio. En esta primera sección, deberías describir al socio en el primer párrafo en una o dos oraciones. Incluye también un enlace al sitio principal de ese socio.

En el segundo párrafo, deberías explorar y explicar la relación entre Braze y este socio. En este párrafo se debería explicar cómo Braze y este socio trabajan juntos para estrechar el vínculo entre el usuario de Braze y su cliente. Explica la "elevación" que se produce cuando un usuario de Braze se integra o aprovecha a este socio y sus servicios.

## Requisitos o prerrequisitos {#requirements-or-prerequisites}

Esta sección trata sobre lo que necesitas para integrarte con el partner y empezar a utilizar sus servicios. La mejor forma de presentar esta información es con un párrafo instructivo rápido que describa cualquier detalle importante no técnico que sea necesario conocer, como si tu integración estará sujeta a verificaciones de seguridad o autorizaciones adicionales. A continuación, deberías usar una tabla para describir los requisitos técnicos de la integración.

{% alert important %}
Los siguientes requisitos son requisitos típicos que podrías necesitar de Braze. Recomendamos usar los títulos con atributos, el origen, los enlaces y la redacción tal como se indican en la siguiente tabla. Asegúrate de ajustar la descripción para que sepas para qué se utiliza cada uno de estos requisitos.
{% endalert %}

| Requisito | Origin | Acceso | Descripción |
|---|---|---|---|
| Clave de API REST or transferencia de estado representacional del espacio de trabajo de Braze | Plataforma Braze | Página **Configuración** > **Clave de API** | Esta descripción debería indicarte qué hacer con la clave de API REST or transferencia de estado representacional del espacio de trabajo. |
| Endpoint de API de Braze | Plataforma Braze | Consulta nuestros [endpoints listados]({{site.baseurl}}/api/basics#endpoints) o abre un [ticket de soporte]({{site.baseurl}}/braze_support). | Descripción pendiente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Requisitos o prerrequisitos" }

## Integración de [tipo de integración] {#type-of-integration-integration}

Aquí es donde desglosas la integración en pasos. No escribas párrafos interminables: estos son documentos técnicos que serán utilizados tanto por especialistas en marketing como por desarrolladores para poner en marcha la integración. Tu único objetivo en esta sección es escribir documentación descriptiva que ayude al usuario de Braze a realizar el trabajo. Con "tipo de integración" en el título de la sección, queremos indicar si se trata de una integración en paralelo, de servidor a servidor o predeterminada. Esto te permite tener varias secciones de integración si hay más de una forma de integrarse con este partner.

Si se trata de una integración de Currents, esta página debe ubicarse en la sección de Currents, y se debe crear una página de navegación correspondiente que redirija a esa ubicación en Currents.

### Paso 1: Esta es una breve descripción del paso uno {#step-1-this-is-a-short-description-of-step-one}

Simplemente desglósalo, incluyendo cualquier código que sea necesario. Recuerda que puedes ofrecer varios conjuntos diferentes de código; no es necesario ofrecer solo una forma de integración.

### Paso 2: Este paso describe imágenes {#step-2-this-step-will-describe-images}

Tienes la opción de incluir imágenes en tu documentación, así que te recomendamos que lo hagas y de manera cuidadosa.

### Paso 3: Cuántos pasos {#step-3-how-many-steps}

Describe el uso de la integración, especialmente si implica insertar Liquid en nuestro creador de mensajes.

## Personalización {#customization}

Esta es una sección **opcional**. Aquí puedes describir cualquier forma específica de personalizar tu integración entre los dos partners.

## Uso de esta integración {#using-this-integration}

Esta sección debe describir cómo usar la integración: informa a tu lector si necesita pulsar algunos botones o si no necesita hacer nada en absoluto después de la integración.

### Paso 1: Esta es una breve descripción del paso uno

Solo tu típico procedimiento paso a paso.

## Ejemplos {#use-cases}

Esta puede ser una parte fundamental de tu documentación. Aunque es opcional, es un buen lugar para describir ejemplos típicos o incluso novedosos de la integración. Puede utilizarse como una forma de vender o potenciar la relación: proporciona contexto, ideas y, sobre todo, una manera de visualizar las capacidades de la integración.