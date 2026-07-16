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
- [Telefonnummern für WhatsApp-Business-Konten](#whatsapp-business-account-phone-numbers)
- [Opt-in und Abo-Management](#opt-in-and-subscription-management)
- [Messaging-Limits und Qualitätsbewertung](#messaging-limits-and-quality-rating)
- [WhatsApp-Templates und Composer](#whatsapp-templates-and-composer)
- [Zustellbarkeit und Abrechnung](#deliverability-and-billing)
- [Integrationen, Daten und Reporting](#integrations-data-and-reporting)

### WhatsApp-Business-Konten {#whatsapp-business-accounts}

#### Wie erstelle ich ein WhatsApp-Business-Konto? {#how-do-i-create-a-whatsapp-business-account}
Wir empfehlen, Ihr WhatsApp-Business-Konto (WABA) über den integrierten Registrierungsablauf im Braze-Dashboard zu erstellen.

#### Ich habe bereits ein Meta-Business-Konto. Benötige ich trotzdem ein WhatsApp-Business-Konto? {#i-already-have-a-meta-business-account-do-i-still-need-a-whatsapp-business-account}
Ja, Sie müssen trotzdem ein WhatsApp-Business-Konto erstellen. Wir empfehlen, [Ihr WABA unter Ihrem Haupt-Meta-Business-Konto einzuordnen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup).

#### Wie greife ich auf mein WhatsApp-Business-Konto zu? {#how-do-i-access-my-whatsapp-business-account}
Nachdem Sie den integrierten Registrierungsablauf abgeschlossen haben, können Sie auf Ihr Konto unter business.facebook.com zugreifen, indem Sie zum [WhatsApp-Bereich](https://business.facebook.com/wa/manage/home) navigieren.

#### Kann ich mehrere WABAs mit Braze verbinden? {#can-i-connect-multiple-wabas-to-braze}
Ja, Sie können bis zu 10 WhatsApp-Business-Konten pro Workspace hinzufügen, und jedes Business-Konto kann unter einem anderen Meta Business Manager eingeordnet werden.

![Diagramm des Braze- und WhatsApp-Ökosystems, das zeigt, wie Workspaces und WhatsApp-Business-Konten miteinander verbunden sind: Sie können eine Abo-Gruppe mit einer Telefonnummer, mehrere WhatsApp-Business-Konten mit einem Workspace und einen Workspace mit mehreren Meta-Business-Portfolios verbinden.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

#### Kann ich die Währung meines WhatsApp-Business-Kontos ändern? {#can-i-change-my-whatsapp-business-account-currency}
Nein. Meta kontrolliert die Währung für Ihr WhatsApp-Business-Konto, und Braze kann diese nicht ändern oder umrechnen. Um eine andere Währung zu verwenden, [erstellen Sie ein separates WhatsApp-Business-Konto]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) mit dieser Währung oder wenden Sie sich an den Meta-Support, um zu fragen, ob die Währung Ihres bestehenden Kontos aktualisiert werden kann.

#### Was ist die Geschäftsverifizierung? {#what-is-business-verification}
Die Geschäftsverifizierung ist ein WhatsApp-Konzept, das sicherstellt, dass die Marke ein legitimes Unternehmen ist. Sie kann im WhatsApp Manager abgeschlossen werden. Die Geschäftsverifizierung ist auch erforderlich, um das Messaging zu skalieren. Ohne Geschäftsverifizierung können Kund:innen nur bis zu 250 eindeutigen Endnutzer:innen in einem rollierenden 24-Stunden-Zeitraum Nachrichten senden.

#### Was ist ein offizielles Business-Konto? {#what-is-an-official-business-account}
OBA verleiht Ihnen das grüne Häkchen neben Ihrem Anzeigenamen und ist optional. Sie können sich für ein offizielles Business-Konto bewerben, nachdem Sie die Geschäftsverifizierung abgeschlossen haben. Beachten Sie, dass die Geschäftsverifizierung und ein offizielles Business-Konto unterschiedliche WhatsApp-Konzepte sind.

### Telefonnummern für WhatsApp-Business-Konten {#whatsapp-business-account-phone-numbers}

#### Benötige ich eine Telefonnummer für mein WhatsApp-Business-Konto? {#do-i-need-a-phone-number-for-my-whatsapp-business-account}
Ja, Sie benötigen eine Nummer, auf die Sie Zugriff haben. Sie werden aufgefordert, Ihre Telefonnummer mit 2-Faktor-Authentifizierung zu verifizieren, wenn Sie den integrierten Registrierungsablauf durchlaufen. Die Telefonnummer kann nicht für andere WhatsApp-Konten (geschäftlich oder privat) verwendet werden.

#### Welche Arten von Telefonnummern werden von WhatsApp unterstützt? {#what-types-of-phone-numbers-are-supported-with-whatsapp}
Weitere Informationen finden Sie in den Meta-Anforderungen für [Telefonnummern](https://developers.facebook.com/docs/whatsapp/phone-numbers).

#### Kann ich eine Telefonnummer für mehrere WABAs verwenden? {#can-i-use-one-phone-number-across-multiple-wabas}
Nein. Eine Telefonnummer kann nicht über mehrere WABAs hinweg geteilt werden.

#### Benötige ich einen bestimmten Telefonnummerntyp, um Nachrichten in bestimmte Länder zu senden? {#do-i-need-a-specific-type-of-phone-number-to-send-messages-to-specific-countries}
Nein. WhatsApp ermöglicht es Ihnen, Nachrichten von jeder unterstützten Telefonnummer in jedem Land an Endnutzer:innen zu senden. Weitere Informationen finden Sie in den Meta-Anforderungen für [Telefonnummern](https://developers.facebook.com/docs/whatsapp/phone-numbers).

#### Wie müssen Telefonnummern von Nutzer:innen in Braze gespeichert werden? {#how-do-user-phone-numbers-need-to-be-stored-in-braze}
Telefonnummern von Nutzer:innen müssen im [E.164-Format]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting) gespeichert werden.

#### Kann ich Telefonnummern von Nutzer:innen importieren? {#can-i-import-user-phone-numbers}
Ja. Sie können [Telefonnummern von Nutzer:innen importieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers).

### Opt-in und Abo-Management {#opt-in-and-subscription-management}

#### Muss ich ein Opt-in einholen, um Marketing-Nachrichten an Endnutzer:innen auf WhatsApp zu senden? {#do-i-need-to-collect-opt-in-to-send-marketing-messages-to-end-users-on-whatsapp}
Ja, WhatsApp verlangt von Unternehmen, dass sie eine [Opt-in-Einwilligung einholen](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/), um Marketing-Nachrichten an Endnutzer:innen zu senden.

#### Kann ich Endnutzer:innen proaktiv auf WhatsApp kontaktieren, um eine Opt-in-Einwilligung einzuholen? {#can-i-proactively-message-end-users-on-whatsapp-to-collect-opt-in-consent}
Wenn Sie sich dafür entscheiden, Endnutzer:innen proaktiv zu kontaktieren, sollte Ihre erste geschäftsinitiierte Nachricht die Nutzer:innen fragen, ob sie Marketing-Nachrichten von Ihrem Unternehmen erhalten möchten, und den Meta-Anforderungen für das [Einholen von Opt-ins](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) entsprechen. Beachten Sie, dass WhatsApp die Reputation Ihres Unternehmens auf dem Kanal überwacht. Die empfohlene Best Practice ist daher, gegenüber Endnutzer:innen transparent zu sein und nur Nachrichten zu senden, die sie ausdrücklich erhalten möchten.

#### Muss ich die Telefonnummer der Endnutzer:innen beim Einholen des Opt-ins erfassen? {#do-i-need-to-collect-the-end-users-phone-number-when-i-collect-opt-in}
Sie benötigen die Telefonnummer der Endnutzer:innen im Braze-Profil, um ihnen Nachrichten senden zu können.
- Wenn Sie die Nummer bereits haben, müssen Sie sie beim Opt-in nicht erneut erfassen.
- Wenn Sie die Nummer der Endnutzer:innen nicht haben, sollte Ihre Opt-in-Methode die Erfassung der Telefonnummer beinhalten.

#### Wie aktualisiere ich den Abo-Status von Endnutzer:innen, die sich angemeldet haben? {#how-do-i-update-the-subscription-status-of-end-users-who-opt-in}
Das Abo-Management des WhatsApp-Kanals funktioniert ähnlich wie bei anderen Braze-Kanälen. Weitere Informationen finden Sie unter [Nutzer-Abos verwalten]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

#### Wenn ich bereits eine Liste von Nutzer:innen habe, die dem Empfang von Marketing-Nachrichten auf WhatsApp zugestimmt haben, wie aktualisiere ich deren Abo-Status in Braze? {#if-i-already-have-a-list-of-users-who-have-opted-in-to-receive-marketing-messages-on-whatsapp-how-do-i-update-their-subscription-status-in-braze}
Sie können deren Abo-Status über den [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional) aktualisieren.

#### Welche Methoden sollte ich verwenden, um Opt-ins einzuholen? {#what-methods-should-i-use-to-collect-opt-ins}
Braze empfiehlt, sich an [Metas Richtlinien für Opt-in-Methoden](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) zu halten, um die Compliance sicherzustellen. Weitere Informationen finden Sie in der folgenden Ressource zu [Kanal- und Opt-in-Ideen und -Vorschlägen](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit).

#### Ist ein Double-Opt-in für WhatsApp erforderlich? {#is-double-opt-in-required-for-whatsapp}
Nein, ein Double-Opt-in ist nicht erforderlich.

#### Wie melden sich meine Nutzer:innen von WhatsApp-Nachrichten ab? {#how-do-my-users-opt-out-of-whatsapp-messages}
Ihre Nutzer:innen können sich auf zwei Arten abmelden:
1. Richten Sie eine eingehende WhatsApp-Nachricht mit einem bestimmten Abmelde-Schlüsselwort ein und verwenden Sie einen Webhook, um den Abo-Status der Nutzer:innen zu aktualisieren.
2. Fügen Sie eine Schnellantwort zur Abmeldung innerhalb des WhatsApp-Templates hinzu, mit einem entsprechenden Webhook zur Aktualisierung.

### Messaging-Limits und Qualitätsbewertung {#messaging-limits-and-quality-rating}

#### Was sind Messaging-Limits? {#what-are-messaging-limits}
Messaging-Limits sind ein WhatsApp-Integritätskonzept. Sie bestimmen die maximale Anzahl geschäftsinitiierter Konversationen, die jede Telefonnummer in einem rollierenden 24-Stunden-Zeitraum starten kann. Es gibt vier Messaging-Limit-Stufen: 1k, 10k, 100k und unbegrenzt.

#### Wie erhöhe ich mein Messaging-Limit? {#how-do-i-increase-my-messaging-limit}
WhatsApp erhöht Ihr Messaging-Limit, wenn Sie die folgenden Bedingungen erfüllen:
1. Der [Telefonnummernstatus](https://www.facebook.com/business/help/896873687365001) ist **Connected**
2. Die [Qualitätsbewertung der Telefonnummer](https://www.facebook.com/business/help/896873687365001) ist **Medium** oder **High**
3. In den letzten sieben Tagen haben Sie X oder mehr Konversationen mit eindeutigen Nutzer:innen initiiert, wobei X Ihr aktuelles Messaging-Limit geteilt durch 2 ist

Um also von 100k auf unbegrenzt zu wechseln, müssen Sie mindestens 50.000 geschäftsinitiierte Konversationen in einem 7-Tage-Zeitraum senden.

#### Wie lange dauert es, mein Messaging-Limit zu erhöhen? {#how-long-does-it-take-to-increase-my-messaging-limits}
Wenn alle vorherigen Bedingungen erfüllt sind, können Sie Ihr Messaging-Limit innerhalb von 4 Tagen von 1k auf unbegrenzt erhöhen.

#### Wo kann ich mein aktuelles Messaging-Limit einsehen? {#where-can-i-see-my-current-messaging-limit}
Sie können Ihre aktuellen Messaging-Limits im Tab **WhatsApp Manager > Overview Dashboard > Insights** überprüfen.

#### Was passiert, wenn ich versuche, Nachrichten zu senden, obwohl ich mein Messaging-Limit bereits erreicht habe? {#what-happens-if-i-attempt-to-send-messages-when-i-have-already-reached-my-messaging-limit}
Wenn Sie versuchen, eine Campaign oder ein Canvas an mehr eindeutige Nutzer:innen zu senden, als Ihr aktuelles Limit erlaubt, werden die Nachrichten nicht zugestellt. Braze versucht weiterhin, die Nachrichten erneut zu senden, wenn/falls Ihr Messaging-Limit innerhalb eines Tages erhöht wird.

#### Kann mein Messaging-Limit sinken? {#can-my-messaging-limit-decrease}
Ja, wenn Ihre Qualitätsbewertung der Telefonnummer zu stark sinkt, besteht das Risiko, dass WhatsApp Ihr Messaging-Limit verringert. Braze empfiehlt, qualitätsbezogene Updates von WhatsApp zu abonnieren und sich benachrichtigen zu lassen, einschließlich Updates zu Ihrem Telefonnummernstatus und Ihrer Messaging-Limit-Stufe. Sie können Benachrichtigungen direkt im WhatsApp-Manager-Dashboard abonnieren.

#### Welche Faktoren beeinflussen die Qualitätsbewertung der Telefonnummer, und was passiert, wenn meine Qualitätsbewertung zu stark sinkt? {#what-factors-affect-phone-number-quality-rating-and-what-happens-when-my-quality-rating-drops-too-low}
Faktoren, die die Qualitätsbewertung der Telefonnummer beeinflussen, sind unter anderem, dass ein:e Endnutzer:in ein Unternehmen blockiert (und die Gründe, die dabei angegeben werden) sowie dass ein:e Endnutzer:in ein Unternehmen meldet.

Wenn die Qualitätsbewertung niedrig ist, ändert sich der Telefonnummernstatus von **Connected** zu **Flagged**. Wenn sich die Qualität innerhalb von sieben Tagen nicht verbessert, kehrt der Status zu **Connected** zurück. Allerdings wird das Messaging-Limit auf die nächstniedrigere Stufe verringert. Beispielsweise hat eine Telefonnummer, die zuvor ein Messaging-Limit von 100.000 hatte, nun ein Messaging-Limit von 10.000.

#### Was ist das Meta-Durchsatzlimit? {#what-is-the-meta-throughput-limit}
Meta hat ein eigenes Durchsatzlimit, das vom WABA-Messaging-Limit getrennt ist. Das Standardlimit, das die Cloud-API unterstützt, beträgt 80 Nachrichten pro Sekunde. Wenn Sie davon ausgehen, dass Ihre Campaigns dieses Limit überschreiten, können Sie eine [Erhöhung beantragen](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput). Meta empfiehlt, diesen Antrag mindestens drei Tage vor dem Versand der Campaigns einzureichen.

### WhatsApp-Templates und Composer {#whatsapp-templates-and-composer}

#### Was ist ein WhatsApp-Template? {#what-is-a-whatsapp-template}
WhatsApp verlangt, dass alle geschäftsinitiierten Nachrichten mit einem genehmigten Template beginnen. Das Template enthält den Nachrichtentext sowie optionale Rich Media wie Bilder, Calls-to-Action und Schnellantwort-Buttons. Nachdem WhatsApp Templates genehmigt hat, können sie zum Verfassen einer WhatsApp-Nachricht in Braze verwendet werden.

#### Wo erstelle, bearbeite und verwalte ich meine WhatsApp-Templates? {#where-do-i-create-edit-and-manage-my-whatsapp-templates}
Sie erstellen, bearbeiten, verwalten und reichen Templates direkt im WhatsApp Manager zur Genehmigung ein. Nachdem Ihr WABA mit Braze verbunden ist, sehen Sie alle Ihre Templates im Dashboard mit einer Statusanzeige. Wenn ein Template abgelehnt wird, reichen Sie es direkt über den WhatsApp Manager erneut ein. **Templates können nicht direkt in Braze erstellt oder bearbeitet werden.**

#### Wie lange dauert es, bis WhatsApp eine Template-Einreichung überprüft? {#how-long-does-it-take-whatsapp-to-review-a-template-submission}
Der Genehmigungsprozess kann bis zu 24 Stunden dauern, aber oft werden Templates innerhalb von Stunden oder Minuten bearbeitet.

#### Wie viele Templates kann ich gleichzeitig haben? {#how-many-templates-can-i-have-at-a-given-time}
Ihr Nachrichtentemplate-Limit hängt von Ihrem Geschäftsverifizierungsstatus ab. Sie können Ihr Limit auf der Seite **WhatsApp Manager > Message Templates** überprüfen.

#### Wie personalisiere ich Template-Text und Rich Media in Braze? {#how-do-i-personalize-template-copy-and-rich-media-in-braze}
WhatsApp ermöglicht das Einfügen variabler Parameter in Nachrichtentemplates. Nachrichten können nicht mit einem variablen Parameter beginnen oder enden. Variable Parameter können mit Liquid-Logik in der Braze-Plattform befüllt werden. Weitere Informationen zu variablen Parametern finden Sie unter [WhatsApp-Nachricht in Braze verfassen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message).

#### Mein Template wurde abgelehnt. Kann Braze mir bei der Genehmigung helfen? {#my-template-got-rejected-can-braze-help-me-get-it-approved}
Das Braze-Team hat keinen Einblick in Template-Ablehnungen. Sie sollten direkt mit Ihrem WhatsApp Business Manager zusammenarbeiten, um das Template zu bearbeiten und erneut einzureichen. Stellen Sie sicher, dass Sie bei Bedarf ein Beispieltemplate bereitstellen. Überprüfen Sie, ob Ihr Template den [Geschäfts-](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) oder [Handelsrichtlinien](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) von Meta entspricht.

#### Können Rich Media in Braze gezielt eingesetzt oder personalisiert werden? {#can-the-rich-media-be-targeted-or-personalized-in-braze}
Bilder können aus der Medienbibliothek hochgeladen werden, aber nicht dynamisch gezielt eingesetzt werden. Bei URLs kann der letzte Teil des Links [dynamisch mit Liquid befüllt werden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

#### Welche Arten von Rich Media werden in WhatsApp-Templates unterstützt? {#what-kind-of-rich-media-is-supported-in-whatsapp-templates}
Sie können Bilder, Calls-to-Action (URL oder Telefonnummer) und Schnellantwort-Buttons zu WhatsApp-Templates hinzufügen. Sie können diese Elemente hinzufügen, wenn Sie Templates direkt in WhatsApp erstellen.

#### Was ist, wenn mein Template fälschlicherweise wegen eines Verstoßes gegen die WhatsApp-Handelsrichtlinie markiert wurde? {#what-if-my-template-was-falsely-flagged-for-violating-whatsapps-commerce-policy}
Wenn Sie der Meinung sind, dass Meta Ihr Template fälschlicherweise markiert hat, verwenden Sie den Überprüfungslink in der E-Mail von WhatsApp, um eine erneute Überprüfung anzufordern. Das WhatsApp-Business-Team prüft die Entscheidung und hebt sie gegebenenfalls auf.

#### Warum zeigt mein importiertes WhatsApp-Template im Composer „Nachricht unvollständig“ an? {#why-does-my-imported-whatsapp-template-show-message-incomplete-in-the-composer}
Die Warnung „Nachricht unvollständig“ erscheint, wenn erforderliche Template-Variablenfelder im Composer nicht mit gültigen Werten befüllt sind.

Wenn Sie Templates mit dem [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder) erstellen, nummeriert Braze die Variablen in sequenzielle Platzhalter um ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %} usw.). Templates, die extern im WhatsApp Manager von Meta erstellt wurden, können weiterhin Muster enthalten, die die Variablenzuordnung fehleranfällig machen, wie z. B.:

- Nicht-sequenzielle Nummerierung (z. B. {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Fehlende Variablen in der Sequenz (z. B. Überspringen von {% raw %}`{{2}}`{% endraw %})
- Variablen, die mit einer anderen Zahl als 1 beginnen

Um dies zu beheben, bearbeiten Sie Ihr Template im WhatsApp Manager von Meta, sodass es sequenzielle Platzhalterformatierung verwendet, und importieren Sie es dann erneut in Braze. Bestätigen Sie in Braze, dass jedes erforderliche Variablenfeld mit einem gültigen Liquid-Wert befüllt ist.

### Zustellbarkeit und Abrechnung {#deliverability-and-billing}

#### Warum wird eine Nachricht möglicherweise nicht zugestellt? {#why-would-a-message-not-be-delivered}
Es gibt verschiedene Gründe, warum eine Nachricht nicht zugestellt werden kann, darunter Netzwerkprobleme und ein ausgeschaltetes Gerät.

#### Wenn eine Nachricht nicht zugestellt wird, werden mir Kosten berechnet? {#if-a-message-is-not-delivered-will-i-be-billed}
Nein. Wenn eine Nachricht nicht zugestellt wird, werden Ihnen keine Kosten berechnet.

#### Was passiert, wenn ein:e Endnutzer:in mein Unternehmen blockiert? {#what-happens-if-an-end-user-blocks-my-business}
Wenn ein:e Endnutzer:in Ihr Unternehmen blockiert, werden nachfolgende Nachrichten, die Sie zu senden versuchen, nicht zugestellt, und Ihnen werden keine Kosten berechnet.

#### Was passiert, wenn ein:e Endnutzer:in eine Nachricht meldet? {#what-happens-if-an-end-user-reports-a-message}
Wenn ein:e Endnutzer:in eine Nachricht meldet, können Sie weiterhin nachfolgende Nachrichten an diese:n Nutzer:in senden. Allerdings kann die Meldung Ihre Qualitätsbewertung auf dem Kanal beeinflussen.

#### Wenn ein:e Endnutzer:in mein Unternehmen blockiert oder meldet, wird deren Abo-Status in Braze aktualisiert? {#if-an-end-user-blocks-or-reports-my-business-will-their-subscription-status-be-updated-in-braze}
Nein. Deren Braze-Abo-Status wird nicht aktualisiert.

### Integrationen, Daten und Reporting {#integrations-data-and-reporting}

#### Unterstützt Braze Kundensupport-Anwendungsfälle wie Chatbots und menschlich unterstützten Chat für WhatsApp? {#does-braze-support-customer-support-use-cases-like-chatbots-and-human-assisted-chat-for-whatsapp}
Wir unterstützen keine Chatbots oder menschlich unterstützten Chat innerhalb von Braze oder über direkte Integrationen.

Wenn Sie WhatsApp bereits als Kundensupport-Kanal nutzen, empfehlen wir, Ihr aktuelles Setup beizubehalten und ein neues WABA über Braze für Marketing-Messaging zu erstellen. Dieses WABA benötigt eine neue Telefonnummer.

#### Wie kann ich die Lücke zwischen meinem Kundensupport-Messaging und meinem Marketing-Messaging über Braze überbrücken? {#how-can-i-bridge-the-gap-between-my-customer-support-messaging-and-my-marketing-messaging-via-braze}
Sie können WhatsApp-Liquid-Eigenschaften verwenden, um eingehende WhatsApp-Nachrichteninhalte (einschließlich Nachrichtentext und Medien-URLs) von Braze an andere Plattformen weiterzuleiten, einschließlich jedes Kundensupport-Tools. Weitere Details finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Um Informationen an Braze zu senden, beispielsweise um anzuzeigen, dass ein:e Nutzer:in sich in einer aktiven Support-Konversation befindet, können Sie ein angepasstes Attribut protokollieren (z. B. einen booleschen Wert „hat bestehenden Support-Chat = wahr/falsch“) und dieses als Segmentierungskriterium in Ihren Marketing-Campaigns verwenden. Sie können auch Deeplinks zwischen zwei Chat-Threads erstellen, um Nutzer:innen vom Marketing-Thread zum Support-Thread und umgekehrt zu leiten.

#### Speichert Braze Nutzerantworten? {#does-braze-store-user-responses}
Nachrichten werden nur so lange gespeichert, wie sie zur Verarbeitung benötigt werden. Um auf Nutzernachrichten zuzugreifen, verwenden Sie Currents.

#### Welche Metriken sind im Braze-Dashboard verfügbar? {#what-metrics-are-available-in-the-braze-dashboard}
Sie können eindeutige Empfänger:innen, Sendungen, Zustellungen, Lesevorgänge und Fehler im Braze-Dashboard einsehen. Beachten Sie, dass die Lesebestätigungen der Endnutzer:innen auf „Ein“ stehen müssen, damit Braze Lesevorgänge tracken kann. Sie können auch Konversions-Events einrichten, um die Campaign-Performance zu überwachen, ähnlich wie bei anderen Kanälen.

#### Was ist eine WhatsApp-Konversation? {#what-is-a-whatsapp-conversation}
WhatsApp ist ein Kanal, der auf bidirektionales Messaging ausgerichtet ist und daher auf Konversationen basiert (anstatt auf der Anzahl einzelner Nachrichten). Eine Konversation ist ein 24-Stunden-Thread zwischen einem Unternehmen und einem:einer Endnutzer:in.

- **Geschäftsinitiierte Konversation**: Eine Konversation, bei der das Unternehmen eine genehmigte Template-Nachricht an die/den Endnutzer:in sendet. Sobald das Unternehmen eine Nachricht sendet, beginnt das 24-Stunden-Fenster.
- **Nutzerinitiierte Konversation**: Eine Konversation, bei der die/der Endnutzer:in eine Nachricht an das Unternehmen sendet. Wenn das Unternehmen eine Nachricht als Antwort sendet, beginnt das 24-Stunden-Fenster.