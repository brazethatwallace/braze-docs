---
page_order: 22
nav_title: Best Practices
article_title: Push-Best-Practices
description: "Diese Seite enthält Best Practices und Anwendungsfälle für Push-Benachrichtigungen, damit Ihre Push-Nachrichten Engagement statt Ärger erzeugen."
channel: push
---

# Push-Best-Practices {#push-best-practices}

> Diese Seite enthält Best Practices und Anwendungsfälle für Push-Benachrichtigungen, damit Ihre Push-Nachrichten Engagement statt Ärger erzeugen.

Push-Benachrichtigungen sind leistungsstarke Werkzeuge, um mit den Nutzer:innen Ihrer App zu interagieren, sollten aber mit Bedacht eingesetzt werden, um zeitnahe und relevante Nachrichten zu übermitteln. Bevor Sie Ihre Push-Nachricht senden, beachten Sie die folgenden Best Practices für Dinge, die Sie wissen und überprüfen sollten.

{% alert important %}
Ihre Push-Nachrichten müssen den Richtlinien des Apple App Store und den Google Play Store-Richtlinien entsprechen, insbesondere in Bezug auf die Verwendung von Push-Nachrichten als Werbung, Spam, Aktionen und mehr. Auf dieser Seite finden Sie [Vorschriften für Push-Nachrichten](#push-message-regulations).
{% endalert %}

## Push-Nachricht verfassen {#compose-your-push-message}

Als Best Practice empfiehlt Braze, jede Textzeile sowohl für den optionalen Titel als auch für den Nachrichtentext in einer mobilen Push-Benachrichtigung auf etwa 30–40 Zeichen zu beschränken. Beachten Sie, dass der Zeichenzähler im Composer keine Liquid-Zeichen berücksichtigt. Das bedeutet, dass die endgültige Zeichenanzahl einer Nachricht davon abhängt, wie Liquid für die einzelnen Nutzer:innen gerendert wird. Im Zweifelsfall halten Sie es kurz und prägnant.

## Push-Benachrichtigungs-Nutzlastgröße reduzieren {#reduce-push-notification-payload-size}

Die maximale Nutzlastgröße hängt von der Plattform ab.

| Plattform | Maximale Nutzlastgröße |
| --- | --- |
| Web | 3.807 Bytes |
| Android | 3.930 Bytes |
| iOS | 3.960 Bytes |
| Kindle | 5.985 Bytes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Benachrichtigungs-Nutzlastgröße reduzieren" }

Wenn Ihre Push-Benachrichtigung die maximale Nutzlastgröße überschreitet, wird die Nachricht möglicherweise nicht gesendet. Als Best Practice sollten Sie Ihre Nutzlast auf wenige Hundert Bytes begrenzen.

### Was ist eine Push-Nutzlast? {#what-is-a-push-payload}

Push-Dienstanbieter prüfen, ob Ihre Push-Benachrichtigung einem/einer Nutzer:in angezeigt werden kann, indem sie die Bytegröße der gesamten Push-Nutzlast betrachten. Die Nutzlast ist bei den meisten Push-Diensten auf **4 KB (4.096 Bytes)** begrenzt, darunter:

- Apple Push Notification service (APNs)
- Androids Firebase Cloud Messaging (FCM)
- Web-Push
- Huawei-Push

Diese Push-Dienste lehnen jede Benachrichtigung ab, die dieses Limit überschreitet.

Braze reserviert einen Teil der Push-Nutzlast für Integrations- und Analysezwecke. Daher beträgt unsere maximale Nutzlastgröße **3.807 Bytes**. Wenn Ihre Push-Benachrichtigung diese Größe überschreitet, wird die Nachricht möglicherweise nicht gesendet. Als Best Practice sollten Sie Ihre Nutzlast auf wenige Hundert Bytes begrenzen.

Die folgenden Elemente in Ihrer Push-Benachrichtigung machen Ihre Push-Nutzlast aus:

- Text, wie Titel und Nachrichtentext
- Finale Darstellung jeder Liquid-Personalisierung
- URLs für Bilder (aber nicht die Größe des Bildes selbst)
- URLs für Klickziele
- Button-Namen
- Schlüssel-Wert-Paare

### Tipps zur Reduzierung der Nutzlastgröße {#tips-to-reduce-payload-size}

So reduzieren Sie die Nutzlastgröße:

- Halten Sie Ihre Nachricht kurz. Eine gute allgemeine Richtlinie ist, sie in weniger als 40 Zeichen umsetzbar und nützlich zu gestalten.
- Verzichten Sie auf Leerzeichen und Zeilenumbrüche in Ihrem Text.
- Berücksichtigen Sie, wie Liquid beim Senden gerendert wird. Da die finale Darstellung jeder Liquid-Personalisierung von Nutzer:in zu Nutzer:in variiert, kann Braze nicht bestimmen, ob eine Push-Nutzlast das Größenlimit überschreitet, wenn Liquid enthalten ist. Wenn Ihr Liquid eine kürzere Nachricht rendert, könnte es passen. Wenn Ihr Liquid jedoch eine längere Nachricht erzeugt, könnte Ihre Push-Benachrichtigung das Nutzlastgrößenlimit überschreiten. Testen Sie Ihre Push-Nachricht immer auf einem echten Gerät, bevor Sie sie an Nutzer:innen senden.
- Erwägen Sie, URLs mithilfe eines URL-Shorteners zu verkürzen.

## Targeting optimieren {#optimize-targeting}

### Relevante Nutzerdaten erfassen {#collect-relevant-user-data}

Push-Benachrichtigungen sollten mit Bedacht eingesetzt werden, um Nutzer:innen mit zeitnahen und relevanten Benachrichtigungen anzusprechen. Braze erfasst nützliche Geräte- und Nutzungsinformationen, die zum Targeting relevanter Segmente verwendet werden können. Diese Informationen sollten durch angepasste Events und Attribute ergänzt werden, die spezifisch für Ihre App sind. Mithilfe dieser Daten können Sie Nachrichten gezielt ausrichten, um Öffnungsraten zu erhöhen und die Anzahl der Nutzer:innen zu verringern, die Push-Benachrichtigungen deaktivieren.

### Eine Seite für Benachrichtigungseinstellungen erstellen {#create-a-notification-settings-page}

Sie können in Ihrer App eine Einstellungsseite erstellen, auf der Nutzer:innen angeben können, welche Benachrichtigungen sie erhalten möchten. Ein gängiger Ansatz ist die Erstellung eines booleschen angepassten Attributs in Braze, das dem Status der App-Einstellung entspricht. Beispielsweise könnte eine Nachrichten-App Abo-Einstellungen für Eilmeldungen, Sportnachrichten oder Politik anbieten.

Wenn die Nachrichten-App eine Campaign erstellen möchte, die nur Nutzer:innen anspricht, die sich für Politik interessieren, fügt sie den Attributfilter `Subscribes to Politics` zum Segment hinzu. Wenn dieser auf „true“ gesetzt ist, erhalten nur Nutzer:innen Benachrichtigungen, die diese auch abonniert haben.

Weitere Informationen zum Festlegen angepasster Attribute finden Sie in den folgenden Artikeln für [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android) oder [REST API]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Opt-ins steigern und Relevanz erhöhen {#increase-opt-ins-and-relevance}

### Nutzer:innen-Erlaubnis einholen {#obtain-user-permission}

Die allgemeinen Statistiken für Push-Aktivierung beziehen sich darauf, ob Nutzer:innen Benachrichtigungen über ihr Betriebssystem genehmigt haben. Wenn Nutzer:innen Benachrichtigungen auf iOS deaktivieren, werden sie automatisch aus unserem System entfernt, da Apple das Senden des Push-Tokens nicht zulässt.

Ab Android 13 muss eine Erlaubnis eingeholt werden, bevor Push-Benachrichtigungen angezeigt werden können. Ältere Android-Versionen abonnieren Nutzer:innen standardmäßig für Benachrichtigungen.

### Nutzer:innen auf Push vorbereiten {#prime-users-for-push}

Sie haben nur eine Chance, Nutzer:innen um die Push-Erlaubnis zu bitten, und nachdem sie abgelehnt haben, ist es sehr schwierig, sie davon zu überzeugen, Push in ihren Geräteeinstellungen wieder zu aktivieren. Aus diesem Grund sollten Sie Nutzer:innen mithilfe einer In-App-Nachricht auf Push vorbereiten, bevor Sie die Systemaufforderung anzeigen. Weitere Informationen zur Steigerung von Opt-ins finden Sie unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

### Push-Abo-Steuerung hinzufügen {#add-push-subscription-controls}

Um zu vermeiden, dass Nutzer:innen Benachrichtigungen auf Geräteebene deaktivieren – was ihr Vordergrund-Push-Token / Textbaustein vollständig entfernt –, lassen Sie Nutzer:innen ihr Push-Abo direkt in Ihrer App steuern. Weitere Details finden Sie unter [Push-Abo-Status aktualisieren]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

### Erweiterte Zeitplanung verwenden oder Verzögerungen hinzufügen {#use-advanced-scheduling-or-add-delays}

Je nach Größe Ihrer Zielgruppe und wie weit im Voraus Ihre Push-Nachricht geplant ist, kann es bei der Push-Zustellung zu Verzögerungen kommen. Wie lange der Versand von Push-Benachrichtigungen dauert, hängt von der zugewiesenen Verarbeitungsleistung ab. Wenn Ihre Push-Nachricht beispielsweise mehrere Connected-Content-Aufrufe verwendet, kann dies die Komplexität des Templating der Push-Nachricht erhöhen und zu Geschwindigkeitseinschränkungen führen, die davon abhängen, wie schnell Ihre Drittanbieter-APIs Daten zurückgeben.

Ein kleinerer Push-Payload und eine höhere Benachrichtigungspriorität können dazu beitragen, Verzögerungen zu reduzieren und Ihre Nachrichten zu skalieren. Sie können `Push Enabled = true` in Ihrem Zielgruppenfilter hinzufügen, um die Zielgruppengröße zu reduzieren, sodass nur Push-aktivierte Nutzer:innen für den Campaign-Versand verarbeitet werden.

Wir empfehlen außerdem, die Anzahl der API-Aufrufe durch Optimierung der benötigten Daten zu minimieren. Wenn möglich, versuchen Sie, alle benötigten Daten in einem einzigen API-Aufruf abzurufen, anstatt mehrere Aufrufe durchzuführen.

### Push-Abo-Status verstehen {#understand-push-subscription-states}

Der Push-Abo-Status garantiert nicht, dass eine Push-Benachrichtigung zugestellt wird – Nutzer:innen müssen außerdem Push-aktiviert sein, um Benachrichtigungen zu empfangen. Dies liegt daran, dass ein Kundenprofil mehrere Geräte mit unterschiedlichen Vordergrund-Push-Berechtigungen haben kann, aber nur einen einzigen Push-Abo-Status besitzt.

Wenn Nutzer:innen kein gültiges Vordergrund-Push-Token / Textbaustein für eine App haben (d. h. sie Push-Tokens auf Geräteebene über die Einstellungen deaktivieren und sich entscheiden, keine Benachrichtigungen zu empfangen), kann ihr Abo-Status dennoch als `subscribed` für Push gelten. Diese Nutzer:innen wären jedoch in Braze nicht als `Foreground Push Enabled for App` eingestuft, da das Vordergrund-Push-Token / Textbaustein ungültig ist.

Darüber hinaus ist der Filter `Foreground Push Enabled` in der Segmentierung auch auf „false“ gesetzt, wenn ein Kundenprofil kein gültiges oder registriertes Push-Token / Textbaustein für andere Apps besitzt.

## Eine Sunset-Richtlinie für nicht reagierende Nutzer:innen umsetzen {#implement-a-sunset-policy-for-unresponsive-users}

Auch wenn Sie nur relevante, zeitnahe Push-Benachrichtigungen versenden, reagieren einige Nutzer:innen möglicherweise trotzdem nicht darauf und empfinden sie als Spam. Angenommen, Nutzer:innen zeigen ein Muster, bei dem sie Ihre Push-Benachrichtigungen wiederholt ignorieren. In diesem Fall ist es ratsam, ihnen keine Push-Benachrichtigungen mehr zu senden, bevor sie sich von der Kommunikation Ihrer App genervt fühlen oder sie sogar deinstallieren.

Erstellen Sie dazu eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies), die nach und nach das Senden von Push-Benachrichtigungen an Nutzer:innen einstellt, die seit langer Zeit keinen direkten oder beeinflussten Open hatten.

1. Identifizieren Sie nicht reagierende Nutzer:innen anhand von direkten oder beeinflussten Opens.
2. Reduzieren Sie schrittweise das Senden von Push-Benachrichtigungen an diese Nutzer:innen.
3. Bevor Sie die Push-Benachrichtigungen vollständig entfernen, senden Sie eine letzte Benachrichtigung, die erklärt, warum sie keine weiteren erhalten werden. So haben Nutzer:innen die Möglichkeit, ihr Interesse an weiteren Push-Benachrichtigungen zu zeigen, indem sie diese Benachrichtigung öffnen.
4. Nachdem die Sunset-Richtlinie in Kraft getreten ist, verwenden Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages), um diese Nutzer:innen daran zu erinnern, dass sie zwar keine Push-Benachrichtigungen mehr erhalten, In-App-Messaging-Kanäle aber weiterhin interessante, hilfreiche Informationen liefern.

Auch wenn Sie möglicherweise zögern, Nutzer:innen keine Push-Benachrichtigungen mehr zu senden, die ursprünglich zugestimmt haben, denken Sie daran, dass andere Messaging-Kanäle diese Nutzer:innen effektiver erreichen können — insbesondere wenn sie Ihre Push-Benachrichtigungen zuvor ignoriert haben. Wenn Nutzer:innen Ihre E-Mails öffnen, sind E-Mail-Campaigns eine gute Möglichkeit, sie außerhalb Ihrer App zu erreichen. Falls nicht, sind In-App-Nachrichten der beste Weg, Inhalte zu übermitteln, ohne zu riskieren, dass Nutzer:innen Ihre App deinstallieren.

## Konversions-Events für App-Öffnungen festlegen {#set-conversion-events-for-app-opens}

Wenn Sie einer Push-Campaign [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) zuweisen, können Sie App-Öffnungen für einen bestimmten Zeitraum nach Empfang der Campaign verfolgen. Das Festlegen eines Konversions-Events für App-Öffnungen bietet andere Insights als die Ergebnisstatistiken, die Sie normalerweise nach einer Push-Campaign erhalten.

Während alle Push-Campaign-Ergebnisse die direkten Öffnungen und Öffnungen einer Nachricht aufschlüsseln (was sowohl direkte als auch [beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens) umfasst), verfolgt das Konversions-Tracking jede Art von Öffnung, ob direkt oder beeinflusst.

Darüber hinaus verfolgen Sie mit dem Konversions-Event „öffnet App“ App-Öffnungen, die vor Ablauf der Konversionsfrist auftreten (zum Beispiel drei Tage). Dies unterscheidet sich von einer beeinflussten Öffnung, da die Zeit, die Nutzer:innen haben, um eine beeinflusste Öffnung zu Registrierung, von Person zu Person variieren kann und vom bisherigen Engagement-Verhalten der jeweiligen Nutzer:innen abhängt.

## Vorschriften für Push-Nachrichten {#push-message-regulations}

Da Push-Nachrichten eine aufdringliche Art von Messaging darstellen, die direkt an das Telefon oder den Browser Ihrer Kund:innen gesendet werden, gibt es Richtlinien für den Versand von Push-Nachrichten über Apps und Websites.

### Mobile Push-Vorschriften für Apps {#mobile-push-regulations-for-apps}

| Richtlinien des Apple App Store |
| --- |
| [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Unzulässig: (i) Erstellen einer Schnittstelle zur Anzeige von Drittanbieter-Apps, Erweiterungen oder Plug-ins, die dem App Store ähneln oder als allgemeine Sammlung dienen. |
| [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Push-Benachrichtigungen dürfen nicht für die Funktion der App erforderlich sein und sollten nicht zum Senden sensibler persönlicher oder vertraulicher Informationen verwendet werden. Push-Benachrichtigungen sollten nicht für Werbeaktionen oder Direktmarketing-Zwecke verwendet werden, es sei denn, Kund:innen haben sich ausdrücklich für den Empfang entschieden, indem eine Einwilligungserklärung in der UI Ihrer App angezeigt wird, und Sie stellen in Ihrer App eine Methode bereit, mit der Nutzer:innen den Empfang solcher Nachrichten abbestellen können. |
| [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) Sie dürfen integrierte Funktionen, die von der Hardware oder dem Betriebssystem bereitgestellt werden, wie Push-Benachrichtigungen, die Kamera oder das Gyroskop, nicht monetarisieren; ebenso wenig Apple-Dienste und -Technologien wie Apple Music-Zugang, iCloud-Speicher oder Screen Time APIs. |
{: .reset-td-br-1 aria-label="Mobile Push-Vorschriften für Apps" }

| Richtlinien des Google Play Store |
| --- |
| [Unbefugte Nutzung oder Nachahmung von Systemfunktionen](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) Wir erlauben keine Apps oder Anzeigen, die Systemfunktionen wie Benachrichtigungen oder Warnungen nachahmen oder beeinträchtigen. Benachrichtigungen auf Systemebene dürfen nur für wesentliche Features einer App verwendet werden, z. B. eine Fluggesellschafts-App, die Nutzer:innen über Sonderangebote informiert, oder ein Spiel, das Nutzer:innen über In-Game-Aktionen benachrichtigt. |
{: .reset-td-br-1 aria-label="Mobile Push-Vorschriften für Apps" }

## Verwandte Artikel {#related-articles}

Sie haben nicht gefunden, wonach Sie gesucht haben? Sehen Sie sich diese zusätzlichen Best-Practices-Artikel an:

- [Formate für Push-Nachrichten und Bilder]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)
- [Zustellbarkeit für chinesische Android-Geräte]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)
- [Vor dem Versand beachten: Kanäle]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)