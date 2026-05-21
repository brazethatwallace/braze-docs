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

## Empfehlungen zur Opt-out-Überwachung {#opt-out-monitoring-recommendations}

Die Einhaltung von Opt-out-Anfragen von Empfänger:innen ist gesetzlich vorgeschrieben. Die Nichteinhaltung von Opt-out-Anfragen von SMS-Empfänger:innen kann Strafen nach sich ziehen, einschließlich Bußgeldern, und zu Klagen führen. Braze verfügt über Funktionen, die ein robustes Opt-in- und Opt-out-Management für SMS und MMS ermöglichen, sowie über Mechanismen, die sicherstellen, dass Anfragen korrekt verarbeitet werden.

Gemäß ihren Abo-Vereinbarungen mit uns sind unsere Kund:innen allein für die Einhaltung der geltenden Gesetze bei der Nutzung unserer Dienste verantwortlich. Dementsprechend empfehlen wir unseren Kund:innen dringend, auf die korrekte Konfiguration ihres SMS-Setups zu achten, diese Konfigurationen gründlich zu testen, Maßnahmen zur Überwachung der Opt-out-Compliance zu ergreifen und umgehend zu handeln, wenn Fälle der Nichteinhaltung von Opt-out-Anfragen festgestellt werden.

Wenn Sie SMS und MMS in Braze einrichten, um Opt-ins und Opt-outs zu verwalten, beachten Sie die folgende Liste von Ressourcen:
* [SMS-Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups/): Abo-Gruppen sowie Opt-in-/Opt-out-Methoden und -Status.
* [Abo-Gruppen-REST-APIs]({{site.baseurl}}/api/endpoints/subscription_groups/): Wie Opt-ins und Opt-outs verarbeitet werden, die aus einer anderen Quelle als einer direkten Antwort auf eine Nachricht stammen.
* [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/): Erläuterungen dazu, wie Braze die Schlüsselwortverarbeitung und -verwaltung handhabt.
* [SMS-Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/): Erfordert, dass Nutzer:innen ihre Opt-in-Absicht ausdrücklich bestätigen, bevor sie SMS-Nachrichten empfangen können. SMS-Double-Opt-in ist in einigen Ländern vorgeschrieben, daher empfiehlt Braze, dies zu konfigurieren.
* [SMS-Nachrichtenversand]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending/): Grundlagen des SMS-Versands bei Braze, einschließlich der Bedeutung von Abo-Gruppen, Anforderungen an SMS-Segmente und Nachrichteninhalte und mehr.

### Hinweise {#considerations}

Wenn SMS und MMS über mehrere Instanzen hinweg eingerichtet wurden und aufgrund einer Fehlkonfiguration Opt-outs einer Campaign oder eines Canvas an den falschen Workspace gesendet werden:

* Braze verfügt über eine Überwachung, um solche Fälle zu erkennen. Wenn dieses Verhalten festgestellt wird, leitet Braze die Opt-outs an die korrekte Instanz um und füllt alle Opt-outs nach, die während des Zeitraums aufgetreten sind.
* Wir empfehlen Kund:innen dringend, Opt-outs für jede Abo-Gruppe zu testen, die sie in Braze haben. Dieses Problem vor dem Versand einer Nachricht zu erkennen, ist besser, als es nach dem Auftreten zu beheben.

Braze verwaltet SMS-/MMS-Abos sowohl auf der Ebene des Nutzerprofils (`user_id`) als auch auf der Ebene der Telefonnummer (`channel_id`). Wenn eine Telefonnummer ein Opt-in oder Opt-out durchführt, gilt das Update für alle Profile, die diese Nummer teilen. Falls ein:e Endnutzer:in sich mit einer bestimmten Telefonnummer angemeldet hat und dann die Telefonnummer wechselt, übernimmt die neue Telefonnummer den Abo-Gruppenstatus der/des Nutzer:in. Wenn ein:e Endnutzer:in ein Opt-out durchgeführt hat, aber dann die App oder Website mit einer neuen Telefonnummer erneut nutzt, erhält sie/er dementsprechend keine unerwünschten Nachrichten.

## Empfehlungen zur Hygiene der Telefonnummernliste {#phone-number-list-hygiene-recommendations}

Die Pflege der Hygiene Ihrer Telefonnummernliste hilft Ihnen, gültige Einwilligungs- und Erreichbarkeitsdaten im Laufe der Zeit beizubehalten. Braze markiert einige Telefonnummern als ungültig, um das Compliance-Risiko zu reduzieren, einwilligungsbasierte Messaging-Praktiken zu unterstützen und den Versand an Nummern zu vermeiden, die möglicherweise nicht mehr der/dem ursprünglichen Nutzer:in gehören.

Gründe, warum Telefonnummern typischerweise als ungültig markiert werden, finden Sie unter [Umgang mit ungültigen Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#handling-invalid-phone-numbers).

Wir empfehlen den folgenden Workflow zum Entfernen ungültiger Telefonnummern:

1. Identifizieren Sie betroffene Telefonnummern über den [`/sms/invalid_phone_numbers`-Endpunkt]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/).
2. Unterscheiden Sie zwischen deaktivierten Telefonnummern und Telefonnummern, die Anbieterfehler erhalten haben.
3. Verifizieren Sie bei deaktivierten Telefonnummern die Telefonnummer erneut mit der/dem Nutzer:in. Nachdem die/der Nutzer:in ihre/seine Telefonnummer bestätigt hat, entfernen Sie die Telefonnummer über den [`/sms/invalid_phone_numbers/remove`-Endpunkt]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) von der Ungültig-Liste.

## Empfehlungen zum Traffic-Pumping {#traffic-pumping-recommendations}

### Was ist Traffic-Pumping? {#what-is-traffic-pumping}

Traffic-Pumping ist eine Form des Betrugs, bei der ein böswilliger Akteur ein Online-Formular nutzt, um den Versand von SMS-Nachrichten in großem Umfang auszulösen (z. B. Opt-in-Nachrichten oder Einmalpasswörter). Der böswillige Akteur richtet eine Premium-Rate-Telefonnummer ein, an die diese Nachrichten gesendet werden, und beansprucht eine Umsatzbeteiligung vom Mobilfunkbetreiber, bei dem die Premium-Rate-Nummer eingerichtet wurde, und generiert so illegale Einnahmen.

### Wie Sie Traffic-Pumping erkennen {#how-to-spot-traffic-pumping}

* Premium-Rate-Nummern, die diese Art von Betrug unterstützen, werden oft, aber nicht immer, in Ländern außerhalb Ihrer normalen Versandregionen eingerichtet.
* Ungewöhnliche Spitzen beim Versand von Nachrichten über Online-Formulare können auf Traffic-Pumping hindeuten.
    * Wir empfehlen, [Campaign-Benachrichtigungen]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts/) einzurichten, um eine Obergrenze festzulegen und benachrichtigt zu werden, wenn eine unplausibel hohe Anzahl von Nachrichten gesendet wird.
* Unvollständige Online-Formulare können auf programmatisches Ausfüllen von Formularen hindeuten.
* Beim Erstellen von Online-Formularen empfehlen wir, Regeln festzulegen, die sicherstellen, dass Formulare vollständig ausgefüllt werden, und Tools wie CAPTCHA zu verwenden, um das Risiko zu minimieren.

### Auswirkungen von Traffic-Pumping {#impact-of-traffic-pumping}

Kund:innen sind für die Überwachung des von ihnen gesendeten Traffics verantwortlich und werden für alle über ihr Konto gesendeten SMS in Rechnung gestellt. Zwischen Braze und dem/der Kund:in ist der/die Kund:in die Partei, die besser in der Lage ist, Traffic-Pumping zu erkennen und zu verhindern.

## Länderübergreifender SMS-Versand {#multi-country-sms-sending}

Einige Marken möchten möglicherweise an eine Gruppe von Nutzer:innen senden, deren Telefonnummern aus verschiedenen Ländern stammen. Um eine SMS-Nachricht an eine Telefonnummer in einem bestimmten Land zu senden, ist es Best Practice, einen Langcode oder Shortcode aus demselben Land zu verwenden. Tatsächlich können Shortcodes nur SMS an Telefonnummern aus dem Land senden, in dem der Shortcode erstellt wurde.

Um diese Einschränkung zu überwinden, können während des [Einrichtungsprozesses]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) der Abo-Gruppen Gruppen eingerichtet werden, die Lang- und Shortcodes aus mehreren verschiedenen Ländern enthalten. Nach Abschluss werden beim Starten einer Campaign automatisch Absender-Telefonnummern mit derselben Landesvorwahl wie die Telefonnummer der/des Zielnutzer:in verwendet. Sie müssen keine separaten Campaigns für Nutzer:innen mit Telefonnummern mit unterschiedlichen Landesvorwahlen erstellen, sodass Sie eine Campaign starten oder eine Canvas-Komponente verwenden können, um relevante Nutzer:innen anzusprechen.

![SMS-Payloads werden mit derselben Landesvorwahl wie die Telefonnummer der/des Zielnutzer:in gesendet.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Allgemeine Best Practices für den Versand {#general-sending-best-practices}

1. **Holen Sie die Erlaubnis ein.** Eine der wichtigsten Regeln für die geschäftliche Nutzung von SMS ist, dass Sie zunächst die Erlaubnis der Kund:innen einholen müssen, sie zu kontaktieren. Andernfalls kann dies Ihrer Marke schaden und zu hohen Rechtskosten führen.
2. **Wählen Sie die richtige Nummer für Ihren Anwendungsfall.** Drei Haupttypen von Telefonnummern können SMS-Nachrichten senden und empfangen: Langcodes, Shortcodes und alphanumerische Absender-IDs, deren Funktionen und Verfügbarkeit in verschiedenen Regionen variieren. Überlegen Sie im Voraus, ob Ihr Unternehmen mit einem Vanity-Code besser bedient ist.
3. **Achten Sie auf das Timing.** Bedenken Sie, dass Kund:innen auf Materialien, die direkt an sie gerichtet sind, besser reagieren. Ein wenig Personalisierung bewirkt viel, z. B. die Verwendung des Vornamens der/des Empfänger:in oder eine persönliche Note, die die Interessen Ihrer Kund:innen widerspiegelt.
4. **Führen Sie Zwei-Wege-Gespräche.** SMS ist ein so effektiver Kanal für die Interaktion mit Kund:innen, dass es wichtig ist, Antworten auf Ihre Nachrichten zu antizipieren und effektiv zu handhaben. 85 % der Verbraucher:innen möchten nicht nur Informationen erhalten, sondern auch Unternehmen antworten oder ein Gespräch führen können.
5. **Messen Sie, was funktioniert.** Erreichen Sie Kund:innen zur richtigen Zeit, mit der besten Häufigkeit und mit den effektivsten Handlungsaufforderungen? Die Verwendung der richtigen Tracking-Tools kann direkte und messbare Metriken liefern, die den ROI belegen.

## Versand großer Mengen {#high-volume-sending}

Planen Sie einen Versand großer Mengen? Wir haben einige Best Practices für Sie, damit alles reibungslos abläuft.

- Passen Sie das Rate-Limiting der Zustellgeschwindigkeit für Ihre Campaign oder Ihre Canvases nach Bedarf an, basierend auf der Größe der Zielgruppe. Dies stellt sicher, dass Sie das benötigte Sendevolumen erreichen und dass Braze die Nachrichten mit der Rate sendet, die Twilio erwartet und verarbeiten kann.
- Stellen Sie sicher, dass Sie das Limit von 160 Zeichen einhalten, und beachten Sie, dass Sonderzeichen doppelt gezählt werden (z. B. Schrägstriche `\`, Zirkumflexe `^` und Tilden `~`).

## Empfehlungen zu Ruhezeiten {#quiet-hours-recommendations}

{% alert warning %}
**Die nativen Ruhezeiten von Braze garantieren keine Zustellzeiten auf Geräteebene.** Wenn eine Nachricht gesendet wird, wird sie an einen Mobilfunkbetreiber übergeben. Sobald der Betreiber die Nachricht akzeptiert hat, hat Braze keine Kontrolle mehr über den genauen Zeitpunkt, zu dem sie auf dem Gerät der/des Nutzer:in zugestellt wird.<br><br> Wenn beispielsweise eine Nachricht um 20:59 Uhr an einen Betreiber übergeben wird, kann sie erst um 21:02 Uhr auf dem Gerät ankommen. Um das Risiko zu reduzieren, empfehlen wir die folgende Liquid-basierte Ruhezeiten-Methode. Diese unterdrückt die Nachricht auf Braze-Engine-Ebene vor der Übergabe.
{% endalert %}

### Native Ruhezeiten von Braze {#braze-native-quiet-hours}

Wir empfehlen dringend, [Ruhezeiten]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/#quiet-hours) für alle SMS-Campaigns und -Canvases zu aktivieren, um regionale Vorschriften und Best Practices einzuhalten.

### Zusätzliche Absicherung durch Content Blocks {#additional-safeguard-through-content-blocks}

Sie können eine Liquid-basierte Prüfung in einem Content-Block hinzufügen. Dies bietet eine zuverlässige, skalierbare Absicherung, die zusammen mit den nativen Einstellungen funktioniert.

#### Einrichtung {#setup}

Fügen Sie das folgende Snippet am Anfang Ihres SMS-Nachrichtentexts ein. Dieses Beispiel bricht den Versand ab, wenn er außerhalb eines Zeitfensters von 9:00 bis 21:00 Uhr in der [Ortszeit]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#what-does-local-time-zone-delivery-offer) der/des Nutzer:in liegt.

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

- {% raw %}`time_zone: ${time_zone}`{% endraw %} ermöglicht es, das Zeitfenster anhand der Ortszeit jeder/jedes Nutzer:in zu bewerten, nicht anhand einer festen globalen Zeit, wie in [dieser FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#what-does-local-time-zone-delivery-offer) erläutert.
- Nachrichten, die durch {% raw %}`abort_message()`{% endraw %} unterdrückt werden, werden nicht für den nächsten Tag neu geplant; sie werden abgebrochen.
- {% raw %} Standardmäßig sind abgebrochene Nachrichten im Standard-Campaign-Reporting nicht sichtbar. Wenn Liquid jedoch einen Versand mit `{% abort_message %}` abbricht, protokolliert Braze dies im Nachrichten-Aktivitätsprotokoll als Nachrichtenfehler (standardmäßig wird `{% abort_message %}` aufgerufen angezeigt). Wenn Sie einen String übergeben, wird dieser Grund im Protokoll angezeigt, z. B. `{% abort_message('language was nil') %}`{% endraw %}. Für Einblicke in diese Unterdrückungen im Dashboard wenden Sie sich an Ihren Customer-Success-Manager, um Zugang zum [Messaging-Diagnose-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/) zu erhalten.