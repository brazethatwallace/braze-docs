---
nav_title: Kampagne nach dem Start bearbeiten
article_title: Kampagne nach dem Start bearbeiten
page_order: 1
tool: Campaigns
page_type: reference
description: "Dieser Referenzartikel gibt einen Überblick darüber, welche Auswirkungen das Bearbeiten bestimmter Aspekte einer Kampagne nach dem Start hat."

---

# Kampagne nach dem Start bearbeiten {#edit-your-campaign-after-launch}

> Dieser Artikel gibt einen Überblick darüber, welche Auswirkungen das Bearbeiten bestimmter Aspekte einer Kampagne nach dem Start hat.

## Warum Sie eine Kampagne vor dem Bearbeiten anhalten sollten {#risks-of-editing-live}

{% alert important %}
Braze empfiehlt, eine Kampagne vor dem Vornehmen von Änderungen anzuhalten, anstatt sie im laufenden Betrieb zu bearbeiten. Das Bearbeiten einer laufenden Kampagne ohne vorheriges Anhalten kann zu unerwartetem Verhalten führen, einschließlich des doppelten Empfangs der Nachricht durch Nutzer:innen.
{% endalert %}

Wenn eine Kampagne gestartet wird, werden alle berechtigten Nutzer:innen in die Warteschlange eingereiht, um die Nachricht zu erhalten. Allerdings werden Nutzer:innen erst als Empfänger:innen der Kampagne markiert, wenn die Nachricht tatsächlich zugestellt wurde – nicht wenn sie in die Warteschlange eingereiht werden. Wenn Sie eine laufende Kampagne bearbeiten, ohne sie vorher anzuhalten, reiht Braze berechtigte Nutzer:innen für die aktualisierte Version erneut in die Warteschlange ein, während die ursprüngliche Warteschlange noch verarbeitet wird. Nutzer:innen, die die ursprüngliche Nachricht noch nicht erhalten haben, befinden sich dann in beiden Warteschlangen, was zu Folgendem führen kann:

- Nutzer:innen erhalten die Kampagne zweimal (die ursprüngliche und die aktualisierte Version), selbst wenn die erneute Berechtigung deaktiviert ist.
- Die ursprüngliche Version der Kampagne wird weiterhin an Nutzer:innen in der ersten Warteschlange zugestellt.
- Unerwartete Zielgruppenzahlen in den Kampagnen-Analytics.

Dies tritt am ehesten bei Kampagnen auf, die eine große Zielgruppe ansprechen und für den sofortigen Versand geplant sind, da eine große Warteschlange von Nutzer:innen gleichzeitig verarbeitet wird. Bei aktionsbasierten Kampagnen mit schrittweisen Triggern (z. B. Registrierungsereignissen) ist das Risiko geringer, da in der Regel nur eine kleine Anzahl von Nutzer:innen zu einem bestimmten Zeitpunkt in der Warteschlange steht.

Um Änderungen sicher vorzunehmen, halten Sie die Kampagne zuerst an und bearbeiten Sie dann entweder die angehaltene Kampagne oder [duplizieren Sie sie](#making-immediate-changes) mit Ihren Änderungen.

## Kampagne anhalten {#stopping-your-campaign}

Um eine Kampagne anzuhalten, öffnen Sie die Seite **Campaign Details** und wählen Sie **Kampagne anhalten**. Wenn eine Kampagne angehalten wird:

- Geplante Nachrichten werden abgebrochen.
- A/B-Tests, bei denen der erste Test bereits gesendet wurde, werden dauerhaft abgebrochen.
- Ereignisse für bereits gesendete Nachrichten (z. B. Öffnungen, Klicks) werden weiterhin getrackt.

Um Ihre Kampagne fortzusetzen, wählen Sie **Resume**. Ihre Kampagne sendet dann wieder Nachrichten und A/B-Tests, aber versäumte Nachrichten werden nicht erneut gesendet oder neu geplant.

### Kampagne während des Sendens anhalten {#stopping-your-campaign-during-sending}

Bei Kampagnen mit einer größeren Zielgruppe und Rate-Limits teilt Braze die Nachrichten in Batches auf und plant deren Versand zu unterschiedlichen Zeitpunkten. Wenn eine Kampagne angehalten wird, werden die Sendungen nicht sofort abgebrochen. Stattdessen werden sie abgebrochen, wenn sie mit der Ausführung beginnen und erkennen, dass die Kampagne angehalten wurde.

Wenn Sie beispielsweise eine E-Mail-Kampagne mit Rate-Limits starten, sie für einige Stunden pausieren und dann fortsetzen, werden alle Nachrichten, die während der Pausenzeit zum Senden geplant waren, abgebrochen und nie gesendet. Alle verbleibenden Nachrichten, die nach der Wiederaufnahme der Kampagne geplant sind, werden weiterhin gesendet. Wenn die erneute Berechtigung für die Kampagne aktiviert ist, können Nutzer:innen erneut berechtigt werden, die Kampagne zu erhalten – zusätzlich zu allen Nachrichten, die bereits in der Warteschlange standen, bevor die Kampagne angehalten wurde.

## Getriggerte Kampagnen {#triggered-campaigns}

Alle Änderungen an Kampagnen mit aktionsbasierter Zustellung und API-getriggerter Zustellung werden sofort für zukünftige Sendungen wirksam.

Wenn diese Kampagnen bereits getriggert, aber noch nicht gesendet wurden (z. B. wenn eine Kampagne mit aktionsbasierter Zustellung und einer Verzögerung von einem Tag während dieser Verzögerungszeit bearbeitet wird), beachten Sie die folgenden Hinweise für geplante Kampagnen.

### Geplante Kampagnen {#scheduled-campaigns}

Wenn Sie nach dem Start Änderungen an einer Kampagne vornehmen müssen, beachten Sie die folgenden Punkte beim Bearbeiten Ihrer Kampagne, um sicherzustellen, dass Ihre Änderungen die gewünschten Auswirkungen haben.

### Nachrichteninhalt {#message-content}

Alle Änderungen am Nachrichteninhalt (einschließlich Titel, Textkörper und Bilder) werden beim Speichern sofort für alle zukünftigen Nachrichtensendungen wirksam. Es ist nicht möglich, den Inhalt von bereits versendeten Nachrichten zu ändern.

### Zeitplan und Zielgruppe {#scheduling-and-audience}

Wenn Sie den geplanten Sendezeitpunkt oder die Zielgruppe Ihrer Kampagne bearbeiten, werden diese Änderungen sofort in der Kampagne übernommen.

#### Hinweise {#considerations}

Wenn Ihre Kampagne intelligentes Timing oder Zustellung nach Ortszeit verwendet, werden Änderungen am geplanten Sendezeitpunkt nicht übernommen, wenn die Bearbeitung weniger als 24 Stunden vor dem ursprünglichen Sendezeitpunkt erfolgt. Das liegt daran:

- **Intelligentes Timing:** Braze beginnt um Mitternacht Samoa-Zeit mit der Berechnung des optimalen Sendezeitpunkts. Wenn dieser Zeitpunkt bereits vergangen ist, hat die Verarbeitung der Nachricht bereits begonnen. Weitere Informationen finden Sie unter [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).
- **Zustellung nach Ortszeit:** Das Bearbeiten einer Kampagne mit Ortszeit-Zustellung, die weniger als 24 Stunden im Voraus geplant ist, ändert den Zeitplan der Nachricht nicht. Weitere Informationen finden Sie unter [Wie plane ich eine Kampagne mit Ortszeit-Zustellung?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign).

### Senderate {#send-rate}

Wenn Sie Rate-Limits verwenden, „plant“ Braze Ihre Nachrichten in minutengenauen Zeitfenstern. Wenn Sie die Senderate ändern möchten, befolgen Sie den folgenden Prozess, um sofortige Änderungen vorzunehmen.

#### Kampagnen mit Zustellgeschwindigkeits-Rate-Limiting pausieren {#pausing-campaigns-with-delivery-speed-rate-limiting}

Wenn Sie eine Kampagne pausieren, die [Zustellgeschwindigkeits-Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) verwendet, verteilt Braze die Sendungen auf minutenbasierte Zeitfenster. **Resume** sendet keine Nachrichten aus Zeitfenstern erneut, die abgebrochen wurden, während die Kampagne pausiert war, und es werden nicht unbedingt alle Nachrichten gesendet, wenn die Kampagne fortgesetzt wird.

Wenn einige Nutzer:innen keine Nachrichten erhalten haben, weil die Kampagne pausiert war, duplizieren Sie die Kampagne und richten Sie sie nur an diese Nutzer:innen, anstatt sich darauf zu verlassen, dass **Resume** die versäumten Nachrichten zustellt.

## Sofortige Änderungen vornehmen {#making-immediate-changes}

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

### Priorisierung von In-App-Nachrichten {#in-app-message-prioritization}

Die Priorität von In-App-Nachrichten wird sofort aktualisiert (bevor der Entwurf gestartet wird), wenn Sie **Genaue Priorität festlegen** auswählen und die Priorität im Verhältnis zu anderen Kampagnen oder Canvases festlegen.