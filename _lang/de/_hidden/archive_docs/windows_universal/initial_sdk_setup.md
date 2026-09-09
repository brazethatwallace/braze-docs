---
nav_title: SDK-Ersteinrichtung
article_title: Erste SDK-Einrichtung für Windows Universal
platform: Windows Universal
page_order: 0
description: "Dieser Referenzartikel beschreibt die ersten Schritte der SDK-Integration, um das Braze SDK auf Ihrer Windows Universal Plattform zu integrieren."
search_rank: 1
hidden: true
---

# Erste SDK-Integration {#initial-sdk-integration}
{% multi_lang_include archive/windows_deprecation.md %}

Das Braze SDK stellt Ihnen eine API zur Verfügung, mit der Sie Informationen für Analytics, Segmentierung und Engagement melden können, sowie die Möglichkeit, Nutzer:innen für Push-Benachrichtigungen zu registrieren und diese zu empfangen.

>  Das Windows Universal SDK ist auch mit .NET MAUI Windows Apps kompatibel.

## 1. Schritt: Installieren Sie das SDK über den NuGet-Paketmanager {#step-1-install-the-sdk-via-the-nuget-package-manager}

Das Windows Universal SDK wird über den [NuGet Package Manager:in](http://www.nuget.org/) installiert. So installieren Sie das Braze Windows SDK über NuGet:

1. Rechtsklicken Sie auf die Projektdatei
2. Klicken Sie auf „Manage NuGet Packages“
3. Klicken Sie auf „Online“ im Dropdown-Menü auf der linken Seite
4. Suchen Sie in „NuGet.org“ nach „Appboy“
5. Klicken Sie auf das NuGet-Paket „AppboyPlatform.Universal.Release“ und klicken Sie auf Installieren

>  Die Windows Universal Library sollte für alle Windows 8.1-, Windows Phone 8.1- und UWP-Anwendungen verwendet werden.

## 2. Schritt: Erstellung und Konfiguration von AppboyConfiguration.xml {#step-2-creation-and-configuration-of-appboyconfigurationxml}

Erstellen Sie eine Datei namens `AppboyConfiguration.xml` im Stammverzeichnis Ihres Projekts und fügen Sie das folgende Code-Snippet in diese Datei ein:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  Stellen Sie sicher, dass Sie `YOUR_API_KEY_HERE` mit Ihrem API-Schlüssel aktualisieren, den Sie auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/) finden.

Sobald Sie dieses Snippet hinzugefügt haben, müssen Sie die folgenden Dateieigenschaften für `AppboyConfiguration.xml` ändern:

1. Setzen Sie die `Build Action` auf `Content`
2. Setzen Sie `Copy to Output Directory` auf `Copy Always`

## 3. Schritt: Konfigurieren von package.appxmanifest {#step-3-configuring-packageappxmanifest}

Vergewissern Sie sich auf dem Tab „Capabilities“, dass `Internet (Client)` aktiviert ist.
![]({% image_buster /assets/img_archive/internet_client.png %})

## 4. Schritt: Bearbeiten Ihrer App-Klasse {#step-4-editing-your-app-class}

- Fügen Sie Folgendes in die `usings` Ihrer `App.xaml.cs`-Datei ein:

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Rufen Sie Folgendes innerhalb Ihrer `OnLaunched`-Lifecycle-Methode auf:

```csharp
Appboy.SharedInstance.OpenSession();
```

- Rufen Sie Folgendes innerhalb Ihrer `OnSuspending`-Lifecycle-Methode auf:

```csharp
Appboy.SharedInstance.CloseSession();
```

## Grundlegende SDK-Integration abgeschlossen {#basic-sdk-integration-complete}

Braze sollte nun Daten von Ihrer Anwendung sammeln. In den folgenden Artikeln erfahren Sie, wie Sie [Attribute]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/), [Ereignisse]({{site.baseurl}}/developer_guide/analytics/logging_events/) und [Käufe]({{site.baseurl}}/developer_guide/analytics/logging_purchases/) in unserem SDK protokollieren und wie Sie Push-Messaging einsetzen können.

>  Wenn Sie das Unity-Projekt von Braze in der gleichen App verwenden, müssen Sie Aufrufe an Braze möglicherweise vollständig als „AppboyPlatform.Universal.Appboy“ qualifizieren.