---
nav_title: Configuración inicial del SDK or kit de desarrollo de software con Eclipse
page_order: 1
page_type: update
noindex: true
description: "Este artículo archivado describe cómo realizar una configuración inicial del SDK or kit de desarrollo de software con Eclipse. Braze ha dejado de ser compatible con el IDE Eclipse."
---

# Configuración inicial del SDK or kit de desarrollo de software con Eclipse {#initial-sdk-setup-with-eclipse}

{% alert update %}
Braze ha eliminado la compatibilidad con el IDE de Eclipse debido a que [Google ha anulado la compatibilidad con el complemento de herramientas para desarrolladores de Android de Eclipse](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Si necesitas ayuda con la integración de Eclipse antes de la migración, [ponte en contacto con el equipo de soporte]({{site.baseurl}}/support_contact/) para recibir asistencia.
{% endalert %}

## Paso 1 {#step-1}
En tu línea de comandos, clona el [repositorio GitHub de Braze Android](https://github.com/braze-inc/braze-android-sdk).

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Paso 2 {#step-2}
Importa el proyecto Braze a tu espacio de trabajo local

En Eclipse:

  - Ve a **File** > **Import**.

    ![File Import]({{site.baseurl}}/assets/img_archive/file_import.png)
  - Selecciona **Android** > **Existing Android Code into Workspace**.

    ![Android Import]({{site.baseurl}}/assets/img_archive/android_import.png)
  - Haz clic en **"Browse"**.

    ![Browse]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Marca la carpeta del proyecto Braze UI, así como **"copy project into workspace"** y haz clic en **"Finish"**.

    ![Select Android UI Project]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## Paso 3 {#step-3}
Haz referencia a Braze en tu propio proyecto.
En Eclipse:

  - Haz clic con el botón derecho en tu proyecto y selecciona **"Properties"**.

    ![Click Properties]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - En **"Android"**, haz clic en **"Add..."** en la sección Library y añade android-SDK or kit de desarrollo de software-ui como biblioteca a tu aplicación.

    ![Braze Add]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## Paso 4 {#step-4}
Resuelve los errores de dependencia y corrige el objetivo de compilación.

En este momento, es posible que aparezcan errores con el código de Braze; esto se debe a que sus dependencias no están cargadas y el objetivo de compilación es posiblemente incorrecto:

   - Haz clic con el botón derecho en el proyecto Braze UI y selecciona **Properties**->**Android** para asegurarte de que el objetivo de compilación está establecido en la versión actual de las herramientas de compilación de Braze.

      ![Build Target]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Haz clic con el botón derecho en el proyecto Braze UI y selecciona **Properties**->**Java Build Path**->**Add JARs…** y añade 'android-support-v4.jar' de la aplicación principal como biblioteca.

      ![Support]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## Paso 5 {#step-5}

Añade las piezas finales.

  - Para la versión 1.10.0 o superior del SDK or kit de desarrollo de software, tendrás que añadir
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  a tu AndroidManifest.xml, ya que Eclipse no admite la fusión de manifiestos.

  - Para la versión 1.7.0 o superior del SDK or kit de desarrollo de software, tendrás que copiar "assets/fontawesome-webfont.ttf" de nuestro proyecto de biblioteca a tu aplicación. Eclipse no incluye automáticamente la carpeta de activos de las bibliotecas.