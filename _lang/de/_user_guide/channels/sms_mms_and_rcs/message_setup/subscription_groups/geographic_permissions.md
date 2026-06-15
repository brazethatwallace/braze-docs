---
nav_title: "Geografische Berechtigungen"
article_title: "Geografische Berechtigungen"
description: "Dieser Artikel behandelt die Länder-Allowlist für geografische Berechtigungen, mit der Sie auswählen können, in welche Länder SMS, MMS und RCS zugestellt werden können."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Geografische Berechtigungen {#geographic-permissions}

> Geografische Berechtigungen erhöhen die Sicherheit und schützen vor betrügerischem SMS-, MMS- und RCS-Datenverkehr, indem sie Kontrollen für die Länder durchsetzen, an die Sie Nachrichten senden können. Sie können eine Allowlist von Ländern festlegen, um sicherzustellen, dass SMS-, MMS- und RCS-Nachrichten nur an genehmigte Regionen gesendet werden. Nachrichten werden nur an Telefonnummern mit den Vorwahlen dieser Länder gesendet.<br><br> Nur Admins können Änderungen an der Länder-Allowlist vornehmen. Nutzer:innen ohne Admin-Rechte haben Zugriff auf eine schreibgeschützte Version der Allowlist, die anzeigt, in welche Länder eine Abo-Gruppe senden kann.

Wenn Sie Admin sind, können Sie die Länder konfigurieren, die auf der Allowlist stehen. Die Länder-Allowlist wird auf Ebene der [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) konfiguriert. Sie können darauf zugreifen, indem Sie zu **Audience** > **Subscription Group Management** navigieren und eine SMS-, MMS- oder RCS-Abo-Gruppe auswählen. Die Allowlist befindet sich unter **Geographic Permissions**.

![Der bearbeitbare Abschnitt „Geographic Permissions“ für Admins mit mehreren ausgewählten Ländern in der „Country allowlist“.]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Länder auswählen {#selecting-countries}

Fügen Sie Länder über das Dropdown-Menü zur Allowlist hinzu. Die gängigsten SMS-, MMS- und RCS-Länder werden oben angezeigt, weitere darunter. Sie können auch nach Ländern suchen, indem Sie in das Textfeld tippen.

![Das Dropdown-Menü „Country allowlist“ mit den gängigsten Ländern oben.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Entfernen Sie zuvor ausgewählte Länder, indem Sie die entsprechenden Kontrollkästchen daneben deaktivieren.

### Änderungen speichern {#saving-your-changes}

Änderungen werden nach dem Speichern wirksam. Wenn Sie Länder von Ihrer Allowlist entfernen, werden alle SMS-, MMS- und RCS-Nachrichten an Telefonnummern mit den Vorwahlen dieser Länder nicht mehr gesendet.

![Warnungs-Modal zur Bestätigung der Länder, die von der Allowlist entfernt werden.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Länder mit hohem Betrugsrisiko {#high-fraud-risk-countries}

Bestimmte Länder haben ein höheres Risiko für SMS-, MMS- und RCS-Traffic-Pumping. Diese Länder sind im Länder-Dropdown mit einem **High Fraud Risk**-Tag gekennzeichnet.

![Das Länder-Dropdown mit Aserbaidschan und einem „High Fraud Risk“-Tag.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Wenn Sie den Versand in diese Länder zulassen, müssen Sie zunächst das Risiko bestätigen, bevor das Land zu Ihrer Allowlist hinzugefügt wird.

{% alert note %}
Beschränken Sie die Länder auf Ihrer Allowlist auf diejenigen, die zur Unterstützung Ihrer geschäftlichen Anforderungen erforderlich sind. Dies minimiert Ihr Potenzial für betrügerischen Datenverkehr. Weitere Hinweise zur Vermeidung von SMS-, MMS- und RCS-Traffic-Pumping finden Sie unter [FAQ zu SMS-Traffic-Pumping-Betrug]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Sichtbarkeit von Sendungen außerhalb der Allowlist {#visibility-of-sends-outside-the-allowlist}

Versuchte Sendungen an Länder, die nicht auf Ihrer Länder-Allowlist stehen, werden abgebrochen. Abgebrochene Nachrichten werden im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) und im [SMS-Abbruch-Nachrichten-Engagement-Ereignis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) protokolliert.

Abgebrochene Nachrichten für Empfänger:innen in Ländern, die nicht auf Ihrer Allowlist stehen, werden als **Aborted Message Errors** angezeigt und enthalten die Meldung „The recipient's phone number is in a blocked country“.

![Abbruchprotokoll mit mehreren abgebrochenen SMS-, MMS- und RCS-Sendungen, weil das Land der Telefonnummer nicht auf der Länder-Allowlist steht.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## Wichtiger Hinweis zu Ländern mit hohem Betrugsrisiko und Traffic-Pumping-Betrug {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### Was ist SMS-, MMS- und RCS-Traffic-Pumping? {#what-is-sms-mms-and-rcs-traffic-pumping}

SMS-, MMS- und RCS-Traffic-Pumping (auch bekannt als „Artificially Inflated Traffic“) ist ein eskalierendes Betrugsschema, das zu erheblichen finanziellen Risiken für Kund:innen führen kann. Betrüger:innen können Ihre ungeschützten öffentlich zugänglichen Webformulare, Authentifizierungsabläufe oder API-Endpunkte ausnutzen, um große Mengen an SMS-, MMS- und RCS-Sendungen (wie Opt-in-Bestätigungen, Einmalpasswörter oder Benachrichtigungen) an Telefonnummern auszulösen, die sie kontrollieren oder beeinflussen. Die Angreifer:innen kassieren dann eine Umsatzbeteiligung von beteiligten oder ahnungslosen Mobilfunknetzen für die Erzeugung dieses künstlichen Datenverkehrs. Die nachgelagerten Auswirkungen führen zu erheblichen finanziellen Risiken.

### Was sind Länder mit hohem Betrugsrisiko? {#what-are-high-fraud-risk-countries}

Ein Land oder Gebiet wird als „High Fraud Risk“ eingestuft, wenn es eine ungewöhnlich hohe Dichte an kleinen, Premium-Rate-Roaming-Carriern aufweist oder keine strenge regulatorische Aufsicht hat. Betrüger:innen zielen systematisch auf diese Carrier-Netzwerke mit hohen Tarifen ab, da sie die Umsatzbeteiligung pro generierter Nachricht maximieren.

Darüber hinaus werden Systemrouting-Beschränkungen basierend auf den Ländervorwahlen des Ziels und nicht auf dem tatsächlichen physischen Standort der Empfänger:innen durchgesetzt. Das bedeutet: Wenn Sie Kund:innen haben, die häufig reisen, müssen Sie deren Reisestandorte nicht zu Ihrer Länder-Allowlist hinzufügen, da das Routing auf der ursprünglichen Ländervorwahl des Ziels basiert und nicht auf dem aktuellen physischen Standort. Beispielsweise tragen Gebiete, die sich eine Ländervorwahl mit risikoärmeren Regionen teilen (wie Jersey oder Guernsey, die die Vorwahl +44 mit Großbritannien teilen), dennoch ein hohes Carrier-Tarif-Risiko und werden unter denselben Rahmenbedingungen für hohes Betrugsrisiko verwaltet.

### Verantwortung und finanzielle Haftung der Kund:innen {#customer-responsibility-and-financial-liability}

Die Kund:innen sind verantwortlich für alle mobilen Nachrichten, die über die Dienste in ihrem Namen gesendet werden, und werden dafür in Rechnung gestellt – einschließlich aller Nachrichten, die aus SMS-, MMS- und RCS-Traffic-Pumping resultieren. Plattform-Schutzmaßnahmen wie die Länder-Allowlist unterstützen Sie dabei, die Zustellung auf vertrauenswürdige Regionen zu beschränken. Letztendlich liegt die Absicherung Ihrer externen Endpunkte und die Vermeidung schwerwiegender finanzieller Schäden jedoch in der alleinigen Verantwortung der Kund:innen.

### So verhindern Sie Traffic-Pumping {#how-to-prevent-traffic-pumping}

Wenn Sie Ihre Nachrichtenverteilung nicht strikt auf die geografischen Regionen beschränken, in denen sich Ihre tatsächlichen Kund:innen befinden, entsteht eine unmittelbare Anfälligkeit für Betrug und schwere finanzielle Schäden. Um Ihr Unternehmen zu schützen, müssen Sie Ihre Zustellregionen proaktiv mithilfe der Länder-Allowlist einschränken. Darüber hinaus – und das ist am wichtigsten – sollten Sie jedes Online-Formular zur Telefonnummernanfrage oder jeden API-Endpunkt, der SMS-, MMS- und RCS-Sendungen auslöst, gemäß den Best Practices der Branche absichern, wie in [SMS-, MMS- und RCS-Traffic-Pumping-Betrug verstehen und verhindern]({{site.baseurl}}/sms_traffic_pumping_fraud/) beschrieben.