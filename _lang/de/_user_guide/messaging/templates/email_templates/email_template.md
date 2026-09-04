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

> Das Braze-Dashboard verfügt über einen E-Mail-Template-Editor, mit dem Sie individuell gestaltete, ansprechende E-Mails erstellen und für die spätere Verwendung in Campaigns speichern können. Sie können auch Ihr eigenes [HTML-E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) hochladen.

## Schritt 1: Zum E-Mail-Template-Editor navigieren {#step-1-navigate-to-the-email-template-editor}

Gehen Sie im Braze-Dashboard zu **Content** > **E-Mail**.

## Schritt 2: Bearbeitungserfahrung auswählen {#step-2-select-your-editing-experience}

Wählen Sie zwischen dem **Drag-and-drop Editor** oder dem **HTML code editor** für Ihre Bearbeitungserfahrung.

Sie können auch aus vorgefertigten Braze-Templates wählen, ein neues Template erstellen oder ein bestehendes Template bearbeiten (einfach oder [mobil responsiv]({{site.baseurl}}/releases/2018/may#mobile-responsive-email-templates)).

![Ein E-Mail-Template für den Frühlingsverkauf eines Unternehmens mit Optionen zur Auswahl des Drag-and-drop-Editors oder des HTML-Editors sowie zur Auswahl aus Braze-Templates.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Bestehende benutzerdefinierte HTML-Templates müssen mit dem Drag-and-drop-Editor neu erstellt werden.
{% endalert %}

## Schritt 3: Template anpassen {#step-3-customize-your-template}

Nachdem Sie Ihren Editor ausgewählt haben, können Sie Ihr E-Mail-Template kreativ gestalten. Sie können HTML verwenden, um Ihr Branding im HTML-Editor zu erstellen und nachzubilden, oder eine Vielzahl von [kreativen Details]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) im Drag-and-Drop-Editor einfügen.

### Abmeldelink einfügen {#include-an-unsubscribe-link}

Wenn Sie beim Gestalten Ihres E-Mail-Templates keinen Abmeldelink einfügen, wird Braze Sie auffordern, diesen in Ihre E-Mail aufzunehmen, da er bei allen Marketing-E-Mails gesetzlich vorgeschrieben ist. Sie können diesen Abmeldelink als Fußzeile am Ende Ihrer E-Mails hinzufügen, indem Sie den Liquid-Tag {% raw %}``${email_footer}``{% endraw %} verwenden oder die [Fußzeile anpassen]({{site.baseurl}}/user_guide/channels/email/subscriptions#custom-footer) in Ihrem Template.

## Schritt 4: E-Mails auf Fehler überprüfen {#step-4-check-for-email-errors}

E-Mail-Fehler werden im Tab **Compose** des Nachrichten-Workflows angezeigt. Fehler verhindern, dass Sie mit dem nächsten Schritt fortfahren können. „Warnungen“ sind Hinweise, die Ihnen helfen, Best Practices einzuhalten. Je nach Ihren geschäftlichen Anforderungen können Sie diese ignorieren.

![Fehler- und Warnungsliste aus einer Beispiel-E-Mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Hier ist eine Liste der Fehler, die in unserem Editor berücksichtigt werden:

- Fehlerhafte Liquid-Syntax
- [E-Mail-Textkörper größer als 400 KB; es wird dringend empfohlen, unter 102 KB zu bleiben]({{site.baseurl}}/user_guide/channels/email/best_practices)
- Templates ohne Abmelde-Link
- E-Mails mit leerem **Body** oder **Subject**
- E-Mails ohne Abmelde-Link

## Schritt 5: Vorschau anzeigen und Nachricht testen {#step-5-preview-and-test-your-message}

Nachdem Sie Ihr Template fertig erstellt haben, können Sie es vor dem Versand testen.

Wählen Sie am unteren Rand des Übersichtsbildschirms **Preview and Test** aus. Hier können Sie eine Vorschau anzeigen, wie Ihre E-Mail im Posteingang einer Kund:in erscheint. Wenn **Preview as User** ausgewählt ist, können Sie Ihre E-Mail als zufällige:r Nutzer:in in der Vorschau anzeigen, eine:n bestimmte:n Nutzer:in auswählen oder eine:n angepasste:n Nutzer:in erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie gewünscht funktionieren.

Anschließend können Sie **Copy preview link** auswählen, um einen teilbaren Vorschau-Link zu erstellen und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussieht. Weitere Informationen finden Sie unter [Teilbare Vorschau]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

Sie können auch zwischen den Ansichten für Desktop, Mobilgerät und Nur-Text wechseln, um einen Eindruck davon zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten dargestellt wird.

{% alert tip %}
Sie möchten wissen, wie Ihre E-Mail für Nutzer:innen im Dark Mode aussieht? Wählen Sie den Umschalter **Dark Mode Preview** im Bereich **Preview and Test** aus (nur im Drag-and-Drop-Editor verfügbar).
{% endalert %}

Wenn Sie bereit für eine abschließende Prüfung sind, wählen Sie **Test Send** aus und senden Sie eine Testnachricht an sich selbst oder eine Gruppe von Testpersonen, um sicherzustellen, dass Ihre E-Mail auf verschiedenen Geräten und E-Mail-Clients korrekt dargestellt wird.

![Beispiel einer E-Mail-Vorschau, die zum Testen gesendet wird.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Ihnen Probleme mit Ihrem Template auffallen oder Sie Änderungen vornehmen möchten, wählen Sie **Edit Email** aus, um zum Editor zurückzukehren. Beachten Sie, dass Änderungen, die im **Classic**-Editor vorgenommen werden, möglicherweise nicht im HTML-Editor oder in der E-Mail-Vorschau angezeigt werden.

## Schritt 6: Template speichern {#step-6-save-your-template}

Speichern Sie Ihr Template, indem Sie **Save Template** auswählen. Sie können dieses Template jetzt in jeder Campaign oder Canvas-Komponente verwenden. Um auf Ihr Template zuzugreifen, wählen Sie die Bearbeitungsoberfläche, mit der Sie es erstellt haben, und wählen Sie es dann aus der Liste der verfügbaren Templates aus.

{% alert note %}
Wenn Sie Änderungen an einem bestehenden Template vornehmen, werden diese Änderungen nicht in Campaigns übernommen, die mit früheren Versionen dieses Templates erstellt wurden.
{% endalert %}

### Templates verwalten {#manage-your-templates}

Sie können E-Mail-Templates unter **Templates** > **Email Templates** einsehen und nach Status, Typ, Tags, der Person, die sie erstellt hat, filtern oder nach Template-Namen suchen. Sie benötigen die entsprechenden Nutzer:innen-Berechtigungen, wie z. B. **View Email Templates**, um diese Templates einsehen zu können. Weitere Informationen finden Sie unter [Nutzer:innen-Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

Wenn Sie mehr E-Mail-Templates erstellen, können Sie E-Mail-Templates [duplizieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicating-templates) und [archivieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archiving-templates). Erfahren Sie mehr über das Erstellen und Verwalten Ihrer Bibliothek von Templates und kreativen Inhalten unter [Templates und Medien]({{site.baseurl}}/user_guide/messaging/templates).

### Templates in API-Campaigns verwenden {#use-your-templates-in-api-campaigns}

Um Ihre E-Mail für eine API-Campaign zu verwenden, benötigen Sie eine `email_template_id`, die am Ende jedes in Braze erstellten E-Mail-Templates zu finden ist.

![API-Bezeichner am Ende eines E-Mail-Templates.]({% image_buster /assets/img/email_templates/template5.png %})

### E-Mail-Templates kommentieren {#comment-on-email-templates}

Sie können im Drag-and-Drop-Editor gemeinsam an E-Mail-Templates arbeiten und diese kommentieren.

1. Wählen Sie den Content-Block oder die Zeile im E-Mail-Text aus, die Sie kommentieren möchten.
2. Wählen Sie das <i class="fas fa-comment" aria-label="Kommentar"></i> Kommentar-Symbol aus.
3. Geben Sie Ihren Kommentar in der Seitenleiste ein und wählen Sie dann **Submit** aus.
4. Nachdem Sie Ihre Kommentare eingegeben haben, wählen Sie **Done** aus.
5. Wählen Sie **Save Template** aus, um Ihre Kommentare zu speichern.

Nachdem Ihr Template gespeichert wurde, können Nutzer:innen Symbole über unbearbeiteten Kommentaren sehen. Wählen Sie **Resolve** aus, um diese Kommentare zu lösen.

![Ein Kommentar zu einem E-Mail-Template mit dem Text „Looks good to me“.]({% image_buster /assets/img/email_templates/template_comment.png %})

Antworten auf häufig gestellte Fragen zu E-Mail-Templates finden Sie in unseren [Template-FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).