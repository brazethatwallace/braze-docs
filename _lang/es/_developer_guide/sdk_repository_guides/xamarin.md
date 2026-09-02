---
nav_title: SDK .NET MAUI (Xamarin)
article_title: Guía del repositorio del SDK .NET MAUI (Xamarin)
page_order: 10
description: "Referencia del README del SDK .NET MAUI (Xamarin) de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del SDK .NET MAUI (Xamarin) {#net-maui-xamarin-sdk-repository-guide}

## Acerca del SDK de Braze .NET MAUI (Xamarin) {#about-the-braze-net-maui-xamarin-sdk}

El SDK de Braze .NET MAUI (Xamarin) te ayuda a integrar las funciones de mensajería, análisis y participación de usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=xamarin)

## Componentes {#components}

El formato de este repositorio es el de un componente Xamarin: dentro de `appboy-component`, encontrarás los directorios `src`,
`libs`, `component`, `nuget` y `samples`. `libs`, `src` y `samples` contienen dos directorios cada uno, uno para Android y otro para iOS. Los directorios
contienen:

- `libs`: Los enlaces DLL compilados para los SDK de Braze.
- `src`: Los proyectos de enlaces Xamarin que generaron los DLL que se encuentran en la carpeta `libs`.
- `samples`: Aplicaciones Xamarin que muestran cómo utilizar los enlaces para acceder al conjunto de características de Braze.
- `nuget`: Archivos Nuspec para nuestros paquetes NuGet de Xamarin.

## Control de versiones {#versioning}

### Enlaces nativos {#native-bindings}

La siguiente tabla enumera los frameworks compatibles y las versiones del framework nativo de Braze para cada enlace de Xamarin.

| Nombre del archivo de enlace               | Frameworks de Xamarin compatibles                         | Framework nativo de Braze                           | Versión del SDK Xamarin de Braze |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 43.1.1+                                 | 10.0.0+                   |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 y anteriores | Android SDK 23.3.0 y anteriores                     | 1.26.0 y anteriores       |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 18.2.0+                                   | 10.0.0+                   |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 y anteriores   | `Appboy_iOS_SDK.framework` versión 4.4.1 y anteriores | 1.27.0 y anteriores       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Enlaces nativos" }

### Xamarin y Xamarin.Forms {#xamarin-xamarinforms}

A partir del 1 de mayo de 2024, [Microsoft anunció el fin del soporte para Xamarin y Xamarin.Forms](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

El SDK de Braze dejó de ser compatible con Xamarin y Xamarin.Forms a partir de la versión `4.0.0` y añadió compatibilidad con [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui).

## ¿Preguntas? {#questions}

Si tienes preguntas, contacta con el soporte técnico de Braze para obtener ayuda.
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).