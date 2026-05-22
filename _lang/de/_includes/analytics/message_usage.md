# Dashboard zur Nachrichtenverwendung {#message-usage-dashboard}

> Das Dashboard zur Nachrichtenverwendung bietet Ihnen Self-Service-Insights über die Nutzung Ihres SMS-, RCS- und WhatsApp-Guthabens. So erhalten Sie einen umfassenden Überblick über die historische und aktuelle Nutzung im Vergleich zu den vertraglich festgelegten Kontingenten. Diese Insights können Unklarheiten ausräumen und Ihnen helfen, Anpassungen vorzunehmen, um Überschussrisiken zu vermeiden.

Das Dashboard **Message Usage** ist in drei Bereiche unterteilt:
- [Übersicht über die Credit-Nutzung](#credit-usage-overview)
- [SMS/MMS](#smsmms)
- [WhatsApp](#whatsapp)

Rufen Sie das Dashboard auf, indem Sie zu **Einstellungen** > **Billing** > **Message Usage** gehen.

## Übersicht über die Credit-Nutzung {#credits-usage-overview}

**Credits Usage Overview** bietet einen Überblick über die Nutzung aller Kanäle, die Credits verwenden. Sie können sehen, wie es um Ihre Credit-Gesamtmenge bestellt ist, und finden Details zu Ihrem aktiven Vertrag und Ihrer Vertragslaufzeit.

Diese Seite wird angezeigt, wenn Sie einen Vertrag über Nachrichtenguthaben abgeschlossen haben. Die Kanäle, die Nachrichtenguthaben verwenden, werden in der **Credits contract overview** angezeigt.

{% alert note %}
Wenn Sie WhatsApp gekauft haben, aber keinen Vertrag über Nachrichtenguthaben abgeschlossen haben, sehen Sie trotzdem den Guthabenverbrauch für WhatsApp, da dies die Art und Weise ist, wie ältere WhatsApp-Verträge abgerechnet werden. Dies unterscheidet sich von herkömmlichen SMS, die nur dann Guthaben verbrauchen, wenn Sie einen Vertrag über Nachrichtenguthaben abgeschlossen haben.
{% endalert %}

Die Daten der **Credits Usage Overview** beschränken sich auf die Vertragslaufzeit, die in der **Credits contract overview** angezeigt wird. Sie können nicht nach einem Datumsbereich außerhalb des **Credits-Zeitraums** filtern.

### Nutzung von Credits über den Vertrag {#credits-usage-over-contract}

Das Diagramm **Credits Usage over Contract** zeigt Ihre Nutzung über den ausgewählten Zeitraum an. Die Granularität dieses Charts hängt von dem von Ihnen gewählten Zeitrahmen ab. Exportoptionen finden Sie über das Menü in der oberen rechten Ecke des Charts.

![Dashboard „Credits Usage Overview“ mit Abschnitten für die Credit-Nutzung, die Übersicht über den Credit-Vertrag und den Credit-Verbrauch über den Vertrag.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS und RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** zeigt die Aufschlüsselung der Nutzung für die Kanäle SMS, MMS und RCS an. Die Spalten in der Datentabelle setzen in der Regel voraus, dass Sie Credits erworben haben (obwohl Braze vorübergehend noch ältere Abrechnungsmodelle unterstützt), und die Spalten **Credit ratio** und **Credits** geben den jeweiligen Ländersatz und die verbrauchten Credits an. Darüber hinaus zeigen übergeordnete Kacheln den gesamten SMS- und gegebenenfalls MMS-Verbrauch für den ausgewählten Zeitraum an.

Es sind Filter verfügbar, mit denen Sie nach **Country** oder SMS- und RCS-Typ filtern können.

![SMS/MMS/RCS Credits Usage mit Kacheln für übergeordnete Daten und einem Abschnitt für den Verbrauch pro Konto.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

Anders als die **Credits Usage Overview** enthält dieser Abschnitt historische Daten aus früheren Vertragszeiträumen.

{% alert note %}
Es ist möglich, einen Datumsbereich auszuwählen, der sowohl die Nutzung ohne Credits als auch mit Credits enthält. In diesem Fall wird der Verbrauch, der außerhalb des Credit-Vertrags stattgefunden hat, in den Spalten **Credit ratio** und **Credits** mit `—` (Null) angezeigt.
{% endalert %}

![SMS/MMS/RCS Credits Usage-Tabelle mit Nullwerten.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp {#whatsapp}

**WhatsApp Credits Usage** zeigt die Aufschlüsselung der Nutzung für den WhatsApp-Kanal. Die Kacheln zeigen die gesamte WhatsApp-Credit-Nutzung an, die im Abschnitt **Usage by account** aufgeschlüsselt werden kann, indem Sie Filter anwenden, um die Ergebnisse der Datentabelle auf einen bestimmten Workspace zu beschränken.

### Filter {#filters}

Sie können Ihre Daten filtern nach:
- Land
- WhatsApp-Business-Konto
- Braze-Workspace
- Gesprächskategorie-Typ
- Region

![WhatsApp Credits Usage mit einer Kachel für insgesamt verbrauchte Credits und einer Nutzungstabelle nach Konto.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## Was Sie wissen sollten {#things-to-know}

{% alert important %}
Die im Dashboard **Message Usage** angezeigten Daten beziehen sich auf die Vertragsebene und sind nicht auf ein einzelnes Dashboard-Unternehmen oder einen Workspace beschränkt. Diese Daten spiegeln die Nutzung aller Workspaces innerhalb Ihres Dashboards wider und möglicherweise auch aller Dashboards (wenn Sie mehrere haben).
{% endalert %}

- Die zugrundeliegenden Daten werden täglich bereitgestellt, wobei die Datentabellen um 3 Uhr, 9 Uhr, 12 Uhr und 18 Uhr EST aktualisiert werden. Das Update des Dashboards **Message Usage** kann länger als 24 Stunden dauern.
- Braze folgt der üblichen Rundungsmethodik: Zahlen werden auf das nächste Zehntel aufgerundet.

### Auswahl des Datumsbereichs {#date-range-selection}

Das Dashboard **Message Usage** schließt das Enddatum des ausgewählten Zeitraums aus den Ergebnissen aus. Wenn Sie beispielsweise den Zeitraum vom 1\. bis 31\. Oktober auswählen, werden die Nutzungsstatistiken für den 31\. Oktober nicht berücksichtigt. Um den letzten Tag Ihres gewünschten Zeitraums einzuschließen, erweitern Sie den Bereich um einen Tag. Um beispielsweise den gesamten Oktober einzubeziehen, wählen Sie den Zeitraum vom 1\. Oktober bis zum 1\. November aus.

### Vergleich mit Drittanbietern {#comparing-with-third-party-providers}

Bitte beachten Sie beim Vergleich der Braze-Nachrichtennutzungsdaten mit denen von Drittanbietern (wie Infobip) Folgendes:

- **Nachrichten-Segmente im Vergleich zu Nachrichten**: Braze zählt SMS-Nachrichten nach Segmenten. Eine einzelne SMS-Nachricht, die in mehrere Segmente unterteilt ist (beispielsweise aufgrund ihrer Länge), wird in Braze als mehrere Segmente gezählt. Weitere Informationen finden Sie unter [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- **Credit-basierte und nicht credit-basierte Nachrichten**: Das Dashboard enthält sowohl credit-basierte als auch nicht credit-basierte Nachrichten. Drittanbieter zählen möglicherweise nur credit-basierte Nachrichten, was zu Abweichungen in den Gesamtzahlen führen kann.
- **Eingehend vs. ausgehend**: Stellen Sie sicher, dass Sie die gleichen Nachrichtentypen vergleichen. Einige Dashboards von Drittanbietern berücksichtigen sowohl eingehende als auch ausgehende Nachrichten in ihren Gesamtzahlen, während Braze die Möglichkeit bietet, nach Richtung zu filtern.
- **Datumsbereichsausrichtung**: Da das Dashboard das Enddatum nicht berücksichtigt, können Tagesvergleiche genauer sein als Vergleiche über längere Zeiträume. Wenn Sie Daten für einen bestimmten Zeitraum vergleichen möchten, erweitern Sie Ihren Braze-Datumsbereich um einen Tag, um den letzten Tag Ihres Vergleichszeitraums einzubeziehen.