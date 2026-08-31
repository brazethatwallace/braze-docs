---
nav_title: FAQ
article_title: E-Mail-FAQ
page_order: 30
description: "Diese Seite enthält Antworten auf häufig gestellte Fragen zum E-Mail-Messaging."
channel: email

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu E-Mails.

## Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

Wenn mehrere Nutzer:innen mit übereinstimmenden E-Mail-Adressen in einem Segment enthalten sind, das eine Campaign erhalten soll, wird zum Zeitpunkt des Versands ein einzelnes Nutzerprofil mit dieser E-Mail-Adresse ausgewählt. Auf diese Weise wird die E-Mail nur einmal gesendet und dedupliziert, um sicherzustellen, dass sie nicht mehrmals an dieselbe E-Mail-Adresse gelangt.

**Eindeutige E-Mail-Adressen:** Braze erzwingt keine eindeutigen E-Mail-Adressen über Profile hinweg. Wenn Sie auf eine Eins-zu-eins-Beziehung zwischen einer E-Mail-Adresse und einem Profil angewiesen sind, überwachen Sie intern auf Duplikate, wenn Sie Nutzer:innen erstellen.

**Deduplizierung vor Liquid:** Bei Versendungen, bei denen Braze innerhalb eines Versands nach E-Mail-Adresse dedupliziert (z. B. geplante Campaigns, bei denen mehrere Segmentmitglieder mit derselben Adresse zusammen verarbeitet werden), erfolgt die Deduplizierung, bevor Liquid für das ausgewählte Profil ausgeführt wird, das diese Adresse repräsentiert. Wenn Liquid für dieses Profil abbricht (z. B. mit [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), erhält diese Adresse die Nachricht bei diesem Versand nicht – einschließlich Profilen, die bereits durch die Deduplizierung übersprungen wurden. Getriggerte Versendungen wenden dieselbe Adress-Deduplizierung innerhalb eines Versands nicht an; mehrere Profile, die eine Adresse teilen, können alle in einem Batch berechtigt bleiben, sodass dieses Abbruchverhalten nicht auf dieselbe Weise gilt (siehe nächster Absatz).

Wenn mehrere Profile eine E-Mail-Adresse teilen und ein Profil sich abmeldet, aktualisiert Braze andere Profile (bis zu 100) mit dieser Adresse auf denselben Abo-Status. Dies gilt für Abmeldungen und andere Änderungen wie den globalen Abo-Status und individuelle Abo-Gruppenstatusänderungen.

**Seed-Gruppen:** Bei Campaigns mit [Seed-Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) wählt Braze ein Profil für die primäre Zustellung aus, wenn mehrere Profile eine Adresse teilen. Diese:r primäre Empfänger:in befindet sich möglicherweise nicht in Ihrer Seed-Gruppe, selbst wenn ein anderes Profil mit derselben Adresse darin enthalten ist.

Die folgenden Szenarien können den Eindruck erwecken, dass ein:e Nutzer:in eine E-Mail doppelt erhalten hat:

- **Seed-Listen oder Testempfänger:innen:** Seed-Adressen und interne Testempfänger:innen können einen Versand zusätzlich zu Ihrer Hauptzielgruppe erhalten, was wie ein Duplikat wirken kann, wenn ein Posteingang sowohl einem Profil als auch einem Seed-Eintrag entspricht.
- **Ein Fehler trat während der Campaign- oder Canvas-Erstellung auf:** Nutzer:innen erhalten möglicherweise nicht denselben Versand doppelt, aber sie erhalten möglicherweise zwei separate E-Mails mit derselben Betreffzeile. Wenn eine Campaign oder ein Canvas dupliziert wird, überprüfen Sie die E-Mail-Konfigurationsdetails wie Bilder oder Betreffzeilen. Sie können auch die Changelogs einsehen, um festzustellen, ob die Campaign oder das Canvas nach dem Start geändert wurde – ein Duplikat kann dieselbe Betreffzeile wie das Original aufweisen, als Nutzer:innen es erhielten.
- **Mehrere Nutzerprofile haben E-Mail-Weiterleitung:** Wenn ein:e Nutzer:in mehrere Konten in einer bestimmten App hat, aber ein Konto E-Mails weiterleitet, erhält der:die Nutzer:in die Campaign einmal pro Posteingang; E-Mails können im Posteingang, in den Nachrichten weitergeleitet werden, doppelt erscheinen. Nur einige Anbieter zeigen an, wenn eine E-Mail von einem anderen Konto weitergeleitet wurde.
- **E-Mail-Konfiguration beim Empfänger:** Einige Clients führen Posteingänge zusammen („universeller Posteingang“). Wenn dieselbe Campaign mehrere Konten mit einem gemeinsamen Posteingang anspricht, kann es so aussehen, als hätte eine Person die Campaign doppelt erhalten, obwohl tatsächlich zwei unterschiedliche Profile angeschrieben wurden. Der:die Empfänger:in kann bestätigen, ob mehrere Konten in einem Posteingang zusammengefasst sind.

Diese Deduplizierung gilt, wenn die angesprochenen Nutzer:innen im selben Versand sind. Die erneute Berechtigung wird pro Profil bewertet, nicht pro E-Mail-Adresse.

Die erneute Berechtigung für E-Mail-Campaigns und Canvas-Schritte basiert auf dem Nutzerprofil – nicht auf dem Posteingang – sodass mehrere Profile sich für separate Versendungen qualifizieren können, während diese Logik erfüllt ist. In Kombination mit Triggern kann dies mehr als eine Nachricht an denselben Posteingang senden, selbst wenn Sie versuchen, eine einzelne Sperrfrist auf Adressebene einzuhalten. Getriggerte Campaigns (ausgenommen API-getriggerte Campaigns) und Canvases können auch zweimal an eine Adresse senden, wenn verschiedene Profile mit übereinstimmenden E-Mail-Adressen den Trigger zu unterschiedlichen Zeiten auslösen – beispielsweise wenn Nutzer:in A und Nutzer:in B `johndoe@example.com` teilen, sich aber in unterschiedlichen Zeitzonen befinden und der Versand lokale Zeitzonen verwendet.

Nutzer:innen werden beim Canvas-Eintritt nicht nach E-Mail dedupliziert, sodass sie möglicherweise über den ersten Schritt eines Canvas hinaus nicht dedupliziert werden, wenn sie aufgrund von Rate-Limited Entry zu leicht unterschiedlichen Zeiten fortschreiten. Wenn ein:e Nutzer:in, die:der einer bestimmten E-Mail-Adresse zugeordnet ist, eine E-Mail öffnet oder anklickt, werden alle Nutzerprofile, die diese E-Mail-Adresse teilen, als geöffnet oder geklickt für die Campaign markiert.

### Ausnahme: API-getriggerte Campaigns {#exception-api-triggered-campaigns}

API-getriggerte Campaigns deduplizieren oder senden Duplikate, je nachdem, wo die Zielgruppe definiert ist. Doppelte E-Mails müssen separat im API-Aufruf unter Verwendung unterschiedlicher `user_ids` angesprochen werden, um mehrere Zustellungen zu erhalten. Hier sind drei mögliche Szenarien für API-getriggerte Campaigns:

- **Szenario 1: Doppelte E-Mails im Zielsegment:** Wenn dieselbe E-Mail in mehreren Nutzerprofilen erscheint, die in den Zielgruppenfiltern des Dashboards für eine API-getriggerte Campaign gruppiert sind, erhält nur eines der Profile die E-Mail.
- **Szenario 2: Doppelte E-Mails in unterschiedlichen `user_ids` innerhalb des Recipients-Objekts:** Wenn dieselbe E-Mail innerhalb mehrerer `external_user_id`-Werte erscheint, die vom `recipients`-Objekt referenziert werden, wird die E-Mail zweimal gesendet.
- **Szenario 3: Doppelte E-Mails aufgrund doppelter `user_ids` innerhalb des Recipients-Objekts:** Wenn Sie versuchen, dasselbe Nutzerprofil zweimal hinzuzufügen, erhält nur eines der Profile die E-Mail.

{% alert important %}
Wenn Sie eine API-Campaign über einen API-Aufruf senden (ausgenommen API-getriggerte Campaigns) und mehrere Nutzer:innen im Segment mit derselben E-Mail-Adresse angegeben sind, wird an diese Adresse so oft gesendet, wie sie im Aufruf aufgeführt ist. Dies liegt daran, dass API-Aufrufe als absichtlich konstruiert angesehen werden.
{% endalert %}

#### A/B-Tests mit doppelten E-Mail-Adressen {#ab-testing-with-duplicate-email-addresses}

Vermeiden Sie [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing) bei E-Mails, wenn mehrere Profile dieselbe E-Mail-Adresse teilen können. Varianten werden pro Profil zugewiesen, was zu mehr als einer Nachricht an denselben Posteingang führen kann. Wenn Sie in dieser Situation testen müssen, kombinieren Sie keinen **Gewinnervariante**-Schritt mit [Ortszeit-Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) in einer Weise, die die Auswahl des Gewinners verzögert – diese Optionen zusammen können die Wahrscheinlichkeit doppelter Versendungen erhöhen.

#### Canvas und doppelte E-Mail-Adressen {#canvas-and-duplicate-email-addresses}

Bei Canvas Journeys kann es von Entry-Batching, Schritt-Timing und anderen Faktoren abhängen, ob doppelte E-Mail-Adressen einen oder mehrere Versendungen erhalten. Betrachten Sie das Verhalten als undefiniert, bis Sie es für Ihre Journey validiert haben. Führen Sie nach Möglichkeit doppelte Profile zusammen oder konsolidieren Sie sie. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="deterministic deduplication for duplicate email addresses in Canvas" %}

### Was passiert mit dem Abo-Status, wenn die E-Mail-Adresse eines:einer Nutzer:in auf eine Adresse geändert wird, die ein:e andere:r Nutzer:in bereits verwendet? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Wenn Sie die E-Mail-Adresse für Nutzer:in A auf eine andere E-Mail-Adresse setzen oder aktualisieren, die bereits von einem bestehenden Nutzer:in B geteilt wird, übernimmt Nutzer:in A den Abo-Status, der bereits von Nutzer:in B existiert, es sei denn, die Einstellung **Nutzer:innen beim Aktualisieren ihrer E-Mail erneut anmelden** ist aktiviert.

### Werden Aktualisierungen meiner E-Mail-Versandeinstellungen rückwirkend angewendet? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

Nein. Aktualisierungen der E-Mail-Versandeinstellungen wirken sich nicht rückwirkend auf bestehende Versendungen aus. Wenn Sie beispielsweise Ihren Standard-Anzeigenamen in den E-Mail-Einstellungen ändern, wird der bestehende Standard-Anzeigename in Ihren aktiven Campaigns oder Canvases nicht automatisch ersetzt.

### Was ist eine „gute“ E-Mail-Zustellrate? {#what-is-a-good-email-delivery-rate}

Typischerweise liegt die „magische Zahl“ bei etwa 98 % zugestellter Nachrichten mit einer Absprungrate von nicht mehr als 3 %. Wenn weniger als 98 % der Nachrichten zugestellt werden, besteht in der Regel Anlass zur Sorge.

Allerdings kann eine Zustellrate von 98 % oder höher dennoch Zustellbarkeitsprobleme aufweisen. Wenn beispielsweise alle Ihre Bounces von einer einzigen Domain stammen, ist das ein klares Signal für ein Reputationsproblem bei diesem Anbieter.

Zusätzlich können Nachrichten zwar zugestellt werden, aber im Spam landen, was auf potenziell ernsthafte Reputationsprobleme hinweist. Es ist wichtig, nicht nur die Anzahl der zugestellten Nachrichten zu überwachen, sondern auch die Öffnungs- und Klickraten, um festzustellen, ob die Nutzer:innen die Nachrichten tatsächlich in ihrem Posteingang sehen. Da Anbieter in der Regel nicht jeden Spam-Fall melden, kann selbst eine Spam-Rate von 1 % Anlass zur Sorge und weiterer Analyse sein.

Schließlich können auch Ihr Unternehmen und die Art der E-Mails, die Sie versenden, die Zustellung beeinflussen. Beispielsweise sollte jemand, der hauptsächlich [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) versendet, eine bessere Rate erwarten als jemand, der viele Marketing-Nachrichten sendet.

### Warum ergeben meine E-Mail-Zustellmetriken zusammen nicht 100 %? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

E-Mail-Zustellmetriken (Zustellungen, Bounces und Spam-Rate) ergeben möglicherweise zusammen nicht 100 %, weil E-Mails soft gebounced werden und dann nach der Wiederholungsperiode von bis zu 72 Stunden nicht zugestellt werden.

Soft Bounces sind E-Mails, die aufgrund eines vorübergehenden Problems zurückgewiesen werden, wie z. B. „Postfach voll“, „Server vorübergehend nicht verfügbar“ und mehr. Wenn eine soft gebouncte E-Mail nach 72 Stunden immer noch nicht zugestellt wird, wird diese E-Mail nicht in den Zustellmetriken der Campaign berücksichtigt.

### Was ist eine E-Mail-Feedback-Schleife? {#what-is-an-email-feedback-loop}

Eine E-Mail-Feedback-Schleife (FBL) ermöglicht es Absendern, ihre Reputation zu überwachen, indem sie Campaigns identifizieren, die ein hohes Volumen an Beschwerden erhalten. Informationen zur Implementierung einer Gmail-Feedback-Schleife finden Sie im Artikel [Googles Feedback Loop](https://support.google.com/a/answer/6254652).

### Was sind Open-Tracking-Pixel? {#what-are-open-tracking-pixels}

[Open-Tracking-Pixel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) verwenden die E-Mail-Klick-Tracking-Domain des Absenders, um E-Mail-Öffnungsereignisse zu verfolgen. Das Pixel ist ein Bild-Tag, das dem HTML der E-Mail angehängt wird. Es ist meist das letzte HTML-Element innerhalb des Body-Tags. Wenn ein:e Nutzer:in ihre E-Mail lädt, wird eine Anfrage gestellt, um das Bild von der markierten Tracking-Domain zu laden, was ein Öffnungsereignis protokolliert.

### Kann ich Öffnungen für E-Mails verfolgen, die als Nur-Text dargestellt werden? {#can-i-track-opens-for-emails-rendered-in-plain-text}

Nein. Braze verfolgt E-Mail-Öffnungen mithilfe eines [Open-Tracking-Pixels]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#open-tracking-pixel), das in das HTML der E-Mail eingebettet ist. Wenn der E-Mail-Client des:der Empfänger:in die E-Mail lädt, wird dieses Bild angefordert, und Braze protokolliert ein Öffnungsereignis.

Da Nur-Text-E-Mails keine Bilder enthalten können, ist das Open-Tracking-Pixel nicht enthalten, sodass Öffnungen für E-Mails, die als Nur-Text dargestellt werden, nicht verfolgt werden können. Klicks können weiterhin verfolgt werden, da Hyperlinks in Nur-Text funktionsfähig bleiben.

Dies ist das erwartete Verhalten. Für die Genauigkeit der Öffnungsrate sollten Sie E-Mails als HTML gestalten und beachten, dass Öffnungen nicht gezählt werden, wenn Empfänger:innen die Nur-Text-Version anzeigen.

### Wie funktioniert das E-Mail-Tracking, wenn Empfänger:innen E-Mails weiterleiten? {#how-does-email-tracking-work-when-recipients-forward-emails}

Wenn ein:e Empfänger:in eine E-Mail weiterleitet, enthält die weitergeleitete E-Mail dasselbe Open-Tracking-Pixel und dieselben Klick-Tracking-Links wie das Original. Das bedeutet:

- Wenn jemand, der nicht zur ursprünglichen Campaign-Zielgruppe gehörte, eine weitergeleitete E-Mail erhält und öffnet, protokolliert Braze ein Öffnungsereignis.
- Wenn diese Person auf einen Link in der weitergeleiteten E-Mail klickt, protokolliert Braze ein Klickereignis.
- Diese Ereignisse werden dem Profil des:der ursprünglichen Empfänger:in zugeordnet, nicht der Person, die die weitergeleitete E-Mail erhalten hat, da das Tracking-Pixel und die Links mit dem:der ursprünglichen Empfänger:in verknüpft sind.

Braze kann nicht zwischen Öffnungen und Klicks des:der ursprünglichen Empfänger:in und denen von Personen, die eine weitergeleitete Kopie erhalten haben, unterscheiden. Dies ist das Standardverhalten für E-Mail-Tracking-Pixel und betrifft alle E-Mail-Anbieter.

Beachten Sie bei der Analyse von E-Mail-Metriken, dass Weiterleitungsaktivitäten zu Öffnungs- und Klickzahlen beitragen können. Wenn Sie ungewöhnlich hohe Engagement-Raten oder wiederholte Aktivitäten desselben Profils über einen Zeitraum bemerken, kann Weiterleitung ein Faktor sein.

### Was passiert, wenn eine E-Mail-Campaign oder ein Canvas gestoppt wird? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Nutzer:innen werden daran gehindert, in das Canvas einzutreten, und es werden keine weiteren Nachrichten gesendet.

Bei E-Mail-Campaigns und Canvases stoppt die Stopp-Schaltfläche den Versand nicht sofort. Wenn die Versandanfragen gesendet werden, können sie nicht mehr davon abgehalten werden, an den:die Nutzer:in zugestellt zu werden, was mit einer gewissen Verzögerung geschehen kann.

Obwohl Braze keine weiteren Anfragen sendet, sobald die Campaign oder das Canvas gestoppt wurde, können die Analytics weiterhin steigen, während der ESP bereits in Bearbeitung befindliche Anfragen abschließt.

### Warum sehe ich in meinen E-Mail-Analytics mehr _Klicks insgesamt_ als _Öffnungen insgesamt_? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

_Öffnungen insgesamt_ ist die Anzahl, wie oft die E-Mail von Nutzer:innen geöffnet wurde, während _Klicks insgesamt_ die Anzahl der Klicks von Nutzer:innen innerhalb der zugestellten E-Mail ist, einschließlich aller Arten von Klicks wie Linkklicks. Sie sehen möglicherweise aus einem der folgenden Gründe mehr Klicks als Öffnungen:

- Nutzer:innen führen innerhalb einer einzelnen Öffnung mehrere Klicks im E-Mail-Body aus.
- Nutzer:innen klicken auf einige E-Mail-Links in der Vorschauansicht ihres Telefons. In diesem Fall protokolliert Braze diese E-Mail als geklickt, aber nicht als geöffnet.
- Nutzer:innen öffnen eine E-Mail erneut, die sie zuvor in der Vorschau angesehen hatten.

### Warum sind meine Klickzahlen höher als mein Segment der Nutzer:innen, die geklickt haben? {#why-are-my-click-counts-higher-than-my-segment-of-users-who-clicked}

Campaign Analytics zeigen die Gesamtzahl der Klickereignisse, während Segmente die Anzahl der eindeutigen Nutzer:innen zurückgeben, die diese Klicks ausgeführt haben. Da jede:r Nutzer:in mehrmals klicken kann, ist die Gesamtzahl der Klicks in den Analytics oft höher als die Anzahl der Nutzer:innen, die geklickt haben, wenn Sie ein Segment erstellen.

Wenn beispielsweise 100 Nutzer:innen jeweils 3-mal auf einen Link klicken, zeigen die Campaign Analytics 300 Klicks insgesamt, aber ein Segment, das nach „E-Mail geklickt“ für diese Campaign gefiltert wird, gibt 100 Nutzer:innen zurück.

### Warum sehe ich keine E-Mail-Öffnungen und -Klicks? {#why-am-i-seeing-zero-email-opens-and-clicks}

Sie sehen möglicherweise keine E-Mail-Öffnungen oder -Klicks, wenn eine Fehlkonfiguration in Ihrer Tracking-Domain vorliegt. Dies kann auf einen der folgenden Gründe zurückzuführen sein:
- Es gibt ein SSL-Problem, bei dem Tracking-URLs `http` statt `https` verwenden.
- Es gibt ein Problem mit Ihrem CDN, bei dem der User-Agent-String bei den Öffnungsereignissen, Klickereignissen oder beiden nicht befüllt wird.

### Warum sehe ich ungewöhnliches E-Mail-Öffnungs- oder -Klickverhalten? {#why-am-i-seeing-unusual-email-open-or-click-behavior}

Wenn Sie unerwartete Muster in Ihren E-Mail-Öffnungs- oder -Klickmetriken bemerken – wie z. B. ein:e einzelne:r Nutzer:in, die:der scheinbar sofort jeden Link klickt, oder Öffnungen, die nicht wie erwartet registriert werden –, überprüfen Sie die folgenden häufigen Ursachen:

#### E-Mail-Clipping entfernt das Tracking-Pixel {#email-clipping-removes-the-tracking-pixel}

Wenn eine E-Mail vom E-Mail-Anbieter des:der Empfänger:in abgeschnitten wird (z. B. wenn Gmail Nachrichten über ca. 102 KB kürzt), kann Inhalt am Ende der E-Mail abgeschnitten werden. Da das Open-Tracking-Pixel normalerweise am Ende der E-Mail eingefügt wird, kann das Clipping verhindern, dass das Open-Tracking funktioniert.

**So erkennen Sie es:** Überprüfen Sie, ob die E-Mail am Ende einen Link wie „Gesamte Nachricht anzeigen“ oder ähnlich anzeigt. Sie können [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) verwenden, um die vollständig scrollbare E-Mail als Vorschau anzuzeigen und zu überprüfen, ob die Nachricht abgeschnitten wird.

**So beheben Sie es:** Sie können Braze so konfigurieren, dass das Tracking-Pixel oben statt unten in der E-Mail platziert wird. Das Verschieben des Tracking-Pixels kann beeinflussen, wie einige E-Mail-Clients Ihr HTML rendern. Testen Sie daher Ihre E-Mails in Inbox Vision, nachdem Sie diese Änderung vorgenommen haben. Beachten Sie, dass Öffnungen nicht verfolgt werden können, wenn der:die Empfänger:in Bilder deaktiviert hat, unabhängig von der Pixel-Platzierung.

#### Tracking-Pixel verursacht weißen Zwischenraum am oberen Rand der E-Mail {#tracking-pixel-causes-white-gap-at-top-of-email}

Wenn das Open-Tracking-Pixel am oberen Rand einer E-Mail positioniert ist, kann eine sichtbare weiße Linie oder Lücke am oberen Rand des E-Mail-Bodys erscheinen, insbesondere auf Mobilgeräten.

**So erkennen Sie es:** Gehen Sie in Braze zu **Einstellungen** > **E-Mail-Einstellungen** und wählen Sie den Abschnitt **Open-Tracking-Pixel**. Wenn **Verschieben für SendGrid**, **Verschieben für SparkPost** oder **Verschieben für Amazon SES** für Ihren Versandanbieter aktiviert ist, wird das Pixel am oberen Rand Ihres E-Mail-HTML positioniert. Wenn Sie eine weiße Lücke oder Linie am oberen Rand Ihrer gerenderten E-Mail bemerken, kann diese Einstellung die Ursache sein.

**So beheben Sie es:** Deaktivieren Sie den entsprechenden Schalter **Verschieben für SendGrid**, **Verschieben für SparkPost** oder **Verschieben für Amazon SES** im Abschnitt **Open-Tracking-Pixel** für Ihren Versandanbieter. Das Tracking-Pixel ist am Ende einer E-Mail normalerweise weniger sichtbar. Testen Sie Ihre E-Mails in [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision), nachdem Sie die Platzierung geändert haben. Weitere Informationen finden Sie unter [Platzierung aktualisieren]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement).

#### Verzögerte Statistiken oder Klicks ohne Öffnungen {#delayed-stats-or-clicks-without-opens}

Open-Tracking basiert darauf, dass der:die Empfänger:in die E-Mail mit aktivierten Bildern lädt. In einigen Fällen können Statistiken verzögert erscheinen oder Klicks ohne entsprechende Öffnungen protokolliert werden, weil:

- Der:die Empfänger:in die E-Mail in einer Vorschauansicht anzeigt, ohne sie vollständig zu öffnen, und dann Links direkt aus der Vorschau klickt.
- Der E-Mail-Client Bilder (und damit das Tracking-Pixel) erst lädt, nachdem der:die Empfänger:in bereits mit Links interagiert hat.

#### Sicherheitssoftware simuliert Linkklicks {#security-software-simulates-link-clicks}

Einige E-Mail-Sicherheitstools für Unternehmen (wie Barracuda, Proofpoint und ähnliche Dienste) scannen eingehende E-Mails, indem sie automatisch alle Links in der Nachricht klicken, um zu überprüfen, ob sie sicher sind. Dies kann dazu führen, dass Klickereignisse innerhalb von Sekunden nach dem Versand erscheinen, oft mit jedem Link in der E-Mail, der in schneller Abfolge geklickt wird.

Dieses Verhalten ist häufiger bei institutionellen E-Mail-Domains (wie Schulen, Universitäten und Unternehmensumgebungen) und ist wahrscheinlicher, wenn sich Ihre Versanddomain erheblich von Ihrer Tracking-Domain unterscheidet. Die Einrichtung einer [benutzerdefinierten markierten Tracking-Domain]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) kann die Häufigkeit dieser automatisierten Klicks reduzieren.

**So erkennen Sie es:** Suchen Sie die IP-Adresse des Klickereignisses (verfügbar in Currents-Daten) in einer Suchmaschine. Wenn die IP mit einem bekannten Sicherheitsanbieter (wie Barracuda Networks) verknüpft ist, sind die Klicks wahrscheinlich automatisiert. Möglicherweise sehen Sie auch einen konsistenten User-Agent-Header über mehrere automatisierte Klicks hinweg.

Weitere Informationen darüber, wie Sicherheitsscans E-Mail-Metriken beeinflussen, finden Sie unter [Umgang mit erhöhten Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting).

### Welche potenziellen Risiken birgt das Auslösen von Server-Klicks? {#what-are-the-potential-risks-of-triggering-server-clicks}

Bestimmte Elemente einer E-Mail-Nachricht, wie übermäßig lange Nachrichten oder zu viele Ausrufezeichen, können E-Mail-Sicherheitsreaktionen auslösen. Diese Reaktionen können das Reporting und die IP-Reputation beeinflussen und dazu führen, dass sich Nutzer:innen abmelden.

Best Practices zum Umgang mit diesen Reaktionen finden Sie unter [Umgang mit erhöhten Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting).

### Kann Braze Abmeldelinks verfolgen, die zur Metrik „Abmeldungen“ gezählt werden? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze verfolgt Abmeldelinks, wenn folgender Liquid in E-Mails verwendet wird: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Warum sehe ich eine andere Anzahl von Abmeldungen als Klicks auf meinen Abmeldelink? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

Wenn es mehr _Abmeldungen_ als Nutzer:innen gibt, die den Abmeldelink im E-Mail-Body geklickt haben, erklärt [**List-Unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) häufig die Differenz. List-Unsubscribe ist ein zusätzlicher Abmeldepfad im E-Mail-Header (nicht der Link in Ihrem Nachrichtentext). Wenn sich ein:e Nutzer:in auf diese Weise abmeldet, zählt dies zu den _Abmeldungen_, wird aber nicht als Klick auf die verfolgte Abmelde-URL im Body gewertet.

Wenn die Gesamtzahl der Klicks auf den Body-Abmeldelink größer ist als die Anzahl der _Abmeldungen_, haben Nutzer:innen den Link möglicherweise mehr als einmal geklickt – beispielsweise wenn sie sich abmelden, erneut anmelden und dann wieder abmelden. Die E-Mail-Analytics können dann mehrere Klicks in der Klick-Aufschlüsselung erfassen.

Wenn ein:e Nutzer:in den Abmeldelink zweimal klickt (z. B. wenn er:sie sich abmeldet, wieder anmeldet und dann erneut abmeldet), wird dies in den E-Mail-Analytics zweimal gezählt.

### Kann ich einen „Diese E-Mail im Browser anzeigen“-Link zu meinen E-Mails hinzufügen? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Nein. Braze bietet diese Funktionalität nicht an. Dies liegt daran, dass eine wachsende Mehrheit der E-Mails auf Mobilgeräten und in modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte ohne Probleme rendern.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing-Page hosten (z. B. Ihrer Website), die dann über das **Link**-Tool beim Bearbeiten des E-Mail-Bodys aus der E-Mail-Campaign verlinkt werden kann.

### Wandelt Braze automatisch Klartext-URLs oder „www.“-Text in Links um? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

Nein. Braze scannt Ihre Nachricht nicht und konvertiert keinen Klartext, wie Text, der mit `www.` beginnt oder wie eine URL aussieht, in Hyperlinks. Nur Links, die Sie mit HTML-Anchor-Tags (`<a href="...">`) definieren, werden durch das normale Rendering und die Link-Funktionen in Braze verarbeitet.

Wenn ein:e Empfänger:in Klartext als klickbaren Link sieht, kommt dieses Verhalten normalerweise von ihrem E-Mail-Client (z. B. Gmail, Outlook oder Apple Mail). Viele Clients erkennen URL-ähnliche Zeichenketten, nachdem die Nachricht zugestellt wurde, und wandeln sie auf dem Gerät des:der Empfänger:in in Links um. Braze kontrolliert dieses Verhalten nicht und kann es für den:die Empfänger:in nicht deaktivieren.

Verwenden Sie für ein vorhersehbares Link-Erscheinungsbild, Tracking und Styling explizite `<a href>`-Tags anstelle von Klartext-URLs.

### Kann ich das `target`-Attribut bei E-Mail-Links steuern? {#can-i-control-the-target-attribute-on-email-links}

Obwohl Sie das `target`-Attribut (wie `target="_blank"` oder `target="_top"`) bei Links in Ihrem E-Mail-HTML setzen können, ignorieren oder überschreiben die meisten E-Mail-Clients dieses Attribut. Gmail beispielsweise erzwingt effektiv ein `_blank`-ähnliches Verhalten, unabhängig davon, was Sie angeben.

Da das Verhalten der E-Mail-Clients variiert, sollte nicht auf das `target`-Attribut vertraut werden, um zu steuern, wie Links geöffnet werden. Details dazu, welche E-Mail-Clients das `target`-Attribut unterstützen, finden Sie auf [caniemail.com](https://www.caniemail.com/features/html-target/).

### Warum wird ein Pluszeichen `+` in meinem E-Mail-Link in ein Leerzeichen umgewandelt? {#why-does-a-plus-sign-in-my-email-link-turn-into-a-space}

Einige Query-Parser behandeln ein nicht codiertes Pluszeichen `+` als Leerzeichen. Wenn Ihre Ziel-URL ein Pluszeichen in einem Query-Parameter benötigt, codieren Sie es als `%2B`, bevor Sie den Link zu Ihrer E-Mail hinzufügen.

### Warum werden meine Nutzer:innen automatisch durch E-Mail-Sicherheitssoftware abgemeldet? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Einige E-Mail-Sicherheitstools für Unternehmen (wie Barracuda, Proofpoint und ähnliche Dienste) laden vorab alle URLs in eingehenden E-Mails, einschließlich Abmeldelinks, oder scannen sie. Dies kann unbeabsichtigte Abmeldungen verursachen, wenn das Sicherheitstool dem One-Click-List-Unsubscribe-Link folgt.

Um dies zu mildern:

- **Empfehlen Sie Empfänger:innen, Ihre Versanddomain auf die Allowlist zu setzen:** Arbeiten Sie mit den IT-Teams der betroffenen Empfänger:innen zusammen, um Ihre Versanddomain und die Braze-Tracking-Domains zu deren E-Mail-Sicherheits-Allowlist hinzuzufügen.
- **Verwenden Sie ein Preference-Center:** Verwenden Sie anstelle eines direkten Abmeldelinks ein [Preference-Center]({{site.baseurl}}/user_guide/channels/email/subscriptions), das eine Nutzerinteraktion zur Bestätigung der Abmeldeaktion erfordert. Sicherheitsscanner füllen in der Regel keine mehrstufigen Formulare aus.
- **Überprüfen Sie die Abmeldeprotokolle:** Überprüfen Sie den `User-Agent`-Header und die IP-Adresse in Ihren Currents-Abmeldeereignisdaten, um Muster zu identifizieren, die mit automatisiertem Scanning übereinstimmen (wie konsistente `User-Agent`-Header über mehrere Abmeldungen hinweg).

Weitere Details dazu, wie serverseitiges Scanning E-Mail-Metriken beeinflussen kann, finden Sie unter [Umgang mit erhöhten Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting).

### Warum hat sich meine Machine-Open-Rate unerwartet verändert? {#why-has-my-machine-open-rate-changed-unexpectedly}

[Machine Opens]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) werden durch E-Mail-Sicherheitsfunktionen wie Apple Mail Privacy Protection (MPP) ausgelöst, die E-Mail-Inhalte (einschließlich des Tracking-Pixels) vorab laden, ohne dass der:die Nutzer:in die E-Mail physisch öffnet. Machine-Open-Raten können schwanken basierend auf:

- Änderungen im Anteil Ihrer Zielgruppe, die Apple Mail oder andere datenschutzaktivierte E-Mail-Clients verwenden.
- Updates der Datenschutzfunktionen von E-Mail-Anbietern oder Änderungen im Bot-Erkennungsverhalten.
- Änderungen in Ihrer Zielgruppensegmentierung oder im Targeting.

Machine-Open-Prozentsätze sind kein verlässliches Maß für tatsächliches Engagement. Für eine genauere Ansicht der E-Mail-Performance konzentrieren Sie sich auf *Sonstige Öffnungen* (Nicht-Machine-Öffnungen) und *Eindeutige Klicks*. Sie können diese Metriken auch im Zeitverlauf mit dem [E-Mail-Performance-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance) vergleichen.

### Warum funktionieren meine Deeplinks in Gmail nicht? {#why-are-my-deep-links-not-working-in-gmail}

Gmail entfernt alle Nicht-HTTP/HTTPS-Links aus E-Mail-Nachrichten. Wenn Ihr Deeplink ein benutzerdefiniertes Schema verwendet (wie `myapp://path/to/content`), wird Gmail es entfernen, und der Link funktioniert nicht für Empfänger:innen, die die E-Mail in Gmail lesen. Dies ist eine Gmail-Einschränkung, keine Braze-Einschränkung.

Um dies zu umgehen:

- **Verwenden Sie Universal Links (iOS) oder App Links (Android).** Diese verwenden Standard-`https://`-URLs, die Ihre App öffnen, wenn sie installiert ist, und ansonsten auf eine Webseite zurückfallen. Anweisungen zur Einrichtung finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).
- **Verwenden Sie einen Deeplinking-Anbieter.** Dienste wie [Branch](https://www.branch.io/) generieren HTTP-formatierte Deeplinks, die mit E-Mail-Clients kompatibel sind, einschließlich Gmail.
- **Richten Sie einen Redirect-Endpunkt ein.** Hosten Sie einen `https://`-Endpunkt auf Ihrem Server, der zur URL mit dem benutzerdefinierten Schema Ihrer App weiterleitet. E-Mail-Clients erhalten den `https://`-Link, und die Weiterleitung kümmert sich um das Öffnen der App.

### Enthält die Metrik *Eindeutige Öffnungen* die *Machine Opens*? {#does-the-unique-opens-metric-include-machine-opens}

Ja. *Eindeutige Öffnungen* enthalten *Machine Opens*. Sie können beide Metriken in der Ansicht **Campaign Analytics** und im **Berichts-Builder** einsehen.

Informationen darüber, wie dies die **Conversion-Dashboard**-Attribution beeinflusst, finden Sie unter [Warum stimmen die E-Mail-Öffnungssummen nicht mit den Campaign Analytics überein?]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#why-dont-email-open-totals-match-campaign-analytics) in der [Fehlerbehebung]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#troubleshooting) auf der Seite des Conversion-Dashboards.

### Warum stimmt mein E-Mail-Zustellvolumen nicht mit meinem Versandvolumen überein? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Nachdem eine E-Mail gesendet wurde, entscheidet der Posteingang des:der Empfänger:in, wann sie zugestellt wird. Nachrichten können aufgrund eines vollen Postfachs, ESP-Drosselung von einer bestimmten IP und ähnlicher Gründe für Stunden oder Tage zurückgestellt werden.

Wenn zurückgestellte Nachrichten an einem anderen Kalendertag als dem Sendetag zugestellt werden, können _Zustellungen_ die _Versendungen_ für denselben Datumsbereich überschreiten. Wenn viele Zurückstellungen an einem Tag landen, können _Versendungen_ die _Zustellungen_ für diesen Bereich überschreiten.

### Warum sehe ich eine Warnung, einen Abmeldelink einzufügen, obwohl meine E-Mail bereits einen enthält? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Diese Warnung kann bei Campaigns bestehen bleiben, die von einer Campaign dupliziert wurden, die keinen Abmeldelink hatte. Um sie zu beheben:

- Gehen Sie bei HTML-E-Mails zum Tab **Klartext** und wählen Sie dann **Aus HTML neu generieren**.
- Duplizieren Sie nach dem Duplizieren die Variante und entfernen Sie dann die ursprüngliche Variante. Wählen Sie **nicht** die ursprüngliche Variante aus, da die Warnung sonst übernommen werden kann.

### Warum hat ein:e Nutzer:in eine E-Mail erhalten, die er:sie nicht hätte erhalten sollen? {#why-did-a-user-receive-an-email-they-shouldnt-have}

Die Zustellung kann falsch aussehen, obwohl Braze wie konfiguriert funktioniert hat. Prüfen Sie Folgendes:

- **Doppelte Profile**, die einen Posteingang teilen (siehe [Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Seed-Listen, Testempfänger:innen oder interne Adressen**, die in der Zielgruppe oder als CC/BCC beim Versand enthalten sind.
- **Segment- oder Canvas-Timing:** Der:die Nutzer:in entsprach der Zielgruppe oder dem Canvas-Schritt, als Braze die Berechtigung evaluierte, und dann änderten sich Attribute oder der Abo-Status, bevor er:sie die Nachricht gelesen hat.
- **Abo-Gruppen:** Der:die Nutzer:in blieb in einer Gruppe, auf die Ihre Nachricht abzielte, angemeldet, selbst wenn sein:ihr globaler Abo-Status etwas anderes nahelegte.
- **API- oder Dateiimporte**, die den:die Nutzer:in nach der Segmentierung, aber bevor Sie die Änderung erwartet haben, aktualisiert haben.

Überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), die Changelogs der Campaign oder des Canvas und die Segmentdefinition. Wenn Sie den Versand immer noch nicht nachvollziehen können, kontaktieren Sie den Braze-Support mit Nutzerkennungen, `dispatch_id` (falls verfügbar) und Zeitstempeln.

### Warum hat ein:e Nutzer:in meine E-Mail-Nachricht nicht erhalten? {#why-hasnt-a-user-received-my-email-message}

Es gibt mehrere Gründe, warum ein:e Nutzer:in eine E-Mail, die Sie erwartet haben, nicht erhält, darunter:

- Er:sie war nicht berechtigt, die E-Mail zu erhalten.
- Die E-Mail-Adresse ist ungültig oder existiert nicht.
- Er:sie hat die Nachricht möglicherweise verpasst oder gelöscht.
- Die Nachricht befindet sich möglicherweise in seinem:ihrem Spam-Ordner.

{% alert tip %}
Ein Zustellungsereignis in Braze bedeutet, dass die E-Mail vom Server des Postfachanbieters akzeptiert wurde. Dies garantiert jedoch nicht, dass die Nachricht im Posteingang des:der Nutzer:in erscheint. Der Postfachanbieter kann die Nachricht in den Spam-Ordner leiten oder in seltenen Fällen die Anzeige der Nachricht stillschweigend verhindern.
{% endalert %}

Verwenden Sie die folgenden Tabellen, um die Ursache einzugrenzen.

#### Die E-Mail wurde nicht gesendet {#the-email-wasnt-sent}

| Mögliche Ursache | Was zu überprüfen ist |
|---|---|
| Der:die Nutzer:in war nicht für die Campaign oder das Canvas berechtigt | Überprüfen Sie die **Zielgruppen** (für Campaigns) oder die **Zielgruppe** (für Canvas) [Einstellungen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), um zu bestätigen, dass der:die Nutzer:in zum Zeitpunkt des Versands alle Zielgruppenfilter, Segmentkriterien und Zustellregeln erfüllte. |
| Die Nachricht wurde abgebrochen | Überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Abbruchgründe, wie Liquid-Fehler oder fehlende Pflichtfelder. |
| Die E-Mail-Adresse des:der Nutzer:in war ungültig oder fehlte | Überprüfen Sie unter **Nutzersuche** das Profil des:der Nutzer:in, um sicherzustellen, dass zum Zeitpunkt des Versands eine gültige E-Mail-Adresse hinterlegt war. |
| Die E-Mail-Adresse des:der Nutzer:in hatte zuvor einen Hard Bounce | Ein Hard Bounce markiert die E-Mail-Adresse als ungültig und verhindert zukünftige Versendungen an diese Adresse. Ebenso sendet Braze nur Transaktions-E-Mails an diese:n Nutzer:in, wenn ein:e Empfänger:in Ihre E-Mail als Spam markiert, keine Standard-Campaigns. Überprüfen Sie den **Engagement**-Tab im Profil des:der Nutzer:in. Weitere Informationen finden Sie unter [Abgemeldete E-Mail-Adressen]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) und [Bounces und ungültige E-Mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| Der:die Nutzer:in hat sich von E-Mails abgemeldet | Überprüfen Sie den Abo-Status des:der Nutzer:in unter **Kontakteinstellungen** auf dem **Engagement**-Tab. Braze sendet keine E-Mails an Nutzer:innen, die sich abgemeldet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ursache für nicht gesendete E-Mail" }

#### Die E-Mail wurde gesendet, ist aber nicht im Posteingang angekommen {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| Mögliche Ursache | Was zu überprüfen ist |
|---|---|
| Der Postfachanbieter (MBP) war nicht erreichbar | Ein vorübergehendes Problem verhinderte, dass die E-Mail den MBP des:der Empfänger:in erreichte. Dies löst sich normalerweise von selbst mit Wiederholungsversuchen. E-Mail-Anbieter versuchen Soft Bounces bis zu 72 Stunden lang erneut zuzustellen. |
| Der MBP hat die E-Mail abgewiesen | Der Mailserver des:der Empfänger:in hat die E-Mail abgelehnt. Überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Bounce-Details. |
| Der MBP hat die E-Mail stillschweigend verworfen | Der MBP hat die E-Mail akzeptiert, sie aber dem:der Nutzer:in nicht angezeigt und keinen Bounce zurückgegeben. Dies liegt außerhalb der Kontrolle von Braze und kann in den Braze-Protokollen nicht erkannt werden. |
| Die E-Mail landete im Spam-Ordner | Der MBP hat die Nachricht als Spam identifiziert und in den Spam- oder Junk-Ordner des:der Nutzer:in geleitet. Bitten Sie den:die Nutzer:in, den Spam-Ordner zu überprüfen. |
| Der:die Empfänger:in hat benutzerdefinierte E-Mail-Filter | Der:die Nutzer:in oder sein:ihr IT-Administrator hat möglicherweise Postfachregeln konfiguriert, die eingehende Nachrichten filtern, weiterleiten oder löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ursache für E-Mail nicht im Posteingang" }

### Wie kann ich eine E-Mail-Adresse von der Bounce-Liste entfernen? {#how-can-i-remove-an-email-address-from-the-bounce-list}

Wenn eine gültige E-Mail-Adresse in Braze als ungültig angezeigt wird (normalerweise nach einem Hard Bounce von Ihrem E-Mail-Anbieter), verwenden Sie den Endpunkt [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces). Dadurch wird die Adresse von Ihrer Braze-Bounce-Liste und der Bounce-Liste Ihres E-Mail-Anbieters entfernt. Braze nimmt dann den Versand an diese Adresse wieder auf.

Wenn die Adresse als Spam markiert wurde statt als Hard Bounce, verwenden Sie stattdessen den Endpunkt [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam).

Weitere Informationen finden Sie unter [Bounces und ungültige E-Mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails) und [E-Mail-Adresse von Ihrer Bounce- oder Spam-Liste entfernen]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#remove-an-email-address-from-your-bounce-or-spam-list).

### Wie behebe ich Probleme mit der E-Mail-Zustellbarkeit? {#how-do-i-troubleshoot-email-deliverability-issues}

Wenn Ihre E-Mails verzögert, zurückgestellt oder abgewiesen werden, überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Bounce- und Zurückstellungsdetails und identifizieren Sie dann, wo das Problem in der Zustellkette auftritt. Häufige Zustellbarkeitsprobleme fallen in vier Kategorien:

#### ESP-Rate-Limit-Antworten lesen {#reading-esp-rate-limit-responses}

Ihr E-Mail-Anbieter (ESP), wie Amazon SES, SparkPost oder SendGrid, gibt SMTP-Antwortcodes zurück, wenn er Nachrichten akzeptiert oder zurückstellt. Rate-Limit-Antworten verwenden typischerweise 4xx-Codes, die vorübergehende Fehler anzeigen:

- **421:** Dienst vorübergehend nicht verfügbar, oft aufgrund von hohem Volumen, Verbindungslimits oder Server-Ressourceneinschränkungen. Die Nachricht bleibt in der Warteschlange und Ihr ESP versucht die Zustellung automatisch erneut.
- **429:** API-Rate-Limit überschritten. Sie haben zu viele Anfragen innerhalb des erlaubten Zeitfensters gesendet.
- **450 / 451:** Vorübergehende Zurückstellung aufgrund von Volumen oder Verbindungen. Der Empfängerserver fordert Sie auf, langsamer zu machen.

Wenn Sie diese Codes im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) oder in Ihrem ESP-Dashboard sehen, reduzieren Sie das Sendevolumen an die betroffene Domain und verwenden Sie schrittweise längere Wiederholungsintervalle. Das Fortsetzen des vollen Volumens bei aktivem Rate-Limiting kann vorübergehende Zurückstellungen zu permanenten Ablehnungen eskalieren.

#### Rate-Limits der Postfachanbieter {#mailbox-provider-rate-limits}

Postfachanbieter setzen eigene Rate-Limits für eingehende E-Mails durch, die unabhängig von den Sendekontrollen von Braze sind. Diese Limits können streng sein und liegen außerhalb Ihrer direkten Kontrolle:

- Virgin Media / NTL (Großbritannien): Verwendet stündliches Rate-Limiting, das `421 4.1.1 MXIN503 Hourly ratelimit for your IP exceeded`-Fehler auslöst. Diese Limits können auch Absender mit niedrigem Volumen betreffen. Sie werden auf IP-Ebene über alle Absender durchgesetzt, die diese IP teilen.
- Gmail, Yahoo, iCloud, Microsoft: Jeder Anbieter hat proprietäre Drosselungsschwellenwerte basierend auf Ihrer Absender-Reputation, Ihrem Volumen und Ihren Engagement-Mustern.

Wenn Sie auf anbieterspezifisches Rate-Limiting stoßen, erwägen Sie, Ihre Versendungen über einen längeren Zeitraum zu bündeln oder nach Postfachanbieter zu segmentieren, um das Volumen gleichmäßiger zu verteilen. Überprüfen Sie Ihre Empfängerliste auf Konzentration bei einem Anbieter – wenn die meisten Empfänger:innen eine Domain verwenden, staffeln Sie die Zustellung.

#### E-Mail-Verzögerungen bei Unternehmen durch Antivirenscanning {#corporate-email-delays-from-antivirus-scanning}

Geschäftliche E-Mail-Adressen durchlaufen oft Sicherheits-Gateways des Unternehmens, die Nachrichten vor der Zustellung scannen. Dies kann E-Mails um 15 bis 20 Minuten oder länger verzögern, insbesondere bei Nachrichten mit:

- Großen Anhängen
- Links zu unbekannten Domains
- Inhalten, die Phishing-Mustern ähneln

Diese Verzögerungen treten auf, weil Sicherheitssysteme Nachrichten zur Verhaltensanalyse in isolierten Sandbox-Umgebungen in die Warteschlange stellen. Wenn ein großes E-Mail-Volumen gleichzeitig eintrifft, werden Nachrichten zur Analyse in die Warteschlange gestellt und die Verzögerung verlängert sich. Dies ist normales Verhalten für E-Mail-Sicherheitssysteme in Unternehmen und kann nicht umgangen werden. Berücksichtigen Sie beim Versand zeitkritischer Nachrichten an Unternehmensempfänger:innen dieses Verarbeitungsfenster in Ihrem Kommunikationszeitplan.

#### Fehlerbehebung bei Google-421-4.7.28-Rate-Limit-Fehlern {#troubleshooting-google-421-4728-rate-limit-errors}

Gmail gibt einen `421-4.7.28`-Fehler zurück, wenn es eine ungewöhnliche Rate unerwünschter E-Mails von Ihrer IP-Adresse, Ihrem sendenden IP-Bereich, Ihrer SPF-Domain, DKIM-Domain oder URL-Domain erkennt. Dies ist eine vorübergehende Drosselung, keine permanente Sperre, aber es signalisiert, dass Ihr Sendevolumen, Ihre Geschwindigkeit oder Ihre Reputation den aktuellen Erwartungen von Gmail nicht entspricht.

Wenn Sie diesen Fehler erhalten:

1. Pausieren Sie nicht-essentielle Versendungen sofort für 24 bis 48 Stunden. Das Fortsetzen des Versands während der Drosselung eskaliert das Problem und kann zu permanenten 550-Ablehnungen führen.
2. Bestätigen Sie, dass SPF, DKIM und DMARC korrekt konfiguriert sind und dass Ihr From:-Header mit Ihrer Authentifizierung übereinstimmt.
3. Überprüfen Sie die [Google Postmaster Tools](https://postmaster.google.com/) und das Braze [Deliverability Center]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) (nach der Verbindung mit Google Postmaster) auf den Compliance-Status und die Spam-Beschwerderate Ihrer Domain. Ihre von Nutzer:innen gemeldete Spam-Rate muss unter 0,1 % bleiben (die harte Obergrenze liegt bei 0,3 %).
4. Nehmen Sie nach der Pause den Versand mit 10 bis 20 % des vorherigen Volumens nur an Ihre engagiertesten Empfänger:innen wieder auf. Erhöhen Sie das Volumen langsam über mehrere Wochen, nur wenn keine weiteren 4xx-Fehler auftreten.

Weitere Hinweise finden Sie in den [Google-Richtlinien für Massen-E-Mail-Absender](https://support.google.com/mail/answer/81126).

### Wie kann ich Bilder in Outlook optimieren? {#how-can-i-optimize-images-in-outlook}

Outlook verwendet häufig Microsoft-Word-Rendering anstelle des Standard-Browser-Renderings, was dazu führen kann, dass Bilder falsch gerendert werden oder Rahmen um Bilder hinzugefügt werden. Dieses clientspezifische Rendering beeinflusst auch, [wie Alt-Text angezeigt wird]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) in verschiedenen E-Mail-Clients.

Wenn Bilder in Outlook breiter als erwartet angezeigt werden, fügen Sie dem Bild folgendes CSS hinzu:

```css
max-width: 100%;
```

Zum Beispiel:

```html
<img src="your-image.png" style="max-width: 100%;" alt="Description">
```

Sie können Inhalte auch so umschließen, dass sie in Outlook Desktop mit bedingten Kommentaren ausgeblendet werden:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Kann ich SVG- oder WebP-Bilder in meinen E-Mail-Nachrichten verwenden? {#can-i-use-svg-or-webp-images-in-my-email-messages}

SVG-Bilder werden für E-Mails aufgrund der eingeschränkten Unterstützung in verschiedenen E-Mail-Clients nicht empfohlen. Gmail und mehrere andere große E-Mail-Anbieter rendern SVG-Bilder nicht, was zu fehlerhaften oder fehlenden Bildern bei Empfänger:innen führen kann. WebP wird ebenfalls nicht einheitlich über alle Clients hinweg unterstützt.

Verwenden Sie stattdessen weit verbreitete Formate wie PNG oder JPEG, damit Bilder zuverlässig gerendert werden.

### Kann ich Videos in E-Mails einbetten? {#can-i-embed-videos-in-emails}

Eingebettete Videos werden von vielen gängigen E-Mail-Clients wie Gmail, Outlook und Yahoo nicht nativ unterstützt. Infolgedessen werden eingebettete Videoelemente möglicherweise nicht wie beabsichtigt angezeigt oder erscheinen überhaupt nicht. Darüber hinaus kann das direkte Einbetten von Videos in eine E-Mail die E-Mail-Größe erheblich erhöhen, was die Wahrscheinlichkeit steigert, dass die Nachricht als Spam markiert wird.

Stattdessen können Sie ein GIF oder ein Standbild erstellen, das einem Video in einem Videoplayer ähnelt, und dieses Bild dann mit Ihrem Video verlinken. Wenn Nutzer:innen auf das Bild klicken, werden sie zum Video weitergeleitet, das auf Ihrer Website oder einer Videoplattform gehostet wird. Braze unterstützt auch die Integration mit [Playable]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/playable), das optimierte Videoinhalte bietet, die in unterstützten E-Mail-Clients automatisch abgespielt werden.

### Können Liquid-Variablen, die in einem Teil des Nachrichten-Editors zugewiesen werden, in einem anderen verwendet werden? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

Nein. Jeder Teil der E-Mail (Betreff, Body, Header, Buttons usw.) wird separat generiert, sodass Liquid, das in einem Feld zugewiesen wird, in einem anderen nicht verfügbar ist. Weisen Sie Variablen in jedem Feld zu, das sie benötigt.

### Mein E-Mail-Template fehlt. Wo ist es? {#my-email-template-is-missing-where-is-it}

Bestätigen Sie zunächst, dass Sie die [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) zum Anzeigen von Templates haben. Um gespeicherte E-Mail-Templates anzuzeigen, gehen Sie zu **Inhalte** > **E-Mail**. Sie können Templates nach Status und Typ (HTML oder Drag-and-Drop) filtern.

### Muss ich Domains für Relay- oder maskierte E-Mails registrieren? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

[Apples Private Email Relay]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) erfordert, dass Sie Ihre Versanddomains im Apple Developer Portal registrieren, um Bounces zu verhindern. Google Shielded Email erfordert keinen manuellen Domain-Registrierungs- oder Allowlisting-Prozess.


### Kann ich Hyperlinks in E-Mail-Betreffzeilen oder Preheadern hinzufügen? {#can-i-add-hyperlinks-in-email-subject-lines-or-preheaders}

Nein. Das Hinzufügen von Hyperlinks in E-Mail-Betreffzeilen wird von Postfachanbietern nicht unterstützt. Einige Postfachanbieter scannen Betreffzeilen automatisch und konvertieren physische Adressen, Daten oder Uhrzeiten in klickbare Links, aber dies geschieht automatisch auf dem Gerät des:der Empfänger:in und liegt außerhalb der Kontrolle von Braze (oder eines anderen ESP).

Ebenso wird das Hinzufügen von Hyperlinks im Preheader branchenweit nicht unterstützt.

Wenn Sie eine Funktionalität benötigen, die klickbaren Inhalten in der Betreffzeile oder im Preheader-Bereich ähnelt, erwägen Sie die Verwendung von [Gmail Promotions]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab), um interaktive Annotationen zu Ihren E-Mails für Gmail-Nutzer:innen hinzuzufügen.

### Was bedeutet der Bounce-Grund `unable to get mx info` oder `failed to get IPs from PTR record`? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

Im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) weist ein Bounce-Grund, der dem Folgenden ähnelt, auf ein Problem bei der Auflösung der E-Mail-Konfiguration der empfangenden Domain hin (die Domain nach dem `@` in der Adresse), nicht auf die Braze-Nachrichtenzusammenstellung:

Typische Ursachen sind:

- Fehlende, falsche oder nicht erreichbare **MX-Einträge** für diese Domain
- Hostnamen für eingehende E-Mails, die nicht auflösen oder die **PTR-(Reverse-DNS)**-Prüfungen nicht bestehen, die von der empfangenden Infrastruktur erwartet werden
- Ungültige oder falsch geschriebene Domains in der E-Mail-Adresse

**Nächste Schritte:**

- Bestätigen Sie die Schreibweise der Adresse und Domain.
- Wenn die Adresse korrekt ist, kontaktieren Sie den:die Postfachinhaber:in oder das IT-Team dieser Domain.
- Bitten Sie sie, MX- und zugehörige DNS-Einträge, einschließlich PTR-Einträge für ihre Mailserver, bei ihrem DNS-Anbieter zu überprüfen.

Andere Empfänger:innen sind in der Regel nicht betroffen. Informationen darüber, wie Soft Bounces im Reporting erscheinen, finden Sie unter [Soft Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Warum erhalte ich eine Spam-Warnung, wenn ich eine E-Mail von Braze an mich selbst sende? {#why-do-i-get-a-spam-alert-when-sending-an-email-from-braze-to-myself}

Wenn Sie eine Test-E-Mail von Braze an Ihre eigene E-Mail-Adresse senden und eine Spam-Warnung oder Phishing-Warnung sehen – wie z. B. „Die Versanddomain ähnelt der Domain Ihres Unternehmens, aber wir erkennen sie nicht“ –, handelt es sich um eine gängige Anti-Phishing-Sicherheitsfunktion, nicht um einen Fehler in Ihrer Braze-Konfiguration.

Diese Warnung erscheint typischerweise, wenn die Versanddomain der E-Mail mit der Empfängerdomain übereinstimmt (z. B. beide `@ihrunternehmen.com`). E-Mail-Sicherheitssysteme markieren dies, weil Betrüger:innen oft Domains fälschen, die der Unternehmensdomain eines:einer Empfänger:in ähneln.

Um zu überprüfen, ob Ihre E-Mail korrekt konfiguriert ist:

1. Zeigen Sie die Originalnachricht (rohe E-Mail-Header) in Ihrem E-Mail-Client an.
2. Überprüfen Sie, dass SPF-, DKIM- und DMARC-Authentifizierung alle bestehen.
3. Wenn alle drei bestehen, ist Ihr Braze-E-Mail-Versand korrekt konfiguriert.

Um zu verhindern, dass diese Warnung erscheint:

Bitten Sie Ihr IT-Team, Ihre Braze-Versanddomain und IP-Adressen in den E-Mail-Sicherheitsdiensten oder dem Mail-Gateway Ihres Unternehmens auf die Allowlist zu setzen. Dies teilt Ihrem Sicherheitssystem mit, E-Mails von Ihrer Braze-Versandinfrastruktur zu vertrauen.