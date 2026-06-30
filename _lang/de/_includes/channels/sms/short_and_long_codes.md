# SMS- und RCS-Absender {#sms-and-rcs-senders}

> Dieser Artikel bietet eine Übersicht über die Codes und Absender, die für den Versand von SMS- und RCS-Nachrichten verfügbar sind.

## Arten von SMS- und RCS-Absendern {#types-of-sms-and-rcs-senders}

{% tabs %}
{% tab RCS-Verified Sender %}

### RCS-verifizierter Sender {#rcs-verified-sender}

RCS ist ein modernes Messaging-System, das mehr Features als herkömmliche SMS bietet und Funktionen wie Marken-Absender-IDs, Rich Media und interaktive Inhalte wie scrollbare Karussells, Schnellantworten, CTA-Buttons und vieles mehr einführt. Es wurde entwickelt, um ein eleganteres und ansprechenderes Nutzererlebnis zu bieten.

#### Details

| Visuelle Komponenten | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| - Markenname<br>- Logo<br>- optionale Beschriftung<br> - verifiziertes Badge | 4–6 Wochen für die Genehmigung durch den Netzbetreiber | Durchsatz und Zustellung hängen davon ab, dass die Empfänger:innen über eine aktive Datenverbindung (mobile Daten oder WLAN) verfügen. RCS unterliegt keinen festen netzwerkseitigen Beschränkungen wie SMS. RCS-Nachrichten werden über Datennetzwerke gesendet und nicht über die herkömmlichen Mobilfunk-Signalkanäle, die von SMS genutzt werden. | N/A | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

#### Vor- und Nachteile {#pros-and-cons}

| Vorteile |
| ---- |
| **Verifiziertes Vertrauen und Branding**<br> Im Gegensatz zu herkömmlichen SMS, bei denen Ihre Marke als zufälliger 5-stelliger Shortcode oder Langcode erscheint, ermöglicht RCS verifizierte Absenderprofile. Diese Profile umfassen das Logo Ihrer Marke, den Namen und ein „Verifiziert“-Häkchen. |
| **Umfangreiche Messaging-Features**<br> RCS unterstützt Karussells, hochauflösende Videos und vorgeschlagene Aktions-Buttons (wie „Jetzt buchen“, „Paket verfolgen“ oder „Rechnung bezahlen“). Nutzer:innen können komplexe Aufgaben erledigen, ohne ihre Messaging-App zu verlassen, was zu höheren Conversion-Raten als bei einem einfachen Textlink führen kann. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| ---- |
| **Fragmentierte Unterstützung**<br> Obwohl Google RCS für Android stark vorangetrieben hat und Apple kürzlich RCS-Unterstützung für iOS eingeführt hat, kann die Implementierung je nach Netzbetreiber und Region noch uneinheitlich sein. Wenn das Telefon oder der Netzbetreiber von Nutzer:innen RCS nicht unterstützt, wird die Nachricht in der Regel als einfache SMS versendet, wodurch alle „erweiterten“ RCS-Features verloren gehen. |
| **Plattforminkonsistenzen**<br> Das RCS-Nutzererlebnis variiert je nach Netzbetreiber, Gerätemodell und der verwendeten Messaging-App der Empfänger:innen (z. B. Google Messages oder iMessage). |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% tab SMS Short Codes %}

#### SMS-Shortcodes {#sms-short-codes}

Ein Shortcode ist eine 5- bis 6-stellige Nummer, mit der SMS schneller als mit Langcodes an Mobiltelefone gesendet und von diesen empfangen werden können. Shortcodes werden für den Versand großer Mengen und zeitkritischer Nachrichten empfohlen.

In einigen Ländern können Sie gegen eine erhöhte Gebühr eine bestimmte Nummer auswählen. Diese Shortcodes werden als Vanity-Shortcodes bezeichnet. Wenn Sie an Vanity-Shortcodes interessiert sind, wenden Sie sich an Ihre Braze-Konto-Vertretung für weitere Informationen.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 5–6 Ziffern | 4–12 Wochen Antragszeit | 100 Nachrichten pro Sekunde oder mehr | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile |
| ---- |
| **Geschwindigkeit und Skalierbarkeit**<br> Shortcodes sind speziell für hohes Nachrichtenaufkommen ausgelegt. Sie können Nachrichten schneller versenden als Langcodes, und da sie direkt von den Netzbetreibern vorab geprüft werden, ist das Risiko, von automatisierten Spam-Filtern markiert zu werden, am geringsten. |
| **Leicht merkbare „Call to Action“**<br> Für Marketingkampagnen (z. B. „Senden Sie WIN an 55555“) ist ein Shortcode für Nutzer:innen wesentlich einfacher zu merken und einzugeben als eine 10-stellige Nummer. Das macht Shortcodes zum Goldstandard für Radio-, Fernseh- und Plakatwerbung, bei der Nutzer:innen nur wenige Sekunden Zeit haben, die Nummer zu sehen oder zu hören. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| ---- |
| **Shortcodes sind in weniger Ländern verfügbar**<br> Shortcodes sind nicht in allen Ländern verfügbar. Wenden Sie sich an Ihr Braze-Konto-Team, um sich über die Länder zu informieren, in die Sie Nachrichten versenden möchten. |
| **Längerer Antragsprozess**<br> Im Gegensatz zu Langcodes und alphanumerischen Absender-IDs, die manchmal innerhalb von 1–2 Wochen bereitgestellt werden können, kann die Bereitstellung eines Shortcodes 4–12 Wochen oder länger dauern. Jeder große Netzbetreiber muss Ihren spezifischen Antrag manuell genehmigen, bevor der Code in seinem Netzwerk aktiv ist. Wenn Sie nächste Woche eine Marketingkampagne starten möchten, ist ein Shortcode keine Option. |
| **Höhere Kosten**<br> Shortcodes sind aufgrund der Einrichtungs- und jährlichen Mietgebühren in der Regel die teuerste Absenderart. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% tab SMS Long Codes %}

#### SMS-Langcodes {#sms-long-codes}

Ein Langcode ist eine Standard-Telefonnummer, die zum Senden und Empfangen von SMS-Nachrichten verwendet wird. Diese Telefonnummern werden im Vergleich zu SMS-Shortcodes (5- bis 6-stellige Nummern) in der Regel als „Langcodes“ (in vielen Ländern 10-stellige Nummern) bezeichnet.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern | 4–6 Wochen Antragszeit (kann je nach Land kürzer oder länger sein) | In den USA hängt der Langcode-Durchsatz von Ihrem 10DLC-Vertrauens-Score ab. Auf internationalen Märkten kann der Durchsatz variieren oder unter bestimmten Umständen steigen, beginnt jedoch in der Regel bei etwa 10 Nachrichten-Segmenten pro Sekunde (MPS). | Ja | 2-Wege (je nachdem, wohin Sie senden) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile |
| ---- |
| **Vertrautheit und Vertrauen**<br> Langcodes sehen aus wie persönliche Telefonnummern und enthalten häufig eine Ortsvorwahl. Für Marken bedeutet dies ein Gleichgewicht zwischen professioneller Präsenz und einer persönlichen, zugänglichen Ausstrahlung. |
| **Größere weltweite Verfügbarkeit**<br> Langcodes sind in über 100 wichtigen Ländern weltweit verfügbar. Wenden Sie sich an Ihren Customer-Success-Manager oder den [Braze-Support]({{site.baseurl}}/braze_support), um eine Liste der verfügbaren Länder zu erhalten.|
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| --- |
| **Langsamere Sendegeschwindigkeiten und tägliche Nachrichtenlimits**<br> Langcodes sind nicht wie Shortcodes für „Blast“-Marketing konzipiert. Wenn Sie versuchen, eine zeitkritische Flash-Sale-Aktion über einen Langcode an 100.000 Personen gleichzeitig zu versenden, kann es Stunden dauern, bis alle Nachrichten zugestellt sind. In den USA können Netzbetreiber wie T-Mobile auch tägliche Versandlimits für 10DLC basierend auf dem Vertrauens-Score Ihrer Marke festlegen. |
| **Höheres Filterrisiko**<br> Da Langcodes wie persönliche Telefonnummern aussehen, werden sie von den Netzbetreibern streng überwacht, um zu verhindern, dass „Person-zu-Person“-Nummern für Spam verwendet werden. Selbst bei einer registrierten 10DLC-Kampagne besteht ein deutlich höheres Risiko, von Netzbetreibern blockiert zu werden, wenn der Inhalt Ihrer Nachricht zu sehr nach Spam aussieht oder nicht den strengen Formatierungsvorschriften entspricht – im Vergleich zu einem vorab genehmigten Shortcode. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% tab SMS Alphanumeric Sender ID %}

#### Alphanumerische SMS-Absender-ID {#sms-alphanumeric-sender-id}

Eine alphanumerische Absender-ID (oft als „Alpha“ bezeichnet) ist ein erkennbarer String aus einer beliebigen Kombination von Buchstaben und Zahlen (häufig Ihr Unternehmensname oder Ihre Marke), der als Absender-ID für einseitige Textnachrichten angezeigt wird.

Sie können bis zu 11 Zeichen lang sein und Großbuchstaben (A–Z), Kleinbuchstaben (a–z), Leerzeichen und Ziffern (0–9) enthalten. Sie **dürfen nicht** ausschließlich aus Zahlen bestehen.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| Bis zu 11 Zeichen | Sofort verfügbar, wenn keine Vorabregistrierung erforderlich ist. Andernfalls 1–4 Wochen in den meisten Ländern, in denen eine Registrierung erforderlich ist. | Variiert je nach Land | Nein | 1-Weg |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile | Nachteile |
| ---- | ---- |
| {::nomarkdown} <ul><li> Verbesserte Markenbekanntheit </li><li> In vielen internationalen Märkten registrieren und prüfen lokale Netzbetreiber alphanumerische Absender vorab, sodass Ihre Nachrichten weniger wahrscheinlich in aggressiven Spam-Filtern hängen bleiben, die andernfalls zufällige Langcodes blockieren könnten. </li><li> Verfügbar innerhalb einer Woche, sofern keine Vorabregistrierung erforderlich ist. </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Zwei-Wege-Messaging</a> wird nicht unterstützt </li><li> Nicht alle Länder unterstützen dieses Feature. Beispielsweise wird es in Großbritannien unterstützt, ist aber in den USA blockiert. </li><li> In einigen Ländern gibt es ein umfangreiches Vorabregistrierungsverfahren, das die Einreichung rechtlicher Dokumente und längere Vorlaufzeiten erfordert. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vor- und Nachteile" }

Für weitere Informationen zu alphanumerischen Absender-IDs wenden Sie sich bitte an Ihren Customer-Success-Manager.
{% endtab %}
{% tab SMS toll-free numbers %}

#### SMS-fähige gebührenfreie Nummern {#sms-enabled-toll-free-numbers}

Gebührenfreie Nummern verfügen über eindeutige dreistellige Vorwahlen (z. B. 800, 888, 877 und 866), die es Nutzer:innen ermöglichen, Unternehmen kostenlos zu erreichen. Sie werden häufig für den Kundenservice eingesetzt und können auch alle Arten von A2P-Messaging (Application-to-Person) verarbeiten, einschließlich Marketing.

##### Details

| Länge | Zugang | Durchsatz | MMS aktiviert | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern	 | 2–4 Wochen Antragszeit | Beginnt bei 3 MPS (Segmente pro Sekunde), kann gegen Aufpreis erhöht werden | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile |
| ---- |
| **Professionelles Image**<br> Gebührenfreie Nummern sind in Nordamerika für die geschäftliche Kommunikation weithin anerkannt und genießen hohes Vertrauen – sie vermitteln einen professionellen und seriösen Eindruck. |
| **Flexibler Durchsatz; keine Versandlimits durch Netzbetreiber**<br> Im Gegensatz zu Standard-Langcodes, bei denen je nach Land Durchsatz- oder Versandlimits durch den Netzbetreiber gelten können, kann bei gebührenfreien Nummern der Durchsatz erhöht werden, um höhere Volumina zu unterstützen, und es gibt in den USA keine täglichen Versandlimits durch den Netzbetreiber.|
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| --- |
| **Unpersönlich und geografisch neutral**<br> Da gebührenfreie Nummern keine Ortsvorwahl haben, können sie zu „unternehmerisch“ oder anonym wirken. Für ein lokales Dienstleistungsunternehmen kann eine gebührenfreie Nummer schlechter abschneiden als ein Standard-Langcode, da sie keine lokale Verbindung herstellt und manchmal mit einer beliebigen Telemarketing-Nummer verwechselt werden kann. |
| **Zusätzliche Ebene der STOP-Filterung**<br> Gebührenfreie Nummern verfügen über eine Opt-out-Verarbeitung außerhalb von Braze, die nicht entfernt oder angepasst werden kann. Wenn Nutzer:innen „STOP“ an Ihre gebührenfreie Nummer senden, werden sie von weiteren Nachrichten Ihrer Nummer abgemeldet und erhalten eine vom Netzwerk generierte automatische Antwort. Sie erhalten keine weiteren Nachrichten von Ihrer gebührenfreien Nummer, bis sie „START“ senden, um von der Sperrliste der gebührenfreien Nummer entfernt zu werden. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% endtabs %}

## Einrichtung {#setup}

Die Einrichtungsanforderungen und Zeitpläne variieren je nach Absendertyp und dem Land, in dem der Absender bereitgestellt wird.

{% tabs local %}
{% tab RCS-verified sender %}

### RCS-verifizierter Sender

RCS-verifizierte Sender werden länderspezifisch bereitgestellt. Der Verifizierungs- und Einrichtungsprozess konzentriert sich auf Ihren Agenten oder Absender – die digitale Persona, die mit den Nutzer:innen interagiert. Sie stellen Marken-Assets und Verifizierungsdetails bereit.

#### Marken-Assets {#brand-assets}

- **Verifizierter Name:** Der Name, den Nutzer:innen oben im Nachrichten-Thread sehen. Es sollte ein wiedererkennbarer Handelsname sein, nicht unbedingt Ihr offizieller Unternehmensname.
- **Logo:** Ein hochauflösendes Bild mit 224×224 px. Es wird in einem kreisförmigen Rahmen angezeigt – platzieren Sie daher wichtige Elemente mittig.
- **Banner (Hero-Bild):** Ein Hintergrundbild für Ihre Unternehmensprofilkarte (ähnlich einem Titelbild auf Facebook oder LinkedIn).
- **Markenfarbe:** Ein Hex-Wert für die Buttons und UI-Elemente, passend zum Stil Ihres Unternehmens.

#### Verifizierungsdetails {#verification-details}

- **Ansprechperson (POC):** Dies ist entscheidend. Sie müssen eine E-Mail-Adresse einer direkten Mitarbeiterin oder eines direkten Mitarbeiters der Marke angeben (keine Agentur-E-Mail). Google oder der Netzbetreiber wird dieser Person eine E-Mail senden, um zu bestätigen, dass sie Braze autorisiert hat, in Ihrem Namen zu handeln.
- **Website und Datenschutzerklärung:** Eine aktive Website und eine Datenschutzerklärung, die erläutert, wie Sie mit Nutzerdaten und Messaging umgehen.
- **Beschreibung des Anwendungsfalls:** Eine klare Erklärung dessen, was Sie versenden (z. B. „Updates zur Bestellzustellung und Kundensupport für Einzelhandelskäufe“).

Die Zeitpläne für RCS variieren je nach Land und je nachdem, wie viele Netzbetreiber den Kanal einführen. Derzeit können Sie davon ausgehen, dass ein RCS-Sender innerhalb von 3–6 Wochen nach Beantragung der Freischaltung von den Netzbetreibern genehmigt wird.

{% endtab %}
{% tab SMS short codes %}

### SMS-Shortcodes

Shortcodes werden länderspezifisch bereitgestellt. Je nach Land ist das Antragsverfahren für Shortcodes dafür bekannt, unvorhersehbar zu sein. Braze unterstützt Sie bei jedem Schritt – wenn Sie einen Shortcode benötigen, wenden Sie sich an Ihren Onboarding-Manager oder eine andere Braze-Vertretung.

Braze hilft Ihnen bei der Zusammenstellung aller Materialien und Informationen, die für die Einreichung eines Antrags und die Konfiguration eines neuen Shortcodes erforderlich sind. Die Anforderungen variieren je nach Land, aber in vielen Fällen sind mindestens die folgenden Unterlagen erforderlich:

| Antragsunterlagen    | Beschreibung    | Anforderungen    |
|----------------------|----------------|-----------------|
| Call-to-Action (Opt-in) | Der Hauptzweck der Offenlegungen besteht darin, zu bestätigen, dass die Nutzer:innen dem Erhalt von Textnachrichten zustimmen und die Art des Programms verstehen. | {::nomarkdown}<ul><li>Produktbeschreibung</li><li>Angabe zur Nachrichtenhäufigkeit</li><li>Vollständige Geschäftsbedingungen ODER Link zu den vollständigen Geschäftsbedingungen</li><li>Datenschutzrichtlinie ODER Link zur Datenschutzrichtlinie</li><li>STOP-Schlüsselwort</li><li>Hinweis „Es können Nachrichten- und Datengebühren anfallen“.</li></ul>{:/} |
| Allgemeine Geschäftsbedingungen | Umfassende Geschäftsbedingungen können vollständig unterhalb des Call-to-Action dargestellt oder über einen Link in der Nähe des Call-to-Action aufgerufen werden. | {::nomarkdown}<ul><li>Programmname (Marke)</li><li>Angabe zur Nachrichtenhäufigkeit</li><li>Produktbeschreibung</li><li>Kontaktinformationen des Kundenservice</li><li>Opt-out-Informationen</li><li>Hinweis „Es können Nachrichten- und Datengebühren anfallen“.</li></ul>{:/} |
| Nachrichtenfluss | Programme für wiederkehrende Nachrichten sollten das Opt-in mit einer einzelnen Textnachricht bestätigen, die ausdrücklich angibt, für welches Programm sich die Nutzer:innen angemeldet haben, und klare Opt-out-Anweisungen enthalten.<br><br> Braze verarbeitet Opt-in-, Opt-out- und Hilfsnachrichten und aktualisiert automatisch den Status der Abo-Gruppe für die Nutzer:innen und die zugehörige Telefonnummer bei allen eingehenden Anfragen.<br><br> Beachten Sie, dass diese Standard-Schlüsselwörter und -Antworten auch angepasst werden können. | {::nomarkdown}<ul><li>Opt-in-Bestätigung:<ul><li>Programmname (Marke) ODER Produktbeschreibung</li><li>Opt-out-Informationen</li><li>Kontaktinformationen des Kundenservice</li><li>Angabe zur Nachrichtenhäufigkeit</li><li>Hinweis „Es können Nachrichten- und Datengebühren anfallen“.</li></ul></li><li>HELP-Antwort:<ul><li>Programmname (Marke) ODER Produktbeschreibung</li><li>Kontaktinformationen des Kundenservice (Support-E-Mail oder Telefonnummer).</li></ul></li><li>Opt-out (STOP)-Antwort:<ul><li>Programmname (Marke) ODER Produktbeschreibung</li><li>Bestätigung, dass keine weiteren Nachrichten zugestellt werden.</li></ul></li></ul>{:/} |
| Programmnachrichten | Programmnachrichten werden im regulären Verlauf des Shortcode-Programms versendet, nachdem die Nutzer:innen eine Opt-in-Bestätigung erhalten haben. | {::nomarkdown}<ul><li>Opt-out-Anweisungen sollten in regelmäßigen Abständen und mindestens einmal pro Monat bereitgestellt werden.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS-Shortcodes" }

Sobald alle Ihre Antragsunterlagen vollständig sind, reicht Braze den Antrag in Ihrem Namen bei unseren Anbietern ein. Der Antrag wird anschließend von lokalen Netzbetreibern geprüft und genehmigt, die möglicherweise zusätzliches Feedback geben oder weitere Informationen anfordern. Nachdem alle Netzbetreiber ihre Genehmigung erteilt haben, können Sie den Shortcode umgehend für die Verwendung in Braze konfigurieren.

Der Zeitrahmen für die Prüfung und Genehmigung von Shortcodes variiert, beträgt jedoch in der Regel 4–12 Wochen, abhängig vom Land und der Art des Programms.

{% alert important %}
Wenn Sie bereits über einen eigenen Shortcode verfügen, wenden Sie sich während des Onboarding-Prozesses an Ihren Customer-Success-Manager, um die Migration oder Übertragung Ihres Shortcodes zu besprechen.
{% endalert %}

{% endtab %}
{% tab SMS long codes and toll-free numbers %}

### SMS-Langcodes (10DLC) und gebührenfreie Nummern {#sms-long-codes-10dlc-and-toll-free-numbers}

In vielen Ländern hat sich die Einrichtung von Langcodes (auch „10DLCs“ oder „10-stellige Langcodes“ genannt) und gebührenfreien Nummern für den SMS-Versand von einem „Plug-and-Play“-Verfahren zu einem regulierten Überprüfungssystem gewandelt. Die Netzbetreiber möchten vor dem Versand genau wissen, wer Sie sind und was Sie senden möchten.

Während des Einrichtungsprozesses für Langcodes werden Sie voraussichtlich Details zu Ihrer Markenidentität und Ihrer Kampagnenabsicht mitteilen.

#### Markenidentität {#brand-identity}

- **Name der juristischen Person:** Muss exakt mit Ihren Steuerunterlagen übereinstimmen (z. B. „Acme Corp LLC“ und nicht „Acme“).
- **Steuer-ID:** In den USA ist dies Ihre Employer Identification Number (EIN). International benötigen Sie eine Umsatzsteuer-Identifikationsnummer (USt-IdNr.) oder eine lokale Gewerbeanmeldungsnummer (BRN).
- **Digitale Präsenz:** Eine aktive und funktionsfähige Website. Netzbetreiber können dies überprüfen, um sicherzustellen, dass es sich nicht um eine Briefkastenfirma handelt.
- **Autorisierte Kontaktperson:** Name, E-Mail-Adresse und Telefonnummer der für das Konto verantwortlichen Person.

#### Kampagnenabsicht {#campaign-intent}

- **Anwendungsfall:** Geben Sie an, ob Sie 2FA-Codes, Terminerinnerungen, Marketing-Aktionen oder andere Nachrichten versenden.
- **Beispielnachrichten:** Stellen Sie 2–5 Beispiele bereit, was Sie versenden werden.
- **Opt-in-Nachweis:** Beschreiben Sie (und zeigen Sie häufig einen Screenshot davon), wie sich Nutzer:innen anmelden. Beispiele sind ein Webformular mit Kontrollkästchen oder ein „Text START“-Schlüsselwort auf einem Plakat.

Braze arbeitet mit Ihnen zusammen, um alle erforderlichen Details für die Bereitstellung Ihres Langcodes oder Ihrer gebührenfreien Nummer zu erfassen, und reicht diese anschließend zur Prüfung und Genehmigung bei unserem Anbieter ein. Sobald unser Anbieter das Programm genehmigt hat, konfigurieren wir den Langcode oder die gebührenfreie Nummer umgehend in Braze.

Der Zeitplan für die Einrichtung hängt vom Bereitstellungsland ab. In der Regel dauert die Genehmigung von Langcodes und gebührenfreien Nummern zwischen 1 und 4 Wochen.

{% alert important %}
Alle Kund:innen, die derzeit US-Langcodes besitzen und/oder verwenden, um Nachrichten an US-Kund:innen zu senden, sind verpflichtet, ihre Langcodes zu registrieren. Weitere Informationen zu den Einzelheiten der US-amerikanischen A2P-10DLC-Registrierung und warum sie erforderlich ist, finden Sie in unserem speziellen [10DLC-Artikel]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc).
{% endalert %}

{% endtab %}
{% tab SMS alphanumeric sender ID %}

### Alphanumerische SMS-Absender-ID

Alphanumerische Absender-IDs unterliegen strengen Vorschriften, da sie leicht für Phishing gefälscht werden können. Während es in einigen Ländern möglich ist, einen Namen einzurichten und darüber zu versenden, müssen Sie in vielen Ländern zunächst nachweisen, dass Sie die Marke besitzen.

Möglicherweise werden Sie um die folgenden Angaben gebeten, um eine alphanumerische Absender-ID einzurichten.

- **Bevorzugte ID:** Ein String mit bis zu 11 Zeichen. Er muss mindestens einen Buchstaben enthalten und darf kein allgemeiner Begriff wie „BANK“ oder „INFO“ sein.
- **Nachweis der Markeninhaberschaft:** Ihr Markenzertifikat oder ein Gewerbeanmeldungsdokument (z. B. eine innerhalb der letzten 12 Monate ausgestellte Gründungsurkunde).
- **Vollmacht:** Ein unterschriebenes Schreiben auf Ihrem Firmenbriefpapier, das Braze und unseren Anbieter autorisiert, in Ihrem Namen Nachrichten unter Verwendung dieser spezifischen ID zu versenden.
- **Beispiel-Nachrichten-Templates:** In einigen Regionen müssen Sie die genauen „Templates“ der Nachrichten registrieren, die Sie versenden möchten. Abweichungen in den tatsächlichen Nachrichten können in diesen Ländern zu Zustellungsfehlern führen.

Der Zeitrahmen für die Einrichtung einer alphanumerischen Absender-ID hängt stark davon ab, ob das jeweilige Land eine „dynamische“ Einrichtung (sofort, keine Registrierung erforderlich) zulässt oder eine „Vorabregistrierung“ verlangt. In Ländern, in denen eine Vorabregistrierung erforderlich ist, variiert der Zeitrahmen, beträgt jedoch in der Regel zwischen 1 und 4 Wochen.

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen {#frequently-asked-questions}

Antworten auf häufig gestellte Fragen zu SMS- und RCS-Absendern finden Sie auf unserer Seite [Häufig gestellte Fragen zu SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions).