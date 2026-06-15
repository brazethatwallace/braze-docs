---
page_order: 5
nav_title: Wichtige Begriffe
article_title: Wichtige Begriffe für SMS, MMS und RCS
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Wichtige Begriffe"
glossary_top_text: "Sehen Sie sich die folgenden Begriffe an, um mehr über die Ökosysteme, Technologien und Prozesse von SMS, MMS und RCS zu erfahren."
page_type: glossary
description: "Dieses Glossar definiert verschiedene SMS-, MMS- und RCS-Begriffe, die Sie kennen sollten."
channel:
  - SMS
  - MMS
  - RCS

glossaries:
  - name: SMS (Short Message Service)
    description: Ein Messaging-Kanal, der 1980 entwickelt wurde und eine der ältesten Textnachrichtentechnologien darstellt. Er ist zudem einer der am weitesten verbreiteten und am häufigsten genutzten Kanäle für Textnachrichten. Dieser Kanal ist ein direkterer Weg, Ihre Nutzer:innen und Kund:innen zu erreichen als die meisten anderen Messaging-Kanäle, da er deren persönliche Telefonnummer nutzt. Daher unterliegt SMS mehr Regeln und Vorschriften als andere Messaging-Kanäle.
  - name: Short Code
    description: Dies ist eine kurze, einprägsame 5-6-stellige Zahlenfolge, die es Absendern ermöglicht, mehr Nachrichten mit konsistenteren Raten zu senden als mit Langcodes (eine Nachricht pro Sekunde).<br><br>Entweder ein Shortcode oder ein Langcode ist erforderlich.
  - name: Long Code
    description: Dies ist die standardmäßige, 10-stellige Telefonnummer (in den meisten Ländern), die es Absendern ermöglicht, Nachrichten mit einer Rate von einer Nachricht pro Sekunde zu senden.<br><br>Entweder ein Shortcode oder ein Langcode ist erforderlich.
  - name: Encoding
    description: Die Umwandlung von Inhalten in eine kodierte Form. SMS-Inhalte können entweder in GSM-7 oder UCS-2 kodiert werden.
  - name: GSM-7 Encoding (Global System for Mobile Communications)
    description: GSM-7 ist der am häufigsten verwendete Kodierungsstandard für die meisten SMS-Nachrichten. Er verwendet den Großteil des griechischen und englischen Alphabets sowie einige zusätzliche Zeichen. Mehr über die GSM-7-Kodierung und die verfügbaren Zeichensätze erfahren Sie bei <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title="GSM 7-bit default alphabet and extension table">Wikipedia</a>. Sprachen wie Chinesisch, Koreanisch oder Japanisch müssen mit der 16-Bit-UCS-2-Zeichenkodierung übertragen werden. <br> <br> Sie können davon ausgehen, dass das Zeichenlimit pro Segment für diesen Kodierungstyp bei 128 Zeichen liegt.
  - name: UCS-2 Encoding (Universal Coded Character Set)
    description: UCS-2-Kodierung ist ein Fallback-Kodierungsstandard, insbesondere wenn eine Nachricht nicht mit GSM-7 kodiert werden kann oder wenn eine Sprache mehr als 128 Zeichen zur Darstellung benötigt. UCS-2 wird besser in <a href='https://en.wikipedia.org/wiki/Code_point'>Code Points</a> gemessen, im Gegensatz zu „Zeichen“. Unabhängig davon können Sie davon ausgehen, dass das Zeichenlimit pro Segment für diesen Kodierungstyp bei 67 Zeichen liegt.
  - name: Subscription Groups for SMS
    description: Abo-Gruppen sind ein Braze-Tool, mit dem Sie bestimmte Abo-Stufen von Nutzer:innen oder Kund:innen ansprechen können. Abo-Gruppen für SMS werden intern basierend auf Ihrem Nachrichtendienst erstellt und können nicht über Workspaces hinweg geteilt werden.
  - name: Message Segments
    description: Ein Nachrichten-Segment ist eine Gruppierung von bis zu einer definierten Anzahl von Zeichen (160 für GSM-7-Kodierung; 67 für UCS-2-Kodierung), die in einem einzelnen SMS-Versand gesendet wird. Wenn Sie eine SMS mit 161 Zeichen unter Verwendung der GSM-7-Kodierung versenden, werden Sie feststellen, dass zwei (2) Nachrichten-Segmente gesendet wurden. Das Senden mehrerer Nachrichten-Segmente kann zu zusätzlichen Kosten führen.
  - name: Message Service
    description: Eine Sammlung von Langcodes, Shortcodes und alphanumerischen IDs, die zum Senden Ihrer SMS-Nachricht mit Braze verwendet werden.
  - name: Keyword
    description: "Ein kurzes Wort, das an einen Shortcode oder Langcode gesendet wird, um mit einem vordefinierten SMS-Programm zu interagieren oder um sich von einem bestimmten Programm oder allen Programmen auf einem Code abzumelden (OPT-OUT). Zum Beispiel <code>STOP</code>. Schlüsselwörter sollten <br> - alphanumerisch sein <br> - keine Leerzeichen enthalten <br> - weniger als 10 Zeichen haben. <br> <br> Eine bestimmte Kombination aus Schlüsselwort und Shortcode darf jeweils nur in einem aktiven Programm verwendet werden. Wenn ein Schlüsselwort eingegeben wird, das bereits von einem anderen Programm verwendet wird, erscheint ein Validierungsfehler. <br> <br> Es gibt zwei obligatorische Schlüsselwortkategorien, die alle SMS-Inhaltsanbieter einhalten müssen: <code>STOP</code> und <code>HELP</code>."
  - name: Mandatory Keyword HELP
    description: Für jedes Programm, das in der SMS Campaign Manager-Plattform erstellt wird, muss Inhalt für dieses Schlüsselwort bereitgestellt werden und den Best Practices sowie der Carrier-Compliance des jeweiligen Landes oder der Region entsprechen, in dem/der der SMS-Verkehr gesendet und empfangen wird. In den meisten Fällen sollte dieser Inhalt eine kurze Erklärung des SMS-Programms und Informationen zur Abmeldung (OPT-OUT) enthalten.
  - name: Global STOP Keywords
    description: Variationen umfassen <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. Diese werden als <code>Global-Stop-Keywords</code> bezeichnet. Wenn eines dieser Schlüsselwörter an einen Shortcode oder Langcode gesendet wird, führt dies dazu, dass die Mobilnummer (die ursprüngliche Mobiltelefonnummer) von jedem aktiven SMS-Programm auf diesem Code abgemeldet wird, mit dem sie verknüpft ist.
  - name: Vanity Code
    description: Ein Vanity-Shortcode ist eine 5-6-stellige Telefonnummer, die speziell von einer Marke ausgewählt wird. Vanity-Shortcodes sind markenspezifisch und für Verbraucher:innen leichter zu merken.
  - name: Shared Short Code
    description: Bei der Verwendung eines geteilten Shortcodes kommen alle Textnachrichten, unabhängig davon, welches Unternehmen oder welche Organisation sie sendet, von derselben 5-6-stelligen Telefonnummer auf dem Mobilgerät der Verbraucher:innen an. Geteilte Shortcodes sind zwar relativ kostengünstig und sofort verfügbar, dies bedeutet jedoch, dass Ihr Unternehmen keinen dedizierten Shortcode hat und davon abhängig ist, dass andere Unternehmen das korrekte Protokoll mit Ihrem geteilten Shortcode einhalten.
  - name: Alphanumeric Sender ID
    description: Die alphanumerische Absender-ID ermöglicht es Ihnen, Ihren Firmennamen oder Ihre Marke als Absender-ID mit alphanumerischen Zeichen festzulegen, wenn Sie Einweg-Nachrichten an unterstützte Länder senden.
  - name: Toll-Free Number
    description: Eine gebührenfreie Telefonnummer ist eine Telefonnummer, bei der alle eingehenden Anrufe dem Empfänger in Rechnung gestellt werden, anstatt dem anrufenden Teilnehmer Kosten zu verursachen. Gebührenfreie Nummern in den USA und Kanada sind SMS-fähig, wobei den Abonnent:innen Gebühren für eingehende und ausgehende Textnachrichten berechnet werden.<br><br>Gebührenfreies Messaging eignet sich am besten, wenn Ihr Anwendungsfall Person-zu-Person ist, wie z. B. Kundensupport oder Vertrieb, bei dem sowohl der Absender als auch der Empfänger per Text kommunizieren.
  - name: One-Way Messaging
    description: Einweg-Messaging ermöglicht es Ihnen, mit Ihren Kund:innen durch das Senden von Textnachrichten zu kommunizieren. Einweg-Messaging ist nützlich, wenn Sie eine alphanumerische Absender-ID in Märkten implementieren, in denen Lang- und Shortcodes nicht verfügbar sind.
  - name: Two-Way Messaging
    description: Zweiweg-Messaging ermöglicht es Ihnen, eine Konversation zu führen, indem Sie sowohl Textnachrichten senden als auch empfangen.
  - name: MMS (Multimedia Message Service)
    description: MMS wird zum Senden von Nachrichten mit Multimedia-Inhalten (JPEG, GIF, PNG) an Mobiltelefone verwendet. Wie SMS ist MMS ein Messaging-Kanal mit hoher Dringlichkeit, der es Ihnen ermöglicht, sofort mit Kund:innen zu kommunizieren. MMS erweitert die Möglichkeiten von SMS, indem es Ihnen die Fähigkeit gibt, Medien zu ansonsten reinen Text-SMS hinzuzufügen.
  - name: RCS (Rich Communication Services)
    description: Rich Communication Services (RCS) erweitert herkömmliche SMS, indem es Marken ermöglicht, Nachrichten zu versenden, die nicht nur informativ, sondern auch deutlich ansprechender sind. RCS bringt Features wie hochwertige Medien, interaktive Buttons und gebrandete Absenderprofile direkt in die vorinstallierten Messaging-Apps der Nutzer:innen.
  - name: RCS-Verified Sender
    description: Die sendende Entität einer RCS-Nachricht, also das, was die Empfänger:innen auf ihrem Gerät sehen, um zu erkennen, woher die Nachricht stammt. RCS-verifizierte Absender enthalten einen Firmennamen, eine Beschreibung, visuelles Branding und ein Verifizierungs-Badge. Nachdem Sie die erforderlichen RCS-Absenderregistrierungsinformationen an Braze übermittelt haben, kümmert sich Braze um die Registrierung und die Einrichtung der Abo-Gruppe.
  - name: SMS Fallback
    description: Wenn eine RCS-Nachricht nicht zugestellt werden kann (z. B. aufgrund fehlender Carrier-Unterstützung in der Region), versucht Braze dennoch, die Nachricht per SMS zuzustellen, wenn ein SMS-Code innerhalb der Abo-Gruppe vorhanden ist.
  - name: Basic RCS
    description: Reine Text-RCS-Nachrichten mit bis zu 160 Zeichen. Wird als einzelne Nachricht abgerechnet. Diese Kategorie wird nur im globalen Modell verwendet.
  - name: Single RCS
    description: Reine Text-RCS-Nachrichten mit mehr als 160 Zeichen oder mit Rich-Elementen wie Buttons oder Medien. Wird als einzelne Nachricht abgerechnet. Diese Kategorie wird nur im globalen Modell verwendet.
  - name: Rich RCS
    description: Reine Text-RCS-Nachrichten, mit oder ohne eingeschränkte Vorschläge oder Buttons. Abrechnung pro Segment (160 UTF-8 Bytes). Diese Kategorie wird nur im US-Modell verwendet.
  - name: Rich Media RCS
    description: RCS-Nachrichten, die eine Mediendatei (Bild, Video) oder eine Rich Card enthalten. Wird als einzelne Nachricht abgerechnet, unabhängig von der Nachrichtenlänge. Diese Kategorie wird nur im US-Modell verwendet.
---