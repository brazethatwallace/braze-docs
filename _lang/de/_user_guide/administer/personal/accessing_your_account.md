---
nav_title: Auf Ihr Konto zugreifen
article_title: Auf Ihr Konto zugreifen
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Ihr Braze-Konto erhalten, wie Sie sich nach erteiltem Zugang anmelden und wie Sie Probleme mit dem Dashboard-Zugang und der Dashboard-Performance beheben können."
---

# Auf Ihr Konto zugreifen {#access-your-account}

> Dieser Artikel beschreibt, wie Sie Ihr Braze-Konto erhalten, wie Sie sich nach erteiltem Zugang anmelden und wie Sie Probleme mit dem Dashboard-Zugang und der Dashboard-Performance beheben können.

Wenn Sie die erste Braze-Nutzer:in Ihres Unternehmens sind und sich zum ersten Mal anmelden, erhalten Sie eine Willkommens-E-Mail von `@alerts.braze.com`, in der Sie aufgefordert werden, Ihre E-Mail-Adresse zu bestätigen und sich am ersten Tag Ihres Vertrags anzumelden.

Nachdem Sie Ihr Konto bestätigt haben, können Sie weitere Nutzer:innen über die Seite [Unternehmensnutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) in Ihrem Dashboard hinzufügen. Alle Nutzer:innen erhalten eine E-Mail mit der Aufforderung, ihr Konto zu bestätigen, nachdem sie hinzugefügt wurden.

Wenn Sie nicht die erste Nutzer:in im Braze-Konto Ihres Unternehmens sind, wenden Sie sich an die Braze-Kontoadministrator:in Ihres Unternehmens und bitten Sie darum, Ihr Konto zu erstellen. Sie erhalten dann eine Willkommens-E-Mail von `@alerts.braze.com`, in der Sie aufgefordert werden, Ihre E-Mail-Adresse zu bestätigen und sich anzumelden.

## Anmelden {#logging-in}

Egal, ob Sie sich zum ersten oder zum hundertsten Mal anmelden – so greifen Sie auf Ihr Dashboard zu. Wenn Sie die erste Nutzer:in Ihres Unternehmens sind, folgen Sie der Anleitung im vorherigen Abschnitt. Andernfalls können Sie sich anmelden, nachdem der Braze-Admin Ihres Unternehmens Ihr Konto erstellt hat.

Sie können sich entweder über die [Braze.com](https://www.braze.com)-Startseite anmelden oder die Dashboard-URL verwenden, die Ihrer spezifischen [Braze-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) entspricht. Für Ihren Komfort bietet Braze mehrere Single-Sign-on-Optionen (Single Sign-on) an, darunter:

* [SAML Single Sign-on]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [SAML-Just-in-Time-Bereitstellung]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [Microsoft Entra Single Sign-on]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

Nachdem Sie sich über Single Sign-on bei Braze angemeldet haben, können Sie sich nicht mehr mit Ihrem Passwort am Dashboard anmelden. Beide E-Mail-Adressen leiten E-Mails an denselben Posteingang weiter, aber Braze erkennt sie bei der Anmeldung als separate Konten. Durch das Löschen von Cookies werden Sie abgemeldet, sodass nicht gespeicherte Arbeit verloren geht.

## Unterstützte Browser {#supported-browsers}

Das Braze-Dashboard unterstützt die folgenden Browser:
- Chrome (Version 87 oder neuer)
- Firefox (Version 85 oder neuer)
- Safari (Version 15.4 oder neuer)
- Edge (Version 87 oder neuer)

Wenn Ihr Braze-Dashboard einen unerwarteten Fehler anzeigt und das Konsolen-Tool Ihres Browsers den Fehler `ReferenceError: structuredClone is not defined` ausgibt, ist Ihr Browser veraltet. Falls dieser Fehler weiterhin auftritt, deinstallieren Sie Ihren Browser und installieren Sie ihn neu.

## Zugriff auf mehrere Braze-Dashboards {#accessing-multiple-braze-dashboards}

Braze erlaubt es nicht, dieselbe E-Mail-Adresse für mehrere Dashboard-Nutzer:innen im selben Cluster zu Registrierung or registrieren (zum Beispiel, wenn Sie zwei Dashboards auf US-01 haben). Sie können dieselbe E-Mail-Adresse verwenden, um Konten auf verschiedenen Clustern zu erstellen (zum Beispiel, wenn Sie ein Dashboard auf US-01 und eines auf US-05 haben). Wenn Sie auf mehrere Braze-Dashboards im selben Cluster zugreifen müssen, können Sie Folgendes tun:

### E-Mail-Aliasse verwenden {#use-email-aliases}

Wenn Ihr E-Mail-Anbieter Gmail ist, können Sie Aliasse erstellen, indem Sie ein `+`-Zeichen gefolgt von beliebigem Text an Ihre E-Mail-Adresse anhängen. Zum Beispiel:
- **Ursprüngliche E-Mail:** `rocky@gmail.com`
- **Alias-E-Mail:** `rocky+1@gmail.com`

Beide E-Mail-Adressen leiten E-Mails an denselben Posteingang weiter, aber Braze erkennt sie bei der Anmeldung als separate Konten.

### Separate Aliasse bei anderen Anbietern erstellen {#create-separate-aliases-with-other-providers}

Wenn Ihr E-Mail-Anbieter kein `+`-Aliasing unterstützt, können Sie dennoch separate Aliasse erstellen, zum Beispiel indem Sie `rocky@braze.com` so einrichten, dass E-Mails an `rocky.lotito@braze.com` weitergeleitet werden. So können mehrere Adressen in denselben Posteingang münden und werden von Braze trotzdem als unterschiedliche E-Mail-Adressen erkannt.

### Multi-Company-Entwickler:innen verwenden {#use-multi-company-developers}

Das Feature „Multi-Company-Entwickler:innen“ ermöglicht die gemeinsame Nutzung eines einzelnen Nutzerkontos über mehrere Unternehmen hinweg. Dashboard-Nutzer:innen können über ihr Nutzerprofilmenü zwischen verschiedenen Unternehmens-Dashboards wechseln.

Wenn Sie Single Sign-on verwenden und Multi-Company-Entwickler:innen einrichten möchten, müssen Sie eine benutzerdefinierte SAML-Entity-ID aktivieren, indem Sie eine benutzerdefinierte SAML-Single Sign-on-Integration einrichten. Folgen Sie den Schritten unter [Service Provider (SP) initiated login]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), wenden Sie jedoch diese Änderungen an:
- Ändern Sie die **Entity ID** für jede Dashboard-Integration auf `braze_dashboard_<companyID>`.
- Kontaktieren Sie Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in oder Account Manager:in, um den `saml_sso_custom_entity_id`-Feature-Flipper für jedes Dashboard zu aktivieren.

#### Zwei-Faktor-Authentifizierung (2FA) {#two-factor-authentication-2fa}

Wie 2FA für Multi-Company-Entwickler:innen funktioniert, hängt von Ihrer 2FA-Methode ab:

- **E-Mail und Kurzmitteilungsdienst or SMS:** Ihre 2FA-Einstellungen werden auf alle verknüpften Entwicklerkonten kopiert. Nachdem Sie E-Mail- oder Kurzmitteilungsdienst or SMS-basierte 2FA für ein Konto eingerichtet haben, gilt dieselbe Methode für alle Ihre Unternehmens-Dashboards.
- **Zeitbasiertes Einmalpasswort (TOTP):** TOTP-Einstellungen werden nicht über Konten hinweg synchronisiert. Wenn Sie eine Authenticator-App verwenden, müssen Sie für jedes Dashboard, bei dem Sie sich direkt anmelden, einen separaten Code einrichten.

Wenn Sie innerhalb des Dashboards zwischen Konten wechseln, müssen Sie die 2FA nur einmal durchführen – beim ersten Anmelden bei einem verknüpften Konto während dieser Sitzung.

### Hinweise zu Single Sign-on (Single Sign-on) {#considerations-for-single-sign-on-sso}

Wenn Sie Single Sign-on (Single Sign-on) verwenden, beachten Sie, dass mehrere unterschiedliche E-Mail-Adressen zu Komplikationen führen können. Stellen Sie sicher, dass Ihre Single Sign-on-Einstellungen korrekt konfiguriert sind, um Zugriffsprobleme zu vermeiden.

## Fehlerbehebung {#troubleshooting}

### Passwort zurücksetzen {#resetting-your-password}

Um Ihr Passwort zurückzusetzen, wählen Sie den Link **Forgot your password?** auf der Anmeldeseite des Dashboards. Sie werden aufgefordert, Ihre E-Mail-Adresse einzugeben, um einen Link zum Zurücksetzen Ihres Passworts zu erhalten.


#### E-Mail zum Zurücksetzen des Passworts nicht erhalten {#password-reset-email-not-received}

Wenn Sie eine Passwortzurücksetzung angefordert haben, aber die E-Mail nicht erhalten haben, probieren Sie die folgenden Schritte zur Fehlerbehebung:

{% alert note %}
Wenn Ihr Unternehmen [Single Sign-on (Single Sign-on)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) erzwingt, bietet die Anmeldeseite möglicherweise kein **Forgot your password?** an und sendet keine E-Mails zum Zurücksetzen des Passworts, da die Passwort-Anmeldung deaktiviert ist. Melden Sie sich stattdessen über den Identitätsanbieter Ihres Unternehmens an oder wenden Sie sich an Ihren Braze-Administrator.
{% endalert %}

1. **Überprüfen Sie Ihre E-Mail-Adresse:** Lassen Sie einen Administrator prüfen, ob die E-Mail-Adresse in Ihrem Konto unter **Settings** > **Company Users** übereinstimmt. Der Link zum Zurücksetzen wird an die im System registrierte E-Mail-Adresse gesendet.
2. **Spam- und Junk-Ordner überprüfen:** Suchen Sie in Ihrem Spam- oder Junk-Ordner nach E-Mails von `@alerts.braze.com`.
3. **IT-E-Mail-Filter überprüfen:** Bestätigen Sie mit Ihrem IT-Team, dass E-Mails von `@alerts.braze.com` nicht blockiert oder gefiltert werden.
4. **Korrekte Dashboard-Instanz bestätigen:** Stellen Sie sicher, dass Sie die Zurücksetzung von der richtigen [Braze-Dashboard-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) anfordern. Wenden Sie sich an Ihren Account-Administrator oder Braze Account Manager:in, wenn Sie unsicher sind.
5. **Anderen Browser verwenden:** Einige Browsererweiterungen oder -einstellungen können den Vorgang zum Zurücksetzen des Passworts beeinträchtigen. Versuchen Sie es mit einem anderen Browser oder einem Inkognito-Fenster.

Links zum Zurücksetzen des Passworts laufen zwei Stunden nach dem E-Mail-Versand ab. Wenn Ihr Link abgelaufen ist, fordern Sie auf der Anmeldeseite eine neue Zurücksetzung an.

Wenn keiner dieser Schritte funktioniert, kann ein Administrator Ihr Nutzerkonto löschen und neu erstellen, um das Problem zu beheben. Weitere Informationen finden Sie unter [Unternehmensnutzer:innen verwalten]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).

{% alert note %}
Das Löschen und Neuerstellen eines Nutzerkontos setzt deren Berechtigungen zurück und kann die Asset-Zuordnung für Campaigns, Canvase und andere Inhalte beeinflussen, die zuvor diesem/dieser Nutzer:in gehörten.
{% endalert %}

### Browser-Cache und Cookies löschen {#clearing-your-browser-cache-and-cookies}

Wenn Sie Probleme mit der Dashboard-Performance haben, z. B. wenn Ihr Dashboard oder Ihre Segment-Performance-Liste nicht geladen wird, versuchen Sie, den Browser-Cache und die Cookies zu löschen, indem Sie den Schritten für Ihren jeweiligen Browser folgen.

{% alert important %}
Das Löschen von Cookies meldet Sie ab, sodass nicht gespeicherte Arbeit verloren geht.
{% endalert %}

- [Cache und Cookies in Chrome löschen](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Cookies in Safari auf dem Mac löschen](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Cookies und Websitedaten in Firefox löschen](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Alle Cookies in Microsoft Edge löschen](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Wenn das Löschen von Browser-Cache und Cookies Ihr Problem nicht löst, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact).

### Fehler „Aw, Snap!“ in Google Chrome {#aw-snap-error-in-google-chrome}

Wenn Google Chrome den Fehler „Aw, Snap!“ anzeigt, hat Chrome Schwierigkeiten, die Braze-Dashboard-Seite zu laden. Schritte zur Fehlerbehebung finden Sie unter [Hilfe bei häufigen Fehlermeldungen in Chrome](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en).

### „Please Refresh Page“ oder „Unexpected Error“ bei der Navigation im Dashboard {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

Dieser Fehler kann auftreten, wenn ein/e Unternehmensnutzer:in keinem Workspace zugeordnet ist. Zur Fehlerbehebung:

1. Gehen Sie zur Seite [Unternehmensnutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).
2. Prüfen Sie, ob der/die Nutzer:in einem Workspace hinzugefügt wurde.
3. Wenn er/sie keinem Workspace angehört, fügen Sie ihn/sie hinzu und weisen Sie die entsprechenden Berechtigungen zu.
4. Bitten Sie den/die Nutzer:in, das Dashboard zu Update or aktualisieren or aktualisieren.
5. Wenn das Problem weiterhin besteht, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact).

### Zugriff auf den Drag-and-Drop-Editor {#accessing-the-drag-and-drop-editor}

Für die meisten Unternehmensnutzer:innen sollte der Drag-and-Drop-Editor geladen werden. Wenn Sie jedoch ein VPN verwenden oder sich hinter einer Firewall befinden, müssen Sie möglicherweise eine Domain auf die Zulassungsliste setzen. Wenden Sie sich an Ihren IT-Administrator, um sicherzustellen, dass `*.bz-rndr.com` auf der Zulassungsliste steht.

Der Editor kann aus folgenden Gründen Ladeprobleme haben:

- **Vorübergehender Fehler:** Dies sind temporäre Ausfälle, die Konnektivität, Kommunikation oder Datenübertragung beeinträchtigen können. Glücklicherweise lösen sie sich in der Regel von selbst, ohne dass ein größerer Eingriff erforderlich ist, da sie oft durch kurzlebige Bedingungen verursacht werden und keine systemischen Probleme darstellen.
- **Schwerwiegender Fehler:** Dies kann ein zugrunde liegendes Infrastruktur- oder Produktproblem betreffen. Sie können unsere [Braze-Systemstatusseite](https://braze.statuspage.io/) prüfen, da wir wahrscheinlich über die Situation informiert sind und aktiv an einer Lösung arbeiten.

{% alert important %}
Wenn weiterhin Probleme auftreten, [erstellen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support). Stellen Sie vorher sicher, dass Ihr IT-Administrator bestätigt hat, dass `*.bz-rndr.com` auf Ihrer Seite auf der Zulassungsliste steht.
{% endalert %}

### Zugriff auf Braze-Lernangebote {#accessing-braze-learning}

Wenn Sie Probleme bei der Anmeldung bei Braze-Lernangeboten haben und in einer Schleife feststecken, die Sie zum Dashboard weiterleitet, führen Sie die folgenden Schritte aus:

1. Wenn Sie mehrere Braze-Konten haben, werden Sie beim zweimaligen Anmelden mit dem falschen Konto zum Braze-Dashboard weitergeleitet. Bestätigen Sie, dass Sie sich beim richtigen Konto anmelden.
2. Wenn Sie einen Werbeblocker verwenden, bestätigen Sie, dass er ausgeschaltet ist. Er kann Cookies blockieren, die für die Single-Sign-on-Funktionalität erforderlich sind.
3. Gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und überprüfen Sie, dass Single Sign-on (Single Sign-on) aktiviert ist.
4. Bestätigen Sie, dass Ihr Dashboard-Kundenprofil or Nutzerprofil sowohl einen Vor- als auch einen Nachnamen enthält. Ein fehlender Nachname kann den Anmeldevorgang stören.
5. Greifen Sie auf die Braze-Lernangebote über Ihr Dashboard zu, indem Sie zu **Support** > **Braze Learning** navigieren.
6. Wenn weiterhin Probleme auftreten, ziehen Sie in Betracht, Ihr Konto neu zu erstellen. Nutzer:innen, die während der kostenlosen Demophase auf die Braze-Lernangebote zugegriffen haben, können jetzt möglicherweise Schwierigkeiten beim Zugriff haben.

### Probleme mit der Zwei-Faktor-Authentifizierung (2FA) {#two-factor-authentication-2fa-issues}

Wenn ein/e Nutzer:in Probleme mit der Zwei-Faktor-Authentifizierung (2FA) hat und nicht auf das Braze-Dashboard zugreifen kann, kann dies verschiedene Ursachen haben. Am häufigsten hat er/sie keinen Zugang mehr zur registrierten Telefonnummer oder dem Gerät, auf dem die Authy-App installiert ist.

Ein Administrator sollte die 2FA für den/die betroffene/n Nutzer:in wie folgt zurücksetzen:

1. Gehen Sie zu **Einstellungen** > **Nutzerverwaltung**.
2. Wählen Sie den/die Nutzer:in mit 2FA-Problemen aus.
3. Wählen Sie unter **Two Factor Authentication** die Option **Reset**.
4. Bestätigen Sie die 2FA-Zurücksetzung, wenn Sie dazu aufgefordert werden.
5. Wenn die Zurücksetzung das Problem nicht sofort löst, löschen Sie Ihre Cookies und den Cache.

Braze kann die 2FA aus Sicherheitsgründen nicht im Namen von Nutzer:innen zurücksetzen. Wenn der Administrator die 2FA nicht zurücksetzen kann, erstellen Sie ein Support-Ticket.

#### Hinweise {#considerations}

- Wenn 2FA auf Unternehmensebene erzwungen wird: Nach der Zurücksetzung fordert Braze den/die Nutzer:in auf, die 2FA bei der nächsten Anmeldung erneut einzurichten.
- Wenn 2FA nicht auf Unternehmensebene erzwungen wird: Der/die Nutzer:in meldet sich am Dashboard an, ohne die 2FA erneut einrichten zu müssen. Wenn er/sie die 2FA aktivieren möchte, kann dies in den Kontoeinstellungen erfolgen.

{% alert note %}
Dieser Zurücksetzungsprozess gilt auch für Nutzer:innen, die aufgrund zu vieler Token / Textbaustein-Anfragen innerhalb der letzten Stunde aus ihrem Konto ausgesperrt wurden.
{% endalert %}

### Konto-Aussperrung {#locked-out-of-account}

Wenn Sie aus Ihrem Braze-Konto ausgesperrt sind, können Sie mit den folgenden Schritten wieder Zugang erhalten.

Sie können anhand der Fehlermeldung erkennen, welche Art von Aussperrung vorliegt:

- [Ich sehe einen Fehler bezüglich meines Passworts.](#password-error)
- [Ich sehe keinen Fehler, aber Braze lässt mich trotzdem nicht rein.](#instance-error)
- [Ich sehe einen Fehler bezüglich einer Kontosperrung.](#account-suspension)

#### Passwortfehler {#password-error}

Ihre Kontosicherheit ist uns wichtig, daher sind Passwörter für die Anmeldung bei Ihrem Braze-Konto erforderlich.
- Überprüfen Sie, ob Sie sich bei der richtigen [Braze-Dashboard-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) anmelden. Wenden Sie sich zur Bestätigung an Ihren Account-Administrator oder Braze Account Manager:in.
- Ihr Passwort ist möglicherweise abgelaufen und Sie müssen es [zurücksetzen](#resetting-your-password).
- Wenn Sie einen [Single-Sign-on]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)-Dienst verwenden, prüfen Sie mit Ihrem Account-Administrator, ob die Einrichtung korrekt abgeschlossen wurde.
- Wenn Ihr Unternehmen mehrere Braze-Instanzen nutzt, verwenden Sie möglicherweise die falsche E-Mail-Adresse zur Anmeldung.

Im Zweifelsfall können Sie jederzeit [Ihr Passwort zurücksetzen](#resetting-your-password).

#### Instanzfehler {#instance-error}

Wenn Sie den gleichen Computer wie üblich zur Anmeldung verwenden, sollte Braze automatisch die richtige Instanz erkennen. Falls dies jedoch nicht der Fall ist oder Sie sich zum ersten Mal anmelden, beachten Sie Folgendes:

- Überprüfen Sie, ob Sie sich bei der richtigen [Braze-Dashboard-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) anmelden. Wenden Sie sich zur Bestätigung an Ihren Account-Administrator oder Braze Account Manager:in.
- Wenn Ihr Unternehmen mehrere Braze-Instanzen nutzt, verwenden Sie möglicherweise die falsche E-Mail-Adresse zur Anmeldung.

#### Kontosperrung {#account-suspension}

Dies kommt nicht sehr häufig vor, aber Braze nimmt Kontosperrungen und -löschungen sehr ernst. Wenn beim Anmeldeversuch der Fehler „Account has been banned“ angezeigt wird, ist Ihr Dashboard-Konto vorübergehend gesperrt. Dies kann verschiedene Gründe haben.

| Grund | Beschreibung |
| --- | --- |
| Zahlungsprobleme | Das Braze-Konto Ihres Unternehmens hat möglicherweise offene Abrechnungs- oder Zahlungsprobleme. |
| Richtlinienverstöße | Das Konto hat möglicherweise gegen die Nutzungsbedingungen oder Richtlinien zur akzeptablen Nutzung von Braze verstoßen. |
| Sicherheitsbedenken | Verdächtige Aktivitäten haben möglicherweise aus Sicherheitsgründen eine automatische Sperrung ausgelöst. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Grund für Kontosperrung" }

Um dieses Problem zu lösen, wenden Sie sich an den Braze-Administrator Ihres Unternehmens, Ihren Braze Account Manager:in oder den [Support]({{site.baseurl}}/support_contact).

### Braze-Dashboard wird nicht geladen oder funktioniert nicht wie erwartet {#braze-dashboard-wont-load-or-work-as-expected}

Testen Sie zunächst, ob das Dashboard in einem anderen Browser geladen wird. Wenn das Problem in einem anderen Browser nicht auftritt, versuchen Sie Folgendes:

- **Dashboard neu starten:** Melden Sie sich ab, schließen Sie Ihren Browser und versuchen Sie dann, sich bei Ihrem Dashboard anzumelden.
- **Lokalen Browser Update or aktualisieren or aktualisieren:** [Löschen Sie Ihre Cookies und Ihren Browser-Cache](#clearing-your-browser-cache-and-cookies) und versuchen Sie dann, sich erneut bei Ihrem Dashboard anzumelden.
- **Kompatible Plugins oder Drittanbieter-Tools verwenden:** Werbeblocker oder Sicherheitssoftware können das Laden des Braze-Dashboards verhindern. Testen Sie dies, indem Sie einen Werbeblocker deaktivieren und sich dann bei Ihrem Braze-Dashboard anmelden.
        - Sie können auch Ihre Browser-Konsolenprotokolle überprüfen. Fehler im Zusammenhang mit `ERR_BLOCKED_BY_CLIENT` können darauf hinweisen, dass der Inhalt von einem Werbeblocker blockiert wird.
- **Verbindungsqualität prüfen:** Ihre Verbindungsqualität ist möglicherweise schlecht. Versuchen Sie, sich auf einem anderen Gerät bei Ihrem Braze-Dashboard anzumelden.
- **Richtigen Cluster bestätigen:** Stellen Sie sicher, dass Sie sich bei dem Cluster anmelden, der Ihrem Unternehmen zugewiesen ist. Beispielsweise könnten Sie US-03 zugewiesen sein, melden sich aber bei US-01 an.
- **Browser Update or aktualisieren or aktualisieren:** Update or aktualisieren or aktualisieren Sie Ihren Browser auf die neueste [unterstützte Browserversion](#supported-browsers) und versuchen Sie dann, sich bei Ihrem Dashboard anzumelden.

Wenn das Problem in allen Browsern auftritt, versuchen Sie Folgendes:

- **Netzwerkverbindung prüfen:** Versuchen Sie, Ihr VPN auszuschalten, falls möglich, oder deaktivieren und reaktivieren Sie Ihre Netzwerkverbindung.
- **Gerät neu starten:** Versuchen Sie, sich nach einem Neustart Ihres Geräts bei Ihrem Braze-Dashboard anzumelden.

Wenn Sie die vorherigen Probleme gelöst haben und Ihr Dashboard immer noch nicht geladen wird oder nicht wie erwartet funktioniert, wenden Sie sich an den [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Nutzer:in gehört keinem Workspace an {#the-user-belongs-to-no-workspace}

Administratoren können dies beheben, indem sie zu **Einstellungen** > **Nutzerverwaltung** gehen, die Workspace-bezogenen Berechtigungen des/der Nutzer:in prüfen und die erforderlichen Workspaces unter **Workspaces** hinzufügen.

### Fehlerbehebung als neue/r Nutzer:in {#troubleshooting-as-a-new-user}

Wenn Sie ein/e neue/r Braze-Nutzer:in sind und Schwierigkeiten bei der Anmeldung oder beim erstmaligen Zugriff auf Ihr Konto haben, befolgen Sie diese Schritte, um häufige Probleme zu beheben:

#### Ich habe nie die Willkommens-E-Mail erhalten {#i-never-received-the-welcome-email}

- Spam-Ordner überprüfen: Bestätigen Sie, dass die Kontoaktivierungs-E-Mail nicht in Ihren Spam- oder Junk-Ordner gefiltert wurde.
- E-Mail-Adresse überprüfen: Lassen Sie Ihren Administrator die E-Mail-Adresse prüfen, die mit Ihrem neuen Braze-Konto verknüpft ist, um sicherzustellen, dass sie korrekt ist.
- IT-Richtlinien: Bestätigen Sie mit Ihrem IT-Team, dass keine Richtlinien vorhanden sind, die den Empfang der Aktivierungs-E-Mail verhindern könnten.

#### Ich habe die E-Mail erhalten, komme aber bei der Einrichtung der Zwei-Faktor-Authentifizierung (2FA) nicht weiter {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

Wenn Sie während der 2FA-Einrichtung **Start setup** auswählen, aber nie einen Bestätigungscode erhalten (per Kurzmitteilungsdienst or SMS oder E-Mail) oder die Einrichtung der Authenticator-App nicht abschließen können, können Browsererweiterungen, Cookie-Einstellungen oder Netzwerkbeschränkungen den Vorgang stören. Versuchen Sie Folgendes:

- Werbeblocker deaktivieren und Drittanbieter-Cookies aktivieren: Werbeblocker oder Datenschutzerweiterungen können den 2FA-Bestätigungsablauf blockieren. Deaktivieren Sie diese vorübergehend und bestätigen Sie, dass Drittanbieter-Cookies in Ihren Browsereinstellungen aktiviert sind.
- Anderen Browser verwenden: Wechseln Sie zu einem anderen Browser, um browserspezifische Probleme auszuschließen.
- Netzwerk wechseln: Wenn Sie sich in einem Unternehmensnetzwerk befinden, können Firewall-Richtlinien die 2FA-Einrichtung beeinträchtigen. Versuchen Sie, zu einer persönlichen Verbindung oder einem mobilen Hotspot zu wechseln.
- Authenticator-App vor der Browser-Einrichtung installieren: Laden Sie eine Authenticator-App herunter und installieren Sie sie (z. B. Authy, Google Authenticator oder LastPass Authenticator) auf Ihrem Mobilgerät, bevor Sie während der Einrichtung **Authenticator app** auswählen.
- Veraltete Authenticator-Profile löschen: Wenn Sie zuvor mit der Einrichtung der Authenticator-App begonnen haben, diese aber nicht abgeschlossen wurde, löschen Sie veraltete Profile in Ihrer App und scannen Sie den QR-Code erneut.

Wenn Sie nach diesen Schritten weiterhin Probleme haben:

- 2FA zurücksetzen: Ihr Administrator kann die 2FA für Ihr Nutzerkonto in den Einstellungen zurücksetzen.
- Nutzer:in erneut hinzufügen: Wenn Probleme bestehen bleiben, kann der Administrator Ihr Nutzerkonto aus dem Dashboard löschen und Sie erneut hinzufügen. Dies ermöglicht die Erstellung des/der Nutzer:in mit den gleichen Daten.

Wenn die Probleme nach diesen Schritten weiterhin bestehen, wenden Sie sich an den [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) für weitere Unterstützung.

## Nächste Schritte {#next-steps}

Nachdem Sie auf Ihr Konto zugegriffen haben, erkunden Sie diese Ressourcen:

- [Das Braze-Dashboard]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard), um zu erfahren, wie Sie wichtige Features und Tools navigieren.
- [Spracheinstellungen]({{site.baseurl}}/user_guide/administer/personal/language_settings), um Ihre bevorzugte Dashboard-Sprache festzulegen.