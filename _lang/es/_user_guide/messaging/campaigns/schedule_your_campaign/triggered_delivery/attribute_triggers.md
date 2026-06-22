---
nav_title: Desencadenantes de atributos
article_title: Desencadenantes de atributos
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los desencadenantes de atributos y cómo puedes usarlos para enviar mensajes basados en acciones a los usuarios."
tool:
  - Campaigns

---

# Desencadenantes de atributos {#attribute-triggers}

> Los desencadenantes de atributos te permiten enviar mensajes basados en acciones cuando cambia el estado de suscripción de un usuario o los valores de sus atributos personalizados.

Los desencadenantes de atributos están disponibles para los siguientes escenarios:

- Actualizaciones del estado de suscripción.
- Los valores de atributos personalizados de tipo booleano, entero, cadena o fecha cambian a cualquier valor.
- Los valores de atributos personalizados de tipo booleano, entero o cadena cambian a un valor específico.

{% alert note %}
En el dashboard, los tipos de atributos personalizados aparecen como `Number` (para enteros) y `Time` (para fechas), no como `String` o `Date`.
{% endalert %}

Para empezar a usar los desencadenantes de atributos, crea una campaña o un componente de Canvas y selecciona **Entrega basada en acciones** como tu método de entrega. Luego, selecciona el desencadenante de atributo que deseas usar.

![Sección "Entrega basada en acciones" con un menú desplegable para seleccionar un desencadenante.]({% image_buster /assets/img_archive/trigger_attribute.png %})

## Actualizar estado de suscripción {#update-subscription-status}

Usa el desencadenante `Update Subscription Status` para dirigirte a los usuarios cuando se actualice su estado de suscripción.

Por ejemplo, puedes dirigirte a los usuarios cuando su estado de suscripción de correo electrónico o push cambie a opted in, y agradecerles por suscribirse. También puedes enviar un webhook a tus sistemas cada vez que un usuario cancele su suscripción de correo electrónico para que tus sistemas internos estén actualizados con la información más reciente del estado de suscripción.

{% alert important %}
Este desencadenante no se aplica cuando se crea un nuevo usuario con el estado global de correo electrónico predeterminado de `subscribed` y hay una solicitud posterior para actualizar el estado a `subscribed`, ya que el estado de suscripción no ha cambiado.
{% endalert %}

## Actualizar estado del grupo de suscripción {#update-subscription-group-status}

Usa el desencadenante `Update Subscription Group Status` para dirigirte a los usuarios cuando se actualice su estado del grupo de suscripción para correo electrónico, SMS o WhatsApp.

Por ejemplo, puedes dirigirte a los usuarios con un mensaje SMS de bienvenida cuando se suscriban a tu programa. También puedes especificar la fuente de la actualización para tener un control más preciso sobre cuándo se envía un mensaje.

Las fuentes de actualización disponibles varían según el canal:
- Paso de actualización de usuario de Canvas
- Importar CSV
- List-Unsubscribe
- Centro de preferencias
- REST API
- SDK
- Shopify (correo electrónico, SMS)
- Mensaje de entrada (SMS)

Por ejemplo, puede que solo quieras enviar tu SMS de bienvenida cuando la actualización proviene de la REST API y no de un mensaje de entrada, ya que Braze ya responde automáticamente a ciertos SMS de entrada.

## Cambiar valor de atributo personalizado {#change-custom-attribute-value}

Para el cambio de atributo, el desencadenante se evalúa primero y luego los criterios de audiencia. Esto difiere del comportamiento predeterminado en el que los criterios de audiencia se evalúan primero y luego el desencadenante. Para evitar una condición de carrera, asegúrate de que el atributo utilizado como desencadenante no sea el mismo que el atributo utilizado para calificar a tu audiencia.

### Opción de cualquier valor nuevo {#any-new-value-option}

Usa el desencadenante `Change Custom Attribute Value` con la opción `any new value` para dirigirte a los usuarios cuando un valor de tipo booleano, entero, cadena o fecha cambie a cualquier valor nuevo.

Por ejemplo, dirígete a los usuarios cuando cambie su número de puntos de recompensa para informarles cuántos puntos tienen ahora. En este ejemplo, supongamos que un usuario tiene 85 puntos de recompensa y has configurado una campaña para que se desencadene cuando el atributo de puntos de recompensa cambie a cualquier valor nuevo. Si el valor del atributo de puntos de recompensa de este usuario cambia a cualquier valor nuevo (como 83, 84, 86, etc.), la campaña se desencadena.

Considera el siguiente ejemplo de caso de uso con una notificación de actualización de nivel. Puede que quieras alertar a los usuarios si cambia su nivel de recompensas. Para lograr este caso de uso, configura una campaña que se desencadene a partir de `Change Custom Attribute Value` y configúrala para que se desencadene cuando el atributo personalizado de nivel de recompensas cambie a cualquier valor nuevo.

{% alert important %}
Los desencadenantes de atributos no están disponibles actualmente para atributos de tipo array.
{% endalert %}

![Un desencadenante "Change Custom Attribute Value" para "AA_current_rewards_tier" que cambia a cualquier valor.]({% image_buster /assets/img_archive/any_value.png %})

También puedes usar Liquid para personalizar el cuerpo del mensaje con el nuevo nivel de recompensas del cliente y proporcionarle más información sobre el cambio.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

### Valor específico {#specific-value}

Usa el desencadenante `Change Custom Attribute Value` con la opción `specific value` para dirigirte a los usuarios cuando un atributo personalizado de tipo booleano, entero o cadena cambie a un valor específico.

Por ejemplo, dirígete a los usuarios cuando su nivel de recompensas cambie al mejor nivel. Para este ejemplo, supongamos que el mejor nivel de recompensas es Super VIP. Puedes configurar una campaña para que se desencadene cuando el atributo personalizado de nivel de recompensas de un usuario cambie a `Super VIP` para poder felicitar al usuario por convertirse en Super VIP.

![Un desencadenante "Change Custom Attribute Value" para "AA_current_rewards_tier" que cambia al valor específico de "super vip".]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Los desencadenantes de atributos para valores específicos de atributos personalizados no están disponibles para atributos personalizados de tipo array y fecha.
- El desencadenante de cambio de valores de atributos personalizados no se activa cuando el valor del atributo personalizado se actualiza a null.
- El desencadenante de cambio de valores de atributos personalizados solo se activa cuando el valor de un atributo personalizado cambia. Si el valor actual de un atributo personalizado se reenvía a Braze (por ejemplo, el valor del atributo de color favorito es rojo y vuelves a enviar el valor rojo a Braze), el desencadenante de cambio de valores de atributos personalizados no se activa.
- El desencadenante de cambio de valores de atributos personalizados también se aplica a los nuevos usuarios creados.
{% endalert %}