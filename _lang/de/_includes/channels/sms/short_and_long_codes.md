# Kurzmitteilungsdienst or SMS- und RCS-Absender {#sms-and-rcs-senders}

> Dieser Artikel bietet eine Übersicht über die Codes und Absender, die für den Versand von Kurzmitteilungsdienst or SMS- und RCS-Nachrichten verfügbar sind.

## Arten von Kurzmitteilungsdienst or SMS- und RCS-Sendern {#types-of-sms-and-rcs-senders}

{% tabs %}
{% tab RCS-verifizierter Sender %}

### RCS-verifizierter Sender {#rcs-verified-sender}

RCS ist ein modernes Messaging-System, das mehr Features bietet als herkömmliche Kurzmitteilungsdienst or SMS und Funktionen wie gebrandete Sender-IDs, Rich-Media und interaktive Inhalte wie scrollbare Karussells, Schnellantworten, CTA-Buttons und mehr einführt. Es ist darauf ausgelegt, eine elegantere und ansprechendere Nutzererfahrung zu bieten.

{% alert important %}
RCS-Nachrichten können nicht über Twilio-Messaging-Dienste gesendet werden. Abo-Gruppen, die Twilio für Kurzmitteilungsdienst or SMS verwenden, müssen einen Infobip-kompatiblen RCS-Sender (oder einen anderen unterstützten RCS-Anbieter) für RCS-Datenverkehr nutzen. Andernfalls werden RCS-Sends zum Sendezeitpunkt abgebrochen.
{% endalert %}

#### Details

| Visuelle Komponenten | Zugang | Durchsatz | MMS-fähig | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| - Markenname<br>- Logo<br>- optionale Bildunterschrift<br> - verifiziertes Badge | 4–6 Wochen für die Carrier-Genehmigung | Durchsatz und Zustellung hängen davon ab, ob die Empfänger:innen eine aktive Datenverbindung (mobile Daten oder WLAN) haben. RCS stützt sich nicht auf feste netzwerkbasierte Grenzen wie Kurzmitteilungsdienst or SMS; RCS-Nachrichten werden über Datennetzwerke gesendet, nicht über die herkömmlichen zellularen Signalisierungskanäle, die von Kurzmitteilungsdienst or SMS genutzt werden. | N/A | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

#### Vor- und Nachteile {#pros-and-cons}

| Vorteile |
| ---- |
| **Verifiziertes Vertrauen und Branding**<br> Im Gegensatz zu herkömmlicher Kurzmitteilungsdienst or SMS, bei der Ihre Marke als zufälliger 5-stelliger Shortcode oder Langcode erscheint, ermöglicht RCS verifizierte Sender-Profile. Diese Profile enthalten das Logo, den Namen und ein „Verifiziert“-Häkchen Ihrer Marke. |
| **Rich-Messaging-Features**<br> RCS unterstützt Karussells, hochauflösende Videos und vorgeschlagene Aktions-Buttons (wie „Jetzt buchen“, „Paket verfolgen“ oder „Rechnung bezahlen“). Nutzer:innen können komplexe Aufgaben erledigen, ohne ihre Messaging-App zu verlassen, was zu höheren Konversionsraten führen kann als ein einfacher Textlink. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| ---- |
| **Fragmentierte Unterstützung**<br> Obwohl Google RCS für Android stark vorangetrieben hat und Apple kürzlich RCS-Unterstützung für iOS eingeführt hat, kann die Implementierung bei verschiedenen Carriern und Regionen noch uneinheitlich sein. Wenn das Gerät oder der Carrier der Nutzer:innen RCS nicht unterstützt, wird die Nachricht in der Regel als einfache Kurzmitteilungsdienst or SMS gesendet, wobei alle „Rich“-RCS-Features verloren gehen. |
| **Plattform-Inkonsistenzen**<br> Die RCS-Nutzererfahrung variiert je nach Carrier, Gerätemodell und verwendeter Messaging-App der Empfänger:innen (z. B. Google Messages oder iMessage). |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS-Shortcodes %}

#### Kurzmitteilungsdienst or SMS-Shortcodes {#sms-short-codes}

Ein Shortcode ist eine 5- bis 6-stellige Nummer, die Kurzmitteilungsdienst or SMS schneller als Langcodes an Mobiltelefone senden und von diesen empfangen kann. Shortcodes werden für den Versand großer Volumina und zeitkritischer Nachrichten empfohlen.

In einigen Ländern können Sie gegen eine zusätzliche Gebühr eine bestimmte Nummer wählen. Diese Shortcodes werden als Vanity-Shortcodes bezeichnet. Wenn Sie sich für Vanity-Shortcodes interessieren, wenden Sie sich an Ihre Braze-Kontaktperson für weitere Details.

##### Details

| Länge | Zugang | Durchsatz | MMS-fähig | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 5–6 Ziffern | 4–12 Wochen Beantragung | 100 Nachrichten pro Sekunde oder mehr | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile |
| ---- |
| **Geschwindigkeit und Skalierbarkeit**<br> Shortcodes sind speziell für hohes Nachrichtenvolumen konzipiert. Sie können Nachrichten schneller senden als Langcodes und haben, da sie direkt von den Carriern vorab geprüft werden, das geringste Risiko, von automatisierten Spam-Filtern markiert zu werden. |
| **Leicht einprägsam für „Call to Action“**<br> Für Marketingkampagnen (z. B. „Sende GEWINN an 55555“) ist ein Shortcode für Nutzer:innen viel leichter zu merken und einzutippen als eine 10-stellige Nummer. Das macht Shortcodes zum Goldstandard für Radio-, TV- und Plakatwerbung, bei der Nutzer:innen nur wenige Sekunden Zeit haben, die Nummer zu sehen oder zu hören. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| ---- |
| **Shortcodes sind in weniger Ländern verfügbar**<br> Shortcodes sind nicht in allen Ländern verfügbar. Wenden Sie sich an Ihr Braze-Kontoteam, um sich nach den Ländern zu erkundigen, in die Sie Nachrichten senden möchten. |
| **Längerer Beantragungsprozess**<br> Im Gegensatz zu Langcodes und alphanumerischen Sender-IDs, die manchmal innerhalb von 1–2 Wochen bereitgestellt werden können, kann die Bereitstellung eines Shortcodes 4–12 Wochen oder länger dauern. Jeder große Carrier muss Ihren spezifischen Antrag manuell genehmigen, bevor der Code in seinem Netzwerk aktiv ist. Wenn Sie nächste Woche einen Marketing-Launch haben, ist ein Shortcode keine Option. |
| **Höhere Kosten**<br> Shortcodes sind aufgrund der Einrichtungs- und jährlichen Mietgebühren in der Regel der teuerste Sender-Typ. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS-Langcodes %}

#### Kurzmitteilungsdienst or SMS-Langcodes {#sms-long-codes}

Ein Langcode ist eine Standard-Telefonnummer, die zum Senden und Empfangen von Kurzmitteilungsdienst or SMS-Nachrichten verwendet wird. Diese Telefonnummern werden im Vergleich zu Kurzmitteilungsdienst or SMS-Shortcodes (5- bis 6-stellige Nummern) typischerweise als „Langcodes“ (in vielen Ländern 10-stellige Nummern) bezeichnet.

##### Details

| Länge | Zugang | Durchsatz | MMS-fähig | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern | 4–6 Wochen Beantragung (kann in verschiedenen Ländern kürzer oder länger sein) | In den USA hängt der Langcode-Durchsatz von Ihrem 10DLC-Vertrauens-Score ab; auf internationalen Märkten kann der Durchsatz variieren oder unter bestimmten Umständen erhöht werden, beginnt aber typischerweise bei etwa 10 Nachrichtensegmenten pro Sekunde (MPS or Messages pro Sekunde). | Ja | 2-Wege (abhängig davon, wohin Sie senden) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile |
| ---- |
| **Vertrautheit und Vertrauen**<br> Langcodes sehen aus wie persönliche Telefonnummern und enthalten oft eine lokale Vorwahl. Für Marken stellt dies eine Balance zwischen professioneller Präsenz und einem persönlichen, zugänglichen Gefühl dar. |
| **Größere weltweite Verfügbarkeit**<br>Langcodes sind in über 100 wichtigen Ländern weltweit verfügbar. Wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in oder den [Braze-Support]({{site.baseurl}}/braze_support) für eine Liste der verfügbaren Länder.|
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| --- |
| **Langsamere Sendegeschwindigkeiten und tägliche Nachrichtenlimits**<br> Langcodes sind nicht für „Massen“-Marketing konzipiert wie Shortcodes. Wenn Sie versuchen, einen zeitkritischen Flash-Sale an 100.000 Personen gleichzeitig von einem Langcode aus zu senden, könnte es Stunden dauern, bis alle Nachrichten zugestellt sind. In den USA können Carrier wie T-Mobile zudem tägliche Sendelimits für 10DLC basierend auf dem Vertrauens-Score Ihrer Marke festlegen. |
| **Höheres Filterrisiko**<br> Da Langcodes wie persönliche Telefonnummern aussehen, überwachen Carrier sie genau, um zu verhindern, dass „Person-zu-Person“-Nummern für Spam verwendet werden. Selbst mit einer registrierten 10DLC-Kampagne haben Sie, wenn Ihr Nachrichteninhalt zu „spamig“ ist oder strenge Formatierungsanforderungen nicht erfüllt, ein deutlich höheres Risiko, von Carriern blockiert zu werden, als mit einem vorab genehmigten Shortcode. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% tab Alphanumerische Kurzmitteilungsdienst or SMS-Sender-ID %}

#### Alphanumerische Kurzmitteilungsdienst or SMS-Sender-ID {#sms-alphanumeric-sender-id}

Eine alphanumerische Sender-ID (oft „Alpha“ genannt) ist ein erkennbarer String aus einer beliebigen Kombination von Buchstaben und Zahlen (häufig Ihr Firmen- oder Markenname), der als Sender-ID für einseitigen Textversand angezeigt wird.

Sie kann bis zu 11 Zeichen haben und Groß- (A–Z) und Kleinbuchstaben (a–z), Leerzeichen und Ziffern (0–9) enthalten. Sie darf **nicht** ausschließlich aus Zahlen bestehen.

##### Details

| Länge | Zugang | Durchsatz | MMS-fähig | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| Bis zu 11 Zeichen | Sofort verfügbar, wenn keine Vorregistrierung erforderlich ist. Andernfalls 1–4 Wochen in den meisten Ländern, in denen eine Registrierung erforderlich ist. | Variiert je nach Land | Nein | 1-Weg |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile | Nachteile |
| ---- | ---- |
| {::nomarkdown} <ul><li> Verbesserte Markenwiedererkennung </li><li> In vielen internationalen Märkten Registrierung or registrieren und prüfen lokale Carrier alphanumerische Sender vorab, sodass Ihre Nachrichten weniger wahrscheinlich in aggressiven Carrier-Spam-Filtern hängen bleiben, die andernfalls zufällige Langcodes blockieren könnten </li><li> Verfügbar innerhalb einer Woche, wenn keine Vorregistrierung erforderlich ist </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling#two-way-messaging-custom-keyword-responses'>Zwei-Wege-Messaging</a> wird nicht unterstützt </li><li> Nicht alle Länder unterstützen dieses Feature. Es wird beispielsweise in Großbritannien unterstützt, ist jedoch in den USA blockiert. </li><li> Einige Länder haben einen umfangreichen Vorregistrierungsprozess, der die Einreichung rechtlicher Dokumente und längere Vorlaufzeiten erfordert. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vor- und Nachteile" }

Für weitere Informationen zu alphanumerischen Sender-IDs wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in.
{% endtab %}
{% tab Gebührenfreie Kurzmitteilungsdienst or SMS-Nummern %}

#### Kurzmitteilungsdienst or SMS-fähige gebührenfreie Nummern {#sms-enabled-toll-free-numbers}

Gebührenfreie Nummern haben eine eigene dreistellige Vorwahl (z. B. 800, 888, 877 und 866), über die Nutzer:innen Unternehmen kostenlos erreichen können. Sie werden häufig für den Kundendienst eingesetzt und können auch alle Arten von A2P-Messaging (Application-to-Person) abwickeln, einschließlich Marketing.

##### Details

| Länge | Zugang | Durchsatz | MMS-fähig | 1-Weg vs. 2-Wege |
| --- | --- | --- | --- | --- |
| 10 Ziffern | 2–4 Wochen Beantragung | Beginnt bei 3 MPS or Messages pro Sekunde (Segmente pro Sekunde), kann gegen zusätzliche Gebühren erhöht werden | Ja | 2-Wege |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Details" }

##### Vor- und Nachteile

| Vorteile |
| ---- |
| **Professionelles Image**<br> Gebührenfreie Nummern sind in Nordamerika für die geschäftliche Kommunikation weithin anerkannt und vertrauenswürdig und verleihen einen professionellen und seriösen Eindruck. |
| **Flexibler Durchsatz; keine Carrier-Sendelimits**<br> Im Gegensatz zu Standard-Langcodes, die je nach Land Durchsatz- oder Carrier-Sendelimits haben können, kann der Durchsatz gebührenfreier Nummern erhöht werden, um höhere Volumina zu unterstützen. Zudem gibt es in den USA keine täglichen Carrier-Sendelimits.|
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

| Nachteile |
| --- |
| **Unpersönlich und geografisch neutral**<br> Da gebührenfreie Nummern keine lokale Vorwahl haben, können sie zu „geschäftsmäßig“ oder anonym wirken. Für ein lokales Dienstleistungsunternehmen kann eine gebührenfreie Nummer schlechter abschneiden als ein Standard-Langcode, da ihr die lokale Verbundenheit fehlt und sie manchmal mit einer zufälligen Telemarketing-Leitung verwechselt werden kann. |
| **Zusätzliche STOP-Filterschicht**<br> Gebührenfreie Nummern haben eine Opt-out-Verarbeitungsschicht außerhalb von Braze, die nicht entfernt oder angepasst werden kann. Wenn Nutzer:innen „STOP“ an Ihre gebührenfreie Nummer senden, werden sie vom weiteren Nachrichtenempfang über Ihre Nummer abgemeldet und erhalten eine netzwerkseitig generierte automatische Antwort. Sie erhalten keine weiteren Nachrichten von Ihrer gebührenfreien Nummer, bis sie „START“ senden, um von der Sperrliste der gebührenfreien Nummer entfernt zu werden. |
{: .reset-td-br-1 aria-label="Vor- und Nachteile" }

{% endtab %}
{% endtabs %}

## Kurzcodes und Langcodes gemeinsam verwenden {#using-short-codes-and-long-codes-together}

Wenn Ihre Abo-Gruppe sowohl Shortcodes als auch Langcodes umfasst, werden Shortcodes in der Regel für ausgehende Nachrichten priorisiert. Einige Anbieter bieten jedoch eine Sticky-Sender-Funktionalität an, die dazu führen kann, dass ein Langcode für bestimmte Nutzer:innen weiterhin verwendet wird, auch nachdem ein Shortcode zum Senderpool hinzugefügt wurde.

Sticky Sender sorgt für Nachrichtenkontinuität, indem alle Nachrichten an eine bestimmte Person von derselben Telefonnummer gesendet werden. Wenn eine Person eine Nachricht von einem Langcode erhalten hat, bevor ein Shortcode zu Ihrer Abo-Gruppe hinzugefügt wurde, kann Ihr Anbieter diesen Langcode für zukünftige Nachrichten an diese Person weiterhin verwenden, obwohl der Shortcode normalerweise priorisiert würde.

Dieses Verhalten wird von den Anbietern gesteuert und kann in Braze nicht geändert werden.

## Einrichtung {#setup}

Die Anforderungen und Zeitrahmen für die Einrichtung variieren je nach Absendertyp und dem Land, in dem der Absender bereitgestellt wird.

{% tabs local %}
{% tab RCS-verifizierter Absender %}

### RCS-verifizierter Absender

RCS-verifizierte Absender werden länderspezifisch bereitgestellt. Der Verifizierungs- und Einrichtungsprozess konzentriert sich auf Ihren Agenten oder Absender – die digitale Persona, die mit Nutzer:innen interagiert. Sie stellen Marken-Assets und Verifizierungsdetails bereit.

#### Marken-Assets {#brand-assets}

- **Verifizierter Name:** Der Name, den Nutzer:innen oben im Nachrichtenthread sehen. Es sollte ein wiedererkennbarer Handelsname sein, nicht unbedingt Ihr rechtlicher Firmenname.
- **Logo:** Ein hochauflösendes Bild mit 224x224 px. Es wird in einem kreisförmigen Rahmen angezeigt, daher sollten wichtige Elemente zentriert sein.
- **Banner (Hero-Bild):** Ein Hintergrundbild für Ihre Geschäftsprofilkarte (ähnlich einem Facebook- oder LinkedIn-Titelbild).
- **Markenfarbe:** Ein Hex-Wert für die Buttons und UI-Elemente, passend zum Styling Ihres Unternehmens.

#### Verifizierungsdetails {#verification-details}

- **Ansprechperson (POC):** Dies ist entscheidend. Sie müssen eine E-Mail-Adresse einer direkten Mitarbeiterin oder eines direkten Mitarbeiters der Marke angeben (keine Agentur-E-Mail). Google oder der Carrier wird diese Person per E-Mail kontaktieren, um zu bestätigen, dass sie Braze autorisiert hat, in Ihrem Namen zu handeln.
- **Website und Datenschutzrichtlinie:** Eine aktive Website und eine Datenschutzrichtlinie, die erklärt, wie Sie Nutzerdaten und Messaging handhaben.
- **Anwendungsfallbeschreibung:** Eine klare Erklärung, was Sie senden (zum Beispiel „Bestellstatusbenachrichtigungen und Kundensupport für Einzelhandelskäufe“).

Die Zeitrahmen für RCS variieren je nach Land und mit zunehmender Einführung des Kanals durch weitere Carrier. Derzeit können Sie damit rechnen, dass ein RCS-Absender innerhalb von 3–6 Wochen nach der Startanfrage von den Carriern genehmigt wird.

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS-Shortcodes %}

### Kurzmitteilungsdienst or SMS-Shortcodes

Shortcodes werden länderspezifisch bereitgestellt. Je nach Land ist der Shortcode-Antragsprozess dafür bekannt, unvorhersehbar zu sein. Braze unterstützt Sie bei jedem Schritt. Wenn Sie einen Shortcode möchten, wenden Sie sich an Ihren Onboarding-Manager:in oder eine andere Braze-Vertretung.

Braze hilft Ihnen bei der Zusammenstellung aller Materialien und Informationen, die für die Einreichung eines Antrags und die Konfiguration eines neuen Shortcodes erforderlich sind. Die Anforderungen variieren je nach Land, aber viele erfordern mindestens Folgendes:

| Antragsmaterial | Beschreibung | Anforderungen |
|----------------------|----------------|-----------------|
| Call-to-Action (Opt-in) | Der Hauptzweck der Offenlegungen besteht darin, zu bestätigen, dass Nutzer:innen dem Empfang von Textnachrichten zustimmen und die Art des Programms verstehen. | {::nomarkdown}<ul><li>Produktbeschreibung</li><li>Offenlegung der Nachrichtenhäufigkeit</li><li>Vollständige Geschäftsbedingungen ODER Link zu vollständigen Geschäftsbedingungen</li><li>Datenschutzrichtlinie ODER Link zur Datenschutzrichtlinie</li><li>STOP-Schlüsselwort</li><li>Hinweis „Es können Nachrichten- und Datengebühren anfallen“.</li></ul>{:/} |
| Geschäftsbedingungen | Umfassende Geschäftsbedingungen können vollständig unter dem Call-to-Action dargestellt oder über einen Link in der Nähe des Call-to-Action zugänglich gemacht werden. | {::nomarkdown}<ul><li>Programmname (Marke)</li><li>Offenlegung der Nachrichtenhäufigkeit</li><li>Produktbeschreibung</li><li>Kontaktinformationen des Kundensupports</li><li>Opt-out-Informationen</li><li>Hinweis „Es können Nachrichten- und Datengebühren anfallen“.</li></ul>{:/} |
| Nachrichtenfluss | Programme mit wiederkehrenden Nachrichten sollten das Opt-in mit einer einzelnen Textnachricht bestätigen, die ausdrücklich angibt, für welches Programm sich die Nutzer:innen angemeldet haben, und klare Opt-out-Anweisungen bereitstellen.<br><br> Braze verarbeitet Opt-in-, Opt-out- und Hilfenachrichten und aktualisiert automatisch den Status der Abo-Gruppe für die Nutzer:innen und ihre zugehörige Telefonnummer bei allen eingehenden Anfragen.<br><br> Beachten Sie, dass diese Standard-Schlüsselwörter und -Antworten auch angepasst werden können. | {::nomarkdown}<ul><li>Opt-in-Bestätigung:<ul><li>Programmname (Marke) ODER Produktbeschreibung</li><li>Opt-out-Informationen</li><li>Kontaktinformationen des Kundensupports</li><li>Offenlegung der Nachrichtenhäufigkeit</li><li>Hinweis „Es können Nachrichten- und Datengebühren anfallen“.</li></ul></li><li>HELP-Antwort:<ul><li>Programmname (Marke) ODER Produktbeschreibung</li><li>Kontaktinformationen des Kundensupports (Support-E-Mail oder Telefonnummer).</li></ul></li><li>Opt-out-Antwort (STOP):<ul><li>Programmname (Marke) ODER Produktbeschreibung</li><li>Bestätigung, dass keine weiteren Nachrichten zugestellt werden.</li></ul></li></ul>{:/} |
| Programmnachrichten | Programmnachrichten werden im normalen Verlauf des Shortcode-Programms gesendet, nachdem die Nutzer:innen eine Opt-in-Bestätigung erhalten haben. | {::nomarkdown}<ul><li>Opt-out-Anweisungen sollten in regelmäßigen Abständen und mindestens einmal pro Monat bereitgestellt werden.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kurzmitteilungsdienst or SMS-Shortcodes" }

Wenn alle Ihre Antragsmaterialien bereit sind, reicht Braze den Antrag in Ihrem Namen bei unseren Providern ein. Der Antrag wird dann von lokalen Operatoren geprüft und genehmigt, die möglicherweise zusätzliches Feedback geben oder weitere Informationen anfordern. Nachdem alle Operatoren die Genehmigung erteilt haben, können Sie den Shortcode sofort für die Nutzung in Braze konfigurieren.

Der Zeitrahmen für die Prüfung und Genehmigung von Shortcodes variiert, beträgt aber in der Regel 4–12 Wochen, abhängig vom Land und der Art des Programms.

{% alert important %}
Wenn Sie bereits über einen eigenen Shortcode verfügen, wenden Sie sich während des Onboarding-Prozesses an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in, um die Migration oder Übertragung Ihres Shortcodes zu besprechen.
{% endalert %}

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS-Langcodes und gebührenfreie Nummern %}

### Kurzmitteilungsdienst or SMS-Langcodes (10DLC) und gebührenfreie Nummern {#sms-long-codes-10dlc-and-toll-free-numbers}

In vielen Ländern hat sich die Einrichtung von Langcodes (auch als „10DLCs“ oder „10-stellige Langcodes“ bezeichnet) und gebührenfreien Nummern für den Kurzmitteilungsdienst or SMS-Versand von einem „Plug-and-Play“-Prozess zu einem regulierten Prüfsystem entwickelt. Carrier möchten genau wissen, wer Sie sind und was Sie zu sagen planen, bevor Sie senden.

Während des Einrichtungsprozesses für Langcodes können Sie damit rechnen, Details zu Ihrer Markenidentität und Ihrem Campaign-Zweck zu teilen.

#### Markenidentität {#brand-identity}

- **Name der juristischen Person:** Muss exakt mit Ihren Steuerunterlagen übereinstimmen (zum Beispiel „Acme Corp LLC“, nicht „Acme“).
- **Steuer-ID:** In den USA ist dies Ihre Arbeitgeber-Identifikationsnummer (EIN). International benötigen Sie eine Umsatzsteuer-Identifikationsnummer (USt-IdNr.) oder eine lokale Handelsregisternummer (BRN).
- **Digitale Präsenz:** Eine aktive und funktionsfähige Website. Carrier können diese überprüfen, um sicherzustellen, dass Sie kein Briefkastenunternehmen sind.
- **Autorisierte Kontaktperson:** Name, E-Mail und Telefonnummer einer für das Konto verantwortlichen Person.

#### Campaign-Zweck {#campaign-intent}

- **Anwendungsfall:** Geben Sie an, ob Sie 2FA-Codes, Terminerinnerungen, Marketing-Aktionen oder Ähnliches senden.
- **Beispielnachrichten:** Stellen Sie 2–5 Beispiele bereit, was Sie senden werden.
- **Opt-in-Nachweis:** Beschreiben Sie (und zeigen Sie oft einen Screenshot), wie sich Nutzer:innen anmelden. Beispiele sind ein Webformular mit einem Kontrollkästchen oder ein „Text START“-Schlüsselwort auf einem Plakat.

Braze arbeitet mit Ihnen zusammen, um alle erforderlichen Details für die Bereitstellung Ihres Langcodes oder Ihrer gebührenfreien Nummer zu sammeln, und reicht die Details dann bei unserem Provider zur Prüfung und Genehmigung ein. Nachdem unser Provider das Programm genehmigt hat, konfigurieren wir den Langcode oder die gebührenfreie Nummer sofort in Braze.

Der Zeitrahmen für die Einrichtung hängt vom Bereitstellungsland ab. In der Regel dauert es 1–4 Wochen, bis Langcodes und gebührenfreie Nummern genehmigt werden.

{% alert important %}
Alle Kund:innen, die derzeit US-Langcodes haben und/oder nutzen, um an US-Kund:innen zu senden, müssen ihre Langcodes Registrierung or registrieren. Weitere Informationen zu den Einzelheiten der US A2P 10DLC-Registrierung und warum sie erforderlich ist finden Sie in unserem speziellen [10DLC-Artikel]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc).
{% endalert %}

{% endtab %}
{% tab Alphanumerische Kurzmitteilungsdienst or SMS-Absender-ID %}

### Alphanumerische Kurzmitteilungsdienst or SMS-Absender-ID

Alphanumerische Absender-IDs sind stark reguliert, da sie leicht für Phishing gefälscht werden können. Während einige Länder es jedem ermöglichen, einen Namen einzurichten und von diesem zu senden, müssen Sie in vielen Ländern zunächst nachweisen, dass Sie die Marke besitzen.

Möglicherweise werden Sie aufgefordert, die folgenden Details für die Einrichtung einer alphanumerischen Absender-ID bereitzustellen.

- **Bevorzugte ID:** Ein String mit bis zu 11 Zeichen. Er muss mindestens einen Buchstaben enthalten und darf kein generisches Wort wie „BANK“ oder „INFO“ sein.
- **Nachweis der Markeninhaberschaft:** Ihre Markenurkunde oder ein Handelsregisterauszug (zum Beispiel eine innerhalb der letzten 12 Monate ausgestellte Gründungsurkunde).
- **Vollmachtsschreiben:** Ein unterschriebenes Schreiben auf Ihrem Firmenbriefkopf, das Braze und unseren Provider autorisiert, Nachrichten in Ihrem Namen unter Verwendung dieser spezifischen ID zu senden.
- **Beispiel-Nachrichtentemplates:** In mehreren Regionen müssen Sie die genauen „Templates“ der Nachrichten Registrierung or registrieren, die Sie zu senden beabsichtigen. Abweichungen in den tatsächlichen Nachrichten können in diesen Ländern zu Zustellfehlern führen.

Der Zeitrahmen für die Einrichtung einer alphanumerischen Absender-ID hängt stark davon ab, ob das Land eine „dynamische“ (sofortige, keine Registrierung erforderlich) Einrichtung erlaubt oder eine „Vorregistrierung“ erfordert. In Ländern, die eine Vorregistrierung erfordern, variiert der Einrichtungszeitrahmen, liegt aber in der Regel zwischen 1–4 Wochen.

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen {#frequently-asked-questions}

Antworten auf häufig gestellte Fragen zu Kurzmitteilungsdienst or SMS- und RCS-Sendern finden Sie auf unserer Seite [Häufig gestellte Fragen zu Kurzmitteilungsdienst or SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).