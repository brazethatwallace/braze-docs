---
nav_title: Storyly
article_title: Storyly
description: "Este artículo de referencia describe la asociación entre Braze y Storyly, un SDK or kit de desarrollo de software ligero, que permite a los propietarios de aplicaciones orientar sus segmentos y alimentar Braze con más datos propios."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) es un SDK or kit de desarrollo de software ligero que lleva historias a tu aplicación o sitio web. Con un estudio de diseño intuitivo, análisis detallados y una conectividad perfecta, Storyly es una potente herramienta para enriquecer la experiencia de la audiencia.

_Esta integración está mantenida por Storyly._

## Sobre la integración {#about-the-integration}

La integración de Braze y Storyly te permite utilizar tus segmentos en Braze como audiencia en la plataforma Storyly. Con esta integración, puedes:
- Dirigirte a tus segmentos con historias específicas
- Utilizar los atributos del usuario para personalizar el contenido de tus historias

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Storyly | Se necesita una cuenta de Storyly para beneficiarse de esta asociación. |
| SDK or kit de desarrollo de software de Storyly | Debes instalar el [SDK or kit de desarrollo de software de Storyly](https://integration.storyly.io/). |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con los siguientes permisos: <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Puede crearse en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Con la integración de Braze y Storyly, los propietarios de aplicaciones pueden mostrar historias a todos los segmentos en Braze y personalizar las historias con atributos de usuario.

Algunos casos de uso comunes son:

__Segmentos objetivo de Braze en Storyly__<br>Una vez finalizada la integración, puedes crear una audiencia de Storyly basada en tus segmentos de Braze. Puede tratarse de un segmento demográfico o de comportamiento. Por ejemplo, dirígete a los usuarios que viven en una ubicación concreta, a los que realizan una acción específica en tu aplicación o a los interesados en productos concretos con historias específicas para aumentar la conversión.<br>
__Historias personalizadas con atributos de usuario__<br>Los atributos de usuario de Braze también se pueden utilizar en Storyly para generar historias dinámicas. Esto podría incluir el nombre de un usuario, los productos de una cesta o incluso los productos favoritos, proporcionando a los usuarios historias personalizadas únicas. La personalización ayuda a aumentar las tasas de conversión de las historias y la tasa de interacción general.

## Integración de exportación de datos {#data-export-integration}

La integración de Braze y Storyly se explica en el siguiente video:

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Asegúrate de que tu integración con Storyly contiene parámetros personalizados. Estos parámetros coincidirán con la propiedad de usuario `external id` de Braze. La implementación de parámetros personalizados se explica aquí para [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) y [Web](https://integration.storyly.io/web/personalization-customaudience.html).

También puedes consultar la documentación de [Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) para obtener más información.

### Paso 1: Configura la integración en el panel de Storyly {#step-1-set-the-integration-on-storyly-dashboard}

Crea una integración en **Storyly Dashboard > Settings > Integrations > Connect with Braze**. Aquí necesitarás tu clave de API REST or transferencia de estado representacional de Braze y tu punto de conexión REST or transferencia de estado representacional de Braze.

### Paso 2: Obtén tus segmentos {#step-2-get-your-segments}

A continuación, puedes utilizar segmentos de Braze para crear una audiencia de Storyly. Se puede crear en **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze**.

Aquí habrá dos opciones de sincronización. Selecciona **One-time sync** para historias de Campaign específicas, o **Daily Sync** para historias de larga duración.