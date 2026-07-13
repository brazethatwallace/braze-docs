---
nav_title: Liquid-Referenz
article_title: Liquid-Referenz
page_order: 3
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Liquid-Referenz"
guide_top_text: "Liquid ist eine Open-Source-Template-Sprache, die von Shopify entwickelt und von Braze für dynamische Personalisierung eingesetzt wird. Anstatt allen dieselbe statische Nachricht zu senden, können Sie mit Liquid Templates erstellen, deren Inhalt sich basierend auf den spezifischen Profildaten, dem Verhalten oder der Sprache der jeweiligen Empfänger:innen anpasst."
description: "Diese Landing-Page behandelt alles rund um Liquid, z. B. unterstützte Personalisierungs-Tags, Filter, das Festlegen von Standardwerten und mehr."

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
- name: Liquid verwenden
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid
  image: /assets/img/braze_icons/beaker-02.svg
- name: Unterstützte Personalisierungs-Tags
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags
  image: /assets/img/braze_icons/tag-01.svg
- name: Operatoren
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/operators
  image: /assets/img/braze_icons/code-02.svg
- name: Filter
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/filters
  image: /assets/img/braze_icons/flag-02.svg
- name: Erweiterte Filter
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters
  image: /assets/img/braze_icons/settings-01.svg
- name: Standardwerte festlegen
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values
  image: /assets/img/braze_icons/table.svg
- name: Bedingte Messaging-Logik
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic
  image: /assets/img/braze_icons/columns-01.svg
- name: Nachrichten abbrechen
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Liquid-Anwendungsfälle
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases
  image: /assets/img/braze_icons/list.svg
- name: Tutorials
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/tutorials
  image: /assets/img/braze_icons/book-open-01.svg
- name: Häufig gestellte Fragen
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/faq
  image: /assets/img/braze_icons/annotation-question.svg

---

## Über Liquid {#about-liquid}

Liquid fungiert als Brücke zwischen Ihrer Nachricht und Ihren Nutzerdaten. Wenn Sie eine Nachricht senden, durchsucht Braze den Text nach Liquid-Syntax. Sobald Liquid gefunden wird, werden die relevanten Daten für die jeweilige Nutzer:in abgerufen und der Code durch den tatsächlichen Wert ersetzt, bevor die Nachricht gesendet wird.

Sie können beispielsweise ein angepasstes Attribut aus einem Nutzerprofil abrufen, das ein ganzzahliger Datentyp ist, und diesen Wert auf die nächste ganze Zahl runden. Weitere Informationen zur Liquid-Syntax und -Verwendung finden Sie unter [**Unterstützte Personalisierungs-Tags**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Die Liquid-Template-Sprache unterstützt die Verwendung von Objekten, Tags und Filtern.

- [**Objekte**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ermöglichen es Ihnen, personalisierte Attribute in Ihre Nachrichten einzufügen.
- [**Tags**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) ermöglichen es Ihnen, Daten in Nachrichten einzufügen und bedingte Logik zu verwenden, um Nachrichten zu senden, wenn bestimmte Bedingungen erfüllt sind. Sie können Tags beispielsweise nutzen, um intelligente Logik wie „if“-Anweisungen in Ihre Campaigns einzubauen.
- [**Filter**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters) ermöglichen es Ihnen, personalisierte Attribute und dynamischen Content umzuformatieren. Sie könnten beispielsweise den [`date`-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter) verwenden, um einen Zeitstempel wie *2016-09-07 08:43:50 UTC* in ein Datum wie *7. September 2016* umzuwandeln.

{% alert warning %}
Braze unterstützt derzeit nicht 100 % von Shopifys Liquid, sondern nur bestimmte Teile, die wir in unserer Dokumentation beschrieben haben. Wir empfehlen dringend, alle Nachrichten mit Liquid vor dem Versand zu testen, um das Risiko von Fehlern oder der Verwendung von nicht unterstütztem Liquid zu minimieren.
{% endalert %}

### Liquid-5-Unterstützung {#liquid-5-support}

Braze unterstützt Liquid bis einschließlich **Liquid 5 von Shopify**. Die Liquid-Implementierung unterstützt Syntax-Personalisierungs-Tag-Typen und Whitespace-Kontrolle. Weitere Informationen zu bestimmten Tags finden Sie unter [Syntax-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#syntax-tags).

Die folgenden neuen Array- und mathematischen Filter stehen Ihnen in Ihrem Liquid beim Erstellen Ihrer Nachrichten zur Verfügung.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

Definitionen finden Sie unter [Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters).

## Wichtige Begriffe {#terms-to-know}

Diese Begriffe sind basierend auf unserem Unterstützungsumfang aus der [**Shopify-Dokumentation**](https://shopify.github.io/liquid/basics/introduction/) abgeleitet.

{% raw %}

| Begriff | Definition | Beispiel |
|---|---|---|
| Liquid | Eine weit verbreitete, kundenorientierte Template-Sprache, die von Shopify erstellt und in Ruby geschrieben wurde und zum Laden und Abrufen dynamischer Inhalte verwendet wird. | `{{${first_name}}}` fügt den Vornamen einer Nutzer:in in eine Nachricht ein. |
| Objekt | Eine Bezeichnung für eine Variable und den Ort des beabsichtigten Variablennamens, die Liquid mitteilt, wo Inhalt in der Nachricht angezeigt werden soll. | `{{${city}}}` fügt den Ort einer Nutzer:in in eine Nachricht ein. |
| Tag für bedingte Logik | Wird verwendet, um Logik zu erstellen und den Fluss des Nachrichteninhalts zu steuern. In Braze werden Tags für bedingte Logik verwendet, um Ausnahmen und Varianten in Nachrichten basierend auf bestimmten, vordefinierten Kriterien zu erstellen. | ```{% if ${language} == 'en' %}``` triggert Ihre Nachricht auf eine bestimmte Weise, wenn eine Nutzer:in „Englisch“ als Sprache angegeben hat. |
| Filter | Werden verwendet, um die Ausgabe des Liquid-Objekts zu ändern, einzugrenzen oder umzuformatieren. Häufig werden sie für mathematische Operationen eingesetzt. | ```{{"Big Sale" | upcase}}``` bewirkt, dass die Wörter „Big Sale“ als „BIG SALE“ in der Nachricht erscheinen. |
| Operatoren | Werden in Nachrichten verwendet, um Abhängigkeiten oder Kriterien zu erstellen, die beeinflussen können, welche Nachricht Ihre Nutzer:in erhält. | Wenn eine Nutzer:in die definierten Kriterien in einer Nachricht mit `{% custom_attribute.${Total_Revenue} > 0%}` erfüllt, erhält sie die Nachricht. Andernfalls erhält sie eine andere festgelegte Nachricht (oder keine), je nachdem, was Sie eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wichtige Begriffe" }

{% endraw %}

<br>