---
nav_title: Judo
article_title: Judo
description: "Este artículo de referencia describe la asociación entre Braze y Judo, una plataforma de interfaz de usuario sin código basada en servidor que te permite añadir contexto y seguimiento de ubicación a tus aplicaciones para iOS y Android."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) es una plataforma de interfaz de usuario basada en servidor que permite a los editores ofrecer experiencias de usuario enriquecidas y atractivas dentro de la aplicación sin necesidad de actualizarla.

_Esta integración la mantiene Judo._

## Sobre la integración {#about-the-integration}

La integración de Braze y Judo proporciona experiencias a medida en tus Campaigns y Canvas. En lugar de una experiencia de página de destino sencilla y con plantillas, una Campaign de Braze puede incorporar contenido que incluya varias pantallas, modales, video, fuentes personalizadas y ajustes de compatibilidad, como el modo oscuro y la accesibilidad, creados sin código y desplegados sin actualizaciones de la aplicación. Los datos de Braze también pueden utilizarse para apoyar el contenido personalizado en una experiencia Judo. Los eventos del usuario y los datos de la experiencia pueden retroalimentarse a Braze para la atribución y la segmentación.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Judo | Se necesita una cuenta de [Judo](https://www.judo.app/) para beneficiarse de esta asociación. |
| Judo SDK or kit de desarrollo de software | El SDK or kit de desarrollo de software de Judo debe integrarse en tus aplicaciones [iOS](https://github.com/judoapp/judo-ios/) y/o [Android](https://github.com/judoapp/judo-android). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

**Incorporación**: Los editores de aplicaciones que utilizan Judo construyen y despliegan experiencias de incorporación nativas y enriquecidas. Estas experiencias pueden ser ahora uno de los elementos de un proceso de incorporación de canales cruzados personalizado coordinado a través de Braze. Las experiencias pueden personalizarse y actualizarse rápidamente sin necesidad de actualizar la aplicación para probar la eficacia de diferentes flujos dentro de la aplicación.

**Conversión**: Los editores de aplicaciones pueden utilizar los datos de Braze para crear una experiencia rica y personalizada dentro de la aplicación para impulsar las compras dentro de la aplicación, las suscripciones de pago o la comercialización contextual utilizando los ganchos de integración en Judo. El acceso a estas experiencias puede activarse a través de Campaigns de marketing de interacción creadas en Braze.

**Contenido basado en eventos**: Un uso principal de Judo en deportes y entretenimiento es la creación de experiencias enriquecedoras que sirvan de vista previa, promoción y recapitulación de eventos. Esta capacidad tiene amplias aplicaciones en otros verticales para contenidos estacionales y basados en noticias. Vincular mensajes para promocionar o destacar eventos de manera oportuna con experiencias enriquecidas dentro de la aplicación permite a los editores impulsar la interacción siendo contextualmente relevantes.

## Integración de SDK or kit de desarrollo de software en paralelo {#side-by-side-sdk-integration}

Judo ofrece bibliotecas adicionales que automatizan parte del esfuerzo necesario para integrar los SDK or kit de desarrollo de software de Judo y Braze en paralelo en tus aplicaciones móviles.

### Paso 1: Instalar la biblioteca de integración Judo-Braze {#step-1-install-the-judo-braze-integration-library}

Instala y configura la biblioteca de integración Judo-Braze en tus aplicaciones. Esto activará automáticamente el seguimiento de eventos.

- [Instrucciones de instalación en
iOS](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Instrucciones de instalación en
Android](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Paso 2: Configurar la mensajería dentro de la aplicación {#step-2-configure-in-app-messaging}

Este paso consistirá en crear implementaciones personalizadas de `ABKInAppMessageControllerDelegate` y `IInAppMessageManagerListener` para iOS y Android.

Consulta la documentación de configuración de mensajes dentro de la aplicación incluida en cada una de las bibliotecas de integración:

- [Configuración de mensajería dentro de la aplicación en
iOS](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Configuración de mensajería dentro de la aplicación en
Android](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Uso de esta integración {#using-this-integration}

Una vez finalizada la integración del lado de la aplicación, puedes probarla ejecutando una Campaign de mensajes dentro de la aplicación de Braze de prueba para una experiencia Judo a fin de verificar que funciona como se espera.

### Paso 1: Crear una Campaign de mensaje dentro de la aplicación de código personalizado {#step-1-create-a-custom-code-in-app-message-campaign}

Desde la plataforma Braze, crea una Campaign de mensaje dentro de la aplicación de Braze con un tipo de mensaje **Custom Code**. A continuación, selecciona **HTML Upload** como tipo personalizado. Asegúrate de rellenar el contenido del mensaje con los campos básicos de mensajería dentro de la aplicación; este contenido no se mostrará al usuario.

![Una imagen del aspecto del dashboard cuando se selecciona el tipo de mensaje "Custom Code".]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

A continuación, utiliza el siguiente fragmento HTML mínimo para satisfacer la validación del formulario:
```
<a href="appboy://close">X</a>
```

Ten en cuenta que esto no se mostrará en producción en tu dispositivo, ya que Judo reescribirá y reemplazará esto con una experiencia Judo.

![Una imagen que muestra el código de validación del formulario añadido al paso de redacción de tu Campaign.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Paso 2: Establecer un par clave-valor para Judo {#step-2-set-a-key-value-pair-for-judo}
![Esta imagen muestra el par clave-valor necesario para esta integración, siendo la "clave" "judo-experience" y el "valor" tu enlace de Judo.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Establece un [par clave-valor personalizado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/) en la Campaign con una clave de `judo-experience`. Proporciona la URL de la experiencia Judo que deseas mostrar aquí. La biblioteca de integración Judo-Braze detectará este par clave-valor en el controlador y lo utilizará para inyectar tu experiencia Judo en lugar de la interfaz de mensajes estándar dentro de la aplicación de Braze.
<br><br>
### Paso 3: Finalización de la Campaign {#step-3-finishing-the-campaign}

Por último, completa la Campaign, configurando un desencadenante para la Campaign y seleccionando usuarios a través de Segments en las secciones **Delivery** y **Target User**. Visita nuestro [artículo]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) sobre mensajes dentro de la aplicación para conocer los distintos componentes de un mensaje dentro de la aplicación de Braze.