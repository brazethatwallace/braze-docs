---
nav_title: Digioh
article_title: Digioh
description: "Este artículo de referencia describe la asociación entre Braze y Digioh, una plataforma de cuestionarios para crear ventanas emergentes, formularios, cuestionarios y centros de preferencias de comunicación que impulsan la interacción a través de tus Campaigns de Braze."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) apoya el crecimiento de la lista, la captura de datos propios y el uso de esos datos en las Campaigns de Braze.

_Esta integración está mantenida por Digioh._

## Sobre la integración {#about-the-integration}

La integración de Braze y Digioh te permite utilizar un constructor de arrastrar y soltar para crear formularios de marca, ventanas emergentes, centros de preferencias, páginas de destino y cuestionarios que te conecten con tus clientes. Digioh te ayuda a configurar la integración y puede crear, diseñar y lanzar tu primera Campaign.

!["Crea centros de preferencias de correo electrónico y comunicaciones flexibles con Digioh"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Digioh | Se necesita una [cuenta Digioh](https://www.digioh.com/) para aprovechar esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**. |
| Punto de conexión de la API de Braze `/users/track/` | La URL de tu punto de conexión REST con los detalles de `/users/track/` añadidos. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints).<br><br>Por ejemplo, si tu punto de conexión de la REST API es `https://rest.iad-01.braze.com`, tu punto de conexión de `/users/track/` será `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integración {#integration}

Para integrar Digioh, primero debes configurar el conector de Braze. Una vez completado, tendrás que aplicar la integración a un lightbox (widget). Visita [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) para leer más sobre los fundamentos de la integración.

### Paso 1: Crear la integración de Digioh {#step-1-create-digioh-integration}

En Digioh, haz clic en la pestaña **Integrations** y luego en el botón **New Integration**. Selecciona **Braze** en el desplegable **Integration** y dale un nombre a la integración.

!["Selecciona la integración correcta en el desplegable"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

A continuación, introduce la clave de API REST de Braze y tu punto de conexión de la API de Braze `/users/track/`.

Por último, utiliza la sección de mapeado de campos para mapear campos personalizados adicionales más allá del correo electrónico y el nombre. El siguiente fragmento de código muestra un ejemplo de carga útil. Cuando hayas terminado, selecciona **Create Integration**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Paso 2: Crear un lightbox de Digioh {#step-2-create-a-digioh-lightbox}

Utiliza el [editor de diseño](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) de Digioh para crear un lightbox (widget). <br>
¿Te interesa ver una galería de formas de aprovechar el editor de diseño? Visita la [galería de temas](https://www.digioh.com/theme-gallery) de Digioh.

### Paso 3: Aplicar la integración {#step-3-apply-integration}

Para aplicar esta integración a un [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) de Digioh, ve a la página **Boxes** y selecciona el enlace **Add** o **Edit** en la columna **Integrations**. También puede añadirse desde la sección **Integration** del editor.

!["Añadir la integración a un lightbox"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Aquí, selecciona **Add Integration**, elige la integración que desees y **Save**. Digioh pasará ahora tus clientes potenciales captados a Braze en tiempo real.