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

## Schritt 1: Ein E-Mail-Präferenzcenter erstellen {#step-1-create-an-email-preference-center}

Erstellen Sie ein Präferenzcenter, indem Sie zu **Zielgruppe** > **E-Mail-Präferenzcenter** navigieren. Hier wird eine Liste benutzerdefinierter Präferenzcenter angezeigt. Wählen Sie **Neu erstellen** aus, um ein neues Präferenzcenter zu erstellen, oder wählen Sie den Namen eines vorhandenen Präferenzcenters aus, um Änderungen vorzunehmen.

## Schritt 2: E-Mail-Präferenzcenter benennen {#step-2-name-the-email-preference-center}

Namen für Präferenzcenter dürfen nur alphanumerische Zeichen, Bindestriche oder Unterstriche enthalten. Der von Ihnen vergebene Name bestimmt die Syntax des generierten Liquid-Tags.

Dieser Liquid-Tag kann in alle ausgehenden E-Mail-Campaigns oder Canvas-Schritte eingefügt werden und leitet Nutzer:innen zum Präferenzcenter weiter.

## Schritt 3: Abo-Gruppen zum Präferenzcenter hinzufügen {#step-3-add-subscription-groups-to-the-preference-center}

Wählen Sie **Launch Editor** aus, um mit der Gestaltung Ihres Präferenzcenters im Drag-and-Drop-Editor zu beginnen.

### Verfügbare Abo-Gruppen festlegen {#define-available-subscription-groups}

Um festzulegen, welche Abo-Gruppen im Präferenzcenter angezeigt werden sollen, wählen Sie den Button **+ Add subscription groups** aus, um ein Modal zu öffnen, in dem die gewünschten Abo-Gruppen ausgewählt werden können. Wählen Sie nach der Auswahl den Button **Add Subscription Groups** aus, um sie zum Präferenzcenter hinzuzufügen.

Sie können die ausgewählten Abo-Gruppen weiter konfigurieren, indem Sie den Smart-Block auswählen und die Block-Eigenschaften anpassen.

- Reihenfolge der Abo-Gruppen anpassen
- Zusätzliche Abo-Gruppen hinzufügen oder entfernen
- Beschreibungen hinzufügen
- Eine Checkbox **Subscribe to all** hinzufügen oder entfernen, die Nutzer:innen für alle in diesem Block angezeigten Abo-Gruppen anmeldet
- Eine Checkbox **Unsubscribe from all** hinzufügen oder entfernen, die Nutzer:innen von allen in diesem Block angezeigten Abo-Gruppen abmeldet

Der Button **Unsubscribe from all** am unteren Rand des Templates kann nicht entfernt werden und [meldet Nutzer:innen global ab]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states), sodass sie keine E-Mail-Nachrichten mehr erhalten.

## Schritt 4: Das Präferenzcenter mit dem Drag-and-Drop-Editor anpassen {#step-4-customize-the-preference-center-using-the-drag-and-drop-editor}

### Gemeinsame Stile festlegen {#set-common-styles}

Sie können bestimmte Stile festlegen, die auf alle relevanten Blöcke in Ihrem Präferenzcenter angewendet werden, indem Sie den Tab **Common Styles** verwenden. Die in diesem Abschnitt festgelegten Stile werden überall in Ihrer Nachricht verwendet, es sei denn, Sie überschreiben sie für einen bestimmten Block. Für ein einfacheres Design-Erlebnis empfehlen wir, zuerst Stile auf Seitenebene einzurichten, bevor Sie Stile auf Blockebene anpassen.

![Ein Beispiel für gemeinsame Stileinstellungen für Text, Buttons und Links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Um zu den gemeinsamen Stilen zurückzukehren, wählen Sie den „X“-Button in den einzelnen Blockeigenschaften aus. Wählen Sie dann den Nachrichtencontainer, den „X“-Button der Nachricht oder den Editor-Hintergrund aus.
{% endalert %}

## Drag-and-Drop-Komponenten für das Präferenzcenter {#drag-and-drop-preference-center-components}

Der Drag-and-Drop-Editor verwendet zwei Schlüsselkomponenten, um die Erstellung des Präferenzcenters schnell und einfach zu gestalten: Zeilen und Blöcke. Alle Blöcke müssen in einer Zeile platziert werden.

{% tabs %}
{% tab Zeilen %}

Zeilen sind strukturelle Einheiten, die die horizontale Zusammensetzung eines Abschnitts der Nachricht mithilfe von Zellen definieren.

![Option zur Auswahl des Zeilentyps in Ihrer Nachricht.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Wenn eine Zeile ausgewählt ist, können Sie im Bereich „Spaltenanpassung“ die Anzahl der benötigten Spalten hinzufügen oder entfernen, um verschiedene Inhaltselemente nebeneinander zu platzieren. Sie können auch die Größe vorhandener Spalten durch Schieben anpassen.

![Optionen zum Anpassen Ihrer Spalteneigenschaften, einschließlich Hintergrundfarbe, Rahmenstil, Rahmenradius und Padding.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Als Best Practice sollten Sie Ihre Zeilen- und Spalteneigenschaften formatieren, bevor Sie Blöcke innerhalb der Zeilen formatieren. Da Sie an vielen Stellen Abstände und Ausrichtung anpassen können, ist es einfacher, von der Grundlage aus zu arbeiten und nach und nach Änderungen vorzunehmen.

{% endtab %}
{% tab Blöcke %}

Blöcke stellen verschiedene Arten von Inhalten dar, die Sie in Ihrer Nachricht verwenden können. Ziehen Sie einen Block in ein vorhandenes Zeilensegment, das sich automatisch an die Zellenbreite anpasst.

![Option zur Auswahl von Blöcken, einschließlich Titel, Absatz, Button, Bild und Abstandshalter.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Jeder Block hat seine eigenen Einstellungen, wie z. B. eine granulare Steuerung des Paddings. Das rechte Panel wechselt automatisch zu einem Styling-Panel für das ausgewählte Inhaltselement. Weitere Informationen finden Sie unter [Editor-Blöcke (Präferenzcenter)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=preference%20center).

Wenn Sie den Custom-Code-Block in Ihrem Präferenzcenter verwenden, werden Inline-Frames im benutzerdefinierten Code möglicherweise nicht generiert, wenn er an Ihre Nutzer:innen zugestellt wird.

{% alert note %}
Content Blocks mit Links können nicht im Drag-and-Drop-Präferenzcenter verwendet werden. Links innerhalb von Content Blocks sind nicht klickbar.
{% endalert %}

{% endtab %}
{% endtabs %}

## Schritt 5: Bestätigungsseite anpassen {#step-5-customize-your-confirmation-page}

Passen Sie als Nächstes die Bestätigungsseite an, indem Sie **Confirmation Page** auswählen. Diese Seite wird Nutzer:innen angezeigt, nachdem sie ihre Präferenzen über das Preference Center aktualisiert haben. Die gleichen Gestaltungsmöglichkeiten aus [Gemeinsame Stile festlegen](#set-common-styles) und [Drag-and-Drop-Preference-Center-Komponenten](#drag-and-drop-preference-center-components) gelten auch für diese Seite.

![Ein Beispiel für eine Bestätigungsseite, die den Nutzer:innen mitteilt, dass ihre Präferenzen aktualisiert wurden.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Schritt 6: Vorschau anzeigen und Präferenzcenter starten {#step-6-preview-and-launch-your-preference-center}

Sie können eine Vorschau Ihres Präferenzcenters anzeigen, indem Sie den Tab **Preview** im Editor auswählen. Die Vorschau zeigt sowohl das Präferenzcenter als auch die Bestätigungsseite.

Die Testfunktionalität ist jedoch deaktiviert. Außerdem erzeugen Testsendungen von Campaigns oder Canvas-Schritten, die den Liquid-Tag des Präferenzcenters enthalten, keinen gültigen Link. Diese Vorschau ermöglicht es Ihnen nicht, Abo-Änderungen zu speichern – sie zeigt nur, wie die Seite aussieht. Informationen zum Testen des Speicherns von Präferenzen finden Sie unter [Präferenzcenter testen](#testing-preference-centers). Nachdem Sie Ihr Präferenzcenter bearbeitet haben, können Sie den Editor schließen, indem Sie den Button **Done** auswählen.

Wählen Sie **Save as Draft**, um später zu diesem Präferenzcenter zurückzukehren, oder wählen Sie **Launch Preference Center**, wenn Sie zufrieden sind.

Beim Starten des Präferenzcenters werden Sie aufgefordert, den Namen zu bestätigen, da dieser nach dem Start nicht mehr bearbeitet werden kann. Nachdem Sie den Namen bestätigt haben, wird das Präferenzcenter gestartet und ist einsatzbereit.

## Preference-Center verwenden {#use-the-preference-center}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Um einen Link zum Preference-Center in Ihren E-Mails zu platzieren, kopieren Sie den Liquid-Tag des gewünschten Preference-Centers, indem Sie das Symbol **Copy Liquid** auswählen.

![Die Option „Copy Liquid“ in der Zeile eines Preference-Centers.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Fügen Sie den Liquid-Tag an der gewünschten Stelle in Ihrer E-Mail ein, ähnlich wie [Abmelde-URLs]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link) eingefügt werden.

{% multi_lang_include preference_center/testing.md %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum funktioniert mein Präferenzcenter bei einem Testversand nicht? {#why-doesnt-my-preference-center-work-in-a-test-send}

Links zum Präferenzcenter erfordern einen Live-Versandkontext. Testversände erzeugen keine gültigen Präferenzcenter-URLs, und der Button **Save Preferences** ist deaktiviert, wenn die Seite geladen wird. Dies ist das erwartete Verhalten. Um End-to-End zu testen, starten Sie eine Campaign oder einen Canvas-Schritt an eine:n Testnutzer:in oder ein kleines internes Segment. Weitere Informationen finden Sie unter [Präferenzcenter testen](#testing-preference-centers).

## Fehler behandeln {#handle-errors}

Wenn ein Fehler auftritt, während Nutzer:innen **Speichern** in einem Präferenzcenter auswählen, wird ihnen die folgende Standard-Fehlermeldung angezeigt, die im Editor nicht angepasst oder gestaltet werden kann. Die Lokalisierung der Fehlermeldungen wird auf diesen Seiten jedoch weiterhin unterstützt.

![Ein Fehler mit dem Hinweis „Beim Speichern Ihrer Einstellungen ist ein Problem aufgetreten. Bitte versuchen Sie es erneut.“]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}