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
Inbox Vision funktioniert möglicherweise nicht, wenn Ihr E-Mail-Inhalt auf Template-Informationen wie Nutzerprofildaten basiert. Braze verwendet beim Versenden von E-Mails für dieses Feature ein leeres Kundenprofil als Template.<br><br>Fügen Sie Standardwerte zu jedem Liquid in Ihrer E-Mail-Nachricht hinzu. Ohne Standardwerte kann es zu einem falschen positiven Ergebnis kommen oder der Test kann fehlschlagen.
{% endalert %}

## Hinweise {#considerations}

Generell funktioniert Ihre E-Mail nicht mit Inbox Vision, wenn der Inhalt Ihrer E-Mail auf Template-Informationen angewiesen ist, wie z. B. Nutzerprofilinformationen. Das liegt daran, dass Braze bei der Verwendung dieses Features ein leeres Nutzerprofil als Template nutzt.

Sie können dieses Problem lösen, indem Sie Standardwerte oder beliebige Werte zum Liquid in Ihrer E-Mail-Nachricht hinzufügen, bevor Sie Inbox Vision ausführen. Wenn Sie das Testen in Inbox Vision abgeschlossen haben, wird die ursprüngliche E-Mail-Nachricht wieder angezeigt. Falls keine Werte angegeben werden, schlägt der Test möglicherweise fehl und die Vorschauen werden nicht korrekt gerendert.

Ihr Unternehmen hat ein Limit für die Anzahl der E-Mails, die Sie mit Inbox Vision in der Vorschau anzeigen können. Sie können dies im Tab **Email Previews** von Inbox Vision überwachen.

Geben Sie eine Betreffzeile und eine gültige Versanddomain an, um Vorschauen anzuzeigen. Beachten Sie die Unterschiede bei der Darstellung auf Desktop- und Mobilgeräten. Nutzen Sie die Vorschauen, um zu bestätigen, dass die E-Mail wie beabsichtigt angezeigt wird.

{% alert note %}
Wenn bei der Vorschau einer Campaign ein Berechtigungsfehler angezeigt wird, leeren Sie Ihren Cache und Ihre Cookies oder versuchen Sie es in einem Inkognito-Fenster. Browsererweiterungen blockieren manchmal die Vorschau.
{% endalert %}

So testen Sie Ihre E-Mail-Nachricht in Inbox Vision:

1. Öffnen Sie Ihren Drag-and-Drop-Editor oder HTML-E-Mail-Editor.
2. Wählen Sie in Ihrem Editor **Preview & Test** aus.
3. Wählen Sie **Inbox Vision** aus.
4. Wählen Sie **Run Inbox Vision** aus. Dies kann bis zu zehn Minuten dauern.
5. Wählen Sie anschließend eine Kachel aus, um die Vorschau im Detail anzuzeigen. Diese Vorschauen sind in folgende Abschnitte unterteilt: **Web Clients**, **Application Clients** und **Mobile Clients**.

![Die Option zur Auswahl von E-Mail-Clients für die Vorschau.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Wählen Sie **Run Inbox Vision** aus. Dies kann zwischen zwei und zehn Minuten dauern.

{% alert note %}
Inbox Vision unterstützt keine E-Mail-Nachrichten, die [Abbruchlogik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) enthalten, da diese E-Mails als statischer Inhalt gerendert werden.
{% endalert %}

### Vorschau als Nutzer:in {#previewing-as-a-user}

Wenn Sie die Vorschau als zufällige:r Nutzer:in anzeigen, speichert Inbox Vision keine nutzerspezifischen Einstellungen oder Attribute (wie Name oder Präferenzen). Wenn Sie eine:n benutzerdefinierte:n Nutzer:in auswählen, kann die Inbox Vision-Vorschau von anderen Vorschauen abweichen, da sie spezifische Nutzerdaten verwendet.

## Code-Analyse {#code-analysis}

Die Code-Analyse hebt potenzielle HTML-Probleme hervor, zeigt die Anzahl der Vorkommen an und weist auf nicht unterstützte HTML-Elemente hin.

### Informationen zur Code-Analyse anzeigen {#viewing-code-analysis-information}

Sie finden diese Informationen auf dem Tab **Inbox Vision**, indem Sie <i class="fas fa-list"></i> **Listenansicht** auswählen. Die Listenansicht ist nur für HTML-E-Mail-Templates verfügbar. Für Drag-and-Drop-Templates verwenden Sie stattdessen Vorschauen, um Probleme zu beheben.

![Beispiel einer Code-Analyse in der Inbox-Vision-Vorschau.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Die Code-Analyse kann schneller erscheinen als die Vorschau für einen bestimmten Client, da Braze wartet, bis die E-Mail eingetroffen ist, bevor der Screenshot erstellt wird.
{% endalert %}

## Spam-Test {#spam-testing}

Spam-Tests schätzen ein, ob eine E-Mail möglicherweise als Spam gefiltert wird. Die Tests werden über Filter wie IronPort, SpamAssassin und Barracuda sowie ISP-Filter wie Gmail und Outlook durchgeführt, wobei statische Seed-Postfächer verwendet werden, die standardmäßig keine Öffnungen oder Klicks erzeugen.

{% alert important %}
Inbox Placement wird hauptsächlich durch das Live-Engagement der Empfänger:innen bestimmt. Spam-Testergebnisse stimmen möglicherweise nicht mit dem überein, was Sie bei echten Campaigns beobachten.
{% endalert %}

Für ein klareres Bild der Zustellbarkeit testen Sie Inhalte mit kleinen Live-Kohorten – starke Öffnungs- und Klickraten sind das zuverlässigste Signal. Nutzen Sie Spam-Tests als einen Baustein neben dem Engagement-Monitoring.

### Spam-Testergebnisse anzeigen {#viewing-spam-test-results}

So überprüfen Sie Ihre Spam-Testergebnisse:

1. Wählen Sie den Tab **Spam Testing** im Bereich **Inbox Vision** aus. Die Tabelle **Spam Test Result** zeigt den Namen des Spam-Filters, den Status und den Typ an.
2. Überprüfen Sie diese Ergebnisse und nehmen Sie gegebenenfalls Anpassungen an Ihrer E-Mail-Campaign vor.
3. Wählen Sie **Re-run Test** aus, um Ihre Spam-Testergebnisse neu zu laden.

## Barrierefreiheitstests {#accessibility-testing}

Barrierefreiheitstests heben potenzielle Probleme mit der Barrierefreiheit in Ihren E-Mails hervor und zeigen, welche Elemente die Standards nicht erfüllen. Braze analysiert Inhalte anhand ausgewählter Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), einer Reihe international anerkannter Standards, die vom W3C entwickelt wurden, um Webinhalte barrierefreier zu gestalten.

### Funktionsweise {#how-it-works}

Wenn Sie Inbox Vision ausführen, prüft Braze automatisch auf häufige Barrierefreiheitsprobleme im [WCAG 2.2 AA-Regelwerk](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (z. B. fehlender Alt-Text, unzureichender Farbkontrast, fehlerhafte Überschriftenstruktur) und kategorisiert den Schweregrad, damit Sie Korrekturen priorisieren können. Beachten Sie, dass selbst wenn Alt-Text vorhanden ist, die [Darstellung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) vom E-Mail-Client der Empfänger:innen gesteuert wird, nicht von Braze.

{% alert important %}
Barrierefreiheitstests können zur Unterstützung der Compliance-Bemühungen von Kund:innen in Bezug auf Vorschriften oder Gesetze wie den [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) verwendet werden. Kund:innen erkennen jedoch an, dass Braze keinerlei Zusicherungen oder Gewährleistungen dahingehend abgibt, ob die Nutzung der Barrierefreiheitstests die Compliance-Verpflichtungen der Kund:innen erfüllt, und lehnt jede diesbezügliche Haftung ab.
{% endalert %}

### Ergebnisse der Barrierefreiheitstests anzeigen {#viewing-accessibility-testing-results}

Barrierefreiheitstests generieren Ergebnisse für jede Regel als bestanden, fehlgeschlagen oder Überprüfung erforderlich im Tab **Accessibility Testing**. Braze kategorisiert jede Regel nach POUR (Perceivable, Operable, Understandable, Robust) – den vier Prinzipien hinter WCAG.

#### POUR-Kategorien {#pour-categories}

Inbox Vision kategorisiert Probleme unter den vier grundlegenden [POUR-Prinzipien](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Wahrnehmbar (Perceivable), Bedienbar (Operable), Verständlich (Understandable) und Robust.

| Prinzip | Definition |
| --- | --- |
| Wahrnehmbar (Perceivable) | Informationen und Komponenten der Benutzeroberfläche müssen den Nutzer:innen so präsentiert werden, dass sie diese wahrnehmen können.<br><br>Nutzer:innen müssen die dargestellten Informationen wahrnehmen können (sie dürfen nicht für alle Sinne unsichtbar sein). |
| Bedienbar (Operable) | Komponenten der Benutzeroberfläche und die Navigation müssen bedienbar sein.<br><br>Nutzer:innen müssen die Schnittstelle bedienen können (die Schnittstelle darf keine Interaktion erfordern, die Nutzer:innen nicht ausführen können). |
| Verständlich (Understandable) | Informationen und die Bedienung der Benutzeroberfläche müssen verständlich sein.<br><br>Nutzer:innen müssen die Informationen sowie die Bedienung der Benutzeroberfläche verstehen können (der Inhalt oder die Bedienung darf nicht über ihr Verständnis hinausgehen). |
| Robust | Inhalte müssen robust genug sein, um von einer Vielzahl von Benutzeragenten, einschließlich assistiver Technologien, zuverlässig interpretiert werden zu können.<br><br>Nutzer:innen müssen auf die Inhalte zugreifen können, auch wenn sich Technologien weiterentwickeln (wenn sich Technologien und Benutzeragenten weiterentwickeln, sollten die Inhalte weiterhin barrierefrei zugänglich bleiben). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="POUR-Kategorien" }

#### Schweregrade {#severity-levels}

Inbox Vision klassifiziert Barrierefreiheitsprobleme nach Schweregrad, um Ihnen bei der Priorisierung der Behebung zu helfen.

| Status | Definition |
| --- | --- |
| Kritisch | Probleme, die den Zugang zu Inhalten oder Funktionen für Nutzer:innen mit Behinderungen blockieren können. Diese sind am schwerwiegendsten und sollten vorrangig behoben werden. |
| Schwerwiegend | Probleme, die erhebliche Barrieren verursachen können, den Zugang aber möglicherweise nicht vollständig blockieren. Diese sollten zeitnah behoben werden. |
| Mäßig | Probleme, die bei Nutzer:innen mit Behinderungen Schwierigkeiten verursachen können, den Zugang jedoch weniger wahrscheinlich vollständig blockieren. |
| Geringfügig | Probleme, die eine relativ geringe Auswirkung auf die Barrierefreiheit haben und möglicherweise nur geringfügige Unannehmlichkeiten verursachen. |
| Überprüfung erforderlich | Es kann nicht automatisch erkannt werden, ob ein Problem vorliegt oder nicht. Dies kann auftreten, wenn das Kontrastverhältnis nicht ermittelt werden kann, da der Text auf einem Hintergrundbild platziert ist. Sie müssen manuell prüfen, da eine automatische Bestimmung nicht möglich ist. |
| Bestanden | WCAG A, AA oder Best Practices für Barrierefreiheit bestanden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schweregrade" }

{% alert important %}
Der Drag-and-Drop-Editor unterstützt das Setzen eines `<title>`-Elements im Dokument nicht, daher schlägt der Barrierefreiheitsscanner bei dieser Prüfung immer fehl.<br><br>Diese Einschränkung wird für zukünftige Verbesserungen verfolgt. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="the drag-and-drop editor document title limitation in Inbox Vision" %}
{% endalert %}

### Automatisierte Barrierefreiheitstests verstehen {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## Best Practices {#best-practices}

### Überprüfen Sie Ihre E-Mail-Abonnent:innenliste {#review-your-email-subscriber-list}

Nutzen Sie das [E-Mail-Insights-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-insights-dashboard), um die beliebtesten Gerätetypen und Anbieter zu ermitteln, bei denen Ihre Abonnent:innen aktiv sind.

Wenn Sie mehr Granularität benötigen, z. B. Browser, Gerätemodell und mehr, können Sie Ihre [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Daten oder den [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) nutzen, um dieses Detailniveau über das aktuelle E-Mail-Engagement Ihrer Nutzer:innen abzurufen.

### Aussagekräftige und betroffene Vorschauen auswählen {#select-meaningful-previews-and-impacted-previews}

Wenn Ihr Unternehmen hauptsächlich in den USA ansässig ist, gibt es möglicherweise bestimmte Vorschauen – wie internationale Vorschauen z. B. GMX.de –, die nur von einer geringen Anzahl an Nutzer:innen verwendet werden. Wir empfehlen, Postfächer mit einer nennenswerten Abonnent:innen-Reichweite zu priorisieren und zu optimieren und Ihre Vorschauen für Postfächer mit höherem Einfluss zu reservieren.

Wenn Sie Korrekturen vornehmen, die bestimmte Vorschauen betreffen, achten Sie darauf, nur die betroffenen Vorschauen auszuwählen, um den Verbrauch ungenutzter Vorschauen zu vermeiden.

### Inbox Vision bei der finalen E-Mail-Version ausführen {#run-inbox-vision-on-the-final-email-version}

Wir empfehlen, Inbox Vision auszuführen, wenn die E-Mail-Nachricht produktionsreif oder nahezu fertig ist. So können Sie die Anzahl der generierten Vorschauen reduzieren, da die E-Mail mehrere Iterationen durchläuft, bevor sie finalisiert und zum Versand an Nutzer:innen bereit ist.

Inbox Vision bei jeder einzelnen Bearbeitung oder Änderung auszuführen, kann schnell Vorschauen verbrauchen. Wir empfehlen, zunächst alle notwendigen Änderungen an der E-Mail vorzunehmen und dann Inbox Vision auszuführen, um eine Vorschau zu erhalten, wie sich all Ihre Änderungen auf das Rendering Ihrer E-Mail in verschiedenen Umgebungen auswirken können.

Braze führt Tests über tatsächliche E-Mail-Clients durch und stellt sicher, dass die Darstellungen korrekt sind. Braze zeigt standardmäßig die Top 20 Vorschauen basierend auf allgemeinen Branchen- und Expertendaten an, die den Großteil der Umgebungen abdecken, in denen Ihre Nutzer:innen mit Ihren E-Mails interagieren. Wenn Ihre Datenanalyse auf andere, beliebtere Vorschauen hinweist, können Sie jedes Mal, wenn Sie Inbox Vision ausführen, einen Standardsatz von Vorschauen definieren.

Wenn Sie regelmäßig ein Problem mit einem Client feststellen, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Fehlerbehebung bei iframe-lastigen Clients {#troubleshoot-iframe-heavy-clients}

Einige E-Mail-Clients, darunter GMX, rendern Nachrichten innerhalb von iframes und können CSS in `<style>`-Blöcken entfernen oder ignorieren. Wenn Inbox Vision oder Live-Sendungen fehlende Styles in diesen Clients anzeigen:

- Verwenden Sie tabellenbasierte Layouts anstelle von CSS-positionierten Layouts.
- Wenden Sie kritische Styles als Inline-`style`-Attribute auf die betroffenen Elemente an.
- Beachten Sie, dass **Auf Desktop ausblenden** und **Auf Mobilgerät ausblenden** auf Media Queries im `<style>`-Block basieren und daher in diesen Clients möglicherweise nicht funktionieren – Inhalte, die per Viewport ausgeblendet werden, können in beiden Ansichten erscheinen.

Testen Sie vor dem Senden die aktualisierte Nachricht in Inbox Vision mit der Vorschau des betroffenen Clients.

### Testgenauigkeit im Vergleich zu Live-Postfächern {#test-accuracy-versus-live-inboxes}

Eine gesendete Nachricht kann anders aussehen als die Editor-Vorschau, da Anbieter denselben HTML-Code unterschiedlich interpretieren. Laden Sie eine Kopie des gesendeten HTML-Codes herunter, um sie zu vergleichen, und verwenden Sie CSS-Inlining, wenn Clients `<style>`-Blöcke entfernen.

#### Leere E-Mail-Inhalte {#blank-email-bodies}

Wenn Empfänger:innen leere E-Mail-Inhalte melden, aber den Absendernamen oder die Betreffzeile noch sehen können:

1. Bestätigen Sie, welche E-Mail-Clients betroffen sind.
2. Verwenden Sie Inbox Vision, um die Variante in diesen Clients zu testen und HTML- oder CSS-Kompatibilitätsprobleme zu identifizieren.
3. Wenn ein Client `<style>`-Blöcke entfernt, fügen Sie `style`-Attribute zu den betroffenen HTML-Elementen hinzu. Weitere Informationen zum Inlining-Verhalten und seinen Einschränkungen finden Sie unter [CSS-Inlining]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline). In Gmail kann zu viel CSS dazu führen, dass der gesamte `<style>`-Block verworfen wird, was eine häufige Ursache für leere E-Mail-Inhalte ist.
4. Im HTML-Editor können Sie außerdem **Inline-CSS aktivieren** unter **Sendeinformationen** > **Erweitert** einschalten, um Stylesheet-Regeln für die gesamte Nachricht inline einzubetten. Diese Option ist nicht für Drag-and-Drop-E-Mails verfügbar, die vom Editor bereits inline eingebettet werden.
5. Testen Sie erneut in Inbox Vision, bevor Sie zukünftige Campaigns versenden.