---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 7
description: "Auf dieser Seite erfahren Sie, wie Sie Inbox Vision einrichten, ein Feature, mit dem Marketer ihre E-Mails aus der Perspektive verschiedener E-Mail-Clients und mobiler Geräte betrachten können."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision {#inbox-vision}

> Mit Inbox Vision können Sie Ihre E-Mails aus der Perspektive verschiedener E-Mail-Clients und mobiler Geräte anzeigen. So können Sie beispielsweise Unterschiede zwischen Dark Mode und Light Mode testen, um sicherzustellen, dass Ihre E-Mails wie beabsichtigt dargestellt werden.

{% alert important %}
Inbox Vision funktioniert möglicherweise nicht, wenn Ihr E-Mail-Inhalt auf Template-Informationen wie Nutzerprofildaten basiert. Braze verwendet beim Versenden von E-Mails für dieses Feature ein leeres Nutzerprofil als Template.<br><br>Fügen Sie Standardwerte zu jedem Liquid in Ihrer E-Mail-Nachricht hinzu. Ohne Standardwerte kann es zu einem falschen positiven Ergebnis kommen oder der Test kann fehlschlagen.
{% endalert %}

## Hinweise {#considerations}

Im Allgemeinen funktioniert Ihre E-Mail nicht mit Inbox Vision, wenn Ihr E-Mail-Inhalt auf Template-Informationen angewiesen ist, wie z. B. Nutzerprofil-Informationen. Das liegt daran, dass Braze bei der Verwendung dieses Features eine:n leere:n Nutzer:in als Template verwendet.

Sie können dies beheben, indem Sie Standardwerte oder beliebige Werte zum Liquid in Ihrer E-Mail-Nachricht hinzufügen, bevor Sie Inbox Vision ausführen. Wenn Sie die Tests in Inbox Vision abgeschlossen haben, wird die ursprüngliche E-Mail-Nachricht wieder angezeigt. Wenn keine Werte angegeben werden, kann der Test die Vorschauen möglicherweise nicht erfolgreich rendern.

Ihr Unternehmen hat ein Limit für die Anzahl der E-Mails, die Sie mit Inbox Vision in der Vorschau anzeigen können. Sie können dies im Tab **E-Mail-Vorschauen** von Inbox Vision überwachen.

Geben Sie eine Betreffzeile und eine gültige Absender-Domain an, um Vorschauen anzuzeigen. Beachten Sie die Unterschiede beim Rendering zwischen Desktop und Mobilgeräten. Verwenden Sie die Vorschauen, um zu bestätigen, dass die E-Mail wie beabsichtigt angezeigt wird.

{% alert note %}
Wenn bei der Vorschau einer Campaign ein Berechtigungsfehler angezeigt wird, leeren Sie Ihren Cache und Ihre Cookies oder versuchen Sie es in einem Inkognito-Fenster. Browser-Erweiterungen blockieren manchmal die Vorschau.
{% endalert %}

So testen Sie Ihre E-Mail-Nachricht in Inbox Vision:

1. Gehen Sie zu Ihrem Drag-and-Drop-Editor oder HTML-E-Mail-Editor.
2. Wählen Sie in Ihrem Editor **Vorschau und Test** aus.
3. Wählen Sie **Inbox Vision** aus.
4. Wählen Sie **Inbox Vision ausführen** aus. Dies kann bis zu zehn Minuten dauern.
5. Wählen Sie anschließend eine Kachel aus, um die Vorschau detaillierter anzuzeigen. Diese Vorschauen sind in folgende Abschnitte gruppiert: **Web Clients**, **Application Clients** und **Mobile Clients**.

![Die Option zur Auswahl von E-Mail-Clients für die Vorschau.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Wählen Sie **Inbox Vision ausführen** aus. Dies kann zwischen zwei und zehn Minuten dauern.

{% alert note %}
Inbox Vision unterstützt keine E-Mail-Nachrichten, die [Abbruchlogik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) enthalten, da diese E-Mails als statischer Inhalt gerendert werden.
{% endalert %}

### Vorschau als Nutzer:in {#previewing-as-a-user}

Wenn Sie die Vorschau als zufällige:r Nutzer:in anzeigen, speichert Inbox Vision keine nutzerspezifischen Einstellungen oder Attribute (wie Name oder Präferenzen). Wenn Sie eine:n benutzerdefinierte:n Nutzer:in auswählen, kann die Inbox-Vision-Vorschau von anderen Vorschauen abweichen, da sie spezifische Nutzerdaten verwendet.

## Code-Analyse {#code-analysis}

Die Code-Analyse hebt potenzielle HTML-Probleme hervor, zeigt die Anzahl der Vorkommen an und weist auf nicht unterstützte HTML-Elemente hin.

### Informationen zur Code-Analyse anzeigen {#viewing-code-analysis-information}

Diese Informationen finden Sie auf dem Tab **Inbox Vision**, indem Sie <i class="fas fa-list"></i> **Listenansicht** auswählen. Die Listenansicht ist nur für HTML-E-Mail-Templates verfügbar. Für Drag-and-drop-Templates verwenden Sie stattdessen Vorschauen, um Probleme zu beheben.

![Beispiel einer Code-Analyse in der Inbox-Vision-Vorschau.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Die Code-Analyse kann schneller erscheinen als die Vorschau für einen bestimmten Client, da Braze wartet, bis die E-Mail eingegangen ist, bevor der Screenshot erstellt wird.
{% endalert %}

## Spam-Test {#spam-testing}

Spam-Tests schätzen ein, ob E-Mails möglicherweise als Spam gefiltert werden. Die Tests werden über Filter wie IronPort, SpamAssassin und Barracuda sowie ISP-Filter wie Gmail und Outlook durchgeführt, wobei statische Seed-Posteingänge verwendet werden, die standardmäßig keine E-Mails öffnen oder anklicken.

{% alert important %}
Die Platzierung im Posteingang wird hauptsächlich durch das Live-Engagement der Empfänger:innen bestimmt. Spam-Test-Ergebnisse stimmen möglicherweise nicht mit dem überein, was Sie bei echten Campaigns sehen.
{% endalert %}

Für eine aussagekräftigere Einschätzung der Zustellbarkeit testen Sie Inhalte mit kleinen Live-Kohorten – starke Öffnungs- und Klickraten sind das zuverlässigste Signal. Nutzen Sie Spam-Tests als einen Faktor neben dem Engagement-Monitoring.

### Spam-Test-Ergebnisse anzeigen {#viewing-spam-test-results}

So überprüfen Sie Ihre Spam-Test-Ergebnisse:

1. Wählen Sie den Tab **Spam Testing** im Bereich **Inbox Vision** aus. Die Tabelle **Spam Test Result** zeigt den Namen des Spam-Filters, den Status und den Typ an.
2. Überprüfen Sie diese Ergebnisse und nehmen Sie gegebenenfalls Anpassungen an Ihrer E-Mail-Campaign vor.
3. Wählen Sie **Re-run Test** aus, um Ihre Spam-Test-Ergebnisse neu zu laden.

## Barrierefreiheitstests {#accessibility-testing}

Barrierefreiheitstests heben potenzielle Barrierefreiheitsprobleme in Ihrer E-Mail hervor und zeigen, welche Elemente die Standards nicht erfüllen. Braze analysiert Inhalte anhand ausgewählter Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), einer Reihe international anerkannter Standards, die vom W3C entwickelt wurden, um Webinhalte barrierefreier zu gestalten.

### Funktionsweise {#how-it-works}

Wenn Sie Inbox Vision ausführen, prüft Braze automatisch auf häufige Barrierefreiheitsprobleme im [WCAG 2.2 AA-Regelwerk](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (wie fehlender Alt-Text, unzureichender Farbkontrast, fehlerhafte Überschriftenstruktur) und kategorisiert den Schweregrad, um Ihnen bei der Priorisierung von Korrekturen zu helfen. Beachten Sie, dass selbst wenn Alt-Text vorhanden ist, die [Darstellung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) vom E-Mail-Client der Empfänger:innen gesteuert wird, nicht von Braze.

{% alert important %}
Barrierefreiheitstests können zur Unterstützung der Compliance-Bemühungen von Kund:innen in Bezug auf Vorschriften oder Gesetze wie den [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) verwendet werden. Kund:innen erkennen jedoch an, dass Braze keine Zusicherungen oder Gewährleistungen dahingehend abgibt, ob die Nutzung der Barrierefreiheitstests die Compliance-Verpflichtungen der Kund:innen erfüllt, und lehnt jegliche diesbezügliche Haftung ab.
{% endalert %}

### Ergebnisse der Barrierefreiheitstests anzeigen {#viewing-accessibility-testing-results}

Barrierefreiheitstests generieren Ergebnisse für jede Regel als bestanden, fehlgeschlagen oder überprüfungsbedürftig im Tab **Accessibility Testing**. Braze kategorisiert jede Regel nach POUR (Perceivable, Operable, Understandable, Robust), den vier Prinzipien hinter WCAG.

#### POUR-Kategorien {#pour-categories}

Inbox Vision kategorisiert Probleme unter den vier grundlegenden [POUR-Prinzipien](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceivable (Wahrnehmbar), Operable (Bedienbar), Understandable (Verständlich) und Robust (Robust).

| Prinzip | Definition |
| --- | --- |
| Perceivable (Wahrnehmbar) | Informationen und Komponenten der Benutzeroberfläche müssen den Nutzer:innen so präsentiert werden, dass sie diese wahrnehmen können.<br><br>Nutzer:innen müssen in der Lage sein, die dargestellten Informationen wahrzunehmen (sie dürfen für keinen ihrer Sinne unsichtbar sein). |
| Operable (Bedienbar) | Komponenten der Benutzeroberfläche und Navigation müssen bedienbar sein.<br><br>Nutzer:innen müssen in der Lage sein, die Schnittstelle zu bedienen (die Schnittstelle darf keine Interaktion erfordern, die Nutzer:innen nicht ausführen können). |
| Understandable (Verständlich) | Informationen und die Bedienung der Benutzeroberfläche müssen verständlich sein.<br><br>Nutzer:innen müssen in der Lage sein, die Informationen sowie die Bedienung der Benutzeroberfläche zu verstehen (der Inhalt oder die Bedienung darf ihr Verständnis nicht übersteigen). |
| Robust (Robust) | Inhalte müssen robust genug sein, damit sie von einer Vielzahl von User Agents, einschließlich assistiver Technologien, zuverlässig interpretiert werden können.<br><br>Nutzer:innen müssen in der Lage sein, auf die Inhalte zuzugreifen, wenn sich Technologien weiterentwickeln (wenn sich Technologien und User Agents weiterentwickeln, sollten die Inhalte weiterhin barrierefrei bleiben). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="POUR-Kategorien" }

#### Schweregrade {#severity-levels}

Inbox Vision klassifiziert Barrierefreiheitsprobleme nach Schweregrad, um Ihnen bei der Priorisierung der Behebung zu helfen.

| Status | Definition |
| --- | --- |
| Kritisch | Probleme, die den Zugang zu Inhalten oder Funktionen für Nutzer:innen mit Behinderungen blockieren können. Diese sind am schwerwiegendsten und sollten vorrangig behoben werden. |
| Schwerwiegend | Probleme, die erhebliche Barrieren verursachen können, den Zugang aber möglicherweise nicht vollständig blockieren. Diese sollten zeitnah behoben werden. |
| Moderat | Probleme, die für Nutzer:innen mit Behinderungen gewisse Schwierigkeiten verursachen können, den Zugang aber weniger wahrscheinlich vollständig blockieren. |
| Geringfügig | Probleme, die einen relativ geringen Einfluss auf die Barrierefreiheit haben und möglicherweise nur geringfügige Unannehmlichkeiten verursachen. |
| Überprüfung erforderlich | Es kann nicht erkannt werden, ob ein Problem vorliegt oder nicht. Dies kann auftreten, wenn das Kontrastverhältnis nicht bestimmt werden kann, weil der Text auf einem Hintergrundbild platziert ist. Sie müssen manuell überprüfen, da eine automatische Bestimmung nicht möglich ist. |
| Bestanden | WCAG A, AA oder Best Practice für Barrierefreiheit bestanden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schweregrade" }

{% alert important %}
Der Drag-and-Drop-Editor unterstützt nicht das Setzen eines `<title>`-Elements für das Dokument, sodass der Barrierefreiheitsscanner diese Prüfung immer als fehlgeschlagen meldet.<br><br>Diese Einschränkung wird für zukünftige Verbesserungen nachverfolgt. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="the drag-and-drop editor document title limitation in Inbox Vision" %}
{% endalert %}

### Automatisierte Barrierefreiheitstests verstehen {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## Best Practices {#best-practices}

### Überprüfen Sie Ihre E-Mail-Abonnent:innen-Liste {#review-your-email-subscriber-list}

Nutzen Sie das [E-Mail-Insights-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-insights-dashboard), um die beliebtesten Gerätetypen und Anbieter zu ermitteln, bei denen Ihre Abonnent:innen aktiv sind. Wenn Sie mehr Granularität benötigen, z. B. den Browser, das Gerätemodell und mehr, können Sie Ihre [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Daten oder den [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) nutzen, um dieses Detailniveau über das aktuelle E-Mail-Engagement Ihrer Nutzer:innen abzurufen.

Andernfalls verwendet Braze standardmäßig die 20 wichtigsten Vorschauen basierend auf allgemeinen Branchen- und Expertendaten, die den Großteil der Umgebungen abdecken, in denen Ihre Abonnent:innen mit Ihren E-Mails interagieren. Wenn Ihre Datenanalyse auf andere, beliebtere Vorschauen hinweist, können Sie jedes Mal, wenn Sie Inbox Vision ausführen, einen Standardsatz von Vorschauen definieren.

### Wählen Sie aussagekräftige und betroffene Vorschauen aus {#select-meaningful-previews-and-impacted-previews}

Wenn Ihr Unternehmen hauptsächlich in den USA ansässig ist, gibt es möglicherweise bestimmte Vorschauen, wie z. B. internationale Vorschauen wie GMX.de, die nur von einer geringen Anzahl von Nutzer:innen verwendet werden. Wir empfehlen, Postfächer mit einer erheblichen Abonnent:innen-Reichweite zu priorisieren und zu optimieren und Ihre Vorschauen für Postfächer mit höherer Wirkung zu reservieren.

Wenn Sie Korrekturen vornehmen, die bestimmte Vorschauen betreffen, wählen Sie nur die betroffenen Vorschauen aus, um zu vermeiden, dass ungenutzte Vorschauen verbraucht werden.

### Führen Sie Inbox Vision für die finale E-Mail-Version aus {#run-inbox-vision-on-the-final-email-version}

Wir empfehlen, Inbox Vision auszuführen, wenn die E-Mail-Nachricht produktionsbereit oder nahezu fertig ist. So können Sie die Anzahl der generierten Vorschauen reduzieren, da die E-Mail vor der Finalisierung und dem Versand an Nutzer:innen mehrere Iterationen durchläuft.

Inbox Vision bei jeder einzelnen Bearbeitung oder Änderung auszuführen, kann schnell Vorschauen verbrauchen. Wir empfehlen, zunächst alle notwendigen Änderungen an der E-Mail vorzunehmen und dann Inbox Vision auszuführen, um eine Vorschau darauf zu erhalten, wie sich alle Ihre Änderungen auf das Rendering Ihrer E-Mail in verschiedenen Umgebungen auswirken können.

Braze führt Tests über tatsächliche E-Mail-Clients durch und stellt sicher, dass die Darstellungen korrekt sind. Wenn Sie bei einem Client durchgehend ein Problem feststellen, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support).

### Testgenauigkeit im Vergleich zu Live-Postfächern {#test-accuracy-versus-live-inboxes}

Eine gesendete Nachricht kann anders aussehen als die Vorschau im Editor, da Anbieter dasselbe HTML unterschiedlich interpretieren. Laden Sie eine Kopie des gesendeten HTML herunter, um es zu vergleichen, und verwenden Sie CSS-Inlining, wenn Clients `<style>`-Blöcke entfernen.