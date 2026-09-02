---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Este artículo de referencia describe la asociación entre Braze y Bluedot, una plataforma de ubicación que proporciona una plataforma de geovallado precisa y sencilla para tus aplicaciones."
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/) es una plataforma de ubicación que proporciona una plataforma de geovallado precisa y sencilla para tus aplicaciones. Usa el SDK or kit de desarrollo de software de Bluedot para enviar mensajes de forma más inteligente, automatizar el registro de pedidos móviles, optimizar los flujos de trabajo y crear experiencias sin fricciones.

_Esta integración está mantenida por Bluedot._

## Sobre la integración {#about-the-integration}

La integración de Braze y Bluedot te permite usar los servicios de ubicación de geovallas de Bluedot para crear eventos de usuario que se pueden utilizar para construir recorridos, campañas y analizar los comportamientos e intereses de los clientes. Los eventos (entrada/salida) generados por el usuario en su dispositivo se envían inmediatamente a Braze con toda la información relevante.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Bluedot | Se requiere una cuenta Bluedot para aprovechar esta integración. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

La información de ubicación de eventos personalizados proporcionada por Bluedot puede utilizarse en tus campañas para lograr casos de uso comunes como:
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (restaurante de servicio rápido)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/)

## Integración {#integration}

### Paso 1: Crear un proyecto Bluedot {#step-1-create-a-bluedot-project}
Configura tu cuenta de Bluedot e inicia sesión en tu [dashboard de Bluedot Canvas](https://docs.bluedot.io/canvas/). Visita la [documentación de Bluedot](https://docs.bluedot.io/canvas/creating-a-new-project/) para saber cómo crear un nuevo proyecto.

### Paso 2: Integrar los SDK or kit de desarrollo de software {#step-2-integrate-the-sdks}
Integra el SDK or kit de desarrollo de software de Bluedot Point y el SDK or kit de desarrollo de software de Braze en tu aplicación siguiendo los pasos indicados en la documentación de [integración Bluedot-Braze](https://docs.bluedot.io/integrations/braze-integration/).

### Paso 3: Autenticar el SDK or kit de desarrollo de software de Bluedot {#step-3-authenticate-the-bluedot-sdk}
Usa el `projectId` creado en el paso 1 para autenticar el SDK or kit de desarrollo de software de Bluedot Point.

### Paso 4: Usar eventos Bluedot en Braze {#step-4-use-bluedot-events-in-braze}

#### Desencadenar mensajes {#triggering-messages}

Puedes configurar una Campaign push o un Canvas que actúe a partir de eventos de ubicación generados por el SDK or kit de desarrollo de software de Bluedot. Esta ruta de integración es ideal para la mensajería en tiempo real justo cuando los usuarios entran en un local o lugar de interés, o para la comunicación de seguimiento diferida después de que se hayan marchado.

Configura una Campaign basada en acciones dentro de Braze que enviará mensajes basados en una ubicación establecida. Para tu desencadenador, usa un evento personalizado de `bluedot_entry` o `bluedot_exit` como se muestra en la siguiente captura de pantalla:

![Una Campaign basada en acciones en el paso de entrega. Aquí tienes dos opciones de programación que enviarán la Campaign si un usuario realiza un evento personalizado `bluedot_entry` o `bluedot_exit`.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Dirigirse a los usuarios {#targeting-users}

Asegúrate de seleccionar **Todos los usuarios** para tu espacio de trabajo.
![Una Campaign basada en acciones con el paso de usuarios objetivo que te anima a seleccionar "Todos los usuarios" como el segmento deseado.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}