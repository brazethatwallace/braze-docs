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

Um auf den Landing-Page-Builder zugreifen zu können, benötigen Sie [bestimmte Berechtigungen]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Wenn Sie keinen Zugriff haben, wenden Sie sich an Ihren Braze-Administrator.

Sie sollten außerdem mit [Landing-Page-Formularblöcken]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) vertraut sein.

## So funktionieren mehrstufige Formulare {#how-multi-step-forms-work}

Um ein mehrstufiges Formular zu erstellen, fügen Sie eine **Form**-Zeile aus dem Abschnitt **Layout** im **Build**-Panel hinzu. Die **Form**-Zeile enthält integrierte Aktions-Buttons und Unterstützung für mehrere Schritte, sodass Sie die Zeilenstruktur nicht selbst zusammenstellen müssen.

Sie können pro Landing-Page nur eine **Form**-Zeile hinzufügen. Wenn Sie sie auf Ihre Seite ziehen, beginnt sie mit einem einzelnen Schritt und einem gesperrten Bestätigungsschritt, der nach dem Absenden ausgeführt wird.

{% alert note %}
Da die **Form**-Zeile ihre eigene mehrstufige Navigation verwaltet, befinden sich alle Ihre Schritte innerhalb dieser einzelnen Zeile auf einer Seite. Dies unterscheidet sich vom Standardansatz, bei dem ein einstufiges Formular erstellt und dessen **Submit**-Button mit einer separaten Bestätigungs-Landing-Page verknüpft wird. Weitere Informationen finden Sie unter [Schritt 4: Bestätigungsseite erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional).
{% endalert %}

![Ein mehrstufiges Landing-Page-Formular im Landing-Page-Composer.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## Ein mehrstufiges Formular hinzufügen {#add-a-multi-step-form}

1. Gehen Sie im Landing-Page-Editor zum **Build**-Panel und wählen Sie **Layout** aus.
2. Ziehen Sie die **Form**-Zeile auf Ihre Seite.
3. Verwenden Sie bei ausgewählter **Form**-Zeile den Abschnitt **Steps** im Eigenschaftenpanel auf der rechten Seite, um Ihr Formular aufzubauen:
   - Fügen Sie [Formularblöcke]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page) (wie **Email Capture**, **Phone Capture**, **Input Field**, **Dropdown**, **Checkbox** oder **Checkbox Group**) zu **Step 1** hinzu.
   - Wählen Sie **Add step**, um weitere Schritte zu erstellen, und fügen Sie jedem Schritt Formularblöcke hinzu.

Ein dreistufiges Formular könnte beispielsweise in **Step 1** nach einem Namen fragen, in **Step 2** nach einer Telefonnummer und dann im **Confirmation**-Schritt den Nutzer:innen für das Absenden danken.

## Zwischen Schritten während der Bearbeitung navigieren {#navigate-between-steps-while-editing}

Wechseln Sie im Editor auf zwei Arten zwischen Schritten:

| Methode | Vorgehensweise |
|---------|----------------|
| Schritt-Navigator | Verwenden Sie im Canvas das Steuerelement **Step X of Y**, um zum vorherigen oder nächsten Schritt zu wechseln. |
| Steps-Panel | Wählen Sie die **Form**-Zeile aus und verwenden Sie dann den Abschnitt **Steps** im Eigenschaftenpanel auf der rechten Seite, um direkt zu einem Schritt zu springen, einschließlich des **Confirmation**-Schritts. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zwischen Schritten während der Bearbeitung navigieren" }

## Schritte verwalten {#manage-steps}

Verwenden Sie den Abschnitt **Steps** im Eigenschaftenpanel der **Form**-Zeile, um Schritte hinzuzufügen, zu entfernen und neu anzuordnen:

| Aktion | Vorgehensweise |
|--------|----------------|
| Schritt hinzufügen | Wählen Sie **Add step**. Neue Schritte werden nach Ihren bestehenden Schritten und vor dem **Confirmation**-Schritt hinzugefügt. |
| Schritt entfernen | Wählen Sie das Papierkorb-Symbol neben dem Schritt, den Sie entfernen möchten.<br><br>Beachten Sie, dass der **Confirmation**-Schritt kein Papierkorb-Symbol hat und weder entfernt noch neu angeordnet werden kann. Er wird immer zuletzt ausgeführt, nachdem Nutzer:innen die vorhergehenden Schritte abgeschlossen haben. |
| Schritte neu anordnen | Verwenden Sie den Ziehgriff neben einem Schritt, um dessen Reihenfolge zu ändern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritte verwalten" }

## Den Bestätigungsschritt anpassen {#customize-the-confirmation-step}

Jedes mehrstufige Formular enthält einen **Confirmation**-Schritt, der unter **After submission** im Abschnitt **Steps** aufgeführt ist. Dieser Schritt ist gesperrt, sodass er nicht gelöscht werden kann, was bedeutet, dass Nutzer:innen nach dem Absenden Ihres Formulars immer eine Bestätigung sehen.

Obwohl der **Confirmation**-Schritt nicht entfernt werden kann, können Sie ihn wie jeden anderen Schritt anpassen: Wählen Sie ihn im Abschnitt **Steps** aus und fügen Sie dann Blöcke hinzu und gestalten Sie diese, um Ihre Bestätigungsnachricht zu erstellen.

## Daten aus teilweise ausgefüllten Formularen erfassen {#track-data-from-partially-completed-forms}

Wenn Nutzer:innen Ihr Formular verlassen, bevor sie den **Confirmation**-Schritt erreichen, speichert Braze dennoch die Daten aus allen abgeschlossenen Schritten in ihrem Nutzerprofil. Das Ereignis **Submitted a Landing Page form** wird erst protokolliert, wenn Nutzer:innen jeden Schritt abgeschlossen haben und den **Confirmation**-Schritt erreichen.

{% alert note %}
[Retargeting und Trigger-Zustellung]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users) basieren auf dem Ereignis **Submitted a Landing Page form**. Nutzer:innen, die einige, aber nicht alle Schritte absenden, werden in ihrem Profil gespeichert, sind aber nicht in diesem Ereignis enthalten – auch wenn ihre teilweisen Daten erfasst wurden.
{% endalert %}

Dies unterscheidet sich von [Landing-Page-Umfragen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys), bei denen Nutzer:innen, die den letzten Schritt nicht erreichen, als teilweise Einreichung erfasst werden.

## Einschränkungen und Hinweise {#limitations-and-considerations}

- Eine Landing-Page unterstützt eine einzelne **Form**-Zeile, sodass sich alle Ihre Schritte und Ihr Bestätigungsschritt in dieser einen Zeile befinden.
- Sie können bis zu 10 Datenerfassungsschritte hinzufügen. Der **Confirmation**-Schritt zählt nicht zu diesem Limit.
- Jeder Schritt enthält einen Standard-Button, dessen Klick-Aktion auf den nächsten Schritt eingestellt ist. Diese Aktion validiert und speichert die Eingaben des aktuellen Schritts; beim letzten Datenerfassungsschritt protokolliert sie außerdem das Ereignis **Submitted a Landing Page form** und wechselt zur **Confirmation**. Wenn ein Schritt nicht verbunden ist, fügen Sie ein Klick-Verhalten hinzu, damit der Button zum nächsten Schritt führt. Weitere Informationen finden Sie unter [Button]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) in Editor-Blöcke.
- Sie müssen keine zweite Landing-Page erstellen oder verlinken, die als Bestätigungserlebnis dient, da der **Confirmation**-Schritt in die **Form**-Zeile integriert ist.
- Wenn Sie die **Form**-Zeile unter **Layout** nicht sehen, wenden Sie sich an Ihren Braze Account Manager.