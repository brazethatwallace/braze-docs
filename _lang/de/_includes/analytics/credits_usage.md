# Dashboard zur Nutzung von Credits {#credits-usage-dashboard}

> Das Dashboard zur Nutzung von Credits bietet Self-Service-Insights zu Ihrer Credit-Nutzung und ermöglicht einen umfassenden Überblick über die historische und aktuelle Nutzung im Vergleich zu den vertraglich vereinbarten Kontingenten. Diese Insights können Unklarheiten reduzieren und Ihnen helfen, Anpassungen vorzunehmen, um Überschreitungsrisiken zu vermeiden.

Das Dashboard **Credits Usage** ist in zwei Abschnitte unterteilt:
- [Übersicht der Credits-Nutzung](#credits-usage-overview)
- [Kanal-Tabs](#credits-features)

Rufen Sie das Dashboard auf, indem Sie zu **Einstellungen** > **Billing** > **Credits Usage** navigieren.

## Übersicht zur Credit-Nutzung {#credits-usage-overview}

Die **Übersicht zur Nutzung von Nachrichten-Credits** bietet einen Überblick über die Nutzung aller Kanäle, die Credits verwenden. Sie können sehen, wie Sie im Verhältnis zu Ihrem gesamten Credit-Kontingent liegen, und Details zu Ihrem aktiven Vertrag sowie Ihrem Vertragszeitraum einsehen.

Diese Seite wird angezeigt, wenn Sie einen Credit-Vertrag haben. Die Kanäle, die Credits verwenden, werden unter **Credit-Nutzung** angezeigt.

{% alert note %}
Wenn Sie WhatsApp erworben haben, aber keinen Credit-Vertrag haben, wird Ihnen trotzdem der Credit-Verbrauch für WhatsApp angezeigt, da ältere WhatsApp-Verträge auf diese Weise abgerechnet werden. Dies unterscheidet sich von älteren SMS-Verträgen, bei denen Credits nur verbraucht werden, wenn Sie einen Credit-Vertrag haben.
{% endalert %}

Die Daten der Übersicht zur Credit-Nutzung sind auf den Vertragszeitraum beschränkt, der in der **Übersicht zum Credit-Vertrag** angezeigt wird. Sie können keinen Datumsbereich außerhalb des **Credit-Zeitraums** filtern.


### Credit-Nutzung über den Vertragszeitraum {#credits-usage-over-contract}

Das Diagramm **Nutzung von Nachrichten-Credits über den Vertragszeitraum** zeigt Ihre Nutzung über den ausgewählten Zeitraum an. Die Granularität dieses Charts hängt vom ausgewählten Zeitrahmen ab. Exportoptionen können Sie über das Menü im Chart-Menü aufrufen.

![Diagramm zur Credit-Nutzung über den Vertragszeitraum.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %})

## Tab „Übersicht“ {#overview-tab}

Der Tab **Übersicht zur Nutzung** zeigt die Credit-Nutzung über alle Kanäle hinweg, die für Ihr Unternehmen relevant sind. Wenn Sie beispielsweise WhatsApp nicht nutzen, wird der entsprechende Tab nicht angezeigt.

### Credit-Features {#credits-features}

In den folgenden Tabs finden Sie Details zu den Informationen, die für jedes Feature angezeigt werden, das Credits verbraucht.

{% tabs %}
{% tab Banner %}

### Banner {#banners}

**Banner-Credit-Nutzung** zeigt die Credit-Nutzung für Banner über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die täglichen eindeutigen Impressionen. Die Tabelle **Nutzung nach Konto** enthält **Braze-Workspace**, **Tägliche eindeutige Impressionen**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter {#filters}

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Banner-Credit-Nutzung mit Kacheln für Credits und eindeutige Impressionen sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_banners.png %})

{% endtab %}
{% tab Content Cards %}

### Content Cards

**Content-Cards-Credit-Nutzung** zeigt die Credit-Nutzung für Content Cards über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die täglichen eindeutigen Impressionen. Die Tabelle **Nutzung nach Konto** enthält **Braze-Workspace**, **Kartentyp**, **Tägliche eindeutige Impressionen**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace
- Kartentyp

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Content-Cards-Credit-Nutzung mit Kacheln für Credits und eindeutige Impressionen sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_content_cards.png %})

{% endtab %}
{% tab E-Mail %}

### E-Mail {#email}

**E-Mail-Credit-Nutzung** zeigt die Credit-Nutzung für E-Mail über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl gesendeter E-Mails. Die Tabelle **Nutzung nach Konto** enthält **Braze-Workspace**, **Gesendete E-Mails**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![E-Mail-Credit-Nutzung mit Kacheln für Credits und gesendete E-Mails sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_email.png %})

{% endtab %}
{% tab KakaoTalk %}

### KakaoTalk

**KakaoTalk-Credit-Nutzung** zeigt die Credit-Nutzung für KakaoTalk über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der KakaoTalk-Sendungen. Die Tabelle im Abschnitt **KakaoTalk** enthält **Braze-Workspace**, **Monat**, **Jahr**, **Unternehmen**, **Sendungen**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace
- Monat
- Jahr
- Unternehmen

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![KakaoTalk-Credit-Nutzung mit Kacheln für Credits und KakaoTalk-Sendungen sowie einer KakaoTalk-Nutzungstabelle.]({% image_buster /assets/img/app_settings/credits_usage_kakaotalk.png %})

{% endtab %}
{% tab LINE %}

### LINE

**LINE-Credit-Nutzung** zeigt die Credit-Nutzung für LINE über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der abrechenbaren Sendungen. Die Tabelle im Abschnitt **Line** enthält **Braze-Workspace**, **Monat**, **Jahr**, **Unternehmen**, **Ziel**, **Abrechenbare Sendungen**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace
- Monat
- Jahr
- Unternehmen
- Ziel

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![LINE-Credit-Nutzung mit Kacheln für Credits und abrechenbare Sendungen sowie einer detaillierten Nutzungstabelle.]({% image_buster /assets/img/app_settings/credits_usage_line.png %})

{% endtab %}
{% tab SMS, MMS und RCS %}

### SMS, MMS und RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS-Credit-Nutzung** zeigt die Aufschlüsselung der Nutzung für den SMS-, MMS- und RCS-Kanal. Die Spalten **Credit-Verhältnis** und **Credits** geben den jeweiligen Ländertarif und die verbrauchten Credits an. Zusätzlich zeigen übergeordnete Kacheln den gesamten SMS- und, falls relevant, MMS-Verbrauch über den ausgewählten Datumsbereich an.

Es stehen Filter zur Verfügung, mit denen Sie nach **Land** oder SMS- und RCS-Typ filtern können.

![SMS/MMS/RCS-Credit-Nutzung mit Kacheln für übergeordnete Daten und einem Abschnitt zum Verbrauch nach Konto.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %})

Im Gegensatz zur **Übersicht zur Credit-Nutzung** enthält dieser Abschnitt historische Daten aus früheren Vertragszeiträumen.

{% alert note %}
Es ist möglich, einen Datumsbereich auszuwählen, der sowohl Nutzung ohne Credits als auch Nutzung mit Credits enthält. In diesem Fall wird der Verbrauch, der außerhalb von Credits stattfand, in den Spalten **Credit-Verhältnis** und **Credits** als `—` (null) angezeigt.
{% endalert %}

![SMS/MMS/RCS-Credit-Nutzungstabelle mit Nullwerten.]({% image_buster /assets/img/app_settings/sms_table_null3.png %})

{% endtab %}
{% tab Webhooks %}

### Webhooks

**Webhooks-Credit-Nutzung** zeigt die Credit-Nutzung für Webhooks über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der Webhook-Sendungen. Die Tabelle **Nutzung nach Konto** enthält **Braze-Workspace**, **Sendungen**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Webhooks-Credit-Nutzung mit Kacheln für Credits und Webhook-Sendungen sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_webhooks.png %})

{% endtab %}
{% tab WhatsApp %}

### WhatsApp

**WhatsApp-Credit-Nutzung** zeigt die Aufschlüsselung der Nutzung für den WhatsApp-Kanal. Die Kacheln zeigen die gesamte WhatsApp-Credit-Nutzung, die im Abschnitt **Nutzung nach Konto** durch Anwenden von Filtern auf einen bestimmten Workspace aufgeschlüsselt werden kann.

#### Filter

Sie können Ihre Daten filtern nach:
- Land
- WhatsApp-Business-Konto
- Braze-Workspace
- Konversationskategorietyp
- Region

![WhatsApp-Credit-Nutzung mit einer Kachel für insgesamt verbrauchte Credits und einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %})

{% endtab %}
{% tab Credit-Verhältnisse %}

### Credit-Verhältnisse {#credit-ratios}

**Credit-Verhältnisse** zeigt die Credit-Verhältnisse über verschiedene Kanäle und Ziele hinweg. Es gibt keine Zusammenfassungskacheln und keine **Datumsbereich**-Steuerung auf dieser Seite. Die Tabelle **Credit-Verhältnisse** enthält **Kanalgruppierung**, **Ziel** und **Credit-Verhältnis**.

#### Filter

Sie können Ihre Daten filtern nach:
- Kanalgruppierung
- Ziel

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Seite „Credit-Verhältnisse“ mit einer Tabelle zu Credit-Verhältnissen und Filtern für Kanal und Ziel.]({% image_buster /assets/img/app_settings/credits_usage_credit_ratios.png %})

{% endtab %}
{% tab Agent Console %}

### Agent Console

**Agent-Console-Credit-Nutzung** zeigt die Credit-Nutzung für Agent Console über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der Aufrufe. Die Tabelle **Nutzung nach Konto** enthält **Braze-Workspace**, **Agent-Name**, **Modellanbieter**, **Aufrufe insgesamt**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

Um die täglichen Ausgaben vor dem Start zu planen, vergleichen Sie diese Verhältnisse mit dem **Täglichen Aktions-Credit-Kostenlimit** jedes Agenten in Agent Console (tägliches Aufruflimit × Credit-Verhältnis). Siehe [Tägliche Aufruf- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace
- Agent-Name
- Modellanbieter

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Agent-Console-Credit-Nutzung mit Kacheln für Credits und Aufrufe sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_agent_console.png %})

{% endtab %}
{% tab Audience Sync %}

### Audience Sync

**Audience-Sync-Credit-Nutzung** zeigt die Credit-Nutzung für Audience Sync über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl der Audience Syncs. Die Tabelle **Nutzung nach Konto** enthält **Braze-Workspace**, **Anbieter**, **Syncs insgesamt**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace
- Anbieter

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Audience-Sync-Credit-Nutzung mit Kacheln für Credits und Audience Syncs sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_audience_sync.png %})

{% endtab %}
{% tab Nachrichtenarchivierung %}

### Nachrichtenarchivierung {#message-archiving}

**Credit-Nutzung für Nachrichtenarchivierung** zeigt die Credit-Nutzung für die Nachrichtenarchivierung über alle Konten hinweg. Die Kacheln zeigen die insgesamt verbrauchten Credits und die Gesamtzahl archivierter Nachrichten. Die Tabelle **Nutzung nach Konto** enthält **Braze-Workspace**, **Kanal**, **Archivierte Nachrichten**, **Credit-Verhältnis** und **Credits**. Wenn Daten verfügbar sind, zeigt **Zuletzt aktualisiert** an, wann die Tabelle zuletzt aktualisiert wurde.

#### Filter

Sie können Ihre Daten filtern nach:
- Datumsbereich (standardmäßig die letzten 30 Tage)
- Braze-Workspace
- Kanal

Verwenden Sie **Export**, um die Tabellendaten herunterzuladen.

![Credit-Nutzung für Nachrichtenarchivierung mit Kacheln für Credits und archivierte Nachrichten sowie einer Tabelle zur Nutzung nach Konto.]({% image_buster /assets/img/app_settings/credits_usage_message_archiving.png %})

{% endtab %}
{% endtabs %}

## Wissenswertes {#things-to-know}

{% alert important %}
Die im Dashboard **Credits Usage** angezeigten Daten beziehen sich auf die Vertragsebene und sind nicht auf ein einzelnes Dashboard-Unternehmen oder einen einzelnen Workspace beschränkt. Diese Daten spiegeln die Nutzung aller Workspaces innerhalb Ihres Dashboards wider – und möglicherweise auch über alle Dashboards hinweg (falls Sie mehrere haben).
{% endalert %}

- Die zugrunde liegenden Daten werden täglich bereitgestellt, wobei die Datentabellen um 3:00 Uhr, 9:00 Uhr, 12:00 Uhr und 18:00 Uhr EST aktualisiert werden. Es kann länger als 24 Stunden dauern, bis das Dashboard **Credits Usage** aktualisiert wird.
- Wenn eine neue Vertragsperiode beginnt, kann es bis zu 24 Stunden dauern, bis aktualisierte Vertrags- und Nachrichten-Credit-Informationen angezeigt werden. Bis diese Daten geladen sind, zeigt das Dashboard möglicherweise nur den Tab **Credit Ratios** anstelle der vollständigen Übersicht und der kanalspezifischen Nutzungsdetails an.
- Braze verwendet die Standard-Rundungsmethodik: Zahlen werden auf die nächste Zehntelstelle aufgerundet.

### Auswahl des Datumsbereichs {#date-range-selection}

Das Dashboard **Credits Usage** schließt das Enddatum des ausgewählten Bereichs aus den Ergebnissen aus. Wenn Sie beispielsweise den 1.–31. Oktober auswählen, werden die Nutzungsstatistiken für den 31. Oktober nicht berücksichtigt. Um den letzten Tag Ihres gewünschten Zeitraums einzubeziehen, erweitern Sie den Bereich um einen Tag. Um beispielsweise den gesamten Oktober einzuschließen, wählen Sie den 1. Oktober bis 1. November aus.

### Vergleich mit Drittanbietern {#comparing-with-third-party-providers}

Beachten Sie beim Vergleich der Braze-Credit-Nutzungsdaten mit Drittanbietern (wie Infobip) Folgendes:

- **Nachrichtensegmente versus Nachrichten**: Braze zählt SMS-Nachrichten nach Segmenten. Eine einzelne SMS-Nachricht, die in mehrere Segmente aufgeteilt wird (z. B. aufgrund der Länge), wird in Braze als mehrere Segmente gezählt. Weitere Informationen finden Sie unter [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments).
- **Credit-basierte versus nicht-credit-basierte Nachrichten**: Das Dashboard umfasst sowohl credit-basierte als auch nicht-credit-basierte Nachrichten. Drittanbieter zählen möglicherweise nur credit-basierte Nachrichten, was zu Abweichungen bei den Gesamtzahlen führen kann.
- **Eingehend versus ausgehend**: Stellen Sie sicher, dass Sie dieselben Nachrichtentypen vergleichen. Einige Drittanbieter-Dashboards berücksichtigen sowohl eingehende als auch ausgehende Nachrichten in ihren Gesamtzahlen, während Braze es Ihnen ermöglicht, nach Richtung zu filtern.
- **Ausrichtung des Datumsbereichs**: Da das Dashboard das Enddatum ausschließt, können tageweise Vergleiche genauer übereinstimmen als längere Datumsbereiche. Wenn Sie Daten für einen bestimmten Zeitraum vergleichen, erweitern Sie Ihren Braze-Datumsbereich um einen Tag, um den letzten Tag Ihres Vergleichszeitraums einzubeziehen.