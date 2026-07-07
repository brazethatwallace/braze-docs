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

Ob es Ihre erste oder hundertste Anmeldung ist – so greifen Sie auf Ihr Dashboard zu. Wenn Sie die erste Nutzer:in Ihres Unternehmens sind, folgen Sie den Anweisungen im vorherigen Abschnitt. Andernfalls können Sie sich anmelden, nachdem die Braze-Admin Ihres Unternehmens Ihr Konto erstellt hat.

Sie können sich entweder über die [Braze.com](https://www.braze.com)-Startseite anmelden oder Ihre Dashboard-URL verwenden, die Ihrer spezifischen [Braze-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) entspricht. Für Ihren Komfort bietet Braze mehrere Single-Sign-on-Optionen (SSO) an, wie zum Beispiel:

* [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [SAML Just-in-Time-Bereitstellung]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

Nachdem Sie sich über SSO bei Braze angemeldet haben, können Sie sich nicht mehr mit Ihrem Passwort im Dashboard anmelden. Beide E-Mail-Adressen leiten E-Mails an denselben Posteingang weiter, aber Braze erkennt sie bei der Anmeldung als separate Konten. Das Löschen von Cookies meldet Sie ab, sodass nicht gespeicherte Arbeit verloren geht.

## Unterstützte Browser {#supported-browsers}

Das Braze-Dashboard unterstützt die folgenden Browser:
- Chrome (Version 87 oder neuer)
- Firefox (Version 85 oder neuer)
- Safari (Version 15.4 oder neuer)
- Edge (Version 87 oder neuer)

Wenn Ihr Braze-Dashboard einen unerwarteten Fehler anzeigt und das Konsolen-Tool Ihres Browsers den Fehler `ReferenceError: structuredClone is not defined` zeigt, ist Ihr Browser veraltet. Wenn dieser Fehler wiederholt auftritt, deinstallieren Sie Ihren Browser und installieren Sie ihn neu.

## Zugriff auf mehrere Braze-Dashboards {#accessing-multiple-braze-dashboards}

Braze erlaubt es nicht, dieselbe E-Mail-Adresse für mehrere Dashboard-Nutzer:innen im selben Cluster zu registrieren (zum Beispiel, wenn Sie zwei Dashboards auf US-01 haben). Sie können dieselbe E-Mail verwenden, um Konten auf verschiedenen Clustern zu erstellen (zum Beispiel, wenn Sie ein Dashboard auf US-01 und eines auf US-05 haben). Wenn Sie auf mehrere Braze-Dashboards im selben Cluster zugreifen müssen, können Sie Folgendes tun:

### E-Mail-Aliase verwenden {#use-email-aliases}

Wenn Ihr E-Mail-Anbieter Gmail ist, können Sie Aliase erstellen, indem Sie ein `+`-Zeichen gefolgt von beliebigem Text an Ihre E-Mail-Adresse anhängen. Zum Beispiel:
- **Original-E-Mail:** `rocky@gmail.com`
- **Alias-E-Mail:** `rocky+1@gmail.com`

Beide E-Mail-Adressen leiten E-Mails an denselben Posteingang weiter, aber Braze erkennt sie bei der Anmeldung als separate Konten.

### Separate Aliase bei anderen Anbietern erstellen {#create-separate-aliases-with-other-providers}

Wenn Ihr E-Mail-Anbieter kein `+`-Aliasing unterstützt, können Sie dennoch separate Aliase erstellen, zum Beispiel indem Sie `rocky@braze.com` so einrichten, dass E-Mails an `rocky.lotito@braze.com` weitergeleitet werden. So können mehrere Adressen an denselben Posteingang geleitet werden, während Braze sie als unterschiedliche E-Mails erkennt.

### Multi-Company-Entwickler:innen verwenden {#use-multi-company-developers}

Das Feature Multi-Company-Entwickler:innen ermöglicht die gemeinsame Nutzung eines einzelnen Nutzerkontos über mehrere Unternehmen hinweg. Dashboard-Nutzer:innen können über ihr Nutzerprofilmenü zwischen verschiedenen Unternehmens-Dashboards umschalten.

Wenn Sie SSO verwenden und Multi-Company-Entwickler:innen einrichten möchten, müssen Sie eine benutzerdefinierte SAML-Entity-ID aktivieren, indem Sie eine benutzerdefinierte SAML-SSO-Integration einrichten. Folgen Sie den Schritten unter [Service-Provider-initiierte Anmeldung (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), wenden Sie jedoch diese Änderungen an:
- Ändern Sie die **Entity-ID** für jede Dashboard-Integration in `braze_dashboard_<companyID>`.
- Kontaktieren Sie Ihren Customer-Success-Manager oder Account Manager, um den Feature-Flipper `saml_sso_custom_entity_id` für jedes Dashboard zu aktivieren.

#### Zwei-Faktor-Authentifizierung (2FA) {#two-factor-authentication-2fa}

Wie 2FA für Multi-Company-Entwickler:innen funktioniert, hängt von Ihrer 2FA-Methode ab:

- **E-Mail und SMS:** Ihre 2FA-Einstellungen werden auf alle verknüpften Entwicklerkonten kopiert. Nachdem Sie E-Mail- oder SMS-2FA auf einem Konto eingerichtet haben, gilt dieselbe Methode für alle Ihre Unternehmens-Dashboards.
- **Zeitbasiertes Einmalpasswort (TOTP):** TOTP-Einstellungen werden nicht kontenübergreifend synchronisiert. Wenn Sie eine Authenticator-App verwenden, müssen Sie für jedes Dashboard, bei dem Sie sich direkt anmelden, einen separaten Code einrichten.

Wenn Sie innerhalb des Dashboards zwischen Konten wechseln, müssen Sie die 2FA nur einmal abschließen – beim ersten Mal, wenn Sie sich während dieser Sitzung bei einem verknüpften Konto anmelden.

### Hinweise zu Single Sign-on (SSO) {#considerations-for-single-sign-on-sso}

Wenn Sie Single Sign-on (SSO) verwenden, beachten Sie, dass mehrere verschiedene E-Mail-Adressen zu Komplikationen führen können. Stellen Sie sicher, dass Ihre SSO-Einstellungen korrekt konfiguriert sind, um Zugriffsprobleme zu vermeiden.

## Fehlerbehebung {#troubleshooting}

### Passwort zurücksetzen {#resetting-your-password}

Um Ihr Passwort zurückzusetzen, wählen Sie den Link **Passwort vergessen?** auf der Dashboard-Anmeldeseite. Sie werden aufgefordert, Ihre E-Mail-Adresse einzugeben, um einen Link zum Zurücksetzen Ihres Passworts zu erhalten.

![Dashboard-Anmeldung mit der Aufforderung „Passwort vergessen?“.]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Browser-Cache und Cookies löschen {#clearing-your-browser-cache-and-cookies}

Wenn Sie Probleme mit der Dashboard-Performance haben, z. B. wenn Ihr Dashboard oder Ihre Segment-Performance-Liste nicht geladen wird, versuchen Sie, den Cache und die Cookies Ihres Browsers zu löschen, indem Sie die Schritte für Ihren jeweiligen Browser befolgen.

{% alert important %}
Das Löschen von Cookies meldet Sie ab, sodass nicht gespeicherte Arbeit verloren geht.
{% endalert %}

- [Cache und Cookies in Chrome löschen](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Cookies in Safari auf dem Mac löschen](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Cookies und Website-Daten in Firefox löschen](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Alle Cookies in Microsoft Edge löschen](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Wenn das Löschen von Browser-Cache und Cookies Ihre Probleme nicht löst, kontaktieren Sie den [Support]({{site.baseurl}}/support_contact).

### „Aw, Snap!“-Fehler in Google Chrome {#aw-snap-error-in-google-chrome}

Wenn Google Chrome einen „Aw, Snap!“-Fehler anzeigt, hat Chrome Probleme beim Laden der Braze-Dashboard-Seite. Schritte zur Fehlerbehebung finden Sie unter [Hilfe bei häufigen Fehlermeldungen in Chrome](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en).

### „Bitte Seite aktualisieren“ oder „Unerwarteter Fehler“ beim Navigieren im Dashboard {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

Dieser Fehler kann auftreten, wenn eine Unternehmensnutzer:in keinem Workspace zugeordnet ist. Zur Fehlerbehebung:

1. Gehen Sie zur Seite [Unternehmensnutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).
2. Prüfen Sie, ob die Nutzer:in einem Workspace hinzugefügt wurde.
3. Wenn sie keinem Workspace zugeordnet ist, fügen Sie sie hinzu und weisen Sie die entsprechenden Berechtigungen zu.
4. Bitten Sie die Nutzer:in, ihr Dashboard zu aktualisieren.
5. Wenn das Problem weiterhin besteht, kontaktieren Sie den [Support]({{site.baseurl}}/support_contact).

### Zugriff auf den Drag-and-Drop-Editor {#accessing-the-drag-and-drop-editor}

Für die meisten Unternehmensnutzer:innen sollte der Drag-and-Drop-Editor geladen werden. Wenn Sie jedoch ein VPN verwenden oder sich hinter einer Firewall befinden, müssen Sie möglicherweise eine Domain auf die Allowlist setzen. Kontaktieren Sie Ihre IT-Administrator:in, um zu prüfen, ob `*.bz-rndr.com` auf der Allowlist steht.

Der Editor kann aufgrund der folgenden Ursachen Ladeprobleme haben:

- **Vorübergehender Fehler:** Dies sind temporäre Ausfälle, die Konnektivität, Kommunikation oder Datenübertragung beeinträchtigen können. Glücklicherweise lösen sie sich in der Regel von selbst, ohne dass ein erheblicher Eingriff erforderlich ist, da sie oft durch kurzlebige Bedingungen verursacht werden und keine systemischen Probleme darstellen.
- **Schwerwiegender Fehler:** Dies kann ein zugrunde liegendes Infrastruktur- oder Produktproblem betreffen. Sie können unsere [Braze-Systemstatusseite](https://braze.statuspage.io/) überprüfen, da wir wahrscheinlich über die Situation informiert sind und aktiv an einer Lösung arbeiten.

{% alert important %}
Wenn Sie weiterhin Probleme haben, [erstellen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support). Stellen Sie vorher sicher, dass Ihre IT-Administrator:in bestätigt hat, dass `*.bz-rndr.com` auf Ihrer Seite auf der Allowlist steht.
{% endalert %}

### Zugriff auf Braze-Lernangebote {#accessing-braze-learning}

Wenn Sie Probleme beim Anmelden bei Braze-Lernangeboten haben und in einer Schleife feststecken, die Sie zum Dashboard weiterleitet, führen Sie die folgenden Schritte aus:

1. Wenn Sie mehrere Braze-Konten haben, kann eine zweimalige Anmeldung mit dem falschen Konto Sie zum Braze-Dashboard weiterleiten. Bestätigen Sie, dass Sie sich beim richtigen Konto anmelden.
2. Wenn Sie einen Werbeblocker verwenden, bestätigen Sie, dass dieser deaktiviert ist. Er kann Cookies blockieren, die für die Single-Sign-on-Funktionalität erforderlich sind.
3. Gehen Sie zu **Unternehmenseinstellungen** > **Sicherheitseinstellungen** und überprüfen Sie, ob Single Sign-on (SSO) aktiviert ist.
4. Bestätigen Sie, dass Ihr Dashboard-Nutzerprofil sowohl einen Vor- als auch einen Nachnamen enthält. Ein fehlender Nachname kann den Anmeldevorgang stören.
5. Greifen Sie auf Braze-Lernangebote über Ihr Dashboard zu, indem Sie zu **Support** > **Braze-Lernangebote** navigieren.
6. Wenn Sie weiterhin Probleme haben, erwägen Sie, Ihr Konto neu zu erstellen. Nutzer:innen, die während der kostenlosen Demo auf Braze-Lernangebote zugegriffen haben, können jetzt möglicherweise Schwierigkeiten beim Zugriff haben.

### Probleme mit der Zwei-Faktor-Authentifizierung (2FA) {#two-factor-authentication-2fa-issues}

Wenn eine Nutzer:in Probleme mit der Zwei-Faktor-Authentifizierung (2FA) hat und nicht auf das Braze-Dashboard zugreifen kann, kann dies verschiedene Gründe haben. Am häufigsten hat die Person keinen Zugriff mehr auf die registrierte Telefonnummer oder das Gerät, auf dem die Authy-App installiert ist.

Eine Admin sollte die 2FA für die betroffene Nutzer:in wie folgt zurücksetzen:

1. Gehen Sie zu **Nutzer:innen verwalten**.
2. Wählen Sie **Nutzer:in bearbeiten** für die Nutzer:in mit 2FA-Problemen.
3. Wählen Sie die Option zum Zurücksetzen der 2FA.
4. Bestätigen Sie das Zurücksetzen der 2FA, wenn Sie dazu aufgefordert werden.
5. Wenn das Zurücksetzen das Problem nicht sofort löst, löschen Sie Ihre Cookies und den Cache.

Braze kann die 2FA aus Sicherheitsgründen nicht im Auftrag von Nutzer:innen zurücksetzen. Wenn die Admin die 2FA nicht zurücksetzen kann, erstellen Sie ein Support-Ticket.

#### Hinweise {#considerations}

- Wenn 2FA auf Unternehmensebene erzwungen wird: Nach dem Zurücksetzen fordert Braze die Nutzer:in auf, ihre 2FA bei der nächsten Anmeldung erneut einzurichten.
- Wenn 2FA nicht auf Unternehmensebene erzwungen wird: Die Nutzer:in meldet sich im Dashboard an, ohne die 2FA erneut einrichten zu müssen. Wenn sie die 2FA aktivieren möchte, kann sie dies in den Kontoeinstellungen tun.

{% alert note %}
Dieser Zurücksetzungsprozess gilt auch für Nutzer:innen, die aus ihrem Konto ausgesperrt wurden, weil sie innerhalb der letzten Stunde zu viele Token angefordert haben.
{% endalert %}

### Aus dem Konto ausgesperrt {#locked-out-of-account}

Wenn Sie aus Ihrem Braze-Konto ausgesperrt sind, können Sie mit den folgenden Schritten wieder Zugang erhalten.

Sie können anhand der Fehlermeldung erkennen, welche Art von Sperrung vorliegt:

- [Ich sehe einen Fehler bezüglich meines Passworts.](#password-error)
- [Ich sehe keinen Fehler, aber Braze lässt mich trotzdem nicht rein.](#instance-error)
- [Ich sehe einen Fehler bezüglich einer Kontosperrung.](#account-suspension)

#### Passwortfehler {#password-error}

Die Sicherheit Ihres Kontos ist uns wichtig, daher sind Passwörter für die Anmeldung bei Ihrem Braze-Konto erforderlich.
- Prüfen Sie, ob Sie sich bei der richtigen [Braze-Dashboard-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) anmelden. Wenden Sie sich an Ihre Kontoadministrator:in oder Ihren Braze-Account-Manager, um sicherzugehen.
- Ihr Passwort ist möglicherweise abgelaufen, sodass Sie es [zurücksetzen](#resetting-your-password) müssen.
- Wenn Sie einen [Single-Sign-on]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)-Dienst verwenden, prüfen Sie bei Ihrer Kontoadministrator:in, ob die Einrichtung korrekt abgeschlossen wurde.
- Wenn Ihr Unternehmen mehrere Braze-Instanzen nutzt, verwenden Sie möglicherweise die falsche E-Mail-Adresse zur Anmeldung.

Im Zweifelsfall können Sie jederzeit [Ihr Passwort zurücksetzen](#resetting-your-password).

#### Instanzfehler {#instance-error}

Wenn Sie denselben Computer verwenden, mit dem Sie sich normalerweise anmelden, sollte Braze automatisch die richtige Instanz erkennen. Falls nicht oder wenn Sie sich zum ersten Mal anmelden, beachten Sie Folgendes:

- Prüfen Sie, ob Sie sich bei der richtigen [Braze-Dashboard-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) anmelden. Wenden Sie sich an Ihre Kontoadministrator:in oder Ihren Braze-Account-Manager, um sicherzugehen.
- Wenn Ihr Unternehmen mehrere Braze-Instanzen nutzt, verwenden Sie möglicherweise die falsche E-Mail-Adresse zur Anmeldung.

#### Kontosperrung {#account-suspension}

Dies kommt nicht sehr häufig vor, aber Braze nimmt Kontosperrungen und -löschungen sehr ernst. Wenn Sie auf diesen Fehler stoßen, wenden Sie sich an die Braze-Administrator:in Ihres Unternehmens, Ihren Braze-Account-Manager oder den [Support][support].

### Braze-Dashboard wird nicht geladen oder funktioniert nicht wie erwartet {#braze-dashboard-wont-load-or-work-as-expected}

Testen Sie zunächst, ob das Dashboard in einem anderen Browser geladen wird. Wenn das Problem in einem anderen Browser nicht auftritt, versuchen Sie Folgendes:

- **Dashboard neu starten:** Melden Sie sich ab, beenden Sie Ihren Browser und versuchen Sie dann, sich erneut in Ihrem Dashboard anzumelden.
- **Lokalen Browser aktualisieren:** [Löschen Sie Ihre Cookies und den Browser-Cache](#clearing-your-browser-cache-and-cookies) und versuchen Sie dann, sich erneut in Ihrem Dashboard anzumelden.
- **Kompatible Plugins oder Drittanbieter-Tools verwenden:** Werbeblocker oder Sicherheitssoftware können das Laden des Braze-Dashboards verhindern. Testen Sie dies, indem Sie einen Werbeblocker deaktivieren und sich dann in Ihrem Braze-Dashboard anmelden.
        - Sie können auch die Konsolenprotokolle Ihres Browsers überprüfen. Fehler im Zusammenhang mit `ERR_BLOCKED_BY_CLIENT` können darauf hinweisen, dass der Inhalt von einem Werbeblocker blockiert wird.
- **Verbindungsqualität prüfen:** Ihre Verbindungsqualität ist möglicherweise schlecht. Versuchen Sie, sich auf einem anderen Gerät in Ihrem Braze-Dashboard anzumelden.
- **Bestätigen Sie, dass Sie auf den richtigen Cluster zugreifen:** Stellen Sie sicher, dass Sie sich bei dem Cluster anmelden, der Ihrem Unternehmen zugewiesen ist. Zum Beispiel könnten Sie US-03 zugewiesen sein, melden sich aber bei US-01 an.
- **Browser aktualisieren:** Aktualisieren Sie Ihren Browser auf den neuesten [unterstützten Browser](#supported-browsers) und versuchen Sie dann, sich in Ihrem Dashboard anzumelden.

Wenn das Problem in allen Browsern auftritt, versuchen Sie Folgendes:

- **Netzwerkverbindung prüfen:** Versuchen Sie, Ihr VPN zu deaktivieren, falls möglich, oder deaktivieren und reaktivieren Sie Ihre Netzwerkverbindung.
- **Gerät neu starten:** Versuchen Sie, sich nach einem Neustart Ihres Geräts in Ihrem Braze-Dashboard anzumelden.

Wenn Sie die vorherigen Probleme gelöst haben und Ihr Dashboard immer noch nicht geladen wird oder nicht wie erwartet funktioniert, kontaktieren Sie den [Support]({{site.baseurl}}/braze_support).

### Die Nutzer:in gehört keinem Workspace an {#the-user-belongs-to-no-workspace}

Überprüfen Sie dies, indem Sie zu **Einstellungen** > **Unternehmensnutzer:innen** gehen und die Workspace-Berechtigungen der Nutzer:in prüfen. Fügen Sie die erforderlichen Workspaces unter **Workspaces** hinzu.

### Fehlerbehebung als neue Nutzer:in {#troubleshooting-as-a-new-user}

Wenn Sie eine neue Braze-Nutzer:in sind und Probleme beim Anmelden oder beim erstmaligen Zugriff auf Ihr Konto haben, befolgen Sie diese Schritte, um häufige Probleme zu lösen:

#### Ich habe die Willkommens-E-Mail nie erhalten {#i-never-received-the-welcome-email}

- Prüfen Sie Ihren Spam-Ordner: Bestätigen Sie, dass die Kontoaktivierungs-E-Mail nicht in Ihren Spam- oder Junk-Ordner gefiltert wurde.
- Überprüfen Sie Ihre E-Mail-Adresse: Lassen Sie Ihre Admin die E-Mail-Adresse überprüfen, die mit Ihrem neuen Braze-Konto verknüpft ist, um sicherzustellen, dass sie korrekt ist.
- IT-Richtlinien: Klären Sie mit Ihrem IT-Team, ob Richtlinien vorhanden sind, die den Empfang der Aktivierungs-E-Mail verhindern könnten.

#### Ich habe die E-Mail erhalten, aber die Einrichtung der Zwei-Faktor-Authentifizierung (2FA) funktioniert nicht {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

- 2FA zurücksetzen: Wenn Sie Probleme bei der Einrichtung der 2FA haben, kann Ihre Admin die 2FA für Ihr Nutzerkonto in den Einstellungen zurücksetzen.
- Nutzer:in erneut hinzufügen: Wenn die Probleme weiterhin bestehen, kann die Admin Ihr Nutzerkonto aus dem Dashboard löschen und Sie erneut hinzufügen. Dies ermöglicht die Erstellung der Nutzer:in mit denselben Daten.

Wenn die Probleme nach diesen Schritten weiterhin bestehen, kontaktieren Sie den [Support]({{site.baseurl}}/braze_support) für weitere Unterstützung.

## Nächste Schritte {#next-steps}

Nachdem Sie auf Ihr Konto zugegriffen haben, erkunden Sie diese Ressourcen:

- [Das Braze-Dashboard]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard), um zu erfahren, wie Sie wichtige Features und Tools navigieren.
- [Spracheinstellungen]({{site.baseurl}}/user_guide/administer/personal/language_settings), um Ihre bevorzugte Dashboard-Sprache festzulegen.