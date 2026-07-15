---
nav_title: Kampagnen für aktive Nutzer:innen
article_title: Kampagnen für aktive Nutzer:innen
page_order: 0.5
page_type: tutorial
description: "Dieser Artikel beschreibt die Vorteile von Kampagnen für aktive Nutzer:innen im Braze-Dashboard und die Schritte, um eine solche Kampagne zu erstellen und einzurichten."
tool:
  - Campaigns

---

# Kampagnen für aktive Nutzer:innen {#active-user-campaigns}

> Identifizieren Sie Ihre aktiven Nutzer:innen, um maßgeschneiderte Kampagnen zu erstellen und diejenigen zu belohnen, die Ihre Plattform regelmäßig nutzen.

Bereits aktive Nutzer:innen Ihrer App anzusprechen, kann ein leistungsstarkes Mittel sein, um eine engagierte Gemeinschaft regelmäßiger App-Nutzer:innen aufzubauen. Ein wenig personalisierte Anerkennung Ihrer aktivsten Nutzer:innen kann diese zu begeisterten Botschaftern Ihrer App machen.

Sie können sich auch unseren [Braze-Lernkurs](https://learning.braze.com/quick-overview-segment-and-campaign-setup) zu Marketing-Strategien für E-Mail und empfohlene Lebenszyklus-Kampagnen ansehen!

## Aktive Nutzer:innen verstehen {#understanding-active-users}

Braze definiert eine:n „aktive:n Nutzer:in“ für einen bestimmten Zeitraum als jede:n Nutzer:in, die oder der in diesem Zeitraum eine Sitzung hatte.

Wenn eine Verbindung unterbrochen wird, werden die Sitzungsdaten lokal zwischengespeichert und hochgeladen, sobald die Netzwerkverbindung wiederhergestellt ist. Diese Sitzungen werden ebenfalls in die Anzahl der aktiven Nutzer:innen einbezogen. Wenn Ihre App einen Registrierungsprozess hat, zählt Braze außerdem alle Nutzer:innen als aktiv – ob registriert oder nicht registriert.

Wenn Sie Nutzer-IDs festlegen, um Nutzer:innen beim Einloggen zu identifizieren, werden neue Anmeldungen als separate aktive Nutzer:innen gezählt. Nutzer:innen, die über die API aktualisiert werden, werden ebenfalls als aktive Nutzer:innen in dem Zeitraum gezählt, in dem sie aktualisiert werden.

## Schritt 1: Ihre Top-Nutzer:innen identifizieren {#step-1-identifying-your-top-users}

Erstellen Sie mithilfe unserer Auswahl an Filtern ein Nutzer:innen-Segment, das Ihre treueste und beständigste Nutzerbasis umfasst. Das folgende Beispiel-Segment definiert die Top-Nutzer:innen.

![Beispielhafte Braze-Segment-Filter zur Definition einer Top-Nutzer:innen-Zielgruppe.]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

Außerdem müssen Sie dieses Segment nicht ständig aktualisieren, da Nutzer:innen, die in die Einschränkungen der Kampagne fallen oder diese verlassen, entsprechend angesprochen oder ausgeschlossen werden.

{% alert note %}
Das obige Beispiel segmentiert Nutzer:innen nach allgemeiner App-Nutzung. In den meisten Fällen wird die Gesamtheit der Filter, die zur Definition Ihres Top-Nutzer:innen-Segments benötigt werden, weitgehend von den Besonderheiten Ihrer App bestimmt.
{% endalert %}

## Schritt 2: Ihre Top-Nutzer:innen kontaktieren {#step-2-contact-your-top-users}

### Zeigen Sie Ihren Nutzer:innen Wertschätzung {#make-your-users-feel-appreciated}

Zeigen Sie Ihren Nutzer:innen Wertschätzung, indem Sie ihnen für ihre Treue und ihr Engagement für Ihre App danken. Geben Sie Ihren Nutzer:innen weitere Gründe, immer wieder zu Ihrer App zurückzukehren, um weitere Aktivität zu fördern. Dies kann in Form von Sonderangeboten oder Boni exklusiv für Ihre Top-Nutzer:innen geschehen.

Unerwartete Belohnungen können effektiver sein, um fortgesetzte Nutzeraktionen zu fördern, als wenn Sie diese von Anfang an versprochen hätten!

![Eine Kampagne im Schritt „Verfassen“ mit einer iOS Rich-Benachrichtigung, die lautet: „Vielen Dank, dass Sie wieder bei uns eingekauft haben! Um unsere Wertschätzung zu zeigen, schenken wir Ihnen kostenlosen Versand bei Ihrem nächsten Einkauf“.]({% image_buster /assets/img/congratulations_push.jpg %})

### Behalten Sie Ihre Ergebnisse im Blick {#keep-track-of-your-results}

Verfolgen Sie die Öffnungen, um sicherzustellen, dass Sie die richtige Gruppe von Nutzer:innen mit dem optimalen Nachrichtentyp ansprechen. Behalten Sie außerdem Push-Abmeldungen im Auge und achten Sie darauf, diese wichtigen Nutzer:innen nicht zu verlieren.