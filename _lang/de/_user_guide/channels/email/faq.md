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

Wenn sich mehrere Nutzer:innen mit übereinstimmenden E-Mail-Adressen in einem Segment befinden, das eine Campaign erhalten soll, wird zum Sendezeitpunkt ein einzelnes Nutzerprofil mit dieser E-Mail-Adresse ausgewählt. Auf diese Weise wird die E-Mail nur einmal gesendet und dedupliziert, sodass sie nicht mehrfach an dieselbe E-Mail-Adresse zugestellt wird.

**Eindeutige E-Mail-Adressen:** Braze erzwingt keine eindeutigen E-Mail-Adressen über Profile hinweg. Wenn Sie auf eine Eins-zu-eins-Beziehung zwischen einer E-Mail-Adresse und einem Profil angewiesen sind, überwachen Sie intern beim Erstellen von Nutzer:innen auf Duplikate.

**Deduplizierung vor Liquid:** Bei Sendungen, bei denen Braze innerhalb eines Versands nach E-Mail-Adresse dedupliziert (zum Beispiel bei geplanten Campaigns, bei denen mehrere Segmentmitglieder mit derselben Adresse zusammen verarbeitet werden), erfolgt diese Deduplizierung, bevor Liquid für das ausgewählte Profil ausgeführt wird, das diese Adresse repräsentiert. Wenn Liquid für dieses Profil abbricht (zum Beispiel mit [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), erhält diese Adresse bei diesem Versand keine Nachricht – einschließlich der Profile, die bereits durch die Deduplizierung übersprungen wurden. Getriggerte Sendungen wenden diese Adress-Deduplizierung innerhalb eines Versands nicht an; mehrere Profile, die eine Adresse teilen, können alle in einem Batch berechtigt bleiben, sodass dieses Abbruchverhalten nicht auf die gleiche Weise gilt (siehe nächster Absatz).

Wenn mehrere Profile eine E-Mail-Adresse teilen und ein Profil sich abmeldet, aktualisiert Braze andere Profile (bis zu 100) mit dieser Adresse auf denselben Abo-Status. Dies gilt für Abmeldungen und andere Änderungen wie den globalen Abo-Status und individuelle Abo-Gruppenstatusänderungen.

**Seed-Gruppen:** Bei Campaigns mit [Seed-Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) wählt Braze ein Profil für die primäre Zustellung aus, wenn mehrere Profile eine Adresse teilen. Diese:r primäre Empfänger:in ist möglicherweise nicht in Ihrer Seed-Gruppe, selbst wenn ein anderes Profil mit derselben Adresse darin enthalten ist.

Die folgenden Szenarien können den Eindruck erwecken, dass ein:e Nutzer:in eine E-Mail zweimal erhalten hat:

- **Seed-Listen oder Testempfänger:innen:** Seed-Adressen und interne Testempfänger:innen können eine Sendung zusätzlich zu Ihrer Hauptzielgruppe erhalten, was wie ein Duplikat aussehen kann, wenn ein Posteingang sowohl einem Profil als auch einem Seed-Eintrag entspricht.
- **Ein Fehler ist bei der Erstellung der Campaign oder des Canvas aufgetreten:** Die Nutzer:innen erhalten möglicherweise nicht dieselbe Sendung zweimal, können aber zwei separate E-Mails mit derselben Betreffzeile erhalten. Wenn eine Campaign oder ein Canvas dupliziert wird, überprüfen Sie die E-Mail-Konfigurationsdetails wie Bilder oder Betreffzeilen. Sie können auch die Changelogs einsehen, um festzustellen, ob die Campaign oder das Canvas nach dem Start geändert wurde – ein Duplikat kann dieselbe Betreffzeile wie das Original haben, als die Nutzer:innen es erhalten haben.
- **Mehrere Nutzerprofile haben E-Mail-Weiterleitung:** Wenn ein:e Nutzer:in mehrere Konten in einer bestimmten App hat, aber ein Konto E-Mails weiterleitet, erhält die Person die Campaign einmal pro Posteingang; E-Mails können im Posteingang, in den Nachrichten weitergeleitet werden, doppelt erscheinen. Nur einige Anbieter zeigen an, wenn eine E-Mail von einem anderen Konto weitergeleitet wurde.
- **E-Mail-Konfiguration beim Empfänger:** Einige Clients führen Posteingänge zusammen („universeller Posteingang“). Wenn dieselbe Campaign mehrere Konten anspricht, die einen Posteingang teilen, kann es so aussehen, als hätte eine Person die Campaign zweimal erhalten, obwohl tatsächlich zwei verschiedene Profile angeschrieben wurden. Die empfangende Person kann bestätigen, ob mehrere Konten in einem Posteingang zusammengeführt sind.

Diese Deduplizierung gilt, wenn die angesprochenen Nutzer:innen im selben Versand sind. Die erneute Berechtigung wird pro Profil bewertet, nicht pro E-Mail-Adresse.

Die erneute Berechtigung für E-Mail-Campaigns und Canvas-Schritte verwendet das Profil jeder Nutzerin und jedes Nutzers – nicht den Posteingang – sodass mehrere Profile für separate Sendungen qualifiziert sein können, während diese Logik erfüllt ist. In Kombination mit Triggern kann dies mehr als eine Nachricht an denselben Posteingang zustellen, selbst wenn Sie versuchen, eine einzelne Sperrfrist auf Adressebene einzuhalten. Getriggerte Campaigns (ausgenommen API-getriggerte Campaigns) und Canvases können ebenfalls zweimal an eine Adresse senden, wenn verschiedene Profile mit übereinstimmenden E-Mail-Adressen den Trigger zu unterschiedlichen Zeiten auslösen – zum Beispiel wenn Nutzer:in A und Nutzer:in B `johndoe@example.com` teilen, sich aber in verschiedenen Zeitzonen befinden, während die Zustellung Ortszeitzonen verwendet.

Nutzer:innen werden beim Canvas-Eintritt nicht nach E-Mail dedupliziert, sodass sie über den ersten Schritt eines Canvas hinaus möglicherweise nicht dedupliziert werden, wenn sie aufgrund von Rate-limitiertem Eintritt zu leicht unterschiedlichen Zeiten fortschreiten. Wenn ein:e Nutzer:in, die/der einer bestimmten E-Mail-Adresse zugeordnet ist, eine E-Mail öffnet oder darauf klickt, werden alle Nutzerprofile, die diese E-Mail-Adresse teilen, als geöffnet oder geklickt markiert.

### Ausnahme: API-getriggerte Campaigns {#exception-api-triggered-campaigns}

API-getriggerte Campaigns deduplizieren oder senden Duplikate, je nachdem, wo die Zielgruppe definiert ist. Doppelte E-Mails müssen im API-Aufruf separat mit unterschiedlichen `user_ids` angesprochen werden, um mehrere Zustellungen zu erhalten. Hier sind drei mögliche Szenarien für API-getriggerte Campaigns:

- **Szenario 1: Doppelte E-Mails im Zielsegment:** Wenn dieselbe E-Mail in mehreren Nutzerprofilen erscheint, die in den Zielgruppenfiltern des Dashboards für eine API-getriggerte Campaign gruppiert sind, erhält nur eines der Profile die E-Mail.
- **Szenario 2: Doppelte E-Mails in verschiedenen `user_ids` innerhalb des Empfängerobjekts:** Wenn dieselbe E-Mail in mehreren `external_user_id`-Werten erscheint, die vom `recipients`-Objekt referenziert werden, wird die E-Mail zweimal gesendet.
- **Szenario 3: Doppelte E-Mails aufgrund doppelter `user_ids` innerhalb des Empfängerobjekts:** Wenn Sie versuchen, dasselbe Nutzerprofil zweimal hinzuzufügen, erhält nur eines der Profile die E-Mail.

{% alert important %}
Wenn Sie eine API-Campaign über einen API-Aufruf senden (ausgenommen API-getriggerte Campaigns) und mehrere Nutzer:innen in der Segmentzielgruppe mit derselben E-Mail-Adresse angegeben sind, wird an diese Adresse so oft gesendet, wie sie im Aufruf aufgeführt ist. Dies liegt daran, dass API-Aufrufe als absichtlich konstruiert angenommen werden.
{% endalert %}

#### A/B-Tests mit doppelten E-Mail-Adressen {#ab-testing-with-duplicate-email-addresses}

Vermeiden Sie [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing) bei E-Mails, wenn mehrere Profile dieselbe E-Mail-Adresse teilen können. Varianten werden pro Profil zugewiesen, was zu mehr als einer Nachricht an denselben Posteingang führen kann. Wenn Sie in dieser Situation testen müssen, kombinieren Sie keinen **Gewinnervariante**-Schritt mit [Ortszeit-Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) auf eine Weise, die die Auswahl der Gewinnervariante verzögert – diese Optionen zusammen können die Wahrscheinlichkeit doppelter Sendungen erhöhen.

#### Canvas und doppelte E-Mail-Adressen {#canvas-and-duplicate-email-addresses}

Bei Canvas-Journeys kann es von Entry-Batching, Schritt-Timing und anderen Faktoren abhängen, ob doppelte E-Mail-Adressen eine Sendung oder mehr als eine erhalten. Betrachten Sie das Verhalten als undefiniert, bis Sie es für Ihre Journey validiert haben. Führen Sie nach Möglichkeit doppelte Profile zusammen oder konsolidieren Sie sie. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="deterministic deduplication for duplicate email addresses in Canvas" %}

### Was passiert mit dem Abo-Status, wenn die E-Mail-Adresse einer Nutzerin oder eines Nutzers auf eine geändert wird, die von einer anderen Person geteilt wird? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Wenn Sie die E-Mail-Adresse von Nutzer:in A auf eine andere E-Mail-Adresse setzen oder aktualisieren, die von einer bestehenden Nutzer:in B geteilt wird, übernimmt Nutzer:in A den Abo-Status, der bereits von Nutzer:in B existiert, es sei denn, die Einstellung **Nutzer:innen bei Aktualisierung ihrer E-Mail erneut abonnieren** ist aktiviert.

### Werden Aktualisierungen meiner ausgehenden E-Mail-Einstellungen rückwirkend angewendet? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

Nein. Aktualisierungen der ausgehenden E-Mail-Einstellungen wirken sich nicht rückwirkend auf bestehende Sendungen aus. Wenn Sie beispielsweise Ihren Standard-Anzeigenamen in den E-Mail-Einstellungen ändern, wird der bestehende Standard-Anzeigename in Ihren aktiven Campaigns oder Canvases nicht automatisch ersetzt.

### Was ist eine „gute“ E-Mail-Zustellrate? {#what-is-a-good-email-delivery-rate}

Typischerweise liegt die „magische Zahl“ bei etwa 98 % zugestellter Nachrichten mit einer Bounce-Rate von nicht mehr als 3 %. Wenn weniger als 98 % der Nachrichten zugestellt werden, gibt es in der Regel Anlass zur Sorge.

Allerdings kann eine Zustellrate von 98 % oder höher dennoch Zustellbarkeitsprobleme aufweisen. Wenn beispielsweise alle Ihre Bounces von einer einzigen Domain stammen, ist das ein klares Signal für ein Reputationsproblem bei diesem Anbieter.

Darüber hinaus können Nachrichten zugestellt werden und im Spam-Ordner landen, was auf potenziell schwerwiegende Reputationsprobleme hinweist. Es ist wichtig, nicht nur die Anzahl der zugestellten Nachrichten zu überwachen, sondern auch die Öffnungs- und Klickraten, um festzustellen, ob die Nutzer:innen die Nachrichten tatsächlich in ihren Posteingängen sehen. Da Anbieter in der Regel nicht jede Spam-Instanz melden, könnte eine Spam-Rate von nur 1 % Anlass zur Sorge und weiteren Analyse sein.

Schließlich können auch Ihr Geschäft und die Art der E-Mails, die Sie senden, die Zustellung beeinflussen. Zum Beispiel sollte jemand, der hauptsächlich [Transaktions-E-Mails]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) sendet, eine bessere Rate erwarten als jemand, der viele Marketing-Nachrichten versendet.

### Warum ergeben meine E-Mail-Zustellmetriken nicht 100 %? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

E-Mail-Zustellmetriken (Zustellungen, Bounces und Spam-Rate) ergeben möglicherweise nicht 100 %, da E-Mails, die einen Soft Bounce erhalten und nach der Wiederholungsperiode von bis zu 72 Stunden nicht zugestellt werden, nicht berücksichtigt werden.

Soft Bounces sind E-Mails, die aufgrund eines temporären oder vorübergehenden Problems zurückgewiesen werden, wie „Postfach voll“, „Server vorübergehend nicht verfügbar“ und mehr. Wenn eine E-Mail mit Soft Bounce nach 72 Stunden immer noch nicht zugestellt wird, wird diese E-Mail nicht in den Zustellmetriken der Campaign berücksichtigt.

### Was ist eine E-Mail-Feedback-Schleife? {#what-is-an-email-feedback-loop}

Eine E-Mail-Feedback-Schleife (FBL) ermöglicht es Absendern, ihre Reputation zu überwachen, indem Campaigns identifiziert werden, die ein hohes Beschwerdeaufkommen erhalten. Schritte zur Implementierung einer Gmail-Feedback-Schleife finden Sie im Artikel [Google's Feedback Loop](https://support.google.com/a/answer/6254652).

### Was sind Open-Tracking-Pixel? {#what-are-open-tracking-pixels}

[Open-Tracking-Pixel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) nutzen die Klick-Tracking-Domain des Absenders, um E-Mail-Öffnungsereignisse zu verfolgen. Das Pixel ist ein Bild-Tag, das an das HTML der E-Mail angehängt wird. Es ist am häufigsten das letzte HTML-Element innerhalb des Body-Tags. Wenn ein:e Nutzer:in die E-Mail lädt, wird eine Anfrage gestellt, um das Bild von der gebrandeten Tracking-Domain zu laden, was ein Öffnungsereignis protokolliert.

### Kann ich Öffnungen für E-Mails verfolgen, die im Nur-Text-Format gerendert werden? {#can-i-track-opens-for-emails-rendered-in-plain-text}

Nein. Braze verfolgt E-Mail-Öffnungen mithilfe eines [Open-Tracking-Pixels]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#open-tracking-pixel), das in das HTML der E-Mail eingebettet ist. Wenn der E-Mail-Client der empfangenden Person die E-Mail lädt, fordert er dieses Bild an, und Braze protokolliert ein Öffnungsereignis.

Da Nur-Text-E-Mails keine Bilder enthalten können, ist das Open-Tracking-Pixel nicht enthalten, sodass Öffnungen für E-Mails im Nur-Text-Format nicht verfolgt werden können. Klicks können weiterhin verfolgt werden, da Hyperlinks im Nur-Text-Format funktionsfähig bleiben.

Dies ist erwartetes Verhalten. Für die Genauigkeit der Öffnungsrate gestalten Sie E-Mails als HTML und beachten Sie, dass Öffnungen nicht gezählt werden, wenn Empfänger:innen die Nur-Text-Version anzeigen.

### Wie funktioniert das E-Mail-Tracking, wenn Empfänger:innen E-Mails weiterleiten? {#how-does-email-tracking-work-when-recipients-forward-emails}

Wenn ein:e Empfänger:in eine E-Mail weiterleitet, enthält die weitergeleitete E-Mail dasselbe Open-Tracking-Pixel und dieselben Klick-Tracking-Links wie das Original. Das bedeutet:

- Wenn jemand, der nicht in Ihrer ursprünglichen Campaign-Zielgruppe war, eine weitergeleitete E-Mail erhält und sie öffnet, protokolliert Braze ein Öffnungsereignis.
- Wenn diese Person auf einen Link in der weitergeleiteten E-Mail klickt, protokolliert Braze ein Klickereignis.
- Diese Ereignisse werden dem Profil der/des ursprünglichen Empfänger:in zugeordnet, nicht der Person, die die weitergeleitete E-Mail erhalten hat, da das Tracking-Pixel und die Links an die/den ursprüngliche:n Empfänger:in gebunden sind.

Braze kann nicht zwischen Öffnungen und Klicks der/des ursprünglichen Empfänger:in und denen von Personen unterscheiden, die eine weitergeleitete Kopie erhalten haben. Dies ist Standardverhalten für E-Mail-Tracking-Pixel und betrifft alle E-Mail-Anbieter.

Beachten Sie bei der Analyse von E-Mail-Metriken, dass Weiterleitungsaktivitäten zu Öffnungs- und Klickzahlen beitragen können. Wenn Sie ungewöhnlich hohe Engagement-Raten oder wiederholte Aktivitäten desselben Profils über die Zeit bemerken, könnte Weiterleitung ein Faktor sein.

### Was passiert, wenn eine E-Mail-Campaign oder ein Canvas gestoppt wird? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Nutzer:innen werden daran gehindert, in das Canvas einzutreten, und es werden keine weiteren Nachrichten gesendet.

Bei E-Mail-Campaigns und Canvases stoppt der Stopp-Button den Versand nicht sofort. Wenn die Sendeanfragen gesendet wurden, können sie nicht daran gehindert werden, an die Nutzer:innen zugestellt zu werden, was nach einer gewissen Verzögerung geschehen kann.

Obwohl Braze keine weiteren Anfragen sendet, sobald die Campaign oder das Canvas gestoppt wurde, können die Analytics weiterhin steigen, während der ESP bereits laufende Anfragen verarbeitet.

### Warum sehe ich mehr _Gesamtklicks_ als _Gesamtöffnungen_ in meinen E-Mail-Analytics? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

_Gesamtöffnungen_ ist die Anzahl, wie oft die E-Mail von Nutzer:innen geöffnet wurde, während _Gesamtklicks_ die Anzahl ist, wie oft Nutzer:innen innerhalb der zugestellten E-Mail geklickt haben, einschließlich aller Arten von Klicks wie Linkklicks. Sie sehen möglicherweise mehr Klicks als Öffnungen aus einem der folgenden Gründe:

- Nutzer:innen führen mehrere Klicks im E-Mail-Text innerhalb einer einzelnen Öffnung durch.
- Nutzer:innen klicken auf einige E-Mail-Links im Vorschaubereich ihrer Telefone. In diesem Fall protokolliert Braze diese E-Mail als geklickt, aber nicht als geöffnet.
- Nutzer:innen öffnen eine E-Mail erneut, die sie zuvor in der Vorschau angesehen haben.

### Warum sind meine Klickzahlen höher als mein Segment der Nutzer:innen, die geklickt haben? {#why-are-my-click-counts-higher-than-my-segment-of-users-who-clicked}

Campaign-Analytics zeigen die Gesamtzahl der Klickereignisse, während Segments die Anzahl der eindeutigen Nutzer:innen zurückgeben, die diese Klicks durchgeführt haben. Da jede:r Nutzer:in mehrfach klicken kann, ist die Gesamtzahl der Klicks in den Analytics oft höher als die Anzahl der Nutzer:innen, die geklickt haben, wenn Sie ein Segment erstellen.

Zum Beispiel: Wenn 100 Nutzer:innen jeweils 3-mal auf einen Link klicken, zeigen die Campaign-Analytics 300 Gesamtklicks, aber ein Segment, das nach „E-Mail geklickt“ für diese Campaign gefiltert wird, gibt 100 Nutzer:innen zurück.

### Warum sehe ich null E-Mail-Öffnungen und -Klicks? {#why-am-i-seeing-zero-email-opens-and-clicks}

Sie sehen möglicherweise keine E-Mail-Öffnungen oder -Klicks, wenn eine Fehlkonfiguration in Ihrer Tracking-Domain vorliegt. Dies kann auf einen der folgenden Gründe zurückzuführen sein:
- Es gibt ein SSL-Problem, bei dem Tracking-URLs `http` statt `https` verwenden.
- Es gibt ein Problem mit Ihrem CDN, bei dem der User-Agent-String bei den Öffnungsereignissen, Klickereignissen oder beiden nicht befüllt wird.

### Warum sehe ich ungewöhnliches E-Mail-Öffnungs- oder Klickverhalten? {#why-am-i-seeing-unusual-email-open-or-click-behavior}

Wenn Sie unerwartete Muster in Ihren E-Mail-Öffnungs- oder Klickmetriken bemerken – wie ein:e einzelne:r Nutzer:in, die/der scheinbar sofort auf jeden Link klickt, oder Öffnungen, die nicht wie erwartet registriert werden – überprüfen Sie die folgenden häufigen Ursachen:

#### E-Mail-Clipping entfernt das Tracking-Pixel {#email-clipping-removes-the-tracking-pixel}

Wenn eine E-Mail vom E-Mail-Anbieter der empfangenden Person gekürzt wird (z. B. Gmail kürzt Nachrichten über ca. 102 KB), kann Inhalt am Ende der E-Mail abgeschnitten werden. Da das Open-Tracking-Pixel typischerweise am Ende der E-Mail eingefügt wird, kann Clipping das Öffnungs-Tracking verhindern.

**So erkennen Sie es:** Prüfen Sie, ob die E-Mail einen Link „Gesamte Nachricht anzeigen“ oder ähnlich am Ende anzeigt. Sie können [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) verwenden, um die vollständige scrollbare E-Mail in der Vorschau anzuzeigen und zu überprüfen, ob die Nachricht gekürzt wird.

**So beheben Sie es:** Sie können Braze so konfigurieren, dass das Tracking-Pixel oben in der E-Mail statt unten platziert wird. Das Verschieben des Tracking-Pixels kann beeinflussen, wie einige E-Mail-Clients Ihr HTML rendern, daher testen Sie Ihre E-Mails in Inbox Vision nach dieser Änderung. Beachten Sie, dass Öffnungen nicht verfolgt werden können, wenn die empfangende Person Bilder deaktiviert hat, unabhängig von der Pixelplatzierung.

#### Tracking-Pixel verursacht weißen Abstand am oberen Rand der E-Mail {#tracking-pixel-causes-white-gap-at-top-of-email}

Wenn das Open-Tracking-Pixel oben in einer E-Mail positioniert ist, kann eine sichtbare weiße Linie oder Lücke am oberen Rand des E-Mail-Textes erscheinen, insbesondere auf mobilen Geräten.

**So erkennen Sie es:** Gehen Sie in Braze zu **Einstellungen** > **E-Mail-Einstellungen** und wählen Sie den Abschnitt **Open-Tracking-Pixel**. Wenn **Verschieben für SendGrid**, **Verschieben für SparkPost** oder **Verschieben für Amazon SES** für Ihren Sendeanbieter aktiviert ist, wird das Pixel oben in Ihrem E-Mail-HTML positioniert. Wenn Sie eine weiße Lücke oder Linie am oberen Rand Ihrer gerenderten E-Mail bemerken, könnte diese Einstellung die Ursache sein.

**So beheben Sie es:** Deaktivieren Sie den entsprechenden **Verschieben für SendGrid**-, **Verschieben für SparkPost**- oder **Verschieben für Amazon SES**-Schalter im Abschnitt **Open-Tracking-Pixel** für Ihren Sendeanbieter. Das Tracking-Pixel ist am unteren Rand einer E-Mail in der Regel weniger sichtbar. Testen Sie Ihre E-Mails in [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) nach der Änderung der Platzierung. Weitere Informationen finden Sie unter [Platzierung aktualisieren]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement).

#### Verzögerte Statistiken oder Klicks ohne Öffnungen {#delayed-stats-or-clicks-without-opens}

Das Öffnungs-Tracking setzt voraus, dass die empfangende Person die E-Mail mit aktivierten Bildern lädt. In einigen Fällen können Statistiken verzögert erscheinen oder Klicks ohne entsprechende Öffnungen protokolliert werden, weil:

- Die empfangende Person die E-Mail in einem Vorschaubereich anzeigt, ohne sie vollständig zu öffnen, und dann Links direkt aus der Vorschau anklickt.
- Der E-Mail-Client Bilder (und damit das Tracking-Pixel) erst lädt, nachdem die empfangende Person bereits mit Links interagiert hat.

#### Sicherheitssoftware simuliert Linkklicks {#security-software-simulates-link-clicks}

Einige Sicherheitstools für Unternehmens-E-Mails (wie Barracuda, Proofpoint und ähnliche Dienste) scannen eingehende E-Mails, indem sie automatisch alle Links in der Nachricht anklicken, um zu überprüfen, ob sie sicher sind. Dies kann dazu führen, dass Klickereignisse innerhalb von Sekunden nach dem Versand erscheinen, oft mit jedem Link in der E-Mail, der in schneller Folge angeklickt wird.

Dieses Verhalten ist häufiger bei institutionellen E-Mail-Domains (wie Schulen, Universitäten und Unternehmensumgebungen) und tritt eher auf, wenn sich Ihre Sendedomain erheblich von Ihrer Tracking-Domain unterscheidet. Das Einrichten einer [benutzerdefinierten gebrandeten Tracking-Domain]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) kann die Häufigkeit dieser automatisierten Klicks reduzieren.

**So erkennen Sie es:** Suchen Sie die IP-Adresse des Klickereignisses (verfügbar in Currents-Daten) in einer Suchmaschine. Wenn die IP mit einem bekannten Sicherheitsanbieter (wie Barracuda Networks) verknüpft ist, sind die Klicks wahrscheinlich automatisiert. Sie können auch einen konsistenten User-Agent-Header über mehrere automatisierte Klicks hinweg sehen.

Weitere Informationen darüber, wie Sicherheitsscans E-Mail-Metriken beeinflussen, finden Sie unter [Umgang mit steigenden Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting).

### Welche potenziellen Risiken bestehen beim Auslösen von Server-Klicks? {#what-are-the-potential-risks-of-triggering-server-clicks}

Bestimmte Elemente einer E-Mail-Nachricht, wie übermäßig lange Nachrichten oder zu viele Ausrufezeichen, können E-Mail-Sicherheitsreaktionen auslösen. Diese Reaktionen können das Reporting und die IP-Reputation beeinflussen und dazu führen, dass sich Nutzer:innen abmelden.

Best Practices zum Umgang mit diesen Reaktionen finden Sie unter [Umgang mit steigenden Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting).

### Kann Braze Abmeldelinks verfolgen, die zur Metrik „Abmeldungen“ gezählt werden? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze verfolgt Abmeldelinks, wenn das folgende Liquid in E-Mails verwendet wird: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Warum sehe ich eine andere Anzahl von Abmeldungen als Klicks auf meinen Abmeldelink? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

Wenn es mehr _Abmeldungen_ als Nutzer:innen gibt, die auf den Abmeldelink im E-Mail-Text geklickt haben, erklärt [**List-Unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) oft die Differenz. List-Unsubscribe ist ein zusätzlicher Abmeldepfad im E-Mail-Header (nicht der Link in Ihrem Nachrichtentext). Wenn sich ein:e Nutzer:in auf diese Weise abmeldet, zählt es zu den _Abmeldungen_, wird aber nicht als Klick auf die verfolgte Abmelde-URL im Text gezählt.

Wenn die Gesamtzahl der Klicks auf den Abmeldelink im Text größer ist als die Anzahl der _Abmeldungen_, haben Nutzer:innen möglicherweise mehr als einmal auf den Link geklickt – zum Beispiel wenn sie sich abmelden, erneut abonnieren und sich wieder abmelden. Die E-Mail-Analytics können in der Klickaufschlüsselung mehrere Klicks erfassen.

Wenn ein:e Nutzer:in zweimal auf den Abmeldelink klickt (zum Beispiel wenn sie sich abgemeldet, erneut abonniert und dann wieder abgemeldet haben), zählt dies in den E-Mail-Analytics zweimal.

### Kann ich einen „Diese E-Mail im Browser anzeigen“-Link zu meinen E-Mails hinzufügen? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Nein. Braze bietet diese Funktionalität nicht an. Dies liegt daran, dass eine wachsende Mehrheit der E-Mails auf mobilen Geräten und in modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte problemlos rendern.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing-Page (z. B. Ihrer Website) hosten, die dann über das **Link**-Tool beim Bearbeiten des E-Mail-Textes aus der E-Mail-Campaign verlinkt werden kann.

### Wandelt Braze automatisch Nur-Text-URLs oder „www.“-Text in Links um? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

Nein. Braze scannt Ihre Nachricht nicht und konvertiert Nur-Text, wie Text, der mit `www.` beginnt oder wie eine URL aussieht, nicht in Hyperlinks. Nur Links, die Sie mit HTML-Anchor-Tags (`<a href="...">`) definieren, werden durch normales Rendering und Link-Features in Braze verarbeitet.

Wenn eine empfangende Person Nur-Text als anklickbaren Link sieht, kommt dieses Verhalten in der Regel von ihrem E-Mail-Client (zum Beispiel Gmail, Outlook oder Apple Mail). Viele Clients erkennen URL-ähnliche Zeichenketten, nachdem die Nachricht zugestellt wurde, und wandeln sie auf dem Gerät der empfangenden Person in Links um. Braze kontrolliert dieses Verhalten nicht und kann es für die empfangende Person nicht deaktivieren.

Für ein vorhersehbares Erscheinungsbild, Tracking und Styling von Links verwenden Sie explizite `<a href>`-Tags anstelle von Nur-Text-URLs.

### Kann ich das `target`-Attribut bei E-Mail-Links steuern? {#can-i-control-the-target-attribute-on-email-links}

Obwohl Sie das `target`-Attribut (wie `target="_blank"` oder `target="_top"`) bei Links in Ihrem E-Mail-HTML setzen können, ignorieren oder überschreiben die meisten E-Mail-Clients dieses Attribut. Zum Beispiel erzwingt Gmail effektiv ein `_blank`-ähnliches Verhalten, unabhängig davon, was Sie angeben.

Da das Verhalten der E-Mail-Clients variiert, sollte das `target`-Attribut nicht verwendet werden, um zu steuern, wie Links geöffnet werden. Details dazu, welche E-Mail-Clients das `target`-Attribut unterstützen, finden Sie unter [caniemail.com](https://www.caniemail.com/features/html-target/).

### Warum werden meine Nutzer:innen automatisch durch E-Mail-Sicherheitssoftware abgemeldet? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Einige Sicherheitstools für Unternehmens-E-Mails (wie Barracuda, Proofpoint und ähnliche Dienste) rufen alle URLs in eingehenden E-Mails vorab ab oder scannen sie, einschließlich Abmeldelinks. Dies kann zu unbeabsichtigten Abmeldungen führen, wenn das Sicherheitstool dem One-Click-List-Unsubscribe-Link folgt.

Um dies zu vermeiden:

- **Empfehlen Sie Empfänger:innen, Ihre Sendedomain auf die Allowlist zu setzen:** Arbeiten Sie mit den IT-Teams der betroffenen Empfänger:innen zusammen, um Ihre Sendedomain und die Braze-Tracking-Domains zur Allowlist ihres E-Mail-Sicherheitsdienstes oder Mail-Gateways hinzuzufügen.
- **Verwenden Sie ein Preference Center:** Verwenden Sie anstelle eines direkten Abmeldelinks ein [Preference Center]({{site.baseurl}}/user_guide/channels/email/subscriptions), das eine Nutzerinteraktion erfordert, um die Abmeldeaktion zu bestätigen. Sicherheitsscanner füllen in der Regel keine mehrstufigen Formulare aus.
- **Überprüfen Sie die Abmeldeprotokolle:** Prüfen Sie den `User-Agent`-Header und die IP-Adresse in Ihren Currents-Abmeldeereignisdaten, um Muster zu identifizieren, die mit automatisiertem Scannen übereinstimmen (wie konsistente `User-Agent`-Header über mehrere Abmeldungen hinweg).

Weitere Details dazu, wie serverseitiges Scannen E-Mail-Metriken beeinflussen kann, finden Sie unter [Umgang mit steigenden Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting).

### Warum hat sich meine Machine-Open-Rate unerwartet geändert? {#why-has-my-machine-open-rate-changed-unexpectedly}

[Machine Opens]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) werden durch E-Mail-Sicherheitsfunktionen wie Apple Mail Privacy Protection (MPP) ausgelöst, die E-Mail-Inhalte (einschließlich des Tracking-Pixels) vorladen, ohne dass die Nutzer:innen die E-Mail physisch öffnen. Machine-Open-Raten können schwanken aufgrund von:

- Änderungen im Anteil Ihrer Zielgruppe, die Apple Mail oder andere datenschutzaktivierte E-Mail-Clients verwenden.
- Aktualisierungen der Datenschutzfunktionen von E-Mail-Anbietern oder des Bot-Erkennungsverhaltens.
- Änderungen in Ihrer Zielgruppensegmentierung oder Ihrem Targeting.

Machine-Open-Prozentsätze sind kein zuverlässiges Maß für tatsächliches Engagement. Für eine genauere Ansicht der E-Mail-Performance konzentrieren Sie sich auf *Andere Öffnungen* (Nicht-Machine-Opens) und *Eindeutige Klicks*. Sie können diese Metriken auch über die Zeit mit dem [E-Mail-Performance-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance) vergleichen.

### Warum funktionieren meine Deeplinks in Gmail nicht? {#why-are-my-deep-links-not-working-in-gmail}

Gmail entfernt alle Nicht-HTTP/HTTPS-Links aus E-Mail-Nachrichten. Wenn Ihr Deeplink ein benutzerdefiniertes Schema verwendet (wie `myapp://path/to/content`), entfernt Gmail ihn, und der Link funktioniert nicht für Empfänger:innen, die die E-Mail in Gmail lesen. Dies ist eine Gmail-Einschränkung, keine Braze-Einschränkung.

Um dies zu umgehen:

- **Verwenden Sie Universal Links (iOS) oder App Links (Android).** Diese verwenden Standard-`https://`-URLs, die Ihre App öffnen, wenn sie installiert ist, und andernfalls auf eine Webseite zurückfallen. Einrichtungsanweisungen finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).
- **Verwenden Sie einen Deeplinking-Anbieter.** Dienste wie [Branch](https://www.branch.io/) generieren HTTP-formatierte Deeplinks, die mit E-Mail-Clients kompatibel sind, einschließlich Gmail.
- **Richten Sie einen Redirect-Endpunkt ein.** Hosten Sie einen `https://`-Endpunkt auf Ihrem Server, der auf die benutzerdefinierte Schema-URL Ihrer App weiterleitet. E-Mail-Clients behalten den `https://`-Link bei, und die Weiterleitung übernimmt das Öffnen der App.

### Enthält die Metrik *Eindeutige Öffnungen* auch *Machine Opens*? {#does-the-unique-opens-metric-include-machine-opens}

Ja. *Eindeutige Öffnungen* enthalten *Machine Opens*. Sie können beide Metriken in der Ansicht **Campaign Analytics** und im **Berichts-Builder** einsehen.

### Warum stimmt mein E-Mail-Zustellvolumen nicht mit meinem Sendevolumen überein? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Nachdem eine E-Mail gesendet wurde, entscheidet der Posteingang der empfangenden Person, wann sie zugestellt wird. Nachrichten können aufgrund eines vollen Postfachs, ESP-Drosselung von einer bestimmten IP und ähnlichen Gründen um Stunden oder Tage verzögert werden.

Wenn verzögerte Nachrichten an einem anderen Kalendertag als dem Sendetag zugestellt werden, können _Zustellungen_ die _Sendungen_ für denselben Zeitraum übersteigen. Wenn viele Verzögerungen an einem Tag landen, können _Sendungen_ die _Zustellungen_ für diesen Zeitraum übersteigen.

### Warum sehe ich eine Warnung, einen Abmeldelink einzufügen, obwohl meine E-Mail bereits einen hat? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Diese Warnung kann bei Campaigns bestehen bleiben, die von einer Campaign dupliziert wurden, die keinen Abmeldelink hatte. Um sie zu beheben:

- Gehen Sie bei HTML-E-Mails zum Tab **Nur-Text** und wählen Sie dann **Aus HTML regenerieren**.
- Duplizieren Sie nach dem Duplizieren die Variante und entfernen Sie dann die ursprüngliche Variante. Wählen Sie **nicht** die ursprüngliche Variante aus, da die Warnung sonst übernommen werden kann.

### Warum hat ein:e Nutzer:in eine E-Mail erhalten, die sie nicht hätte erhalten sollen? {#why-did-a-user-receive-an-email-they-shouldnt-have}

Die Zustellung kann falsch aussehen, selbst wenn Braze wie konfiguriert funktioniert hat. Gehen Sie Folgendes durch:

- **Doppelte Profile**, die einen Posteingang teilen (siehe [Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Seed-Listen, Testempfänger:innen oder interne Adressen**, die in der Zielgruppe oder bei einer Sendung als CC/BCC enthalten sind.
- **Segment- oder Canvas-Timing:** Die/der Nutzer:in entsprach der Zielgruppe oder dem Canvas-Schritt, als Braze die Berechtigung bewertete, dann änderten sich Attribute oder der Abo-Status, bevor sie die Nachricht gelesen haben.
- **Abo-Gruppen:** Die/der Nutzer:in blieb in einer Gruppe angemeldet, die Ihre Nachricht ansprach, auch wenn ihr globaler Abo-Status etwas anderes vermuten ließ.
- **API- oder Dateiimporte**, die die/den Nutzer:in nach der Segmentierung, aber bevor Sie die Änderung erwartet haben, aktualisiert haben.

Überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), die Campaign- oder Canvas-Changelogs und die Segmentdefinition. Wenn Sie den Versand immer noch nicht nachvollziehen können, kontaktieren Sie den Braze-Support mit Nutzerbezeichnern, `dispatch_id` (falls verfügbar) und Zeitstempeln.

### Warum hat ein:e Nutzer:in meine E-Mail-Nachricht nicht erhalten? {#why-hasnt-a-user-received-my-email-message}

Es gibt mehrere Gründe, warum ein:e Nutzer:in eine E-Mail nicht erhält, die Sie erwartet haben, darunter:

- Sie waren nicht berechtigt, die E-Mail zu erhalten.
- Ihre E-Mail-Adresse ist ungültig oder existiert nicht.
- Sie haben die Nachricht möglicherweise verpasst oder gelöscht.
- Die Nachricht befindet sich möglicherweise in ihrem Spam-Ordner.

{% alert tip %}
Ein Zustellungsereignis in Braze bedeutet, dass die E-Mail vom Server des Postfachanbieters akzeptiert wurde. Dies garantiert jedoch nicht, dass die Nachricht im Posteingang der Nutzer:innen erscheint. Der Postfachanbieter kann die Nachricht in den Spam-Ordner leiten oder in seltenen Fällen die Anzeige der Nachricht stillschweigend verhindern.
{% endalert %}

Verwenden Sie die folgenden Tabellen, um die Ursache einzugrenzen.

#### Die E-Mail wurde nicht gesendet {#the-email-wasnt-sent}

| Mögliche Ursache | Was zu prüfen ist |
|---|---|
| Die/der Nutzer:in war nicht für die Campaign oder das Canvas berechtigt | Überprüfen Sie die **Zielgruppen**-[Einstellungen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) (für Campaigns) oder **Zielgruppe** (für Canvas), um zu bestätigen, dass die/der Nutzer:in alle Zielgruppenfilter, Segmentkriterien und Zustellregeln zum Zeitpunkt des Versands erfüllt hat. |
| Die Nachricht wurde abgebrochen | Überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Abbruchgründe, wie Liquid-Fehler oder fehlende Pflichtfelder. |
| Die E-Mail-Adresse der/des Nutzer:in war ungültig oder fehlte | Überprüfen Sie in der **Nutzersuche** das Profil der/des Nutzer:in, um zu verifizieren, dass zum Zeitpunkt des Versands eine gültige E-Mail-Adresse hinterlegt war. |
| Die E-Mail-Adresse der/des Nutzer:in hatte zuvor einen Hard Bounce | Ein Hard Bounce markiert die E-Mail-Adresse als ungültig und verhindert zukünftige Sendungen an diese Adresse. Ebenso sendet Braze, wenn ein:e Empfänger:in Ihre E-Mail als Spam markiert, nur Transaktions-E-Mails an diese:n Nutzer:in, keine Standard-Campaigns. Überprüfen Sie den Tab **Engagement** im Profil der/des Nutzer:in. Weitere Informationen finden Sie unter [Abgemeldete E-Mail-Adressen]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) und [Bounces und ungültige E-Mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| Die/der Nutzer:in hat sich von E-Mails abgemeldet | Überprüfen Sie den Abo-Status der/des Nutzer:in unter **Kontakteinstellungen** im Tab **Engagement**. Braze sendet keine E-Mails an Nutzer:innen, die sich abgemeldet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ursache für nicht gesendete E-Mail" }

#### Die E-Mail wurde gesendet, ist aber nicht im Posteingang angekommen {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| Mögliche Ursache | Was zu prüfen ist |
|---|---|
| Der Postfachanbieter (MBP) war nicht erreichbar | Ein temporäres Problem verhinderte, dass die E-Mail den MBP der empfangenden Person erreichte. Dies löst sich in der Regel durch Wiederholungsversuche von selbst. E-Mail-Anbieter wiederholen Soft Bounces bis zu 72 Stunden lang. |
| Der MBP hat die E-Mail zurückgewiesen | Der Mailserver der empfangenden Person hat die E-Mail abgelehnt. Überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Bounce-Details. |
| Der MBP hat die E-Mail stillschweigend verworfen | Der MBP hat die E-Mail akzeptiert, sie aber der/dem Nutzer:in nicht angezeigt und keinen Bounce zurückgegeben. Dies liegt außerhalb der Kontrolle von Braze und kann in Braze-Protokollen nicht erkannt werden. |
| Die E-Mail ist im Spam-Ordner gelandet | Der MBP hat die Nachricht als Spam identifiziert und in den Spam- oder Junk-Ordner der/des Nutzer:in geleitet. Bitten Sie die/den Nutzer:in, ihren Spam-Ordner zu überprüfen. |
| Die empfangende Person hat benutzerdefinierte E-Mail-Filterung | Die/der Nutzer:in oder ihr:sein IT-Administrator hat möglicherweise Postfachregeln konfiguriert, die eingehende Nachrichten filtern, umleiten oder löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ursache für E-Mail nicht im Posteingang" }

### Wie kann ich eine E-Mail-Adresse von der Bounce-Liste entfernen? {#how-can-i-remove-an-email-address-from-the-bounce-list}

Wenn eine gültige E-Mail-Adresse in Braze als ungültig angezeigt wird (typischerweise nach einem Hard Bounce von Ihrem E-Mail-Anbieter), verwenden Sie den Endpunkt [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces). Dieser entfernt die Adresse von Ihrer Braze-Bounce-Liste und der Bounce-Liste Ihres E-Mail-Anbieters. Braze nimmt dann den Versand an diese Adresse wieder auf.

Wenn die Adresse als Spam markiert wurde und nicht als Hard Bounce, verwenden Sie stattdessen den Endpunkt [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam).

Weitere Informationen finden Sie unter [Bounces und ungültige E-Mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails) und [Eine E-Mail-Adresse von Ihrer Bounce- oder Spam-Liste entfernen]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#remove-an-email-address-from-your-bounce-or-spam-list).

### Wie behebe ich Probleme mit der E-Mail-Zustellbarkeit? {#how-do-i-troubleshoot-email-deliverability-issues}

Wenn Ihre E-Mails verzögert, zurückgestellt oder zurückgewiesen werden, überprüfen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Bounce- und Zurückstellungsdetails und identifizieren Sie dann, wo das Problem in der Zustellkette auftritt. Häufige Zustellbarkeitsprobleme fallen in vier Kategorien:

#### ESP-Rate-Limit-Antworten lesen {#reading-esp-rate-limit-responses}

Ihr E-Mail-Anbieter (ESP), wie Amazon SES, SparkPost oder SendGrid, gibt SMTP-Antwortcodes zurück, wenn er Nachrichten annimmt oder zurückstellt. Rate-Limit-Antworten verwenden typischerweise 4xx-Codes, die temporäre Fehler anzeigen:

- **421:** Dienst vorübergehend nicht verfügbar, oft aufgrund von hohem Volumen, Verbindungslimits oder Server-Ressourcenbeschränkungen. Die Nachricht bleibt in der Warteschlange und Ihr ESP wiederholt die Zustellung automatisch.
- **429:** API-Rate-Limit überschritten. Sie haben zu viele Anfragen innerhalb des erlaubten Zeitfensters gesendet.
- **450 / 451:** Temporäre Zurückstellung aufgrund von Volumen oder Verbindungen. Der Empfängerserver fordert Sie auf, langsamer zu senden.

Wenn Sie diese Codes im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) oder Ihrem ESP-Dashboard sehen, reduzieren Sie das Sendevolumen an die betroffene Domain und verwenden Sie progressiv längere Wiederholungsintervalle. Wenn Sie bei aktivem Rate-Limiting mit vollem Volumen weitersenden, können temporäre Zurückstellungen zu permanenten Ablehnungen eskalieren.

#### Rate-Limits von Postfachanbietern {#mailbox-provider-rate-limits}

Postfachanbieter erzwingen ihre eigenen Rate-Limits für eingehende E-Mails, getrennt von den Sendekontrollen von Braze. Diese Limits können streng sein und liegen außerhalb Ihrer direkten Kontrolle:

- Virgin Media / NTL (Großbritannien): Verwendet stündliches Rate-Limiting, das `421 4.1.1 MXIN503 Hourly ratelimit for your IP exceeded`-Fehler auslöst. Diese Limits können auch Absender mit geringem Volumen betreffen. Sie werden auf IP-Ebene über alle Absender hinweg durchgesetzt, die diese IP teilen.
- Gmail, Yahoo, iCloud, Microsoft: Jeder Anbieter hat proprietäre Drosselungsschwellenwerte basierend auf Ihrer Absender-Reputation, Ihrem Volumen und Ihren Engagement-Mustern.

Wenn Sie auf anbieterspezifisches Rate-Limiting stoßen, erwägen Sie, Ihre Sendungen über einen längeren Zeitraum zu verteilen oder nach Postfachanbieter zu segmentieren, um das Volumen gleichmäßiger zu verteilen. Überprüfen Sie Ihre Empfängerliste auf Konzentration bei einem Anbieter – wenn die meisten Empfänger:innen eine Domain verwenden, staffeln Sie die Zustellung.

#### Verzögerungen bei Unternehmens-E-Mails durch Antivirenscans {#corporate-email-delays-from-antivirus-scanning}

Geschäftliche E-Mail-Adressen durchlaufen oft Sicherheits-Gateways von Unternehmen, die Nachrichten vor der Zustellung scannen. Dies kann E-Mails um 15 bis 20 Minuten oder länger verzögern, insbesondere bei Nachrichten mit:

- Großen Anhängen
- Links zu unbekannten Domains
- Inhalten, die Phishing-Mustern ähneln

Diese Verzögerungen treten auf, weil Sicherheitssysteme Nachrichten für Verhaltensanalysen in isolierten Sandbox-Umgebungen in die Warteschlange stellen. Wenn ein großes Volumen an E-Mails gleichzeitig eintrifft, werden Nachrichten zur Analyse in die Warteschlange gestellt und die Verzögerung verlängert sich weiter. Dies ist normales Verhalten für Unternehmens-E-Mail-Sicherheit und kann nicht umgangen werden. Berücksichtigen Sie bei zeitkritischen Nachrichten an Unternehmensempfänger:innen dieses Verarbeitungsfenster in Ihrer Kommunikationsplanung.

#### Fehlerbehebung bei Google 421 4.7.28 Rate-Limit-Fehlern {#troubleshooting-google-421-4728-rate-limit-errors}

Gmail gibt einen `421-4.7.28`-Fehler zurück, wenn es eine ungewöhnliche Rate unerwünschter E-Mails von Ihrer IP-Adresse, Ihrem Sende-IP-Bereich, Ihrer SPF-Domain, DKIM-Domain oder URL-Domain erkennt. Dies ist eine temporäre Drosselung, keine permanente Sperre, signalisiert aber, dass Ihr Sendevolumen, Ihre Sendegeschwindigkeit oder Ihre Reputation nicht den aktuellen Erwartungen von Gmail entsprechen.

Wenn Sie diesen Fehler erhalten:

1. Pausieren Sie nicht-essentielle Sendungen sofort für 24 bis 48 Stunden. Wenn Sie während der Drosselung weitersenden, eskaliert das Problem und kann zu permanenten 550-Ablehnungen führen.
2. Bestätigen Sie, dass SPF, DKIM und DMARC korrekt konfiguriert sind und dass Ihr From:-Header mit Ihrer Authentifizierung übereinstimmt.
3. Überprüfen Sie die [Google Postmaster Tools](https://postmaster.google.com/) und das Braze [Deliverability Center]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center) (nach Verbindung mit Google Postmaster) auf den Compliance-Status Ihrer Domain und die Spam-Beschwerderate. Ihre von Nutzer:innen gemeldete Spam-Rate muss unter 0,1 % bleiben (die harte Obergrenze liegt bei 0,3 %).
4. Nehmen Sie nach der Pause den Versand mit 10 bis 20 % des vorherigen Volumens nur an Ihre engagiertesten Empfänger:innen wieder auf. Erhöhen Sie das Volumen langsam über mehrere Wochen, nur wenn keine weiteren 4xx-Fehler auftreten.

Weitere Hinweise finden Sie in [Googles Richtlinien für Massenversender](https://support.google.com/mail/answer/81126).

### Wie kann ich Bilder in Outlook optimieren? {#how-can-i-optimize-images-in-outlook}

Outlook verwendet oft Microsoft-Word-Rendering anstelle von Standard-Browser-Rendering, was dazu führen kann, dass Bilder falsch gerendert werden oder Rahmen um Bilder hinzugefügt werden. Dasselbe clientspezifische Rendering beeinflusst auch, [wie Alternativtext angezeigt wird]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) in verschiedenen E-Mail-Clients.

Wenn Bilder in Outlook größer als ihre erwartete Breite angezeigt werden, fügen Sie dem Bild das folgende CSS hinzu:

```css
max-width: 100%;
```

Zum Beispiel:

```html
<img src="your-image.png" style="max-width: 100%;" alt="Description">
```

Sie können Inhalte auch so umschließen, dass sie in Outlook Desktop mithilfe von bedingten Kommentaren ausgeblendet werden:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Kann ich SVG- oder WebP-Bilder in meinen E-Mail-Nachrichten verwenden? {#can-i-use-svg-or-webp-images-in-my-email-messages}

SVG-Bilder werden für E-Mails aufgrund der eingeschränkten Unterstützung durch E-Mail-Clients nicht empfohlen. Gmail und mehrere andere große E-Mail-Anbieter rendern SVG-Bilder nicht, was zu fehlerhaften oder fehlenden Bildern für Empfänger:innen führen kann. WebP wird nicht konsistent über alle Clients hinweg unterstützt.

Verwenden Sie stattdessen weit verbreitete Formate wie PNG oder JPEG, damit Bilder zuverlässig gerendert werden.

### Kann ich Videos in E-Mails einbetten? {#can-i-embed-videos-in-emails}

Eingebettete Videos werden von vielen beliebten E-Mail-Clients wie Gmail, Outlook und Yahoo nicht nativ unterstützt. Infolgedessen werden eingebettete Videoelemente möglicherweise nicht wie beabsichtigt angezeigt oder erscheinen gar nicht. Darüber hinaus kann das direkte Einbetten von Videos in eine E-Mail die E-Mail-Größe erheblich erhöhen, was die Wahrscheinlichkeit erhöht, dass die Nachricht als Spam markiert wird.

Stattdessen können Sie ein GIF oder ein statisches Bild erstellen, das einem Video in einem Videoplayer ähnelt, und dieses Bild dann mit Ihrem Video verlinken. Wenn Nutzer:innen auf das Bild klicken, werden sie zum Video weitergeleitet, das auf Ihrer Website oder einer Videoplattform gehostet wird. Braze unterstützt auch die Integration mit [Playable]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/playable), das optimierte Videoinhalte bereitstellt, die in unterstützten E-Mail-Clients automatisch abgespielt werden.

### Können Liquid-Variablen, die in einem Teil des Nachrichten-Editors zugewiesen werden, in einem anderen verwendet werden? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

Nein. Jeder Teil der E-Mail (Betreff, Text, Header, Buttons usw.) wird separat generiert, sodass Liquid, das in einem Feld zugewiesen wird, in einem anderen nicht verfügbar ist. Weisen Sie Variablen in jedem Feld zu, das sie benötigt.

### Mein E-Mail-Template fehlt. Wo ist es? {#my-email-template-is-missing-where-is-it}

Bestätigen Sie zunächst, dass Sie die [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) zum Anzeigen von Templates haben. Um gespeicherte E-Mail-Templates anzuzeigen, gehen Sie zu **Inhalte** > **E-Mail**. Sie können Templates nach Status und Typ (HTML oder Drag-and-Drop) filtern.

### Muss ich Domains für Relay- oder maskierte E-Mails registrieren? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

[Apples Private Email Relay]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) erfordert, dass Sie Ihre Sendedomains im Apple Developer Portal registrieren, um Bounces zu vermeiden. Google Shielded Email erfordert keinen manuellen Domainregistrierungs- oder Allowlisting-Prozess.

### Kann ich Hyperlinks in E-Mail-Betreffzeilen oder Preheadern hinzufügen? {#can-i-add-hyperlinks-in-email-subject-lines-or-preheaders}

Nein. Das Hinzufügen von Hyperlinks in E-Mail-Betreffzeilen wird von Postfachanbietern nicht unterstützt. Einige Postfachanbieter scannen Betreffzeilen automatisch und konvertieren physische Adressen, Daten oder Uhrzeiten in anklickbare Links, aber dies geschieht automatisch auf dem Gerät der empfangenden Person und liegt außerhalb der Kontrolle von Braze (oder eines anderen ESP).

Ebenso wird das Hinzufügen von Hyperlinks im Preheader branchenweit nicht unterstützt.

Wenn Sie eine Funktionalität benötigen, die anklickbaren Inhalten in der Betreffzeile oder im Preheader-Bereich ähnelt, erwägen Sie die Verwendung von [Gmail Promotions]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab), um interaktive Annotationen zu Ihren E-Mails für Gmail-Nutzer:innen hinzuzufügen.

### Was bedeutet der Bounce-Grund `unable to get mx info` oder `failed to get IPs from PTR record`? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

Im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) weist ein Bounce-Grund ähnlich dem folgenden auf ein Problem bei der Auflösung der E-Mail-Konfiguration der Empfängerdomain hin (die Domain nach dem `@` in der Adresse), nicht auf die Braze-Nachrichtenkomposition:

Typische Ursachen sind:

- Fehlende, falsche oder nicht erreichbare **MX-Einträge** für diese Domain
- Hostnamen für eingehende E-Mails, die nicht aufgelöst werden oder die **PTR (Reverse-DNS)**-Prüfungen nicht bestehen, die von der empfangenden Infrastruktur erwartet werden
- Ungültige oder falsch geschriebene Domains in der E-Mail-Adresse

**Nächste Schritte:**

- Bestätigen Sie die Adress- und Domain-Schreibweise.
- Wenn die Adresse korrekt ist, kontaktieren Sie die Postfachinhaber:innen oder das IT-Team für diese Domain.
- Bitten Sie sie, MX- und zugehörige DNS-Einträge, einschließlich PTR-Einträge für ihre Mailserver, bei ihrem DNS-Anbieter zu überprüfen.

Andere Empfänger:innen sind in der Regel nicht betroffen. Informationen dazu, wie Soft Bounces im Reporting erscheinen, finden Sie unter [Soft Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Warum erhalte ich eine Spam-Warnung, wenn ich eine E-Mail von Braze an mich selbst sende? {#why-do-i-get-a-spam-alert-when-sending-an-email-from-braze-to-myself}

Wenn Sie eine Test-E-Mail von Braze an Ihre eigene E-Mail-Adresse senden und eine Spam-Warnung oder Phishing-Warnung sehen – wie „die Sendedomain ähnelt der Domain Ihres Unternehmens, aber wir erkennen sie nicht“ – handelt es sich um eine gängige Anti-Phishing-Sicherheitsfunktion, nicht um einen Fehler in Ihrer Braze-Konfiguration.

Diese Warnung erscheint typischerweise, wenn die Sendedomain der E-Mail mit der Empfängerdomain übereinstimmt (zum Beispiel beide `@yourcompany.com` sind). E-Mail-Sicherheitssysteme markieren dies, weil Betrüger oft Domains fälschen, die der Unternehmensdomain einer empfangenden Person ähneln.

Um zu überprüfen, ob Ihre E-Mail korrekt konfiguriert ist:

1. Zeigen Sie die Originalnachricht (Roh-E-Mail-Header) in Ihrem E-Mail-Client an.
2. Prüfen Sie, ob SPF-, DKIM- und DMARC-Authentifizierung alle bestehen.
3. Wenn alle drei bestehen, ist Ihr Braze-E-Mail-Versand korrekt konfiguriert.

Um zu verhindern, dass diese Warnung erscheint:

Bitten Sie Ihr IT-Team, Ihre Braze-Sendedomain und IP-Adressen in den E-Mail-Sicherheitsdiensten oder dem Mail-Gateway Ihres Unternehmens auf die Allowlist zu setzen. Dies teilt Ihrem Sicherheitssystem mit, E-Mails von Ihrer Braze-Sendeinfrastruktur zu vertrauen.