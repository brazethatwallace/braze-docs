---
nav_title: "Botones de acción para notificación push"
article_title: "Botones de acción para notificación push"
page_order: 1
page_type: reference
description: "Este artículo de referencia cubre qué son los botones de acción para notificación push y las diferencias entre las plataformas iOS y Android."
channel:
  - Push

---

# Botones de acción para notificación push {#push-action-buttons}

> Los botones de acción para notificación push te permiten configurar contenido y acciones para los botones cuando utilizas notificaciones push de Braze en iOS y Android. Con los botones de acción, tus usuarios pueden interactuar directamente con tu aplicación desde una notificación sin necesidad de acceder a la experiencia de la aplicación.

![Una notificación push de iOS con dos botones de acción push: Aceptar y Rechazar.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

## Crear botones de acción {#creating-action-buttons}

Cada botón interactivo puede enlazar a una página web, un vínculo profundo o abrir la aplicación.

- Para Campaigns push estándar, puedes especificar tus botones de acción push en la sección **On-Click Behavior** del creador de mensajes push en el dashboard.
- Para [Campaigns push rápidas]({{site.baseurl}}/quick_push/), los botones de acción se pueden configurar por separado para cada plataforma en la pestaña **Settings**.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Para usar botones de acción en tus mensajes push de iOS, haz lo siguiente:

1. Activa los botones de acción en la pestaña **Compose** para una Campaign estándar o en la pestaña **Settings** para push rápido.
2. Selecciona tu **iOS Notification Category** de las siguientes combinaciones de botones disponibles:
 - Aceptar / Rechazar
 - Sí / No
 - Confirmar / Cancelar
 - Más
 - Categoría personalizada de iOS preregistrada

![Menú desplegable de categoría de notificación de iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Debido a la forma en que iOS gestiona los botones, necesitas realizar pasos de integración adicionales al configurar los botones de acción push, que se describen en nuestra [documentación para desarrolladores]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). En particular, necesitas configurar las categorías de iOS o seleccionar entre ciertas opciones de botones predeterminadas. Para las integraciones de Android, estos botones funcionarán automáticamente.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Para usar botones de acción en tus mensajes push de Android, haz lo siguiente:

1. Activa los botones de acción en la pestaña **Compose** para una Campaign estándar o en la pestaña **Settings** para push rápido.
2. Selecciona <i class="fas fa-plus-circle"></i> **Add Button** y especifica el texto del botón y el **On-Click Behavior**. Puedes seleccionar entre las siguientes acciones disponibles:
  - Abrir aplicación
  - Redirigir a URL web
  - [Vínculo profundo]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) a la aplicación

![Seleccionando "Abrir aplicación" como el comportamiento al hacer clic para un botón de notificación.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Puedes añadir hasta tres botones en tu push.

#### Límites de caracteres en Android {#android-character-limits}

A diferencia de los botones de iOS, que se apilan verticalmente, los botones de Android se muestran uno al lado del otro en una fila. Esto significa que cuantos más botones añadas (hasta tres), menos espacio tendrás para el texto del botón.

![Botones de acción push de Android con texto truncado.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

La siguiente tabla describe cuántos caracteres puedes añadir antes de que el texto del botón se trunque, dependiendo de cuántos botones tengas:

| Número de botones | Máximo de caracteres por botón |
| --- | --- |
| 1 | 46 caracteres |
| 2 | 20 caracteres |
| 3 | 11 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}