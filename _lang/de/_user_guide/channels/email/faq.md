---
nav_title: FAQ
article_title: E-Mail-FAQ
page_order: 30
description: "Diese Seite enthält Antworten auf häufig gestellte Fragen zum E-Mail-Messaging."
channel: email

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu E-Mails.

### Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben?

Wenn sich mehrere Nutzer:innen mit übereinstimmenden E-Mail-Adressen in einem Segment befinden, das eine Kampagne erhalten soll, wird zum Sendezeitpunkt ein zufälliges Nutzerprofil mit dieser E-Mail-Adresse ausgewählt. Auf diese Weise wird die E-Mail nur einmal gesendet und dedupliziert, sodass sie nicht mehrfach an dieselbe E-Mail-Adresse zugestellt wird.

Wenn mehrere Profile eine E-Mail-Adresse teilen und ein Profil sich abmeldet, aktualisiert Braze andere Profile (bis zu 100) mit dieser Adresse auf denselben Abo-Status. Dies gilt für Abmeldungen und andere Änderungen wie den globalen Abo-Status und einzelne Abo-Gruppenstatus.

Die folgenden Szenarien können den Eindruck erwecken, dass ein:e Nutzer:in eine E-Mail zweimal erhalten hat:

- **Bei der Erstellung der Kampagne oder des Canvas ist ein Fehler aufgetreten:** Die/der Nutzer:in erhält möglicherweise nicht buchstäblich denselben Versand zweimal, kann aber zwei separate E-Mails mit derselben Betreffzeile erhalten. Wenn eine Kampagne oder ein Canvas dupliziert wird, überprüfen Sie die E-Mail-Konfigurationsdetails wie Bilder oder Betreffzeilen. Sie können auch die Changelogs einsehen, um festzustellen, ob die Kampagne oder das Canvas nach dem Start geändert wurde – ein Duplikat kann dieselbe Betreffzeile wie das Original haben, als die/der Nutzer:in es erhalten hat.
- **Mehrere Nutzerprofile haben E-Mail-Weiterleitung:** Wenn ein:e Nutzer:in mehrere Konten in einer bestimmten App hat, aber ein Konto E-Mails weiterleitet, erhält die/der Nutzer:in die Kampagne einmal pro Posteingang; E-Mails können im Posteingang, an den Nachrichten weitergeleitet werden, doppelt erscheinen. Nur einige Anbieter zeigen an, wenn eine E-Mail von einem anderen Konto weitergeleitet wurde.
- **E-Mail-Konfiguration bei der/dem Empfänger:in:** Einige Clients führen Posteingänge zusammen („universeller Posteingang"). Wenn dieselbe Kampagne mehrere Konten anspricht, die einen Posteingang teilen, kann es so aussehen, als hätte eine Person die Kampagne zweimal erhalten, obwohl tatsächlich zwei verschiedene Profile angeschrieben wurden. Die/der Empfänger:in kann bestätigen, ob mehrere Konten in einem Posteingang zusammengeführt sind.

Beachten Sie, dass diese Deduplizierung erfolgt, wenn die angesprochenen Nutzer:innen im selben Versand enthalten sind. Getriggerte Kampagnen (mit Ausnahme von API-getriggerten Kampagnen) und Canvases können zu mehreren Sendungen an dieselbe E-Mail-Adresse führen (auch innerhalb eines Zeitraums, in dem Nutzer:innen aufgrund der Wiederberechtigung ausgeschlossen werden könnten), wenn verschiedene Nutzer:innen mit übereinstimmenden E-Mail-Adressen das Trigger-Ereignis zu unterschiedlichen Zeiten auslösen. Wenn beispielsweise Nutzer:in A und Nutzer:in B die E-Mail-Adresse `johndoe@example.com` teilen, sich ihre Profile aber in unterschiedlichen Zeitzonen befinden, und das Kampagnen-Trigger-Ereignis den Versand in der Zeitzone der/des Nutzers:in vorsieht, erhält die E-Mail-Adresse `johndoe@example.com` zwei E-Mails.

Nutzer:innen werden beim Canvas-Eintritt nicht nach E-Mail dedupliziert, sodass sie über den ersten Schritt eines Canvas hinaus möglicherweise nicht dedupliziert werden, wenn sie aufgrund eines ratenbegrenzten Eintritts zu leicht unterschiedlichen Zeiten fortschreiten. Wenn ein:e Nutzer:in, die/der mit einer bestimmten E-Mail-Adresse verknüpft ist, eine E-Mail öffnet oder anklickt, werden alle Nutzerprofile, die diese E-Mail-Adresse teilen, als geöffnet oder angeklickt markiert.

#### Ausnahme: API-getriggerte Kampagnen

API-getriggerte Kampagnen deduplizieren oder senden Duplikate, je nachdem, wo die Zielgruppe definiert ist. Doppelte E-Mails müssen im API-Aufruf separat mit unterschiedlichen `user_ids` angesprochen werden, um mehrere Details zu erhalten. Hier sind drei mögliche Szenarien für API-getriggerte Kampagnen:

- **Szenario 1: Doppelte E-Mails im Zielsegment:** Wenn dieselbe E-Mail in mehreren Nutzerprofilen erscheint, die in den Zielgruppen-Filtern des Dashboards für eine API-getriggerte Kampagne gruppiert sind, erhält nur eines der Profile die E-Mail.
- **Szenario 2: Doppelte E-Mails in verschiedenen `user_ids` innerhalb des Empfängerobjekts:** Wenn dieselbe E-Mail in mehreren `external_user_id`-Werten erscheint, die vom `recipients`-Objekt referenziert werden, wird die E-Mail zweimal gesendet.
- **Szenario 3: Doppelte E-Mails aufgrund doppelter `user_ids` innerhalb des Empfängerobjekts:** Wenn Sie versuchen, dasselbe Nutzerprofil zweimal hinzuzufügen, erhält nur eines der Profile die E-Mail.

{% alert important %}
Wenn Sie eine API-Kampagne über einen API-Aufruf senden (mit Ausnahme von API-getriggerten Kampagnen) und mehrere Nutzer:innen in der Segment-Zielgruppe mit derselben E-Mail-Adresse angegeben sind, wird an diese Adresse so oft gesendet, wie sie im Aufruf aufgeführt ist. Dies liegt daran, dass API-Aufrufe als absichtlich konstruiert angenommen werden.
{% endalert %}

### Was passiert mit dem Abo-Status, wenn die E-Mail-Adresse einer/eines Nutzers:in auf eine geändert wird, die von einer/einem anderen Nutzer:in geteilt wird?

Wenn Sie die E-Mail-Adresse für Nutzer:in A auf eine andere E-Mail-Adresse setzen oder aktualisieren, die von einer/einem bestehenden Nutzer:in B geteilt wird, übernimmt Nutzer:in A den Abo-Status, der bereits von Nutzer:in B existiert, es sei denn, die Einstellung **Nutzer:innen bei Aktualisierung ihrer E-Mail erneut abonnieren** ist aktiviert.

### Werden Aktualisierungen meiner ausgehenden E-Mail-Einstellungen rückwirkend angewendet?

Nein. Aktualisierungen der ausgehenden E-Mail-Einstellungen wirken sich nicht rückwirkend auf bestehende Sendungen aus. Wenn Sie beispielsweise Ihren Standard-Anzeigenamen in den E-Mail-Einstellungen ändern, wird der bestehende Standard-Anzeigename in Ihren aktiven Kampagnen oder Canvases nicht automatisch ersetzt.

### Was ist eine „gute" E-Mail-Zustellrate?

Typischerweise liegt die „magische Zahl" bei etwa 98 % zugestellter Nachrichten mit einer Bounce-Rate von nicht mehr als 3 %. Wenn Ihre Zustellrate darunter fällt, gibt es in der Regel Grund zur Sorge.

Allerdings kann eine Rate über 98 % dennoch Zustellbarkeitsprobleme aufweisen. Wenn beispielsweise alle Ihre Bounces von einer einzigen Domain stammen, ist das ein klares Signal für ein Reputationsproblem bei diesem Anbieter.

Darüber hinaus können Nachrichten zugestellt werden und im Spam-Ordner landen, was auf potenziell schwerwiegende Reputationsprobleme hinweist. Es ist wichtig, nicht nur die Anzahl der zugestellten Nachrichten zu überwachen, sondern auch die Öffnungs- und Klickraten, um festzustellen, ob die Nutzer:innen die Nachrichten tatsächlich in ihren Posteingängen sehen. Da Anbieter in der Regel nicht jede Spam-Instanz melden, könnte eine Spam-Rate von selbst 1 % Anlass zur Sorge und weiteren Analyse sein.

Schließlich können auch Ihr Geschäft und die Art der E-Mails, die Sie senden, die Zustellung beeinflussen. Jemand, der hauptsächlich [Transaktions-E-Mails]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) sendet, sollte beispielsweise eine bessere Rate erwarten als jemand, der viele Marketing-Nachrichten versendet.

### Warum ergeben meine E-Mail-Zustellmetriken nicht 100 %?

E-Mail-Zustellmetriken (Zustellungen, Bounces und Spam-Rate) ergeben möglicherweise nicht 100 %, da E-Mails, die einen Soft Bounce hatten und nach der Wiederholungsperiode von bis zu 72 Stunden nicht zugestellt wurden, nicht berücksichtigt werden.

Soft Bounces sind E-Mails, die aufgrund eines temporären oder vorübergehenden Problems zurückgewiesen werden, wie z. B. „Postfach voll", „Server vorübergehend nicht verfügbar" und mehr. Wenn eine E-Mail mit Soft Bounce nach 72 Stunden immer noch nicht zugestellt wurde, wird diese E-Mail nicht in den Zustellmetriken der Kampagne berücksichtigt.

### Was ist eine E-Mail-Feedback-Schleife?

Eine E-Mail-Feedback-Schleife (FBL) ermöglicht es Absendern, ihre Reputation zu überwachen, indem Kampagnen identifiziert werden, die ein hohes Beschwerdeaufkommen erhalten. Schritte zur Implementierung einer Gmail-Feedback-Schleife finden Sie im Artikel [Google's Feedback Loop](https://support.google.com/a/answer/6254652).

### Was sind Open-Tracking-Pixel?

[Open-Tracking-Pixel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel) nutzen die E-Mail-Klick-Tracking-Domain eines Absenders, um E-Mail-Öffnungsereignisse zu verfolgen. Das Pixel ist ein Bild-Tag, das an das HTML der E-Mail angehängt wird. Es ist üblicherweise das letzte HTML-Element innerhalb des Body-Tags. Wenn ein:e Nutzer:in die E-Mail lädt, wird eine Anfrage gestellt, um das Bild von der gebrandeten Tracking-Domain zu laden, was ein Öffnungsereignis protokolliert.

### Was passiert, wenn eine E-Mail-Kampagne oder ein Canvas gestoppt wird?

Nutzer:innen werden daran gehindert, das Canvas zu betreten, und es werden keine weiteren Nachrichten gesendet.

Bei E-Mail-Kampagnen und Canvases stoppt der Stopp-Button den Versand nicht sofort. Wenn die Sendeanfragen bereits gesendet wurden, können sie nicht mehr daran gehindert werden, an die/den Nutzer:in zugestellt zu werden, was mit einer gewissen Verzögerung geschehen kann.

Obwohl Braze keine weiteren Anfragen sendet, sobald die Kampagne oder das Canvas gestoppt wurde, können die Analytics noch steigen, während der ESP bereits laufende Anfragen weiter verarbeitet.

### Warum sehe ich mehr _Gesamtklicks_ als _Gesamtöffnungen_ in meinen E-Mail-Analytics?

_Gesamtöffnungen_ ist die Anzahl, wie oft die E-Mail von Nutzer:innen geöffnet wurde, während _Gesamtklicks_ die Anzahl ist, wie oft Nutzer:innen innerhalb der zugestellten E-Mail geklickt haben, einschließlich aller Arten von Klicks wie Link-Klicks. Sie sehen möglicherweise mehr Klicks als Öffnungen aus einem der folgenden Gründe:

- Nutzer:innen führen innerhalb einer einzelnen Öffnung mehrere Klicks im E-Mail-Text durch.
- Nutzer:innen klicken auf einige E-Mail-Links im Vorschaubereich ihres Telefons. In diesem Fall protokolliert Braze diese E-Mail als angeklickt, aber nicht als geöffnet.
- Nutzer:innen öffnen eine E-Mail erneut, die sie zuvor in der Vorschau angesehen haben.

### Warum sehe ich null E-Mail-Öffnungen und -Klicks?

Sie sehen möglicherweise keine E-Mail-Öffnungen oder -Klicks, wenn es eine Fehlkonfiguration in Ihrer Tracking-Domain gibt. Dies kann folgende Gründe haben:
- Es gibt ein SSL-Problem, bei dem Tracking-URLs `http` statt `https` verwenden.
- Es gibt ein Problem mit Ihrem CDN, bei dem der User-Agent-String bei den Öffnungsereignissen, Klickereignissen oder beiden nicht befüllt wird.

### Welche potenziellen Risiken bestehen beim Auslösen von Server-Klicks?

Bestimmte Elemente einer E-Mail-Nachricht, wie übermäßig lange Nachrichten oder zu viele Ausrufezeichen, können E-Mail-Sicherheitsreaktionen auslösen. Diese Reaktionen können das Reporting und die IP-Reputation beeinflussen und dazu führen, dass sich Nutzer:innen abmelden.

Best Practices zum Umgang mit diesen Reaktionen finden Sie unter [Umgang mit Anstiegen der Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting/).

### Kann Braze Abmeldelinks verfolgen, die zur Metrik „Abmeldungen" gezählt werden?

Braze verfolgt Abmeldelinks, wenn das folgende Liquid in E-Mails verwendet wird: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Warum sehe ich eine andere Anzahl von Abmeldungen als Klicks auf meinen Abmeldelink?

Wenn es mehr _Abmeldungen_ gibt als Nutzer:innen, die auf den Abmeldelink im E-Mail-Text geklickt haben, erklären List-Unsubscribe-Header-Aktionen oft die Differenz – ein Klick auf den List-Unsubscribe-Header zählt als _Abmeldung_, aber nicht als _Klick_ auf den Body-Link.

Wenn die Gesamtzahl der Klicks auf den Body-Abmeldelink größer ist als die Anzahl der _Abmeldungen_, haben Nutzer:innen möglicherweise mehr als einmal auf den Link geklickt.

### Kann ich einen „Diese E-Mail im Browser anzeigen"-Link zu meinen E-Mails hinzufügen?

Nein. Braze bietet diese Funktionalität nicht an. Dies liegt daran, dass eine wachsende Mehrheit der E-Mails auf Mobilgeräten und in modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte problemlos rendern.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing-Page (z. B. Ihrer Website) hosten, die dann über das **Link**-Tool beim Bearbeiten des E-Mail-Textes aus der E-Mail-Kampagne heraus verlinkt werden kann.

### Wandelt Braze automatisch Klartext-URLs oder „www."-Text in Links um?

Nein. Braze scannt Ihre Nachricht nicht und konvertiert keinen Klartext, wie Text, der mit `www.` beginnt oder wie eine URL aussieht, in Hyperlinks. Nur Links, die Sie mit HTML-Anchor-Tags (`<a href="...">`) definieren, werden durch das normale Rendering und die Link-Features in Braze verarbeitet.

Wenn ein:e Empfänger:in Klartext als anklickbaren Link sieht, kommt dieses Verhalten in der Regel von ihrem/seinem E-Mail-Client (z. B. Gmail, Outlook oder Apple Mail). Viele Clients erkennen URL-ähnliche Strings, nachdem die Nachricht zugestellt wurde, und wandeln sie auf dem Gerät der/des Empfängers:in in Links um. Braze kontrolliert dieses Verhalten nicht und kann es für die/den Empfänger:in nicht deaktivieren.

Für ein vorhersehbares Link-Erscheinungsbild, Tracking und Styling verwenden Sie explizite `<a href>`-Tags anstelle von Klartext-URLs.

### Warum werden meine Nutzer:innen automatisch durch E-Mail-Sicherheitssoftware abgemeldet?

Einige Unternehmens-E-Mail-Sicherheitstools (wie Barracuda, Proofpoint und ähnliche Dienste) rufen alle URLs in eingehenden E-Mails vorab ab oder scannen sie, einschließlich Abmeldelinks. Dies kann zu unbeabsichtigten Abmeldungen führen, wenn das Sicherheitstool dem One-Click-List-Unsubscribe-Link folgt.

Um dies zu vermeiden:

- **Empfehlen Sie Empfänger:innen, Ihre Absenderdomain auf die Allowlist zu setzen:** Arbeiten Sie mit den IT-Teams der betroffenen Empfänger:innen zusammen, um Ihre Absenderdomain und die Braze-Tracking-Domains zu deren E-Mail-Sicherheits-Allowlist hinzuzufügen.
- **Verwenden Sie ein Präferenzzentrum:** Verwenden Sie anstelle eines direkten Abmeldelinks ein [Präferenzzentrum]({{site.baseurl}}/user_guide/channels/email/subscriptions/), das eine Nutzerinteraktion zur Bestätigung der Abmeldeaktion erfordert. Sicherheitsscanner schließen in der Regel keine mehrstufigen Formulare ab.
- **Überprüfen Sie die Abmeldeprotokolle:** Prüfen Sie den `User-Agent`-Header und die IP-Adresse in Ihren Currents-Abmeldeereignisdaten, um Muster zu identifizieren, die auf automatisiertes Scannen hindeuten (wie konsistente `User-Agent`-Header über mehrere Abmeldungen hinweg).

Weitere Details dazu, wie serverseitiges Scannen E-Mail-Metriken beeinflussen kann, finden Sie unter [Umgang mit Anstiegen der Klickraten]({{site.baseurl}}/user_guide/channels/email/reporting/#handling-increases-in-click-rates).

### Warum hat sich meine Machine-Open-Rate unerwartet geändert?

[Machine Opens]({{site.baseurl}}/user_guide/analytics/metrics_glossary/#machine-opens) werden durch E-Mail-Sicherheitsfunktionen wie Apple Mail Privacy Protection (MPP) ausgelöst, die E-Mail-Inhalte (einschließlich des Tracking-Pixels) vorladen, ohne dass die/der Nutzer:in die E-Mail physisch öffnet. Machine-Open-Raten können schwanken aufgrund von:

- Änderungen im Anteil Ihrer Zielgruppe, die Apple Mail oder andere datenschutzaktivierte E-Mail-Clients verwendet.
- Updates der Datenschutzfunktionen von E-Mail-Anbietern oder des Bot-Erkennungsverhaltens.
- Änderungen in Ihrer Zielgruppen-Segmentierung oder Ihrem Targeting.

Machine-Open-Prozentsätze sind kein zuverlässiges Maß für das tatsächliche Engagement. Für eine genauere Ansicht der E-Mail-Performance konzentrieren Sie sich auf *Andere Öffnungen* (Nicht-Machine-Opens) und *Eindeutige Klicks*. Sie können diese Metriken auch im Zeitverlauf mit dem [E-Mail-Performance-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance/) vergleichen.

### Warum funktionieren meine Deeplinks in Gmail nicht?

Gmail entfernt alle Nicht-HTTP/HTTPS-Links aus E-Mail-Nachrichten. Wenn Ihr Deeplink ein benutzerdefiniertes Schema verwendet (wie `myapp://path/to/content`), entfernt Gmail ihn, und der Link funktioniert nicht für Empfänger:innen, die die E-Mail in Gmail lesen. Dies ist eine Gmail-Einschränkung, keine Braze-Einschränkung.

Um dies zu umgehen:

- **Verwenden Sie Universal Links (iOS) oder App Links (Android).** Diese verwenden Standard-`https://`-URLs, die Ihre App öffnen, wenn sie installiert ist, und andernfalls auf eine Webseite zurückfallen. Einrichtungsanweisungen finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/).
- **Verwenden Sie einen Deeplinking-Anbieter.** Dienste wie [Branch](https://www.branch.io/) generieren HTTP-formatierte Deeplinks, die mit E-Mail-Clients einschließlich Gmail kompatibel sind.
- **Richten Sie einen Redirect-Endpunkt ein.** Hosten Sie einen `https://`-Endpunkt auf Ihrem Server, der auf die benutzerdefinierte Schema-URL Ihrer App weiterleitet. E-Mail-Clients behalten den `https://`-Link bei, und die Weiterleitung übernimmt das Öffnen der App.

### Enthält die Metrik *Eindeutige Öffnungen* auch *Machine Opens*?

Nein. *Eindeutige Öffnungen* zählen nur [Andere Öffnungen]({{site.baseurl}}/user_guide/analytics/metrics_glossary/#other-opens), was E-Mails ausschließt, die als Machine Opens identifiziert wurden. *Machine Opens* werden separat erfasst. In der Ansicht **Kampagnen-Analytics** und im **Berichts-Builder** können Sie beide Metriken unabhängig voneinander einsehen.

### Warum stimmt mein E-Mail-Zustellvolumen nicht mit meinem Sendevolumen überein?

Nachdem eine E-Mail gesendet wurde, entscheidet der Posteingang der/des Empfängers:in, wann sie zugestellt wird. Nachrichten können aufgrund eines vollen Postfachs, ESP-Drosselung von einer bestimmten IP und ähnlichen Gründen um Stunden oder Tage verzögert werden.

Wenn verzögerte Nachrichten an einem anderen Kalendertag als dem Sendetag zugestellt werden, können _Zustellungen_ die _Sendungen_ für denselben Zeitraum übersteigen. Wenn viele Verzögerungen an einem Tag landen, können _Sendungen_ die _Zustellungen_ für diesen Zeitraum übersteigen.

### Warum sehe ich eine Warnung, einen Abmeldelink einzufügen, obwohl meine E-Mail bereits einen hat?

Diese Warnung kann bei Kampagnen bestehen bleiben, die von einer Kampagne dupliziert wurden, die keinen Abmeldelink hatte. Um sie zu beheben:

- Gehen Sie bei HTML-E-Mails zum Tab **Klartext** und wählen Sie dann **Aus HTML regenerieren**.
- Duplizieren Sie nach dem Duplizieren die Variante und entfernen Sie dann die ursprüngliche Variante. Wählen Sie **nicht** die ursprüngliche Variante aus, da die Warnung sonst übernommen werden kann.

### Was sind Gründe, warum mein:e Nutzer:in keine E-Mail-Kampagne erhalten hat?

Gründe, warum ein:e Nutzer:in keine E-Mail-Kampagne erhalten hat, sind unter anderem:

- Sie/er war nicht berechtigt, die E-Mail zu erhalten.
- Die E-Mail-Adresse ist ungültig oder existiert nicht.
- Die Nachricht wurde möglicherweise verpasst oder gelöscht.
- Die Nachricht befindet sich möglicherweise im Spam-Ordner.

### Wie kann ich Bilder in Outlook optimieren?

Outlook verwendet häufig ein Microsoft-Word-ähnliches Rendering, das einen Rahmen um Bilder hinzufügen kann. Sie können Inhalte so umschließen, dass sie in Office-Clients ausgeblendet werden, indem Sie standardmäßige bedingte Kommentare verwenden, zum Beispiel:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Kann ich SVG- oder WEBP-Bilder in meinen E-Mail-Nachrichten verwenden?

SVG-Bilder werden in Gmail Web oder Gmail iOS nicht gerendert. WEBP wird nicht konsistent über alle Clients hinweg unterstützt. Verwenden Sie stattdessen weit verbreitete Formate wie PNG oder JPEG, damit Bilder zuverlässig gerendert werden.

### Können Liquid-Variablen, die in einem Teil des Nachrichten-Editors zugewiesen wurden, in einem anderen verwendet werden?

Nein. Jeder Teil der E-Mail (Betreff, Text, Header, Buttons usw.) wird separat generiert, sodass Liquid, das in einem Feld zugewiesen wurde, in einem anderen nicht verfügbar ist. Weisen Sie Variablen in jedem Feld zu, das sie benötigt.

### Mein E-Mail-Template fehlt. Wo ist es?

Gehen Sie zu **Templates** > **E-Mail-Templates**. Sie können nach Typ filtern (HTML oder Drag-and-Drop).

Bestätigen Sie, dass Sie die Berechtigung haben, Templates anzuzeigen – siehe [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

### Muss ich Domains für Relay- oder maskierte E-Mails registrieren?

[Apples Private E-Mail-Relay]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO/) erfordert, dass Sie Ihre Absenderdomains im Apple Developer Portal registrieren, um Bounces zu vermeiden. Google Shielded Email erfordert keinen manuellen Domain-Registrierungs- oder Allowlisting-Prozess.