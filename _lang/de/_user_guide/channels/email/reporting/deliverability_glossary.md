---
nav_title: Glossar zur E-Mail-Zustellbarkeit
article_title: Glossar zur E-Mail-Zustellbarkeit
layout: glossary_page
glossary_top_header: "Glossar zur E-Mail-Zustellbarkeit"
glossary_top_text: "Dieses Glossar definiert gängige Begriffe zur E-Mail-Zustellbarkeit und E-Mail-Infrastruktur, die Ihnen beim Versand von E-Mails über Braze begegnen können."
page_order: 1
page_type: glossary
description: "Dieses Glossar definiert gängige Begriffe zur E-Mail-Zustellbarkeit und E-Mail-Infrastruktur, die Ihnen beim Versand von E-Mails über Braze begegnen können."
channel:
  - email

glossaries:
  - name: Allowlist
    description: Eine Liste von Kontakten, die Nutzer:innen als akzeptable E-Mail-Absender einstufen und deren Nachrichten nicht gefiltert oder in den Papierkorb bzw. Spam-Ordner verschoben werden sollen.
  - name: Block
    description: Ein Block-Bounce entsteht, wenn eine E-Mail vom Postfachanbieter nicht zur Zustellung angenommen wird. Viele Postfachanbieter blockieren E-Mails von IP-Adressen oder Domains, die als Spam- oder Virenquellen gemeldet wurden oder deren Inhalt gegen E-Mail-Richtlinien oder Spam-Filter verstößt. SendGrid verwendet „Block“ für das, was üblicherweise als Soft Bounce bezeichnet wird. Bei SendGrid entsteht ein Block, wenn eine E-Mail aus technischen oder vorübergehenden Gründen nicht zur Zustellung angenommen wird.
  - name: Blocklist
    description: Listen von IP-Adressen, die als bekannte Spam-Quellen gemeldet und aufgeführt wurden. Es gibt öffentliche und private Blocklists. Öffentliche Blocklists werden veröffentlicht und der Öffentlichkeit zugänglich gemacht – oft als kostenloser Dienst, manchmal gegen Gebühr.
  - name: Bounce
    description: Auch als Hard Bounce bekannt. Eine Adresse, die einen Bounce verursacht hat, ist dauerhaft unzustellbar und wird bei nachfolgenden Sendungen unterdrückt. Weitere Informationen zu Bounces in Braze finden Sie unter <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#bounces">Bounces</a> im E-Mail-Analytics-Glossar.
  - name: Bulk-Ordner
    description: Wird in einigen E-Mail-Clients auch als Junk- oder Spam-Ordner bezeichnet.
  - name: CAN-SPAM Act
    description: "US-amerikanisches Gesetz zur Regulierung kommerzieller E-Mails (vollständiger Name: Controlling the Assault of Non-Solicited Pornography and Marketing Act of 2003)."
  - name: Klickrate
    description: Die Rate, mit der Empfänger:innen auf einen Link in der Nachricht geklickt haben. Weitere Informationen finden Sie unter <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-clicks">Unique Clicks</a> im E-Mail-Analytics-Glossar.
  - name: Inhaltsfilter
    description: Softwarefilter, die E-Mails basierend auf Text, Wörtern, Phrasen oder Header-Informationen innerhalb der E-Mail selbst blockieren.
  - name: Deferred
    description: Wenn eine Nachricht beim ersten Zustellversuch nicht zugestellt werden kann, gilt sie als „deferred“ (zurückgestellt). Die meisten zurückgestellten E-Mails werden letztendlich zugestellt.
  - name: Zustellbarkeit
    description: In der Zustellbarkeits-Community bezieht sich Zustellbarkeit primär auf die Fähigkeit, den Posteingang zu erreichen. Diese Rate kann Braze nicht direkt verfolgen, daher müssen Sie andere verfügbare Daten nutzen, um Rückschlüsse auf die Posteingangsplatzierung zu ziehen.
  - name: Zustellrate
    description: Die Rate erfolgreicher Zustellungen, unabhängig von der Posteingangsplatzierung oder ob die E-Mail geöffnet wird. Weitere Informationen finden Sie unter <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#deliveries">Deliveries %</a> im E-Mail-Analytics-Glossar.
  - name: DKIM
    description: DomainKeys Identified Mail ermöglicht es einer Organisation, die Verantwortung für eine Nachricht während der Übertragung zu übernehmen. Die Organisation ist ein Handler der Nachricht, entweder als Absender oder als Vermittler. Ihre Reputation bildet die Grundlage für die Bewertung, ob die Nachricht für die Zustellung vertrauenswürdig ist.
  - name: DMARC
    description: Domain-based Message Authentication, Reporting & Conformance ist eine technische Spezifikation, die von Organisationen entwickelt wurde, um E-Mail-Phishing und -Betrug zu reduzieren. Sie wird derzeit von allen großen Postfachanbietern verwendet, darunter Google, Yahoo und Microsoft.
  - name: Drop
    description: SendGrid führt E-Mail-Listen, um Bounces, Spam-Berichte und Abmeldungen für alle Nutzer:innen zu verfolgen. Wenn Nutzer:innen eine Nachricht an eine E-Mail-Adresse senden, die auf einer dieser Listen in ihrem Konto existiert, verwirft SendGrid die Nachricht automatisch (d. h. sie wird nicht an die Adresse gesendet).
  - name: ESP (E-Mail-Anbieter)
    description: Unternehmen, das E-Mail-Versand- und Transportfunktionen für E-Mail-Marketer bereitstellt. Viele der heutigen Marketing-, CRM or Customer-Relationship-Management [-System] (CRM)- und Customer-Engagement-Plattformen enthalten eine E-Mail-Versandkomponente und werden in Bezug auf die E-Mail-Versandfähigkeit häufig als ESPs bezeichnet. Beispiele sind ConstantContact, MailChimp, Emarsys, Salesforce Marketing Cloud, Cheetah Digital und Sailthru.
  - name: Feedback Loop (FBL)
    description: Der Mechanismus, über den Absender über Spam-Berichte benachrichtigt werden, damit sie eine Spam-Berichtsrate berechnen und die Adresse aus zukünftigen Sendungen entfernen können.
  - name: Hard Bounce
    description: Nachricht, die an eine ungültige, geschlossene oder nicht existierende E-Mail-Adresse gesendet wurde. Typischerweise können Hard Bounces anhand eines SMTP-Antwortcodes der 500er-Serie identifiziert werden. Weitere Informationen finden Sie unter <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#hard-bounce">Hard Bounce</a> im E-Mail-Analytics-Glossar.
  - name: IP
    description: Eine eindeutige Nummer, die jedem mit dem Internet verbundenen Gerät zugewiesen wird.
  - name: ISP (Internet-Provider)
    description: Unternehmen, das Internetdienste für Verbraucher:innen bereitstellt, wie AT&T, British Telecom, Comcast (Xfinity), Cox, Orange, Sky, Spectrum, Tiscali, TalkTalk und Virgin. Umgangssprachlich werden auch Postfachanbieter wie Gmail, Yahoo und Microsoft dazu gezählt.
  - name: Listenhygiene
    description: Die Pflege einer Liste, bei der Hard Bounces und abgemeldete Namen aus den Mailings entfernt werden.
  - name: List-Unsubscribe
    description: Der List-Unsubscribe-Header ist ein Text, den Sie im Header-Bereich Ihrer Nachrichten einfügen können, damit Empfänger:innen einen Abmelde-Button sehen, den sie auswählen können, um zukünftige Nachrichten automatisch zu stoppen.
  - name: Postfachanbieter (MBP)
    description: Der Anbieter des E-Mail-Zugangs für Empfänger:innen, wie Gmail, Yahoo und Microsoft.
  - name: MX-Eintrag
    description: Ein MX-Eintrag ist ein Typ von Ressourceneintrag im Domain Name System (DNS), der festlegt, wie Internet-E-Mails über das Simple Mail Transfer Protocol (SMTP) weitergeleitet werden sollen.
  - name: NDR (Non-Delivery Report)
    description: Rückmeldung eines E-Mail-Empfängers, wenn dieser eine E-Mail nicht zur Zustellung annimmt, in Form einer SMTP-Antwort. NDRs werden häufig als Bounces bezeichnet.
  - name: Rate eindeutiger Öffnungen
    description: Die Rate, mit der das Open-Tracking-Pixel geladen wurde, wobei nur eindeutige Empfänger:innen gezählt werden (keine Duplikate). Weitere Informationen finden Sie unter <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-opens">Unique Opens</a> im E-Mail-Analytics-Glossar.
  - name: Phishing
    description: Eine Form des Identitätsdiebstahls, bei der Betrüger:innen eine authentisch aussehende E-Mail verwenden, um Empfänger:innen dazu zu bringen, sensible persönliche Informationen preiszugeben, wie Kreditkarten- oder Bankkontonummern, Sozialversicherungsnummern und andere personenbezogene Daten (PII).
  - name: Re-Engagement-Campaign
    description: Eine E-Mail-Campaign, die an inaktive oder nicht reagierende Empfänger:innen gesendet wird, um sie zurückzugewinnen und erneut mit Ihren E-Mails zu interagieren – in Form von Öffnungen, Klicks und Conversions. Eine Re-Engagement-Campaign kann als eigenständige Campaign oder als Serie von Campaigns an inaktive Empfänger:innen gesendet werden.
  - name: Reverse DNS (rDNS)
    description: Der Prozess, bei dem eine IP-Adresse korrekt einem Domainnamen zugeordnet wird, anstatt dass ein Domainname einer IP-Adresse zugeordnet wird. Wenn ein Spam-Filter oder -Programm die IP-Adresse nicht dem Domainnamen zuordnen kann, kann die E-Mail abgelehnt werden.
  - name: Smart Network Data Services (SNDS)
    description: SNDS wird von Windows Live Hotmail angeboten und stellt Absendern Daten basierend auf tatsächlich an Hotmail-Abonnent:innen gesendeten E-Mails zur Verfügung. Zu den gemeldeten Metriken gehören Beschwerden, SmartScreen-Filterergebnisse und Spam-Trap-Treffer.
  - name: Soft Bounce
    description: "Jeder Bounce aufgrund eines vorübergehenden oder temporären Problems wie „Postfach voll“, „Nutzer:in über Kontingent“, „E-Mail wegen spamähnlicher Merkmale blockiert“, „Nachricht abgelehnt, da sie gegen Organisationsrichtlinien verstößt“ oder „Server vorübergehend nicht verfügbar“. SendGrid bezeichnet diese als „Blocks“.<br><br>Die Zustellung an Soft-Bounce-Adressen, bei denen ein vorübergehendes Problem vermutet wird (in der Regel mit einem SMTP-4xx-Code), wird erneut versucht, bis die Nachricht entweder zugestellt wird oder 72 Stunden vergangen sind. Wenn eine Soft-Bounce-Nachricht nach 72 Stunden nicht zugestellt werden kann, werden weitere Zustellversuche eingestellt und die fehlgeschlagene Nachrichtenzustellung wird als Bounce gezählt. Weitere Informationen finden Sie unter <a href=\"/docs/user_guide/channels/email/reporting/analytics_glossary#soft-bounce\">Soft Bounce</a> im E-Mail-Analytics-Glossar."
  - name: Spam
    description: Unerwünschte E-Mail. In den Metriken müssen Nutzer:innen diese E-Mails als Spam markieren (daher sind sie in den Zustellungen enthalten, da die E-Mail zuerst zugestellt werden muss). Weitere Informationen finden Sie unter <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">Spam</a> im E-Mail-Analytics-Glossar.
  - name: SpamCop
    description: Eine Blocklist und IP-Adressdatenbank, die früher in Privatbesitz war, aber jetzt Teil des E-Mail-Anbieters Ironport ist. Viele Postfachanbieter prüfen die IP-Adressen eingehender E-Mails anhand der SpamCop-Einträge, um festzustellen, ob die Adresse aufgrund von Spam-Beschwerden auf die Blocklist gesetzt wurde.
  - name: Spam-Rate
    description: Die Rate, mit der Empfänger:innen eine Nachricht beim Anzeigen als Spam markiert haben. Diese Rate umfasst keine E-Mails, die im Spam-Ordner landen. Sie umfasst auch keine Beschwerden von Postfachanbietern, die keine Feedback Loop haben, wie Gmail und iCloud. Weitere Informationen finden Sie unter <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">Spam</a> im E-Mail-Analytics-Glossar.
  - name: Spam-Trap
    description: Eine E-Mail-Adresse, die von ISPs und Anti-Spam-Organisationen verwendet wird, um Spam zu sammeln und zu erkennen. Auch als Spamtrap bekannt. Weitere Informationen finden Sie unter <a href="/docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps">Zustellbarkeitsfallen und Spam-Traps</a>.
  - name: Unterdrückungsliste
    description: Braze verfügt nicht über Unterdrückungslisten, Sie können jedoch eine Sunset-Richtlinie erstellen, wie unter <a href="/docs/user_guide/channels/email/best_practices/sunset_policies">Sunset-Richtlinien</a> dokumentiert. Weitere Informationen zur Verwaltung von E-Mail-Abos finden Sie unter <a href="/docs/user_guide/channels/email/subscriptions">Abos</a>.
  - name: Throttling
    description: Die Praxis, zu regulieren, wie viele E-Mail-Nachrichten ein Absender gleichzeitig an einen Postfachanbieter oder Mailserver sendet. Einige Postfachanbieter lehnen E-Mails ab, wenn sie zu viele Nachrichten erhalten.
  - name: Transaktions-E-Mail
    description: Transaktionsnachrichten werden unter CAN-SPAM als jede E-Mail definiert, die „eine zuvor vereinbarte Transaktion erleichtert, abschließt oder bestätigt“. Im Gegensatz zu kommerziellen Nachrichten müssen Transaktionsnachrichten keine US-Postadresse oder einen Abmeldelink enthalten.

---