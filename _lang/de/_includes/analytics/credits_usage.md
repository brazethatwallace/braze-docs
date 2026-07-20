# Dashboard zur Nutzung von Credits {#credits-usage-dashboard}

> Das Dashboard zur Nutzung von Credits bietet Self-Service-Insights zu Ihrer Credit-Nutzung und ermöglicht einen umfassenden Überblick über die historische und aktuelle Nutzung im Vergleich zu den vertraglich vereinbarten Kontingenten. Diese Insights können Unklarheiten reduzieren und Ihnen helfen, Anpassungen vorzunehmen, um Überschreitungsrisiken zu vermeiden.

Das Dashboard **Credits Usage** ist in zwei Abschnitte unterteilt:
- [Übersicht der Credits-Nutzung](#credits-usage-overview)
- [Kanal-Tabs](#credits-features)

Rufen Sie das Dashboard auf, indem Sie zu **Einstellungen** > **Billing** > **Credits Usage** navigieren.

## Übersicht der Credits-Nutzung {#credits-usage-overview}

**Message credit usage overview** bietet eine Übersicht über die Nutzung aller Kanäle, die Credits verwenden. Sie können sehen, wie Ihr Verbrauch im Verhältnis zu Ihrem gesamten Credit-Kontingent steht, und Details zu Ihrem aktiven Vertrag und Ihrem Vertragszeitraum einsehen.

Diese Seite wird angezeigt, wenn Sie einen Credits-Vertrag haben. Die Kanäle, die Credits verwenden, werden unter **Credits usage** angezeigt.

{% alert note %}
Wenn Sie WhatsApp erworben haben, aber keinen Credits-Vertrag haben, wird der Credit-Verbrauch für WhatsApp trotzdem angezeigt, da ältere WhatsApp-Verträge auf diese Weise abgerechnet werden. Dies unterscheidet sich von älteren SMS-Verträgen, bei denen Credits nur verbraucht werden, wenn Sie einen Credits-Vertrag haben.
{% endalert %}

Die Übersichtsdaten zur Credits-Nutzung sind auf den Vertragszeitraum beschränkt, der in der **Credits contract overview** angezeigt wird. Sie können keinen Datumsbereich außerhalb des **Credits period** filtern.


### Credits-Nutzung über den Vertragszeitraum {#credits-usage-over-contract}

Das Diagramm **Message credits usage over contract** zeigt Ihre Nutzung über den ausgewählten Zeitraum. Die Granularität dieses Charts hängt vom ausgewählten Zeitrahmen ab. Exportoptionen können Sie über das Menü im Chart aufrufen.

![Diagramm zur Credit-Nutzung über den Vertragszeitraum.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %})

## Tab „Übersicht“ {#overview-tab}

Der Tab **Overview Usage** zeigt die Credit-Nutzung über alle Kanäle, die für Ihr Unternehmen relevant sind. Wenn Sie beispielsweise kein WhatsApp haben, wird der entsprechende Tab nicht angezeigt.

### Credits-Features {#credits-features}

In den folgenden Tabs finden Sie Details zu den Informationen, die für jedes Feature angezeigt werden, das Credits verbraucht.

{% tabs %}
{% tab Banner %}

### Banner {#banners}

**Banners Credits Usage** zeigt die Credit-Nutzung für Banner über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die täglichen eindeutigen Impressionen. Die Tabelle **Usage by account** enthält **Braze workspace**, **Daily unique impressions**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter {#filters}

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Banner-Credits-Nutzung mit Kacheln für Credits und eindeutige Impressionen sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_banners.png %})

{% endtab %}
{% tab Content Cards %}

### Content Cards

**Content Cards Credits Usage** zeigt die Credit-Nutzung für Content Cards über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die täglichen eindeutigen Impressionen. Die Tabelle **Usage by account** enthält **Braze workspace**, **Card type**, **Daily Unique Impressions**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace
- Kartentyp

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Content-Cards-Credits-Nutzung mit Kacheln für Credits und eindeutige Impressionen sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_content_cards.png %})

{% endtab %}
{% tab E-Mail %}

### E-Mail {#email}

**Email Credits Usage** zeigt die Credit-Nutzung für E-Mails über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl gesendeter E-Mails. Die Tabelle **Usage by account** enthält **Braze workspace**, **Email sent**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![E-Mail-Credits-Nutzung mit Kacheln für Credits und gesendete E-Mails sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_email.png %})

{% endtab %}
{% tab KakaoTalk %}

### KakaoTalk

**KakaoTalk Credits Usage** zeigt die Credit-Nutzung für KakaoTalk über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der KakaoTalk-Sendungen. Die Tabelle im Abschnitt **KakaoTalk** enthält **Braze workspace**, **Month**, **Year**, **Company**, **Sends**, **Credit Ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace
- Monat
- Jahr
- Unternehmen

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![KakaoTalk-Credits-Nutzung mit Kacheln für Credits und KakaoTalk-Sendungen sowie einer KakaoTalk-Nutzungstabelle.]({% image_buster /assets/img/app_settings/credits_usage_kakaotalk.png %})

{% endtab %}
{% tab LINE %}

### LINE

**LINE Credits Usage** zeigt die Credit-Nutzung für LINE über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der abrechenbaren Sendungen. Die Tabelle im Abschnitt **Line** enthält **Braze workspace**, **Month**, **Year**, **Company**, **Destination**, **Billable sends**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace
- Monat
- Jahr
- Unternehmen
- Ziel

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![LINE-Credits-Nutzung mit Kacheln für Credits und abrechenbare Sendungen sowie einer detaillierten Nutzungstabelle.]({% image_buster /assets/img/app_settings/credits_usage_line.png %})

{% endtab %}
{% tab SMS, MMS und RCS %}

### SMS, MMS und RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** zeigt die Aufschlüsselung der Nutzung für den SMS-, MMS- und RCS-Kanal. Die Spalten **Credit ratio** und **Credits** geben den jeweiligen Ländertarif und die verbrauchten Credits an. Zusätzlich zeigen übergeordnete Kacheln den gesamten SMS- und, falls relevant, MMS-Verbrauch über den ausgewählten Datumsbereich.

Es stehen Filter zur Verfügung, mit denen Sie nach **Land** oder SMS- und RCS-Typ filtern können.

![SMS/MMS/RCS-Credits-Nutzung mit Kacheln für übergeordnete Daten und einem Abschnitt zum Verbrauch nach Konto.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %})

Im Gegensatz zur **Credits Usage Overview** enthält dieser Abschnitt historische Daten aus früheren Vertragszeiträumen.

{% alert note %}
Es ist möglich, einen Datumsbereich auszuwählen, der sowohl Nicht-Credits- als auch Credits-Nutzung enthält. In diesem Fall wird der Verbrauch, der außerhalb von Credits stattfand, in den Spalten **Credit ratio** und **Credits** als `—` (null) angezeigt.
{% endalert %}

![SMS/MMS/RCS-Credits-Nutzungstabelle mit Nullwerten.]({% image_buster /assets/img/app_settings/sms_table_null3.png %})

{% endtab %}
{% tab Webhooks %}

### Webhooks

**Webhooks Credits Usage** zeigt die Credit-Nutzung für Webhooks über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der Webhook-Sendungen. Die Tabelle **Usage by account** enthält **Braze workspace**, **Sends**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Webhooks-Credits-Nutzung mit Kacheln für Credits und Webhook-Sendungen sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_webhooks.png %})

{% endtab %}
{% tab WhatsApp %}

### WhatsApp

**WhatsApp Credits Usage** zeigt die Aufschlüsselung der Nutzung für den WhatsApp-Kanal. Die Kacheln zeigen den gesamten WhatsApp-Credit-Verbrauch, der im Abschnitt **Usage by account** aufgeschlüsselt werden kann, indem Sie Filter anwenden, um die Datentabelle auf einen bestimmten Workspace einzuschränken.

#### Filter

Sie können Ihre Daten filtern nach:
- Land
- WhatsApp Business-Konto
- Braze Workspace
- Konversationskategorietyp
- Region

![WhatsApp-Credits-Nutzung mit einer Kachel für insgesamt verbrauchte Credits und einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %})

{% endtab %}
{% tab Credit-Verhältnisse %}

### Credit-Verhältnisse {#credit-ratios}

**Credit Ratios** zeigt Credit-Verhältnisse über verschiedene Kanäle und Ziele hinweg. Auf dieser Seite gibt es keine Zusammenfassungskacheln und keine **Date range**-Steuerung. Die Tabelle **Credit ratios** enthält **Channel grouping**, **Destination** und **Credit ratio**.

#### Filter

Sie können Ihre Daten filtern nach:
- Kanalgruppierung
- Ziel

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Seite „Credit Ratios“ mit einer Credit-Verhältnistabelle und Filtern für Kanal und Ziel.]({% image_buster /assets/img/app_settings/credits_usage_credit_ratios.png %})

{% endtab %}
{% tab Agentenkonsole %}

### Agentenkonsole {#agent-console}

**Agent Console Credits Usage** zeigt die Credit-Nutzung der Agentenkonsole über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der Aufrufe. Die Tabelle **Usage by account** enthält **Braze workspace**, **Agent name**, **Model owner**, **Total invocations**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

Um die täglichen Ausgaben vor dem Start zu planen, vergleichen Sie diese Verhältnisse mit dem **Daily action credit cost limit** jedes Agenten in der Agentenkonsole (tägliches Aufruflimit × Credit-Verhältnis). Siehe [Tägliche Aufruf- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace
- Agentenname
- Modelleigentümer

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Agentenkonsole-Credits-Nutzung mit Kacheln für Credits und Aufrufe sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_agent_console.png %})

{% endtab %}
{% tab Audience Sync %}

### Audience Sync

**Audience Sync Credits Usage** zeigt die Credit-Nutzung für Audience Sync über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der Audience Syncs. Die Tabelle **Usage by account** enthält **Braze workspace**, **Provider**, **Total syncs**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace
- Anbieter

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Audience-Sync-Credits-Nutzung mit Kacheln für Credits und Audience Syncs sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_audience_sync.png %})

{% endtab %}
{% tab Nachrichtenarchivierung %}

### Nachrichtenarchivierung {#message-archiving}

**Message Archiving Credits Usage** zeigt die Credit-Nutzung für die Nachrichtenarchivierung über alle Konten hinweg. Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl archivierter Nachrichten. Die Tabelle **Usage by account** enthält **Braze workspace**, **Channel**, **Messages archived**, **Credit ratio** und **Credits**. Wenn Daten verfügbar sind, zeigt **Last updated** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (Standard: letzte 30 Tage)
- Braze Workspace
- Kanal

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Nachrichtenarchivierung-Credits-Nutzung mit Kacheln für Credits und archivierte Nachrichten sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_message_archiving.png %})

{% endtab %}
{% endtabs %}

## Wissenswertes {#things-to-know}

{% alert important %}
Die im Dashboard **Credits Usage** angezeigten Daten beziehen sich auf die Vertragsebene und sind nicht auf ein einzelnes Dashboard-Unternehmen oder einen einzelnen Workspace beschränkt. Diese Daten spiegeln die Nutzung aller Workspaces innerhalb Ihres Dashboards wider – und möglicherweise über alle Dashboards hinweg (wenn Sie mehrere haben).
{% endalert %}

- Die zugrunde liegenden Daten werden täglich bereitgestellt, wobei die Datentabellen um 3:00 Uhr, 9:00 Uhr, 12:00 Uhr und 18:00 Uhr EST aktualisiert werden. Die Aktualisierung des Dashboards **Credits Usage** kann länger als 24 Stunden dauern.
- Braze verwendet die Standard-Rundungsmethodik: Zahlen werden auf die nächste Zehntelstelle aufgerundet.

### Auswahl des Datumsbereichs {#date-range-selection}

Das Dashboard **Credits Usage** schließt das Enddatum des ausgewählten Bereichs aus den Ergebnissen aus. Wenn Sie beispielsweise den 1.–31. Oktober auswählen, sind die Nutzungsstatistiken für den 31. Oktober nicht enthalten. Um den letzten Tag Ihres gewünschten Zeitraums einzuschließen, erweitern Sie den Bereich um einen Tag. Um beispielsweise den gesamten Oktober einzuschließen, wählen Sie 1. Oktober–1. November.

### Vergleich mit Drittanbietern {#comparing-with-third-party-providers}

Beim Vergleich der Braze-Credits-Nutzungsdaten mit Drittanbietern (wie Infobip) sollten Sie Folgendes beachten:

- **Nachrichtensegmente versus Nachrichten**: Braze zählt SMS-Nachrichten nach Segmenten. Eine einzelne SMS-Nachricht, die in mehrere Segmente aufgeteilt wird (z. B. aufgrund der Länge), wird in Braze als mehrere Segmente gezählt. Weitere Informationen finden Sie unter [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments).
- **Credit-basierte versus nicht-credit-basierte Nachrichten**: Das Dashboard enthält sowohl credit-basierte als auch nicht-credit-basierte Nachrichten. Drittanbieter zählen möglicherweise nur credit-basierte Nachrichten, was zu Abweichungen bei den Gesamtzahlen führen kann.
- **Eingehend versus ausgehend**: Stellen Sie sicher, dass Sie die gleichen Nachrichtentypen vergleichen. Einige Drittanbieter-Dashboards enthalten sowohl eingehende als auch ausgehende Nachrichten in ihren Gesamtzahlen, während Braze Ihnen ermöglicht, nach Richtung zu filtern.
- **Ausrichtung des Datumsbereichs**: Da das Dashboard das Enddatum ausschließt, können tagesweise Vergleiche genauer übereinstimmen als längere Datumsbereiche. Wenn Sie Daten für einen bestimmten Zeitraum vergleichen, erweitern Sie Ihren Braze-Datumsbereich um einen Tag, um den letzten Tag Ihres Vergleichszeitraums einzuschließen.