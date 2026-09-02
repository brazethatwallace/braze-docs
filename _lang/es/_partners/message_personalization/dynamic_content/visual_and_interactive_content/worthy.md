---
nav_title: Worthy
article_title: Worthy
description: "Este artículo de referencia describe la asociación entre Braze y Worthy, una plataforma de personalización de mensajes que te permite crear experiencias ricas y personalizadas dentro de la aplicación y entregarlas a través de Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> La integración de [Worthy](https://worthy.ai/) y Braze te permite crear experiencias ricas y personalizadas dentro de la aplicación utilizando el editor de arrastrar y soltar de Worthy y entregarlas a través de Braze. Además, Worthy hace automáticamente lo siguiente:

_Esta integración está mantenida por Worthy._

## Sobre la integración {#about-the-integration}

- Crea un servidor de contenido conectado y una API segura para tu mensajería.
- Construye tus mensajes dentro de la aplicación con análisis y seguimiento de clics que aparecerán directamente en Braze.
- Exporta automáticamente HTML a través del editor de arrastrar y soltar de Worthy para utilizarlo en campañas de mensajes dentro de la aplicación con **Custom Code** en Braze, junto con las conexiones API necesarias y el contenido dinámico que configures.

## Casos de uso {#use-cases}

- Experiencias de bienvenida personalizadas basadas en las selecciones de incorporación del usuario
- Experiencias dentro de la aplicación para eventos especiales y promociones
- Recopilación de opiniones y valoraciones de los clientes basadas en el comportamiento de la aplicación
- Probar rápidamente posibles ideas de productos de aplicaciones
- Avisos enriquecidos, noticias y actualizaciones de la comunidad

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta [Worthy](https://worthy.ai/) | Se requiere una cuenta Worthy para beneficiarse de esta asociación. |
| SDK or kit de desarrollo de software de Braze | Tendrás que configurar el SDK or kit de desarrollo de software de Braze en tu aplicación móvil para enviar mensajes enriquecidos dentro de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear mensajes personalizados en Worthy {#step-1-create-personalized-messaging-in-worthy}

Ve a tu aplicación en el dashboard de Worthy, selecciona **Message Creator** y crea un mensaje personalizado que quieras utilizar para interactuar con tus usuarios.

### Paso 2: Crear una campaña en Braze {#step-2-create-a-braze-campaign}

Crea una [campaña de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) en Braze y establece **Message Type** en **Custom Code**.

### Paso 3: Copia tu mensaje personalizado en Braze {#step-3-copy-your-personalized-message-into-braze}

En el creador de mensajes de Worthy, haz clic en **Export** y selecciona **Braze** para exportar tu mensaje personalizado y utilizarlo en campañas de Braze. Copia el contenido exportado en el cuadro de texto HTML en **HTML + Asset Zip** en el editor de campañas de Braze.

¡Eso es todo! Puedes probar inmediatamente tu mensaje personalizado utilizando la pestaña **Test** del editor de campañas de Braze.