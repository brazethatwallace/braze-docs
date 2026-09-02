---
nav_title: SAML Single Sign-on einrichten
article_title: SAML Single Sign-on einrichten
page_order: 0
page_type: tutorial
toc_headers: h2
description: "Dieser Artikel führt Sie durch die Aktivierung von SAML Single Sign-on für Ihr Braze-Konto."
---

# Vom Service Provider (SP) initiierte Anmeldung {#service-provider-sp-initiated-login}

> Dieser Artikel führt Sie durch die Aktivierung von SAML Single Sign-on für Ihr Braze-Konto und erklärt, wie Sie einen SAML-Trace erhalten.

## Voraussetzungen {#requirements}

Bei der Einrichtung werden Sie aufgefordert, eine Anmelde-URL und eine Assertion Consumer Service (ACS)-URL anzugeben.

| Voraussetzung | Details |
|---|---|
| Assertion Consumer Service (ACS)-URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Für Domains in der Europäischen Union lautet die ACS-URL `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Bei einigen IdPs kann dies auch als Reply-URL, Anmelde-URL, Audience-URL oder Audience-URI bezeichnet werden. |
| Entity-ID | Standardmäßig `braze_dashboard`. Wenn Ihr IdP eine unternehmensspezifische Entity-ID erfordert, aktivieren Sie **Benutzerdefinierte Entity-ID** in den **Sicherheitseinstellungen** und verwenden Sie `braze_dashboard_<companyID>`. |
| RelayState-API-Schlüssel | Gehen Sie zu **Einstellungen** > **Einrichtung und Testen** > **APIs und Bezeichner**, öffnen Sie den Tab **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login`-Berechtigungen. Geben Sie den generierten API-Schlüssel als `RelayState`-Parameter in Ihrem IdP ein. Detaillierte Schritte finden Sie unter [Einrichten Ihres RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## SAML Single Sign-on einrichten {#setting-up-saml-sso}

### Schritt 1: Identitätsanbieter konfigurieren {#step-1-configure-your-identity-provider}

Richten Sie Braze als Dienstanbieter (SP) in Ihrem Identitätsanbieter (IdP) mit den folgenden Informationen ein. Richten Sie außerdem die SAML-Attributzuordnung ein.

{% alert important %}
Wenn Sie Okta als Identitätsanbieter verwenden möchten, stellen Sie sicher, dass Sie die vorgefertigte Integration auf der [Okta-Website](https://www.okta.com/integrations/braze/) nutzen.
{% endalert %}

| SAML-Attribut | Erforderlich? | Akzeptierte SAML-Attribute |
|---|---|---|
|`email` | Erforderlich | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1: Identitätsanbieter konfigurieren" }

{% alert note %}
Braze benötigt in der SAML-Assertion nur `email`.
{% endalert %}

### Schritt 2: Braze konfigurieren {#step-2-configure-braze}

Wenn Sie die Einrichtung von Braze in Ihrem Identitätsanbieter abgeschlossen haben, stellt Ihnen Ihr Identitätsanbieter eine Ziel-URL und ein `x.509`-Zertifikat zur Eingabe in Ihr Braze-Konto bereit.

Nachdem Ihr Account Manager:in SAML Single Sign-on für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML Single Sign-on auf **EIN**.

Geben Sie auf derselben Seite Folgendes ein:

| Anforderung | Details |
|---|---|
| SAML-Name | Dieser wird als Button-Text auf dem Anmeldebildschirm angezeigt.<br>Dies ist in der Regel der Name Ihres Identitätsanbieters, z. B. „Okta“. |
| Ziel-URL | Diese wird nach der Einrichtung von Braze in Ihrem IdP bereitgestellt.<br> Einige IdPs bezeichnen dies als Single Sign-on-URL oder SAML 2.0-Endpunkt. |
| Zertifikat | Das `x.509`-Zertifikat, das von Ihrem Identitätsanbieter bereitgestellt wird.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Braze konfigurieren" }

### Benutzerdefinierte Entity-ID {#custom-entity-id}

Standardmäßig verwendet Braze `braze_dashboard` als Entity-ID (in einigen IdPs auch als Audience oder Audience-URI bezeichnet). Wenn Ihr IdP eine unternehmensspezifische Entity-ID erfordert:

1. Aktivieren Sie unter **Sicherheitseinstellungen** die Option **Benutzerdefinierte Entity-ID**.
2. Kopieren Sie die generierte Entity-ID (`braze_dashboard_<companyID>`).
3. Fügen Sie diesen Wert in das Feld Entity-ID, Audience oder Audience-URI Ihres IdP ein.
4. Speichern Sie die Änderungen sowohl in Braze als auch in Ihrem IdP, bevor Sie die Anmeldung testen.

{% alert important %}
Nutzer:innen können sich nicht anmelden, bis die Entity-ID in Braze und Ihrem IdP übereinstimmt. Die benutzerdefinierte Entity-ID erfordert eine zusätzliche Konfiguration in Ihrem Identitätsanbieter.
{% endalert %}

Stellen Sie sicher, dass Ihr `x.509`-Zertifikat beim Hinzufügen zum Dashboard folgendes Format hat:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![SAML SSO-Einstellungen mit aktiviertem Umschalter.]({% image_buster /assets/img/samlsso.png %})

### Schritt 3: Bei Braze anmelden {#step-3-sign-into-braze}

Speichern Sie Ihre Sicherheitseinstellungen und melden Sie sich ab. Melden Sie sich anschließend mit Ihrem Identitätsanbieter wieder an.

## Verwendung einer benutzerdefinierten Entity-ID {#using-a-custom-entity-id}

Standardmäßig verwendet jedes Braze-Dashboard die gemeinsame Entity-ID `braze_dashboard`. Eine benutzerdefinierte Entity-ID gibt Ihrem Dashboard einen eindeutigen Bezeichner, damit Ihr Identitätsanbieter überprüfen kann, dass Anmeldeanfragen für genau dieses Dashboard bestimmt sind. Dies ist nützlich, wenn Sie SAML Single Sign-on über mehrere Braze-Unternehmen im selben Identitätsanbieter einrichten.

Die Verwendung einer benutzerdefinierten Entity-ID ist optional. Wenn Sie sie nicht aktivieren, verwendet Ihr Dashboard weiterhin `braze_dashboard`.

{% alert warning %}
Die vorgefertigte [Braze Okta Marketplace-App](https://www.okta.com/integrations/braze/) erzwingt die gemeinsame Entity-ID `braze_dashboard` und ist nicht mit einer benutzerdefinierten Entity-ID kompatibel. Wenn Sie SAML Single Sign-on bereits mit der Braze Okta Marketplace-App eingerichtet haben, wird das Aktivieren einer benutzerdefinierten Entity-ID ohne Aktualisierung des Entity-ID-Felds in Okta über eine benutzerdefinierte SAML-App die Anmeldung unterbrechen und kann Nutzer:innen aus dem Dashboard aussperren. Um eine benutzerdefinierte Entity-ID mit Okta zu verwenden, richten Sie stattdessen eine benutzerdefinierte SAML-App ein.
{% endalert %}

### Schritt 1: Benutzerdefinierte Entity-ID aktivieren {#step-1-turn-on-the-custom-entity-id}

Gehen Sie zu **Einstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und öffnen Sie den Abschnitt „SAML Single Sign-on“. Aktivieren Sie den Schalter **Benutzerdefinierte Entity-ID**. Braze generiert eine eindeutige Entity-ID für Ihr Dashboard im Format `braze_dashboard_<COMPANY_ID>`. Wenn Sie die Option **Benutzerdefinierte Entity-ID** nicht sehen, wenden Sie sich an Ihren Braze Account Manager:in.

### Schritt 2: Identitätsanbieter Update or aktualisieren or aktualisieren {#step-2-update-your-identity-provider}

Kopieren Sie die generierte Entity-ID und fügen Sie sie in das Entity-ID-Feld der Braze-Anwendung Ihres Identitätsanbieters ein. Je nach Anbieter kann dieses Feld als **Entity ID**, **Audience** oder **Audience URI** bezeichnet sein.

{% alert important %}
Die Entity-ID muss sowohl in Braze als auch bei Ihrem Identitätsanbieter übereinstimmen. Solange nicht beide Seiten denselben Wert verwenden, können sich Nutzer:innen nicht mit SAML Single Sign-on anmelden. Update or aktualisieren or aktualisieren Sie Ihren Identitätsanbieter, bevor Sie diese Seite speichern, um zu vermeiden, dass Nutzer:innen ausgesperrt werden.
{% endalert %}

### Schritt 3: Speichern und testen {#step-3-save-and-test}

Speichern Sie Ihre Sicherheitseinstellungen, melden Sie sich ab und melden Sie sich dann über Ihren Identitätsanbieter wieder an, um zu bestätigen, dass die Anmeldung mit der benutzerdefinierten Entity-ID funktioniert.

## RelayState einrichten {#setting-up-your-relaystate}

1. Gehen Sie in Braze zu **Einstellungen** > **Einrichtung und Tests** > **APIs und Bezeichner**.
2. Wählen Sie im Tab **API-Schlüssel** den Button **API-Schlüssel erstellen** aus.
3. Geben Sie im Feld **API-Schlüsselname** einen Namen für Ihren Schlüssel ein.
4. Erweitern Sie das Dropdown-Menü **Single Sign-on** unter **Berechtigungen** und aktivieren Sie **Single Sign-on.saml.login**.
5. Wählen Sie **API-Schlüssel erstellen** aus.
6. Kopieren Sie im Tab **API-Schlüssel** den Bezeichner neben dem von Ihnen erstellten API-Schlüssel.
7. Fügen Sie den RelayState-API-Schlüssel in den RelayState Ihres IdP ein (er kann je nach IdP auch als „Relay State“ oder „Default Relay State“ erscheinen).

## IdP-initiierte Anmeldung {#idp-initiated-login}

Einige Identitätsanbieter unterstützen die IdP-initiierte Anmeldung, bei der Nutzer:innen den Anmeldevorgang über das IdP-Portal starten, anstatt über die Braze-Anmeldeseite. Die IdP-initiierte Anmeldung erfordert einen gültigen RelayState-API-Schlüssel und eine korrekte Konfiguration der ACS-URL. Anbieterspezifische Einrichtungsleitfäden:

- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Microsoft Entra Single Sign-on]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)

{% alert note %}
Bei der IdP-initiierten Anmeldung mit Microsoft Entra Single Sign-on muss das Feld **Sign-On URL** leer gelassen werden. Weitere Informationen finden Sie unter [Microsoft Entra Single Sign-on]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso).
{% endalert %}

## Single Sign-on-Verhalten {#sso-behavior}

Mitglieder, die sich für die Nutzung von Single Sign-on entscheiden, können ihr Passwort nicht mehr verwenden. Nutzer:innen, die weiterhin ihr Passwort verwenden, können dies tun, sofern sie nicht durch die folgenden Einstellungen eingeschränkt werden.

## Einschränkung {#restriction}

Sie können die Mitglieder Ihrer Organisation darauf beschränken, sich ausschließlich über Google Single Sign-on oder SAML Single Sign-on anzumelden. Um Einschränkungen zu aktivieren, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und wählen Sie entweder **Nur Google Single Sign-on-Anmeldung erzwingen** oder **Nur benutzerdefinierte SAML Single Sign-on-Anmeldung erzwingen** aus.

![Beispielkonfiguration des Abschnitts „Authentifizierungsregeln“ mit einer Mindestpasswortlänge von 8 Zeichen und einer Passwort-Wiederverwendbarkeit von 3 Mal. Die Passwörter laufen nach 180 Tagen ab, und Nutzer:innen werden nach 1.440 Minuten Inaktivität abgemeldet.]({% image_buster /assets/img/sso3.png %})

Wenn Sie Einschränkungen aktivieren, können sich die Braze-Nutzer:innen Ihres Unternehmens nicht mehr mit einem Passwort anmelden, selbst wenn sie sich zuvor mit einem Passwort angemeldet haben.

{% alert important %}
Nachdem Single Sign-on erzwungen wurde, gibt es keine Fallback-Option für die Anmeldung, wenn die Single Sign-on-Authentifizierung fehlschlägt. Stellen Sie vor der Aktivierung der Single Sign-on-Erzwingung sicher, dass Ihre Single Sign-on-Konfiguration korrekt ist, alle Zertifikate aktuell und erneuert sind und Ihre Sicherheitseinstellungen ordnungsgemäß verwaltet werden, um Anmeldeprobleme zu vermeiden.
{% endalert %}

## SAML-Trace abrufen {#obtaining-a-saml-trace}

Wenn Sie bei der Anmeldung Probleme im Zusammenhang mit Single Sign-on feststellen, kann das Abrufen eines SAML-Traces Ihnen bei der Fehlerbehebung Ihrer Single Sign-on-Verbindung helfen, indem identifiziert wird, was in den SAML-Anfragen gesendet wird.

### Voraussetzungen {#prerequisites}

Um einen SAML-Trace auszuführen, benötigen Sie einen SAML-Tracer. Hier sind zwei mögliche Optionen je nach Ihrem Browser:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Schritt 1: SAML-Tracer öffnen {#step-1-open-the-saml-tracer}

Wählen Sie den SAML-Tracer in der Navigationsleiste Ihres Browsers aus. Stellen Sie sicher, dass **Pause** nicht ausgewählt ist, da dies verhindert, dass der SAML-Tracer erfasst, was in den SAML-Anfragen gesendet wird. Wenn der SAML-Tracer geöffnet ist, sehen Sie, wie er den Trace füllt.

![SAML-Tracer für Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Schritt 2: Mit Single Sign-on bei Braze anmelden {#step-2-sign-into-braze-using-sso}

Gehen Sie zu Ihrem Braze-Dashboard und versuchen Sie, sich mit Single Sign-on anzumelden. Wenn ein Fehler auftritt, öffnen Sie den SAML-Tracer und versuchen Sie es erneut. Ein SAML-Trace wurde erfolgreich erfasst, wenn eine Zeile mit einer URL wie `https://dashboard-XX.braze.com/auth/saml/callback` und einem orangefarbenen SAML-Tag vorhanden ist.

### Schritt 3: Exportieren und an Braze senden {#step-3-export-and-send-to-braze}

Wählen Sie **Export**. Wählen Sie unter **Select Cookie-filter profile** die Option **None** aus. Wählen Sie dann **Export**. Dadurch wird eine JSON-Datei generiert, die Sie zur weiteren Fehlerbehebung an den Braze-Support senden können.

![Menü „Export SAML-trace preferences“ mit ausgewählter Option „None“.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Fehlerbehebung {#troubleshooting}

### Ist die E-Mail-Adresse der Nutzer:in korrekt eingerichtet? {#is-the-users-email-address-correctly-set-up}

Wenn Sie den Fehler `ERROR_CODE_SSO_INVALID_EMAIL` erhalten, ist die E-Mail-Adresse der Nutzer:in ungültig. Überprüfen Sie im SAML-Trace, ob das Feld `saml2:Attribute Name="email"` mit der E-Mail-Adresse übereinstimmt, die die Nutzer:in zur Anmeldung verwendet. Wenn Sie Microsoft Entra ID (ehemals Azure Active Directory) verwenden, lautet die Attribut-Abbildung `email = user.userprincipalname`.

Die E-Mail-Adresse unterscheidet zwischen Groß- und Kleinschreibung und muss exakt mit der in Braze eingerichteten Adresse übereinstimmen, einschließlich der in Ihrem Identitätsanbieter (z. B. Okta, OneLogin, Microsoft Entra ID und andere) konfigurierten Adresse.

Weitere Fehler, die auf Probleme mit der E-Mail-Adresse der Nutzer:in hinweisen, sind unter anderem:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: Die E-Mail-Adresse der Nutzer:in ist nicht im Dashboard vorhanden.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: Die E-Mail-Adresse der Nutzer:in ist leer oder anderweitig falsch konfiguriert.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` oder `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: Die E-Mail-Adresse der Nutzer:in stimmt nicht mit der für die Single Sign-on-Einrichtung verwendeten Adresse überein.

### Haben Sie ein gültiges SAML-Zertifikat (x.509-Zertifikat)? {#do-you-have-a-valid-saml-certificate-x509-certificate}

Sie können Ihr SAML-Zertifikat mit [diesem SAML-Validierungstool](https://www.samltool.com/validate_response.php) überprüfen. Beachten Sie, dass ein abgelaufenes SAML-Zertifikat ebenfalls ein ungültiges SAML-Zertifikat ist.

### Haben Sie ein korrektes SAML-Zertifikat (x.509-Zertifikat) hochgeladen? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

Überprüfen Sie, ob das Zertifikat im Abschnitt `ds:X509Certificate` des SAML-Trace mit dem in Braze hochgeladenen Zertifikat übereinstimmt. Dies schließt den Header `-----BEGIN CERTIFICATE-----` und den Footer `-----END CERTIFICATE-----` nicht ein.

### Haben Sie Ihr SAML-Zertifikat (x.509-Zertifikat) falsch eingegeben oder falsch formatiert? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Stellen Sie sicher, dass im Zertifikat, das Sie im Braze-Dashboard eingereicht haben, keine Leerzeichen oder zusätzlichen Zeichen enthalten sind.

Wenn Sie Ihr Zertifikat in Braze eingeben, muss es PEM-kodiert (Privacy Enhanced Mail) und korrekt formatiert sein (einschließlich des Headers `-----BEGIN CERTIFICATE-----` und des Footers `-----END CERTIFICATE-----`).

Hier ist ein Beispiel für ein korrekt formatiertes Zertifikat:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### Ist das Sitzungs-Token / Textbaustein der Nutzer:in gültig? {#is-the-users-session-token-valid}

Lassen Sie die betroffene Nutzer:in [den Cache und die Cookies ihres Browsers löschen](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) und versuchen Sie dann erneut, sich mit SAML Single Sign-on anzumelden.

### Haben Sie Ihren RelayState eingerichtet? {#did-you-set-your-relaystate}

Wenn Sie den Fehler `ERROR_CODE_SSO_INVALID_RELAY_STATE` erhalten, ist Ihr RelayState möglicherweise falsch konfiguriert oder nicht vorhanden. Falls noch nicht geschehen, müssen Sie Ihren RelayState in Ihrem IdP-Verwaltungssystem einrichten. Weitere Informationen finden Sie unter [Ihren RelayState einrichten](#setting-up-your-relaystate).

### Werden Sie nach erfolgreicher Single Sign-on-Anmeldung zur Braze-Anmeldeseite zurückgeleitet? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

Dies kann auftreten, wenn der RelayState nicht korrekt konfiguriert ist. Vergewissern Sie sich, dass Sie einen API-Schlüssel (unter **Einstellungen** > **Einrichtung und Tests** > **APIs und Bezeichner**) für die IdP-Anmeldung erstellt und diesen API-Schlüssel als `RelayState`-Parameter in Ihrem IdP festgelegt haben. Der RelayState identifiziert, bei welchem Unternehmenskonto Sie sich anmelden. Eine schrittweise Anleitung finden Sie unter [Ihren RelayState einrichten](#setting-up-your-relaystate).

Wenn Sie sich weiterhin nicht anmelden können, [kontaktieren Sie den Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) und fügen Sie nach Möglichkeit einen SAML-Trace bei. Hilfe bei der Aufzeichnung eines Trace finden Sie unter [Einen SAML-Trace aufzeichnen](#obtaining-a-saml-trace).

### Steckt die Nutzer:in in einer Anmeldeschleife zwischen Okta und Braze fest? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

Wenn sich eine Nutzer:in nicht anmelden kann, weil sie zwischen Okta-Single Sign-on und dem Braze-Dashboard in einer Schleife feststeckt, müssen Sie in Okta die Single Sign-on-URL-Zieladresse auf Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) setzen (z. B. `https://dashboard-07.braze.com`).

Wenn Sie einen anderen IdP verwenden, prüfen Sie, ob Ihr Unternehmen das korrekte SAML- oder x.509-Zertifikat in Braze hochgeladen hat.

### Verwenden Sie eine manuelle Integration? {#are-you-using-a-manual-integration}

Wenn Ihr Unternehmen die Braze-App nicht aus dem App-Store Ihres IdP heruntergeladen hat, müssen Sie die vorgefertigte Integration herunterladen. Wenn beispielsweise Okta Ihr IdP ist, würden Sie die Braze-App von deren [Integrationsseite](https://www.okta.com/integrations/braze/) herunterladen.

## Google Single Sign-on

Wenn Ihr Unternehmen Google Single Sign-on anstelle von benutzerdefiniertem SAML verwendet, kontaktieren Sie Ihren Braze Account Manager:in, um Google Single Sign-on für Ihren Workspace zu aktivieren. Nach der Aktivierung gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und wählen Sie **Nur Google Single Sign-on-Anmeldung erzwingen**, um die Google-Authentifizierung für alle Unternehmensnutzer:innen verpflichtend zu machen.

Wenn die Google Single Sign-on-Erzwingung aktiviert ist, müssen sich Nutzer:innen mit der Google-Authentifizierung anmelden und können kein Braze-Passwort mehr verwenden. Jede Nutzerin und jeder Nutzer muss sich mit dem Google-Konto anmelden, das mit der E-Mail-Adresse ihres bzw. seines Braze-Dashboards übereinstimmt. Wenn eine Nutzerin oder ein Nutzer bei der Anmeldung ein anderes Google-Konto auswählt, lehnt Braze den Authentifizierungsversuch ab.

### Fehlerbehebung bei der Google Single Sign-on-Anmeldung {#troubleshooting-google-sso-sign-in}

Wenn sich einige Nutzer:innen nicht mit Google Single Sign-on anmelden können, überprüfen Sie Folgendes:

- Die E-Mail-Adresse des Google-Kontos der Nutzerin oder des Nutzers stimmt exakt mit der E-Mail-Adresse im Braze-Dashboard überein.
- Die Nutzerin oder der Nutzer hat Zugriff auf ein Google-Konto für die E-Mail-Adresse des Unternehmens.
- Die Nutzerin oder der Nutzer ist in Braze nicht gesperrt (**Einstellungen** > **Unternehmensnutzer:innen**).

## Nächste Schritte {#next-steps}

Nach der Einrichtung von SAML Single Sign-on können Sie:

- [Ausschließliche Single Sign-on-Anmeldung erzwingen]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication) in Ihren Sicherheitseinstellungen, um Nutzer:innen daran zu hindern, sich mit einem Passwort anzumelden.
- [SAML Just-in-Time-Bereitstellung einrichten]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning), damit neue Nutzer:innen bei ihrer ersten Single Sign-on-Anmeldung automatisch ein Braze-Konto erstellen.