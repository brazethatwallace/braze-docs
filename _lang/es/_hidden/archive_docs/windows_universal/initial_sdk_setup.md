---
nav_title: Configuración inicial del SDK or kit de desarrollo de software
article_title: Configuración inicial del SDK or kit de desarrollo de software para Windows Universal
platform: Windows Universal
page_order: 0
description: "En este artículo de referencia se cubren los pasos iniciales de integración del SDK or kit de desarrollo de software para integrar el SDK or kit de desarrollo de software de Braze en tu plataforma Windows Universal."
search_rank: 1
hidden: true
---

# Integración inicial del SDK or kit de desarrollo de software {#initial-sdk-integration}
{% multi_lang_include archive/windows_deprecation.md %}

El SDK or kit de desarrollo de software de Braze te proporcionará una API para reportar información que se utilizará en análisis, segmentación e interacción, así como la capacidad de registrar usuarios para push y recibir notificaciones.

>  El SDK or kit de desarrollo de software de Windows Universal también es compatible con aplicaciones .NET MAUI para Windows.

## Paso 1: Instala el SDK or kit de desarrollo de software mediante el administrador de paquetes NuGet {#step-1-install-the-sdk-via-the-nuget-package-manager}

El SDK or kit de desarrollo de software de Windows Universal se instala a través del [administrador de paquetes NuGet](http://www.nuget.org/). Para instalar el SDK or kit de desarrollo de software de Braze para Windows a través de NuGet:

1. Haz clic con el botón derecho en el archivo del proyecto
2. Haz clic en "Manage NuGet Packages"
3. Haz clic en "Online" en el menú desplegable de la izquierda
4. Busca "Appboy" en "NuGet.org"
5. Haz clic en el paquete NuGet "AppboyPlatform.Universal.Release" y haz clic en Install

>  La biblioteca de Windows Universal debe utilizarse para todas las aplicaciones de Windows 8.1, Windows Phone 8.1 y UWP.

## Paso 2: Creación y configuración de AppboyConfiguration.xml {#step-2-creation-and-configuration-of-appboyconfigurationxml}

Crea un archivo llamado `AppboyConfiguration.xml` en el directorio raíz de tu proyecto y añade el siguiente fragmento de código en ese archivo:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  Asegúrate de actualizar `YOUR_API_KEY_HERE` con tu clave de API, que puedes encontrar en la página [Claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/).

Una vez que hayas añadido ese fragmento de código, asegúrate de modificar las siguientes propiedades de archivo para `AppboyConfiguration.xml`

1. Configura `Build Action` en `Content`
2. Configura `Copy to Output Directory` en `Copy Always`

## Paso 3: Configuración de package.appxmanifest {#step-3-configuring-packageappxmanifest}

En la pestaña "Capabilities", asegúrate de que `Internet (Client)` está marcada.
![]({% image_buster /assets/img_archive/internet_client.png %})

## Paso 4: Editar la clase de tu aplicación {#step-4-editing-your-app-class}

- Añade lo siguiente a los `usings` de tu archivo `App.xaml.cs`:

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Llama a lo siguiente dentro de tu método del ciclo de vida `OnLaunched`:

```csharp
Appboy.SharedInstance.OpenSession();
```

- Llama a lo siguiente dentro de tu método del ciclo de vida `OnSuspending`:

```csharp
Appboy.SharedInstance.CloseSession();
```

## Integración básica del SDK or kit de desarrollo de software completa {#basic-sdk-integration-complete}

Ahora Braze debería estar recopilando datos de tu aplicación. Consulta los siguientes artículos sobre cómo registrar [atributos]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/), [eventos]({{site.baseurl}}/developer_guide/analytics/logging_events/) y [compras]({{site.baseurl}}/developer_guide/analytics/logging_purchases/) en nuestro SDK or kit de desarrollo de software y cómo instrumentar la mensajería push.

>  Si estás utilizando el proyecto Unity de Braze en la misma aplicación, puede que tengas que cualificar completamente las llamadas a Braze como "AppboyPlatform.Universal.Appboy"