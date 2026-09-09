---
nav_title: "Best Practices"
article_title: Best Practices für SMS, MMS und RCS
page_order: 2
description: "Dieser Referenzartikel behandelt Best Practices für SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS



---

# Best Practices für SMS, MMS und RCS {#best-practices-for-sms-mms-and-rcs}

> Erfahren Sie mehr über Best Practices für SMS, MMS und RCS mit Braze, einschließlich unserer Empfehlungen zur Opt-out-Überwachung und zum Traffic-Pumping.

## Empfehlungen zur Überwachung von Opt-outs {#opt-out-monitoring-recommendations}

Die Einhaltung von Empfängeranfragen zum Opt-out aus der Kommunikation ist gesetzlich vorgeschrieben. Die Nichtbeachtung von Opt-out-Anfragen von SMS-Empfänger:innen kann Strafen nach sich ziehen, einschließlich Bußgeldern, und zu Klagen führen. Braze bietet Features für ein robustes SMS- und MMS-Opt-in- und Opt-out-Management sowie Mechanismen, die sicherstellen, dass Anfragen korrekt verarbeitet werden.

Gemäß ihren Abonnementvereinbarungen mit uns sind unsere Kund:innen allein für die Einhaltung der geltenden Gesetze bei der Nutzung unserer Dienste verantwortlich. Daher empfehlen wir dringend, dass Kund:innen besonders auf die korrekte Konfiguration ihres SMS-Setups achten, diese Konfigurationen gründlich testen, Maßnahmen zur Überwachung der Opt-out-Compliance ergreifen und umgehend handeln, wenn sie Fälle der Nichteinhaltung von Opt-out-Anfragen feststellen.

Wenn Sie SMS und MMS in Braze einrichten, um Opt-ins und Opt-outs zu verwalten, beachten Sie die folgende Liste von Ressourcen:
* [SMS-Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups): Abo-Gruppen und Opt-in-/Opt-out-Methoden und -Status.
* [REST APIs für Abo-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups): Wie Opt-ins und Opt-outs verarbeitet werden, die aus einer anderen Quelle als einer direkten Antwort auf eine Nachricht stammen.
* [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Erklärungen dazu, wie Braze die Schlüsselwortverarbeitung und -verwaltung handhabt.
* [SMS-Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): Erfordert, dass Nutzer:innen ihre Opt-in-Absicht explizit bestätigen, bevor sie SMS-Nachrichten erhalten können. SMS-Double-Opt-in ist in einigen Ländern vorgeschrieben, daher empfiehlt Braze, dies zu konfigurieren.
* [SMS-Nachrichtenversand]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): Grundlagen des SMS-Versands bei Braze, einschließlich der Bedeutung von Abo-Gruppen, Anforderungen an SMS-Segmente und Nachrichtentexte und mehr.

### Hinweise {#considerations}

Wenn SMS und MMS über mehrere Instanzen hinweg eingerichtet werden, kann eine Fehlkonfiguration dazu führen, dass Campaign- oder Canvas-Opt-outs an den falschen Workspace gesendet werden.

* Braze verfügt über Überwachungsmechanismen, um solche Fälle zu erkennen. Wenn dieses Verhalten festgestellt wird, leitet Braze Opt-outs an die richtige Instanz weiter und gleicht alle Opt-outs nach, die während des Zeitraums aufgetreten sind.
* Wir empfehlen dringend, dass Kund:innen Opt-outs für jede Abo-Gruppe testen, die sie in Braze haben. Es ist besser, dieses Problem vor dem Versand einer Nachricht zu identifizieren, als es nachträglich zu beheben.

Braze verwaltet SMS-/MMS-Abos sowohl auf der Ebene des Nutzerprofils (`user_id`) als auch auf der Ebene der Telefonnummer (`channel_id`). Wenn für eine Telefonnummer ein Opt-in oder Opt-out durchgeführt wird, gilt die Aktualisierung für alle Profile, die diese Nummer teilen. Falls Endnutzer:innen sich mit einer bestimmten Telefonnummer angemeldet haben und dann die Telefonnummer wechseln, übernimmt die neue Telefonnummer den Abo-Gruppenstatus der Nutzer:innen. Wenn sich Endnutzer:innen also abgemeldet haben, aber dann mit einer neuen Telefonnummer die App oder Website erneut aufrufen, erhalten sie keine unerwünschten Nachrichten.

## Empfehlungen zur Pflege von Telefonnummernlisten {#phone-number-list-hygiene-recommendations}

Die Pflege Ihrer Telefonnummernlisten hilft Ihnen, gültige Einwilligungs- und Erreichbarkeitsdaten langfristig aufrechtzuerhalten. Braze markiert einige Telefonnummern als ungültig, um Compliance-Risiken zu reduzieren, einwilligungsbasierte Messaging-Praktiken zu unterstützen und den Versand an Nummern zu vermeiden, die möglicherweise nicht mehr dem/der ursprünglichen Nutzer:in gehören.

Informationen zu den Gründen, warum Telefonnummern typischerweise als ungültig markiert werden, finden Sie unter [Umgang mit ungültigen Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Wir empfehlen den folgenden Workflow zum Entfernen ungültiger Telefonnummern:

1. Identifizieren Sie betroffene Telefonnummern über den [`/sms/invalid_phone_numbers`-Endpunkt]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Unterscheiden Sie zwischen Telefonnummern, die deaktiviert wurden, die aufgrund von Anbieterfehlern als ungültig markiert wurden und die aufgrund von Formatierungsproblemen als ungültig markiert wurden (`invalid_format`, z. B. Nummern, die nicht dem E.164-Format entsprechen). Verwenden Sie den `reason`-Filter in der API für ungültige Telefonnummern, um nach Kategorie abzufragen. Weitere Informationen finden Sie unter [Umgang mit ungültigen Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).
3. Verifizieren Sie deaktivierte Telefonnummern erneut mit dem/der Nutzer:in. Nachdem der/die Nutzer:in die Telefonnummer bestätigt hat, entfernen Sie die Telefonnummer über den [`/sms/invalid_phone_numbers/remove`-Endpunkt]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) aus der Ungültigkeitsliste.

## Empfehlungen zu Traffic Pumping {#traffic-pumping-recommendations}

### Was ist Traffic Pumping? {#what-is-traffic-pumping}

Traffic Pumping ist eine Form von Betrug, bei der ein böswilliger Akteur ein Online-Formular nutzt, um den Versand von SMS-Nachrichten in großem Umfang auszulösen (zum Beispiel Opt-in-Nachrichten oder Einmalpasswörter). Der böswillige Akteur richtet eine Premium-Telefonnummer ein, an die diese Nachrichten gesendet werden, und beansprucht eine Umsatzbeteiligung vom Mobilfunkbetreiber, bei dem die Premium-Nummer eingerichtet wurde, und generiert so unrechtmäßige Einnahmen.

### Wie Sie Traffic Pumping erkennen {#how-to-spot-traffic-pumping}

* Premium-Nummern, die diese Art von Betrug unterstützen, werden oft, aber nicht immer, in Ländern außerhalb Ihrer üblichen Versandregionen eingerichtet.
* Ungewöhnliche Spitzen beim Nachrichtenversand über Online-Formulare können auf Traffic Pumping hindeuten.
    * Wir empfehlen, [Campaign-Benachrichtigungen]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) einzurichten, um bei einer unplausibel hohen Anzahl gesendeter Nachrichten eine Obergrenze zu setzen und Benachrichtigungen zu erhalten.
* Unvollständig ausgefüllte Online-Formulare können auf ein programmatisches Ausfüllen hinweisen.
* Beim Erstellen von Online-Formularen empfehlen wir, Regeln festzulegen, die sicherstellen, dass Formulare vollständig ausgefüllt werden, und Tools wie CAPTCHA zu verwenden, um das Risiko zu minimieren.

### Auswirkungen von Traffic Pumping {#impact-of-traffic-pumping}

Kund:innen sind für die Überwachung des von ihnen gesendeten Datenverkehrs verantwortlich und werden für alle über ihr Konto gesendeten SMS in Rechnung gestellt. Zwischen Braze und dem/der Kund:in ist der/die Kund:in die Partei, die besser in der Lage ist, Traffic Pumping zu erkennen und zu verhindern.

## SMS-Versand in mehreren Ländern {#multi-country-sms-sending}

Einige Marken möchten Nachrichten an eine Gruppe von Nutzer:innen senden, deren Telefonnummern aus verschiedenen Ländern stammen. Um eine SMS an eine Telefonnummer in einem bestimmten Land zu senden, empfiehlt es sich als Best Practice, einen Langcode oder Shortcode aus demselben Land zu verwenden. Shortcodes können tatsächlich nur SMS an Telefonnummern aus dem Land senden, in dem der Shortcode erstellt wurde.

Um diese Einschränkung zu überwinden, können während des [Einrichtungsprozesses]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) der Abo-Gruppen Gruppen so konfiguriert werden, dass sie Lang- und Shortcodes aus mehreren verschiedenen Ländern enthalten. Nach der Einrichtung werden beim Start einer Campaign automatisch Telefonnummern mit derselben Landesvorwahl wie die Telefonnummer der Zielnutzer:innen verwendet. Sie müssen keine separaten Campaigns für Nutzer:innen mit Telefonnummern unterschiedlicher Landesvorwahlen erstellen, sodass Sie eine einzelne Campaign starten oder eine Canvas-Komponente verwenden können, um relevante Nutzer:innen anzusprechen.

![SMS-Payloads werden mit derselben Landesvorwahl wie die Telefonnummer der Zielnutzer:innen gesendet.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Allgemeine Best Practices für den Versand {#general-sending-best-practices}

1. **Erlaubnis einholen.** Eine der wichtigsten Regeln bei der geschäftlichen Nutzung von SMS ist, dass Sie zunächst die Erlaubnis von Kund:innen einholen müssen, bevor Sie sie kontaktieren. Andernfalls kann dies Ihrer Marke schaden und zu erheblichen Rechtskosten führen.
2. **Die richtige Nummer für Ihren Anwendungsfall wählen.** Drei Haupttypen von Telefonnummern können SMS senden und empfangen: Langcodes, Shortcodes und alphanumerische Absender-IDs. Ihre Funktionen und die Verfügbarkeit in verschiedenen Regionen variieren. Überlegen Sie im Voraus, ob ein Vanity-Code für Ihr Unternehmen besser geeignet ist.
3. **Auf das Timing achten.** Bedenken Sie, dass Kund:innen besser auf Inhalte reagieren, die direkt an sie gerichtet sind. Ein wenig Personalisierung bewirkt viel, z. B. die Verwendung des Vornamens der Empfänger:innen oder ein gesprächiger Ton, der die Interessen Ihrer Kund:innen widerspiegelt.
4. **Bidirektionale Gespräche führen.** SMS ist ein so effektiver Kanal für die Interaktion mit Kund:innen, dass es wichtig ist, Antworten auf Ihre Nachrichten zu antizipieren und effektiv zu handhaben. 85 % der Verbraucher:innen möchten nicht nur Informationen erhalten, sondern auch Unternehmen antworten oder ein Gespräch führen.
5. **Messen, was funktioniert.** Erreichen Sie Kund:innen zur richtigen Zeit, mit der besten Frequenz und mit den effektivsten Handlungsaufrufen? Die richtigen Tracking-Tools bieten direkte und messbare Metriken, die den ROI belegen.

## Versand in großen Mengen {#high-volume-sending}

Planen Sie einen Versand in großen Mengen? Wir haben einige Best Practices für Sie, damit alles reibungslos abläuft.

- Passen Sie das Rate-Limiting für die Zustellgeschwindigkeit Ihrer Campaign oder Canvases nach Bedarf an, basierend auf der Größe Ihrer Zielgruppe. So stellen Sie sicher, dass Sie das benötigte Sendevolumen erreichen und dass Braze Nachrichten mit der Rate sendet, die Ihr SMS- oder RCS-Anbieter erwartet und verarbeiten kann.
- Halten Sie sich an das Limit von 160 Zeichen und beachten Sie, dass Sonderzeichen doppelt gezählt werden (z. B. Schrägstriche `\`, Zirkumflexe `^` und Tilden `~`).

## Empfehlungen für Ruhezeiten {#quiet-hours-recommendations}

{% alert warning %}
**Die nativen Ruhezeiten von Braze garantieren keine Zustellzeiten auf Geräteebene.** Wenn eine Nachricht gesendet wird, wird sie an einen Mobilfunkanbieter übergeben. Sobald der Anbieter die Nachricht akzeptiert hat, hat Braze keine Kontrolle mehr über den genauen Zeitpunkt, zu dem sie auf dem Gerät der Nutzer:innen zugestellt wird.<br><br> Zum Beispiel: Wenn eine Nachricht um 20:59 Uhr an einen Anbieter übergeben wird, kann es sein, dass sie erst um 21:02 Uhr auf dem Gerät eintrifft. Um das Risiko zu reduzieren, empfehlen wir die folgende Liquid-basierte Ruhezeiten-Methode. Diese unterdrückt die Nachricht auf der Braze-Engine-Ebene, bevor sie übergeben wird.
{% endalert %}

### Native Ruhezeiten von Braze {#braze-native-quiet-hours}

Sie können [Ruhezeiten]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) über SMS-Campaigns und Canvases hinweg als zusätzliche Planungskontrolle aktivieren. Für Compliance-relevante Sendungen verwenden Sie die Liquid-basierte Absicherung im folgenden Abschnitt als primäre Kontrolle, bevor Nachrichten an Mobilfunkanbieter übergeben werden.

### Zusätzliche Absicherung durch Content Blocks {#additional-safeguard-through-content-blocks}

Sie können eine Liquid-basierte Prüfung in einem Content-Block hinzufügen. Dies bietet eine zuverlässige, skalierbare Absicherung, die zusammen mit den nativen Einstellungen funktioniert.

#### Einrichtung {#setup}

Fügen Sie den folgenden Snippet am Anfang Ihres SMS-Nachrichtentexts ein. Dieses Beispiel bricht den Versand ab, wenn er außerhalb eines Zeitfensters von 9:00 bis 21:00 Uhr in der [Ortszeit]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) der Nutzer:innen liegt.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour >= 21 or hour < 9 %}
  {% abort_message("Outside allowed time window") %}
{% endif %}
```
{% endraw %}

#### Hinweise

- {% raw %}`time_zone: ${time_zone}`{% endraw %} ermöglicht es, das Zeitfenster gegen die Ortszeit der einzelnen Nutzer:innen auszuwerten, nicht gegen eine feste globale Zeit, wie in den [Campaigns-FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) erläutert.
- Nachrichten, die durch {% raw %}`abort_message()`{% endraw %} unterdrückt werden, werden nicht für den nächsten Tag neu eingeplant; sie werden storniert.
- {% raw %} Standardmäßig sind abgebrochene Nachrichten nicht im regulären Campaign-Reporting sichtbar. Wenn Liquid jedoch einen Versand mit `{% abort_message %}` abbricht, protokolliert Braze dies im Nachrichtenaktivitätsprotokoll als Nachrichtenfehler (standardmäßig wird `{% abort_message %}` aufgerufen angezeigt). Wenn Sie einen String übergeben, wird dieser Grund im Protokoll angezeigt, z. B. `{% abort_message('language was nil') %}`{% endraw %}. Für Einblick in diese Unterdrückungen im Dashboard wenden Sie sich an Ihren Customer-Success-Manager, um Zugang zum [Messaging-Diagnostics-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) zu erhalten.