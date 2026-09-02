---
nav_title: Zeotap
description: "Este artículo de referencia describe la asociación entre Braze y Zeotap, una CDP or plataforma de datos de los clientes or plataforma de datos de los clientes de nueva generación que proporciona resolución de identidades, información y enriquecimiento."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) es una CDP or plataforma de datos de los clientes or plataforma de datos de los clientes de nueva generación que te ayuda a descubrir y comprender a tu audiencia móvil proporcionando resolución de identidades, información y enriquecimiento de datos.

Con la integración de Zeotap y Braze, puedes ampliar la escala y el alcance de tus campañas sincronizando los segmentos de clientes de Zeotap para asignar los datos de usuario a las cuentas de usuario de Braze. Después, puedes actuar en función de estos datos y ofrecer experiencias personalizadas a tus usuarios.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta Zeotap | Se necesita una [cuenta Zeotap](https://zeotap.com/) para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. <br><br> Se puede crear en el panel de Braze desde **Settings** > **API Keys**. |
| Endpoint REST de Braze | La URL de tu endpoint REST. Tu endpoint dependerá de la [URL de Braze para tu instancia]({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear un destino Zeotap {#step-1-create-a-zeotap-destination}

1. Desde la plataforma Zeotap Unity, navega hasta la aplicación **DESTINATIONS**.
2. En **All Channels**, selecciona **Braze**.
3. En el mensaje que aparece, asigna un nombre a tu destino e indica tu nombre de cliente y la clave de API REST or transferencia de estado representacional de Braze asociada a tu cuenta de Braze.
4. Por último, selecciona tu instancia de endpoint REST de Braze en el menú desplegable y guarda el destino. <br><br>![Configuración del destino Zeotap Braze con el menú desplegable de instancia de endpoint.]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Paso 2: Crea y vincula un segmento Zeotap a tu destino {#step-2-create-and-link-a-zeotap-segment-to-your-destination}

1. Desde la plataforma Zeotap Unity, navega hasta la aplicación **CONNECT**.
2. Crea un segmento y selecciona el destino Braze creado en el paso 1.
3. Selecciona un identificador de salida compatible: MAID, dirección de correo electrónico con hash SHA256 o cualquier identificador de cliente 1P reconocido por Braze (si deseas utilizar un identificador personalizado para tu cuenta de Braze, ponte en contacto con Zeotap para que se habilite en tu cuenta). Solo se puede utilizar un identificador de salida para la integración con Braze. Estos identificadores deben ser los mismos que el ID externo establecido al recopilar los datos del SDK or kit de desarrollo de software de Braze.
4. Guarda el segmento.

![Configuración de segmento en Zeotap CONNECT vinculado al destino Braze.]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Los identificadores que aparecen están disponibles en el segmento y son compatibles con Braze.
{% endalert %}

### Paso 3: Crear un segmento en Braze {#step-3-create-braze-segment}

Tras crear, enviar y procesar correctamente un segmento en Zeotap, los usuarios de Zeotap aparecerán en el panel de Braze. Puedes buscar usuarios por ID de usuario en el panel de Braze.

![Un perfil de usuario de Braze que muestra los segmentos del uno al cuatro como "true" en "Custom attributes".]({% image_buster /assets/img/zeotap/zeotap4.png %})

Si un usuario forma parte del segmento de Zeotap, el nombre del segmento aparece como atributo personalizado en su perfil de usuario con el valor booleano `true`. Toma nota del nombre del atributo personalizado, ya que lo necesitarás al crear un segmento en Braze.

A continuación, debes crear y definir este segmento en Braze:
1. En el panel de Braze, selecciona **Segments** y luego **Create Segment**.
2. A continuación, asigna un nombre a tu segmento y selecciona el segmento de atributos personalizados creado en Zeotap.
3. Guarda los cambios.

![En el constructor de segmentos de Braze, puedes encontrar los segmentos importados establecidos como atributos personalizados.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Ahora puedes añadir este segmento recién creado a futuras Campaigns y Canvas de Braze para dirigirte a estos usuarios finales.