---
nav_title: Komo
article_title: Komo
description: "Este artículo de referencia describe la asociación entre Braze y Komo, una plataforma de interacción con los clientes especializada en gamificación, contenido interactivo, concursos, premios y fidelización. A través de esta integración, los datos propios y de zero-party data capturados en Komo pueden publicarse en Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) es una plataforma de interacción con los clientes especializada en gamificación, contenidos interactivos, concursos, premios y fidelización.

_Esta integración está mantenida por Komo._

## Acerca de la integración {#about-the-integration}

La integración de Braze y Komo te permite recopilar datos first-party y zero-party data a través de los Komo Engagement Hubs. Estos hubs son micrositios dinámicos que ofrecen contenido interactivo y características de gamificación. Los datos de usuario recopilados de estos hubs se transmiten luego a la API de Braze.

{% multi_lang_include partners/extensions/landing_pages/komo_integration_bullets.md %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Komo | Necesitarás una cuenta activa de Komo para aprovechar esta integración. Visita [Komo](https://komo.tech/) para iniciar una prueba ahora. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos de `users.track`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze | [La URL de tu endpoint REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Tu endpoint dependerá de la URL de Braze de tu instancia.<br><br>Por ejemplo, debería verse algo como: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

{% tabs local %}
{% tab Captura de datos - Envío de formulario %}

Cuando un usuario envía un formulario de captura de datos personalizable en Komo, los campos de Komo mapeados en la integración de Braze se pasan a Braze a través de la llamada a la API `/users/track/`.

Los formularios de captura de datos existen al inicio o al final de las tarjetas.

{% endtab %}
{% tab Investigación de mercado - Próximamente %}

Komo también permite pasar datos de investigación de mercado capturados cuando un usuario responde una pregunta de cuestionario, encuesta, test de personalidad, swiper y similares. Estos datos te permitirán enriquecer el perfil de un usuario más allá de los datos capturados en los envíos de formularios.

{% endtab %}
{% endtabs %}

## Integración {#integration}

### Paso 1: Publicar un Komo Engagement Hub y una tarjeta {#step-1-publish-a-komo-engagement-hub-and-card}

Necesitarás publicar un Komo Hub con al menos una tarjeta que contenga un formulario de captura de datos. Una vez publicado, puedes probar la experiencia del usuario de extremo a extremo y verificar que la integración funciona correctamente.

![Komo Hub.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Paso 2: Añadir la aplicación conectada de Braze {#step-2-add-the-braze-connected-app}

En Komo, ve a la pestaña **Company Settings** y selecciona la sección **Connected Apps**.

A continuación, busca la integración de Braze en la lista y selecciona el botón **Connect** para habilitar la integración.

![Conectar la integración de Braze.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Conectar la integración de Braze, paso 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Configurar la integración mediante un flujo de trabajo {#configure-the-integration-via-a-workflow}

Ahora necesitas configurar un flujo de trabajo, dentro de un espacio de trabajo, sitio o tarjeta, para sincronizar datos con Braze.

Si defines el alcance del flujo de trabajo a nivel de todo el espacio de trabajo, de un sitio (que contiene muchas tarjetas) o de una sola tarjeta, dependerá de si quieres que el flujo de trabajo se active en varias tarjetas o Campaigns.

Después de crear un flujo de trabajo, define tu desencadenador, busca Braze en el menú de pasos y añade el paso "Track User".

![Configuración de Track User.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

Desde aquí, configura los eventos, las atribuciones y las suscripciones que quieres sincronizar de Komo a Braze.

![Lista de Content Blocks.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Uso de la integración {#using-the-integration}

Ahora tu integración está en funcionamiento y puedes monitorear cada ejecución en la pestaña Workflow Runs.