---
nav_title: E-Mail-Template erstellen
article_title: E-Mail-Template erstellen
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Sie E-Mail-Templates erstellen, anpassen und verwalten."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# E-Mail-Template erstellen {#create-an-email-template}

> Das Braze-Dashboard verfügt über einen E-Mail-Template-Editor, mit dem Sie individuell gestaltete, ansprechende E-Mails erstellen und für die spätere Verwendung in Kampagnen speichern können. Sie können auch Ihr eigenes [HTML-E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template/) hochladen.

## 1. Schritt: Zum E-Mail-Template-Editor navigieren {#step-1-navigate-to-the-email-template-editor}

Gehen Sie im Braze-Dashboard zu **Content** > **Email**.

## 2. Schritt: Bearbeitungsmodus auswählen {#step-2-select-your-editing-experience}

Wählen Sie zwischen **Drag-and-drop Editor** oder **HTML code editor** für Ihren Bearbeitungsmodus.

Sie können auch aus vorgefertigten Braze-Templates wählen, ein neues Template erstellen oder ein bestehendes Template bearbeiten (einfach oder [mobil-responsiv]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)).

![Ein E-Mail-Template für den Frühlingsverkauf eines Unternehmens mit Optionen zur Auswahl des Drag-and-drop-Editors oder HTML-Editors oder zur Auswahl aus Braze-Templates.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Bestehende benutzerdefinierte HTML-Templates müssen mit dem Drag-and-drop-Editor neu erstellt werden.
{% endalert %}

## 3. Schritt: Ihr Template anpassen {#step-3-customize-your-template}

Nachdem Sie Ihren Bearbeitungsmodus ausgewählt haben, können Sie Ihr E-Mail-Template kreativ gestalten. Sie können HTML verwenden, um Ihr Branding im HTML-Editor zu erstellen und nachzubilden, oder eine Vielzahl von [kreativen Details]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/#creative-details) im Drag-and-drop-Editor einfügen.

### Abmeldelink einfügen {#include-an-unsubscribe-link}

Wenn Sie beim Entwerfen Ihres E-Mail-Templates keinen Abmeldelink einfügen, wird Braze Sie auffordern, diesen in Ihre E-Mail einzufügen, da er für alle Marketing-E-Mails gesetzlich vorgeschrieben ist. Sie können diesen Abmeldelink als Fußzeile am Ende Ihrer E-Mails hinzufügen, indem Sie den Liquid-Tag {% raw %}``${email_footer}``{% endraw %} verwenden oder die [Fußzeile anpassen]({{site.baseurl}}/user_guide/channels/email/subscriptions/#custom-footer) in Ihrem Template.

## 4. Schritt: Auf E-Mail-Fehler prüfen {#step-4-check-for-email-errors}

E-Mail-Fehler werden im Tab **Verfassen** des Nachrichten-Workflows angezeigt. Fehler verhindern, dass Sie fortfahren können. „Warnungen“ sind Hinweise, die Ihnen helfen, Best Practices einzuhalten. Je nach Ihren geschäftlichen Anforderungen können Sie diese ignorieren.

![Fehler- und Warnungsliste aus einer Beispiel-E-Mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Hier ist eine Liste der Fehler, die in unserem Editor berücksichtigt werden:

- Fehlerhafte Liquid-Syntax
- [E-Mail-Textkörper größer als 400 KB; es wird dringend empfohlen, dass Textkörper weniger als 102 KB groß sind]({{site.baseurl}}/user_guide/channels/email/best_practices/)
- Templates ohne Abmeldelink
- E-Mails mit leerem **Textkörper** oder **Betreff**
- E-Mails ohne Abmeldelink

## 5. Schritt: Vorschau anzeigen und Nachricht testen {#step-5-preview-and-test-your-message}

Nachdem Sie Ihr Template fertiggestellt haben, können Sie es vor dem Versand testen.

Wählen Sie am unteren Rand des Übersichtsbildschirms **Preview and Test** aus. Hier können Sie eine Vorschau anzeigen, wie Ihre E-Mail im Posteingang einer Kund:in erscheint. Mit der ausgewählten Option **Preview as User** können Sie Ihre E-Mail als zufällige:r Nutzer:in anzeigen, eine:n bestimmte:n Nutzer:in auswählen oder eine:n benutzerdefinierte:n Nutzer:in erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie erwartet funktionieren.

Anschließend können Sie **Copy preview link** auswählen, um einen teilbaren Vorschaulink zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussieht. Der Link ist sieben Tage gültig, bevor er neu generiert werden muss.

Sie können auch zwischen Desktop-, Mobil- und Nur-Text-Ansichten wechseln, um einen Eindruck davon zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheint.

{% alert tip %}
Möchten Sie wissen, wie Ihre E-Mail für Nutzer:innen im Dark Mode aussieht? Wählen Sie den Schalter **Dark Mode Preview** im Abschnitt **Preview and Test** aus (nur im Drag-and-drop-Editor).
{% endalert %}

Wenn Sie bereit für eine abschließende Prüfung sind, wählen Sie **Test Send** und senden Sie eine Testnachricht an sich selbst oder eine Gruppe von Inhaltstester:innen, um sicherzustellen, dass Ihre E-Mail auf verschiedenen Geräten und E-Mail-Clients korrekt angezeigt wird.

![Beispiel einer E-Mail-Vorschau, die zum Testen gesendet werden soll.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Sie Probleme mit Ihrem Template feststellen oder Änderungen vornehmen möchten, wählen Sie **Edit Email**, um zum Editor zurückzukehren. Beachten Sie, dass Änderungen, die im **Classic**-Editor vorgenommen werden, möglicherweise nicht im HTML-Editor oder in der E-Mail-Vorschau angezeigt werden.

## 6. Schritt: Template speichern {#step-6-save-your-template}

Speichern Sie Ihr Template unbedingt, indem Sie **Save Template** auswählen. Sie können dieses Template jetzt in jeder Kampagne oder Canvas-Komponente verwenden. Um auf Ihr Template zuzugreifen, wählen Sie den Bearbeitungsmodus aus, mit dem Sie es erstellt haben, und wählen Sie es dann aus der Liste der verfügbaren Templates aus.

{% alert note %}
Wenn Sie Änderungen an einem bestehenden Template vornehmen, werden diese Änderungen nicht in Kampagnen übernommen, die mit früheren Versionen dieses Templates erstellt wurden.
{% endalert %}

### Ihre Templates verwalten {#manage-your-templates}

Sie können E-Mail-Templates unter **Templates** > **Email Templates** anzeigen und nach Status, Typ, Tags, der erstellenden Person filtern oder nach Template-Name suchen. Sie benötigen die entsprechenden Nutzer:innenberechtigungen, wie z. B. **View Email Templates**, um diese Templates anzuzeigen. Weitere Details finden Sie unter [Nutzer:innenberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).

Wenn Sie mehr E-Mail-Templates erstellen, können Sie E-Mail-Templates [duplizieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#duplicate-templates) und [archivieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#archive-templates). Erfahren Sie mehr über das Erstellen und Verwalten Ihrer Template- und Kreativinhalte-Bibliothek unter [Templates und Medien]({{site.baseurl}}/user_guide/messaging/templates/).

### Ihre Templates in API-Kampagnen verwenden {#use-your-templates-in-api-campaigns}

Um Ihre E-Mail für eine API-Kampagne zu verwenden, benötigen Sie eine `email_template_id`, die Sie am unteren Rand jedes in Braze erstellten E-Mail-Templates finden.

![API-Bezeichner am unteren Rand eines E-Mail-Templates.]({% image_buster /assets/img/email_templates/template5.png %})

### E-Mail-Templates kommentieren {#comment-on-email-templates}

Sie können im Drag-and-drop-Editor an E-Mail-Templates zusammenarbeiten und diese kommentieren.

1. Wählen Sie den Content-Block oder die Zeile im E-Mail-Textkörper aus, die Sie kommentieren möchten.
2. Wählen Sie das <i class="fas fa-comment" aria-label="Kommentar"></i> Kommentarsymbol aus.
3. Geben Sie Ihren Kommentar in der Seitenleiste ein und wählen Sie dann **Submit** aus.
4. Nachdem Sie Ihre Kommentare eingegeben haben, wählen Sie **Done** aus.
5. Wählen Sie **Save Template** aus, um Ihre Kommentare zu speichern.

Nachdem Ihr Template gespeichert wurde, können Nutzer:innen Symbole über unbearbeiteten Kommentaren sehen. Wählen Sie **Resolve** aus, um diese Kommentare zu lösen.

![Ein E-Mail-Template-Kommentar mit dem Text „Sieht gut aus für mich“.]({% image_buster /assets/img/email_templates/template_comment.png %})

Antworten auf häufig gestellte Fragen zu E-Mail-Templates finden Sie in unseren [Template-FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq/).