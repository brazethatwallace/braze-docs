---
nav_title: Übersicht
page_order: 0
noindex: true
---

# Beispiel-Layout: Übersicht

> Das Übersichtslayout eignet sich gut, um eine spezielle Navigationsoption am oberen Rand einer Seite zu erstellen, die es Nutzer:innen ermöglicht, durch Klicken auf einen Button zu einem bestimmten Teil einer Seite oder zu einer ganz anderen Seite zu gelangen.

Klassische Beispiele für das Selektor-Layout sind die Seite [SDK or Software-Development-Kit Changelogs]({{site.baseurl}}/developer_guide/changelogs) oder die Seite [Kreative Details für In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types).

## Erforderliche Komponenten

1. YAML-Anfangs- und Endmarkierung. Das heißt, --- vor dem Inhalt und --- danach.
2. Anführungszeichen um bestimmte Parameterinhalte. (Header-Parameter, Textparameter, Inhalte mit Bindestrichen oder anderen Sonderzeichen.)
3. Glossary-Tags-Notation (Dies sind Filter-Tags)

## Erforderliche Parameter

| Parameter | Inhaltstyp | Details |
|---|---|---|
| `page_order` | Numerisch | Ordnet die Seite innerhalb des Abschnitts an. Diese Reihenfolge wird in der linken Navigation widergespiegelt. |
| `nav-title` | Alphanumerisch | Titel, der in der linken Navigation angezeigt wird. |
| `layout` | Alphanumerisch – Keine Leerzeichen | Wählen Sie ein Layout aus dem [Layout-Bereich](https://github.com/Appboy/braze-docs/tree/develop/_layouts) der Dokumentation aus. |
| `guide_top_header` | Alphanumerisch | Vergeben Sie einen Titel für Ihre Seite. |
| `guide_top_text` | Alphanumerisch | Beschreiben Sie Ihre Seite. Dieser Text wird direkt über den Buttons und deren Titel angezeigt. Der Inhalt muss in Anführungszeichen stehen. |
| `guide_featured_title` | Alphanumerisch | Vergeben Sie einen Titel für Ihre Karten. Dieser wird direkt über den Buttons angezeigt. |
| `guide_featured_list` | Weiteres YAML, Alphanumerisch | Siehe [Format für Guide-Auflistung](#guide-listing-format) unten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erforderliche Parameter" }

### Format für Guide-Auflistung {#guide-listing-format}

| Parameter | Inhaltstyp | Details |
|---|---|---|
| `name` | Alphanumerisch | Benennen Sie die Box. |
| `link` | URL oder Pfad | Link zum Ziel der Box. Muss eine vollständige URL oder (bei einem internen Link) `/docs...` enthalten. |
| `image` | Pfad | Link zum Speicherort des Bildes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Format für Guide-Auflistung" }

Formatbeispiel:

```yaml
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

```yaml
---
nav_title: Kreative Details
page_order: 4
layout: featured
guide_top_header: "Kreative Details"
guide_top_text: "Werden Sie kreativ mit unseren In-App-Nachrichten! Aber Sie sollten zuerst einige Richtlinien kennen! Schließlich müssen Sie die Regeln kennen, um sie zu brechen! Sehen Sie sich die kreativen Spezifikationen der einzelnen Nachrichtentypen oder die allgemeinen kreativen Details unten an."

guide_featured_title: "Kreative Spezifikationen nach Nachrichtentyp"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/channels/in_app_messages/message_types/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Vollbild
  link: /docs/user_guide/channels/in_app_messages/message_types/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Kreative Details {#general}

In-App-Nachrichten von Braze verfügen sowohl über allgemeine als auch über individuelle kreative Spezifikationen. Weitere Informationen zu unseren stärker anpassbaren In-App-Nachrichtentypen finden Sie auf unserer Seite [Anpassen]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% alert important %}
  Diese Details gelten nur für unsere neueste In-App-Nachrichten-Generation (Generation 3). Wenn Sie nicht unsere neueste Generation von In-App-Nachrichten verwenden, lesen Sie unsere Dokumentation zu [früheren In-App-Nachrichten-Generationen]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/).
{% endalert %}