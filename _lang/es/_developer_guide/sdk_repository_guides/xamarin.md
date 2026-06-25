---
nav_title: SDK .NET MAUI (Xamarin)
article_title: Guía del repositorio del SDK .NET MAUI (Xamarin)
page_order: 10
description: "Referencia del README del SDK .NET MAUI (Xamarin) de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Acerca del SDK .NET MAUI (Xamarin) de Braze {#about-the-braze-net-maui-xamarin-sdk}

El SDK .NET MAUI (Xamarin) de Braze te ayuda a integrar las funciones de mensajería, análisis e interacción con el usuario de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=xamarin)

## Componentes {#components}

El formato de este repositorio es el de un componente Xamarin: dentro de `appboy-component`, encontrarás los directorios `src`,
`libs`, `component`, `nuget` y `samples`. `libs`, `src` y `samples` contienen cada uno dos directorios, uno para Android y otro para iOS. Los directorios
contienen:

- `libs`: los archivos DLL compilados de los bindings para los SDK de Braze.
- `src`: los proyectos de bindings de Xamarin que generaron los DLL que se encuentran en la carpeta libs.
- `samples`: aplicaciones Xamarin que muestran cómo utilizar los bindings para acceder al conjunto de características de Braze.
- `nuget`: archivos Nuspec para nuestros paquetes NuGet de Xamarin.

## Versionado {#versioning}

### Bindings nativos {#native-bindings}

| Nombre del archivo de binding               | Frameworks de Xamarin compatibles                         | Framework nativo de Braze                           | Versión del SDK Xamarin de Braze |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 41.0.0+                                 | 9.0.0+                    |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 y anteriores | Android SDK 23.3.0 y anteriores                     | 1.26.0 y anteriores       |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 14.0.1+                                   | 9.0.0+                    |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 y anteriores   | `Appboy_iOS_SDK.framework` versión 4.4.1 y anteriores | 1.27.0 y anteriores       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bindings nativos" }

### Xamarin y Xamarin.Forms {#xamarin-xamarinforms}

A partir del 1 de mayo de 2024, [Microsoft anunció el fin del soporte para Xamarin y Xamarin.Forms](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

El SDK de Braze dejó de ser compatible con Xamarin y Xamarin.Forms a partir de la versión `4.0.0` y añadió compatibilidad con [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui).

## ¿Tienes preguntas? {#questions}

Si tienes preguntas, ponte en contacto con [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para obtener detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).