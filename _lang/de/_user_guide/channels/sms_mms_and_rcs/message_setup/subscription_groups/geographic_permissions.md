---
nav_title: "Geografische Berechtigungen"
article_title: "Geografische Berechtigungen"
description: "Dieser Artikel behandelt die Länder-Allowlist für geografische Berechtigungen, mit der Sie auswählen können, in welche Länder Kurzmitteilungsdienst or SMS, MMS und RCS zugestellt werden können."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Geografische Berechtigungen {#geographic-permissions}

> Geografische Berechtigungen erhöhen die Sicherheit und schützen vor betrügerischem Kurzmitteilungsdienst or SMS-, MMS- und RCS-Datenverkehr, indem sie Kontrollen für die Länder durchsetzen, an die Sie Nachrichten senden können. Sie können eine Allowlist von Ländern festlegen, um Kurzmitteilungsdienst or SMS-, MMS- und RCS-Nachrichten nur an genehmigte Regionen zu senden. Nachrichten werden nur an Telefonnummern mit den Vorwahlen dieser Länder gesendet.<br><br> Nur Admins können Änderungen an der Länder-Allowlist vornehmen. Nutzer:innen ohne Admin-Rechte haben Zugriff auf eine schreibgeschützte Version der Allowlist, die anzeigt, in welche Länder eine Abo-Gruppe senden kann.

Wenn Sie Admin sind, können Sie die Länder konfigurieren, die auf der Allowlist stehen. Die Länder-Allowlist wird auf Ebene der [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups) konfiguriert. Sie können darauf zugreifen, indem Sie zu **Zielgruppe** > **Abo-Gruppen-Verwaltung** navigieren und eine Kurzmitteilungsdienst or SMS-, MMS- oder RCS-Abo-Gruppe auswählen. Die Allowlist befindet sich unter **Geographic Permissions**.

![Der bearbeitbare Abschnitt „Geographic Permissions“ für Admins mit mehreren ausgewählten Ländern in der „Country allowlist“.]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## Länder auswählen {#selecting-countries}

Fügen Sie der Positivliste über das Dropdown-Menü Länder hinzu. Die gängigsten Kurzmitteilungsdienst or SMS-, MMS- und RCS-Länder werden oben angezeigt, weitere Länder folgen im nächsten Abschnitt. Sie können auch nach Ländern suchen, indem Sie den Namen in das Textfeld eingeben.

![Das Dropdown-Menü „Länder-Positivliste“ mit den gängigsten Ländern oben.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Entfernen Sie zuvor ausgewählte Länder, indem Sie die jeweiligen Kontrollkästchen daneben deaktivieren.

### Änderungen speichern {#saving-your-changes}

Änderungen werden wirksam, nachdem Sie sie gespeichert haben. Wenn Sie Länder aus Ihrer Positivliste entfernen, wird verhindert, dass Kurzmitteilungsdienst or SMS-, MMS- und RCS-Nachrichten an Telefonnummern mit den Vorwahlen dieser Länder gesendet werden.

![Warnungs-Modal zur Bestätigung der Länder, die aus der Positivliste entfernt werden.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Länder mit hohem Betrugsrisiko {#high-fraud-risk-countries}

Bestimmte Länder haben ein höheres Risiko für Kurzmitteilungsdienst or SMS-, MMS- und RCS-Traffic-Pumping. Diese Länder sind im Länder-Dropdown durch ein **High Fraud Risk**-Tag gekennzeichnet.

![Das Länder-Dropdown, in dem Aserbaidschan ein „High Fraud Risk“-Tag aufweist.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Wenn Sie den Versand in diese Länder zulassen möchten, müssen Sie zunächst das damit verbundene Risiko bestätigen, bevor das Land zu Ihrer Zulassungsliste hinzugefügt wird.

{% alert note %}
Beschränken Sie die Länder auf Ihrer Zulassungsliste auf diejenigen, die für Ihre geschäftlichen Anforderungen erforderlich sind. Dies minimiert Ihr Risiko für betrügerischen Datenverkehr. Weitere Informationen zur Vermeidung von Kurzmitteilungsdienst or SMS-, MMS- und RCS-Traffic-Pumping finden Sie unter [Häufig gestellte Fragen zu Kurzmitteilungsdienst or SMS-Traffic-Pumping-Betrug]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud).
{% endalert %}

## Sichtbarkeit von Sendungen außerhalb der Länderliste {#visibility-of-sends-outside-the-allowlist}

Versuchte Sendungen an Länder, die nicht auf Ihrer Länderliste stehen, werden abgebrochen. Abgebrochene Nachrichten werden im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) und im [Kurzmitteilungsdienst or SMS-Abbruch-Nachrichtenengagement-Ereignis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) protokolliert.

Abgebrochene Nachrichten für Empfänger:innen in Ländern, die nicht auf Ihrer Länderliste stehen, werden als **Aborted Message Errors** angezeigt und enthalten die Meldung „The recipient's phone number is in a blocked country“.

![Abbruchprotokoll mit mehreren abgebrochenen SMS-, MMS- und RCS-Sendungen, da das Land der Telefonnummer nicht auf der Länderliste steht.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## Wichtiger Hinweis für Länder mit hohem Betrugsrisiko und Traffic-Pumping-Betrug {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### Was ist Kurzmitteilungsdienst or SMS-, MMS- und RCS-Traffic-Pumping? {#what-is-sms-mms-and-rcs-traffic-pumping}

Kurzmitteilungsdienst or SMS-, MMS- und RCS-Traffic-Pumping (auch bekannt als künstlich aufgeblähter Datenverkehr) ist ein eskalierendes Betrugsschema, das zu erheblichen finanziellen Risiken für Kund:innen führen kann. Betrüger:innen können Ihre ungeschützten, öffentlich zugänglichen Webformulare, Authentifizierungsabläufe oder API-Endpunkte ausnutzen, um große Mengen an Kurzmitteilungsdienst or SMS-, MMS- und RCS-Nachrichten (wie Opt-in-Bestätigungen, Einmalpasswörter oder Benachrichtigungen) an Telefonnummern auszulösen, die sie kontrollieren oder beeinflussen. Die Angreifer:innen kassieren dann eine Umsatzbeteiligung von mitwirkenden oder ahnungslosen Mobilfunknetzen für die Erzeugung dieses künstlichen Datenverkehrs. Die nachgelagerten Auswirkungen verursachen erhebliche finanzielle Risiken.

### Was sind Länder mit hohem Betrugsrisiko? {#what-are-high-fraud-risk-countries}

Ein Land oder Gebiet wird als Land mit hohem Betrugsrisiko eingestuft, wenn es eine ungewöhnlich hohe Dichte an kleinen, Premium-Rate-Roaming-Netzbetreibern aufweist oder keine strenge regulatorische Aufsicht hat. Betrüger:innen zielen systematisch auf diese hochpreisigen Netzbetreiber ab, da sie die Umsatzbeteiligung pro generierter Nachricht maximieren.

Darüber hinaus werden Systemrouting-Einschränkungen auf Basis der Ländervorwahl des Ziels und nicht auf Basis des tatsächlichen physischen Standorts der Empfänger:innen durchgesetzt. Das bedeutet: Wenn Sie Kund:innen haben, die häufig reisen, müssen Sie deren Reisestandorte nicht zu Ihrer Länder-Zulassungsliste hinzufügen, da Nachrichten auf Basis der ursprünglichen Ländervorwahl des Ziels geroutet werden und nicht auf Basis des aktuellen physischen Standorts. So tragen beispielsweise Gebiete, die sich eine Ländervorwahl mit Regionen mit geringerem Risiko teilen (wie Jersey oder Guernsey, die die Ländervorwahl +44 mit Großbritannien teilen), dennoch ein hohes Risiko durch hohe Netzbetreibergebühren und werden unter denselben Rahmenbedingungen für hohes Betrugsrisiko verwaltet.

### Kundenverantwortung und finanzielle Haftung {#customer-responsibility-and-financial-liability}

Die Kund:innen sind verantwortlich für alle mobilen Nachrichten, die über die Dienste in ihrem Namen gesendet werden, und diese werden ihnen in Rechnung gestellt – einschließlich aller Nachrichten, die aus Kurzmitteilungsdienst or SMS-, MMS- und RCS-Traffic-Pumping resultieren. Plattform-Schutzmaßnahmen wie die Länder-Zulassungsliste unterstützen Sie dabei, die Zustellung auf vertrauenswürdige Regionen zu beschränken. Letztendlich liegt es jedoch in der alleinigen Verantwortung der Kund:innen, ihre nach außen gerichteten Endpunkte abzusichern und verheerenden finanziellen Schaden zu verhindern.

### So verhindern Sie Traffic-Pumping {#how-to-prevent-traffic-pumping}

Wenn Sie Ihre Nachrichtenverteilung nicht strikt auf die geografischen Regionen beschränken, in denen Ihre tatsächlichen Kund:innen ansässig sind, entsteht eine unmittelbare Anfälligkeit für Betrug und schwere finanzielle Schäden. Um Ihr Unternehmen zu schützen, müssen Sie Ihre Zustellungsregionen proaktiv mithilfe der Länder-Zulassungsliste einschränken. Darüber hinaus – und das ist am wichtigsten – sollten Sie jedes Online-Formular zur Telefonnummernanfrage oder jeden API-Endpunkt, der Kurzmitteilungsdienst or SMS-, MMS- und RCS-Nachrichten auslöst, gemäß den Best Practices der Branche absichern, wie in [Kurzmitteilungsdienst or SMS-, MMS- und RCS-Traffic-Pumping-Betrug verstehen und verhindern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud) beschrieben.