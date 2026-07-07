---
nav_title: Drag-and-Drop-E-Mail-Präferenzzentrum
article_title: Drag-and-Drop-E-Mail-Präferenzzentrum
alias: "/dnd_preference_center/"
description: "Diese Referenzseite beschreibt, wie Sie ein E-Mail-Präferenzzentrum mit dem Drag-and-Drop-Editor erstellen."
page_order: 2
---

# Ein E-Mail-Präferenzzentrum mit Drag-and-Drop erstellen {#create-an-email-preference-center-with-drag-and-drop}

> Mit dem Drag-and-Drop-Editor können Sie ein Präferenzzentrum erstellen und anpassen, um zu verwalten, welche Nutzer:innen bestimmte Arten von Kommunikation erhalten. Sie können bis zu 100 Präferenzzentren pro Workspace haben.

Sie können bestehende Drag-and-Drop-Präferenzzentren unter **Zielgruppe** > **E-Mail-Präferenzzentren** verwalten:

- Um den Namen oder Inhalt eines Präferenzzentrums zu ändern, öffnen Sie das Präferenzzentrum im Dashboard.
- Drag-and-Drop-Präferenzzentren können nicht über das Dashboard gelöscht werden. Um eines zu entfernen, entfernen Sie zunächst seinen Liquid-Tag aus allen E-Mail-Campaigns oder Canvas-Schritten und kontaktieren Sie dann den [Braze-Support]({{site.baseurl}}/support_contact).
- Wenn ein entferntes Präferenzzentrum in zuvor gesendeten Nachrichten verwendet wurde, funktioniert es in diesen zugestellten E-Mails nicht mehr.
{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## 1. Schritt: Ein E-Mail-Präferenzzentrum erstellen {#step-1-create-an-email-preference-center}

Erstellen Sie ein Präferenzzentrum, indem Sie zu **Zielgruppe** > **E-Mail-Präferenzzentren** navigieren.

Hier wird eine Liste benutzerdefinierter Präferenzzentren angezeigt. Wählen Sie **Neu erstellen**, um ein neues Präferenzzentrum zu erstellen, oder wählen Sie den Namen eines bestehenden, um Änderungen vorzunehmen.


## 2. Schritt: Das E-Mail-Präferenzzentrum benennen {#step-2-name-the-email-preference-center}

Namen von Präferenzzentren dürfen nur alphanumerische Zeichen, Bindestriche oder Unterstriche enthalten. Der von Ihnen angegebene Name bestimmt die Syntax des generierten Liquid-Tags.

Dieser Liquid-Tag kann in alle ausgehenden E-Mail-Campaigns oder Canvas-Schritte eingefügt werden und leitet Nutzer:innen zum Präferenzzentrum weiter.


## 3. Schritt: Abo-Gruppen zum Präferenzzentrum hinzufügen {#step-3-add-subscription-groups-to-the-preference-center}

Wählen Sie **Editor starten**, um mit der Gestaltung Ihres Präferenzzentrums im Drag-and-Drop-Editor zu beginnen.

### Verfügbare Abo-Gruppen definieren {#define-available-subscription-groups}

Um festzulegen, welche Abo-Gruppen im Präferenzzentrum angezeigt werden sollen, wählen Sie die Schaltfläche **+ Abo-Gruppen hinzufügen**, um ein Modal zu öffnen, in dem die gewünschten Abo-Gruppen ausgewählt werden können. Wählen Sie nach der Auswahl die Schaltfläche **Abo-Gruppen hinzufügen**, um sie dem Präferenzzentrum hinzuzufügen.

Sie können die ausgewählten Abo-Gruppen weiter konfigurieren, indem Sie den Smart-Block auswählen und die Block-Eigenschaften anpassen.
- Reihenfolge der Abo-Gruppen anpassen
- Zusätzliche Abo-Gruppen hinzufügen oder entfernen
- Beschreibungen hinzufügen
- Eine Checkbox **Alle abonnieren** hinzufügen oder entfernen, die die Nutzer:innen für alle in diesem Block angezeigten Abo-Gruppen anmeldet
- Eine Checkbox **Von allen abmelden** hinzufügen oder entfernen, die die Nutzer:innen von allen in diesem Block angezeigten Abo-Gruppen abmeldet


Die Schaltfläche **Von allen abmelden** am Ende des Templates kann nicht entfernt werden und meldet Nutzer:innen [global ab]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states), sodass sie keine E-Mail-Nachrichten mehr erhalten.

## 4. Schritt: Das Präferenzzentrum mit dem Drag-and-Drop-Editor anpassen {#step-4-customize-the-preference-center-using-the-drag-and-drop-editor}

### Gemeinsame Stile festlegen {#set-common-styles}

Sie können bestimmte Stile festlegen, die auf alle relevanten Blöcke in Ihrem Präferenzzentrum angewendet werden, und zwar über den Tab **Gemeinsame Stile**. Die in diesem Abschnitt festgelegten Stile werden überall in Ihrer Nachricht verwendet, es sei denn, Sie überschreiben sie für einen bestimmten Block. Für ein einfacheres Design-Erlebnis empfehlen wir, seitenweite Stile einzurichten, bevor Sie Stile auf Block-Ebene anpassen.

![Ein Beispiel für gemeinsame Stileinstellungen für Text, Buttons und Links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Um zu den gemeinsamen Stilen zurückzukehren, wählen Sie die „X“-Schaltfläche bei den einzelnen Block-Eigenschaften. Wählen Sie dann den Nachrichtencontainer, die „X“-Schaltfläche der Nachricht oder den Editor-Hintergrund.
{% endalert %}

## Drag-and-Drop-Präferenzzentrum-Komponenten {#drag-and-drop-preference-center-components}

Der Drag-and-Drop-Editor verwendet zwei Schlüsselkomponenten, um die Erstellung von Präferenzzentren schnell und einfach zu gestalten: Zeilen und Blöcke. Alle Blöcke müssen in einer Zeile platziert werden.

{% tabs %}
{% tab Zeilen %}

Zeilen sind strukturelle Einheiten, die die horizontale Zusammensetzung eines Abschnitts der Nachricht mithilfe von Zellen definieren.

![Option zur Auswahl des Zeilentyps in Ihrer Nachricht.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Wenn eine Zeile ausgewählt ist, können Sie im Abschnitt „Spaltenanpassung“ die Anzahl der benötigten Spalten hinzufügen oder entfernen, um verschiedene Inhaltselemente nebeneinander zu platzieren. Sie können auch die Größe bestehender Spalten durch Verschieben anpassen.

![Optionen zur Anpassung Ihrer Spalteneigenschaften, einschließlich Hintergrundfarbe, Rahmenstil, Rahmenradius und Padding.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Als Best Practice sollten Sie Ihre Zeilen- und Spalteneigenschaften formatieren, bevor Sie Blöcke innerhalb der Zeilen formatieren. Sie können Abstände und Ausrichtung an vielen Stellen anpassen, daher erleichtert es das Bearbeiten, wenn Sie mit dem Fundament beginnen.

{% endtab %}
{% tab Blöcke %}

Blöcke repräsentieren verschiedene Arten von Inhalten, die Sie in Ihrer Nachricht verwenden können. Ziehen Sie einen in ein bestehendes Zeilensegment, das sich automatisch an die Zellenbreite anpasst.

![Option zur Auswahl von Blöcken, einschließlich Titel, Absatz, Button, Bild und Abstandshalter.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Jeder Block hat seine eigenen Einstellungen, wie z. B. eine granulare Steuerung des Paddings. Das rechte Panel wechselt automatisch zu einem Styling-Panel für das ausgewählte Inhaltselement. Weitere Informationen finden Sie unter [Editor-Blöcke (Präferenzzentrum)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=preference%20center).

Wenn Sie den Custom-Code-Block in Ihrem Präferenzzentrum verwenden, werden Inline-Frames möglicherweise nicht im benutzerdefinierten Code generiert, wenn er an Ihre Nutzer:innen zugestellt wird.

{% endtab %}
{% endtabs %}

## 5. Schritt: Ihre Bestätigungsseite anpassen {#step-5-customize-your-confirmation-page}

Vergessen Sie nicht, die Bestätigungsseite anzupassen! Sie können diese Seite bearbeiten, indem Sie **Bestätigungsseite** oben im Drag-and-Drop-Editor-Fenster auswählen. Diese Seite wird Nutzer:innen angezeigt, nachdem sie ihre Präferenzen über das Präferenzzentrum aktualisiert haben. Die gleichen oben beschriebenen Styling-Möglichkeiten gelten auch für diese Seite.

![Ein Beispiel für eine Bestätigungsseite, die den Nutzer:innen mitteilt, dass ihre Präferenzen aktualisiert wurden.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## 6. Schritt: Vorschau anzeigen und Präferenzzentrum starten {#step-6-preview-and-launch-your-preference-center}

Sie können eine Vorschau Ihres Präferenzzentrums anzeigen, indem Sie den Tab **Vorschau** im Editor auswählen. Die Testfunktionalität ist jedoch deaktiviert. Nachdem Sie Ihr Präferenzzentrum bearbeitet haben, können Sie den Editor schließen, indem Sie die Schaltfläche **Fertig** auswählen.

Sie sehen eine Vorschau sowohl des Präferenzzentrums als auch der Bestätigungsseite. Wählen Sie **Als Entwurf speichern**, um später zu diesem Präferenzzentrum zurückzukehren, oder wählen Sie **Präferenzzentrum starten**, wenn Sie zufrieden sind.

Beim Starten des Präferenzzentrums werden Sie aufgefordert, den Namen zu bestätigen, da er nach dem Start nicht mehr bearbeitet werden kann. Nachdem Sie den Namen bestätigt haben, wird das Präferenzzentrum gestartet und ist einsatzbereit.

## Das Präferenzzentrum verwenden {#using-the-preference-center}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Um einen Link zum Präferenzzentrum in Ihren E-Mails zu platzieren, kopieren Sie den Liquid-Tag des gewünschten Präferenzzentrums, indem Sie das Symbol **Liquid kopieren** auswählen.

![Die Option „Liquid kopieren“ in der Zeile eines Präferenzzentrums.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Fügen Sie den Liquid-Tag an der gewünschten Stelle in Ihrer E-Mail ein, ähnlich wie [Abmelde-URLs]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link) eingefügt werden.

## Fehlerbehandlung {#handling-errors}

Wenn ein Fehler auftritt, wenn Nutzer:innen **Speichern** in einem Präferenzzentrum auswählen, wird ihnen die folgende Standard-Fehlermeldung angezeigt, die im Editor nicht angepasst oder gestaltet werden kann. Die Lokalisierung der Fehlermeldungen wird auf diesen Seiten jedoch weiterhin unterstützt.

![Eine Fehlermeldung mit dem Hinweis „Beim Speichern Ihrer Präferenzen ist ein Problem aufgetreten. Bitte versuchen Sie es erneut.“]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}