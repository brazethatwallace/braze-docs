---
nav_title: API-getriggerte Zustellung
article_title: API-getriggerte Zustellung
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie eine API-getriggerte Campaign planen und einrichten."
tool: Campaigns
platform: API

---

# API-getriggerte Zustellung {#api-triggered-delivery}

> API-getriggerte Campaigns oder servergetriggerte Campaigns sind ideal für fortgeschrittene transaktionale Anwendungsfälle. Mit API-getriggerten Campaigns von Braze können Marketer Kampagnentexte, multivariate Tests und Regeln zur erneuten Berechtigung im Braze-Dashboard verwalten und gleichzeitig die Zustellung dieser Inhalte über ihre eigenen Server und Systeme triggern. Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Realtime in die Nachricht eingebunden werden.

## Einrichten einer API-getriggerten Campaign {#setting-up-an-api-triggered-campaign}

Das Einrichten einer API-getriggerten Campaign erfordert einige Schritte. Erstellen Sie zunächst eine neue Multichannel- oder Einzelkanal-Campaign (mit multivariatem Test).

{% alert note %}
Eine API-getriggerte Campaign unterscheidet sich von einer [API-Campaign]({{site.baseurl}}/developer_guide/rest_api/api_campaigns#api-campaigns).
{% endalert %}

Konfigurieren Sie als Nächstes Ihren Text und Ihre Benachrichtigungen auf die gleiche Weise wie bei geplanten Benachrichtigungen und wählen Sie **API-Triggered Delivery** aus. Weitere Informationen zum Triggern dieser Campaigns von Ihrem Server aus finden Sie in diesem Artikel zum [Senden API-getriggerter Campaigns]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

![Konfigurieren Sie Ihren Text und Ihre Benachrichtigungen wie bei geplanten Benachrichtigungen und wählen Sie „API-Triggered Delivery“ aus.]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Verzögerung zwischen API-Trigger und Versand reduzieren {#reducing-delay-between-your-api-trigger-and-send}

Wenn Nachrichten nach dem Aufruf des Trigger-Endpunkts länger als erwartet zum Senden brauchen, prüfen Sie, ob das Nutzerprofil zum Zeitpunkt des Triggers bereits bereit ist.

Standardmäßig ist `send_to_existing_only` auf `true` gesetzt bei [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). Braze sendet nur an bestehende Nutzer:innen und erstellt in diesem Aufruf keine neuen Profile. Um Nutzer:innen im selben Request zu erstellen oder zu aktualisieren und gleichzeitig zu senden, setzen Sie `send_to_existing_only` auf `false` und fügen Sie bei jedem Empfänger bzw. jeder Empfängerin ein `attributes`-Objekt hinzu.

Für E-Mail-Campaigns sollten Sie außerdem `email` (und alle weiteren erforderlichen Zustellungsfelder) innerhalb von `attributes` angeben. Wenn das Profil zum Zeitpunkt des Triggers keine E-Mail-Adresse hat, versucht Braze es bis zu etwa 2 Stunden lang erneut, während auf eingehende Profildaten gewartet wird. Wenn Sie `email` im selben Aufruf mitgeben, vermeiden Sie diese Verzögerung.

Vollständige Anfrageparameter, Beispiele und Informationen zum Retry-Verhalten finden Sie unter [API-getriggerte Campaigns senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#recipient-limits-and-profile-creation) und im [Recipients-Objekt]({{site.baseurl}}/api/objects_filters/recipient_object).

{% alert note %}
Diese Anleitung gilt für API-getriggerte Campaigns (`/campaigns/trigger/send`). Der [Transaktions-E-Mail-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) verwendet eine andere Anfrage-Struktur (`recipient`, Singular) und unterstützt `send_to_existing_only` nicht. Um Nutzer:innen inline bei transaktionalen Sendungen zu erstellen, übergeben Sie `attributes` stattdessen im `recipient`-Objekt.
{% endalert %}

## Verwendung der Template-Inhalte aus einer API-Anfrage {#using-the-templated-content-included-with-an-api-request}

Zusätzlich zum Triggern der Nachricht können Sie auch Inhalte mit der API-Anfrage einschließen, die über das Objekt `trigger_properties` in die Nachricht eingebunden werden. Auf diese Inhalte kann im Nachrichtentext verwiesen werden.

Verwenden Sie genau zwei geschweifte Klammern pro Liquid-Tag in `trigger_properties` und im Nachrichtentext. Ein Beispiel: {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} Ein zusätzliches `{` oder `}` ist eine häufige Ursache für [Fehler bei der API-getriggerten Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).

Sehen Sie sich das folgende Beispiel einer Social-Benachrichtigung für zusätzlichen Kontext an.

![Die oben genannte Trigger-Eigenschaft in der Nachricht, die automatisch den Namen der Nutzer:innen einfügt, gefolgt vom Text: „liked your photo! Click here to see what they've been up to.“]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Wiederzulassung bei API-getriggerten Campaigns {#re-eligibility-with-api-triggered-campaigns}

Die Häufigkeit, mit der Nutzer:innen eine API-getriggerte Campaign erhalten, kann über die Einstellungen zur Wiederzulassung begrenzt werden. Das bedeutet, dass Nutzer:innen die Campaign nur einmal oder einmal innerhalb eines bestimmten Zeitfensters erhalten, unabhängig davon, wie oft der API-Trigger ausgelöst wird.

Angenommen, Sie verwenden eine API-getriggerte Campaign, um Nutzer:innen eine Campaign über einen kürzlich angesehenen Artikel zu senden. In diesem Fall können Sie die Campaign so begrenzen, dass maximal eine Nachricht pro Tag gesendet wird – unabhängig davon, wie viele Artikel angesehen wurden, während der API-Trigger für jeden Artikel ausgelöst wird. Wenn Ihre API-getriggerte Campaign transaktionsbezogen ist, stellen Sie sicher, dass Nutzer:innen die Campaign bei jeder Transaktion erhalten, indem Sie die Verzögerung auf null Minuten setzen.

![Screenshot zu den Einstellungen für die Wiederzulassung bei API-getriggerten Campaigns.]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})