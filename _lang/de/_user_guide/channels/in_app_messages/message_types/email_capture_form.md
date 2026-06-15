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

> E-Mail-Erfassungsnachrichten ermöglichen es Ihnen, Nutzer:innen Ihrer Website aufzufordern, ihre E-Mail-Adresse einzugeben. Braze fügt die Adresse ihrem Nutzerprofil hinzu, damit sie in all Ihren Messaging-Kampagnen verwendet werden kann.

Dieser Nachrichtentyp ist im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) verfügbar.

## So funktioniert es {#how-it-works}

Wenn Endnutzer:innen ihre E-Mail-Adresse in dieses Formular eingeben, fügt Braze die E-Mail-Adresse ihrem Nutzerprofil hinzu.

- Bei [anonymen Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#anonymous-user-profiles), die noch kein Konto haben, wird die E-Mail-Adresse im anonymen Nutzerprofil gespeichert, das mit dem Gerät der Nutzer:in verknüpft ist.
- Wenn bereits eine E-Mail-Adresse im Nutzerprofil vorhanden ist, wird die bestehende E-Mail-Adresse durch die neu eingegebene überschrieben.
- Wenn bekannte Nutzer:innen eine E-Mail-Adresse haben, die als [Hard Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary/#hard-bounce) markiert ist, prüft Braze, ob die neu eingegebene E-Mail-Adresse von der im Braze-Profil gespeicherten abweicht. Wenn die angegebene E-Mail-Adresse anders ist, aktualisiert Braze die E-Mail-Adresse und entfernt den Hard-Bounce-Status.
- Wenn Nutzer:innen eine ungültige E-Mail-Adresse eingeben, wird die Fehlermeldung angezeigt: „Please enter a valid email.“
    - Ungültige E-Mail-Adressen:
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Gültige E-Mail-Adressen:
        - `example@gmail.com`
        - `example@gnail.com` (mit Tippfehler)
    - Weitere Informationen zur E-Mail-Validierung in Braze finden Sie unter [Technische Richtlinien und Hinweise für E-Mails]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/).

{% details Mehr zu identifizierten und anonymen Nutzer:innen %}

Das E-Mail-Erfassungsformular setzt die E-Mail-Adresse im aktuell aktiven Nutzerprofil in Braze. Das Verhalten unterscheidet sich je nachdem, ob die Nutzer:in identifiziert (eingeloggt, `changeUser` aufgerufen) ist oder nicht.

Wenn eine anonyme Nutzer:in ihre E-Mail-Adresse in das Formular eingibt und absendet, fügt Braze die E-Mail-Adresse ihrem Profil hinzu. Wenn `changeUser` später in der Web-Journey aufgerufen wird und eine neue `external_id` zugewiesen wird (z. B. wenn sich eine neue Nutzer:in beim Dienst registriert), werden alle anonymen Nutzerprofildaten einschließlich der E-Mail-Adresse zusammengeführt.

Wenn `changeUser` mit einer bestehenden `external_id` aufgerufen wird, wird das anonyme Nutzerprofil verwaist und [bestimmte Nutzerprofil-Datenfelder]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior), die noch nicht im identifizierten Profil vorhanden sind, werden zusammengeführt. Felder, die bereits vorhanden sind, gehen jedoch verloren – einschließlich der E-Mail-Adresse.

Weitere Informationen finden Sie unter [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/).

{% enddetails %}

## 1. Schritt: Eine In-App-Nachrichten-Campaign erstellen {#step-1-create-an-in-app-message-campaign}

Um zu dieser Option zu navigieren, müssen Sie eine In-App-Nachrichten-Campaign erstellen. Stellen Sie dort je nach Anwendungsfall **Send To** auf **Web Browsers**, **Mobile Apps** oder **Both Mobile Apps & Web Browsers** ein und wählen Sie dann **Email Capture Form** als Ihren **Message Type** aus.

{% alert note %}
**Targeting von Web-Nutzer:innen?** <br>Um HTML-In-App-Nachrichten über das Web SDK zu aktivieren, müssen Sie die Initialisierungsoption `allowUserSuppliedJavascript` an Braze übergeben, z. B. `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies dient Sicherheitszwecken, da HTML-In-App-Nachrichten JavaScript ausführen können, weshalb eine Website-Verwaltung diese aktivieren muss.
{% endalert %}

## 2. Schritt: Das Formular anpassen {#customizable-features}

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

## 3. Schritt: Ihre Entry-Zielgruppe festlegen {#step-3-set-your-entry-audience}

Wenn Sie eine In-App-Nachricht zur Erfassung von E-Mail-Adressen verwenden, möchten Sie die Zielgruppe möglicherweise auf Nutzer:innen beschränken, die diese Information noch nicht angegeben haben.

- **Um Nutzer:innen ohne E-Mail-Adresse anzusprechen:** Verwenden Sie den Filter `Email Available` ist `false`. Dadurch wird das Formular nur Nutzer:innen angezeigt, die keine E-Mail-Adresse hinterlegt haben, und Sie vermeiden überflüssige Aufforderungen für bekannte Nutzer:innen.
- **Um anonyme Nutzer:innen ohne externe IDs anzusprechen:** Verwenden Sie den Filter `External User ID` `is blank`. Dies ist nützlich, wenn Sie Nutzer:innen identifizieren möchten, die sich noch nicht authentifiziert oder registriert haben.

Sie können die beiden Filter bei Bedarf auch mit `AND`-Logik kombinieren. Dadurch wird das Formular nur Nutzer:innen angezeigt, denen sowohl eine E-Mail-Adresse als auch eine externe Nutzer-ID fehlt – ideal für die Erfassung neuer Leads oder die Aufforderung zur Kontoerstellung.

## 4. Schritt: Nutzer:innen ansprechen, die das Formular ausgefüllt haben (optional) {#step-4-target-users-who-filled-out-the-form-optional}

Nachdem Sie das E-Mail-Erfassungsformular gestartet und E-Mail-Adressen Ihrer Nutzer:innen gesammelt haben, können Sie Nutzer:innen ansprechen, die das Formular ausgefüllt haben.

1. Wählen Sie in einem beliebigen Segment-Filter in Braze den Filter `Clicked/Opened Campaign` aus.
2. Wählen Sie im Dropdown `clicked in-app message button 1` aus.
3. Wählen Sie Ihre E-Mail-Erfassungsformular-Campaign aus.