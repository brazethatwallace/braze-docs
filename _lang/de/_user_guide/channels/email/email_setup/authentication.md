---
nav_title: E-Mail-Authentifizierung
article_title: E-Mail-Authentifizierung
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die E-Mail-Authentifizierung, eine Sammlung von Techniken, die darauf abzielen, Ihre E-Mails mit überprüfbaren Informationen über ihre Herkunft auszustatten."
channel: email

---

# E-Mail-Authentifizierung {#email-authentication}

> Die E-Mail-Authentifizierung ist eine Sammlung von Techniken, die Ihre E-Mails mit überprüfbaren Informationen über ihre Herkunft ausstatten.<br><br>Eine ordnungsgemäße Authentifizierung ist entscheidend dafür, dass Internet-Provider (ISPs) Sie als Absender erwünschter E-Mails erkennen und Ihre Post sofort zustellen können. Ohne Authentifizierung werden Ihre Nachrichten als Betrugsversuche eingestuft.

{% alert note %}
Für **BIMI** (Brand Indicators for Message Identification) ist keine besondere Abstimmung mit Braze erforderlich. Die erforderlichen DNS-Einträge und Zertifikate werden auf Ihrer Seite verwaltet.
{% endalert %}

## Methoden der Authentifizierung {#methods-of-authentication}

### Sender Policy Framework (SPF) {#spf}

Diese Methode bestätigt, dass die IP-Adresse, von der aus Braze E-Mails versendet, berechtigt ist, in Ihrem Namen E-Mails zu versenden. SPF ist Ihre Basisauthentifizierung und wird durch die Veröffentlichung der Texteinträge in den DNS-Einstellungen erreicht. Der empfangende Server überprüft die DNS-Einträge und stellt fest, ob sie authentisch sind. Diese Methode dient dazu, den E-Mail-Absender zu überprüfen.

Braze richtet Ihren SPF-Eintrag ein, wenn wir Ihre IPs und Domains konfigurieren. Abgesehen vom Hinzufügen der von uns bereitgestellten DNS-Einträge sind keine weiteren Maßnahmen erforderlich.

### Domain Keys Identified Mail (DKIM) {#dkim}

Diese Methode bestätigt, dass Ihre Braze-E-Mail-Versanddomain berechtigt ist, in Ihrem Namen E-Mails zu versenden. Diese Methode dient dazu, die Authentizität des Absenders und die Integrität der Nachricht zu überprüfen. Außerdem werden individuelle kryptografische digitale Signaturen verwendet, damit ISPs sicherstellen können, dass die zugestellte E-Mail mit der von Ihnen gesendeten E-Mail übereinstimmt.

Braze signiert die E-Mail mit Ihrem geheimen Private Key. Die ISPs überprüfen die Signatur anhand Ihres Public Keys, der in Ihrem benutzerdefinierten DNS-Eintrag gespeichert ist. Keine zwei Signaturen sind exakt gleich, und nur Ihr Public Key kann die Signatur Ihres Private Keys erfolgreich verifizieren.

Braze richtet Ihren DKIM-Eintrag ein, wenn wir Ihre IPs und Domains konfigurieren. Abgesehen vom Hinzufügen der von uns bereitgestellten DNS-Einträge sind keine weiteren Maßnahmen erforderlich.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC) {#dmarc}

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) ist ein E-Mail-Authentifizierungsprotokoll für E-Mail-Absender, um die Legitimität ihrer E-Mails nachzuweisen. Es stärkt das Vertrauen der Empfänger-Postfächer und fördert die Zustellung von E-Mails. DMARC ermöglicht es E-Mail-Absendern festzulegen, wie mit E-Mails umgegangen werden soll, die nicht über Sender Policy Framework (SPF) oder Domain Keys Identified Mail (DKIM) authentifiziert wurden. Dies wird erreicht, indem überprüft wird, dass sowohl SPF- als auch DKIM-Prüfungen bestanden werden.

Absender weisen Postfach-Anbieter an, wie mit E-Mails umzugehen ist, die Signatur- oder Authentifizierungsprüfungen nicht bestehen. Fehlschläge können auf Spoofing hindeuten. Sie können Anbieter anweisen, fehlgeschlagene E-Mails abzulehnen oder in Quarantäne zu stellen und automatisierte Berichte zu senden. Dies hilft Anbietern, Spammer zu identifizieren, bösartige E-Mails zu blockieren, Fehlalarme zu minimieren und die Transparenz der Authentifizierungsberichte zu verbessern.

#### Funktionsweise {#how-it-works}

Um DMARC einzusetzen, müssen Sie einen DMARC-Eintrag in Ihrem Domain Name System (DNS) veröffentlichen. Dies ist ein TXT-Eintrag, der die Richtlinie Ihrer E-Mail-Domain nach der Prüfung des SPF- und DKIM-Status öffentlich ausdrückt. DMARC authentifiziert, wenn entweder SPF oder DKIM oder beide bestanden werden. Dies wird als DMARC Alignment bezeichnet.

Ein DMARC-Eintrag weist E-Mail-Server außerdem an, XML-Berichte an die im DMARC-Eintrag aufgeführte Berichts-E-Mail-Adresse zurückzusenden. Diese Berichte bieten Insights darüber, wie sich Ihre E-Mails durch das Ökosystem bewegen, und ermöglichen es Ihnen, alles zu identifizieren, was versucht, Ihre E-Mail-Domain zum Versand von E-Mail-Kommunikation zu nutzen.

Legen Sie eine DMARC-Richtlinie auf der Root-Domain fest, damit sie für alle Subdomains gilt. So vermeiden Sie zusätzliche Einrichtungsschritte für aktuelle und zukünftige Subdomains. Sie können eine der folgenden Richtlinien festlegen:

| Richtlinie | Auswirkung |
| --- | --- |
| None | Weist den Postfach-Anbieter an, keine Maßnahmen gegen Nachrichten zu ergreifen, die die Prüfung nicht bestehen. |
| Quarantine | Weist den Postfach-Anbieter an, Nachrichten, die die Prüfung nicht bestehen, in den Spam-Ordner zu verschieben. |
| Reject | Weist den Postfach-Anbieter an, dass Nachrichten, die die Prüfung nicht bestehen, in den Spam-Ordner verschoben und blockiert werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Funktionsweise" }

#### So überprüfen Sie die DMARC-Authentifizierung Ihrer Domain {#how-to-check-your-domains-dmarc-authentication}

Es gibt zwei Möglichkeiten, die DMARC-Authentifizierung Ihrer Domain zu überprüfen:

- **Option 1:** Sie können Ihre übergeordnete Domain oder Subdomain in einen beliebigen DMARC-Checker eines Drittanbieters eingeben, z. B. [MXToolbox](https://mxtoolbox.com/dmarc.aspx), um zu prüfen, ob eine DMARC-Richtlinie vorhanden ist und wie diese konfiguriert ist.
    - **MXToolbox**: Wenn Sie Ihren DMARC-Eintrag auf der Root-Domain festgelegt haben, geben Sie diese in MXToolbox ein. Wenn Sie den DMARC-Eintrag auf der Subdomain festgelegt haben, geben Sie die Subdomain in MXToolbox ein. Beachten Sie, dass MXToolbox bei Abfragen nicht „nach oben oder unten schaut“. Das bedeutet: Wenn Sie den DMARC-Eintrag auf der Root-Domain festgelegt haben und die Subdomain eingeben, zeigt MXToolbox einen Fehler an, da es nicht erkennt, dass der DMARC-Eintrag auf der Root-Domain gesetzt wurde.
- **Option 2:** Öffnen Sie eine E-Mail von Ihrer Domain oder Subdomain in Ihrem Postfach und suchen Sie die Originalnachricht, um zu überprüfen, ob DMARC die Authentifizierung für diese E-Mail besteht.

Wenn Sie beispielsweise Gmail verwenden, gehen Sie wie folgt vor:

1. Klicken Sie auf **Mehr** <i class="fa-solid fa-ellipsis"></i> in einer E-Mail-Nachricht.
2. Wählen Sie **Original anzeigen** aus.
3. Überprüfen Sie, ob für **DMARC** der Status „PASS“ angezeigt wird.

![Eine E-Mail, die „PASS“ als DMARC-Wert anzeigt.]({% image_buster /assets/img_archive/dmarc_example.png %})

#### Fehlerbehebung bei DMARC-Fehlschlägen {#troubleshoot-dmarc-failures}

Wenn DMARC für über Braze gesendete Nachrichten **FAIL** anzeigt:

1. Öffnen Sie die Roh-Header oder Authentifizierungsergebnisse einer kürzlich gesendeten Nachricht und prüfen Sie, ob **SPF** und **DKIM** jeweils bestanden werden oder fehlschlagen.
2. **Alignment:** DMARC wird bestanden, wenn *entweder* SPF *oder* DKIM mit der **From**-Domain übereinstimmt. Alignment bedeutet, dass die **From**-Domain mit der Domain übereinstimmt, die SPF bestanden hat (häufig die **Return-Path**- / Envelope-Domain) *oder* mit der Domain in der DKIM-**d=**-Signatur.
3. Wenn SPF bestanden wird, DMARC aber fehlschlägt, stimmt die Return-Path-Domain möglicherweise nicht mit Ihrer **From**-Domain überein – überprüfen Sie, ob Ihre [Whitelabel-Versand- und Tracking-Domains]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/) mit den Domains übereinstimmen, für die Sie SPF und DKIM veröffentlichen.
4. Wenn DKIM fehlschlägt, überprüfen Sie, ob die von Braze bereitgestellten DKIM-DNS-Einträge vorhanden und unverändert sind.

Drittanbieter-Checker (z. B. [MXToolbox](https://mxtoolbox.com/dmarc.aspx)) helfen bei der Überprüfung veröffentlichter Einträge. Validieren Sie jedoch immer auch mit einer Live-Nachricht von Braze.