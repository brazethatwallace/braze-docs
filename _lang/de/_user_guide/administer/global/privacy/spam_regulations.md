---
nav_title: Spam-Vorschriften
article_title: Spam-Vorschriften
page_order: 0
page_type: reference
description: "Dieser Artikel enthält Zusammenfassungen und Ressourcen zu verschiedenen Spam-Vorschriften, die Sie oder Ihre Nutzer:innen betreffen können."
channel:
- email
- push
- SMS

---

# Spam-Vorschriften {#spam-regulations}

> Es gibt eine Reihe von Gesetzen, die Absender elektronischer Kommunikation regulieren, einschließlich E-Mail, Push-Benachrichtigungen und SMS. Sie sollten sich immer über die [örtlichen Vorschriften](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country) informieren, die Sie oder Ihre Nutzer:innen betreffen können.

Braze stellt relevante Informationen auf Grundlage eigener Recherchen bereit. Für vollständige und aktuelle Details sollten Sie jedoch auch den vollständigen Text dieser Gesetze lesen.

- [CAN-SPAM](#can-spam)
- [Kanadisches Anti-Spam-Gesetz](#casl)

## CAN-SPAM {#can-spam}

Das CAN-SPAM-Gesetz von 2003 regelt die Versendung von E-Mails in den USA: „Jede elektronische Nachricht, deren Hauptzweck die kommerzielle Werbung oder die Förderung eines kommerziellen Produkts oder Dienstes ist.“ Weitere Einzelheiten können Sie auf der offiziellen Website der [Federal Trade Commission](http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business) nachlesen.

Es gibt sieben Hauptanforderungen für CAN-SPAM:

1. Verwenden Sie keine falschen oder irreführenden Kopfzeileninformationen (wie „Von“, „An“ und „Antwort an“)
2. Verwenden Sie keine irreführenden Betreffzeilen
3. Kennzeichnen Sie die Nachricht als Werbung
4. Teilen Sie den Empfänger:innen mit, wo Sie sich befinden (z. B. Ihre physische Adresse)
5. Teilen Sie den Empfänger:innen mit, wie sie sich von zukünftigen E-Mails abmelden können
6. Kommen Sie Abmeldeanfragen umgehend nach
7. Überwachen Sie, was andere in Ihrem Auftrag tun

Transaktions-E-Mails sind von diesen Regeln ausgenommen, mit Ausnahme von Nr. 1.

## Kanadisches Anti-Spam-Gesetz (CASL) {#casl}

Am 1. Juli 2014 trat das kanadische Anti-Spam-Gesetz (CASL) für E-Mails in Kraft, die an kanadische Einwohner:innen gesendet werden. Den vollständigen Gesetzestext können Sie auf der Website [Justice Laws](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) der kanadischen Regierung nachlesen. Das Gesetz besagt im Wesentlichen, dass kanadische Empfänger:innen von E-Mails und Push-Benachrichtigungen eine „ausdrückliche oder stillschweigende“ Zustimmung zu Ihrer Kommunikation mit ihnen erteilen müssen.

### CASL im Vergleich zu CAN-SPAM {#casl-versus-can-spam}

Es gibt einige wesentliche Unterschiede zwischen CASL und CAN-SPAM, insbesondere:

- CASL gilt dort, wo die Nachricht empfangen wird, sodass auch Absender außerhalb Kanadas betroffen sind
- Nachrichtenempfänger:innen müssen sich aktiv anmelden (Opt-in), anstatt sich abzumelden (Opt-out)

### Haftung {#liability}

Obwohl CASL eine dreijährige Übergangsfrist hat, die am 1. Juli 2017 endet, können die Canadian Radio-Television and Telecommunications Commission (CRTC), das Competition Bureau und das Office of the Privacy Commissioner of Canada während dieses Zeitraums bereits Untersuchungen und Rechtsstreitigkeiten einleiten. Nach Ablauf der Übergangsfrist können auch Einzelpersonen gegen Unternehmen klagen, von denen sie glauben, dass sie Spam versenden.

### Ausgenommene Nachrichten {#exempt-messages}

Die folgenden Nachrichtentypen sind von den Anforderungen des CASL ausgenommen:

- Nachrichten, die außerhalb Kanadas geöffnet werden
- Nachrichten an Familienmitglieder oder andere persönliche Kontakte
- Nachrichten an Personen, die mit Ihrem Unternehmen verbunden sind, einschließlich Mitarbeiter:innen oder Auftragnehmer:innen
- Nachrichten mit Garantieinformationen, Produktrückrufinformationen oder Sicherheitsinformationen zu einem Produkt oder Dienst, den die Empfänger:innen genutzt oder gekauft haben
- Nachrichten mit sachlichen Informationen über ein Abo, eine Mitgliedschaft oder ein Konto
- Nachrichten, die ein Produkt oder einen Dienst bereitstellen, einschließlich Produkt-Updates oder Upgrades

{% alert note %}
Dies ist keine vollständige Liste der Ausnahmen. Weitere Details finden Sie im [vollständigen Gesetzestext](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html).
{% endalert %}

### Zustimmung zu Nachrichten {#message-consent}

Braze erfordert eine ausdrückliche Zustimmung für alle E-Mail- und SMS/MMS-Nachrichten.

#### Stillschweigende Zustimmung {#implied-consent}

Eine stillschweigende Zustimmung kann in einigen Rechtsgebieten rechtlich zulässig sein, reicht jedoch nicht aus, um E-Mails über Braze zu versenden. Unsere Richtlinie zur akzeptablen Nutzung geht über die gesetzlichen Anforderungen hinaus.

#### Ausdrückliche Zustimmung {#express-consent}

Eine ausdrückliche Zustimmung ist eine schriftliche oder mündliche Bestätigung der Nachrichtenempfänger:innen und ist nur gültig, wenn die Nachricht eine klare und einfache Beschreibung enthält von:

- Warum die Zustimmung eingeholt wird
- Der Person oder Organisation, die die Zustimmung einholt

## Spam-Filter {#spam-filters}

Nur weil Ihre E-Mails erfolgreich gesendet wurden, bedeutet das nicht, dass sie auch tatsächlich gesehen wurden. Es gibt keine Universallösung, um alle Spam-Filter zu umgehen, da jeder Filter den „Spam-Score“ einer E-Mail unterschiedlich bewertet. Hier sind jedoch einige Tipps, um zu vermeiden, dass Ihre E-Mails als „Spam“ eingestuft werden.

### Erlaubnis einholen {#get-permission}

Ein Double-Opt-in-Verfahren besteht darin, nach einer ersten Anmeldung eine Folge-E-Mail mit einem Bestätigungslink zu senden. Dies bestätigt, dass die Empfänger:innen Ihre Inhalte tatsächlich erhalten möchten. Sie können noch einen Schritt weiter gehen und die Nutzer:innen bitten, Sie zu ihrem Adressbuch hinzuzufügen. Achten Sie außerdem darauf, Ihre E-Mail-Listen organisch aufzubauen&#8212;gekaufte Listen sind oft veraltet!

### Reputation aufbauen {#build-your-reputation}

Stellen Sie sicher, dass Sie Erwartungen setzen, wenn sich Personen für den Empfang Ihrer E-Mails anmelden. Seien Sie klar darüber, was Sie senden und wie oft Sie es senden werden. Ermutigen Sie dann die Nutzer:innen, mit Ihren E-Mail-Kampagnen zu interagieren, indem Sie wertvolle Inhalte bereitstellen. Personalisierte und relevante Inhalte verringern die Wahrscheinlichkeit, dass Ihre Empfänger:innen die Nachrichten als Spam markieren.

### Reputation pflegen {#maintain-your-reputation}

Bleiben Sie in ständigem Kontakt mit Ihren Nutzer:innen, um zu verhindern, dass Ihre E-Mail-Listen veralten. Wenn Sie zu lange mit dem Senden einer Nachricht warten, vergessen die Empfänger:innen Sie möglicherweise und markieren Sie als Spam. Halten Sie Ihre E-Mail-Listen aktuell, indem Sie eine Sunset-Richtlinie implementieren, um E-Mail-Adressen zu entfernen, die Bounces verursachen. Bounce-Raten sind ein wichtiger Faktor, den ISPs zur Bewertung der Reputation eines Absenders verwenden.

### Prüfen und testen {#check-and-test}

Stellen Sie sicher, dass Ihre Nachricht nichts enthält, was Spam-Filter auslösen könnte. Dazu gehören überflüssige Tags von externen Texteditoren wie Microsoft Word, ungewöhnliche Textformatierungen, übermäßige Verwendung von Ausrufezeichen (!) und Fragezeichen (?) als Satzzeichen, Schreiben in GROSSBUCHSTABEN und Spam-Triggerwörter. Senden Sie E-Mails mit unterschiedlichen Inhalten mithilfe von multivariaten Testfunktionen, um sicherzustellen, dass Ihre E-Mails nicht im Spam landen.

## Messaging-Kanal {#messaging-channel}

### E-Mail {#spam-email}

Die Qualität Ihrer E-Mail-Liste ist besonders wichtig. Eine Handvoll fehlerhafter E-Mails auf Ihrer Liste kann die Zustellung für eine Million guter Nutzer:innen ruinieren. Das Sammeln fehlerhafter E-Mails erzeugt Bounces, Blocklisting, Spam-Trap-Treffer und verschlechtert Ihre Antwortraten. Das regelmäßige Entfernen von E-Mails ohne Aktivität und das Bereinigen offensichtlicher Bounces sind der erste Schritt. Ob Sie ein Opt-in (Kästchen ankreuzen), Opt-out (Kästchen abwählen), bestätigtes Opt-in (eine E-Mail, die sich für die Anmeldung bedankt und einen Abmeldelink enthält) oder Double-Opt-in (eine E-Mail, die einen Klick zur Bestätigung erfordert) implementieren – worauf es ankommt, ist die Qualität der Liste.

### iOS {#spam-ios-windows}

Unter iOS werden Ihre Nutzer:innen immer aufgefordert, Push-Benachrichtigungen zu aktivieren. Das iOS-Dialogfeld erscheint einfach beim Öffnen der App und fordert die Nutzer:innen auf, Benachrichtigungen für Ihre App zu aktivieren. Die App-Nutzer:innen sehen dieselbe Aufforderung, sobald sie eine App zum ersten Mal öffnen, sodass alle Personen auf Ihrer iOS-Push-Liste per Definition ein Opt-in gegeben haben.

### Android {#spam-android}

Unter Android können Ihre Nutzer:innen als angemeldet betrachtet werden, basierend auf dem stillschweigenden Opt-in, das in Ihrer Datenschutzrichtlinie oder Endnutzer-Lizenzvereinbarung festgelegt ist. Möglicherweise möchten Sie ein ausdrückliches Opt-in-Verfahren implementieren, beispielsweise auf einem Startbildschirm, wenn die Nutzer:innen die App zum ersten Mal starten. Weitere Details finden Sie im Artikel [Best Practices für Push]({{site.baseurl}}/user_guide/channels/push/best_practices). Sie können die Nutzer:innen auch darüber informieren, welche Arten von Push-Benachrichtigungen sie erhalten werden, um die Opt-in-Rate zu erhöhen.