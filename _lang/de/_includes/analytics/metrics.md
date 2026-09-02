{% if include.metric == "AMP Clicks" %}
<i>AMP-Klicks</i> ist die Gesamtzahl der Klicks in Ihrer AMP-HTML-E-Mail, kumuliert aus der HTML-, Klartext- und AMP-HTML-Version der E-Mail.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>AMP-Öffnungen</i> ist die Gesamtzahl der Öffnungen in Ihrer AMP-HTML-E-Mail und den AMP-HTML-Versionen der E-Mail.
{% endif %}

{% if include.metric == "Audience" %}
Die <i>Zielgruppe</i> ist der Prozentsatz der Nutzer:innen, die eine bestimmte Nachricht erhalten haben. Diese Zahl wird von Braze bereitgestellt.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Bounces</i> ist die Gesamtzahl der Nachrichten, die nicht erfolgreich an die vorgesehenen Empfänger:innen zugestellt werden konnten.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
Die <i>geschätzten realen Öffnungen</i> sind eine Schätzung der Anzahl der eindeutigen Öffnungen, die es geben würde, wenn es keine maschinellen Öffnungen gäbe, und sind das Ergebnis eines proprietären statistischen Modells von Braze.
{% endif %}

{% if include.metric == "Help" %}
<i>Hilfe</i> bedeutet, dass ein:e Nutzer:in auf Ihre Nachricht mit dem <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">Schlüsselwort HELP</a> geantwortet hat und eine automatische HELP-Antwort erhalten hat.
{% endif %}

{% if include.metric == "Hard Bounce" %}
Ein <i>Hard Bounce</i> liegt vor, wenn eine E-Mail aufgrund eines dauerhaften Zustellungsfehlers nicht an die Empfänger:in zugestellt werden kann. Ein Hard Bounce kann auftreten, weil der Domainname nicht existiert oder weil die Empfänger:in unbekannt ist.
{% endif %}

{% if include.metric == "Soft Bounce" %}
Ein <i>Soft Bounce</i> liegt vor, wenn eine E-Mail aufgrund eines vorübergehenden Zustellungsfehlers nicht an die Empfänger:in zugestellt werden kann, obwohl die E-Mail-Adresse der Empfänger:in gültig ist. Ein Soft Bounce kann auftreten, weil der Posteingang der Empfänger:in voll ist, der Server ausgefallen ist oder die Nachricht zu groß für den Posteingang der Empfänger:in war.
{% endif %}

{% if include.metric == "Deferral" %}
Eine <i>Zurückstellung</i> liegt vor, wenn eine E-Mail nicht sofort zugestellt werden konnte. Braze versucht jedoch, die E-Mail bis zu 72 Stunden nach diesem vorübergehenden Zustellungsfehler erneut zuzustellen, um die Chancen auf eine erfolgreiche Zustellung zu maximieren, bevor die Versuche für diese spezifische Campaign eingestellt werden.
{% endif %}

{% if include.metric == "Body Click" %}
Push-Story-Benachrichtigungen zeichnen einen <i>Body Click</i> auf, wenn die Benachrichtigung angeklickt wird. Er wird nicht aufgezeichnet, wenn eine Nachricht erweitert oder ein Aktions-Button angeklickt wird.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>Body Clicks</i> treten auf, wenn ein:e Nutzer:in auf eine Nachricht klickt, die keine Buttons (Button 1, Button 2) hat und mit dem traditionellen Editor erstellt wurde, und wenn eine Nachricht, die mit dem HTML-Editor oder dem Drag-and-Drop-Editor erstellt wurde, <code>brazeBridge.logClick()</code> ohne Argumente verwendet.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Button-1-Klicks</i> ist die Gesamtzahl der Klicks auf Button 1 der Nachricht.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Button-2-Klicks</i> ist die Gesamtzahl der Klicks auf Button 2 der Nachricht.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Eingereichte Auswahlen</i> ist die Gesamtzahl der ausgewählten Optionen, wenn ein:e Nutzer:in auf der Seite mit den Umfragefragen einer <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a> auf den Button „Senden“ klickt.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
Die <i>Klick-Öffnungsrate</i> ist der Prozentsatz der geöffneten E-Mails, die mindestens einmal von einer einzelnen Nutzer:in oder einem Gerät angeklickt wurden, und ist nur im <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/data_and_analytics/reporting/report_builder/'>Berichts-Builder</a> verfügbar.
{% endif %}

{% if include.metric == "Close Message" %}
<i>Nachricht schließen</i> ist die Gesamtzahl der Klicks auf den Button „Schließen“ der Nachricht. Dies gilt nur für In-App-Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, nicht mit dem traditionellen Editor.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>Bestätigte Zustellungen</i> liegen vor, wenn der Anbieter bestätigt hat, dass die Nachricht an die Zielrufnummer zugestellt wurde.
{% endif %}

{% if include.metric == "Confidence" %}
Die <i>Konfidenz</i> ist der Prozentsatz des Vertrauens, dass eine bestimmte Variante einer Nachricht besser abschneidet als die Kontrollgruppe.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Bestätigungsseiten-Button</i> ist die Gesamtzahl der Klicks auf den Call-to-Action-Button auf der Bestätigungsseite einer <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>Bestätigungsseiten-Ausblendungen</i> ist die Gesamtzahl der Klicks auf den Button „Schließen“ (x) auf der Bestätigungsseite einer <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
Die <i>Konversionsrate</i> ist der Prozentsatz der Häufigkeit, mit der ein definiertes Ereignis im Vergleich zu allen Empfänger:innen einer Nachricht eingetreten ist. Dieses definierte Ereignis wird festgelegt, wenn Sie die Campaign erstellen.
{% endif %}

{% if include.metric == "Conversion Window" %}
Das <i>Konversionsfenster</i> ist die Anzahl der Tage nach Erhalt der Nachricht, in denen die Aktionen der Nutzer:innen verfolgt und einem Konversions-Event zugeordnet werden. Konversionen, die nach diesem Fenster stattfinden, werden nicht dem Konversions-Event zugeschrieben.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>Konversionen (B, C, D)</i> sind zusätzliche Konversions-Events, die nach dem primären Konversions-Event hinzugefügt werden. Dies ist die Anzahl der Male, die ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Campaign eingetreten ist.
{% endif %}

{% if include.metric == "Total Conversions" %}
Die <i>Gesamtzahl der Konversionen</i> ist die Gesamtzahl der Fälle, in denen ein:e Nutzer:in ein bestimmtes Konversions-Event abschließt, nachdem er/sie eine In-App-Nachrichten-Campaign gesehen hat.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Zustellungen</i> ist die Gesamtzahl (oder der Prozentsatz) der Nachrichtenanfragen, die vom empfangenden Server angenommen wurden. Das bedeutet nicht, dass die Nachricht an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht vom Server akzeptiert wurde.
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>Zustellungen %</i> ist der prozentuale Anteil an der Gesamtzahl der Nachrichten (Sendungen), die erfolgreich an E-Mail-fähige Empfänger:innen gesendet und von diesen empfangen wurden.
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>Zustellungsfehler</i> treten auf, wenn die SMS nicht gesendet werden konnte, weil die Warteschlangen überlaufen sind (SMS werden mit einer höheren Rate gesendet, als Ihre Lang- oder Shortcodes verarbeiten können).
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>Zustellungsfehler</i> treten auf, wenn die RCS nicht gesendet werden konnte, weil die Warteschlangen überlaufen sind (RCS werden mit einer höheren Rate gesendet, als Ihr RCS-verifizierter Sender verarbeiten kann).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
Die <i>Rate der fehlgeschlagenen Zustellungen</i> ist der Prozentsatz der Sendungen, die fehlgeschlagen sind, weil die Nachricht nicht zugestellt werden konnte. Dafür kann es verschiedene Gründe geben, z. B. Überläufe in der Warteschlange, Kontosperrungen und Medienfehler bei MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direkte Öffnungen</i> ist die Gesamtzahl (oder der Prozentsatz) der Nutzer:innen, die Ihre App oder Website durch direktes Drücken der Benachrichtigung geöffnet haben.
{% endif %}

{% if include.metric == "Emailable" %}
<i>E-Mail-erreichbar</i> ist die Gesamtzahl der Nutzer:innen, die über eine hinterlegte E-Mail-Adresse verfügen und sich explizit angemeldet oder abonniert haben.
{% endif %}

{% if include.metric == "Errors" %}
<i>Fehler</i> ist die Anzahl der von Webhook-Events zurückgegebenen Fehler (wird während des Sendevorgangs erhöht).
{% endif %}

{% if include.metric == "Failures" %}
<i>Fehlschläge</i> treten auf, wenn die WhatsApp-Nachricht nicht gesendet werden konnte, weil der Internet-Provider einen Hard Bounce zurückgegeben hat. Ein Hard Bounce bedeutet einen dauerhaften Zustellbarkeitsfehler.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Beeinflusste Öffnungen</i> ist die Gesamtzahl (oder der Prozentsatz) der Nutzer:innen, die die App geöffnet haben, nachdem die Push-Benachrichtigung gesendet wurde, ohne die Push-Nachricht direkt zu öffnen.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>Lifetime-Umsatz</i> ist der gesamte <code>PurchaseEvents</code>-Preiswert (in USD), der seit der Einführung eingenommen wurde.
{% endif %}

{% if include.metric == "LTV Per User" %}
Der <i>LTV pro Nutzer:in</i> ist der <i>Lifetime-Umsatz</i> geteilt durch Ihre gesamten <i>Nutzer:innen</i> (auf Ihrer Startseite).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
Der <i>durchschnittliche Tagesumsatz</i> ist der Durchschnitt der Summe der Campaign- und Canvas-Einnahmen für einen bestimmten Tag.
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>Tägliche Käufe</i> ist der Durchschnitt der gesamten eindeutigen <code>PurchaseEvents</code> über den Zeitraum.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
Der <i>Tagesumsatz pro Nutzer:in</i> ist der durchschnittliche Tagesumsatz pro täglich aktiver Nutzer:in.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Automatische Öffnungen</i> umfasst sowohl nicht-menschliche als auch menschliche Öffnungen, die auf eine Öffnung durch eine:n Nutzer:in mit aktiviertem Apple E-Mail-Datenschutz (E-Mail-Datenschutz) hinweisen. Das bedeutet, dass ein:e Nutzer:in mehrere <i>automatische Öffnungen</i> protokollieren kann. <i>Automatische Öffnungen</i> werden nicht automatisch generiert, wenn das Gerät nicht mit WLAN verbunden ist, sodass ein:e Nutzer:in eine E-Mail in der Apple-Mail-App möglicherweise öffnet, bevor Apple die Bilder vorab abruft, was dennoch als <i>automatische Öffnung</i> protokolliert wird.
<br><br>
Für Nutzer:innen mit aktiviertem E-Mail-Datenschutz:
<ul>
  <li>1+ <i>automatische Öffnung</i>: Apple hat die Nachricht vorab abgerufen oder die Nutzer:in hat eine E-Mail auf einem iOS-Gerät proaktiv geöffnet</li>
  <li>2+ <i>automatische Öffnungen</i>: Braze hat keinen Einblick in menschliche gegenüber nicht-menschlichen Öffnungen, sodass dies aus mehreren menschlichen Öffnungen (auf einem Apple-Gerät oder mehreren) oder einer Kombination aus menschlichen Öffnungen und einer Öffnung durch Apples Vorabruf der Nachricht bestehen kann</li>
</ul>
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Andere Öffnungen</i> umfasst menschliche Öffnungen, die nicht von E-Mail-Datenschutz betroffen sind (z. B. wenn ein:e Nutzer:in eine E-Mail in der Gmail-App oder auf Gmail Desktop öffnet, wodurch ein Tracking-Pixel ausgelöst und eine reguläre Öffnung protokolliert wird). <i>Andere Öffnungen</i> sind in der Regel menschliche Öffnungen, es kann jedoch auch Szenarien geben, in denen ein Gerät die E-Mail öffnet (ein Bot oder ein Posteingangs-Dienstleister wie Gmail oder Yahoo). Es ist auch möglich, dass ein:e Nutzer:in eine E-Mail auf einem Nicht-iOS-Gerät öffnet und die <i>andere Öffnung</i> protokolliert wird, bevor eine <i>automatische Öffnung</i> protokolliert wird.
<br><br>
Da <i>automatische Öffnungen</i> nutzergesteuert sein können, ist das Verhältnis zwischen <i>automatischen Öffnungen</i> und <i>anderen Öffnungen</i> nicht menschlich gegenüber nicht-menschlich, sondern vielmehr E-Mail-Datenschutz-betroffen gegenüber nicht E-Mail-Datenschutz-betroffen. Während <i>andere Öffnungen</i> weiterhin herangezogen werden können, um einen Teil der menschlichen Öffnungen zu messen, ist es derzeit nicht möglich, den Prozentsatz der <i>automatischen Öffnungen</i> zu bestimmen, die menschlich gesteuert sind, sodass eine genaue „echte“ Öffnungsrate derzeit nicht ermittelt werden kann.
<br><br>
Für Nutzer:innen mit aktiviertem E-Mail-Datenschutz:
<ul>
  <li>+1 <i>andere Öffnung(en)</i>: Die Nutzer:in hat eine E-Mail auf einem Nicht-iOS-Gerät proaktiv geöffnet</li>
  <li>+1 <i>automatische Öffnung(en)</i> und +1 <i>andere Öffnungen</i>: Apple hat die Nachricht vorab abgerufen oder die Nutzer:in hat eine E-Mail auf einem iOS-Gerät proaktiv geöffnet und eine E-Mail auf einem Nicht-iOS-Gerät proaktiv geöffnet</li>
</ul>
Für Nutzer:innen ohne aktiviertes E-Mail-Datenschutz:
<ul>
  <li>+1 <i>andere Öffnung(en)</i>: Die Nutzer:in hat eine E-Mail auf einem beliebigen Gerät proaktiv geöffnet</li>
</ul>
{% endif %}

{% if include.metric == "Opens" %}
<i>Öffnungen</i> sind Instanzen, die sowohl <i>direkte Öffnungen</i> als auch <i>beeinflusste Öffnungen</i> umfassen, bei denen das Braze SDK mithilfe eines proprietären Algorithmus festgestellt hat, dass eine Push-Benachrichtigung ein:e Nutzer:in zum Öffnen der App veranlasst hat.
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>Opt-Out</i> liegt vor, wenn ein:e Nutzer:in auf Ihre Nachricht mit einem <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">Opt-Out-Schlüsselwort</a> geantwortet hat und sich von Ihrem SMS- oder RCS-Programm abgemeldet hat.
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Ausstehende Wiederholung</i> ist die Anzahl der Anfragen, die vom empfangenden Server vorübergehend abgelehnt wurden, bei denen der E-Mail-Anbieter (E-Mail-Anbieter) aber dennoch versucht hat, sie erneut zuzustellen. Der E-Mail-Anbieter versucht die Zustellung so lange zu wiederholen, bis eine Timeout-Periode erreicht ist (normalerweise nach 72 Stunden).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Primäre Konversionen (A)</i> oder <i>primäres Konversions-Event</i> ist die Anzahl der Male, die ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Campaign eingetreten ist. Dieses definierte Ereignis wird von Ihnen bei der Erstellung der Campaign festgelegt.
{% endif %}

{% if include.metric == "Reads" %}
<i>Gelesen</i> bedeutet, dass ein:e Nutzer:in die Nachricht gelesen hat. Die Lesebestätigungen der Nutzer:innen müssen aktiviert sein, damit Braze die Lesevorgänge verfolgen kann.
{% endif %}

{% if include.metric == "Read Rate" %}
Die <i>Leserate</i> ist der Prozentsatz der Sendungen, die zu einem Lesevorgang geführt haben. Dies gilt nur für Nutzer:innen, die Lesebestätigungen aktiviert haben.
{% endif %}

{% if include.metric == "Received" %}
<i>Empfangen</i> wird je nach Kanal unterschiedlich definiert und kann erfolgen, wenn Nutzer:innen die Nachricht ansehen, eine definierte Trigger-Aktion ausführen oder die Nachricht an den Nachrichtenanbieter gesendet wird.
{% endif %}

{% if include.metric == "Rejections" %}
<i>Ablehnungen</i> liegen vor, wenn die SMS oder RCS vom Netzbetreiber abgelehnt wurde. Dies kann verschiedene Gründe haben, z. B. die Filterung von Inhalten durch den Anbieter, die Verfügbarkeit des Zielgeräts, die Telefonnummer ist nicht mehr in Betrieb und Ähnliches.
{% endif %}

{% if include.metric == "Revenue" %}
Der <i>Umsatz</i> ist der Gesamtumsatz in Dollar von Campaign-Empfänger:innen innerhalb des festgelegten <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>primären Konversionsfensters</a>.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Gesendete Nachrichten</i> ist die Gesamtzahl der in einer Campaign gesendeten Nachrichten. Nach dem Start einer geplanten Campaign umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sent" %}
<i>Gesendet</i> bedeutet, dass eine Campaign oder ein Canvas-Schritt gestartet oder getriggert wurde und eine SMS oder RCS von Braze gesendet wurde. Es ist möglich, dass die SMS oder RCS das Gerät einer Nutzer:in aufgrund von Fehlern nicht erreicht hat.
{% endif %}

{% if include.metric == "Sends" %}
<i>Sendungen</i> ist die Gesamtzahl der in einer Campaign gesendeten Nachrichten. Nach dem Start einer geplanten Campaign umfasst diese Metrik alle gesendeten Nachrichten, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden. Das bedeutet nicht, dass die Nachricht empfangen oder an ein Gerät zugestellt wurde, sondern nur, dass die Nachricht gesendet wurde.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>Sendungen an Netzbetreiber</i> ist veraltet, wird aber für Nutzer:innen, die es bereits haben, weiterhin unterstützt. Es handelt sich um die Summe der <i>bestätigten Zustellungen</i>, <i>Ablehnungen</i> und <i>Sendungen</i>, bei denen die Zustellung oder Ablehnung nicht vom Netzbetreiber bestätigt wurde. Dies umfasst auch Fälle, in denen Netzbetreiber keine Zustell- oder Ablehnungsbestätigung liefern, da einige Netzbetreiber diese Bestätigung nicht liefern oder zum Zeitpunkt des Versands nicht liefern können.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
Die <i>Rate der Sendungen an Netzbetreiber</i> ist der Prozentsatz der insgesamt gesendeten Nachrichten, die als <i>Sendungen an Netzbetreiber</i> eingestuft wurden. Dies umfasst auch Fälle, in denen Netzbetreiber keine Zustell- oder Ablehnungsbestätigung liefern, da einige Netzbetreiber diese Bestätigung nicht liefern oder zum Zeitpunkt des Versands nicht liefern können. Diese Metrik ist veraltet, wird aber für Nutzer:innen, die sie bereits haben, weiterhin unterstützt.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> ist die Gesamtzahl der zugestellten E-Mails, die von der Empfänger:in als „Spam“ markiert wurden. Braze ändert zwar nicht den Abo-Status dieser Nutzer:innen, aber diese Nutzer:innen werden in zukünftigen E-Mails automatisch ausgeschlossen, es sei denn, Sie senden eine Transaktions-E-Mail, die so konfiguriert ist, dass sie „an alle Nutzer:innen gesendet wird, einschließlich Abgemeldeter“.
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Umfrageseiten-Ausblendungen</i> ist die Gesamtzahl der Klicks auf den Button „Schließen“ (x) auf der Seite mit den Umfragefragen einer <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Umfrage-Übermittlungen</i> ist die Gesamtzahl der Klicks auf den Button „Senden“ einer <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>einfachen Umfrage</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Klicks insgesamt</i> ist die Anzahl (oder der Prozentsatz) der eindeutigen Empfänger:innen, die auf einen Link in der zugestellten Nachricht geklickt haben.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Ausblendungen insgesamt</i> ist die Anzahl der Fälle, in denen Nutzer:innen eine Nachricht aus einer Campaign ausgeblendet haben. Bei Content Cards wird jede Kartenausblendung gezählt. Bei Bannern wird jedes Mal gezählt, wenn ein:e Nutzer:in das Banner ausgeblendet hat, sofern das Ausblendungsverhalten aktiviert ist.
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>Impressionen insgesamt</i> ist die Anzahl der Fälle, in denen eine Nachricht angezeigt wird. Braze protokolliert eine Impression nur dann, wenn die Nachricht für die Nutzer:in auf dem Bildschirm sichtbar wird. Wenn beispielsweise eine Nachricht am Ende einer Seite platziert wird, wird die Impression erst protokolliert, wenn die Nutzer:in nach unten scrollt und die Nachricht sichtbar wird. Wenn einer Nutzer:in dieselbe Nachricht zweimal angezeigt wird, wird dies als zwei Impressionen gezählt.
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Öffnungen gesamt</i> ist die Gesamtzahl der Nachrichten, die geöffnet wurden.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Gesamtumsatz</i> ist der Gesamtumsatz in Dollar von Campaign-Empfänger:innen innerhalb des festgelegten primären Konversionsfensters.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Eindeutige Klicks</i> ist die eindeutige Anzahl von Empfänger:innen, die mindestens einmal auf einen Link innerhalb einer Nachricht geklickt haben, und wird gemessen durch <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a>.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Eindeutige Ausblendungen</i> ist die Anzahl der eindeutigen Empfänger:innen, die eine Content Card aus einer Campaign ausgeblendet haben. Wenn ein:e Nutzer:in eine Content Card aus einer Campaign mehrmals ausblendet, zählt dies als eine eindeutige Ausblendung.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>Eindeutige Impressionen</i> ist die Gesamtzahl der Nutzer:innen, die eine Nachricht aus einer bestimmten Campaign angesehen haben. Eine Impression wird nur dann protokolliert, wenn die Nachricht auf dem Bildschirm einer Nutzer:in sichtbar wird.
{% endif %}

{% if include.metric == "Unique Daily Impressions" %}
<i>Eindeutige tägliche Impressionen</i> ist die Anzahl der eindeutigen Nutzer:innen, die die Nachricht an einem bestimmten Tag angesehen haben. Dieser Zähler wird jeden Kalendertag zurückgesetzt, sodass ein:e Nutzer:in, die dieselbe Nachricht an zwei verschiedenen Tagen ansieht, zweimal gezählt wird. Diese Metrik entspricht der gleichnamigen Abrechnungsmetrik.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Eindeutige Empfänger:innen</i> ist die Anzahl der eindeutigen täglichen Empfänger:innen, also der Nutzer:innen, die an einem Tag eine neue Nachricht erhalten haben. Damit diese Zahl für ein:e Nutzer:in mehr als einmal erhöht wird, muss die Person eine neue Nachricht an einem anderen Tag erhalten.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Eindeutige Öffnungen</i> ist die Gesamtzahl (oder der Prozentsatz) der zugestellten Nachrichten, die von einer einzelnen Nutzer:in mindestens einmal geöffnet wurden und über einen Zeitraum von sieben Tagen verfolgt werden.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Abmelder:innen</i> oder <i>Unsub</i> ist die Anzahl der Nachrichten, die zu einer Abmeldung geführt haben. Abmeldungen erfolgen, wenn Braze eine Abmeldung über die Braze-Abmelde-URL im Nachrichtentext oder über den List-Unsubscribe-Header verarbeitet, sofern dieser Pfad von Braze gehandhabt wird.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Abmeldungen</i> ist die Anzahl der Empfänger:innen, deren Abo-Status sich über einen von Braze verwalteten Abmeldepfad in „Abgemeldet“ geändert hat, einschließlich der Braze-Abmelde-URL im Nachrichtentext und des List-Unsubscribe-Headers, wenn Braze die Anfrage verarbeitet.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variante</i> ist die Anzahl der Varianten einer Campaign, die sich nach den Vorgaben der Ersteller:in unterscheiden.
{% endif %}