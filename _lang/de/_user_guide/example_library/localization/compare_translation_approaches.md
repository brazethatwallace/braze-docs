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

Kitchenerie, ein fiktiver Küchenausstattungs-Einzelhändler, versendet E-Mails, Push-Nachrichten und In-App-Nachrichten auf Englisch, Französisch und Deutsch. Marketing und Engineering benötigen einen wiederholbaren, skalierbaren Weg, um Übersetzungen über Campaigns hinweg zu verwalten.

Braze unterstützt mehrere Lokalisierungsmuster:

- **Manuelles bedingtes Liquid:** Pro Sprache eingegebener Text im Nachrichtentext
- **Content Blocks:** Wiederverwendbare Blöcke (mit oder ohne Multi-Language-Übersetzungs-Tags)
- **Kataloge:** Strukturierte Übersetzungszeilen, die nach Gebietsschema zugeordnet sind
- **Multi-Language-Nachrichten:** Übersetzungs-Tags, CSV-Uploads und die Übersetzungs-API (Early Access)
- **Übersetzungspartner:** Smartling, Phrase, Lokalise und andere
- **Connected Content:** Lokalisierte Strings, die zur Sendezeit von Ihrem CMS oder Ihrer API abgerufen werden

Dieses Beispiel vergleicht die jeweiligen Vor- und Nachteile, damit Sie einen Ansatz finden, der zu Ihrem QA-Workflow, Ihrem Kanalmix, Ihrer Aktualisierungshäufigkeit und Ihren Team-Ressourcen passt. Es ersetzt nicht die Schritt-für-Schritt-Einrichtung für eine einzelne Methode. Für Feature-Walkthroughs beginnen Sie mit [Lokalisierung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) und [Multi-Language-Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Überlegungen {#considerations}

- Entscheiden Sie, ob Sie Dashboard-Vorschau und QA, professionelle Übersetzungsworkflows, häufige Inhaltsaktualisierungen oder Realtime-CMS-gesteuerte Texte benötigen, bevor Sie sich für ein Muster entscheiden.
- [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) unterstützen E-Mail, Push, Banner, In-App-Nachrichten und Content Blocks. Beachten Sie, dass SMS und WhatsApp andere Lokalisierungsmuster verwenden. Manuelles Liquid, Content Blocks, Kataloge, Partner und Connected-Content können kanalübergreifend eingesetzt werden, sofern diese Features unterstützt werden.
- Braze generiert keine Übersetzungen. Sie stellen Texte über das Dashboard, CSV, API, Katalogimport, Partner-Workflow oder ein externes CMS bereit.
- Manuelles Liquid und Content Blocks mit eingebetteter bedingter Logik erfordern Namenskonventionen und Überprüfungsprozesse, wenn die Anzahl der Sprachen wächst. Mehrsprachige und Partner-Workflows zentralisieren Aktualisierungen, können jedoch CSV- oder API-Pflege erfordern.
- Connected-Content und einige Partner-Flows sind von externen Systemen abhängig. Wenn eine API oder ein CMS zum Sendezeitpunkt nicht verfügbar ist, können lokalisierte Inhalte möglicherweise nicht geladen werden.
- Überschneidungen sind üblich. Beispielsweise können Sie in demselben Programm mehrsprachige Tags für E-Mail-Texte, Content Blocks für gemeinsame Fußzeilen und Kataloge für Produkttexte verwenden.

## Einrichtung {#setup}

### Schritt 1: Lokalisierungsanforderungen erfassen {#step-1-capture-your-localization-requirements}

| Anforderung | Zu beantwortende Fragen |
| --- | --- |
| Vorschau und QA | Müssen Marketer jede Locale im Braze-Composer vor dem Versand in der Vorschau prüfen? |
| Skalierung | Wie viele Sprachen gibt es und wie oft ändert sich der Text? |
| Workflow | Benötigen Sie Überprüfung, Überarbeitung und Freigabe durch Übersetzer:innen? |
| Datenstruktur | Handelt es sich um freiformatigen Marketingtext oder strukturierte Produktfelder (Namen, Preise, URLs)? |
| Automatisierung | Sollen Übersetzungen automatisch aktualisiert werden, wenn sich Ihr CMS ändert? |
| Team-Kompetenzen | Kann Ihr Team Liquid, CSV-Uploads, APIs oder Partnerintegrationen pflegen? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lokalisierungsanforderungen erfassen" }

### Schritt 2: Ansätze im Überblick vergleichen {#step-2-compare-approaches-at-a-glance}

| Dimension | Manuelles Liquid | Content Blocks | Kataloge | Mehrsprachige Nachrichten | Übersetzungspartner | Connected Content |
| --- | --- | --- | --- | --- | --- | --- |
| Dashboard-Vorschau / QA | Ja | Ja | Ja | Ja | Variiert je nach Partner | Eingeschränkt – schwieriger, abgerufene Inhalte in der Vorschau anzuzeigen |
| Standard (keine Integration) | Ja | Ja | Teilweise – Katalog-Einrichtung erforderlich | Ja | Nein – Anbieter-Einrichtung | Nein – API oder CMS erforderlich |
| Kanalabdeckung | Alle unterstützten Kanäle | Alle unterstützten Kanäle | Alle unterstützten Kanäle | E-Mail, Push, Banner, In-App-Nachrichten, Content Blocks | Variiert je nach Partner | Alle unterstützten Kanäle |
| Implementierungsaufwand | Niedrig | Niedrig–mittel | Mittel | Niedrig | Hoch (partnerabhängig) | Mittel |
| Laufender Aufwand (BAU) | Hoch – Bearbeitungen pro Nachricht | Mittel – Block-Pflege | Mittel – CSV- oder API-Aktualisierungen | Mittel – CSV-Uploads | Mittel – in der Plattform verwaltet | Niedrig – wird zum Sendezeitpunkt abgerufen |
| Häufige Aktualisierungen | Nein | Teilweise | Nein | Teilweise | Ja | Ja |
| Professioneller Übersetzungsworkflow | Nein | Nein | Nein | Nein | Ja | Nein |
| Strukturierte / Produktdaten | Eingeschränkt | Eingeschränkt | Ja – ideal für schlüsselbasierte Texte | Eingeschränkt | Variiert | Ja – über externe Quelle |
| Risiko externer Abhängigkeiten | Keines | Keines | Keines | Keines | Mittel | Mittel – Versand schlägt fehl, wenn die Quelle nicht erreichbar ist |
| Am besten geeignet für | Wenige Sprachen, seltene Aktualisierungen | Gemeinsam genutzte Komponenten über Nachrichten hinweg | Viele Locales mit strukturierten Strings | Viele Sprachen mit geringerem Copy-Paste-Aufwand | Unternehmensweite Übersetzung mit Freigaben | Dynamische CMS-gesteuerte Lokalisierung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Ansätze im Überblick vergleichen" }

### Schritt 3: Kitchenerie-Szenarien einem Ansatz zuordnen {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Kitchenerie-Szenario | Empfohlener Ausgangspunkt |
| --- | --- |
| Drei Sprachen, wenige Campaigns pro Monat, kleines Marketing-Team | Manuelles bedingtes Liquid oder Content Blocks mit Liquid |
| Gemeinsamer Header, Fußzeile und rechtliche Blöcke über E-Mail und IAM hinweg | Content Blocks – mit [mehrsprachigen Übersetzungen, die im Block gespeichert werden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks), wenn die Anzahl der Locales wächst |
| Produktnamen, Promo-Texte und Bild-URLs nach Locale geschlüsselt | [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| E-Mail und Push in acht oder mehr Locales mit Composer-Vorschau | [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| Zentrales TMS mit Übersetzer-Workflow und Freigaben | [Lokalisierungspartner]({{site.baseurl}}/partners/message_personalization/localization) (zum Beispiel Smartling oder Phrase) |
| Texte in einem CMS, das täglich aktualisiert wird | [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kitchenerie-Szenarien einem Ansatz zuordnen" }

### Schritt 4: Den gewählten Ansatz implementieren {#step-4-implement-the-approach-you-selected}

1. **Manuelles bedingtes Liquid:** Verwenden Sie Profil-Attribute wie `language` oder Locale mit `if` / `elsif` / `else` in Liquid. Siehe [Alternative Ansätze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches) und [Bedingte Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
2. **Content Blocks:** Erstellen Sie wiederverwendbare Blöcke; optional können Sie bedingtes Liquid in Blöcken verbergen. Siehe [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) und den Tab „Content Blocks“ unter [Übersetzte Nachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
3. **Kataloge:** Importieren Sie Übersetzungszeilen (zum Beispiel `id`, `context`, `language`, `body`) und referenzieren Sie diese mit Liquid `catalog_items`. Siehe den Tab „Kataloge“ unter [Übersetzte Nachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
4. **Mehrsprachige Nachrichten:** [Fügen Sie Locales hinzu]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), umschließen Sie Texte mit Übersetzungs-Tags und laden Sie dann eine CSV hoch. Wenn Sie frühzeitigen Zugang zu den [Übersetzungsendpunkten]({{site.baseurl}}/api/endpoints/translations) haben, können Sie Übersetzungen stattdessen per API aktualisieren. Nutzen Sie die Vorschau mit **Multi-language user** im Composer.
5. **Übersetzungspartner:** Konfigurieren Sie Workspace-Locales und folgen Sie dann Ihrer Partnerintegration (zum Beispiel [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling) oder [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)).
6. **Connected Content:** Rufen Sie Ihr CMS oder Ihre Übersetzungs-API zum Sendezeitpunkt auf. Testen Sie gründlich; die Vorschau spiegelt möglicherweise nicht die Live-API-Antworten wider. Siehe [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

Informationen zur Canvas- und Campaign-Orchestrierung über Regionen hinweg (eine Journey versus eine Journey pro Land) finden Sie unter [Übersetzungsmanagement]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management) auf der Lokalisierungsseite.

## Verwandte Artikel {#related-articles}

- [Lokalisierung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Lokalisierungseinstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Lokalisierungspartner]({{site.baseurl}}/partners/message_personalization/localization)
- [Barrierefreiheitssprache für lokalisierte Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)