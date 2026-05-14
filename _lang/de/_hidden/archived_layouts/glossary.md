---
nav_title: Glossar
article_title: Glossar-Layout
page_order: 0
noindex: true
---

# Beispiel-Layout: Glossar {#example-layout-glossary}

> Das Glossar-Layout ist in YAML verfasst. Es erfordert mehrere Komponenten und Parameter. Glossar-Layouts eignen sich gut für lokalisierte, durchsuchbare Inhalte wie Wörterbücher und bestimmte Inhaltskategorien.

## Erforderliche Komponenten {#required-components}

1. YAML-Notation für Öffnungen und Schließungen. Mit anderen Worten: `---` vor dem Inhalt und `---` danach.
2. Anführungszeichen um bestimmte Parameterinhalte. (Header-Parameter, Textparameter, Inhalte mit Bindestrichen oder anderen Sonderzeichen.)
3. Glossar-Tags-Notation (Dies sind Filter-Tags)

## Erforderliche Parameter {#required-parameters}

| Parameter | Inhaltstyp | Details |
|---|---|---|
| `page_order` | Numerisch | Ordnen Sie die Seite innerhalb des Abschnitts. Diese Reihenfolge wird in der linken Navigation angezeigt. |
| `nav-title` | Alphanumerisch | Titel, der in der linken Navigation erscheint. |
| `layout` | Alphanumerisch – Keine Leerzeichen | Wählen Sie ein Layout aus dem [Layout-Abschnitt](https://github.com/Appboy/braze-docs/tree/develop/_layouts) der Dokumentation aus. |
| `glossary_top_header` | Alphanumerisch | Erfordert doppelte Anführungszeichen. Der Titel erscheint oben auf der Seite. |
| `glossary_top_text` | String, Alphanumerisch | Beschreiben Sie Ihre Glossarseite. Dies erscheint über der Suchleiste und den Filtern (falls Sie diese aktiviert haben). Dies ist im Wesentlichen in HTML geschrieben, sodass Sie ```<br>``` verwenden können, um Zeilenumbrüche zu erstellen. |
| `glossary_tag_name` | Einzelnes Wort, Alphanumerisch | Benennen Sie Ihre Filter. Diese erscheinen in Kontrollkästchen unterhalb der Suchleiste sowie in den Daten darunter. |
| `glossary_filter_text` | String, Alphanumerisch | Beschreiben Sie Ihre Filter. Wird in der Regel zur Anleitung verwendet. |
| `glossary_tags` | Weiteres YAML plus Inhalt. | Format wie unten gezeigt: <br> glossary_tags: <br>  - name: Content Cards <br>  - name: Email |
| `glossaries` | Weiteres YAML plus Inhalt. | Siehe [Glossar-Parameter](#glossaries-parameters) unten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Required Parameters" }

### Glossar-Parameter {#glossaries-parameters}

| Parameter | Inhaltstyp | Details |
|---|---|---|
| `name` | Alphanumerisch | Benennen Sie Ihren Glossar-Artikel. |
| `description` | String, Alphanumerisch | Beschreiben Sie Ihren Glossar-Artikel. |
| `calculation` | String | (optional) Beschreiben Sie, wie Ihr Glossar-Artikel berechnet wird (wird normalerweise bei der Beschreibung von Daten oder Metriken verwendet). |
| `tags` | Alphanumerisch | Sollte mit dem übereinstimmen, was als `name` unter `glossary_tags` aufgeführt ist. Führen Sie so viele auf, wie zutreffend sind. Wenn Sie `All` schreiben, wird der Artikel in alle Filter aufgenommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Glossaries Parameters" }

## Beispiel {#example}

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
