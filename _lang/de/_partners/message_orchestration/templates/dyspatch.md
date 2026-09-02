---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Dyspatch, einem Drag-and-Drop-E-Mail-Builder, mit dem Sie ansprechende, responsive und überzeugende E-Mails erstellen können, ohne Code schreiben zu müssen."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) bietet einen intuitiven Drag-and-Drop-E-Mail-Builder, mit dem Sie ansprechende, responsive und überzeugende E-Mails erstellen können, ohne Code schreiben zu müssen. Arbeiten Sie mit Ihrem Team zusammen, um E-Mails in Dyspatch zu erstellen und zu genehmigen, und exportieren Sie sie dann in wenigen Schritten nach Braze!

_Diese Integration wird von Dyspatch gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Dyspatch und Braze ermöglicht es Ihnen, den Lebenszyklus Ihrer E-Mail-Erstellung zu vereinfachen, indem Sie Dyspatch-E-Mail-Templates direkt nach Braze exportieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dyspatch-Konto | Ein [Dyspatch-Konto](https://www.dyspatch.io/login/) mit einer [Eigentümer- oder Administratorrolle](https://docs.dyspatch.io/administration/dyspatch_roles/) ist erforderlich, um diese Partnerschaft zu nutzen. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit vollständigen **Templates**-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Mit der Integration von Braze und Dyspatch können Sie Dyspatch-E-Mail-Templates direkt in Ihre Braze-Medienbibliothek exportieren oder Ihr Template herunterladen und manuell hochladen.

### 1. Schritt: Braze-Integration erstellen {#step-1-create-the-braze-integration}

Öffnen Sie im Dyspatch-Administrationsportal das Dropdown-Menü Ihres Benutzernamens und wählen Sie **Integrations**. Erstellen Sie eine neue Integration, wählen Sie **Braze** aus und geben Sie Ihren Braze-API-Schlüssel ein.

Im Feld **Localize Exports By** können Sie festlegen, wie Sie die Lokalisierung verwalten möchten. Mit diesem Feld können Sie [Ihre E-Mail-Templates lokalisieren](https://docs.dyspatch.io/localization/localizing_a_template/) und nach Braze exportieren, um auf einfache Weise E-Mails zu versenden, die nach Sprache oder Region personalisiert sind.

![Dyspatch-Template exportieren]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### 2. Schritt: Template nach Braze exportieren {#step-2-export-template-to-braze}

Nachdem Sie eine E-Mail in Dyspatch fertiggestellt haben, rufen Sie das veröffentlichte E-Mail-Template auf und klicken Sie auf **Download/Export** und dann auf **Export to Integration**, um Ihr Template an Braze zu senden.

Wenn Sie Ihr Template manuell hochladen möchten, rufen Sie das veröffentlichte E-Mail-Template auf und klicken Sie auf **Download/Export** und dann auf **Download HTML**. Wählen Sie anschließend in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail-Templates** die Option **From File**, um Ihr Template hochzuladen.

![Dyspatch-Template exportieren]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Wählen Sie nicht **Inline CSS** im Abschnitt **Sending Info** für Dyspatch-E-Mail-Templates in Braze aus. Dyspatch übernimmt dies und sorgt dafür, dass Ihre E-Mails stabil, responsiv und versandfertig sind.
{% endalert %}

### Nutzung {#usage}

Sie finden Ihr hochgeladenes Dyspatch-Template in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail-Templates**. Sie können dieses E-Mail-Template jetzt verwenden, um ansprechende E-Mail-Nachrichten an Ihre Kund:innen zu versenden!