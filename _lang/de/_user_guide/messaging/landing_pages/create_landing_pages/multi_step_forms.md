---
nav_title: Mehrstufige Formulare
article_title: Mehrstufige Landing-Page-Formulare
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie ein mehrstufiges Formular auf einer Braze Landing-Page erstellen, Schritte im Drag-and-Drop-Editor verwalten und den integrierten Bestätigungsschritt anpassen."
---

# Mehrstufige Landing-Page-Formulare {#multi-step-landing-page-forms}

> Teilen Sie ein langes Landing-Page-Formular in mehrere Schritte auf, jeder mit eigenen Feldern, sodass Nutzer:innen Ihr Formular Schritt für Schritt durchlaufen. Jedes mehrstufige Formular enthält einen gesperrten Bestätigungsschritt, damit Nutzer:innen nach dem Absenden immer eine Bestätigung sehen.

## Voraussetzungen {#prerequisites}

Um auf den Landing-Page-Builder zuzugreifen, benötigen Sie [bestimmte Berechtigungen]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Falls Sie keinen Zugriff haben, wenden Sie sich an Ihre:n Braze-Admin.

Sie sollten außerdem mit [Landing-Page-Formularblöcken]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) vertraut sein.

## So funktionieren mehrstufige Formulare {#how-multi-step-forms-work}

Um ein mehrstufiges Formular zu erstellen, fügen Sie eine **Formular**-Zeile aus dem Bereich **Layout** im **Build**-Panel hinzu. Die **Formular**-Zeile enthält integrierte Aktions-Buttons und Unterstützung für mehrere Schritte, sodass Sie die Zeilenstruktur nicht selbst zusammenstellen müssen.

Sie können pro Landing-Page nur eine **Formular**-Zeile hinzufügen. Wenn Sie sie auf Ihre Seite ziehen, beginnt sie mit einem einzelnen Schritt und einem gesperrten Bestätigungsschritt, der nach dem Absenden ausgeführt wird.

{% alert note %}
Da die **Formular**-Zeile ihre eigene mehrstufige Navigation verwaltet, befinden sich alle Ihre Schritte innerhalb dieser einzelnen Zeile auf einer Seite. Dies unterscheidet sich vom Standardansatz, bei dem ein einstufiges Formular erstellt und dessen **Absenden**-Button mit einer separaten Bestätigungs-Landing-Page verknüpft wird. Weitere Informationen finden Sie unter [Schritt 4: Bestätigungsseite erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional).
{% endalert %}

![Ein mehrstufiges Landing-Page-Formular im Landing-Page-Composer.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## Mehrstufiges Formular hinzufügen {#add-a-multi-step-form}

1. Gehen Sie im Landing-Page-Editor zum Panel **Build** und wählen Sie **Layout** aus.
2. Ziehen Sie die Zeile **Form** auf Ihre Seite.
3. Verwenden Sie bei ausgewählter Zeile **Form** den Abschnitt **Steps** im Eigenschaftenpanel auf der rechten Seite, um Ihr Formular aufzubauen:
   - Fügen Sie [Formularblöcke]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) (wie **Email Capture**, **Phone Capture**, **Input Field**, **Dropdown**, **Checkbox** oder **Checkbox Group**) zu **Step 1** hinzu.
   - Wählen Sie **Add step** aus, um weitere Schritte zu erstellen, und fügen Sie jedem Schritt Formularblöcke hinzu.

Ein dreistufiges Formular könnte beispielsweise in **Step 1** nach einem Namen fragen, in **Step 2** nach einer Telefonnummer und dann auf dem Schritt **Confirmation** landen, um den Nutzer:innen für das Absenden zu danken.

## Zwischen Schritten beim Bearbeiten navigieren {#navigate-between-steps-while-editing}

Bewegen Sie sich im Editor auf zwei Arten zwischen den Schritten:

| Methode | Vorgehensweise |
|--------|--------|
| Schritt-Navigator | Verwenden Sie im Canvas die Steuerung **Schritt X von Y**, um zum vorherigen oder nächsten Schritt zu wechseln. |
| Schritte-Panel | Wählen Sie die Zeile **Formular** aus und verwenden Sie dann den Abschnitt **Schritte** im Eigenschaften-Panel auf der rechten Seite, um direkt zu einem Schritt zu springen, einschließlich des Schritts **Bestätigung**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zwischen Schritten beim Bearbeiten navigieren" }

## Schritte verwalten {#manage-steps}

Verwenden Sie den Bereich **Steps** im Eigenschafts-Panel der Zeile **Form**, um Schritte hinzuzufügen, zu entfernen und neu anzuordnen:

| Aktion | Vorgehensweise |
|--------|----------------|
| Schritt hinzufügen | Wählen Sie **Add step** aus. Neue Schritte werden nach Ihren bestehenden Schritten und vor dem Schritt **Confirmation** hinzugefügt. |
| Schritt entfernen | Wählen Sie das Papierkorb-Symbol neben dem Schritt aus, den Sie entfernen möchten.<br><br>Beachten Sie, dass der Schritt **Confirmation** kein Papierkorb-Symbol hat und weder entfernt noch neu angeordnet werden kann. Er wird immer zuletzt ausgeführt, nachdem Nutzer:innen die vorherigen Schritte abgeschlossen haben. |
| Schritte neu anordnen | Verwenden Sie den Ziehgriff neben einem Schritt, um dessen Reihenfolge zu ändern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritte verwalten" }

## Bestätigungsschritt anpassen {#customize-the-confirmation-step}

Jedes mehrstufige Formular enthält einen **Bestätigungs**-Schritt, der unter **Nach dem Absenden** im Abschnitt **Schritte** aufgeführt ist. Dieser Schritt ist gesperrt, sodass er nicht gelöscht werden kann – Nutzer:innen sehen also immer eine Bestätigungserfahrung, nachdem sie Ihr Formular abgesendet haben.

Obwohl der **Bestätigungs**-Schritt nicht entfernt werden kann, können Sie ihn wie jeden anderen Schritt anpassen: Wählen Sie ihn im Abschnitt **Schritte** aus und fügen Sie dann Blöcke hinzu und gestalten Sie diese, um Ihre Bestätigungsnachricht zu erstellen.

## Den Formularblock gestalten {#style-the-form-block}

Wählen Sie die Zeile **Form** aus und verwenden Sie den Abschnitt **Styles** im Panel **Multi-step form**, um den Formularcontainer anzupassen:

| Steuerelement | Beschreibung |
|---|---|
| Background image | Fügen Sie ein Bild hinter dem Formular hinzu. Sie können auch die Bildgröße, Position und Wiederholungseinstellungen anpassen. |
| Background color | Legen Sie die Hintergrundfarbe des Formularcontainers fest. |
| Border style | Wählen Sie einen durchgezogenen, gestrichelten oder gepunkteten Rahmen für den Formularcontainer. |
| Border color | Legen Sie die Rahmenfarbe für den Formularcontainer fest. |
| Border radius | Runden Sie die Ecken des Formularcontainers ab. |
| Padding | Passen Sie den Abstand zwischen dem Rand des Formularcontainers und seinem Inhalt an. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Stiloptionen für mehrstufige Formulare" }

Diese Stile gelten für den Formularcontainer über alle Schritte hinweg, einschließlich des Schritts **Confirmation**.

## Daten aus teilweise ausgefüllten Formularen erfassen {#track-data-from-partially-completed-forms}

Wenn Nutzer:innen Ihr Formular verlassen, bevor sie den Schritt **Bestätigung** erreichen, speichert Braze trotzdem die Daten aus allen Schritten, die sie abgeschlossen haben, in ihrem Nutzerprofil. Das Ereignis **Landing-Page-Formular eingereicht** wird erst protokolliert, wenn Nutzer:innen jeden Schritt abschließen und den Schritt **Bestätigung** erreichen.

{% alert note %}
[Retargeting und Trigger-Zustellung]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users) basieren auf dem Ereignis **Landing-Page-Formular eingereicht**. Nutzer:innen, die einige, aber nicht alle Schritte einreichen, werden in ihrem Profil gespeichert, sind aber nicht in diesem Ereignis enthalten – auch wenn ihre teilweisen Daten erfasst wurden.
{% endalert %}

Dies unterscheidet sich von [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys), bei denen Nutzer:innen, die den letzten Schritt nicht erreichen, als teilweise Einreichung erfasst werden.

## Einschränkungen und Hinweise {#limitations-and-considerations}

- Eine Landing-Page unterstützt eine einzelne **Formular**-Zeile, sodass alle Ihre Schritte und Ihr Bestätigungsschritt in dieser einen Zeile enthalten sind.
- Sie können bis zu 10 Datenerfassungsschritte hinzufügen. Der **Bestätigungs**-Schritt zählt nicht zu diesem Limit.
- Jeder Schritt enthält einen Standard-Button, dessen Klick-Aktion so eingestellt ist, dass er zum nächsten Schritt führt. Diese Aktion validiert und speichert die Eingaben des aktuellen Schritts. Beim letzten Datenerfassungsschritt wird zusätzlich das Ereignis **Submitted a Landing Page form** protokolliert und zum **Bestätigungs**-Schritt weitergeleitet. Wenn ein Schritt nicht verbunden ist, fügen Sie ein Klick-Verhalten hinzu, damit der Button zum nächsten Schritt führt. Weitere Informationen finden Sie unter [Button]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) in Editor-Blöcke.
- Sie müssen keine zweite Landing-Page erstellen oder verlinken, die als Bestätigungserlebnis dient, da der **Bestätigungs**-Schritt in die **Formular**-Zeile integriert ist.
- Wenn Sie die **Formular**-Zeile unter **Layout** nicht sehen, wenden Sie sich an Ihren Braze Account Manager.