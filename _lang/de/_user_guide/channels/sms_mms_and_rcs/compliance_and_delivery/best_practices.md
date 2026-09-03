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

Die Einhaltung von Abmeldewünschen (Opt-out) durch Empfänger:innen ist gesetzlich vorgeschrieben. Die Nichteinhaltung von Opt-out-Anfragen durch SMS-Empfänger:innen kann Strafen nach sich ziehen, einschließlich Bußgelder, und zu Klagen führen. Braze bietet Features für ein robustes SMS- und MMS-Opt-in- und Opt-out-Management sowie Mechanismen, die sicherstellen, dass Anfragen korrekt verarbeitet werden.

Gemäß ihren Abonnementvereinbarungen mit uns sind unsere Kund:innen allein für die Einhaltung der geltenden Gesetze bei der Nutzung unserer Dienste verantwortlich. Daher empfehlen wir unseren Kund:innen dringend, die korrekte Konfiguration ihres SMS-Setups genau zu beachten, diese Setups gründlich zu testen, Maßnahmen zur Überwachung der Opt-out-Compliance zu ergreifen und umgehend zu handeln, wenn Fälle der Nichteinhaltung von Opt-out-Anfragen festgestellt werden.

Wenn Sie SMS und MMS in Braze einrichten, um Opt-ins und Opt-outs zu verwalten, beachten Sie die folgende Liste mit Ressourcen:
* [SMS-Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups): Abo-Gruppen und Opt-in-/Opt-out-Methoden und -Status.
* [Abo-Gruppen-REST-APIs]({{site.baseurl}}/api/endpoints/subscription_groups): Verarbeitung von Opt-ins und Opt-outs, die aus einer anderen Quelle als einer direkten Antwort auf eine Nachricht stammen.
* [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Erläuterungen zur Schlüsselwortverarbeitung und -verwaltung in Braze.
* [SMS-Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): Erfordert, dass Nutzer:innen ihre Opt-in-Absicht ausdrücklich bestätigen, bevor sie SMS-Nachrichten empfangen können. SMS-Double-Opt-in ist in einigen Ländern vorgeschrieben, daher empfiehlt Braze, dies zu konfigurieren.
* [SMS-Nachrichtenversand]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): Grundlagen des SMS-Versands bei Braze, einschließlich der Bedeutung von Abo-Gruppen, Anforderungen an SMS-Segmente und Nachrichtentexte und mehr.

### Hinweise {#considerations}

Wenn SMS und MMS über mehrere Instanzen hinweg eingerichtet sind, kann eine fehlerhafte Konfiguration dazu führen, dass Opt-outs aus Campaigns oder Canvases an den falschen Workspace gesendet werden.

* Braze verfügt über Überwachungsmechanismen, um solche Fälle zu erkennen. Wird dieses Verhalten festgestellt, wendet Braze die Opt-outs auf die richtige Instanz an und gleicht alle nach, die während des Zeitraums aufgetreten sind.
* Wir empfehlen Kund:innen dringend, Opt-outs für jede Abo-Gruppe zu testen, die sie in Braze haben. Dieses Problem vor dem Versand einer Nachricht zu erkennen, ist besser, als es erst nach dem Auftreten zu beheben.

Braze verwaltet SMS-/MMS-Abonnements sowohl auf Kundenprofil-Ebene (`user_id`) als auch auf Telefonnummer-Ebene (`channel_id`). Wenn für eine Telefonnummer ein Opt-in oder Opt-out durchgeführt wird, gilt die Aktualisierung für alle Profile, die diese Nummer teilen. Wenn ein:e Nutzer:in sich mit einer bestimmten Telefonnummer angemeldet hat und dann die Telefonnummer wechselt, übernimmt die neue Telefonnummer den Abo-Gruppenstatus des/der Nutzer:in. Wenn sich ein:e Nutzer:in abgemeldet hat und dann mit einer neuen Telefonnummer die App oder Website erneut nutzt, erhält er/sie entsprechend keine unerwünschten Nachrichten.

## Empfehlungen zur Pflege der Telefonnummernlisten {#phone-number-list-hygiene-recommendations}

Die Pflege der Telefonnummernlisten hilft Ihnen, gültige Einwilligungs- und Erreichbarkeitsdaten über die Zeit hinweg beizubehalten. Braze markiert einige Telefonnummern als ungültig, um Compliance-Risiken zu reduzieren, einwilligungsbasierte Messaging-Praktiken zu unterstützen und den Versand an Nummern zu vermeiden, die möglicherweise nicht mehr der/dem ursprünglichen Nutzer:in gehören.

Informationen zu den Gründen, warum Telefonnummern typischerweise als ungültig markiert werden, finden Sie unter [Umgang mit ungültigen Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Wir empfehlen den folgenden Workflow, um ungültige Telefonnummern zu entfernen:

1. Identifizieren Sie betroffene Telefonnummern über den [`/sms/invalid_phone_numbers`-Endpunkt]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Unterscheiden Sie zwischen Telefonnummern, die deaktiviert wurden, und Telefonnummern, die Anbieterfehler erhalten haben.
3. Verifizieren Sie deaktivierte Telefonnummern erneut mit der/dem Nutzer:in. Nachdem die/der Nutzer:in ihre/seine Telefonnummer bestätigt hat, entfernen Sie die Telefonnummer über den [`/sms/invalid_phone_numbers/remove`-Endpunkt]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) von der Ungültigkeitsliste.

## Empfehlungen zu Traffic Pumping {#traffic-pumping-recommendations}

### Was ist Traffic Pumping? {#what-is-traffic-pumping}

Traffic Pumping ist eine Form von Betrug, bei der ein böswilliger Akteur ein Online-Formular nutzt, um in großem Umfang den Versand von SMS-Nachrichten auszulösen (zum Beispiel Opt-in-Nachrichten oder Einmalpasswörter). Der böswillige Akteur richtet eine Premiumnummer ein, an die diese Nachrichten gesendet werden, und beansprucht eine Umsatzbeteiligung vom Mobilfunkanbieter, bei dem die Premiumnummer eingerichtet wurde, um so illegale Einnahmen zu generieren.

### Wie Sie Traffic Pumping erkennen {#how-to-spot-traffic-pumping}

* Premiumnummern, die diese Art von Betrug unterstützen, werden häufig, aber nicht immer, in Ländern außerhalb Ihrer üblichen Versandregionen eingerichtet.
* Ungewöhnliche Spitzen beim Nachrichtenversand über Online-Formulare können auf Traffic Pumping hinweisen.
    * Wir empfehlen, [Campaign-Benachrichtigungen]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) einzurichten, um eine Obergrenze festzulegen und benachrichtigt zu werden, wenn eine unplausibel hohe Anzahl an Nachrichten versendet wird.
* Unvollständige Online-Formulare können auf programmatisches Ausfüllen hinweisen.
* Beim Erstellen von Online-Formularen empfehlen wir, Regeln festzulegen, die sicherstellen, dass Formulare vollständig ausgefüllt werden, und Tools wie CAPTCHA zu verwenden, um das Risiko zu minimieren.

### Auswirkungen von Traffic Pumping {#impact-of-traffic-pumping}

Kund:innen sind dafür verantwortlich, den von ihnen generierten Datenverkehr zu überwachen, und erhalten eine Rechnung für alle über ihr Konto gesendeten SMS. Zwischen Braze und dem/der Kund:in ist der/die Kund:in die Partei, die in der besseren Position ist, Traffic Pumping zu erkennen und zu verhindern.

## SMS-Versand in mehrere Länder {#multi-country-sms-sending}

Einige Marken möchten Nachrichten an eine Gruppe von Nutzer:innen senden, deren Telefonnummern aus verschiedenen Ländern stammen. Um eine SMS an eine Telefonnummer in einem bestimmten Land zu senden, empfiehlt es sich als Best Practice, einen Langcode oder Shortcode zu verwenden, der aus demselben Land stammt. Tatsächlich können Shortcodes nur SMS an Telefonnummern aus dem Land senden, in dem der Shortcode erstellt wurde.

Um diese Einschränkung zu umgehen, können während des [Einrichtungsprozesses]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) der Abo-Gruppen Gruppen eingerichtet werden, die Lang- und Shortcodes aus mehreren verschiedenen Ländern enthalten. Nach Abschluss werden beim Starten einer Campaign automatisch Absender-Telefonnummern mit derselben Landesvorwahl wie die Telefonnummer der/des Zielnutzer:in verwendet. Sie müssen keine separaten Campaigns für Nutzer:innen mit Telefonnummern mit unterschiedlichen Landesvorwahlen erstellen, sodass Sie eine Campaign starten oder eine Canvas-Komponente verwenden können, um relevante Nutzer:innen anzusprechen.

![SMS-Payloads werden mit derselben Landesvorwahl wie die Telefonnummer der/des Zielnutzer:in gesendet.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Allgemeine Best Practices für den Versand {#general-sending-best-practices}

1. **Holen Sie die Erlaubnis ein.** Eine der wichtigsten Regeln bei der geschäftlichen Nutzung von SMS ist, dass Sie zunächst die Erlaubnis der Kund:innen einholen müssen, sie zu kontaktieren. Wenn Sie dies versäumen, kann das Ihrer Marke schaden und zu hohen Rechtskosten führen.
2. **Wählen Sie die richtige Nummer für Ihren Anwendungsfall.** Es gibt drei Haupttypen von Telefonnummern, die SMS senden und empfangen können: Langcodes, Shortcodes und alphanumerische Absender-IDs. Deren Funktionen und Verfügbarkeit variieren je nach Region. Überlegen Sie im Voraus, ob Ihr Unternehmen mit einem Vanity-Code besser bedient ist.
3. **Achten Sie auf das Timing.** Bedenken Sie, dass Kund:innen stärker auf Inhalte reagieren, die direkt an sie gerichtet sind. Ein wenig Personalisierung kann viel bewirken, etwa die Verwendung des Vornamens der Empfänger:innen oder ein gesprächiger Ton, der die Interessen Ihrer Kund:innen widerspiegelt.
4. **Führen Sie Zwei-Wege-Gespräche.** SMS ist ein so effektiver Kanal für die Interaktion mit Kund:innen, dass es wichtig ist, Antworten auf Ihre Nachrichten zu antizipieren und effektiv zu bearbeiten. 85 % der Verbraucher:innen möchten nicht nur Informationen empfangen, sondern auch Unternehmen antworten oder an einem Gespräch teilnehmen.
5. **Messen Sie, was funktioniert.** Erreichen Sie Ihre Kund:innen zur richtigen Zeit, mit der besten Frequenz und mit den effektivsten Handlungsaufforderungen? Die Verwendung der richtigen Tracking-Tools kann direkte und messbare Metriken liefern, die den Kapitalrendite belegen.

## Versand großer Mengen {#high-volume-sending}

Planen Sie einen Versand großer Mengen? Wir haben einige Best Practices für Sie, damit alles reibungslos abläuft.

- Passen Sie das Rate-Limiting für die Zustellgeschwindigkeit Ihrer Campaign oder Canvases nach Bedarf an die Größe der Zielgruppe an. So stellen Sie sicher, dass Sie das benötigte Sendevolumen erreichen und Braze die Nachrichten mit der Rate sendet, die Twilio erwartet und verarbeiten kann.
- Halten Sie sich an das Limit von 160 Zeichen und beachten Sie, dass Sonderzeichen doppelt gezählt werden (zum Beispiel Schrägstriche `\`, Zirkumflexe `^` und Tilden `~`).

## Empfehlungen für Ruhezeiten {#quiet-hours-recommendations}

{% alert warning %}
**Die nativen Ruhezeiten von Braze garantieren keine gerätebezogenen Zustellzeiten.** Wenn eine Nachricht gesendet wird, wird sie an einen Mobilfunkanbieter übergeben. Sobald der Anbieter die Nachricht akzeptiert hat, hat Braze keine Kontrolle mehr über den genauen Zeitpunkt, zu dem sie auf dem Gerät der Nutzer:innen zugestellt wird.<br><br> Wenn beispielsweise eine Nachricht um 20:59 Uhr an einen Anbieter übergeben wird, kann sie möglicherweise erst um 21:02 Uhr auf dem Gerät ankommen. Um dieses Risiko zu verringern, empfehlen wir die folgende Liquid-basierte Methode für Ruhezeiten. Diese unterdrückt die Nachricht auf Braze-Engine-Ebene vor der Übergabe.
{% endalert %}

### Native Ruhezeiten von Braze {#braze-native-quiet-hours}

Wir empfehlen dringend, [Ruhezeiten]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) für alle SMS-Campaigns und Canvases zu aktivieren, um regionale Vorschriften und Best Practices einzuhalten.

### Zusätzliche Absicherung durch Content Blocks {#additional-safeguard-through-content-blocks}

Sie können eine Liquid-basierte Prüfung in einem Content-Block hinzufügen. Dies bietet eine zuverlässige, skalierbare Absicherung, die neben den nativen Einstellungen funktioniert.

#### Einrichtung {#setup}

Fügen Sie das folgende Snippet am Anfang Ihres SMS-Nachrichtentexts ein. Dieses Beispiel bricht den Versand ab, wenn er außerhalb eines Zeitfensters von 9:00 bis 21:00 Uhr in der [Ortszeit]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) der Nutzer:innen liegt.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour >= 21 or hour < 9 %}
  {% abort_message("Outside allowed time window") %}
{% endif %}
```
{% endraw %}

#### Überlegungen

- {% raw %}`time_zone: ${time_zone}`{% endraw %} ermöglicht es, das Zeitfenster anhand der Ortszeit jeder einzelnen Nutzer:in zu bewerten – nicht anhand einer festen globalen Zeit, wie in den [FAQ zu Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) erläutert.
- Nachrichten, die durch {% raw %}`abort_message()`{% endraw %} unterdrückt werden, werden nicht für den nächsten Tag neu geplant; sie werden storniert.
- {% raw %} Standardmäßig sind abgebrochene Nachrichten nicht in der standardmäßigen Campaign-Berichterstattung sichtbar. Wenn Liquid einen Versand jedoch mit `{% abort_message %}` abbricht, protokolliert Braze dies im Message Activity Log als Nachrichtenfehler (standardmäßig wird `{% abort_message %}` called angezeigt). Wenn Sie einen String übergeben, wird dieser Grund im Log angezeigt, z. B. `{% abort_message('language was nil') %}`{% endraw %}. Für einen Einblick in diese Unterdrückungen im Dashboard wenden Sie sich an Ihren CSM, um Zugang zum [Messaging Diagnostics Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) zu erhalten.