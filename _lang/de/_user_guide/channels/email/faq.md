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

**Eindeutige E-Mail-Adressen:** Braze erzwingt keine eindeutigen E-Mail-Adressen über Profile hinweg. Wenn Sie auf eine Eins-zu-eins-Beziehung zwischen einer E-Mail-Adresse und einem Profil angewiesen sind, überwachen Sie beim Erstellen von Nutzer:innen intern auf Duplikate.

**Deduplizierung vor Liquid:** Bei Sendungen, bei denen Braze innerhalb eines Versands nach E-Mail-Adresse dedupliziert (z. B. geplante Campaigns, bei denen mehrere Segment-Mitglieder mit derselben Adresse zusammen verarbeitet werden), erfolgt diese Deduplizierung, bevor Liquid für das ausgewählte Profil ausgeführt wird, das diese Adresse repräsentiert. Wenn Liquid für dieses Profil abbricht (z. B. mit [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), erhält diese Adresse die Nachricht bei diesem Versand nicht – einschließlich der Profile, die bereits durch die Deduplizierung übersprungen wurden. Getriggerte Sendungen wenden diese In-Dispatch-Adress-Deduplizierung nicht an; mehrere Profile, die eine Adresse teilen, können alle in einem Batch berechtigt bleiben, sodass dieses Abbruchverhalten nicht auf dieselbe Weise gilt (siehe nächster Absatz).

Wenn mehrere Profile eine E-Mail-Adresse teilen und ein Profil sich abmeldet, aktualisiert Braze andere Profile (bis zu 100) mit dieser Adresse auf denselben Abo-Status. Dies gilt für Abmeldungen und andere Änderungen wie den globalen Abo-Status und einzelne Abo-Gruppenstatus.

**Seed-Gruppen:** Bei Campaigns mit [Seed-Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) wählt Braze ein Profil für die primäre Zustellung aus, wenn mehrere Profile eine Adresse teilen. Diese:r primäre Empfänger:in ist möglicherweise nicht in Ihrer Seed-Gruppe, selbst wenn ein anderes Profil mit derselben Adresse darin enthalten ist.

Die folgenden Szenarien können den Eindruck erwecken, dass ein:e Nutzer:in eine E-Mail zweimal erhalten hat:

- **Seed-Listen oder Testempfänger:innen:** Seed-Adressen und interne Testempfänger:innen können einen Versand zusätzlich zu Ihrer Hauptzielgruppe erhalten, was wie ein Duplikat aussehen kann, wenn ein Posteingang sowohl einem Profil als auch einem Seed-Eintrag entspricht.
- **Bei der Erstellung der Campaign oder des Canvas ist ein Fehler aufgetreten:** Die/der Nutzer:in erhält möglicherweise nicht denselben Versand zweimal, kann aber zwei separate E-Mails mit derselben Betreffzeile erhalten. Wenn eine Campaign oder ein Canvas dupliziert wird, überprüfen Sie die E-Mail-Konfigurationsdetails wie Bilder oder Betreffzeilen. Sie können auch die Changelogs einsehen, um festzustellen, ob die Campaign oder das Canvas nach dem Start geändert wurde – ein Duplikat kann dieselbe Betreffzeile wie das Original haben, als die/der Nutzer:in es erhalten hat.
- **Mehrere Nutzerprofile haben E-Mail-Weiterleitung:** Wenn ein:e Nutzer:in mehrere Konten in einer bestimmten App hat, aber ein Konto E-Mails weiterleitet, erhält die/der Nutzer:in die Campaign einmal pro Posteingang; E-Mails können im Posteingang, an den Nachrichten weitergeleitet werden, doppelt erscheinen. Nur einige Anbieter zeigen an, wenn eine E-Mail von einem anderen Konto weitergeleitet wurde.
- **E-Mail-Konfiguration bei der/dem Empfänger:in:** Einige Clients führen Posteingänge zusammen („universeller Posteingang“). Wenn dieselbe Campaign mehrere Konten anspricht, die einen Posteingang teilen, kann es so aussehen, als hätte eine Person die Campaign zweimal erhalten, obwohl tatsächlich zwei verschiedene Profile angeschrieben wurden. Die/der Empfänger:in kann bestätigen, ob mehrere Konten in einem Posteingang zusammengeführt sind.

Diese Deduplizierung erfolgt, wenn die angesprochenen Nutzer:innen im selben Versand enthalten sind. Die Wiederberechtigung wird pro Profil ausgewertet, nicht pro E-Mail-Adresse.

Die Wiederberechtigung für E-Mail-Campaigns und Canvas-Schritte basiert auf dem Nutzerprofil – nicht auf dem Posteingang –, sodass mehrere Profile sich für separate Sendungen qualifizieren können, während diese Logik erfüllt ist. In Kombination mit Triggern kann dies dazu führen, dass mehr als eine Nachricht an denselben Posteingang zugestellt wird, selbst wenn Sie versuchen, einen einzelnen Ausschlusszeitraum auf Adressebene einzuhalten. Getriggerte Campaigns (mit Ausnahme von API-getriggerten Campaigns) und Canvases können ebenfalls zweimal an dieselbe Adresse senden, wenn verschiedene Profile mit übereinstimmenden E-Mail-Adressen den Trigger zu unterschiedlichen Zeiten auslösen – zum Beispiel, wenn Nutzer:in A und Nutzer:in B die Adresse `johndoe@example.com` teilen, sich aber in unterschiedlichen Zeitzonen befinden und die Zustellung Ortszeitzonen verwendet.

Nutzer:innen werden beim Canvas-Eintritt nicht nach E-Mail dedupliziert, sodass sie über den ersten Schritt eines Canvas hinaus möglicherweise nicht dedupliziert werden, wenn sie aufgrund eines ratenbegrenzten Eintritts zu leicht unterschiedlichen Zeiten fortschreiten. Wenn ein:e Nutzer:in, die/der mit einer bestimmten E-Mail-Adresse verknüpft ist, eine E-Mail öffnet oder anklickt, werden alle Nutzerprofile, die diese E-Mail-Adresse teilen, als geöffnet oder angeklickt markiert.

### Ausnahme: API-getriggerte Campaigns {#exception-api-triggered-campaigns}

API-getriggerte Campaigns deduplizieren oder senden Duplikate, je nachdem, wo die Zielgruppe definiert ist. Doppelte E-Mails müssen im API-Aufruf separat mit unterschiedlichen `user_ids` angesprochen werden, um mehrere Zustellungen zu erhalten. Hier sind drei mögliche Szenarien für API-getriggerte Campaigns:

- **Szenario 1: Doppelte E-Mails im Zielsegment:** Wenn dieselbe E-Mail in mehreren Nutzerprofilen erscheint, die in den Zielgruppen-Filtern des Dashboards für eine API-getriggerte Campaign gruppiert sind, erhält nur eines der Profile die E-Mail.
- **Szenario 2: Doppelte E-Mails in verschiedenen `user_ids` innerhalb des Empfängerobjekts:** Wenn dieselbe E-Mail in mehreren `external_user_id`-Werten erscheint, die vom `recipients`-Objekt referenziert werden, wird die E-Mail zweimal gesendet.
- **Szenario 3: Doppelte E-Mails aufgrund doppelter `user_ids` innerhalb des Empfängerobjekts:** Wenn Sie versuchen, dasselbe Nutzerprofil zweimal hinzuzufügen, erhält nur eines der Profile die E-Mail.

{% alert important %}
Wenn Sie eine API-Campaign über einen API-Aufruf senden (mit Ausnahme von API-getriggerten Campaigns) und mehrere Nutzer:innen in der Segment-Zielgruppe mit derselben E-Mail-Adresse angegeben sind, wird an diese Adresse so oft gesendet, wie sie im Aufruf aufgeführt ist. Dies liegt daran, dass API-Aufrufe als absichtlich konstruiert angenommen werden.
{% endalert %}

#### A/B-Tests mit doppelten E-Mail-Adressen {#ab-testing-with-duplicate-email-addresses}

Vermeiden Sie [multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing) bei E-Mails, wenn mehrere Profile dieselbe E-Mail-Adresse teilen können. Varianten werden pro Profil zugewiesen, was dazu führen kann, dass mehr als eine Nachricht an denselben Posteingang gesendet wird. Wenn Sie in dieser Situation testen müssen, kombinieren Sie keinen **Gewinnervariante**-Schritt mit [Ortszeit-Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) auf eine Weise, die die Auswahl der Gewinnervariante verzögert – diese Optionen zusammen können die Wahrscheinlichkeit doppelter Sendungen erhöhen.

#### Canvas und doppelte E-Mail-Adressen {#canvas-and-duplicate-email-addresses}

Bei Canvas-Journeys kann es von der Eintritts-Batchverarbeitung, dem Schritt-Timing und anderen Faktoren abhängen, ob doppelte E-Mail-Adressen einen oder mehrere Versände erhalten. Betrachten Sie das Verhalten als undefiniert, bis Sie es für Ihre Journey validiert haben. Führen Sie nach Möglichkeit doppelte Profile zusammen oder konsolidieren Sie sie. Wenn Sie eine Produktänderung benötigen, reichen Sie Feedback über Ihr Braze-Team ein.

### Was passiert mit dem Abo-Status, wenn die E-Mail-Adresse einer/eines Nutzers:in auf eine geändert wird, die von einer/einem anderen Nutzer:in geteilt wird? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Wenn Sie die E-Mail-Adresse für Nutzer:in A auf eine andere E-Mail-Adresse setzen oder aktualisieren, die von einer/einem bestehenden Nutzer:in B geteilt wird, übernimmt Nutzer:in A den Abo-Status, der bereits von Nutzer:in B existiert, es sei denn, die Einstellung **Resubscribe users when they update their email** ist aktiviert.

### Werden Aktualisierungen meiner ausgehenden E-Mail-Einstellungen rückwirkend angewendet? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

Nein. Aktualisierungen der ausgehenden E-Mail-Einstellungen wirken sich nicht rückwirkend auf bestehende Sendungen aus. Wenn Sie beispielsweise Ihren Standard-Anzeigenamen in den E-Mail-Einstellungen ändern, wird der bestehende Standard-Anzeigename in Ihren aktiven Campaigns oder Canvases nicht automatisch ersetzt.

### Was ist eine „gute“ E-Mail-Zustellrate? {#what-is-a-good-email-delivery-rate}

Typischerweise liegt die „magische Zahl“ bei etwa 98 % zugestellter Nachrichten mit einer Bounce-Rate von nicht mehr als 3 %. Wenn Ihre Zustellrate darunter fällt, gibt es in der Regel Grund zur Sorge.

Allerdings kann eine Rate über 98 % dennoch Zustellbarkeitsprobleme aufweisen. Wenn beispielsweise alle Ihre Bounces von einer einzigen Domain stammen, ist das ein klares Signal für ein Reputationsproblem bei diesem Anbieter.

Darüber hinaus können Nachrichten zugestellt werden und im Spam-Ordner landen, was auf potenziell schwerwiegende Reputationsprobleme hinweist. Es ist wichtig, nicht nur die Anzahl der zugestellten Nachrichten zu überwachen, sondern auch die Öffnungs- und Klickraten, um festzustellen, ob die Nutzer:innen die Nachrichten tatsächlich in ihren Posteingängen sehen. Da Anbieter in der Regel nicht jede Spam-Instanz melden, könnte selbst eine Spam-Rate von 1 % Anlass zur Sorge und weiteren Analyse sein.

Schließlich können auch Ihr Geschäft und die Art der E-Mails, die Sie senden, die Zustellung beeinflussen. Jemand, der hauptsächlich [Transaktions-E-Mails]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) sendet, sollte beispielsweise eine bessere Rate erwarten als jemand, der viele Marketing-Nachrichten versendet.

### Warum ergeben meine E-Mail-Zustellmetriken nicht 100 %? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

E-Mail-Zustellmetriken (Zustellungen, Bounces und Spam-Rate) ergeben möglicherweise nicht 100 %, da E-Mails, die einen Soft Bounce hatten und nach der Wiederholungsperiode von bis zu 72 Stunden nicht zugestellt wurden, nicht berücksichtigt werden.

Soft Bounces sind E-Mails, die aufgrund eines temporären oder vorübergehenden Problems zurückgewiesen werden, wie z. B. „Postfach voll“, „Server vorübergehend nicht verfügbar“ und mehr. Wenn eine E-Mail mit Soft Bounce nach 72 Stunden immer noch nicht zugestellt wurde, wird diese E-Mail nicht in den Zustellmetriken der Campaign berücksichtigt.

### Was ist eine E-Mail-Feedback-Schleife? {#what-is-an-email-feedback-loop}

Eine E-Mail-Feedback-Schleife (FBL) ermöglicht es Absendern, ihre Reputation zu überwachen, indem Campaigns identifiziert werden, die ein hohes Beschwerdeaufkommen erhalten. Schritte zur Implementierung einer Gmail-Feedback-Schleife finden Sie im Artikel [Google's Feedback Loop](https://support.google.com/a/answer/6254652).

### Was sind Open-Tracking-Pixel? {#what-are-open-tracking-pixels}

[Open-Tracking-Pixel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#changing-location-of-tracking-pixel) nutzen die E-Mail-Klick-Tracking-Domain eines Absenders, um E-Mail-Öffnungsereignisse zu verfolgen. Das Pixel ist ein Bild-Tag, das an das HTML der E-Mail angehängt wird. Es ist üblicherweise das letzte HTML-Element innerhalb des Body-Tags. Wenn ein:e Nutzer:in die E-Mail lädt, wird eine Anfrage gestellt, um das Bild von der gebrandeten Tracking-Domain zu laden, was ein Öffnungsereignis protokolliert.

### Was passiert, wenn eine E-Mail-Campaign oder ein Canvas gestoppt wird? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Nutzer:innen werden daran gehindert, das Canvas zu betreten, und es werden keine weiteren Nachrichten gesendet.

Bei E-Mail-Campaigns und Canvases stoppt der Stopp-Button den Versand nicht sofort. Wenn die Sendeanfragen bereits gesendet wurden, können sie nicht mehr daran gehindert werden, an die/den Nutzer:in zugestellt zu werden, was mit einer gewissen Verzögerung geschehen kann.

Obwohl Braze keine weiteren Anfragen sendet, sobald die Campaign oder das Canvas gestoppt wurde, können die Analytics noch steigen, während der ESP bereits laufende Anfragen weiter verarbeitet.

### Warum sehe ich mehr *Gesamtklicks* als *Gesamtöffnungen* in meinen E-Mail-Analytics? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

*Gesamtöffnungen* ist die Anzahl, wie oft die E-Mail von Nutzer:innen geöffnet wurde, während *Gesamtklicks* die Anzahl ist, wie oft Nutzer:innen innerhalb der zugestellten E-Mail geklickt haben, einschließlich aller Arten von Klicks wie Link-Klicks. Sie sehen möglicherweise mehr Klicks als Öffnungen aus einem der folgenden Gründe:

- Nutzer:innen führen innerhalb einer einzelnen Öffnung mehrere Klicks im E-Mail-Text durch.
- Nutzer:innen klicken auf einige E-Mail-Links im Vorschaubereich ihres Telefons. In diesem Fall protokolliert Braze diese E-Mail als angeklickt, aber nicht als geöffnet.
- Nutzer:innen öffnen eine E-Mail erneut, die sie zuvor in der Vorschau angesehen haben.

### Warum sehe ich null E-Mail-Öffnungen und -Klicks? {#why-am-i-seeing-zero-email-opens-and-clicks}

Sie sehen möglicherweise keine E-Mail-Öffnungen oder -Klicks, wenn es eine Fehlkonfiguration in Ihrer Tracking-Domain gibt. Dies kann folgende Gründe haben:
- Es gibt ein SSL-Problem, bei dem Tracking-URLs `http` statt `https` verwenden.
- Es gibt ein Problem mit Ihrem CDN, bei dem der User-Agent-String bei den Öffnungsereignissen, Klickereignissen oder beiden nicht befüllt wird.

### Welche potenziellen Risiken bestehen beim Auslösen von Server-Klicks? {#what-are-the-potential-risks-of-triggering-server-clicks}

Bestimmte Elemente einer E-Mail-Nachricht, wie übermäßig lange Nachrichten oder zu viele Ausrufezeichen, können E-Mail-Sicherheitsreaktionen auslösen. Diese Reaktionen können das Reporting und die IP-Reputation beeinflussen und dazu führen, dass sich Nutzer:innen abmelden.

Best Practices zum Umgang mit diesen Reaktionen finden Sie unter [Umgang mit Anstiegen der Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting).

### Kann Braze Abmeldelinks verfolgen, die zur Metrik „Abmeldungen“ gezählt werden? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze verfolgt Abmeldelinks, wenn das folgende Liquid in E-Mails verwendet wird: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Warum sehe ich eine andere Anzahl von Abmeldungen als Klicks auf meinen Abmeldelink? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

Wenn es mehr *Abmeldungen* gibt als Nutzer:innen, die auf den Abmeldelink im E-Mail-Text geklickt haben, erklärt [**List-Unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) oft die Differenz. List-Unsubscribe ist ein zusätzlicher Abmeldepfad im E-Mail-Header (nicht der Link in Ihrem Nachrichtentext). Wenn sich ein:e Nutzer:in auf diesem Weg abmeldet, zählt dies als *Abmeldung*, aber nicht als Klick auf die getrackte Abmelde-URL im Text.

Wenn die Gesamtzahl der Klicks auf den Body-Abmeldelink größer ist als die Anzahl der *Abmeldungen*, haben Nutzer:innen möglicherweise mehr als einmal auf den Link geklickt – zum Beispiel, wenn sie sich abgemeldet, erneut abonniert und dann wieder abgemeldet haben, können die E-Mail-Analytics mehrere Klicks in der Klick-Aufschlüsselung erfassen.

Wenn ein:e Nutzer:in den Abmeldelink zweimal anklickt (z. B. wenn sie/er sich abgemeldet, erneut abonniert und dann wieder abgemeldet hat), wird dies in den E-Mail-Analytics zweimal gezählt.

### Kann ich einen „Diese E-Mail im Browser anzeigen“-Link zu meinen E-Mails hinzufügen? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Nein. Braze bietet diese Funktionalität nicht an. Dies liegt daran, dass eine wachsende Mehrheit der E-Mails auf Mobilgeräten und in modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte problemlos rendern.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing-Page (z. B. Ihrer Website) hosten, die dann über das **Link**-Tool beim Bearbeiten des E-Mail-Textes aus der E-Mail-Campaign heraus verlinkt werden kann.

### Wandelt Braze automatisch Klartext-URLs oder „www.“-Text in Links um? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

Nein. Braze scannt Ihre Nachricht nicht und konvertiert keinen Klartext, wie Text, der mit `www.` beginnt oder wie eine URL aussieht, in Hyperlinks. Nur Links, die Sie mit HTML-Anchor-Tags (`<a href="...">`) definieren, werden durch das normale Rendering und die Link-Features in Braze verarbeitet.

Wenn ein:e Empfänger:in Klartext als anklickbaren Link sieht, kommt dieses Verhalten in der Regel von ihrem/seinem E-Mail-Client (z. B. Gmail, Outlook oder Apple Mail). Viele Clients erkennen URL-ähnliche Strings, nachdem die Nachricht zugestellt wurde, und wandeln sie auf dem Gerät der/des Empfängers:in in Links um. Braze kontrolliert dieses Verhalten nicht und kann es für die/den Empfänger:in nicht deaktivieren.

Für ein vorhersehbares Link-Erscheinungsbild, Tracking und Styling verwenden Sie explizite `<a href>`-Tags anstelle von Klartext-URLs.

### Warum werden meine Nutzer:innen automatisch durch E-Mail-Sicherheitssoftware abgemeldet? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Einige Unternehmens-E-Mail-Sicherheitstools (wie Barracuda, Proofpoint und ähnliche Dienste) rufen alle URLs in eingehenden E-Mails vorab ab oder scannen sie, einschließlich Abmeldelinks. Dies kann zu unbeabsichtigten Abmeldungen führen, wenn das Sicherheitstool dem One-Click-List-Unsubscribe-Link folgt.

Um dies zu vermeiden:

- **Empfehlen Sie Empfänger:innen, Ihre Absenderdomain auf die Allowlist zu setzen:** Arbeiten Sie mit den IT-Teams der betroffenen Empfänger:innen zusammen, um Ihre Absenderdomain und die Braze-Tracking-Domains zu deren E-Mail-Sicherheits-Allowlist hinzuzufügen.
- **Verwenden Sie ein Präferenzzentrum:** Verwenden Sie anstelle eines direkten Abmeldelinks ein [Präferenzzentrum]({{site.baseurl}}/user_guide/channels/email/subscriptions), das eine Nutzerinteraktion zur Bestätigung der Abmeldeaktion erfordert. Sicherheitsscanner schließen in der Regel keine mehrstufigen Formulare ab.
- **Überprüfen Sie die Abmeldeprotokolle:** Prüfen Sie den `User-Agent`-Header und die IP-Adresse in Ihren Currents-Abmeldeereignisdaten, um Muster zu identifizieren, die auf automatisiertes Scannen hindeuten (wie konsistente `User-Agent`-Header über mehrere Abmeldungen hinweg).

Weitere Details dazu, wie serverseitiges Scannen E-Mail-Metriken beeinflussen kann, finden Sie unter [Umgang mit Anstiegen der Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting#handling-increases-in-click-rates).

### Warum hat sich meine Machine-Open-Rate unerwartet geändert? {#why-has-my-machine-open-rate-changed-unexpectedly}

[Machine Opens]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) werden durch E-Mail-Sicherheitsfunktionen wie Apple Mail Privacy Protection (MPP) ausgelöst, die E-Mail-Inhalte (einschließlich des Tracking-Pixels) vorladen, ohne dass die/der Nutzer:in die E-Mail physisch öffnet. Machine-Open-Raten können schwanken aufgrund von:

- Änderungen im Anteil Ihrer Zielgruppe, die Apple Mail oder andere datenschutzaktivierte E-Mail-Clients verwendet.
- Updates der Datenschutzfunktionen von E-Mail-Anbietern oder des Bot-Erkennungsverhaltens.
- Änderungen in Ihrer Zielgruppen-Segmentierung oder Ihrem Targeting.

Machine-Open-Prozentsätze sind kein zuverlässiges Maß für das tatsächliche Engagement. Für eine genauere Ansicht der E-Mail-Performance konzentrieren Sie sich auf *Andere Öffnungen* (Nicht-Machine-Opens) und *Eindeutige Klicks*. Sie können diese Metriken auch im Zeitverlauf mit dem [E-Mail-Performance-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance) vergleichen.

### Warum funktionieren meine Deeplinks in Gmail nicht? {#why-are-my-deep-links-not-working-in-gmail}

Gmail entfernt alle Nicht-HTTP/HTTPS-Links aus E-Mail-Nachrichten. Wenn Ihr Deeplink ein benutzerdefiniertes Schema verwendet (wie `myapp://path/to/content`), entfernt Gmail ihn, und der Link funktioniert nicht für Empfänger:innen, die die E-Mail in Gmail lesen. Dies ist eine Gmail-Einschränkung, keine Braze-Einschränkung.

Um dies zu umgehen:

- **Verwenden Sie Universal Links (iOS) oder App Links (Android).** Diese verwenden Standard-`https://`-URLs, die Ihre App öffnen, wenn sie installiert ist, und andernfalls auf eine Webseite zurückfallen. Einrichtungsanweisungen finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).
- **Verwenden Sie einen Deeplinking-Anbieter.** Dienste wie [Branch](https://www.branch.io/) generieren HTTP-formatierte Deeplinks, die mit E-Mail-Clients einschließlich Gmail kompatibel sind.
- **Richten Sie einen Redirect-Endpunkt ein.** Hosten Sie einen `https://`-Endpunkt auf Ihrem Server, der auf die benutzerdefinierte Schema-URL Ihrer App weiterleitet. E-Mail-Clients behalten den `https://`-Link bei, und die Weiterleitung übernimmt das Öffnen der App.

### Enthält die Metrik *Eindeutige Öffnungen* auch *Machine Opens*? {#does-the-unique-opens-metric-include-machine-opens}

Ja. *Eindeutige Öffnungen* enthalten *Machine Opens*. Sie können beide Metriken in der Ansicht **Campaign Analytics** und im **Berichts-Builder** einsehen.

### Warum stimmt mein E-Mail-Zustellvolumen nicht mit meinem Sendevolumen überein? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Nachdem eine E-Mail gesendet wurde, entscheidet der Posteingang der/des Empfängers:in, wann sie zugestellt wird. Nachrichten können aufgrund eines vollen Postfachs, ESP-Drosselung von einer bestimmten IP und ähnlichen Gründen um Stunden oder Tage verzögert werden.

Wenn verzögerte Nachrichten an einem anderen Kalendertag als dem Sendetag zugestellt werden, können *Zustellungen* die *Sendungen* für denselben Zeitraum übersteigen. Wenn viele Verzögerungen an einem Tag landen, können *Sendungen* die *Zustellungen* für diesen Zeitraum übersteigen.

### Warum sehe ich eine Warnung, einen Abmeldelink einzufügen, obwohl meine E-Mail bereits einen hat? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Diese Warnung kann bei Campaigns bestehen bleiben, die von einer Campaign dupliziert wurden, die keinen Abmeldelink hatte. Um sie zu beheben:

- Gehen Sie bei HTML-E-Mails zum Tab **Plaintext** und wählen Sie dann **Regenerate from HTML**.
- Duplizieren Sie nach dem Duplizieren die Variante und entfernen Sie dann die ursprüngliche Variante. Wählen Sie **nicht** die ursprüngliche Variante aus, da die Warnung sonst übernommen werden kann.

### Warum hat ein:e Nutzer:in eine E-Mail erhalten, die sie/er nicht hätte erhalten sollen? {#why-did-a-user-receive-an-email-they-shouldnt-have}

Die Zustellung kann falsch aussehen, selbst wenn Braze wie konfiguriert funktioniert hat. Gehen Sie Folgendes durch:

- **Doppelte Profile**, die einen Posteingang teilen (siehe [Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Seed-Listen, Testempfänger:innen oder interne Adressen**, die in der Zielgruppe enthalten sind oder als CC/BCC bei einem Versand hinzugefügt wurden.
- **Segment- oder Canvas-Timing:** Die/der Nutzer:in entsprach der Zielgruppe oder dem Canvas-Schritt, als Braze die Berechtigung ausgewertet hat, und dann änderten sich Attribute oder der Abo-Status, bevor sie/er die Nachricht gelesen hat.
- **Abo-Gruppen:** Die/der Nutzer:in war weiterhin in einer Gruppe angemeldet, die Ihre Nachricht angesprochen hat, auch wenn ihr/sein globaler Abo-Status etwas anderes vermuten ließ.
- **API- oder Dateiimporte**, die die/den Nutzer:in nach der Segmentierung, aber bevor Sie die Änderung erwartet haben, aktualisiert haben.

Überprüfen Sie das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), die Campaign- oder Canvas-Changelogs und die Segment-Definition. Wenn Sie den Versand immer noch nicht nachvollziehen können, kontaktieren Sie den Braze-Support mit Nutzer-Bezeichnern, `dispatch_id` (falls verfügbar) und Zeitstempeln.

### Warum hat ein:e Nutzer:in meine E-Mail-Nachricht nicht erhalten? {#why-hasnt-a-user-received-my-email-message}

Es gibt mehrere Gründe, warum ein:e Nutzer:in eine E-Mail, die Sie erwartet haben, nicht erhalten hat, darunter:

- Sie/er war nicht berechtigt, die E-Mail zu erhalten.
- Die E-Mail-Adresse ist ungültig oder existiert nicht.
- Die Nachricht wurde möglicherweise verpasst oder gelöscht.
- Die Nachricht befindet sich möglicherweise im Spam-Ordner.

{% alert tip %}
Ein Zustellereignis in Braze bedeutet, dass die E-Mail vom Server des Postfachanbieters akzeptiert wurde. Dies garantiert jedoch nicht, dass die Nachricht im Posteingang der/des Nutzers:in erscheint. Der Postfachanbieter kann die Nachricht in den Spam-Ordner leiten oder in seltenen Fällen die Anzeige der Nachricht stillschweigend verhindern.
{% endalert %}

Verwenden Sie die folgenden Tabellen, um die Ursache einzugrenzen.

#### Die E-Mail wurde nicht gesendet {#the-email-wasnt-sent}

| Mögliche Ursache | Was zu prüfen ist |
|---|---|
| Die/der Nutzer:in war nicht für die Campaign oder das Canvas berechtigt | Überprüfen Sie die **Target Audiences** (für Campaigns) oder **Target Audience** (für Canvas) [Einstellungen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), um zu bestätigen, dass die/der Nutzer:in zum Sendezeitpunkt alle Zielgruppen-Filter, Segment-Kriterien und Zustellregeln erfüllt hat. |
| Die Nachricht wurde abgebrochen | Überprüfen Sie das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Abbruchgründe, wie Liquid-Fehler oder fehlende Pflichtfelder. |
| Die E-Mail-Adresse der/des Nutzers:in war ungültig oder fehlte | Überprüfen Sie in der **Nutzersuche** das Profil der/des Nutzers:in, um sicherzustellen, dass zum Sendezeitpunkt eine gültige E-Mail-Adresse hinterlegt war. |
| Die E-Mail-Adresse der/des Nutzers:in hatte zuvor einen Hard Bounce | Ein Hard Bounce markiert die E-Mail-Adresse als ungültig und verhindert zukünftige Sendungen an diese Adresse. Ebenso sendet Braze, wenn ein:e Empfänger:in Ihre E-Mail als Spam markiert, nur Transaktions-E-Mails an diese:n Nutzer:in, keine Standard-Campaigns. Überprüfen Sie den Tab **Engagement** im Profil der/des Nutzers:in. Weitere Informationen finden Sie unter [Abgemeldete E-Mail-Adressen]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) und [Bounces und ungültige E-Mails]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| Die/der Nutzer:in hat E-Mails abgemeldet | Überprüfen Sie den Abo-Status der/des Nutzers:in unter **Kontakteinstellungen** im Tab **Engagement**. Braze sendet keine E-Mails an Nutzer:innen, die abgemeldet sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ursache für nicht gesendete E-Mail" }

#### Die E-Mail wurde gesendet, ist aber nicht im Posteingang angekommen {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| Mögliche Ursache | Was zu prüfen ist |
|---|---|
| Der Postfachanbieter (MBP) war nicht erreichbar | Ein vorübergehendes Problem verhinderte, dass die E-Mail den MBP der/des Empfängers:in erreichte. Dies löst sich in der Regel durch Wiederholungsversuche von selbst. E-Mail-Anbieter wiederholen Soft Bounces bis zu 72 Stunden lang. |
| Der MBP hat die E-Mail zurückgewiesen | Der Mailserver der/des Empfängers:in hat die E-Mail abgelehnt. Überprüfen Sie das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) auf Bounce-Details. |
| Der MBP hat die E-Mail stillschweigend verworfen | Der MBP hat die E-Mail akzeptiert, sie aber der/dem Nutzer:in nicht angezeigt und keinen Bounce zurückgegeben. Dies liegt außerhalb der Kontrolle von Braze und kann in den Braze-Protokollen nicht erkannt werden. |
| Die E-Mail ist im Spam-Ordner gelandet | Der MBP hat die Nachricht als Spam identifiziert und in den Spam- oder Junk-Ordner der/des Nutzers:in geleitet. Bitten Sie die/den Nutzer:in, den Spam-Ordner zu überprüfen. |
| Die/der Empfänger:in hat benutzerdefinierte E-Mail-Filterung | Die/der Nutzer:in oder ihr/sein IT-Administrator hat möglicherweise Postfachregeln konfiguriert, die eingehende Nachrichten filtern, umleiten oder löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ursache für E-Mail nicht im Posteingang" }

### Wie kann ich Bilder in Outlook optimieren? {#how-can-i-optimize-images-in-outlook}

Outlook verwendet häufig ein Microsoft-Word-ähnliches Rendering, das einen Rahmen um Bilder hinzufügen kann. Sie können Inhalte so umschließen, dass sie in Office-Clients ausgeblendet werden, indem Sie standardmäßige bedingte Kommentare verwenden, zum Beispiel:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Kann ich SVG- oder WebP-Bilder in meinen E-Mail-Nachrichten verwenden? {#can-i-use-svg-or-webp-images-in-my-email-messages}

SVG-Bilder werden für E-Mails nicht empfohlen, da die Unterstützung über E-Mail-Clients hinweg eingeschränkt ist. Gmail und mehrere andere große E-Mail-Anbieter rendern SVG-Bilder nicht, was zu fehlerhaften oder fehlenden Bildern für Empfänger:innen führen kann. WebP wird nicht konsistent über alle Clients hinweg unterstützt.

Verwenden Sie stattdessen weit verbreitete Formate wie PNG oder JPEG, damit Bilder zuverlässig gerendert werden.

### Können Liquid-Variablen, die in einem Teil des Nachrichten-Editors zugewiesen wurden, in einem anderen verwendet werden? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

Nein. Jeder Teil der E-Mail (Betreff, Text, Header, Buttons usw.) wird separat generiert, sodass Liquid, das in einem Feld zugewiesen wurde, in einem anderen nicht verfügbar ist. Weisen Sie Variablen in jedem Feld zu, das sie benötigt.

### Mein E-Mail-Template fehlt. Wo ist es? {#my-email-template-is-missing-where-is-it}

Bestätigen Sie zunächst, dass Sie die [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) zum Anzeigen von Templates haben. Um gespeicherte E-Mail-Templates anzuzeigen, gehen Sie zu **Inhalt** > **E-Mail**. Sie können Templates nach Status und Typ (HTML oder Drag-and-Drop) filtern.

### Muss ich Domains für Relay- oder maskierte E-Mails registrieren? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

[Apples Private E-Mail-Relay]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) erfordert, dass Sie Ihre Absenderdomains im Apple Developer Portal registrieren, um Bounces zu vermeiden. Google Shielded Email erfordert keinen manuellen Domain-Registrierungs- oder Allowlisting-Prozess.

### Was bedeutet der Bounce-Grund `unable to get mx info` oder `failed to get IPs from PTR record`? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

Im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) weist ein Bounce-Grund ähnlich dem folgenden auf ein Problem bei der Auflösung der E-Mail-Konfiguration der empfangenden Domain hin (die Domain nach dem `@` in der Adresse), nicht auf die Braze-Nachrichtenerstellung:

Typische Ursachen sind:

- Fehlende, falsche oder nicht erreichbare **MX-Einträge** für diese Domain
- Hostnamen für eingehende E-Mails, die nicht aufgelöst werden oder die von der empfangenden Infrastruktur erwarteten **PTR-Prüfungen (Reverse DNS)** nicht bestehen
- Ungültige oder falsch geschriebene Domains in der E-Mail-Adresse

**Nächste Schritte:**

- Überprüfen Sie die Adresse und die Domain-Schreibweise.
- Wenn die Adresse korrekt ist, kontaktieren Sie die/den Postfachinhaber:in oder das IT-Team für diese Domain.
- Bitten Sie sie, die MX- und zugehörigen DNS-Einträge, einschließlich der PTR-Einträge für ihre Mailserver, bei ihrem DNS-Anbieter zu überprüfen.

Andere Empfänger:innen sind in der Regel nicht betroffen. Informationen dazu, wie Soft Bounces im Reporting erscheinen, finden Sie unter [Soft Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).