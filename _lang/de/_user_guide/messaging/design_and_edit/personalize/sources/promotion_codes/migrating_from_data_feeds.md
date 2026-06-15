---
nav_title: Migration von Daten-Feeds
article_title: Migration von Daten-Feeds zu Aktionscodes
page_order: 10
description: "Dieser Referenzartikel bietet eine Anleitung zur Migration von Daten-Feeds zu Aktionscodes."
---

# Migration von Daten-Feeds zu Aktionscodes {#migrate-from-data-feeds-to-promotion-codes}

> Diese Seite führt Sie durch die Migration von Daten-Feeds zu Aktionscodes. Es handelt sich um einen unkomplizierten Prozess, bei dem Sie manuell Aktionscode-Listen mit den Informationen aus Ihren Daten-Feeds erstellen und Ihre Nachrichtenreferenzen entsprechend aktualisieren.

{% alert note %}
Daten-Feeds werden eingestellt. Braze empfiehlt Kund:innen, die Daten-Feeds verwenden, auf Aktionscode-Listen umzusteigen.
{% endalert %}

## Features und Funktionalität {#features-and-functionality}

Es gibt einige Unterschiede zwischen Aktionscode-Listen und Daten-Feeds.

| Feature          | Aktionscodes | Daten-Feeds   |
|------------------|-----------------|--------------|
| Beschreibungen     | Ja             | Nein           |
| Ablaufdaten | Ja             | Nein           |
| Erstellungsmethode  | Hochladen einer CSV | Text einfügen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Features und Funktionalität" }

## So migrieren Sie {#how-to-migrate}

Um einen Daten-Feed durch eine Aktionscode-Liste zu ersetzen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** und wählen Sie **Aktionscode-Liste erstellen** aus.
2. [Richten Sie Ihre Aktionscode-Liste ein]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/).
3. Navigieren Sie zu Ihren Nachrichten, die zuvor den Daten-Feed referenziert haben, und aktualisieren Sie diese, um die Aktionscode-Liste zu verwenden.