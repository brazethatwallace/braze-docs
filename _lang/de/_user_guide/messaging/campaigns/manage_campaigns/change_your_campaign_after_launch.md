---
nav_title: Kampagne nach dem Start bearbeiten
article_title: Kampagne nach dem Start bearbeiten
page_order: 1
tool: Campaigns
page_type: reference
description: "Dieser Referenzartikel gibt einen Überblick darüber, welche Auswirkungen das Bearbeiten bestimmter Aspekte einer Kampagne nach dem Start hat."

---

# Kampagne nach dem Start bearbeiten

> Dieser Artikel gibt einen Überblick darüber, welche Auswirkungen das Bearbeiten bestimmter Aspekte einer Kampagne nach dem Start hat.

## Kampagne anhalten

Um eine Kampagne anzuhalten, öffnen Sie die Seite **Kampagnendetails** und wählen Sie **Kampagne anhalten**. Wenn eine Kampagne angehalten wird:

- Geplante Nachrichten werden abgebrochen.
- A/B-Tests, bei denen der erste Test bereits gesendet wurde, werden dauerhaft abgebrochen.
- Events für bereits gesendete Nachrichten (z. B. Öffnungen, Klicks) werden weiterhin getrackt.

Um Ihre Kampagne fortzusetzen, wählen Sie **Fortsetzen**. Ihre Kampagne sendet dann wieder Nachrichten und A/B-Tests, aber versäumte Nachrichten werden nicht erneut gesendet oder neu geplant.

## Getriggerte Kampagnen

Alle Änderungen an Kampagnen mit aktionsbasierter Zustellung und API-getriggerter Zustellung werden sofort für zukünftige Sendungen wirksam.

Wenn diese Kampagnen bereits getriggert, aber noch nicht gesendet wurden (z. B. wenn eine Kampagne mit aktionsbasierter Zustellung und einer Verzögerung von einem Tag während dieser Verzögerungszeit bearbeitet wird), beachten Sie die folgenden Hinweise für geplante Kampagnen.

### Geplante Kampagnen

Wenn Sie nach dem Start Änderungen an einer Kampagne vornehmen müssen, beachten Sie die folgenden Punkte beim Bearbeiten Ihrer Kampagne, um sicherzustellen, dass Ihre Änderungen die gewünschten Auswirkungen haben.

### Nachrichteninhalt

Alle Änderungen am Nachrichteninhalt (einschließlich Titel, Textkörper und Bilder) werden beim Speichern sofort für alle zukünftigen Nachrichtensendungen wirksam. Es ist nicht möglich, den Inhalt von bereits versendeten Nachrichten zu ändern.

### Zeitplan und Zielgruppe

Wenn Sie den geplanten Sendezeitpunkt oder die Zielgruppe Ihrer Kampagne bearbeiten, werden diese Änderungen sofort in der Kampagne übernommen.

#### Hinweise

Wenn Ihre Kampagne intelligentes Timing oder Zustellung nach Ortszeit verwendet, werden Änderungen am geplanten Sendezeitpunkt nicht übernommen, wenn die Bearbeitung weniger als 24 Stunden vor dem ursprünglichen Sendezeitpunkt erfolgt. Das liegt daran:

- **Intelligentes Timing:** Braze beginnt um Mitternacht Samoa-Zeit mit der Berechnung des optimalen Sendezeitpunkts. Wenn dieser Zeitpunkt bereits vergangen ist, hat die Verarbeitung der Nachricht bereits begonnen. Weitere Informationen finden Sie unter [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).
- **Zustellung nach Ortszeit:** Das Bearbeiten einer Kampagne mit Ortszeit-Zustellung, die weniger als 24 Stunden im Voraus geplant ist, ändert den Zeitplan der Nachricht nicht. Weitere Informationen finden Sie unter [Wie plane ich eine Kampagne mit Ortszeit-Zustellung?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign).

### Senderate

Wenn Sie Rate-Limits verwenden, „plant" Braze Ihre Nachrichten in minutengenauen Zeitfenstern. Wenn Sie die Senderate ändern möchten, befolgen Sie den folgenden Prozess, um sofortige Änderungen vorzunehmen.

## Sofortige Änderungen vornehmen

Wenn Änderungen sofort wirksam werden sollen, gehen Sie wie folgt vor:

1. Halten Sie die betroffene Kampagne an.
2. Duplizieren Sie die Kampagne.
3. Nehmen Sie die Änderungen an der duplizierten Kampagne vor.

{% alert important %}
Dadurch wird die Berechtigung für Personen zurückgesetzt, die die ursprüngliche Kampagne bereits erhalten haben. Möglicherweise müssen Sie die duplizierte Kampagne daher nach Personen filtern, die die ursprüngliche Kampagne nicht erhalten haben.
{% endalert %}

## Entwürfe aktiver Kampagnen speichern {#campaign-drafts}

Entwürfe eignen sich hervorragend für umfangreiche Änderungen an aktiven Kampagnen. Durch das Erstellen eines Entwurfs können Sie geplante Änderungen vor dem nächsten Start testen.

{% alert note %}
Eine Kampagne kann jeweils nur einen Entwurf haben. Außerdem sind keine Analytics verfügbar, da die entworfenen Änderungen noch nicht gestartet wurden.
{% endalert %}

Um einen Entwurf zu erstellen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrer aktiven Kampagne.
2. Nehmen Sie Ihre Änderungen vor.
3. Wählen Sie **Als Entwurf speichern**. Beachten Sie, dass Sie nach dem Erstellen eines Entwurfs die aktive Kampagne nicht bearbeiten können, bis Sie Ihren Entwurf entweder starten oder verwerfen.

![Ein Entwurf einer aktiven Kampagne mit der Option, die aktive Kampagne anzuzeigen.]({% image_buster /assets/img/campaign_draft.png %})

Während Sie den Entwurf bearbeiten, können Sie auch die aktive Kampagne im Header des Kampagnenentwurfs oder im Footer der Kampagnen-Analytics referenzieren.

Um zu einer aktiven Kampagne zurückzukehren, wählen Sie **Entwurf bearbeiten** in der Analytics-Ansicht oder der Ansicht der aktiven Kampagne.

### Priorisierung von In-App-Nachrichten

Die Priorität von In-App-Nachrichten wird sofort aktualisiert (bevor der Entwurf gestartet wird), wenn Sie **Genaue Priorität festlegen** auswählen und die Priorität im Verhältnis zu anderen Kampagnen oder Canvases festlegen.