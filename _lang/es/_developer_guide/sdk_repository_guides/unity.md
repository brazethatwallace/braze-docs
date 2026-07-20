---
nav_title: SDK de Unity
article_title: Guía del repositorio del SDK de Unity
page_order: 9
description: "Referencia del README del SDK de Unity de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del SDK de Unity {#unity-sdk-repository-guide}

## Acerca del SDK de Unity de Braze {#about-the-braze-unity-sdk}

El SDK de Unity de Braze te ayuda a integrar las funciones de mensajería, análisis y participación de usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=unity)

## Configuración del plugin {#plugin-setup}

Antes de poder empezar a utilizar Braze en scripts de Unity, tendrás que importar los archivos del plugin a tu proyecto de Unity.

**Recomendado:** Los plugins de Android e iOS están incluidos como un paquete de Unity disponible para su descarga en la [página de versiones del SDK][1].

**Configuración manual del plugin:** Alternativamente, puedes copiar los plugins en tu proyecto de Unity:
  1. Primero, clona este repositorio.
  2. Si no estás utilizando ningún otro plugin, lo único que tienes que hacer es copiar el directorio `Plugins` de este repositorio en la carpeta `Assets` de tu proyecto de Unity.
  3. Si ya tienes un directorio `/<your-project>/Assets/Plugins` (probablemente porque ya estás utilizando otro plugin), copia `Plugins/Appboy/AppboyBinding.cs` en `/<your-project>/Assets/Plugins`. Luego copia el contenido de `Plugins/iOS` y `Plugins/Android` de este repositorio en `/<your-project>/Assets/Plugins/iOS` y `/<your-project>/Assets/Plugins/Android` respectivamente.

## Configuración de la integración {#integration-setup}

Para integrar Braze en tu aplicación de Unity, completa nuestras instrucciones para [integrar el SDK de Unity de Braze][2].

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=unity

## Ponte en contacto {#contact}

Si tienes preguntas, ponte en contacto con [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para obtener detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk).