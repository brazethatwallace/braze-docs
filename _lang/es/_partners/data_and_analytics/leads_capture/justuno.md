---
nav_title: Justuno
article_title: Justuno
description: "Aprende a integrar Justuno con Braze para aprovechar los datos de clientes en ambas plataformas y crear experiencias más personalizadas para todas las audiencias."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) te permite crear experiencias de visita totalmente optimizadas para todas tus audiencias con segmentos dinámicos, ofreciendo la segmentación más avanzada disponible&#8212;todo ello sin afectar a la velocidad del sitio ni aumentar el trabajo de desarrollo. Analiza las tasas de conversión consultando análisis personalizados como el número de perfiles creados, la tasa de retorno de visitantes influenciados y las páginas por sesión para mantener una ventaja de marketing en tu sector. Justuno te permite aumentar los ingresos por visitante, establecer interacciones significativas con los clientes y hacer crecer tu negocio. Optimiza todo el recorrido de la audiencia de extremo a extremo con una plataforma conectada.

## Casos de uso {#use-cases}

Braze permite a cualquier especialista en marketing recopilar cualquier cantidad de datos de cualquier fuente y actuar sobre ellos, para que puedas interactuar de forma creativa con los clientes en tiempo real, en todos los canales y desde una sola plataforma.

La integración de Justuno y Braze te ofrece lo mejor de ambos mundos. Puedes combinar los datos de clientes guardados en Braze con los datos de visitantes y clientes guardados en Justuno y crear experiencias más personalizadas para todas las audiencias. Esto aumenta la eficacia de tus campañas de marketing y la interacción con los clientes.

## Requisitos previos {#prerequisites}

| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con los permisos `users.track` y `custom_attributes.get`.<br><br>Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | La URL de tu punto de conexión REST or transferencia de estado representacional. Tu punto de conexión dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de Justuno con Braze {#integrating-justuno-with-braze}

### Paso 1: Crear atributos personalizados en Braze {#step-1-create-custom-attributes-in-braze}

Para sincronizar los atributos de usuario de Justuno con Braze, tendrás que crear esos atributos en Braze si aún no lo has hecho. Para ello, ve a **Data Settings** > **Custom Attributes** y, a continuación, crea tus atributos personalizados. Para una guía completa, consulta [Gestionar atributos personalizados en Braze]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).

### Paso 2: Añadir la aplicación Braze a Justuno {#step-2-add-the-braze-app-to-justuno}

#### Paso 2.1: Añádela a tu cuenta {#step-21-add-it-to-your-account}

Para añadir la aplicación Braze a tu cuenta de Justuno, ve a **Account Settings** > **Apps** y, a continuación, busca y selecciona la aplicación Braze.

![La página "Connect Apps" en Justuno con la aplicación Braze mostrada en la lista de resultados de búsqueda.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Introduce la clave de API y la URL base [que creaste anteriormente](#prerequisites) y, a continuación, selecciona **Connect**.

![La ventana emergente de autenticación de Braze que solicita una clave de API de Braze y una URL base.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Paso 2.2: Añádela a tu flujo de trabajo {#step-22-add-it-to-your-workflow}

Para añadir la aplicación Braze a tu [flujo de trabajo de Justuno](https://hub.justuno.com/knowledge/workflows-overview), arrastra y suelta la acción **Sync to App** en tu flujo de trabajo, y luego elige **Select App** > **Braze**.

![La opción "Select App" situada en la acción "Sync to App".]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Paso 3: Conectar tus grupos de suscripción de Braze {#step-3-connect-your-braze-subscription-groups}

Para enviar datos de perfil desde Justuno a un grupo de suscripción de correo electrónico o servicio de mensajes cortos de Braze específico, tendrás que añadir su ID a la aplicación Braze en tu flujo de trabajo de Justuno.

| Tipo de ID                          | ¿Obligatorio? | Descripción                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| ID de grupo de suscripción servicio de mensajes cortos de Braze  | Sí       | Este ID se utiliza para recoger el consentimiento de servicio de mensajes cortos de los perfiles de usuario. Si no se introduce ningún ID en Justuno, los perfiles no tendrán consentimiento cuando Justuno envíe ese perfil a Braze. |
| ID de grupo de suscripción de correo electrónico de Braze | No        | Si no se introduce este ID en Justuno, Justuno enviará los datos de perfil a Braze como un usuario sin grupos de suscripción asociados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 3: Conectar tus grupos de suscripción de Braze" }

#### Paso 3.1: Localizar los ID en Braze {#step-31-locate-the-ids-in-braze}

Para localizar estos ID en el panel de Braze:

1. Ve a **Audience** > **Subscriptions**.
2. Para cada grupo de suscripción, anota el ID situado en la columna ID.

#### Paso 3.2: Añadir los ID a la aplicación Braze {#step-32-add-the-ids-to-the-braze-app}

En tu flujo de trabajo de Justuno, abre la aplicación Braze e introduce los ID de cada grupo de suscripción.

![La aplicación Braze abierta en un flujo de trabajo de Justuno con la opción de añadir ID de grupo de suscripción de correo electrónico y SMS.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Paso 4: Configurar tus atributos {#step-4-configure-your-attributes}

Los siguientes atributos se sincronizan automáticamente desde Justuno a Braze:

- Correo electrónico
- Teléfono
- Nombre
- Apellido
- Idioma
- Género
- País

Para sincronizar atributos adicionales:

1. En la aplicación Braze dentro de tu flujo de trabajo, selecciona **Sync Another Property**.
    ![La aplicación Braze abierta en un flujo de trabajo de Justuno mostrando la opción "Sync Another Property".]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Elige qué atributos de Braze quieres sincronizar.
3. Haz coincidir las propiedades en Justuno con sus equivalentes en Braze (como identificadores sociales, cumpleaños, preferencias de compra, respuestas a cuestionarios y similares). Ten en cuenta que estas propiedades se consideran datos de parte cero o datos de primera parte. Para saber más, consulta [Justuno: Recopilación de datos de visitantes](https://www.justuno.com/guides/zero-first-party-data/).
4. En el constructor de flujos de trabajo, elige **Save**, **vista previa** o **Publish** para tu flujo de trabajo.
    ![El menú "Publish" abierto con las opciones de guardar, vista previa o mostrar el historial de versiones.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Lo que debes saber {#things-to-know}

- Debes introducir manualmente el ID del grupo de suscripción en la configuración de la aplicación.
- Los siguientes tipos de datos de Braze **no son compatibles**: Object, Object Array.
- El consentimiento implícito de servicio de mensajes cortos se proporciona cuando no se utiliza el campo de consentimiento de servicio de mensajes cortos de Justuno.
- El consentimiento explícito de servicio de mensajes cortos se respeta si el diseño de Justuno incluye el campo de consentimiento.