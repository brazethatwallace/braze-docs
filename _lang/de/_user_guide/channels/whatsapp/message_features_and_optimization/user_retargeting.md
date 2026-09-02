---
nav_title: Nutzer:innen-Retargeting
article_title: Nutzer:innen-Retargeting
page_order: 5
description: "Dieser Referenzartikel beschreibt, wie Nutzer:innen ihre Nachrichten anhand von WhatsApp-Interaktionen retargeten können."
page_type: reference
channel:
  - WhatsApp
---

# Nutzer:innen-Retargeting {#user-retargeting}

> Zusätzlich zur Änderung des Abo-Status von Nutzer:innen zeichnet Braze auch Interaktionen mit dem Kundenprofil auf, um Nachrichten zu filtern und zu triggern.<br><br>Diese Filter und Trigger ermöglichen es Ihnen, Nutzer:innen zu filtern, die WhatsApp-Nachrichten erhalten haben oder WhatsApp-Nachrichten aus einer bestimmten WhatsApp-Campaign oder einem bestimmten Canvas-Schritt erhalten haben.

## Retargeting-Optionen {#retargeting-options}

{% alert note %}
Beim Aufbau von Zielgruppen mit Nutzer:innen-Retargeting möchten Sie möglicherweise bestimmte Nutzer:innen basierend auf ihren Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, wie z. B. das „Do Not Sell or Share“-Recht gemäß dem CCPA. Marketer sollten die relevanten Filter für die Berechtigung von Nutzer:innen in ihren Canvas- und/oder Campaign-Eintrittskriterien implementieren.
{% endalert %}

### Nutzer:innen nach WhatsApp filtern {#filter-users-by-whatsapp}

Nutzer:innen können danach gefiltert werden, wann sie zuletzt eine WhatsApp-Nachricht erhalten haben oder ob sie eine WhatsApp-Nachricht aus einer bestimmten WhatsApp-Campaign erhalten haben. Filter können im Schritt „Zielgruppe zusammenstellen“ des Campaign-Builders festgelegt werden.

#### Nach zuletzt erhaltener WhatsApp-Nachricht filtern {#filter-by-last-received-whatsapp}

![Filter für den letzten Empfang einer WhatsApp-Nachricht am 22. April 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

#### Nach erhaltenen Nachrichten aus einer WhatsApp-Campaign filtern {#filter-by-received-messages-from-whatsapp-campaign}

Filtert Nutzer:innen, die eine Nachricht aus einer bestimmten WhatsApp-Campaign erhalten haben. Mit diesem Filter haben Sie auch die Möglichkeit, diejenigen herauszufiltern, die keine Nachrichten aus einer WhatsApp-Campaign erhalten haben.

{% alert note %}
Wenn eine WhatsApp-Nachricht zugestellt, geöffnet oder angeklickt wird, aktualisiert Braze die Daten für alle Profile, die dieselbe Telefonnummer wie das Profil teilen, das die Interaktion protokolliert hat. Daher können Nutzer:innen, die diese Nummer mit jemandem teilen, der die Nachricht erhalten, geöffnet oder angeklickt hat, mit „Erhalten“-Filtern übereinstimmen, auch wenn sie die Nachricht nicht direkt erhalten haben.
{% endalert %}

![Filter für den Empfang einer WhatsApp-Campaign.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Nach Engagement filtern {#filter-by-engagement}

Retargeten Sie Nutzer:innen, die eine WhatsApp-Campaign oder einen Canvas-Schritt gelesen oder nicht gelesen haben.

#### Nutzer:innen retargeten, die eine bestimmte WhatsApp-Campaign geöffnet/gelesen haben {#retarget-users-who-have-openedread-a-specific-whatsapp-campaign}

1. Erstellen Sie ein Segment mit dem Filter **Clicked/Opened Campaign**.
2. Wählen Sie **read WhatsApp message** aus.
3. Wählen Sie die gewünschte Campaign aus.

![Filter für das Lesen einer WhatsApp-Nachricht.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

#### Nutzer:innen retargeten, die einen bestimmten Canvas-Schritt geöffnet/gelesen haben {#retarget-users-who-have-openedread-a-specific-canvas-step}

1. Erstellen Sie ein Segment mit dem Filter **Clicked/Opened Step**.
2. Wählen Sie **read WhatsApp message** aus.
3. Wählen Sie den gewünschten Canvas und die Canvas-Schritte aus.

![Filter für das Lesen eines WhatsApp-Schritts.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

#### Nach Campaign- oder Canvas-Attribution filtern {#filter-by-campaign-or-canvas-attribution}

Filtern Sie nach Nutzer:innen, die eine bestimmte WhatsApp-Campaign, eine Canvas-Komponente oder einen Tag geöffnet/gelesen haben.

![Filter für das Öffnen einer bestimmten WhatsApp-Nachricht.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}