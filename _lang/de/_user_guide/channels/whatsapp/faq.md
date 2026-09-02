---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von WhatsApp-Campaigns auftreten."
page_type: FAQ
channel:
  - WhatsApp

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Auf dieser Seite beantworten wir Ihre wichtigsten Fragen zu WhatsApp!<br><br>Diese FAQ sind nicht als Rechtsberatung gedacht und dürfen auch nicht als solche herangezogen werden. Die Nutzung des WhatsApp-Kanals unterliegt bestimmten Anforderungen von Meta Platforms, Inc. Um sicherzustellen, dass Sie den WhatsApp-Kanal in Übereinstimmung mit allen geltenden Anforderungen und Gesetzen nutzen, denen Sie möglicherweise unterliegen, sollten Sie den Rat Ihrer Rechtsabteilung einholen.

## FAQ-Themen {#faq-topics}
- [WhatsApp-Business-Konten](#whatsapp-business-accounts)
- [Telefonnummer des WhatsApp-Business-Kontos](#whatsapp-business-account-phone-numbers)
- [Opt-in und Abo-Management](#opt-in-and-subscription-management)
- [Messaging-Limits und Qualitätsbewertung](#messaging-limits-and-quality-rating)
- [WhatsApp-Templates und Composer](#whatsapp-templates-and-composer)
- [Zustellbarkeit und Abrechnung](#deliverability-and-billing)
- [Integrationen, Daten und Reporting](#integrations-data-and-reporting)
- [Medien und Bilder](#media-and-images)

### WhatsApp-Business-Konten {#whatsapp-business-accounts}

#### Wie erstelle ich ein WhatsApp-Business-Konto? {#how-do-i-create-a-whatsapp-business-account}
Wir empfehlen, Ihr WhatsApp-Business-Konto (WABA) über den eingebetteten Registrierungsflow im Braze-Dashboard zu erstellen.

#### Ich habe bereits ein Meta-Business-Konto. Brauche ich trotzdem ein WhatsApp-Business-Konto? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Ja, Sie müssen dennoch ein WhatsApp-Business-Konto erstellen. Wir empfehlen Ihnen, [Ihr WABA unter Ihrem Haupt-Meta-Business-Konto zu verschachteln]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### Wie greife ich auf mein WhatsApp-Business-Konto zu? {#how-do-i-access-my-whatsapp-business-account}
Nach Abschluss des eingebetteten Registrierungsflows können Sie auf Ihr Konto unter business.facebook.com zugreifen, indem Sie zum [WhatsApp-Bereich](https://business.facebook.com/wa/manage/home) navigieren.

#### Kann ich mehrere WABAs mit Braze verbinden? {#can-i-connect-multiple-wabas-to-braze}
Ja, Sie können bis zu 10 WhatsApp-Business-Konten pro Workspace hinzufügen, und jedes Business-Konto kann unter einem anderen Meta Business Manager:in verschachtelt sein.

![Diagramm des Braze- und WhatsApp-Ökosystems, das zeigt, wie Workspaces und WhatsApp-Business-Konten miteinander verbunden sind: Sie können eine Abo-Gruppe mit einer Telefonnummer, mehrere WhatsApp-Business-Konten mit einem Workspace und einen Workspace mit mehreren Meta-Business-Portfolios verbinden.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### Kann ich die Währung meines WhatsApp-Business-Kontos ändern? {#can-i-change-my-whatsapp-business-account-currency}
Nein. Meta steuert die Währung für Ihr WhatsApp-Business-Konto, und Braze kann diese nicht ändern oder konvertieren. Um eine andere Währung zu verwenden, [erstellen Sie ein separates WhatsApp-Business-Konto]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) mit dieser Währung, oder kontaktieren Sie den Meta-Support, um zu fragen, ob die Währung Ihres bestehenden Kontos aktualisiert werden kann.

#### Was ist die Geschäftsverifizierung? {#what-is-business-verification}
Die Geschäftsverifizierung ist ein WhatsApp-Konzept, das sicherstellt, dass die Marke ein legitimiertes Unternehmen ist. Sie kann im WhatsApp Manager:in abgeschlossen werden. Die Geschäftsverifizierung ist auch erforderlich, um das Messaging zu skalieren. Ohne Geschäftsverifizierung können Kund:innen nur bis zu 250 eindeutigen Endnutzer:innen in einem rollierenden 24-Stunden-Zeitraum Nachrichten senden.

#### Was ist ein offizielles Business-Konto? {#what-is-an-official-business-account}
Ein OBA verleiht Ihnen das grüne Häkchen neben Ihrem Anzeigenamen und ist optional. Sie können ein offizielles Business-Konto beantragen, nachdem Sie die Geschäftsverifizierung abgeschlossen haben. Beachten Sie, dass die Geschäftsverifizierung und ein offizielles Business-Konto unterschiedliche WhatsApp-Konzepte sind.

#### Warum könnte mein WhatsApp-Business-Anzeigename abgelehnt werden? {#why-might-my-whatsapp-business-display-name-be-rejected}
Ablehnungen von WhatsApp-Business-Anzeigenamen unterliegen den Regeln von Meta. Wenn Ihr Anzeigename abgelehnt wird, lesen Sie die [Richtlinien für Anzeigenamen von WhatsApp](https://faq.whatsapp.com/793641088597363).

Wenn Ihr Anzeigename die Richtlinien erfüllt und dennoch abgelehnt wird, kann Braze die spezifischen Gründe nicht einsehen. Der häufigste Grund für eine Ablehnung ist jedoch, dass die Online-Präsenz eines Unternehmens zu gering ist oder das Unternehmen [regulierte oder eingeschränkte Produkte](https://business.whatsapp.com/policy#further-guidance) vermarktet.

Weitere Hinweise zu Ablehnungen von Anzeigenamen finden Sie unter [Meta-Ressourcen]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources).

### Telefonnummer des WhatsApp-Business-Kontos {#whatsapp-business-account-phone-numbers}
#### Benötige ich eine Telefonnummer für mein WhatsApp-Business-Konto? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Ja, Sie benötigen eine Nummer, auf die Sie Zugriff haben. Sie werden aufgefordert, Ihre Telefonnummer per Zwei-Faktor-Authentifizierung zu verifizieren, wenn Sie den eingebetteten Registrierungsflow durchlaufen. Die Telefonnummer kann nicht für andere WhatsApp-Konten (geschäftlich oder privat) verwendet werden.

#### Welche Arten von Telefonnummern werden von WhatsApp unterstützt? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Weitere Informationen finden Sie in den Meta-Anforderungen für [Telefonnummern](https://developers.facebook.com/docs/whatsapp/phone-numbers).

#### Kann ich eine Telefonnummer für mehrere WABAs verwenden? {#can-i-use-one-phone-number-across-multiple-wabas}
Nein. Eine Telefonnummer kann nicht über mehrere WABAs hinweg geteilt werden.

#### Benötige ich eine bestimmte Art von Telefonnummer, um Nachrichten in bestimmte Länder zu senden? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
Nein. WhatsApp ermöglicht es Ihnen, Nachrichten an Endnutzer:innen von jeder unterstützten Telefonnummer in jedem Land zu senden. Weitere Informationen finden Sie in den Meta-Anforderungen für [Telefonnummern](https://developers.facebook.com/docs/whatsapp/phone-numbers).

#### Wie müssen Telefonnummern von Nutzer:innen in Braze gespeichert werden? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Telefonnummern von Nutzer:innen müssen im [E.164-Format]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting) gespeichert werden.

#### Kann ich Telefonnummern von Nutzer:innen importieren? {#can-i-import-user-phone-numbers}
Ja. Sie können [Telefonnummern von Nutzer:innen importieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

### Opt-in und Abo-Management {#opt-in-and-subscription-management}

#### Muss ich ein Opt-in einholen, um Marketing-Nachrichten an Endnutzer:innen auf WhatsApp zu senden? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Ja, WhatsApp verlangt von Unternehmen, dass sie eine [Opt-in-Zustimmung einholen](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/), um Marketing-Nachrichten an Endnutzer:innen zu senden.

#### Kann ich Endnutzer:innen proaktiv auf WhatsApp anschreiben, um eine Opt-in-Zustimmung einzuholen? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Wenn Sie Endnutzer:innen proaktiv anschreiben, sollte Ihre erste geschäftsinitiierte Nachricht fragen, ob die Person Marketing-Nachrichten von Ihrem Unternehmen erhalten möchte, und den Meta-Anforderungen für [Opt-in einholen](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) entsprechen. Beachten Sie, dass WhatsApp die Reputation Ihres Unternehmens auf dem Kanal überwacht. Die empfohlene Best Practice ist daher, gegenüber Endnutzer:innen transparent zu sein und nur Nachrichten zu senden, die sie auch erhalten möchten.

#### Muss ich die Telefonnummer der Endnutzer:innen erheben, wenn ich das Opt-in einholen? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Sie benötigen die Telefonnummer der Endnutzer:innen im Braze-Profil, um ihnen Nachrichten senden zu können.
- Wenn Sie die Nummer bereits haben, müssen Sie sie beim Opt-in nicht erneut erheben.
- Wenn Sie die Nummer der Endnutzer:innen nicht haben, sollte Ihre Opt-in-Methode die Erfassung der Telefonnummer beinhalten.

#### Wie aktualisiere ich den Abo-Status von Endnutzer:innen, die sich angemeldet haben? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
Das Abo-Management des WhatsApp-Kanals funktioniert ähnlich wie bei anderen Braze-Kanälen. Weitere Informationen finden Sie unter [Nutzer-Abos verwalten]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

#### Wenn ich bereits eine Liste von Nutzer:innen habe, die dem Empfang von Marketing-Nachrichten auf WhatsApp zugestimmt haben – wie aktualisiere ich ihren Abo-Status in Braze? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Sie können den Abo-Status über den [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional) aktualisieren.

#### Welche Methoden sollte ich verwenden, um Opt-ins zu sammeln? {#what-methods-should-i-use-to-collect-opt-ins}
Braze empfiehlt, sich an die [Meta-Richtlinien für Opt-in-Methoden](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) zu halten, um die Compliance zu wahren. Weitere Informationen zu Canvas- und Campaign-Einrichtungsmethoden finden Sie unter [Opt-in und Opt-out]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

#### Ist ein Double-Opt-in für WhatsApp erforderlich? {#is-double-opt-in-required-for-whatsapp}
Nein, ein Double-Opt-in ist nicht erforderlich.

#### Wie melden sich meine Nutzer:innen von WhatsApp-Nachrichten ab? {#how-do-my-users-opt-out-of-whatsapp-messages}
Ihre Nutzer:innen können sich auf zwei Arten abmelden:
1. Richten Sie eine eingehende WhatsApp-Nachricht mit einem bestimmten Abmelde-Stichwort ein und verwenden Sie einen Webhook, um den Abo-Status der Nutzer:innen zu aktualisieren.
2. Fügen Sie eine Schnellantwort zur Abmeldung innerhalb des WhatsApp-Templates hinzu, zusammen mit einem entsprechenden Webhook zur Aktualisierung.

#### Kann ich eine Braze WhatsApp-Abo-Gruppe verwenden, wenn ich WhatsApp-Nachrichten über einen Drittanbieter sende? {#can-i-use-a-braze-whatsapp-subscription-group-if-i-send-whatsapp-messages-through-a-third-party}
Nein. Braze WhatsApp-Abo-Gruppen gelten für Nachrichten, die über den Braze-WhatsApp-Kanal gesendet werden. Wenn Sie WhatsApp-Nachrichten über einen Drittanbieter oder benutzerdefinierte Integrationen außerhalb von Braze WhatsApp-Campaigns und Canvases senden, können Sie die Opt-in-Zustimmung in einem angepassten Attribut (oder Ihrem eigenen Abo-Modell) speichern und dieses Attribut für die Segmentierung und Berechtigung verwenden. Verwandte Muster, wenn Braze die WhatsApp-Nummer besitzt, finden Sie unter [Wie verbinde ich WhatsApp-Support und -Marketing in Braze?](#how-do-i-connect-whatsapp-support-and-marketing-in-braze).

### Messaging-Limits und Qualitätsbewertung {#messaging-limits-and-quality-rating}

#### Was sind Messaging-Limits? {#what-are-messaging-limits}
Messaging-Limits sind ein WhatsApp-Konzept zur Integritätssicherung. Sie legen die maximale Anzahl geschäftsinitiierter Konversationen fest, die jede Telefonnummer in einem rollierenden 24-Stunden-Zeitraum starten kann. Es gibt vier Messaging-Limit-Stufen: 1.000, 10.000, 100.000 und unbegrenzt.

#### Wie erhöhe ich mein Messaging-Limit? {#how-do-i-increase-my-messaging-limit}
WhatsApp erhöht Ihr Messaging-Limit, wenn Sie die folgenden Bedingungen erfüllen:
1. Der [Telefonnummern-Status](https://www.facebook.com/business/help/896873687365001) ist **Connected**
2. Die [Qualitätsbewertung der Telefonnummer](https://www.facebook.com/business/help/896873687365001) ist **Medium** oder **High**
3. In den letzten sieben Tagen haben Sie X oder mehr Konversationen mit eindeutigen Nutzer:innen initiiert, wobei X Ihr aktuelles Messaging-Limit geteilt durch 2 ist

Um also von 100.000 auf unbegrenzt zu wechseln, müssen Sie mindestens 50.000 geschäftsinitiierte Konversationen in einem Zeitraum von 7 Tagen senden.

#### Wie lange dauert es, mein Messaging-Limit zu erhöhen? {#how-long-does-it-take-to-increase-my-messaging-limits}
Wenn alle oben genannten Bedingungen erfüllt sind, können Sie Ihr Messaging-Limit in 4 Tagen von 1.000 auf unbegrenzt erhöhen.

#### Wo kann ich mein aktuelles Messaging-Limit einsehen? {#where-can-i-see-my-current-messaging-limit}
Sie können Ihr aktuelles Messaging-Limit im Tab **WhatsApp Manager:in > Overview Dashboard > Insights** einsehen.

#### Was passiert, wenn ich versuche, Nachrichten zu senden, obwohl ich mein Messaging-Limit bereits erreicht habe? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Wenn Sie versuchen, eine Campaign oder ein Canvas an mehr eindeutige Nutzer:innen zu senden, als Ihr aktuelles Limit zulässt, werden die Nachrichten nicht zugestellt. Braze versucht weiterhin, die Nachrichten erneut zu senden, wenn/falls Ihr Messaging-Limit innerhalb von bis zu einem Tag erhöht wird.

#### Kann mein Messaging-Limit sinken? {#can-my-messaging-limit-decrease}
Ja, wenn Ihre Qualitätsbewertung der Telefonnummer zu stark sinkt, riskieren Sie, dass WhatsApp Ihr Messaging-Limit verringert. Braze empfiehlt, qualitätsbezogene Updates von WhatsApp zu abonnieren und sich benachrichtigen zu lassen, einschließlich Aktualisierungen Ihres Telefonnummern-Status und Ihres Messaging-Limit-Levels. Sie können Benachrichtigungen direkt im WhatsApp Manager:in-Dashboard abonnieren.

#### Welche Faktoren beeinflussen die Qualitätsbewertung der Telefonnummer und was passiert, wenn meine Qualitätsbewertung zu niedrig wird? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Faktoren, die die Qualitätsbewertung der Telefonnummer beeinflussen, umfassen das Blockieren eines Unternehmens durch Endnutzer:innen (und die Gründe, die sie beim Blockieren angeben) sowie das Melden eines Unternehmens durch Endnutzer:innen.

Wenn die Qualitätsbewertung niedrig ist, ändert sich der Telefonnummern-Status von **Connected** zu **Flagged**. Wenn sich die Qualität innerhalb von sieben Tagen nicht verbessert, kehrt der Status zu **Connected** zurück. Allerdings sinkt das Messaging-Limit auf die nächstniedrigere Stufe. Zum Beispiel hat eine Telefonnummer, die zuvor ein Messaging-Limit von 100.000 hatte, jetzt ein Messaging-Limit von 10.000.

#### Was ist das Meta-Durchsatzlimit? {#what-is-the-meta-throughput-limit}
Meta hat ein eigenes Durchsatzlimit, das vom WABA-Messaging-Limit getrennt ist. Das Standardlimit, das die Cloud-API unterstützt, beträgt 80 Nachrichten pro Sekunde. Wenn Sie der Meinung sind, dass Ihre Campaigns dieses Limit überschreiten könnten, können Sie [eine Erhöhung Ihres Limits beantragen](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput). Meta empfiehlt, diesen Antrag mindestens drei Tage vor dem Campaign-Versand einzureichen.

### WhatsApp-Templates und Composer {#whatsapp-templates-and-composer}

#### Was ist ein WhatsApp-Template? {#what-is-a-whatsapp-template}
WhatsApp verlangt, dass alle geschäftsinitiierten Nachrichten mit einem genehmigten Template beginnen. Das Template enthält den Nachrichtentext sowie optionale Rich-Media-Elemente wie Bilder, Calls-to-Action und Schnellantwort-Buttons. Nachdem WhatsApp Templates genehmigt hat, können sie zum Erstellen einer WhatsApp-Nachricht in Braze verwendet werden.

#### Wo erstelle, bearbeite und verwalte ich meine WhatsApp-Templates? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Sie können Templates in Braze mit dem [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder) erstellen und einreichen, oder im WhatsApp Manager:in von Meta. Templates, die an einem der beiden Orte erstellt wurden, erscheinen im Braze-Dashboard mit einer Statusanzeige. Nach der Einreichung erfordern gesperrte Felder eine erneute Genehmigung durch Meta – weitere Details finden Sie unter den [Bearbeitungsbeschränkungen in den Template-Builder-FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder#can-i-edit-a-template-after-its-been-approved).

#### Wie lange dauert es, bis WhatsApp eine Template-Einreichung überprüft? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
Der Genehmigungsprozess kann bis zu 24 Stunden dauern, aber oft werden Templates innerhalb von Stunden oder Minuten bearbeitet.

#### Wie viele Templates kann ich gleichzeitig haben? {#how-many-templates-can-i-have-at-a-given-time}
Ihr Nachrichtentemplate-Limit hängt von Ihrem Geschäftsverifizierungsstatus ab. Sie können Ihr Limit auf der Seite **WhatsApp Manager:in > Message Templates** überprüfen.

#### Wie personalisiere ich Template-Text und Rich-Media in Braze? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp erlaubt das Einfügen variabler Parameter in Nachrichtentemplates. Nachrichten können nicht mit einem variablen Parameter beginnen oder enden. Variable Parameter können mit Liquid-Logik in der Braze-Plattform befüllt werden. Weitere Informationen zu variablen Parametern finden Sie unter [WhatsApp-Nachricht in Braze verfassen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message).

#### Mein Template wurde abgelehnt. Kann Braze mir helfen, es genehmigen zu lassen? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
Das Braze-Team hat keinen Einblick in Template-Ablehnungen. Sie sollten direkt mit Ihrem WhatsApp Business Manager:in zusammenarbeiten, um das Template zu bearbeiten und erneut einzureichen. Stellen Sie sicher, dass Sie bei Bedarf ein Muster-Template bereitstellen. Überprüfen Sie, ob Ihr Template den [Business-](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) oder [Commerce-Richtlinien](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) von Meta entspricht.

#### Können Rich-Media in Braze zielgerichtet oder personalisiert werden? {#can-rich-media-be-targeted-or-personalized-in-braze}
Ja. Sie können statische Bilder aus der Medienbibliothek hochladen oder Bilder per URL hinzufügen und diese mit [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) oder [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) personalisieren. Bild-URLs unterstützen die vollständige Liquid-Logik an jeder Stelle der URL. Dies gilt für Template-Nachrichten und Antwortnachrichten (Mediennachrichten und Schnellantwort-Layouts). Weitere Details finden Sie unter [Dynamische Bilder]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#dynamic-images).

#### Welche Art von Rich-Media wird in WhatsApp-Templates unterstützt? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Sie können Bilder, Calls-to-Action (URL oder Telefonnummer) und Schnellantwort-Buttons zu WhatsApp-Templates hinzufügen. Sie können diese Elemente hinzufügen, wenn Sie Templates direkt in WhatsApp erstellen.

#### Was ist, wenn mein Template fälschlicherweise als Verstoß gegen die WhatsApp-Commerce-Richtlinie gekennzeichnet wurde? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Wenn Sie glauben, dass Meta Ihr Template fälschlicherweise gekennzeichnet hat, nutzen Sie den Überprüfungslink in der E-Mail von WhatsApp, um eine erneute Überprüfung anzufordern. Das WhatsApp-Business-Team überprüft die Entscheidung und hebt sie gegebenenfalls auf.

#### Warum zeigt mein importiertes WhatsApp-Template „Message Incomplete“ im Composer an? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
Die Warnung „Message Incomplete“ erscheint, wenn erforderliche Template-Variablenplätze im Composer nicht mit gültigen Werten befüllt sind.

Wenn Sie Templates mit dem [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder) erstellen, nummeriert Braze die Variablen in sequenzielle Platzhalter um ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %} usw.). Templates, die extern im WhatsApp Manager:in von Meta erstellt wurden, können noch Muster enthalten, die die Variablenzuordnung fehleranfällig machen, wie zum Beispiel:

- Nicht-sequenzielle Nummerierung (z. B. {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Fehlende Variablen in der Sequenz (z. B. Überspringen von {% raw %}`{{2}}`{% endraw %})
- Variablen, die mit einer anderen Nummer als 1 beginnen

Um dies zu lösen, bearbeiten Sie Ihr Template im WhatsApp Manager:in von Meta, um sequenzielle Platzhalterformatierung zu verwenden, und importieren Sie es dann erneut in Braze. Bestätigen Sie in Braze, dass jedes erforderliche Variablenfeld mit einem gültigen Liquid-Wert befüllt ist.

#### Warum wird meine WhatsApp-Campaign nicht gesendet, obwohl die Template-Vorschau funktioniert? {#why-is-my-whatsapp-campaign-not-sending-despite-template-previewing}
Wenn Ihr Template korrekt in der Vorschau angezeigt wird, aber das Verarbeitungsprotokoll **Abort** mit dem Detail „Param text cannot have new-line/tab characters or more than 4 consecutive spaces“ anzeigt, überprüfen Sie die per Liquid befüllten Parameterwerte in Ihrer Nachricht. WhatsApp verlangt, dass Parametertextwerte Folgendes nicht enthalten:

- Zeilenumbruchzeichen
- Tabulatorzeichen
- Mehr als 4 aufeinanderfolgende Leerzeichen

Stellen Sie sicher, dass jede Liquid-Logik, die Template-Parameter befüllt, diese Zeichen entfernt oder den Text entsprechend formatiert, bevor die Nachricht gesendet wird.

### Zustellbarkeit und Abrechnung {#deliverability-and-billing}

#### Warum könnte eine Nachricht nicht zugestellt werden? {#why-would-a-message-not-be-delivered}
Es gibt verschiedene Gründe, warum eine Nachricht nicht zugestellt werden könnte, darunter Netzwerkprobleme und ein ausgeschaltetes Gerät.

#### Werde ich berechnet, wenn eine Nachricht nicht zugestellt wird? {#if-a-message-is-not-delivered-will-i-be-billed}
Nein. Wenn eine Nachricht nicht zugestellt wird, werden Ihnen keine Kosten berechnet.

#### Was passiert, wenn ein:e Nutzer:in mein Unternehmen blockiert? {#what-happens-if-a-user-blocks-my-business}
Wenn ein:e Nutzer:in Ihr Unternehmen blockiert, werden nachfolgende Nachrichten, die Sie zu senden versuchen, nicht zugestellt, und Ihnen werden keine Kosten berechnet. Der Abo-Status der Person wird nicht aktualisiert.

#### Was passiert, wenn ein:e Nutzer:in eine Nachricht meldet? {#what-happens-if-a-user-reports-a-message}
Wenn ein:e Nutzer:in eine Nachricht meldet, können Sie weiterhin Nachrichten an die Person senden. Allerdings kann die Meldung Ihre Qualitätsbewertung auf dem Kanal beeinflussen. Der Abo-Status der Person wird nicht aktualisiert.

#### Wie kann ich Nutzer:innen, die mein WhatsApp-Konto melden, von kommenden Versendungen ausschließen? {#how-can-i-exclude-users-who-report-my-whatsapp-account-from-upcoming-launches}
Braze erhält keine Benachrichtigungen von WhatsApp, wenn Ihr Konto gekennzeichnet oder gemeldet wird. Daher können Sie diese Nutzer:innen nicht automatisch in Braze identifizieren oder ausschließen. Nutzer:innen, die Ihr Konto melden, können in Ihrer WhatsApp-Abo-Gruppe verbleiben und weiterhin für zukünftige Nachrichten berechtigt sein.

Sie können jedoch eine Campaign einrichten, die ausgelöst wird, wenn ein:e Nutzer:in mit einem Abmelde-Stichwort antwortet, wodurch die Person automatisch über den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) abgemeldet wird. Weitere Informationen finden Sie unter [WhatsApp Opt-in- und Opt-out-Prozess]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

#### Unterstützt Braze einen automatischen SMS-Fallback, wenn die WhatsApp-Zustellung fehlschlägt? {#does-braze-support-automatic-sms-fallback-when-whatsapp-delivery-fails}

Nein. Braze bietet keinen nativen WhatsApp-zu-SMS-Fallback-Pfad an. Um es über einen anderen Kanal erneut zu versuchen, segmentieren Sie Nutzer:innen mit fehlgeschlagenen WhatsApp-Sendungen (z. B. über Currents-Fehlerereignisse) und erstellen Sie eine SMS- oder E-Mail-Campaign für diese Zielgruppe.

#### Sind WhatsApp-Antwortnachrichten kostenlos? {#are-whatsapp-response-messages-free}

Antwortnachrichten, die im Braze-Campaign- oder Canvas-Editor verfasst werden (keine genehmigten WhatsApp-Templates), werden von Meta als Servicenachrichten behandelt. Bis zum 30. September 2026 verbrauchen Servicenachrichten, die über die native WhatsApp-Integration von Braze gesendet werden, keine Action Credits, wenn sie als [Antwortnachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) innerhalb eines offenen Kundenservice-Fensters gesendet werden.

Ab dem 1. Oktober 2026 verbrauchen Servicenachrichten Action Credits pro zugestellter Nachricht. Diese Klassifizierung hängt von der Nachricht selbst ab: Eine nicht-templatebasierte Antwort ist eine Servicenachricht, auch wenn die Konversation mit einem Template begonnen wurde. Wenn Sie mit einem genehmigten Marketing-, Utility- oder Authentifizierungs-Template antworten, wird die Nachricht gemäß ihrer Template-Kategorie abgerechnet.

| Nachrichtentyp | Action Credits | Hinweise |
|---|---|---|
| Antwortnachricht (eingehende Antwort) | Kein Verbrauch bis 30. September 2026; Verbrauch ab 1. Oktober 2026 | Wird in Braze verfasst; kein von Meta genehmigtes Template. Meta klassifiziert sie als Servicenachricht. |
| Template-Nachricht | Wird verbraucht | Marketing-, Utility-, Authentifizierungs- und zeitlich begrenzte Angebots-Templates werden pro Versand abgerechnet. |
| Utility-Template im Servicefenster | Keine Berechnung durch Meta bis 30. September 2026; Berechnung ab 1. Oktober 2026 | Der Action-Credit-Verbrauch richtet sich nach Ihrem Vertrag. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Action Credits für Antwortnachrichten" }

Für Canvas-Flows, bei denen Nutzer:innen nach dem ursprünglichen 24-Stunden-Fenster auf Schnellantworten tippen, siehe [Schnellantworten und eingehende Nachrichten außerhalb des 24-Stunden-Fensters]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Was passiert, wenn ein:e Nutzer:in nach Ablauf des 24-Stunden-Fensters antwortet oder auf eine Schnellantwort tippt? {#what-happens-if-a-user-replies-or-taps-a-quick-reply-after-the-24-hour-window-closes}
Ein neues 24-Stunden-Kundenservice-Fenster wird geöffnet. Siehe [Schnellantworten und eingehende Nachrichten außerhalb des 24-Stunden-Fensters]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Muss ich die Dauer meines Canvas-Aktionspfads auf 31 Tage für WhatsApp-Schnellantworten einstellen? {#do-i-need-to-set-my-canvas-action-path-to-31-days-for-whatsapp-quick-replies}
Nein. Die Standard-Aktionspfad-Dauer ist ausreichend. Siehe [Schnellantworten und eingehende Nachrichten außerhalb des 24-Stunden-Fensters]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Kann ich sehen, wie viele WhatsApp-Credits eine bestimmte Campaign oder ein Canvas verbraucht hat? {#can-i-see-how-many-whatsapp-credits-a-specific-campaign-or-canvas-consumed}
Derzeit nicht im Braze-Dashboard. Campaign- und Canvas-Analytics zeigen Sendungen, Zustellungen und Fehler an, aber keinen Credit-Verbrauch pro Nachricht. Sendezahlen stimmen nicht eins-zu-eins mit dem Credit-Verbrauch überein, da Template-Kategorie und Nachrichtentyp die Abrechnung unterschiedlich beeinflussen. Details zur Abrechnung finden Sie unter [Sind WhatsApp-Antwortnachrichten kostenlos?](#are-whatsapp-response-messages-free).

### Integrationen, Daten und Reporting {#integrations-data-and-reporting}

#### Warum wird WhatsApp nicht unter Technologie-Partner aufgeführt? {#why-isnt-whatsapp-listed-under-technology-partners}
WhatsApp erscheint auf der Seite **Technologie-Partner**, wenn WhatsApp für Ihr Unternehmen aktiviert ist. Wenn Sie WhatsApp auf dieser Seite nicht sehen, kontaktieren Sie Ihr Braze-Kontoteam, um zu bestätigen, dass WhatsApp für Ihr Dashboard bereitgestellt wurde.

#### Unterstützt Braze Kundenservice-Anwendungsfälle wie Chatbots und menschenunterstützten Chat für WhatsApp? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Wir unterstützen keine Chatbots oder menschenunterstützten Chat innerhalb von Braze oder über direkte Integrationen.

Wenn Sie WhatsApp bereits als Kundenservicekanal nutzen, empfehlen wir, Ihr aktuelles Setup beizubehalten und ein neues WABA über Braze für Marketing-Messaging zu erstellen. Dieses WABA benötigt eine neue Telefonnummer.

#### Wie verbinde ich WhatsApp-Support und -Marketing in Braze? {#how-do-i-connect-whatsapp-support-and-marketing-in-braze}

Sie können WhatsApp-Liquid-Eigenschaften verwenden, um eingehende WhatsApp-Nachrichteninhalte (einschließlich Nachrichtentext und Medien-URLs) von Braze an andere Plattformen weiterzuleiten, einschließlich jedes Kundenservice-Tools. Weitere Details finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Um Informationen in Braze zu senden – zum Beispiel, um anzuzeigen, dass ein:e Nutzer:in sich in einem aktiven Support-Gespräch befindet – können Sie ein angepasstes Attribut loggen (z. B. ein Boolean „has existing support chat = true/false“) und dieses als Segmentierungskriterium in Ihren Marketing-Campaigns verwenden. Sie können auch Deeplinks zwischen zwei Chat-Threads einrichten, um Nutzer:innen vom Marketing-Thread zum Support-Thread und umgekehrt zu leiten.

#### Speichert Braze Antworten von Nutzer:innen? {#does-braze-store-user-responses}
Nachrichten werden nur so lange gespeichert, wie sie für die Verarbeitung benötigt werden. Um auf Nachrichten von Nutzer:innen zuzugreifen, verwenden Sie Currents.

#### Welche Metriken sind im Braze-Dashboard verfügbar? {#what-metrics-are-available-in-the-braze-dashboard}
Sie können im Braze-Dashboard eindeutige Empfänger:innen, Sendungen, Zustellungen, Lesungen und Fehler einsehen. Beachten Sie, dass die Lesebestätigungen der Nutzer:innen auf „Ein“ gestellt sein müssen, damit Braze Lesungen verfolgen kann. Sie können auch Konversions-Events einrichten, um die Campaign-Performance zu überwachen, ähnlich wie bei anderen Kanälen.

#### Was ist eine WhatsApp-Konversation? {#what-is-a-whatsapp-conversation}
WhatsApp ist ein auf Zwei-Wege-Messaging ausgerichteter Kanal und basiert daher auf Konversationen (anstatt auf der Anzahl einzelner Nachrichten). Eine Konversation ist ein 24-Stunden-Thread zwischen einem Unternehmen und einer Endnutzerin bzw. einem Endnutzer.

- **Geschäftsinitiierte Konversation**: Eine Konversation, bei der das Unternehmen den Anfang macht, indem es eine genehmigte Template-Nachricht an die Endnutzerin oder den Endnutzer sendet. Sobald das Unternehmen eine Nachricht sendet, beginnt das 24-Stunden-Fenster.
- **Nutzerinitiierte Konversation**: Eine Konversation, bei der die Endnutzerin bzw. der Endnutzer eine Nachricht an das Unternehmen sendet. Wenn das Unternehmen als Antwort eine Nachricht sendet, beginnt das 24-Stunden-Fenster.

### Medien und Bilder {#media-and-images}

#### Warum werden Bilder nicht geladen, wenn sie als WhatsApp-Nachricht gesendet werden? {#why-wont-images-load-when-sent-as-a-whatsapp-message}
Wenn Nutzer:innen berichten, dass Bilder in WhatsApp-Nachrichten nicht heruntergeladen werden können oder das Download-Symbol nicht reagiert, liegt dies wahrscheinlich an einem bekannten Problem in älteren Versionen der WhatsApp-App. Dieses Problem kann in der Regel durch ein Upgrade des Geräts auf die neueste Version von WhatsApp behoben werden.