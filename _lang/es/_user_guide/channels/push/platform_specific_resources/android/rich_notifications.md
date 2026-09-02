---
nav_title: Crear notificaciones enriquecidas
article_title: "Creación de notificaciones push enriquecidas para Android"
page_order: 3
page_layout: tutorial
description: "Este tutorial cubre cómo configurar notificaciones enriquecidas de Android para tus Campaigns de Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns

---

# Crear notificaciones push enriquecidas para Android {#create-rich-push-notifications-for-android}

> Las notificaciones enriquecidas permiten una mayor personalización en tus notificaciones push al añadir contenido adicional más allá del texto. Las notificaciones de Android incluyen imágenes en las notificaciones push desde hace tiempo, lo que se conoce como "imagen de notificación expandida".

## Requisitos previos {#prerequisites}

Antes de crear una notificación push enriquecida para Android, ten en cuenta los siguientes detalles:

- Las imágenes de notificación expandida de Android deben tener una proporción de 2:1, pero no tienen un límite de tamaño.
- Android también permite configurar una imagen independiente para la vista de notificación estándar. Estos son los tamaños de imagen recomendados:
  - **Pequeña:** 512x256
  - **Mediana:** 1024x512
  - **Grande:** 2048x1024
- Actualmente, las notificaciones enriquecidas de Android solo admiten imágenes estáticas, incluidos los formatos de imagen JPEG y PNG. Los GIF y otros formatos de imagen aún no son compatibles.
- Añadir botones de acción a tu notificación push puede afectar el área de la imagen que se muestra. Prueba con la vista previa del panel y dispositivos reales para confirmar que los resultados son los esperados.
- El SDK de Braze para Android debe estar habilitado para que la imagen se renderice.

{% alert note %}
Aunque Braze proporciona instrucciones sobre cómo configurar notificaciones push enriquecidas, la representación real de las notificaciones push enriquecidas puede variar en función de factores externos como la relación de aspecto del dispositivo, la versión de Android, las restricciones específicas del fabricante (OEM) y otros. Te recomendamos realizar un envío de prueba a varios dispositivos Android para asegurarte de que tus notificaciones push enriquecidas se muestren como esperas.
{% endalert %}

## Configurar tu notificación enriquecida de Android {#setting-up-your-android-rich-notification}

### Paso 1: Crear una campaña push {#step-1-create-a-push-campaign}

Sigue los pasos para [crear una campaña]({{site.baseurl}}/user_guide/channels/push/create_a_push_message) y redactar una notificación push para Android. Utilizarás el mismo creador para configurar notificaciones push que no contengan contenido enriquecido.

### Paso 2: Añadir texto descriptivo {#step-2-add-captioning}

Añade el **Summary Text** que deseas mostrar antes de la imagen en la notificación.

![Una notificación push enriquecida de una aplicación de comida para mascotas llamada Dog que indica que es hora de pedir más comida para Spot con texto de resumen.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Paso 3: Añadir contenido multimedia {#step-3-add-media}

Añade tu imagen en el campo **Android Notification Image** en el creador del mensaje. Las imágenes se pueden cargar directamente a través del panel o especificando una URL de contenido alojada en otro lugar.

Para obtener detalles sobre las imágenes compatibles, consulta [Especificaciones de imagen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications).

![La sección de imagen de notificación de Android donde puedes añadir una imagen o introducir una URL de imagen.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Paso 4: Continuar creando tu campaña {#step-4-continue-creating-your-campaign}

Una vez que el contenido de tu notificación enriquecida se haya cargado en el panel, puedes continuar [planificando tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).