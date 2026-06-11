---
nav_title: "Configuración de RCS"
article_title: "Configuración de RCS"
page_order: 1
alias: /rcs_setup/
description: "Este artículo de referencia cubre los requisitos necesarios para poner en marcha RCS."
page_type: reference
channel:
  - RCS
---

# Configurar RCS {#set-up-rcs}

> Este artículo cubre los requisitos necesarios para poner en marcha tu canal RCS.

Configurar RCS es tan sencillo como configurar SMS. Sigue leyendo para aprender cómo puedes empezar a enviar mensajes enriquecidos e interactivos.

## Paso 1: Cumplir los criterios de elegibilidad {#step-1-meet-the-eligibility-criteria}

Para ser elegible para enviar RCS con Braze, tu empresa debe cumplir tres criterios de antemano:

1. Tu contrato actual de Braze debe incluir créditos de mensajes o de acciones.
2. Debes enviar tus mensajes RCS a uno de los siguientes países compatibles con Braze:
- Estados Unidos
- Reino Unido
- Alemania
- México
- Suecia
- España
- Singapur
- Brasil
- Francia
- Italia
- Colombia
3. Debes adquirir uno o más SKU de RCS en tu contrato.

## Paso 2: Registrar un remitente verificado de RCS {#step-2-register-an-rcs-verified-sender}

Antes de poder enviar mensajes RCS, debes registrar un remitente verificado de RCS. Esta es la representación de tu marca que los usuarios verán en sus dispositivos móviles, que incluye el nombre de tu marca, el logotipo, una señal de verificación y un eslogan opcional. El remitente verificado de RCS refuerza la confianza del cliente y confirma que tus mensajes provienen de una fuente autenticada.

![Un ejemplo de remitente verificado de RCS en un mensaje RCS llamado "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Después de que hayas añadido el o los SKU de RCS a tu formulario de pedido, Braze será notificado y se pondrá en contacto contigo con la información de registro del remitente RCS. El formato de estos dependerá de los países a los que desees enviar mensajes RCS.

Cuando hayas enviado tus formularios completados a Braze, completaremos el proceso de registro en tu nombre.

### Paso 2.1: Configurar alternativas de SMS para los grupos de suscripción de RCS {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Dado que la cobertura actual de los operadores varía según el país, y el hardware y software de los usuarios varían según el individuo, la alternativa de SMS es un componente clave para tener un programa de RCS exitoso hoy en día. Recomendamos configurar la alternativa de SMS. Si un operador no es compatible con RCS o el dispositivo de un usuario no puede recibir mensajes RCS, la alternativa de SMS enviará tu mensaje de todos modos, para que nunca pierdas un momento importante con tus usuarios.

Recomendamos encarecidamente revisar tu experiencia actual de adhesión voluntaria a SMS, los grupos de suscripción y la segmentación de audiencia antes de desplegar tu primera campaña de RCS. Si es necesario, tu administrador del éxito del cliente siempre está disponible para brindarte orientación y ayudarte a navegar el proceso de configuración.

### Plazo para la aprobación del operador {#timeline-for-carrier-approval}

El plazo para la aprobación del operador varía según el país y también puede variar dentro de un mismo país. Ten en cuenta que el mercado de RCS aún está en sus inicios, por lo que los procesos de los operadores y agregadores están evolucionando rápidamente. En Estados Unidos, Braze estima que el tiempo de respuesta para la aprobación del operador de un remitente verificado de RCS generalmente se encuentra en el rango de 4 a 6 semanas, con un remitente de prueba generalmente aprobado en una semana.

Cuando tu remitente verificado de RCS sea aprobado, nuestro equipo de operaciones actualizará tus grupos de suscripción según sea necesario para confirmar que incluyen el remitente RCS.

## Paso 3: Configurar los grupos de suscripción {#step-3-set-up-subscription-groups}

Dependiendo de tu integración, Braze puede añadir remitentes verificados de RCS a tus grupos de suscripción de SMS existentes o configurar nuevos. Para instrucciones detalladas de configuración, consulta [Grupos de suscripción de SMS y RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

## Migrar tráfico de SMS a RCS {#migrating-sms-traffic-to-rcs}

Si tienes grupos de suscripción de SMS y RCS separados, puedes migrar usuarios de SMS a RCS usando un Canvas de un solo paso.

Braze recomienda que primero pruebes enviando RCS a volúmenes más pequeños de usuarios y migres más usuarios al grupo de suscripción de RCS con el tiempo. Por ejemplo, si tienes 1,000,000 de usuarios suscritos a un grupo de suscripción de SMS, esto podría verse como primero migrar a todos los usuarios al nuevo grupo de suscripción y luego segmentar en una audiencia más pequeña de 50,000 a 100,000 (5-10%) para probar los mensajes RCS.

### Paso 1: Crear un Canvas y completar el horario de entrada {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Crea un Canvas y nómbralo con algo fácilmente identificable (como "Transferencia de usuarios de grupo de suscripción SMS-RCS"). Luego, planifica la campaña cuando te resulte conveniente.

### Paso 2: Definir tu audiencia {#step-2-define-your-audience}

Define tu audiencia usando uno de los siguientes métodos. A continuación, ve al paso **Ajustes de envío** y selecciona **Users who are subscribed or opted-in**.

| Método | Descripción |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Crear un segmento** | Construye un segmento que incluya a todos los usuarios en un grupo de suscripción o un subconjunto usando filtros de segmentación (como un 5-10% aleatorio). Los segmentos se actualizan antes de cada envío para reflejar tu base de usuarios actual. |
| **Aplicar filtros de Campaign o Canvas** | Refina la audiencia en el paso **Target Audience** de tu Campaign o Canvas. Ajusta las opciones de segmentación sin salir de la página para mayor flexibilidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 3: Configurar un paso de Actualización de usuario {#step-3-configure-a-user-update-step}

Añade un paso de Actualización de usuario a tu Canvas. En el paso, abre el **Advanced JSON Editor** e introduce lo siguiente (para el campo de identificador único de usuario, recomendamos usar el campo `braze_id`):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![Objeto de Actualización de usuario que contiene el código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Paso 4: Probar el Canvas {#step-4-test-the-canvas}

Recomendamos encarecidamente [probar tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases/) para confirmar que funciona como se espera antes de enviarlo a tu audiencia más amplia.

### Paso 5: Lanzar tu Canvas {#step-5-launch-your-canvas}

Después de haber probado exitosamente tu Canvas, ¡adelante, lánzalo para tu subconjunto de usuarios!

Para confirmar que tus usuarios fueron migrados exitosamente, recomendamos verificar algunos perfiles de usuario individuales que fueron actualizados. En la pestaña **Engagement**, busca **Contact Settings** y desplázate para ver los grupos de suscripción a los que el usuario está suscrito. El interruptor del grupo de suscripción de RCS debería estar ahora activado.