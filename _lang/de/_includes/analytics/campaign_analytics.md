## Analytics anzeigen {#viewing-analytics}

Sobald Sie Ihre Kampagne gestartet haben, können Sie zur Detailseite dieser Kampagne zurückkehren, um die wichtigsten Kennzahlen einzusehen. Navigieren Sie zur Seite **Campaigns** und wählen Sie Ihre Kampagne aus, um die Detailseite zu öffnen.{% if include.channel != "banner" %} Für {% if include.channel == "Content Card" %}Content Cards {% elsif include.channel == "banner" %}Banner {% elsif include.channel == "email" %}E-Mails {% elsif include.channel == "in-app message" %}In-App-Nachrichten {% elsif include.channel == "KakaoTalk" %}KakaoTalk-Nachrichten {% elsif include.channel == "push" %}Push-Nachrichten {% elsif include.channel == "SMS" %}SMS-Nachrichten {% elsif include.channel == "whatsapp" %}WhatsApp-Nachrichten {% elsif include.channel == "webhook" %}Webhooks {% endif %}, die in Canvas gesendet werden, lesen Sie den Abschnitt [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).{% endif %}

{% alert tip %}
Suchen Sie nach Definitionen für die in Ihrem Bericht aufgeführten Begriffe und Metriken? Sehen Sie sich unser
  {% if include.channel == "email" %}[E-Mail-Analytics-Glossar]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary) an.
  {% elsif include.channel == "banner" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) an und filtern Sie nach Banner.
  {% elsif include.channel == "Content Card" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) an und filtern Sie nach Content Cards.
  {% elsif include.channel == "in-app message" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) an und filtern Sie nach In-App-Nachrichten.
  {% elsif include.channel == "push" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) an und filtern Sie nach Push.
  {% elsif include.channel == "SMS" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) an und filtern Sie nach SMS/MMS und RCS.
  {% elsif include.channel == "whatsapp" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) an und filtern Sie nach WhatsApp.
  {% elsif include.channel == "webhook" %}[Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) an und filtern Sie nach Webhook.{% endif %}
{% endalert %}

Auf dem Tab **Kampagnen-Analytics** können Sie Ihre Berichte in einer Reihe von Panels einsehen. Möglicherweise sehen Sie mehr oder weniger als die in den folgenden Abschnitten aufgelisteten, aber jedes hat seinen eigenen nützlichen Zweck.

### Zeitraum {#time-range}

Standardmäßig zeigt **Kampagnen-Analytics** die letzten 90 Tage ab dem aktuellen Zeitpunkt an. Das bedeutet: Wenn die Kampagne vor mehr als 90 Tagen gestartet wurde, werden die Analytics für den angegebenen Zeitraum als „0“ angezeigt. Um alle Analytics für ältere Kampagnen anzuzeigen, passen Sie den Berichtszeitraum an.

### Kampagnendetails {#campaign-details}

Das Panel **Campaign Details** zeigt einen Überblick über die gesamte Performance Ihrer
  {% if include.channel == "banner" %}Banner.
  {% elsif include.channel == "Content Card" %}Content-Card.
  {% elsif include.channel == "email" %}E-Mail.
  {% elsif include.channel == "in-app message" %}In-App-Nachricht.
  {% elsif include.channel == "KakaoTalk" %}KakaoTalk-Nachricht.
  {% elsif include.channel == "push" %}Push-Nachricht.
  {% elsif include.channel == "SMS" %}SMS, MMS und RCS.
  {% elsif include.channel == "whatsapp" %}WhatsApp-Nachrichten.
  {% elsif include.channel == "webhook" %}Webhook.
  {% endif %}

In diesem Panel sehen Sie Gesamtmetriken wie die Anzahl der gesendeten Nachrichten, die Anzahl der Empfänger:innen, die primäre Konversionsrate und den Gesamtumsatz, der mit dieser Nachricht erzielt wurde. Auf dieser Seite können Sie auch die Einstellungen für Zustellung, Zielgruppe und Konversion überprüfen.

{% alert note %}
Die Analytics-Zahlen im Dashboard und in Snowflake können leicht voneinander abweichen. Braze misst die Zahlen im Dashboard und schreibt Zeilen separat nach Snowflake. Snowflake ist die präzisere Datenquelle. Wenn Sie Abweichungen zwischen diesen Quellen feststellen, empfehlen wir, sich auf die Snowflake-Daten zu beziehen.
{% endalert %}

{% if include.channel == "whatsapp" %}
{% alert note %}
Der WhatsApp-Kanal enthält die Leserate. Diese Metrik wird nur für Nutzer:innen mit aktivierten Lesebestätigungen geliefert, was variieren kann.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken zur Bestimmung der Kampagnen-Performance.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken zur Bestimmung der Kampagnen-Performance.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken zur Bestimmung der Kampagnen-Performance.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken zur Bestimmung der Kampagnen-Performance.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken zur Bestimmung der Kampagnen-Performance.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken zur Bestimmung der Kampagnen-Performance.]({% image_buster /assets/img/campaign_details_iam.png %})

In Canvas sehen Sie die Performance von In-App-Nachrichten, die dem von Ihnen erstellten Canvas zugeordnet sind. Sie können das Bedienfeld oben auf der Seite verwenden, um andere Nachrichtentypen (Kanäle) auszublenden und nur die In-App-Nachrichten in Ihrem Canvas anzuzeigen.

![Eine Option zur Auswahl des Kanals, wobei das Kontrollkästchen „In-App Message“ ausgewählt ist.]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![Der Abschnitt „Kampagnendetails“.]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![Kampagnendetails-Panel mit einer Übersicht über die Metriken zur Bestimmung der Kampagnen-Performance.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

#### Estimated Audience und Current Audience {#estimated-audience-and-current-audience}

Je nach Gesamtzahl der Nutzer:innen in Ihrem Workspace kann das Panel **Campaign Details** die Zielgruppenstatistiken als **Current Audience** oder **Estimated Audience** bezeichnen.

Die folgende Tabelle erklärt, was die jeweilige Bezeichnung bedeutet.

| Bezeichnung in der Fußzeile | Wann sie verwendet wird |
| --- | --- |
| **Current Audience** | Der Workspace hat 50.000 Nutzer:innen oder weniger. Braze führt einen vollständigen Scan der Workspace-Profile für die Standardstatistik durch, sodass die angezeigte Zielgruppengröße ein aktueller, nicht auf Stichproben basierender Wert ist (der dennoch von Kanal-Erreichbarkeit, Abo-Regeln und anderen Targeting-Optionen abhängt). |
| **Estimated Audience** | Der Workspace hat mehr als 50.000 Nutzer:innen. Braze führt standardmäßig keine vollständige Datenbankzählung durch. Die Zielgruppengröße wird anhand einer Stichprobe geschätzt und hochgerechnet, ähnlich wie der Bereich **Reachable users** im Segment Builder. Abweichungen sind zu erwarten, insbesondere bei kleinen Segmenten im Verhältnis zum Workspace. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estimated Audience und Current Audience" }

Weitere Informationen zum Stichprobenverhalten, zu **Calculate exact statistics** und zur Segmentierung **erreichbarer Nutzer:innen** finden Sie unter [Segmentgröße messen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

{% if include.channel == "Content Card" %}

#### Kontrollgruppen {#cc-control-group}

Um die Wirkung einer einzelnen Content-Card zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Campaign Details** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% elsif include.channel == "SMS" %}

#### Kontrollgruppen {#sms-control-group}

Um die Wirkung einer einzelnen SMS-, MMS- oder RCS-Nachricht zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Campaign Details** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% elsif include.channel == "whatsapp" %}

#### Kontrollgruppen {#whatsapp-control-group}

Um die Wirkung einer einzelnen WhatsApp-Nachricht zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Campaign Details** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% elsif include.channel == "webhook" %}

#### Kontrollgruppen {#webhook-control-group}

Um die Wirkung einer einzelnen Webhook-Nachricht zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Das übergeordnete Panel **Campaign Details** enthält keine Metriken aus der Kontrollgruppen-Variante.

{% endif %}

#### Changes Since Last Viewed

Die Anzahl der Aktualisierungen der Kampagne durch andere Mitglieder Ihres Teams wird durch die Metrik *Changes Since Last Viewed* auf der Kampagnenübersichtsseite erfasst. Wählen Sie **Changes Since Last Viewed**, um ein Changelog der Aktualisierungen an Name, Zeitplan, Tags, Nachricht, Zielgruppe, Genehmigungsstatus oder Teamzugriffskonfiguration der Kampagne anzuzeigen. Bei jeder Aktualisierung können Sie sehen, wer die Änderung vorgenommen hat und wann. Sie können dieses Changelog verwenden, um Änderungen an Ihrer Kampagne nachzuvollziehen.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can Klick, der on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Content-Card-Performance

Das Panel **Content Card Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![Content-Card-Nachrichten-Performance-Analytics]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### E-Mail-Performance {#email-performance}

Das Panel **Email Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![E-Mail-Nachrichten-Performance-Analytics]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### In-App-Nachrichten-Performance {#in-app-message-performance}

Das Panel **In-App Message Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![In-App-Nachrichten-Performance-Analytics]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Push-Performance {#push-performance}

Das Panel **Push Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![Push-Nachrichten-Performance-Analytics]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCS-Performance

Das Panel **SMS/MMS/RCS Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![SMS/MMS/RCS-Performance-Panel mit einer Tabelle mit Metriken für eine Kontrollgruppe, Variante 1 und Variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Banner-Performance

Das Panel **Banner Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Diese Metriken variieren je nach Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen.

![Banner-Performance-Panel mit einer Tabelle mit Metriken für eine Kontrollgruppe, Variante 1 und Variante 2.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### KakaoTalk-Performance

Das Panel **KakaoTalk Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

{% elsif include.channel == "webhook" %}
### Webhook-Performance

Das Panel **Webhook Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![Webhook-Performance-Panel mit einer Tabelle mit Metriken für eine Kontrollgruppe und Variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp-Performance

Das Panel **WhatsApp Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und je nachdem, ob Sie einen multivariaten Test durchführen. Klicken Sie auf das Symbol <i class="fa fa-eye preview-icon"></i> **Preview**, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![WhatsApp-Performance-Panel mit einer Tabelle mit Metriken für Variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

#### Credits und Sendezähler {#credits-versus-send-counts}

Die WhatsApp-Sendezähler in den Kampagnen-Analytics spiegeln Zustellversuche wider. Die verbrauchten Credits können abweichen, wenn Meta nach Nachrichtenkategorie (Marketing, Utility, Authentifizierung, Service) abrechnet.

- Antwortnachrichten, die in Braze erstellt werden, verbrauchen keine Braze-WhatsApp-Credits.
- Verwenden Sie **Analytics** > **Daily Stats** für eine Orientierung zum Sendevolumen. Credit-Aufschlüsselungen pro Kampagne oder Canvas sind nicht verfügbar.

{% endif %}

Wenn Sie Ihre Ansicht vereinfachen möchten, klicken Sie auf <i class="fas fa-plus"></i> **Add/Remove Columns** und deaktivieren Sie die gewünschten Metriken. Standardmäßig werden alle Metriken angezeigt.

{% if include.channel == "email" %}

#### Heatmaps

Mit Heatmaps können Sie sehen, wie erfolgreich verschiedene Links in einer einzelnen E-Mail-Kampagne sind. Gehen Sie im Abschnitt **Message Analytics** zum Panel **Email Performance**. Wählen Sie **Preview & Heatmap**, um eine Vorschau Ihrer E-Mail-Kampagne und der Heatmap anzuzeigen. Alternativ können Sie den Hyperlink im Variantennamen auswählen, um die Heatmap aufzurufen.

{% alert note %}
Kampagnen-Analytics zeigen Klickdaten für bis zu 100 eindeutige URLs pro Variante an, sortiert nach Gesamtklicks. URLs werden nach ihrer normalisierten Form gruppiert, die keine Abfrageparameter enthält. Wenn eine Variante mehr als 100 eindeutige normalisierte URLs hat, werden nur die Top 100 nach Klickanzahl angezeigt. Klickdaten für URLs jenseits dieses Limits existieren weiterhin, werden aber nicht im Dashboard oder in der Heatmap angezeigt. Wenn Link Aliasing aktiviert ist, werden Klicks anhand der Link-ID statt der Roh-URL getrackt, was in der Regel zu weniger eindeutigen Einträgen führt und dieses Limit seltener erreicht wird.
{% endalert %}

In dieser Ansicht können Sie mit dem Schalter **Show Heatmap** eine visuelle Darstellung Ihrer E-Mail aufrufen, die die Gesamthäufigkeit und den Ort der Klicks innerhalb der Laufzeit der Kampagne anzeigt. Im Panel **Link Table by Total Clicks** können Sie alle Links in Ihrer E-Mail-Kampagne anzeigen und nach Gesamtklicks sortieren. Dies kann zusätzliche Insights darüber liefern, wohin Ihre Nutzer:innen navigieren. Um eine Kopie der Heatmap als Referenz zu speichern, klicken Sie auf den Download-Button.

{% alert note %}
Wenn Links Liquid für dynamische URLs verwenden, stimmen die angeklickten URLs möglicherweise nicht genau genug mit dem gerenderten Link in der Nachricht überein, sodass die Heatmap die Klicks nicht mit diesem Link verknüpfen kann – diese Links werden dann möglicherweise nicht auf der Heatmap angezeigt. Um Klickdaten auf der Heatmap mit Template-Links zu verknüpfen, verwenden Sie [Link Aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing). Für ein vollständiges Bild verwenden Sie die Klickdaten im Panel **Link Table by Total Clicks**.
{% endalert %}

![Beispiel für die Seite „Preview & Heatmap“ mit einer E-Mail-Kampagne und einem Panel mit Beispielen für Link-Aliase und deren Gesamtklicks.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

##### Heatmap-Abmeldeklicks versus Kampagnen-Analytics {#heatmap-unsubscribe-clicks-versus-campaign-analytics}

Klicks auf Abmeldelinks in der Heatmap können von der Metrik *Unsubscribers* in den Kampagnen-Analytics abweichen:

- Wenn Sie eine benutzerdefinierte Abmelde-URL im Nachrichtentext verwenden, behandelt Braze diesen Link für Heatmap-Zwecke als einen standardmäßig getrackten Link – er erscheint in der **Link Table by Total Clicks** wie jeder andere Link. Wenn Braze eine Abmeldung über den von Braze bereitgestellten Abmeldelink verarbeitet, wird die Metrik *Unsubscribers* erhöht. Benutzerdefinierte Abmelde-URLs erhöhen diese Metrik nicht, es sei denn, Sie aktualisieren Nutzer:innen über die API.
- Wenn sich eine Nutzer:in über den [List-Unsubscribe-Header]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) abmeldet (eine Ein-Klick-Abmeldeoption, die von einigen Posteingangs-Anbietern angezeigt wird), wird *Unsubscribers* in den Kampagnen-Analytics erhöht, aber dies erscheint nicht als Klick in der Heatmap. Wenn die Nachricht **Unsubscribe from specific subscription group** verwendet, meldet Braze die Nutzer:in nur von der konfigurierten Abo-Gruppe ab, nicht global. Die Verfügbarkeit dieser Option variiert je nach Empfänger:in, da sich die Posteingangs-Anbieter darin unterscheiden, ob sie den List-Unsubscribe-Header rendern oder unterstützen.

Für eine vollständige Übersicht über das Abmeldeverhalten überprüfen Sie sowohl die Heatmap-Link-Aufschlüsselung als auch die Metrik *Unsubscribers*. Weitere Details finden Sie unter [Warum sich *Unsubscribes* und Abmeldelink-Klicks unterscheiden können]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#why-unsubscribes-and-unsubscribe-link-clicks-can-differ).

##### Nur-Mobil-Links in der Heatmap {#mobile-only-links-in-the-heatmap}

Die Heatmap zeigt nur Wärmesignaturen für Links an, die bei der ausgewählten Vorschaugröße sichtbar sind.

Links, die nur im mobilen Layout erscheinen, sind in der **Desktop**-Ansicht ausgeblendet (und können je nach Vorschaubreite auch in **Overall** ausgeblendet sein), sodass diese Klicks nicht als Wärmesignaturen angezeigt werden. Diese Links erscheinen dennoch im Panel **Link Table by Total Clicks** mit ihren Gesamtklicks und Prozentsätzen.

Um Wärmesignaturen für Nur-Mobil-Links anzuzeigen, wählen Sie **Mobile**. Die mobile Vorschau entspricht dem mobilen Breakpoint des Drag-and-Drop-Editors (620&nbsp;px). Wenn die E-Mail erst bei einer schmaleren Breite das Layout wechselt, bleiben diese Links auch in der **Mobile**-Vorschaugröße ausgeblendet.

#### Bilder {#images}

Wir empfehlen, CORS für Ihre Bild-URLs zu aktivieren, damit Bilder in Heatmap-Vorschauen und -Exporten nicht fehlen.

Wenn Bilder in einem Export fehlen, arbeiten Sie mit Ihren Entwickler:innen zusammen, damit Bild-Assets den Cross-Origin-Zugriff erlauben: Der Server sollte den Header `Access-Control-Allow-Origin` mit entweder `*` oder Ihrer Braze-Dashboard-Domain zurückgeben.

{% endif %}

{% if include.channel == "Content Card" %}

#### Content-Card-Metriken {#content-card-metrics}

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller Content-Cards-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Filtern Sie dort nach Content Cards.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Content-Card-Metriken">
    <caption class="sr-only">Content-Card-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Messages Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                Die Berechnung hängt davon ab, was Sie für die
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-Entry-versus-at-first-impression">Kartenerstellung</a> ausgewählt haben:<br><br>
                <ul>
                    <li><b>Beim Start oder beim Einstieg in den Schritt:</b> Die Anzahl der erstellten und verfügbaren Karten. Dabei wird nicht berücksichtigt, ob die Nutzer:innen die Karte angesehen haben.</li>
                    <li><b>Bei der ersten Impression:</b> Die Anzahl der Karten, die den Nutzer:innen angezeigt wurden.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Dieser Wert kann für dieselbe Nutzer:in mehrfach gezählt werden.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Dieser Zähler</span> wird nicht erhöht, wenn eine Nutzer:in eine Content-Card zum zweiten Mal aufruft.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Da eine Nutzer:in jeden Tag eine eindeutige tägliche Impression haben kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dies umfasst auch Klicks auf die von Braze bereitgestellten Abmeldelinks.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Unique Dismissals</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
Bei der Protokollierung von Impressionen gibt es einige Unterschiede zwischen Web, Android und iOS. Generell protokolliert Braze eine Impression, wenn eine Karte gesehen wird – also nachdem eine Nutzer:in zur entsprechenden Content-Card in ihrem Feed gescrollt hat.
{% endalert %}

#### Unique Daily Impressions versus Unique Impressions

Es gibt mehrere Metriken, die die Sichtbarkeit Ihrer Nachricht erfassen, darunter _Unique Daily Impressions_ und _Unique Impressions_. Anhand einiger Beispielszenarien lassen sich diese Metriken besser verstehen.

Angenommen, Sie sehen sich heute eine Content-Card an, erhalten morgen eine neue Karte aus derselben Kampagne und übermorgen wieder eine – dann werden Sie dreimal als _Unique Daily Impression_ gezählt. Sie werden jedoch nur für eine _Unique Impression_ gezählt. Außerdem werden Sie in der Anzahl der _Messages Sent_ berücksichtigt, da die Karte auf Ihrem Gerät verfügbar war.

Ein weiteres Beispiel: Angenommen, Sie sehen fünf _Unique Impressions_ für eine Content-Card-Kampagne mit 150.000 _Messages Sent_. Das bedeutet, dass die Karte (im Backend) einer Zielgruppe von 150.000 Nutzer:innen zur Verfügung gestellt wurde, aber nur die Geräte von fünf Nutzer:innen alle folgenden Schritte nach dem Senden ausgeführt haben:

1. Eine Sitzung gestartet oder die App hat explizit eine Content-Cards-Synchronisierung angefordert (oder beides)
2. Zur Content-Cards-Ansicht navigiert
3. Das SDK hat eine Impression aufgezeichnet und an den Server gesendet

_Messages Sent_ bezieht sich auf Content Cards, die zum Ansehen verfügbar sind, während _Unique Daily Impressions_ die Content Cards bezeichnet, die tatsächlich angesehen wurden.

{% elsif include.channel == "banner" %}

### Banner-Metriken {#banner-metrics}

Dies sind die wichtigsten Metriken, die Sie bei der Überprüfung der Performance Ihrer Banner-Kampagne im Blick behalten sollten. Klicks und Impressionen für Banner werden automatisch über das SDK getrackt.

Die vollständigen Definitionen aller Banner-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Filtern Sie dort nach Banner.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Banner-Metriken">
    <caption class="sr-only">Banner-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Bei Bannern werden Impressionen einmal pro Nutzersitzung protokolliert. Wenn dasselbe Banner innerhalb derselben Sitzung mehrfach angezeigt wird, wird nur eine Impression protokolliert.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Jede Nutzer:in wird nur einmal gezählt.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split"><i>Total Clicks</i> ist die Gesamtzahl (und der Prozentsatz) der Nutzer:innen, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob dieselbe Nutzer:in mehrmals geklickt hat.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-dismissals">Total Dismissals</a></td>
            <td class="no-split"><i>Total Dismissals</i> ist die Gesamtzahl der Male, die Nutzer:innen das Banner geschlossen haben. Nur für Banner mit aktiviertem Schließverhalten verfügbar.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} Jede Nutzer:in wird nur einmal gezählt.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Primary Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Da eine Betrachterin oder ein Betrachter jeden Tag eine eindeutige tägliche Impression haben kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Revenue</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Confidence</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Berechnungsbeispiele für Banner-Metriken {#banner-metrics-calculation-examples}

Es gibt mehrere Metriken, die die Sichtbarkeit Ihrer Nachricht erfassen, darunter _Unique Daily Impressions_ und _Unique Impressions_. Anhand einiger Beispielszenarien lassen sich diese Metriken besser verstehen.

Angenommen, Sie sehen sich heute ein Banner an, morgen dasselbe Banner und übermorgen erneut – dann werden Sie dreimal als _Unique Daily Impression_ gezählt. Sie werden jedoch nur für eine _Unique Impression_ gezählt.

Nehmen wir als weiteres Beispiel an, Sie sehen fünf _Unique Impressions_ in einer Banner-Kampagne. Das bedeutet, dass nur die Geräte von fünf Nutzer:innen alle folgenden Schritte ausgeführt haben:

1. Eine Sitzung gestartet oder die App hat explizit eine Banner-Synchronisierung angefordert (oder beides)
2. Zur Banner-Ansicht navigiert
3. Das SDK hat eine Impression aufgezeichnet und an den Server gesendet

_Unique Daily Impressions_ bezieht sich auf die Banner, die tatsächlich angesehen wurden.

#### Abweichungen zwischen Kontrollgruppen und Varianten {#discrepancies-between-control-groups-and-variants}

Wenn eine Banner-Kampagne eine Kontrollgruppe verwendet, können die Impressionen der Kontrollgruppe höher sein als die der Variante, selbst wenn die Zielgruppenaufteilung zwischen den Gruppen gleichmäßig ist. Diese Abweichung wird durch einen Unterschied in der Art und Weise verursacht, wie Impressionen für Kontroll- und Varianten-Banner protokolliert werden.

Sowohl Kontroll- als auch Varianten-Impressionen erfordern, dass die Banner-Platzierung in den sichtbaren Bereich gelangt. Varianten-Impressionen werden erst protokolliert, wenn das vollständige Banner auf dem Bildschirm sichtbar ist. Kontroll-Impressionen können bereits protokolliert werden, sobald die Platzierung in den sichtbaren Bereich gelangt – bevor das vollständige Banner für eine Variante sichtbar wäre.

{% elsif include.channel == "email" %}

#### E-Mail-Metriken {#email-metrics}

Im Folgenden finden Sie einige wichtige E-Mail-spezifische Metriken, die in anderen Kanälen nicht verfügbar sind. Die vollständigen Definitionen aller in Braze verwendeten E-Mail-Metriken finden Sie in unserem [E-Mail-Analytics-Glossar]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="E-Mail-Metriken">
    <caption class="sr-only">E-Mail-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dieser Wert wird über einen Zeitraum von sieben Tagen für E-Mails getrackt und anhand der <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a> gemessen. Dazu gehören auch Klicks auf die von Braze bereitgestellten Abmeldelinks. Dieser Wert sollte zwischen 5–10 % liegen. Alles über 10 % ist außergewöhnlich!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Unique Opens</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Bei E-Mails erfolgt das Tracking über einen Zeitraum von 7 Tagen. Dieser Wert sollte zwischen 30–40 % liegen. Alles über 40 % ist außergewöhnlich!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#Klick, der-to-open-rate">Klick, der-to-Open Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Klick, der-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Spam Rate</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} Wenn diese Metrik größer als 0,08 ist, könnte dies ein Hinweis darauf sein, dass entweder Ihr Nachrichtentext zu verkaufsorientiert ist oder Sie Ihre Methoden zur Erfassung von E-Mail-Adressen überdenken sollten (um sicherzustellen, dass Sie nur Personen anschreiben, die an Ihrer Korrespondenz interessiert sind).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Unsubscribers or Unsub</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Other Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimated Real Opens</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Weitere Informationen finden Sie im folgenden Abschnitt.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Machine Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Deferral</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Zustellungen und Bounces {#deliveries-and-bounces}

Das Dashboard hebt _Hard Bounces_ hervor. Einige _Bounces_ können Soft Bounces sein und stimmen allein nicht mit dieser Zahl überein. Sie können Soft Bounces mit dieser Formel annähern:

_Sendungen − (Zustellungen + Hard Bounces) ≈ Soft Bounces_

_Zustellungen_ können während des Wiederholungsfensters Ihres E-Mail-Anbieters (E-Mail-Anbieter) steigen, wenn Wiederholungsversuche erfolgreich sind, während _Sendungen_ und Hard Bounces bei einem einmaligen Versand nach Abschluss des Versands feststehen. SendGrid und SparkPost wiederholen bis zu 72 Stunden; Amazon SES wiederholt bis zu 14 Stunden.

###### Häufige Szenarien bei der Fehlerbehebung der Zustellung {#common-delivery-troubleshooting-scenarios}

Beachten Sie bei der Überprüfung Ihrer E-Mail-Analytics die folgenden Muster:

- **Lücke zwischen _Sendungen_ und (_Zustellungen_ + _Hard Bounces_):** Während des E-Mail-Anbieter-Wiederholungsfensters nach einem einmaligen Versand spiegelt diese Lücke häufig Soft Bounces oder Deferrals wider, die noch wiederholt werden. Nach Abschluss der Wiederholungsversuche bedeutet eine verbleibende Lücke in der Regel, dass Nachrichten einen Soft Bounce hatten und nie zugestellt wurden – diese Sendungen werden nicht in den Kampagnen-_Zustellungen_ oder _Bounces_ gezählt. Verwenden Sie die Formel unter [Zustellungen und Bounces](#deliveries-and-bounces), um laufende Soft Bounces abzuschätzen.
- **Niedrige _Zustellungen_ nach Abschluss der Wiederholungsversuche:** Wenn die Zustellraten nach Abschluss der Wiederholungsversuche niedrig bleiben, vergleichen Sie das Sendevolumen mit Ihren üblichen Mustern. Postfach-Anbieter können E-Mails verzögern, drosseln oder mit einem Soft Bounce versehen, wenn das Volumen im Verhältnis zu Ihrer Absender-Reputation ansteigt. Möglicherweise sehen Sie Nachrichten wie `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Verwenden Sie [Rate-Limiting für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), um große Sendungen zu dosieren, und lesen Sie [Gedrosselte IPs]({{site.baseurl}}/user_guide/channels/email/reporting#throttled-ips) für weitere Schritte zur Fehlerbehebung.
- **Soft Bounces und Deferrals werden nicht in den Kampagnen-Analytics angezeigt:** Kampagnen-Analytics heben _Hard Bounces_ hervor, enthalten aber _Soft Bounces_ oder _Deferrals_ nicht als separate Spalten. Überwachen Sie diese Ereignisse im Nachrichten-Aktivitätsprotokoll, mit dem [Segmentfilter „Soft Bounced“]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced) oder über Currents-Deferral-Events. Informationen zur Funktionsweise von Wiederholungsversuchen finden Sie unter [Deferrals](#deferrals).
- **Zustellprozentsätze, die sich möglicherweise nicht zu 100 % addieren:** _Zustellungen %_, _Bounce %_ und _Spam Rate %_ ergeben möglicherweise nicht 100 % der _Sendungen_. Nachrichten, die einen Soft Bounce haben und nach dem E-Mail-Anbieter-Wiederholungsfenster nie zugestellt werden, werden nicht in den Kampagnen-_Zustellungen_ oder _Bounces_ gezählt, sodass ein Teil der _Sendungen_ in diesen Raten nicht berücksichtigt wird. Warten Sie, bis die Wiederholungsversuche abgeschlossen sind, bevor Sie die endgültige Zustellleistung beurteilen, oder verwenden Sie die Formel unter [Zustellungen und Bounces](#deliveries-and-bounces), um abzuschätzen, wie viele Sendungen sich noch im Wiederholungsversuch befinden.

##### Klicks ohne Öffnungs-Event {#clicks-without-an-open-event}

Ein Klick kann ohne eine Öffnung protokolliert werden, wenn das Öffnungs-Pixel nie geladen wird. Zum Beispiel wird die Nachricht in Gmail abgeschnitten, oder die Nutzer:in hat Bilder deaktiviert (das Öffnungs-Pixel befindet sich normalerweise in der Fußzeile). Einige Clients leiten Bilder über Proxys weiter (wie Apple Mail), sodass die Öffnung protokolliert werden kann, wenn der Server das Pixel zum ersten Mal abruft – nicht wenn die Nutzer:in die E-Mail liest. Unternehmensdomains blockieren Bilder oft standardmäßig.

Ein Klick und eine Öffnung können auch an verschiedenen Tagen stattfinden: Eine Nutzer:in könnte am 16. Mai mit deaktivierten Bildern klicken (keine Öffnung) und dann am 17. Mai im Webmail öffnen (Öffnung wird dann protokolliert).

##### Höhere _Unique Clicks_ als _Unique Opens_ {#higher-unique-clicks-than-unique-opens}

Es kann vorkommen, dass _Unique Clicks_ die _Unique Opens_ deutlich übersteigen (z. B. mehrere eindeutige Klicks pro eindeutiger Öffnung), selbst wenn Sie von Ihrer Zielgruppe ein niedrigeres Verhältnis erwarten. Dieses Muster bedeutet in der Regel, dass Öffnungen zu niedrig gezählt, Klicks überhöht oder beides der Fall ist. Das bedeutet jedoch nicht, dass Braze Klicks isoliert falsch zählt.

Braze protokolliert eine E-Mail-Öffnung, wenn das Öffnungs-Tracking-Pixel geladen wird. Dieses Pixel ist ein kleines transparentes Bild (oft als 1 x 1&nbsp;px beschrieben), das Braze dem Nachrichten-HTML hinzufügt. Wenn das Pixel nie geladen wird, wird für diese Ansicht keine Öffnung protokolliert, aber Link-Klicks können dennoch registriert werden – sodass Ihre Klick, der-to-Open-Rate und das Verhältnis zwischen diesen beiden Metriken verzerrt aussehen können.

**Das Postfach hat das Öffnungs-Tracking-Pixel nie geladen**

Das Pixel wird möglicherweise nicht geladen, wenn:

- **Die Nachricht abgeschnitten wird.** Langes HTML schiebt Inhalte – einschließlich des Pixels am Ende – hinter einen „Gesamte Nachricht anzeigen“-Abschnitt. In Gmail werden Nachrichten, die größer als etwa [102&nbsp;KB]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size) sind, häufig abgeschnitten, was das Laden des Pixels verhindern kann, bis die vollständige Nachricht geöffnet wird (und manchmal auch dann nicht, je nach Client).
- **Bilder blockiert oder eingeschränkt sind.** Strengere Posteingangs-Sicherheit (häufig bei Unternehmenskonten) kann Remote-Bilder blockieren, bis die Empfänger:in sich entscheidet, sie zu laden, sodass das Öffnungs-Pixel nicht ausgelöst wird, obwohl getrackte Links angeklickt werden.
- **Die Nachricht sich im Spam- oder Massenordner befindet.** Viele Anbieter laden Remote-Bilder (einschließlich des Öffnungs-Pixels) in diesen Ordnern standardmäßig nicht.

**Was Sie tun können**

- **Abschneiden:** Kürzen und vereinfachen Sie das HTML, entfernen Sie ungenutzte Styles oder Assets und halten Sie die Gesamtgröße der Nachricht innerhalb der Client-Limits. Für Gmail sollten Sie unter etwa 102&nbsp;KB bleiben, wie unter [E-Mail-Größe]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size) beschrieben.
- **Posteingangs-Sicherheit und Bildladen:** Nur die Empfänger:in (oder deren IT-Richtlinie) kann ändern, ob Bilder standardmäßig geladen werden.
- **Spam-Platzierung:** Konzentrieren Sie sich auf die [Verbesserung der E-Mail-Zustellbarkeit]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) und Listenhygiene. Wenn E-Mails regelmäßig im Spam landen und die Metriken falsch aussehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

**Sicherheits- oder Bot-Aktivität bei Links**

Einige E-Mail-Sicherheitsprodukte folgen Links, um nach Bedrohungen zu scannen. Diese Anfragen können einen Klick protokollieren, ohne Bilder zu laden, sodass Sie Klickaktivität ohne eine entsprechende Öffnung sehen können.

##### Deferrals {#deferrals}

Ein Deferral bedeutet, dass eine E-Mail nicht sofort zugestellt werden konnte, Braze die E-Mail jedoch über Ihren E-Mail-Anbieter nach diesem vorübergehenden Zustellungsfehler erneut versucht, um die Chancen auf eine erfolgreiche Zustellung zu maximieren, bevor die Versuche für diese spezielle Kampagne eingestellt werden. SendGrid und SparkPost wiederholen bis zu 72 Stunden; Amazon SES wiederholt bis zu 14 Stunden. Typische Gründe für Deferrals sind reputationsbasiertes Rate-Limiting des Posteingangs-Anbieters für das E-Mail-Volumen, vorübergehende Verbindungsprobleme oder DNS-Fehler.

_Deferrals_ unterscheiden sich von _Soft Bounces_. Wenn während dieses Wiederholungszeitraums keine E-Mail erfolgreich zugestellt wurde, sendet Braze ein Soft-Bounce-Event pro versuchtem Kampagnenversand. Vor dem 25. Februar 2025 wurden diese Wiederholungsversuche als mehrere Soft Bounces für einen Kampagnenversand gezählt.

Beachten Sie, dass _Deferrals_ derzeit nur über Currents oder Braze-Snowflake-Features (wie Abfrage-Builder, SQL-Segmente, Snowflake-Datenfreigabe) verfügbar sind. {% multi_lang_include product_feedback_cta.md context="gap" feature="Deferrals in campaign or Canvas analytics" %}

##### Geschätzte reale Öffnungsrate {#estimated-real-open-rate}

Diese Statistik verwendet ein proprietäres, von Braze entwickeltes Analysemodell, um eine Schätzung der individuellen Öffnungsrate der Kampagne zu rekonstruieren – so, als ob es keine automatischen Öffnungen gäbe. Obwohl wir bei einigen Öffnungs-Events von E-Mail-Absendern die Kennzeichnung *Machine Opens* erhalten, können diese Kennzeichnungen häufig tatsächliche Öffnungen fälschlicherweise als automatische Öffnungen markieren. Mit anderen Worten: Die *Other Opens* sind wahrscheinlich eine Unterschätzung der tatsächlichen Öffnungen (durch echte Nutzer:innen). Stattdessen verwendet Braze die Klickdaten der einzelnen Kampagnen, um auf die Rate zu schließen, mit der Menschen die Nachricht tatsächlich geöffnet haben. Dies kompensiert verschiedene Mechanismen zum automatischen Öffnen, einschließlich Apples E-Mail-Datenschutz.

Die _Estimated Real Open Rate_ wird 24 Stunden nach Beginn des E-Mail-Versands berechnet und danach alle 72 Stunden neu berechnet.

Da diese Metrik kontinuierlich neu berechnet wird, kann sich der Wert der _Estimated Real Open Rate_ im Laufe der Zeit ändern, wenn neue Engagement-Signale (wie Öffnungen und Klicks) empfangen und in das Modell integriert werden. In der Praxis kann die _Estimated Real Open Rate_ täglich aktualisiert werden, solange eine Kampagne aktiv ist.

Normalerweise sind etwa 10.000 zugestellte E-Mails erforderlich, damit die Statistik erfolgreich berechnet werden kann, wobei diese Zahl je nach Klickrate variieren kann. Wenn die Statistik nicht berechnet werden kann, wird in der Spalte „--“ angezeigt.

###### Einschränkungen {#considerations}

Die Estimated Real Open Rate ist nur in Campaigns verfügbar und wird nicht in Currents-Events gemeldet. Diese Metrik wird nur für aktive Kampagnen, die vor dem 14. November 2023 gestartet wurden, rückwirkend berechnet.

##### Umgang mit steigenden Klickraten {#handling-increases-in-click-rates}

Öffnungsraten können eine aufschlussreiche Metrik für das Tracking Ihrer E-Mail-Kampagnen sein. Allerdings sind diese Öffnungsraten nicht unbedingt ein genauer Indikator für das menschliche Engagement bei E-Mail-Kampagnen. Ein Öffnungs-Event tritt definitionsgemäß ein, wenn eine Nutzer:in eine E-Mail öffnet, was bedeutet, dass ein transparentes Tracking-Pixel für die Öffnung erfolgreich heruntergeladen wurde.

Darüber hinaus kann die Verwendung von Sicherheitsscannern die Öffnungsraten in die Höhe treiben. Einige dieser Tools schützen ihre Nutzer:innen, indem sie eingehende E-Mails auf bösartige Inhalte überprüfen und auf Links klicken, um deren Legitimität zu verifizieren. Diese Klicks werden oft als „Bot-Klicks“ oder „nicht-menschliche Interaktion“ (NHI) bezeichnet.

Nachdem eine E-Mail unsere Server verlassen hat, haben wir nur begrenzte Einblicke in den weiteren Verlauf. Hier sind einige Empfehlungen zum Umgang mit NHI, die sich auf Ihre Ergebnisse auswirken können:

1. Seien Sie sich bewusst, dass dies bei jedem Absender und fast jeder Empfänger:in passieren kann. Klicks sind ebenso wie Öffnungen kein vollständig zuverlässiger Indikator für die menschliche Interaktion mit Ihren Nachrichten – NHI lässt sich nicht verhindern.
2. Ein höheres positives Engagement korreliert in der Regel mit niedrigerer NHI. Daher ist es wichtig, die [Best Practices]({{site.baseurl}}/user_guide/channels/email/best_practices) für E-Mail-Messaging zu befolgen. Dazu gehört, die ausdrückliche Erlaubnis Ihrer Nutzer:innen für den E-Mail-Versand einzuholen und nicht engagierte Abonnent:innen regelmäßig per Sunsetting zu entfernen.
3. Verwenden Sie wenn möglich HTTPS-Links in Ihren E-Mails. NHI ist bei Absendern, die sichere Links verwenden, weniger verbreitet.
4. Wenn Sie einen Ein-Klick-Abmeldeprozess verwenden, sollten Sie die Einrichtung eines [Präferenzzentrums]({{site.baseurl}}/user_guide/channels/email/subscriptions) in Betracht ziehen, das die Nutzer:innen zu einer Seite weiterleitet, auf der sie ihre Benachrichtigungseinstellungen bearbeiten und verwalten können. Dies kann hilfreich sein, da NHI Nutzer:innen versehentlich abmelden kann.
5. Ziehen Sie [andere Metriken]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance) in Betracht, um den Erfolg Ihres E-Mail-Marketings zu messen, z. B. Konversionen, App-Sitzungen oder Website-Besuche.
6. Fügen Sie einen versteckten Link in Ihre E-Mail-Kampagnen ein. Dieser Link sollte für Menschen nicht sichtbar sein, z. B. weißer Text auf weißem Hintergrund oder ein Interpunktionszeichen. Bots neigen dazu, alle Links anzuklicken. Daher können Sie davon ausgehen, dass Nutzer:innen, die Klick-Events auf dem unsichtbaren Link generieren, tatsächlich das Ergebnis von NHI sind – die Öffnung oder der Klick deutet also nicht unbedingt auf positives Engagement hin.

{% elsif include.channel == "in-app message" %}

#### Metriken für In-App-Nachrichten {#in-app-message-metrics}

Im Folgenden finden Sie einige wichtige Metriken für In-App-Nachrichten, die Sie in Ihren Analytics sehen können. Die vollständigen Definitionen aller in Braze verwendeten Metriken für In-App-Nachrichten finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert note %}
Die Berichterstattung für _Button 1 Clicks_ und _Button 2 Clicks_ funktioniert nur, wenn Sie in der In-App-Nachricht den **Identifier for Reporting** auf „0“ bzw. „1“ setzen.

![Das Feld „Identifier for Reporting“ mit dem Wert „0“.]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Metriken für In-App-Nachrichten">
    <caption class="sr-only">In-App-Nachrichten-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Body Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Button 1 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Button 2 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversions (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Total Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Conversion Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Close Message</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

#### Abweichungen zwischen Kontrollgruppen und Varianten

Wenn eine In-App-Nachrichten-Kampagne eine 50/50-Variantenaufteilung hat, kann die Kontrollgruppe manchmal einen etwas höheren Prozentsatz aufweisen als die Variante (z. B. 51 % für die Kontrollgruppe und 49 % für die Variante). Diese Abweichung wird durch einen Unterschied in der Rendering-Zeit verursacht – zum Beispiel wenn Varianten-Nachrichten große Bilder oder templated Connected-Content verwenden und Nutzer:innen die Seite verlassen, bevor das Rendering abgeschlossen ist, während die Kontrollgruppe Impressionen protokolliert, ohne eine Nachricht anzuzeigen.

Die Verteilung zwischen Kontroll- und Variantengruppen ist grundsätzlich annähernd gleichmäßig, aber die Zuweisung zu einer Variante erfolgt erst, wenn die In-App-Nachricht tatsächlich an das Gerät gesendet wird. Einige Nutzer:innen lösen die In-App-Nachricht möglicherweise nie aus (z. B. weil sie die Aktion, die das erforderliche angepasste Event triggert, nie ausführen), was zu Unterschieden in den Gruppengrößen führen kann.

{% elsif include.channel == "KakaoTalk" %}

### KakaoTalk-Metriken {#kakaotalk-metrics}

Im Folgenden finden Sie einige wichtige KakaoTalk-Metriken, die Sie in Ihren Analytics sehen können. Weitere Details finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert note %}
Derzeit sind für KakaoTalk-Kampagnen keine geschätzten oder exakten Zielgruppenstatistiken verfügbar.
{% endalert %}

| Begriff | Definition |
| --- | --- |
| Zielgruppe | _Zielgruppe_ ist der Prozentsatz der Nutzer:innen, die eine bestimmte Nachricht erhalten haben. <br><br>_(Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)_ |
| Eindeutige Empfänger:innen | _Eindeutige Empfänger:innen_ ist die Anzahl der eindeutigen täglichen Empfänger:innen, also Nutzer:innen, die an einem Tag eine neue Nachricht erhalten haben. Damit dieser Zähler für eine Nutzer:in mehr als einmal erhöht wird, muss die Nutzer:in an einem anderen Tag eine neue Nachricht erhalten. Diese Zahl basiert auf der `user_id`. Weitere Details finden Sie unter [Eindeutige Empfänger:innen im Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics#unique-recipients). |
| Sendungen | Die Gesamtzahl der in einer Kampagne gesendeten Nachrichten. Dies bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde. |
| Klicks gesamt | Die Gesamtzahl der Male, die die gesendeten KakaoTalk-Nachrichten von Nutzer:innen angeklickt wurden. |
| Fehler | _Fehler_ ist die Anzahl der vom KakaoTalk-Anbieter zurückgegebenen Fehler (wird während des Sendevorgangs erhöht). |
| Umsatz | _Umsatz_ ist der Umsatz in Dollar von Kampagnenempfänger:innen innerhalb des festgelegten primären Konversionsfensters. |
| Primäre Konversionen | _Primäre Konversionen_ ist die Anzahl der Male, die ein definiertes Ereignis nach der Interaktion mit oder dem Anzeigen einer empfangenen Nachricht aus einer Braze-Kampagne aufgetreten ist. Dieses definierte Ereignis wird von Ihnen beim Erstellen der Kampagne festgelegt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KakaoTalk-Metriken" }

{% elsif include.channel == "push" %}

#### Push-Metriken {#push-metrics}

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller Push-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Filtern Sie dort nach Push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Push-Metriken">
    <caption class="sr-only">Push-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} Siehe <a href="#bounced-push">Zurückgewiesene Push-Benachrichtigungen</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direct Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> Die Zustellung von Benachrichtigungen erfolgt nach dem „Best-Effort“-Prinzip durch die Apple Push Notification Services (APNs). Sie ist nicht dazu gedacht, Daten an Ihre App zu liefern, sondern nur die Nutzer:in darüber zu informieren, dass neue Daten verfügbar sind. Der wichtige Unterschied ist, dass wir anzeigen, wie viele Nachrichten wir erfolgreich an APNs zugestellt haben – nicht unbedingt, wie viele APNs erfolgreich an Geräte zugestellt hat.

##### Tracking von Abmeldungen {#tracking-unsubscribes}

Push-Abmeldungen werden nicht als Metrik in die Kampagnen-Analytics einbezogen und hängen von Updates des Push-Status einer Nutzer:in durch Anbieter wie Apple oder Google ab. Diese Updates können unregelmäßig und unvorhersehbar sein. Daher werden Push-Abmeldungen nicht als Metrik in den Push-Kampagnen-Analytics berücksichtigt.

Dennoch kann das manuelle Tracking von Push-Abmeldungen wertvolle Insights über die Reaktionen der Nutzer:innen auf Ihre Benachrichtigungshäufigkeit und die Relevanz der Inhalte liefern. Es gibt zwei Möglichkeiten für das Tracking von Push-Abmeldungen: Segmentfilter oder angepasste Filter.

{% tabs local %}
{% tab Segmentfilter %}

Sie können ein Segment erstellen, um Nutzer:innen zu identifizieren, die keine Push-Benachrichtigungen aktiviert haben – also nicht abonniert oder per Opt-in registriert sind und kein [Vordergrund-Push-Token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration#push-tokens) besitzen. Um beispielsweise die Anzahl der Abmeldungen in Ihrer App anzuzeigen, verwenden Sie eine „ODER“-Kombination der folgenden Segmente:

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![Der Abschnitt „Segment Builder“ mit dem Filter „Background or Foreground Push Enabled for App“ für eine App ist „false“, und der Filter „Has Uninstalled“ ist ausgewählt.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Bitte beachten Sie, dass die Segmentierungsfilter nur Näherungswerte liefern und nicht konkret mit einem Datum und einer Kampagne verknüpft werden können.

{% endtab %}
{% tab Angepasste Filter %}

{% alert important %}
Das Protokollieren eines angepassten Events für Abo-Änderungen verbraucht [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Verwenden Sie alternativ Segmentfilter, um Nutzer:innen zu identifizieren und zu targetieren, die nicht Push-aktiviert sind.
{% endalert %}

Als weitere Möglichkeit empfehlen wir, ein angepasstes Event für Push-Abmeldungen zu erstellen, das darauf basiert, ob der Push-Aktivierungsstatus einer Nutzer:in `true` oder `false` ist, um diese Metrik zu verfolgen.

{% endtab %}
{% endtabs %}

##### Öffnungen verstehen {#understanding-opens}

Auch wenn _Direct Opens_ und _Influenced Opens_ das Wort „Opens“ enthalten, handelt es sich um unterschiedliche Metriken. _Direct Opens_ bezieht sich auf das direkte Öffnen einer Push-Benachrichtigung. _Influenced Opens_ bezieht sich auf das Öffnen einer App, ohne dass eine Push-Benachrichtigung innerhalb eines bestimmten Zeitraums nach Erhalt geöffnet wurde. _Influenced Opens_ bezieht sich also auf App-Öffnungen, nicht auf das Öffnen von Push-Benachrichtigungen.

##### Push-Action-Buttons und Berichterstattung {#push-action-buttons-and-reporting}

Wenn Sie [Push-Action-Buttons]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons) hinzufügen, kann das Panel **Push Performance** neben Metriken wie **Direct Opens** auch **Body Clicks**, **Button 1 Clicks** und **Button 2 Clicks** enthalten. Diese Spalten messen unterschiedliche Interaktionen – vergleichen Sie sie daher bei der Interpretation des Engagements.

_Direct Opens_ spiegelt die Dashboard-Metriken für Interaktionen wider, die als direkte Öffnung Ihrer Nachricht gezählt werden. **Push Notification Open**-Events in [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) oder Snowflake beschreiben Push-Interaktionen umfassender und können optionale Felder wie `button_action_type` (z. B. `close`) und `button_string` enthalten. Felddefinitionen finden Sie unter [Push Notification Open-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#push-notification-open-events).

Für **iOS** verwenden die Standard-Benachrichtigungskategorien von Braze (wie **Yes** / **No**, **Accept** / **Decline** oder **Confirm** / **Cancel**) eine feste Zuordnung: Die erste Aktion unterstützt `OPEN_APP`, eine URI oder einen Deeplink (entsprechend dem **On-Click Behavior** im Composer). Die Begleitaktion verwendet standardmäßig `CLOSE` – sie schließt die Benachrichtigung und öffnet die App nicht. Siehe die Standardzuordnung unter [Apple Push-Action-Button-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-action-button-object-for-braze-default-buttons).

Aus diesem Grund werden Taps auf den abweisenden voreingestellten Button (z. B. **No** oder **Decline**) in der Regel **nicht** als _Direct Opens_ gezählt. Diese Taps können dennoch in **Push Notification Open**-Exporten erscheinen, wenn sie protokolliert werden, wobei `button_action_type` auf `close` und `button_string` die getippte Aktion identifiziert. Wenn Sie Kampagnen-Analytics mit Warehouse-Daten vergleichen, verwenden Sie diese Payload-Felder, damit Sie abweisende Taps nicht mit Taps auf den Nachrichtentext oder die primäre Aktion gleichsetzen.

Für **Android** legen Sie das **On-Click Behavior** pro Button fest (**Open App**, **Redirect to Web URL** oder **Deep Link**), sodass die Berichterstattung den von Ihnen konfigurierten Aktionen folgt und nicht der iOS-Standard-Aufteilung `OPEN_APP` / `CLOSE`.

##### Warum Push-Sendungen die Zahl der eindeutigen Empfänger:innen übersteigen können {#why-push-sends-can-exceed-unique-recipients}

Die Anzahl der _Sendungen_ kann die Anzahl der _eindeutigen Empfänger:innen_ aus folgenden Gründen übersteigen:

- **Wiederzulassung ist aktiviert:** Wenn die Wiederzulassung in Ihren Kampagnen- oder Canvas-Einstellungen aktiviert ist, können Nutzer:innen, die das Segment und die Zustellungskriterien erfüllen, dieselbe Push-Benachrichtigung mehrmals erhalten. Dies führt zu einer höheren Gesamtzahl an Sendungen.
- **Nutzer:innen haben mehrere Geräte:** Wenn die Wiederzulassung nicht aktiviert ist, kann der Unterschied dadurch erklärt werden, dass Nutzer:innen mehrere Geräte mit ihrem Profil verknüpft haben. Eine Nutzer:in könnte zum Beispiel sowohl ein Smartphone als auch ein Tablet besitzen, und die Push-Benachrichtigung wird an alle registrierten Geräte gesendet. Jede Zustellung zählt als eine Sendung, aber es wird nur eine eindeutige Empfänger:in erfasst.
- **Nutzer:innen sind mehreren Apps zugewiesen:** Wenn Nutzer:innen mit mehr als einer App verbunden sind (z. B. beim Testen einer neuen App), erhalten sie möglicherweise dieselbe Push-Benachrichtigung in jeder App. Dies trägt zu einer höheren Anzahl von Sendungen bei.

##### Warum Bounces auftreten {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

Bounces treten bei Apple Push Notification Services (APNs) auf, wenn eine Push-Benachrichtigung versucht, an ein Gerät zugestellt zu werden, auf dem die gewünschte App nicht installiert ist. APNs hat außerdem das Recht, Token für Geräte beliebig zu ändern. Wenn Sie versuchen, an das Gerät einer Nutzer:in zu senden, deren Push-Token sich zwischen der Registrierung (z. B. zu Beginn jeder Sitzung, wenn wir eine Nutzer:in für ein Push-Token manuell registrieren) und dem Zeitpunkt des Sendens geändert hat, führt dies zu einem Bounce.

Wenn eine Nutzer:in Push in den Geräteeinstellungen deaktiviert, erkennt das SDK beim nächsten Öffnen der App, dass Push deaktiviert wurde, und benachrichtigt Braze. An diesem Punkt aktualisieren wir den Push-Aktivierungsstatus auf „deaktiviert“. Wenn eine deaktivierte Nutzer:in eine Push-Kampagne erhält, bevor sie eine neue Sitzung hat, wird die Kampagne erfolgreich gesendet und erscheint als zugestellt. Der Push wird für diese Nutzer:in nicht bouncen. Bei einer nachfolgenden Sitzung weiß Braze bereits, ob ein Vordergrund-Token vorhanden ist, sodass keine Benachrichtigung gesendet wird.

Push-Benachrichtigungen, die vor der Zustellung ablaufen, gelten nicht als fehlgeschlagen und werden nicht als Bounce registriert.

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging (FCM) Bounces können in drei Fällen auftreten:

| Szenario | Beschreibung |
| -- | -- |
| Deinstallierte Anwendungen | Wenn eine Nachricht versucht, an ein Gerät zugestellt zu werden, und die vorgesehene App auf diesem Gerät deinstalliert ist, wird die Nachricht verworfen und die Registrierungs-ID des Geräts wird ungültig. Alle weiteren Versuche, das Gerät zu benachrichtigen, geben den Fehler NotRegistered zurück. |
| Gesicherte Anwendung | Wenn eine Anwendung gesichert wird, kann ihre Registrierungs-ID ungültig werden, bevor die Anwendung wiederhergestellt wird. In diesem Fall speichert FCM die Registrierungs-ID der Anwendung nicht mehr und die Anwendung empfängt keine Nachrichten mehr. Registrierungs-IDs sollten daher **nicht** gespeichert werden, wenn eine Anwendung gesichert wird. |
| Aktualisierte Anwendung | Wenn eine Anwendung aktualisiert wird, funktioniert die Registrierungs-ID der vorherigen Version möglicherweise nicht mehr. Daher sollte eine aktualisierte Anwendung ihre bestehende Registrierungs-ID ersetzen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Warum Bounces auftreten" }

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS-, MMS- und RCS-Metriken {#sms-mms-and-rcs-metrics}

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller SMS-, MMS- und RCS-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Filtern Sie dort nach SMS/MMS und RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="SMS-, MMS- und RCS-Metriken">
    <caption class="sr-only">SMS-, MMS- und RCS-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Delivery Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Confirmed Delivery</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rejections</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Opt-Out</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Help</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Webhook-Metriken {#webhook-metrics}

Hier sind einige wichtige Webhook-Metriken, die Sie in Ihren Analytics sehen können. Die vollständigen Definitionen aller in Braze verwendeten Webhook-Metriken finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Webhook-Metriken">
    <caption class="sr-only">Webhook-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Unique Recipients</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Errors</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp-Metriken {#whatsapp-metrics}

Hier sind einige wichtige WhatsApp-Metriken, die Sie in Ihren Analytics sehen können. Die vollständigen Definitionen aller in Braze verwendeten WhatsApp-Metriken finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="WhatsApp-Metriken">
    <caption class="sr-only">WhatsApp-Performance-Metriken</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Deliveries</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Reads</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

Wenn die Fehlerrate erhöht ist, lesen Sie [WhatsApp-Sendefehler untersuchen]({{site.baseurl}}/user_guide/channels/whatsapp/send_failures).

#### Metriken zu Sperrung und Meldung durch Endnutzer:innen {#end-user-blocking-and-reporting-metrics}

Über das [Dashboard des WhatsApp Managers](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx) können Sie auf weitere Metriken zugreifen. Allerdings ist eine [Bestätigung Ihres Zugriffs](https://www.facebook.com/business/help/218116047387456) erforderlich, um alle verfügbaren Insights einzusehen.

{% endif %}

### Historische Performance {#historical-performance}

Im Panel **Historical Performance** können Sie die Metriken aus dem Panel **Message Performance** als Diagramm im Zeitverlauf betrachten. Verwenden Sie die Filter am oberen Rand des Panels, um die angezeigten Statistiken und Kanäle zu ändern. Der Zeitraum dieses Diagramms entspricht immer dem oben auf der Seite angegebenen Zeitraum.

Um eine tagesgenaue Aufschlüsselung zu erhalten, klicken Sie auf das <i class="fas fa-bars"></i> Hamburger-Menü und wählen Sie **Download CSV**, um einen CSV-Export des Berichts zu erhalten.

![Ein Diagramm des Panels „Historical Performance“ mit Beispielstatistiken für eine E-Mail von Februar 2021 bis Mai 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Wenn Sie sich dafür entscheiden, nur an Nutzer:innen zu senden, die die neueste Braze-Version der In-App-Nachrichten (Generation 3) sehen können, wird Ihre **Zielgruppe** nicht entsprechend Ihrer Auswahl angepasst.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Schlüsselwort-Antworten {#keyword-responses}

Das Panel **Keyword Responses** zeigt Ihnen eine Zeitleiste der eingehenden Schlüsselwörter, mit denen Nutzer:innen nach Erhalt Ihrer Nachricht geantwortet haben.

![Das Panel „Kampagnenebene – SMS/MMS/RCS Keyword Responses“ mit einem Liniendiagramm zur Verteilung der Schlüsselwörter im Zeitverlauf und einem Abschnitt „Keyword Categories“ mit ausgewählten Kontrollkästchen für Opt-In, Opt-Out, Help, Other, More und Coaching.]({% image_buster /assets/img/sms/keyword_responses.png %})

Hier können Sie auch die Antwortverteilung für jede Schlüsselwort-Kategorie einsehen, um die nächsten Schritte für das [Retargeting]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns) festzulegen und bequem [ein Segment zu erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

![Eine Tabelle mit Spalten für Keyword Category, Response Distribution und Retargeting, wobei Sie die Möglichkeit haben, ein Segment mit der Schlüsselwort-Kategorie zu erstellen.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Details zum Konversions-Event {#conversion-event-details}

Das Panel **Conversion Event Details** zeigt Ihnen die Performance Ihrer Konversions-Events für Ihre Kampagne. Weitere Informationen finden Sie unter [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events#step-3-view-results).

![Das Panel „Conversion Event Details“.]({% image_buster /assets/img/cc-conversion.png %})

### Konversionskorrelation {#conversion-correlation}

Das Panel **Conversion Correlation** gibt Ihnen Aufschluss darüber, welche Nutzerattribute und Verhaltensweisen die von Ihnen für Kampagnen festgelegten Ergebnisse fördern oder beeinträchtigen. Weitere Informationen finden Sie unter [Konversionskorrelation]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation).

![Das Panel „Conversion Correlation“ mit einer Analyse der Nutzerattribute und des Verhaltens aus dem primären Konversions-Event – A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## Berichts-Builder {#report-builder}

Sie können auch den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, um benutzerdefinierte Berichte für Ihre KakaoTalk-Kampagnen zu erstellen. Beim Erstellen eines Berichts können Sie filtern, um nur KakaoTalk-Kampagnen einzubeziehen, indem Sie unter **Channels** die Option **KakaoTalk** auswählen oder nach Tags filtern, die Sie Ihren KakaoTalk-Kampagnen zugewiesen haben.

{% endif %}

{% if include.channel == "whatsapp" %}

### Meta-Analytics

Zusätzlich zu den Braze-Analytics können Sie im WhatsApp Business Manager:in auf Analytics auf Template-Ebene zugreifen. Weitere Informationen finden Sie in der [Dokumentation von Meta](https://www.facebook.com/business/help/218116047387456).

{% endif %}

{% if include.channel == "SMS" %}

### SMS-Currents-Events

Wie bei E-Mails empfängt Braze Ereignisse auf Nutzerebene im Zusammenhang mit einer SMS-Nachricht auf ihrem Weg zur Nutzer:in. Alle eingehenden SMS-Ereignisse werden auch als Currents-Event über das Ereignis [SMS InboundReceived]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) gesendet. So können Sie zusätzliche Aktionen durchführen oder Berichte zu den Nachrichten erstellen, die Ihre Nutzer:innen außerhalb der Braze-Plattform senden.

{% alert note %}
Eingehende Nachrichten werden nach 1.600 Zeichen abgeschnitten.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Bindungsbericht {#retention-report}

Bindungsberichte zeigen Ihnen die Raten, mit denen Ihre Nutzer:innen ein ausgewähltes Bindungs-Ereignis über Zeiträume in einer bestimmten Kampagne{% if include.channel != "banner" %} oder Canvas{% endif %} durchgeführt haben. Weitere Informationen finden Sie unter [Bindungsberichte]({{site.baseurl}}/user_guide/analytics/reports/retention_reports).

## Funnel-Bericht {#funnel-report}

Funnel-Berichte bieten einen visuellen Bericht, mit dem Sie die Journeys Ihrer Kund:innen nach dem Erhalt einer Kampagne{% if include.channel != "banner" %} oder Canvas{% endif %} analysieren können. Wenn Ihre Kampagne {% if include.channel != "banner" %}oder Canvas {% endif %}eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie nachvollziehen, wie sich die verschiedenen Varianten auf den Konversions-Funnel ausgewirkt haben, und auf Grundlage dieser Daten optimieren.

Weitere Informationen finden Sie unter [Funnel-Berichte]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports).

{% endif %}