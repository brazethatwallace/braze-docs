---
nav_title: Campañas de usuarios activos
article_title: Campañas de usuarios activos
page_order: 0.5
page_type: tutorial
description: "Este artículo práctico describe los beneficios de las campañas de usuarios activos dentro del panel de Braze y los pasos para crear y configurar una."
tool:
  - Campaigns

---

# Campañas de usuarios activos {#active-user-campaigns}

> Identifica a tus usuarios activos para crear campañas personalizadas y recompensar a quienes frecuentan tu plataforma.

Contactar a los usuarios ya activos de tu aplicación puede ser una herramienta poderosa para construir una base fiel de usuarios recurrentes. Un poco de reconocimiento personalizado hacia tus usuarios más comprometidos puede convertirlos en promotores de tu aplicación.

También puedes consultar nuestro [Curso de Braze Learning](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sobre estrategia de marketing para correo electrónico y campañas según el ciclo de vida recomendadas.

## Comprender a los usuarios activos {#understanding-active-users}

Braze define un "usuario activo" para un periodo de tiempo determinado como cualquier usuario que tiene una sesión en ese periodo.

Si un usuario pierde la conectividad, los datos de la sesión se almacenarán en caché localmente y se cargarán cuando el usuario recupere la conexión de red. Estas sesiones también se aplicarán al recuento de usuarios activos. Además, si tu aplicación tiene un proceso de registro, Braze contará a todos los usuarios como activos, estén registrados o no.

Si configuras ID de usuario para identificar a los usuarios cuando un nuevo usuario inicia sesión, se contará como un usuario activo independiente. Los usuarios que se actualicen a través de la API también se contarán como usuarios activos en el periodo en que se actualicen.

## Paso 1: Identificar a tus mejores usuarios {#step-1-identifying-your-top-users}

Usando nuestra selección de filtros, crea un segmento de usuarios que consideres que abarca tu base de usuarios más leales y constantes. El siguiente segmento de ejemplo define a los mejores usuarios.

![Ejemplo de filtros de segmento en Braze que definen una audiencia de mejores usuarios.]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

Además, no tendrás que seguir actualizando este segmento, ya que los usuarios que entren o salgan de las restricciones de la campaña serán segmentados o descartados de forma correspondiente.

{% alert note %}
El ejemplo anterior segmenta a los usuarios por uso general de la aplicación. En la mayoría de los casos, el conjunto total de filtros necesarios para definir tu segmento de mejores usuarios estará determinado en gran medida por las características específicas de tu aplicación.
{% endalert %}

## Paso 2: Ponte en contacto con tus mejores usuarios {#step-2-contact-your-top-users}

### Haz que tus usuarios se sientan valorados {#make-your-users-feel-appreciated}

Haz que tus usuarios se sientan valorados agradeciéndoles su lealtad y dedicación a tu aplicación. Dales más razones para seguir volviendo a tu aplicación y fomentar más actividad. Esto puede tomar la forma de ofertas especiales o bonificaciones exclusivas para tus mejores usuarios.

Las recompensas inesperadas pueden ser más efectivas para fomentar acciones continuas de los usuarios que si las hubieras prometido desde el principio.

![Una campaña en el paso Redactar con una notificación enriquecida de iOS que dice: "¡Gracias de nuevo por comprar con nosotros! Para mostrar nuestro agradecimiento, te ofrecemos envío gratuito en tu próxima compra".]({% image_buster /assets/img/congratulations_push.jpg %})

### Haz seguimiento de tus resultados {#keep-track-of-your-results}

Haz seguimiento de las aperturas para asegurarte de que estás segmentando al grupo adecuado de usuarios con el tipo de mensaje óptimo. Además, haz seguimiento de las cancelaciones de suscripción push y ten cuidado de no perder a estos usuarios clave.