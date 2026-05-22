---
nav_title: "Geografische Berechtigungen"
article_title: "Geografische Berechtigungen"
description: "Dieser Artikel behandelt die Länder-Allowlist für geografische Berechtigungen, mit der Sie auswählen können, in welche Länder SMS, MMS und RCS zugestellt werden können."
page_order: 4
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Geografische Berechtigungen {#geographic-permissions}

> Geografische Berechtigungen erhöhen die Sicherheit und schützen vor betrügerischem SMS-, MMS- und RCS-Datenverkehr, indem sie Kontrollen für die Länder durchsetzen, an die Sie Nachrichten senden können. Sie können eine Allowlist von Ländern festlegen, um sicherzustellen, dass SMS-, MMS- und RCS-Nachrichten nur an genehmigte Regionen gesendet werden. Nur Admins können Änderungen an der Länder-Allowlist vornehmen. Nutzer:innen ohne Admin-Rechte haben Zugriff auf eine schreibgeschützte Version der Allowlist, die anzeigt, in welche Länder eine Abo-Gruppe senden kann.

Wenn Sie Admin sind, können Sie die Länder konfigurieren, die auf der Allowlist stehen. Die Länder-Allowlist wird auf Ebene der [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) konfiguriert. Sie können darauf zugreifen, indem Sie zu **Audience** > **Subscriptions** navigieren und eine SMS-, MMS- oder RCS-Abo-Gruppe auswählen. Die Allowlist befindet sich unter **Geographic Permissions**.

![Der bearbeitbare Abschnitt „SMS Geographic Permissions“ für Admins mit mehreren ausgewählten Ländern in der „Country allowlist“.]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Länder auswählen {#selecting-countries}

Fügen Sie Länder über das Dropdown-Menü zur Allowlist hinzu. Die gängigsten SMS- und RCS-Länder werden oben angezeigt, weitere darunter. Sie können auch nach Ländern suchen, indem Sie in das Textfeld tippen.

![Das Dropdown-Menü „Country allowlist“ mit den gängigsten Ländern oben.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Entfernen Sie zuvor ausgewählte Länder, indem Sie die entsprechenden Kontrollkästchen daneben deaktivieren.

### Änderungen speichern {#saving-your-changes}

Änderungen werden wirksam, nachdem Sie **Save** ausgewählt haben. Das Entfernen von Ländern aus Ihrer Allowlist verhindert, dass alle SMS-, MMS- und RCS-Nachrichten an Nummern in diesen Ländern gesendet werden.

![Warnungs-Modal zur Bestätigung der Länder, die aus der Allowlist gelöscht werden.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Hochrisikoländer {#high-risk-countries}

Bestimmte Länder haben ein höheres Risiko für SMS- und RCS-Traffic-Pumping. Diese Länder sind im Länder-Dropdown mit einem **High Risk**-Tag gekennzeichnet.

![Das Länder-Dropdown mit Aserbaidschan, das ein „High Risk“-Tag hat.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Wenn Sie den Versand in diese Länder zulassen, müssen Sie zunächst das Risiko bestätigen, bevor das Land zu Ihrer Allowlist hinzugefügt wird.

{% alert note %}
Beschränken Sie die Länder auf Ihrer Allowlist auf diejenigen, die zur Unterstützung Ihrer Geschäftsanforderungen erforderlich sind. Dies minimiert Ihr Potenzial für betrügerischen Datenverkehr. Weitere Hinweise zur Vermeidung von SMS-Traffic-Pumping finden Sie unter [FAQ zu SMS-Traffic-Pumping-Betrug]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Sichtbarkeit blockierter Sendungen {#visibility-of-blocked-sends}

Versuchte Sendungen an Länder, die nicht auf Ihrer Allowlist stehen, werden abgebrochen. Abgebrochene Nachrichten werden im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) und im [SMS-Abbruch-Nachrichten-Engagement-Ereignis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) protokolliert.

Abgebrochene Nachrichten aufgrund blockierter Sendungen werden als **Aborted Message Errors** angezeigt und enthalten die Meldung „The recipient's phone number is in a blocked country“.

![Abbruchprotokoll mit mehreren SMS-Sendungen, die blockiert wurden, weil sich die Telefonnummer in einem blockierten Land befindet.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}