---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Stensul, einer E-Mail-Plattform für Unternehmen zur Erstellung mobiler, responsiver E-Mail-Templates für verschiedene Kanäle."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) stellt E-Mail-Marketern Tools zur Verfügung, mit denen sie in Stensul responsive, markengerechte E-Mails erstellen können, bevor sie diese zur Erstellung von Campaigns in Echtzeit an Braze weiterleiten.

_Diese Integration wird von Stensul gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Stensul ermöglicht es Ihnen, Ihre HTML-formatierten E-Mails aus Stensul zu exportieren und sie als Templates in Braze hochzuladen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ------------| ----------- |
| Stensul-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Stensul-Konto. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit vollständigen **Templates**-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster-Instanz | Ihre Braze-[Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Stellen Sie Ihrem Stensul Customer-Success-Team Ihren Braze REST-API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Team wird dann die erste Integration für Sie einrichten.

{% alert important %}
Dies ist eine einmalige Einrichtung, und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

### 1. Schritt: Stensul-E-Mail erstellen {#step-1-create-stensul-email}

Erstellen Sie eine Stensul-E-Mail auf der Stensul-Plattform und klicken Sie auf **Complete**.

![Stensul-Speicheroptionen]({% image_buster /assets/img_archive/stensul_save_options.png %})

### 2. Schritt: Template nach Braze exportieren {#step-2-export-template-to-braze}
Wählen Sie in dem neuen Dialog, der auf der Fertigstellungsseite erscheint, **Upload to ESP** aus.

![Stensul-Upload-Optionen]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Geben Sie dann den **Template-Namen**, den **Betreff** und den **Preheader** für Ihre E-Mail ein und wählen Sie **Upload**. Sie erhalten anschließend eine Bestätigung, dass der Upload erfolgreich war, sowie ggf. einen Verlauf früherer Uploads der Datei.

![Stensul-Upload erfolgreich]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Nutzung {#usage}

Sie finden Ihr hochgeladenes Stensul-Template in Ihrem Braze-Konto im Bereich **Templates & Media > Email Templates**. Mit diesem E-Mail-Template können Sie jetzt damit beginnen, ansprechende E-Mail-Nachrichten an Ihre Kund:innen zu versenden!