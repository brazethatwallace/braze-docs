---
nav_title: Extole
article_title: Extole
description: "Este artículo describe la asociación entre Braze y Extole, una empresa de marketing de referidos, que permite extraer eventos y atributos de los clientes de los programas de recomendación a un amigo y de crecimiento en Braze."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole](https://www.extole.com/), una empresa de software como servicio (SaaS), es líder en el sector del marketing de recomendación a amigos y ayuda a crear y optimizar programas eficaces de marketing de referidos para aumentar la captación de clientes.

_Esta integración está mantenida por Extole._

## Sobre la integración {#about-the-integration}

Con la integración de Braze y Extole, puedes extraer eventos y atributos de clientes de los programas de crecimiento y de recomendación de amigos de Extole a Braze, lo que te permite crear campañas de marketing más personalizadas que impulsan la captación, la participación y la fidelización de los clientes. También puedes incorporar dinámicamente atributos de contenido de Extole, como códigos de compartición y enlaces personalizados, a las comunicaciones de Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Extole | Se necesita una cuenta de Extole para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con el permiso `users.track`. Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| URL de la API de Braze | La URL de la API de Braze es específica de tu [instancia de Braze]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Los siguientes casos de uso muestran algunas formas de utilizar la integración de Extole con Braze. Trabaja con tus administradores de implementación y de éxito del cliente de Extole para desarrollar una opción que se adapte a las necesidades específicas de tu empresa.

- Usa eventos personalizados de tus programas de referidos y participación para desencadenar una Campaign o Canvas de Braze
- Crea segmentos personalizados, paneles e informes utilizando los datos de tus programas impulsados por Extole
- Cancela la suscripción o suscribe usuarios automáticamente a tu lista de marketing en Braze

## Integración {#integration}

Completa los siguientes pasos para poner en marcha rápidamente tu integración. Tus administradores de éxito del cliente y de implementación de Extole te ayudarán en este proceso y responderán a cualquier pregunta que puedas tener.

### Conéctate a tu cuenta Braze {#connect-to-your-braze-account}

1. Selecciona la integración Braze en la página [Partners](https://my.extole.com/partners) de tu cuenta My Extole.
2. En la integración Braze, selecciona **Install** para iniciar la conexión entre Extole y Braze.
3. Rellena los campos obligatorios, empezando por tu clave de API REST de Braze.
4. Introduce la URL de tu API de Braze. Esta URL depende de la instancia en la que esté aprovisionada tu cuenta Braze.
5. Añade los eventos de Extole que quieras enviar a Braze. Los eventos predeterminados, las propiedades de los eventos y los atributos de usuario se describen en la [tabla de eventos de Extole](https://dev.extole.com/docs/braze#extole-program-events).
6. Añade los estados de recompensa que quieras enviar a Braze, aparte del estado `FULFILLED`. Consulta la [tabla de recompensas de Extole](https://dev.extole.com/docs/braze#extole-rewards) para ver las descripciones de los estados de recompensa disponibles.
7. Selecciona tu mapeado de clave de ID externo de Braze. Así es como Extole actualiza los perfiles de los usuarios en Braze. Puedes asignar la clave de ID externo de Braze a `email_address` o `partner_user_id` de Extole para el usuario. Recomendamos utilizar `external_id` en lugar de `email_address`, ya que es más seguro.
8. Guarda la configuración para completar la conexión. Ahora, los eventos de Extole pueden fluir a tu cuenta Braze.

### Eventos del programa Extole {#extole-program-events}

A continuación se muestran los eventos predeterminados, las propiedades de los eventos y los atributos de usuario que Extole enviará a Braze. Ponte en contacto con tus administradores de implementación o de éxito del cliente de Extole para identificar y añadir eventos adicionales de Extole a tu integración.

| Evento | Descripción | Propiedades del evento | Atributos del usuario |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Un participante crea su enlace para compartir introduciendo su correo electrónico en Extole Share Experience. | Nombre de evento  <br>Hora del evento  <br>Partner (Extole)  <br>Embudo (defensor o amigo)  <br>Programa | <br>ID externo <br>Correo electrónico  <br>Enlace para compartir |
| `extole_shared` | Un participante comparte su enlace de recomendación con un amigo. | Nombre de evento  <br>Hora del evento  <br>Partner (Extole)  <br>ID externo  <br>Embudo (defensor o amigo)  <br>Programa  <br>Canal para compartir | Correo electrónico <br>Nombre <br>Apellido |
| `outcome` - El resultado es dinámico en función de la configuración de tu programa (como `extole_shipped`, `extole_converted`) | Un participante ha convertido o completado el evento de resultado deseado configurado para el programa. | Dinámicas por programa | Correo electrónico <br>Nombre <br>Apellido |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eventos del programa Extole" }

### Estados de suscripción de Extole {#extole-subscription-states}

| Estado de suscripción | Descripción | Propiedades del evento | Atributos del usuario |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Un participante ha optado por recibir mensajes de marketing. | N/A | Correo electrónico  <br>Tipo de lista  <br>ID externo  <br>Suscripción por correo electrónico (adhesión voluntaria) |
| `unsubscribed` | Un participante ha optado por no recibir comunicaciones por correo electrónico de Extole. | Correo electrónico  <br>ID externo  <br>Estado de la suscripción (cancelada)  <br>ID del grupo de suscripción  | Tipo de lista |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Estados de suscripción de Extole" }

### Recompensas de Extole {#extole-rewards}

Por defecto, Extole enviará los eventos de recompensa en el estado `FULFILLED` a Braze para que puedas desencadenar notificaciones de recompensa a través de una Campaign o Canvas de Braze. Consulta la tabla siguiente para conocer otros estados de recompensa.

| Estado de la recompensa | Descripción | Propiedades del evento | Atributos del usuario |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | El estado predeterminado. Un proveedor de recompensas de Extole ha asignado un valor a la recompensa (como un cupón o una tarjeta regalo). | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `EARNED` | Se ha creado una recompensa y se ha asociado a una persona. | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `SENT` | La recompensa se ha cumplido y se ha enviado por correo electrónico o a través de un dispositivo al destinatario. | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `REDEEMED` | La recompensa ha sido utilizada por el destinatario, como lo demuestra un evento de conversión o canje enviado a Extole. | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `FAILED` | Un problema ha impedido que se emita o envíe la recompensa, lo que requiere atención. | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `CANCELED` | La recompensa se ha desactivado y volverá al inventario. | Correo electrónico <br>Valor nominal  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `REVOKED` | La recompensa cumplida ha sido invalidada. Por ejemplo, Extole solicitó una tarjeta regalo de un proveedor y luego determinó que la tarjeta se había enviado por error. Si el proveedor admite la revocación de la recompensa, Extole solicitará la devolución de los fondos y la recompensa dejará de ser válida. | Correo electrónico <br>Valor nominal   <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Recompensas de Extole" }


## Personalización {#customization}

### Buscar y crear usuarios en Braze {#find-and-create-users-in-braze}

Para determinados casos de uso, como una nueva suscripción por correo electrónico o SMS en la que Extole no dispone de un ID externo (ID de usuario), Extole puede comprobar el identificador del usuario mediante el [endpoint Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) de Braze. Extole añadirá y actualizará los atributos del perfil si el usuario existe en Braze. Si la solicitud no devuelve un perfil de usuario, Extole utilizará el endpoint `/users/track` para crear un alias de usuario con la dirección de correo electrónico del usuario como nombre del alias.

## Uso de esta integración {#using-this-integration}

Tras conectar tus cuentas, los eventos comenzarán a fluir automáticamente de Extole a Braze sin ninguna acción por tu parte. Puedes ver en vivo los eventos que se envían a Braze en el centro de webhooks salientes de Extole para la solución de problemas.