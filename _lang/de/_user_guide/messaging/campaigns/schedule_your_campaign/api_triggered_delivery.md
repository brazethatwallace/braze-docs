---
nav_title: API-getriggerte Zustellung
article_title: API-getriggerte Zustellung
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie eine API-getriggerte Kampagne planen und einrichten."
tool: Campaigns
platform: API

---

# API-getriggerte Zustellung {#api-triggered-delivery}

> API-getriggerte Kampagnen oder servergetriggerte Kampagnen sind ideal für fortgeschrittene transaktionale Anwendungsfälle. Mit API-getriggerten Kampagnen von Braze können Marketer Kampagnentexte, multivariate Tests und Regeln zur erneuten Berechtigung im Braze-Dashboard verwalten und gleichzeitig die Zustellung dieser Inhalte über ihre eigenen Server und Systeme triggern. Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Realtime in die Nachricht eingebunden werden.

## Eine API-getriggerte Kampagne einrichten {#setting-up-an-api-triggered-campaign}

Das Einrichten einer API-getriggerten Kampagne erfordert einige Schritte. Erstellen Sie zunächst eine neue Mehrkanal- oder Einkanal-Kampagne (mit multivariaten Tests).

{% alert note %}
Eine API-getriggerte Kampagne unterscheidet sich von einer [API-Kampagne]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Konfigurieren Sie als Nächstes Ihre Texte und Benachrichtigungen genauso, wie Sie es normalerweise für geplante Benachrichtigungen tun würden, und wählen Sie **API-Triggered Delivery** aus. Weitere Informationen zum Triggern dieser Kampagnen von Ihrem Server aus finden Sie in diesem Artikel zum [Senden API-getriggerter Kampagnen]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Verwendung von Template-Inhalten aus einer API-Anfrage {#using-the-templated-content-included-with-an-api-request}

Zusätzlich zum Triggern der Nachricht können Sie auch Inhalte mit der API-Anfrage einbinden, die über das `trigger_properties`-Objekt in die Nachricht eingesetzt werden. Auf diese Inhalte kann im Nachrichtentext referenziert werden. Verwenden Sie genau zwei geschweifte Klammern pro Liquid-Tag in `trigger_properties` und im Nachrichtentext. Ein Beispiel: {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} Eine zusätzliche `{` oder `}` ist eine häufige Ursache für [Fehler bei der API-getriggerten Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq/#why-is-my-api-triggered-liquid-failing-in-braze).

Sehen Sie sich das folgende Beispiel einer sozialen Benachrichtigung für zusätzlichen Kontext an.

![Die oben genannte Trigger-Eigenschaft, die in die Nachricht eingefügt wird, um automatisch den Namen der Nutzerin oder des Nutzers einzusetzen, gefolgt vom Text: „liked your photo! Click here to see what they've been up to.“.]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Erneute Berechtigung bei API-getriggerten Kampagnen {#re-eligibility-with-api-triggered-campaigns}

Die Anzahl, wie oft eine Nutzerin oder ein Nutzer eine API-getriggerte Kampagne erhält, kann mithilfe von Einstellungen zur erneuten Berechtigung begrenzt werden. Das bedeutet, dass die Nutzerin oder der Nutzer die Kampagne nur einmal oder einmal innerhalb eines bestimmten Fensters erhält, unabhängig davon, wie oft der API-Trigger ausgelöst wird.

Nehmen wir zum Beispiel an, Sie verwenden eine API-getriggerte Kampagne, um Nutzer:innen eine Kampagne über einen Artikel zu senden, den sie kürzlich angesehen haben. In diesem Fall können Sie die Kampagne so begrenzen, dass maximal eine Nachricht pro Tag gesendet wird – unabhängig davon, wie viele Artikel angesehen wurden, während der API-Trigger für jeden Artikel ausgelöst wird. Wenn Ihre API-getriggerte Kampagne hingegen transaktional ist, sollten Sie sicherstellen, dass die Nutzerin oder der Nutzer die Kampagne bei jeder Transaktion erhält, indem Sie die Verzögerung auf null Minuten setzen.

![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})