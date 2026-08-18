---
nav_title: Übersetzungsansätze vergleichen
article_title: Ansätze für die Verwaltung mehrsprachiger Übersetzungen vergleichen
page_order: 1
page_type: reference
description: "Vergleichen Sie manuelles Liquid, Content Blocks, Kataloge, mehrsprachige Nachrichten, Übersetzungspartner und Connected Content, um zu entscheiden, wie Kitchenerie lokalisierte Texte verwaltet."
tool:
  - Campaigns
  - Canvas
---

# Ansätze für die Verwaltung mehrsprachiger Übersetzungen vergleichen {#compare-approaches-for-managing-multi-language-translations}

> Bewerten Sie, wie lokalisierte Texte gespeichert, aktualisiert, in der Vorschau angezeigt und versendet werden, damit Sie einen Lokalisierungsansatz wählen können, der zu Ihrem QA-Workflow, Ihrem Kanalmix und Ihrer Aktualisierungshäufigkeit passt.

## Über dieses Beispiel {#about-this-example}

Kitchenerie, ein Einzelhändler für Küchenartikel, versendet E-Mails, Push-Nachrichten und In-App-Nachrichten auf Englisch, Französisch und Deutsch. Marketing und Engineering benötigen einen wiederholbaren, skalierbaren Weg, um Übersetzungen über Kampagnen hinweg zu verwalten.

Braze unterstützt mehrere Lokalisierungsmuster:

- **Manuelles bedingtes Liquid:** Text wird pro Sprache im Nachrichtentext eingegeben
- **Content Blocks:** Wiederverwendbare Blöcke (mit oder ohne mehrsprachige Übersetzungs-Tags)
- **Kataloge:** Strukturierte Übersetzungszeilen, die nach Gebietsschema geschlüsselt sind
- **Mehrsprachige Nachrichten:** Übersetzungs-Tags, CSV-Uploads und die Übersetzungs-API (Early Access)
- **Übersetzungspartner:** Smartling, Phrase, Lokalise und andere
- **Connected Content:** Lokalisierte Strings, die zur Sendezeit von Ihrem CMS oder Ihrer API abgerufen werden

Dieses Beispiel vergleicht die Vor- und Nachteile, damit Sie einen Ansatz an Ihren QA-Workflow, Kanalmix, Ihre Aktualisierungshäufigkeit und Teamressourcen anpassen können. Es ersetzt keine Schritt-für-Schritt-Einrichtung für eine einzelne Methode. Für Feature-Walkthroughs beginnen Sie mit [Lokalisierung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) und [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Überlegungen {#considerations}

- Entscheiden Sie, ob Sie Dashboard-Vorschau und QA, professionelle Übersetzungsworkflows, häufige Inhaltsaktualisierungen oder Realtime-CMS-gesteuerte Texte benötigen, bevor Sie ein Muster wählen.
- [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) unterstützen E-Mail, Push, Banner, In-App-Nachrichten und Content Blocks. Beachten Sie, dass SMS und WhatsApp andere Lokalisierungsmuster verwenden. Manuelles Liquid, Content Blocks, Kataloge, Partner und Connected Content können kanalübergreifend eingesetzt werden, wo diese Features unterstützt werden.
- Braze generiert keine Übersetzungen. Sie liefern Texte über das Dashboard, CSV, API, Katalogimport, Partner-Workflow oder externes CMS.
- Manuelles Liquid und Content Blocks mit eingebetteten Bedingungen erfordern Namenskonventionen und Überprüfungsprozesse, wenn die Anzahl der Sprachen wächst, und mehrsprachige sowie Partner-Workflows zentralisieren Aktualisierungen, erfordern aber möglicherweise CSV- oder API-Pflege.
- Connected Content und einige Partner-Flows hängen von externen Systemen ab. Wenn eine API oder ein CMS zur Sendezeit nicht verfügbar ist, kann lokalisierter Inhalt möglicherweise nicht geladen werden.
- Überschneidungen sind üblich. Beispielsweise können Sie mehrsprachige Tags für E-Mail-Texte, Content Blocks für gemeinsame Fußzeilen und Kataloge für Produkttexte im selben Programm verwenden.

## Einrichtung {#setup}

### Schritt 1: Erfassen Sie Ihre Lokalisierungsanforderungen {#step-1-capture-your-localization-requirements}

| Anforderung | Zu beantwortende Fragen |
| --- | --- |
| Vorschau und QA | Müssen Marketer jedes Gebietsschema im Braze-Composer vor dem Versand in der Vorschau anzeigen? |
| Skalierung | Wie viele Sprachen gibt es und wie oft ändert sich der Text? |
| Workflow | Benötigen Sie Überprüfung, Revisionen und Freigaben durch Übersetzer:innen? |
| Datenstruktur | Handelt es sich um freiformatigen Marketingtext oder strukturierte Produktfelder (Namen, Preise, URLs)? |
| Automatisierung | Sollen Übersetzungen automatisch aktualisiert werden, wenn sich Ihr CMS ändert? |
| Team-Kompetenzen | Kann Ihr Team Liquid, CSV-Uploads, APIs oder Partnerintegrationen pflegen? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erfassen Sie Ihre Lokalisierungsanforderungen" }

### Schritt 2: Ansätze auf einen Blick vergleichen {#step-2-compare-approaches-at-a-glance}

| Dimension | Manuelles Liquid | Content Blocks | Kataloge | Mehrsprachige Nachrichten | Übersetzungspartner | Connected Content |
| --- | --- | --- | --- | --- | --- | --- |
| Dashboard-Vorschau / QA | Ja | Ja | Ja | Ja | Variiert je nach Partner | Eingeschränkt – abgerufene Inhalte sind schwerer in der Vorschau anzuzeigen |
| Standard (keine Integration) | Ja | Ja | Teilweise – Katalog-Einrichtung erforderlich | Ja | Nein – Anbieter-Einrichtung | Nein – API oder CMS erforderlich |
| Kanalabdeckung | Alle unterstützten Kanäle | Alle unterstützten Kanäle | Alle unterstützten Kanäle | E-Mail, Push, Banner, In-App-Nachrichten, Content Blocks | Variiert je nach Partner | Alle unterstützten Kanäle |
| Implementierungsaufwand | Niedrig | Niedrig–mittel | Mittel | Niedrig | Hoch (partnerabhängig) | Mittel |
| Laufender (BAU-)Aufwand | Hoch – Bearbeitungen pro Nachricht | Mittel – Block-Pflege | Mittel – CSV- oder API-Aktualisierungen | Mittel – CSV-Uploads | Mittel – in der Plattform verwaltet | Niedrig – zur Sendezeit abgerufen |
| Häufige Aktualisierungen | Nein | Teilweise | Nein | Teilweise | Ja | Ja |
| Professioneller Übersetzungsworkflow | Nein | Nein | Nein | Nein | Ja | Nein |
| Strukturierte / Produktdaten | Eingeschränkt | Eingeschränkt | Ja – ideal für geschlüsselte Texte | Eingeschränkt | Variiert | Ja – über externe Quelle |
| Risiko externer Abhängigkeiten | Keines | Keines | Keines | Keines | Mittel | Mittel – Versand schlägt fehl, wenn die Quelle nicht erreichbar ist |
| Am besten geeignet für | Wenige Sprachen, seltene Aktualisierungen | Gemeinsame Komponenten über Nachrichten hinweg | Viele Gebietsschemata mit strukturierten Strings | Viele Sprachen mit geringerem Copy-Paste-Aufwand | Enterprise-Übersetzung mit Freigaben | Dynamische CMS-gesteuerte Lokalisierung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Ansätze auf einen Blick vergleichen" }

### Schritt 3: Kitchenerie-Szenarien einem Ansatz zuordnen {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Kitchenerie-Szenario | Empfohlener Ausgangspunkt |
| --- | --- |
| Drei Sprachen, wenige Kampagnen pro Monat, kleines Marketing-Team | Manuelles bedingtes Liquid oder Content Blocks mit Liquid |
| Gemeinsame Kopfzeile, Fußzeile und rechtliche Blöcke über E-Mail und IAM hinweg | Content Blocks – mit [mehrsprachigen Übersetzungen, die im Block gespeichert werden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks), wenn die Anzahl der Gebietsschemata wächst |
| Produktnamen, Promo-Zeilen und Bild-URLs nach Gebietsschema geschlüsselt | [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| E-Mail und Push in acht oder mehr Gebietsschemata mit Composer-Vorschau | [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| Zentrales TMS mit Übersetzer-Workflow und Freigaben | [Lokalisierungspartner]({{site.baseurl}}/partners/message_personalization/localization) (zum Beispiel Smartling oder Phrase) |
| Texte, die in einem CMS verwaltet werden und sich täglich ändern | [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kitchenerie-Szenarien einem Ansatz zuordnen" }

### Schritt 4: Den gewählten Ansatz implementieren {#step-4-implement-the-approach-you-selected}

1. **Manuelles bedingtes Liquid:** Verwenden Sie Profil-Attribute wie `language` oder Gebietsschema mit `if` / `elsif` / `else` Liquid. Siehe [Alternative Ansätze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches) und [Bedingte Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
2. **Content Blocks:** Erstellen Sie wiederverwendbare Blöcke; optional können Sie bedingtes Liquid in Blöcken verbergen. Siehe [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) und den Tab „Content Blocks“ unter [Übersetzte Nachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
3. **Kataloge:** Importieren Sie Übersetzungszeilen (zum Beispiel `id`, `context`, `language`, `body`) und referenzieren Sie diese mit Liquid `catalog_items`. Siehe den Tab „Kataloge“ unter [Übersetzte Nachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
4. **Mehrsprachige Nachrichten:** [Fügen Sie Gebietsschemata hinzu]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), umschließen Sie Texte mit Übersetzungs-Tags und laden Sie dann eine CSV hoch. Wenn Sie Early Access zu den [Übersetzungsendpunkten]({{site.baseurl}}/api/endpoints/translations) haben, können Sie Übersetzungen stattdessen per API aktualisieren. Nutzen Sie die Vorschau mit **Multi-language user** im Composer.
5. **Übersetzungspartner:** Konfigurieren Sie Workspace-Gebietsschemata und folgen Sie dann Ihrer Partnerintegration (zum Beispiel [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling) oder [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)).
6. **Connected Content:** Rufen Sie Ihr CMS oder Ihre Übersetzungs-API zur Sendezeit auf. Testen Sie gründlich; die Vorschau spiegelt möglicherweise nicht die Live-API-Antworten wider. Siehe [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

Informationen zur Canvas- und Campaign-Orchestrierung über Regionen hinweg (eine Journey versus eine Journey pro Land) finden Sie unter [Übersetzungsverwaltung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management) auf der Lokalisierungsseite.

## Verwandte Artikel {#related-articles}

- [Lokalisierung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Lokalisierungseinstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Lokalisierungspartner]({{site.baseurl}}/partners/message_personalization/localization)
- [Barrierefreiheitssprache für lokalisierte Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)