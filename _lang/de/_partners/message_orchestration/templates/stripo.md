---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Stripo, einem Drag-and-Drop-E-Mail-Template-Builder für die Erstellung anspruchsvoller E-Mails mit interaktiven Elementen."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) ist ein Drag-and-Drop-E-Mail-Template-Builder für die Gestaltung responsiver E-Mails mit interaktiven Elementen. Nutzer:innen von Stripo können mit dem Stripo-Editor auch HTML bearbeiten und entscheiden, welche Elemente auf verschiedenen Geräten angezeigt oder ausgeblendet werden sollen.

_Diese Integration wird von Stripo gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Stripo ermöglicht es Ihnen, Ihre angepassten Stripo-E-Mails zu exportieren und als Templates in Braze hochzuladen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ------------| ----------- |
| Stripo-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Stripo-Konto. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit vollständigen **Templates**-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster-Instanz | Ihre Braze-[Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren Representational State Transfer-Endpunkt abgestimmt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Stripo-E-Mail erstellen {#step-1-create-stripo-email}

Erstellen Sie eine Stripo-E-Mail auf der Stripo-Plattform und klicken Sie auf **Export**.

![Stripo-Export]({% image_buster /assets/img_archive/stripo_export.png %})

### 2. Schritt: Template nach Braze exportieren {#step-2-export-template-to-braze}

Wählen Sie in dem erscheinenden Dialog **Braze** als Exportmethode aus.

Geben Sie anschließend Ihren **Kontonamen** (z. B. den Workspace-Namen), den **API-Schlüssel** und Ihre **Cluster-Instanz** ein.

![Stripo-Formular]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Dies ist eine einmalige Einrichtung, und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

## Nutzung {#usage}

Ihr hochgeladenes Stripo-Template finden Sie in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail-Templates**. Mit diesem E-Mail-Template können Sie jetzt damit beginnen, ansprechende E-Mail-Nachrichten an Ihre Kund:innen zu versenden!