---
nav_title: Wyng
article_title: Wyng
description: "Este artículo de referencia describe la asociación entre Braze y Wyng, una plataforma de zero-party data utilizada para recopilar, utilizar e integrar las preferencias y atributos de los clientes a través de microexperiencias, portales de preferencias de clientes y una plataforma API."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/) proporciona herramientas para crear experiencias digitales interactivas (cuestionarios, centros de preferencias, promociones) que atraen a los consumidores en momentos clave, recopilan preferencias y otros zero-party data, y personalizan en tiempo real.

_Esta integración está mantenida por Wyng._

## Sobre la integración {#about-the-integration}

La integración de Braze y Wyng te permite aprovechar los zero-party data obtenidos a través de las experiencias Wyng para personalizar las interacciones en Braze Campaigns y BRAZE Canvas. Wyng también puede impulsar un centro de preferencias, para que los consumidores puedan controlar los datos y preferencias (incluidas las preferencias de comunicación) que comparten con tu marca.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Wyng | Se necesita una cuenta Wyng para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar la integración de Braze {#step-1-connect-the-braze-integration}

En Wyng, ve a [**Integraciones**](https://wyng.com/dashboard/integrations/) y selecciona la pestaña **Add**. A continuación, sitúate sobre **Braze** y haz clic en **Connect** para la integración.

![El mosaico del socio Braze en la plataforma Wyng.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### Paso 2: Configurar el conector de Braze {#step-2-configure-the-braze-connector}

1. En la ventana de configuración que se abre, proporciona tu clave de API REST or transferencia de estado representacional de Braze.
![Una imagen del aspecto de la solicitud de credenciales.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. A continuación, utiliza el menú desplegable para seleccionar la campaña Wyng que deseas compartir con Braze.![Imagen del conector de Braze que te pide que selecciones una campaña Wyng existente que desees compartir con Braze.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. A continuación, debes configurar las suscripciones, los objetos de atributo y evento, y los eventos personalizados.<br><br>
- **Configuración de suscripciones (obligatorio)**<br>
Para suscribir usuarios a grupos de suscripción, haz clic en **Add Subscription** y añade el nombre y el ID del grupo de suscripción. Para añadir varios nombres e ID de grupo, pulsa de nuevo el botón **Add Subscription**.<br>![Una imagen que te pide el nombre y el ID de un grupo de suscripción.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **Configuración del seguimiento del usuario**<br>
Haz clic en **Add custom property** para añadir pares de atributos y objetos de evento para enviar al punto de conexión `/users/track`. Utilízalo para añadir valores de atributos codificados para cada transacción de datos enviada para la integración. Para añadir varias propiedades, haz clic de nuevo en el botón **Add custom property**.<br>![Una imagen que te pide que añadas propiedades personalizadas de atributos.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Enviar evento personalizado**<br>
Opcionalmente, puedes habilitar **Sending custom event**. Si está habilitado, debes incluir el nombre del evento y el ID de la aplicación correspondiente.<br>![Una imagen que te pide que envíes eventos personalizados, si es necesario.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Por último, debes asignar los campos de Wyng a los campos de la API de Braze en función de tu caso de uso. Haz clic en **Select a field** para elegir los campos que deseas asignar y, a continuación, haz clic en **Save** para guardar la integración. Una vez guardados, estos campos asignados se pueden encontrar en **Integrations > Manage**.
![Un ejemplo de los diferentes campos de Wyng que puedes asignar a determinados campos de Braze.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![Una lista de los campos de sincronización disponibles.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### Paso 3: Prueba tu integración {#step-3-test-your-integration}

En Wyng, prueba a enviar el formulario en tu campaña Wyng. También puedes enviarlo en la campaña de vista previa si no deseas añadir un registro a la campaña de producción principal. Deberías ver una transacción correcta en el dashboard de **Integration**.

## Uso de esta integración {#using-this-integration}

Una vez establecido el conector de datos, los campos creados en Wyng y añadidos a Braze pueden utilizarse como cualquier otro campo de datos para desencadenar Campaigns, segmentar audiencias o alimentar contenidos personalizados.

Las aplicaciones son amplias, y las preguntas específicas pueden dirigirse a [contact@wyng.com](mailto:contact@wyng.com) o a tu director de cuentas específico.

## Solución de problemas {#troubleshooting}

### Envío fallido {#failed-submission}

En el caso de un envío fallido, al enviar datos a Braze, haz clic en el enlace **View Log** para revisar el envío fallido y el mensaje de error asociado.

![El enlace "View Log" que se encuentra bajo el encabezado de acciones.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

La página de registro mostrará el envío fallido, el recuento de reintentos, los datos del envío, el error y un enlace para volver a enviar el envío.

![Un ejemplo de lo que mostrará un envío fallido.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

La sección **View Error** mostrará el código de error y alguna información adicional sobre la causa del error. A continuación, puedes cotejar el código de error con Braze para determinar la causa.

![Un ejemplo de registro de errores mostrado en la plataforma Wyng.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

Si tienes más preguntas, ponte en contacto con el servicio de soporte de Wyng ([support@wyng.com](mailto:contact@wyng.com)) para que te ayuden.