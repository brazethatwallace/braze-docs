---
nav_title: E-Mail-Erfassungsformular
article_title: E-Mail-Erfassungsformular
page_order: 5
page_type: reference
description: "Dieser Artikel bietet einen Überblick über den In-App-Nachrichtentyp zur E-Mail-Erfassung."
channel:
  - in-app messages
---

# E-Mail-Erfassungsformular {#email-capture-form}

> E-Mail-Erfassungsnachrichten ermöglichen es Ihnen, Nutzer:innen Ihrer Website aufzufordern, ihre E-Mail-Adresse einzugeben. Braze fügt die Adresse ihrem Kundenprofil hinzu, damit sie in all Ihren Messaging-Kampagnen verwendet werden kann.

Dieser Nachrichtentyp ist im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) verfügbar.

Wenn Sie E-Mail-Adressen über ein benutzerdefiniertes Formular anstelle dieses In-App-Nachrichtentyps erfassen und dann die Zugehörigkeit zu Abo-Gruppen über die REST API festlegen, prüfen Sie, ob bereits ein Profil existiert, bevor Sie eine:n Nutzer:in erstellen. Siehe [Best Practices für die Erfassung]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices#step-1-check-if-the-user-exists).

## So funktioniert es {#how-it-works}

Wenn Endnutzer:innen ihre E-Mail-Adresse in dieses Formular eingeben, fügt Braze die E-Mail-Adresse zu ihrem Kundenprofil hinzu.

- Bei [anonymen Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles), die noch kein Konto haben, wird die E-Mail-Adresse im anonymen Kundenprofil gespeichert, das mit dem Gerät der Nutzer:innen verknüpft ist.
- Wenn bereits eine E-Mail-Adresse im Kundenprofil vorhanden ist, überschreibt die neu eingegebene E-Mail-Adresse die bestehende.
- Wenn bekannte Nutzer:innen eine E-Mail-Adresse haben, die als [Hard Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#hard-bounce) gekennzeichnet ist, prüft Braze, ob die neu eingegebene E-Mail-Adresse sich von der Adresse in ihrem Braze-Profil unterscheidet. Wenn die angegebene E-Mail-Adresse abweicht, aktualisiert Braze die E-Mail-Adresse und entfernt den Hard-Bounce-Status.
- Wenn Nutzer:innen eine ungültige E-Mail-Adresse eingeben, wird die Fehlermeldung angezeigt: „Please enter a valid email.“
    - Ungültige E-Mail-Adressen:
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Gültige E-Mail-Adressen:
        - `example@gmail.com`
        - `example@gnail.com` (mit einem Tippfehler)
    - Weitere Informationen zur E-Mail-Validierung in Braze finden Sie unter [Technische Richtlinien und Hinweise für E-Mails]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation).

{% details Mehr zu identifizierten versus anonymen Nutzer:innen %}

Das E-Mail-Erfassungsformular setzt die E-Mail-Adresse im derzeit aktiven Kundenprofil in Braze. Das Verhalten unterscheidet sich je nachdem, ob die Nutzer:innen identifiziert (eingeloggt, `changeUser` aufgerufen) sind oder nicht.

Wenn anonyme Nutzer:innen ihre E-Mail-Adresse in das Formular eingeben und absenden, fügt Braze die E-Mail-Adresse zu ihrem Profil hinzu. Wenn `changeUser` später im Verlauf ihrer Web-Journey aufgerufen wird und eine neue `external_id` zugewiesen wird (z. B. wenn sich neue Nutzer:innen beim Dienst registrieren), werden alle anonymen Nutzerprofildaten einschließlich der E-Mail-Adresse zusammengeführt.

Wenn `changeUser` mit einer bestehenden `external_id` aufgerufen wird, wird das anonyme Kundenprofil verwaist und [bestimmte Kundenprofil-Datenfelder]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior), die noch nicht im identifizierten Profil vorhanden sind, werden zusammengeführt. Felder, die bereits vorhanden sind, gehen jedoch verloren – einschließlich der E-Mail-Adresse.

Weitere Informationen finden Sie unter [Kundenprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).

{% enddetails %}

## Schritt 1: Eine In-App-Nachrichten-Campaign erstellen {#step-1-create-an-in-app-message-campaign}

Um zu dieser Option zu gelangen, müssen Sie eine In-App-Messaging-Campaign erstellen. Legen Sie dort je nach Anwendungsfall unter **Send To** entweder **Web Browsers**, **Mobile Apps** oder **Both Mobile Apps & Web Browsers** fest und wählen Sie dann **Email Capture Form** als **Message Type** aus.

{% alert note %}
**Targeting für Internet-Nutzer:innen?** <br>Um HTML-In-App-Nachrichten über das Web-SDK zu aktivieren, müssen Sie die Initialisierungsoption `allowUserSuppliedJavascript` an Braze übergeben, zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies dient der Sicherheit, da HTML-In-App-Nachrichten JavaScript ausführen können und daher von einem Website-Administrator aktiviert werden müssen.
{% endalert %}

## Schritt 2: Das Formular anpassen {#customizable-features}

Passen Sie als Nächstes Ihr Formular nach Bedarf an. Sie können die folgenden Features Ihres E-Mail-Erfassungsformulars anpassen:

- Überschrift, Textkörper und Text des Senden-Buttons
- Ein optionales Bild
- Ein optionaler Link zu den „Nutzungsbedingungen“
- Verschiedene Farben für Überschrift und Textkörper, Buttons und Hintergrund
- Schlüssel-Wert-Paare
- Stil für Überschrift und Textkörper, Buttons, Button-Rahmenfarbe, Hintergrund und Overlay
- Senden-Button
    - Hinweis: Der Senden-Button wird erst angezeigt, nachdem Nutzer:innen eine gültige E-Mail-Adresse eingegeben haben. So stellen Sie sicher, dass vollständige E-Mail-Adressen erfasst werden.

![Composer für das E-Mail-Erfassungsformular.]({% image_buster /assets/img/email_capture.png %})

Wenn Sie weitere Anpassungen vornehmen möchten, wählen Sie **Custom Code** als Ihren **Message Type**. Verwenden Sie dieses [E-Mail-Erfassungs-Modal-Template](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) aus dem [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) GitHub-Repository als Ausgangscode.

## Schritt 3: Eintritts-Zielgruppe festlegen {#step-3-set-your-entry-audience}

Wenn Sie eine In-App-Nachricht verwenden, um E-Mail-Adressen von Nutzer:innen zu erfassen, möchten Sie die Zielgruppe möglicherweise auf Nutzer:innen beschränken, die diese Informationen noch nicht angegeben haben.

- **Um Nutzer:innen ohne E-Mail-Adresse anzusprechen:** Verwenden Sie den Filter `Email Available` ist `false`. Dadurch wird das Formular nur Nutzer:innen angezeigt, die keine E-Mail-Adresse hinterlegt haben, sodass Sie überflüssige Aufforderungen für bereits bekannte Nutzer:innen vermeiden.
- **Um anonyme Nutzer:innen ohne externe IDs anzusprechen:** Verwenden Sie den Filter `External User ID` `is blank`. Dies ist nützlich, wenn Sie Nutzer:innen identifizieren möchten, die sich noch nicht authentifiziert oder registriert haben.

Sie können die beiden Filter bei Bedarf auch mit `AND`-Logik kombinieren. Dadurch wird das Formular nur Nutzer:innen angezeigt, denen sowohl eine E-Mail-Adresse als auch eine externe ID fehlt – ideal, um neue Leads zu erfassen oder zur Kontoerstellung aufzufordern.

## Schritt 4: Nutzer:innen ansprechen, die das Formular ausgefüllt haben (optional) {#step-4-target-users-who-filled-out-the-form-optional}

Nachdem Sie das E-Mail-Erfassungsformular gestartet und E-Mail-Adressen Ihrer Nutzer:innen gesammelt haben, können Sie Nutzer:innen ansprechen, die das Formular ausgefüllt haben.

1. Wählen Sie in einem beliebigen Segment-Filter in Braze den Filter `Clicked/Opened Campaign` aus.
2. Wählen Sie im Dropdown-Menü `clicked in-app message button 1` aus.
3. Wählen Sie Ihre Campaign für das E-Mail-Erfassungsformular aus.