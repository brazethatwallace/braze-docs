---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Phrase, einer cloudbasierten Software für die Lokalisierung. Diese Integration erlaubt es Ihnen, E-Mail-Templates und Content Blocks zu übersetzen, ohne die Braze-Schnittstelle zu verlassen."
page_type: partner
search_tag: Partner

---

# Phrase

> [Phrase](https://phrase.com/) ist eine cloudbasierte Software zur Verwaltung der Lokalisierung. Phrase ermöglicht automatisierte Übersetzungsworkflows und unterstützt die kontinuierliche Lokalisierung für agile Teams.

_Diese Integration wird von Phrase gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Phrase und Braze erlaubt es Ihnen, E-Mail-Templates und Content Blocks zu übersetzen, ohne die Braze-Schnittstelle zu verlassen. Mit der Phrase-TMS-Integration für Braze können Sie das Customer-Engagement steigern und das Wachstum in neuen Märkten mit nahtloser Lokalisierung vorantreiben.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Phrase-TMS-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Phrase TMS Ultimate- oder Enterprise-Konto. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit allen Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

## 1. Schritt: Phrase-TMS-Einstellungen {#step-1-phrase-tms-settings}

Navigieren Sie in Phrase zu **Settings > Integrations > Connectors > New**.

1. Geben Sie einen Namen für die Verbindung ein und ändern Sie den Typ in **Braze**.<br><br>
2. Geben Sie den Representational State Transfer-API-Schlüssel und den Braze-Representational State Transfer-Endpunkt ein. <br><br>
3. Wählen Sie aus, wie der Konnektor E-Mail-Templates mit verknüpften Content Blocks importieren soll.
- Nur ausgewähltes E-Mail-Template
- Content Blocks einbinden<br><br>
4. Wählen Sie aus, wie der Konnektor Übersetzungen von E-Mail-Templates exportieren soll.
- Neuen Artikel erstellen
- Originalartikel
  - Der Originalartikel exportiert Übersetzungen in dasselbe Template/denselben Block. Sprachsegmente werden durch das angegebene Attribut definiert.<br><br>
    {% raw %}
    Geben Sie das Sprachattribut an, wenn der Originalartikel ausgewählt ist. Das Sprachattribut definiert die Sprache des if/elsif-Arguments. Wenn Sie die Option für den Originalartikel verwenden, muss die Struktur wie unten dargestellt aufgebaut sein:

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    Oder Sie verwenden die Abbildung Schlüssel/Werte zuweisen:
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    Das obige Liquid muss strikt befolgt werden, aber das Sprachattribut sowie Sprache, Schlüssel und Werte sind anpassbar.<br><br>
    Jeder Sprachcode kann nur einmal verwendet werden. Für ein Segment können jedoch mehrere Sprachen verwendet werden, zum Beispiel:
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Klicken Sie auf **Test connection**. Wenn die Verbindung erfolgreich ist, erscheint ein Häkchen. Bewegen Sie den Mauszeiger über das Symbol, um weitere Details zu sehen.<br><br>
7. Klicken Sie abschließend auf **Save**. Dieser Konnektor wird auf der Seite **Connectors** verfügbar sein.

## 3. Schritt: Inhalte an Phrase senden und zurück nach Braze exportieren {#step-3-send-content-to-phrase-and-export-back-to-braze}

1. Richten Sie zunächst das [Portal für Einreicher](https://support.phrase.com/hc/en-us/articles/5709602111132) ein, damit diese den Anfragen direkt aus dem Online-Repository Dateien hinzufügen können.<br><br>
2. Verwenden Sie die [automatische Projekterstellung (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356), damit Phrase TMS automatisch neue Projekte erstellt, wenn eine Änderung in den angegebenen Workflow-Status erkannt wird.<br><br>
3. Ausgewählte Inhalte werden bei der ersten Ausführung von APC importiert.

Die [Konnektor-API](https://cloud.memsource.com/web/docs/api#) kann Schritte automatisieren, die sonst manuell über die UI ausgeführt werden. Mit [Webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) kann Phrase TMS Systeme von Drittanbietern über bestimmte Ereignisse benachrichtigen (z. B. eine Änderung des Auftragsstatus).