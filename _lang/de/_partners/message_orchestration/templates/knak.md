---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Knak, einer Plattform zur Erstellung von Kampagnen, die es Ihnen ermöglicht, vollständig responsive E-Mails in Minuten oder Stunden statt in Tagen oder Wochen zu erstellen und diese als gebrauchsfertige Braze Templates zu exportieren."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) ist die erste Plattform zur Erstellung von Kampagnen, die für den internen Einsatz in Marketing-Teams von Unternehmen entwickelt wurde. Mit der Drag-and-Drop-Plattform kann jeder in wenigen Minuten ansprechende, markenkonforme E-Mails und Landing-Pages erstellen – ganz ohne Programmieraufwand oder externe Hilfe.

_Diese Integration wird von Knak gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Knak ermöglicht es Ihnen, vollständig responsive E-Mails in Minuten oder Stunden statt in Tagen oder Wochen zu erstellen und sie als gebrauchsfertige Braze Templates zu exportieren. Knak wurde für Marketer entwickelt, die ihre E-Mail-Erstellung für Campaigns, die in Braze verwaltet werden, verbessern möchten – ohne externe Agenturen oder manuelles Programmieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Knak-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Knak-Konto. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit vollständigen **Templates**-Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Knak wurde für Marketer entwickelt, die ihre E-Mail-Erstellung verbessern möchten – ganz ohne Code oder externe Hilfe. Es ist ideal für alle, die:
- Derzeit einfache Templates für E-Mails verwenden und diese aufwerten möchten
- Sich auf externe Agenturen oder Entwickler:innen verlassen, um E-Mails für Braze zu erstellen
- Die kreative Kontrolle über die Asset-Erstellung zurückgewinnen und deutlich schneller auf den Markt kommen möchten

## Integration

### 1. Schritt: Integration konfigurieren {#step-1-configure-your-integration}

Navigieren Sie in Knak zu **Integrations > Platforms > + Add New Integration**.

![Button „Integration hinzufügen“]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

Wählen Sie als Nächstes die Plattform **Braze** aus und geben Sie den Braze-API-Schlüssel sowie den REST-Endpunkt ein. Klicken Sie auf **Create New Integration**, um Ihre Integration abzuschließen.

![Neue Integration erstellen]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### 2. Schritt: Knak Templates synchronisieren {#step-2-sync-your-knak-templates}

Suchen Sie in Knak eine E-Mail, die Sie mit Braze synchronisieren möchten, und wählen Sie **Publish** und dann **Sync**.

![Knak-Integration 1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

Überprüfen Sie anschließend den Namen der E-Mail und klicken Sie auf **Sync**.

![Knak-Integration 2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## Verwendung der Integration {#using-the-integration}

Sie finden Ihre hochgeladenen Knak-E-Mails in Braze unter **Engagement > Templates & Media**. Sie werden ansprechend, markenkonform und vollständig responsiv sein. Die einzige Grenze ist Ihre eigene Kreativität!