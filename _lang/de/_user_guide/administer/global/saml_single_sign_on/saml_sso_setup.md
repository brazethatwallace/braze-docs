---
nav_title: SAML SSO einrichten
article_title: SAML SSO einrichten
page_order: 0
page_type: tutorial
toc_headers: h2
description: "Dieser Artikel führt Sie durch die Aktivierung von SAML Single Sign-on für Ihr Braze-Konto."

---

# Vom Service Provider (SP) initiierte Anmeldung {#service-provider-sp-initiated-login}

> Dieser Artikel führt Sie durch die Aktivierung von SAML Single Sign-on für Ihr Braze-Konto und erklärt, wie Sie einen SAML-Trace erhalten.

## Anforderungen {#requirements}

Bei der Einrichtung werden Sie aufgefordert, eine Anmelde-URL und eine Assertion Consumer Service (ACS)-URL anzugeben.

| Anforderung | Details |
|---|---|
| Assertion Consumer Service (ACS)-URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Für Domains in der Europäischen Union lautet die ACS-URL `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Bei einigen IdPs kann dies auch als Reply-URL, Anmelde-URL, Audience-URL oder Audience-URI bezeichnet werden. |
| Entity ID | `braze_dashboard` |
| RelayState-API-Schlüssel | Gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login`-Berechtigungen. Geben Sie dann den generierten API-Schlüssel als `RelayState`-Parameter in Ihrem IdP ein. Detaillierte Schritte finden Sie unter [Ihren RelayState einrichten](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## SAML SSO einrichten {#setting-up-saml-sso}

### 1. Schritt: Ihren Identity Provider konfigurieren {#step-1-configure-your-identity-provider}

Richten Sie Braze als Service Provider (SP) in Ihrem Identity Provider (IdP) mit den folgenden Informationen ein. Richten Sie außerdem das SAML-Attribut-Mapping ein.

{% alert important %}
Wenn Sie Okta als Identity Provider verwenden möchten, stellen Sie sicher, dass Sie die vorgefertigte Integration auf der [Okta-Website](https://www.okta.com/integrations/braze/) nutzen.
{% endalert %}

| SAML-Attribut | Erforderlich? | Akzeptierte SAML-Attribute |
|---|---|---|
|`email` | Erforderlich | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1: Ihren Identity Provider konfigurieren" }

{% alert note %}
Braze benötigt in der SAML-Assertion nur `email`.
{% endalert %}

### 2. Schritt: Braze konfigurieren {#step-2-configure-braze}

Wenn Sie die Einrichtung von Braze in Ihrem Identity Provider abgeschlossen haben, stellt Ihnen Ihr Identity Provider eine Ziel-URL und ein `x.509`-Zertifikat zur Eingabe in Ihr Braze-Konto bereit.

Nachdem Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**.

Geben Sie auf derselben Seite Folgendes ein:

| Anforderung | Details |
|---|---|
| SAML-Name | Dieser wird als Button-Text auf dem Anmeldebildschirm angezeigt.<br>Dies ist in der Regel der Name Ihres Identity Providers, z. B. „Okta“. |
| Ziel-URL | Diese wird nach der Einrichtung von Braze in Ihrem IdP bereitgestellt.<br> Einige IdPs bezeichnen dies als SSO-URL oder SAML 2.0-Endpunkt. |
| Zertifikat | Das `x.509`-Zertifikat, das von Ihrem Identity Provider bereitgestellt wird.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Braze konfigurieren" }

Stellen Sie sicher, dass Ihr `x.509`-Zertifikat beim Hinzufügen zum Dashboard folgendes Format hat:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![SAML SSO-Einstellungen mit aktiviertem Umschalter.]({% image_buster /assets/img/samlsso.png %})

### 3. Schritt: Bei Braze anmelden {#step-3-sign-into-braze}

Speichern Sie Ihre Sicherheitseinstellungen und melden Sie sich ab. Melden Sie sich dann mit Ihrem Identity Provider wieder an.

![Dashboard-Anmeldebildschirm mit aktiviertem SSO]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## Ihren RelayState einrichten {#setting-up-your-relaystate}

1. Gehen Sie in Braze zu **Einstellungen** > **APIs und Bezeichner**.
2. Wählen Sie im Tab **API-Schlüssel** den Button **API-Schlüssel erstellen**.
3. Geben Sie im Feld **API-Schlüsselname** einen Namen für Ihren Schlüssel ein.
4. Erweitern Sie das Dropdown **SSO** unter **Berechtigungen** und aktivieren Sie **sso.saml.login**.<br><br>![Der Abschnitt „Berechtigungen“ mit aktiviertem sso.saml.login.]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. Wählen Sie **API-Schlüssel erstellen**.
6. Kopieren Sie im Tab **API-Schlüssel** den Bezeichner neben dem von Ihnen erstellten API-Schlüssel.
7. Fügen Sie den RelayState-API-Schlüssel in den RelayState Ihres IdP ein (er kann je nach IdP auch als „Relay State“ oder „Default Relay State“ angezeigt werden).

## SSO-Verhalten {#sso-behavior}

Mitglieder, die sich für die Nutzung von SSO entscheiden, können ihr Passwort nicht mehr wie zuvor verwenden. Nutzer:innen, die weiterhin ihr Passwort verwenden, können dies tun, sofern sie nicht durch die folgenden Einstellungen eingeschränkt werden.

## Einschränkung {#restriction}

Sie können die Mitglieder Ihrer Organisation darauf beschränken, sich nur mit Google SSO oder SAML SSO anzumelden. Um Einschränkungen zu aktivieren, gehen Sie zu **Sicherheitseinstellungen** und wählen Sie entweder **Nur Google SSO-Anmeldung erzwingen** oder **Nur benutzerdefinierte SAML SSO-Anmeldung erzwingen**.

![Beispielkonfiguration des Abschnitts „Authentifizierungsregeln“ mit einer Mindestpasswortlänge von 8 Zeichen und einer Passwort-Wiederverwendbarkeit von 3 Mal. Passwörter laufen nach 180 Tagen ab, und Nutzer:innen werden nach 1.440 Minuten Inaktivität abgemeldet.]({% image_buster /assets/img/sso3.png %})

Durch die Aktivierung von Einschränkungen können sich die Braze-Nutzer:innen Ihres Unternehmens nicht mehr mit einem Passwort anmelden, selbst wenn sie sich zuvor mit einem Passwort angemeldet haben.

## Einen SAML-Trace erhalten {#obtaining-a-saml-trace}

Wenn Sie Anmeldeprobleme im Zusammenhang mit SSO haben, kann Ihnen ein SAML-Trace bei der Fehlerbehebung Ihrer SSO-Verbindung helfen, indem er zeigt, was in den SAML-Anfragen gesendet wird.

### Voraussetzungen {#prerequisites}

Um einen SAML-Trace auszuführen, benötigen Sie einen SAML-Tracer. Hier sind zwei mögliche Optionen je nach Browser:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### 1. Schritt: Den SAML-Tracer öffnen {#step-1-open-the-saml-tracer}

Wählen Sie den SAML-Tracer in der Navigationsleiste Ihres Browsers aus. Stellen Sie sicher, dass **Pause** nicht ausgewählt ist, da dies den SAML-Tracer daran hindert, die in den SAML-Anfragen gesendeten Daten zu erfassen. Wenn der SAML-Tracer geöffnet ist, sehen Sie, wie er den Trace befüllt.

![SAML-Tracer für Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### 2. Schritt: Bei Braze mit SSO anmelden {#step-2-sign-into-braze-using-sso}

Gehen Sie zu Ihrem Braze-Dashboard und versuchen Sie, sich mit SSO anzumelden. Wenn ein Fehler auftritt, öffnen Sie den SAML-Tracer und versuchen Sie es erneut. Ein SAML-Trace wurde erfolgreich erfasst, wenn eine Zeile mit einer URL wie `https://dashboard-XX.braze.com/auth/saml/callback` und einem orangefarbenen SAML-Tag vorhanden ist.

### 3. Schritt: Exportieren und an Braze senden {#step-3-export-and-send-to-braze}

Wählen Sie **Export**. Wählen Sie unter **Select cookie-filter profile** die Option **None**. Wählen Sie dann **Export**. Dies generiert eine JSON-Datei, die Sie zur weiteren Fehlerbehebung an den Braze-Support senden können.

![Menü „Export SAML-trace preferences“ mit ausgewählter Option „None“.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Fehlerbehebung {#troubleshooting}

### Ist die E-Mail-Adresse der Nutzerin oder des Nutzers korrekt eingerichtet? {#is-the-users-email-address-correctly-set-up}

Wenn Sie den Fehler `ERROR_CODE_SSO_INVALID_EMAIL` erhalten, ist die E-Mail-Adresse der Nutzerin oder des Nutzers ungültig. Überprüfen Sie im SAML-Trace, ob das Feld `saml2:Attribute Name="email"` mit der E-Mail-Adresse übereinstimmt, die die Nutzerin oder der Nutzer zur Anmeldung verwendet. Wenn Sie Microsoft Entra ID (ehemals Azure Active Directory) verwenden, lautet das Attribut-Mapping `email = user.userprincipalname`.

Die E-Mail-Adresse unterscheidet zwischen Groß- und Kleinschreibung und muss exakt mit der in Braze eingerichteten übereinstimmen, einschließlich der in Ihrem Identity Provider (wie Okta, OneLogin, Microsoft Entra ID und andere) konfigurierten Adresse.

Weitere Fehler, die auf Probleme mit der E-Mail-Adresse der Nutzerin oder des Nutzers hinweisen:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: Die E-Mail-Adresse der Nutzerin oder des Nutzers ist nicht im Dashboard vorhanden.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: Die E-Mail-Adresse der Nutzerin oder des Nutzers ist leer oder anderweitig falsch konfiguriert.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` oder `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: Die E-Mail-Adresse der Nutzerin oder des Nutzers stimmt nicht mit der für SSO eingerichteten überein.

### Haben Sie ein gültiges SAML-Zertifikat (x.509-Zertifikat)? {#do-you-have-a-valid-saml-certificate-x509-certificate}

Sie können Ihr SAML-Zertifikat mit [diesem SAML-Validierungstool](https://www.samltool.com/validate_response.php) überprüfen. Beachten Sie, dass ein abgelaufenes SAML-Zertifikat ebenfalls ein ungültiges SAML-Zertifikat ist.

### Haben Sie ein korrektes SAML-Zertifikat (x.509-Zertifikat) hochgeladen? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

Überprüfen Sie, ob das Zertifikat im Abschnitt `ds:X509Certificate` des SAML-Trace mit dem übereinstimmt, das Sie in Braze hochgeladen haben. Dies schließt den Header `-----BEGIN CERTIFICATE-----` und den Footer `-----END CERTIFICATE-----` nicht ein.

### Haben Sie Ihr SAML-Zertifikat (x.509-Zertifikat) falsch eingegeben oder formatiert? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Stellen Sie sicher, dass im Zertifikat, das Sie im Braze-Dashboard eingereicht haben, keine Leerzeichen oder zusätzlichen Zeichen enthalten sind.

Wenn Sie Ihr Zertifikat in Braze eingeben, muss es Privacy Enhanced Mail (PEM)-kodiert und korrekt formatiert sein (einschließlich des Headers `-----BEGIN CERTIFICATE-----` und des Footers `-----END CERTIFICATE-----`).

Hier ist ein Beispielzertifikat mit korrekter Formatierung:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### Ist das Sitzungs-Token der Nutzerin oder des Nutzers gültig? {#is-the-users-session-token-valid}

Lassen Sie die betroffene Nutzerin oder den betroffenen Nutzer [den Cache und die Cookies des Browsers löschen](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) und versuchen Sie dann erneut, sich mit SAML SSO anzumelden.

### Haben Sie Ihren RelayState eingerichtet? {#did-you-set-your-relaystate}

Wenn Sie den Fehler `ERROR_CODE_SSO_INVALID_RELAY_STATE` erhalten, könnte Ihr RelayState falsch konfiguriert oder nicht vorhanden sein. Falls noch nicht geschehen, müssen Sie Ihren RelayState in Ihrem IdP-Verwaltungssystem einrichten. Die Schritte finden Sie unter [Ihren RelayState einrichten](#setting-up-your-relaystate).

### Führt eine erfolgreiche SSO-Anmeldung zurück zur Braze-Anmeldeseite? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

Dies kann auftreten, wenn der RelayState nicht korrekt konfiguriert ist. Bestätigen Sie, dass Sie einen API-Schlüssel (unter **Einstellungen** > **API-Schlüssel**) für die IdP-Anmeldung erstellt und diesen API-Schlüssel als `RelayState`-Parameter in Ihrem IdP festgelegt haben. Der RelayState identifiziert, bei welchem Unternehmenskonto Sie sich anmelden. Eine Schritt-für-Schritt-Anleitung finden Sie unter [Ihren RelayState einrichten](#setting-up-your-relaystate).

Wenn Sie sich immer noch nicht anmelden können, [kontaktieren Sie den Braze-Support]({{site.baseurl}}/braze_support/) und fügen Sie nach Möglichkeit einen SAML-Trace bei. Hilfe beim Erfassen eines Trace finden Sie unter [Einen SAML-Trace erhalten](#obtaining-a-saml-trace).

### Steckt die Nutzerin oder der Nutzer in einer Anmeldeschleife zwischen Okta und Braze fest? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Wenn sich eine Nutzerin oder ein Nutzer nicht anmelden kann, weil sie oder er in einer Schleife zwischen Okta SSO und dem Braze-Dashboard feststeckt, müssen Sie in Okta die SSO-URL-Zieladresse auf Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/) setzen (z. B. `https://dashboard-07.braze.com`).

Wenn Sie einen anderen IdP verwenden, überprüfen Sie, ob Ihr Unternehmen das korrekte SAML- oder x.509-Zertifikat in Braze hochgeladen hat.

### Verwenden Sie eine manuelle Integration? {#are-you-using-a-manual-integration}

Wenn Ihr Unternehmen die Braze-App nicht aus dem App Store Ihres IdP heruntergeladen hat, müssen Sie die vorgefertigte Integration herunterladen. Wenn beispielsweise Okta Ihr IdP ist, laden Sie die Braze-App von deren [Integrationsseite](https://www.okta.com/integrations/braze/) herunter.

## Google SSO

Wenn Ihr Unternehmen Google SSO anstelle von benutzerdefiniertem SAML verwendet, kontaktieren Sie Ihren Braze Account Manager, um Google SSO für Ihren Workspace zu aktivieren. Nach der Aktivierung gehen Sie zu **Sicherheitseinstellungen** und wählen Sie **Nur Google SSO-Anmeldung erzwingen**, um die Google-Authentifizierung für alle Unternehmensnutzer:innen verpflichtend zu machen.

Wenn die Google SSO-Erzwingung aktiviert ist, müssen sich Nutzer:innen mit der Google-Authentifizierung anmelden und können kein Braze-Passwort mehr verwenden. Jede Nutzerin und jeder Nutzer muss sich mit dem Google-Konto anmelden, das mit der E-Mail-Adresse ihres bzw. seines Braze-Dashboards übereinstimmt. Wenn eine Nutzerin oder ein Nutzer bei der Anmeldung ein anderes Google-Konto auswählt, lehnt Braze den Authentifizierungsversuch ab.

### Fehlerbehebung bei der Google SSO-Anmeldung {#troubleshooting-google-sso-sign-in}

Wenn sich einige Nutzer:innen nicht mit Google SSO anmelden können, überprüfen Sie Folgendes:

- Die E-Mail-Adresse des Google-Kontos der Nutzerin oder des Nutzers stimmt exakt mit der E-Mail-Adresse im Braze-Dashboard überein.
- Die Nutzerin oder der Nutzer hat Zugriff auf ein Google-Konto für die E-Mail-Adresse des Unternehmens.
- Die Nutzerin oder der Nutzer ist in Braze nicht gesperrt (**Einstellungen** > **Unternehmensnutzer:innen**).

## Nächste Schritte {#next-steps}

Nach der Einrichtung von SAML SSO können Sie:

- [Nur-SSO-Anmeldung erzwingen]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#restriction) in Ihren Sicherheitseinstellungen, um Nutzer:innen daran zu hindern, sich mit einem Passwort anzumelden.
- [SAML Just-in-Time-Bereitstellung einrichten]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning/), damit neue Nutzer:innen bei ihrer ersten SSO-Anmeldung automatisch Braze-Konten erstellen.