---
nav_title: OneLogin
article_title: OneLogin
page_order: 4
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie Braze für die Verwendung von Single Sign-on mit OneLogin konfigurieren."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) ist eine Cloud-Identitätsplattform für die umfassende Verwaltung von Nutzer:innen-Identitäten. OneLogin lässt sich per SAML 2.0 in Cloud- und On-Premise-Anwendungen integrieren – für Single Sign-On (SSO), Nutzer:innen-Bereitstellung, mehrstufige Authentifizierung und vieles mehr.

## Anforderungen {#requirements}

Bei der Einrichtung werden Sie aufgefordert, eine Anmelde-URL und eine Assertion Consumer Service (ACS)-URL anzugeben.

| Anforderung | Details |
|---|---|
| Assertion Consumer Service (ACS)-URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Für Domains in der Europäischen Union lautet die ACS-URL `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. |
| Entity-ID | Standardmäßig `braze_dashboard`. Wenn Ihr IdP eine unternehmensspezifische Entity-ID erfordert, aktivieren Sie **Benutzerdefinierte Entity-ID** unter **Sicherheitseinstellungen** und verwenden Sie `braze_dashboard_<companyID>`. |
| Braze-Domain | Sie benötigen Ihre Braze-Domain, um Braze innerhalb von OneLogin einzurichten. Wenn Ihre Instanz `US-01` ist, müssen Sie Ihre Dashboard-URL im OneLogin-Dashboard eingeben. <br><br> Wenn Ihre Dashboard-URL beispielsweise `https://dashboard-01.braze.com` lautet, müssen Sie `dashboard-01.braze.com` eingeben.  |
| RelayState-API-Schlüssel | Um die IdP-Anmeldung zu aktivieren, navigieren Sie zu **Einstellungen** > **Einrichtung und Test** > **APIs und Bezeichner**, öffnen Sie den Tab **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login`-Berechtigungen. Die entsprechenden Schritte finden Sie unter [Einrichten Ihres RelayState]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## IdP-initiierte Anmeldung bei OneLogin {#idp-initiated-login-within-onelogin}

### Schritt 1: Die Braze-App konfigurieren {#step-1-configure-the-braze-app}

1. Melden Sie sich bei [OneLogin](https://app.onelogin.com/login) an. Klicken Sie auf **Administration**.![OneLogin-Administrationsseite.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Gehen Sie in der oberen Navigationsleiste zu **Apps** > **Add Apps**. Suchen Sie nach „Braze“ und wählen Sie die Braze-App aus.![Suchergebnisse für Braze in OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Speichern Sie die Braze-App in Ihrem Unternehmen.![Suchergebnisse für Braze in OneLogin.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Gehen Sie nach dem Speichern zu **Configuration** und fügen Sie Ihre **Braze Domain** und den **RelayState**-API-Schlüssel hinzu. Falls Ihr IdP eine unternehmensspezifische Entity-ID erfordert, konfigurieren Sie außerdem die **ACS URL** (`https://<SUBDOMAIN>.braze.com/auth/saml/callback`) und die Entity-ID aus der [SAML-SSO-Einrichtung]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements).![OneLogin-Konfigurationstab für die Braze-App.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze erwartet die SAML-Assertions in einem [bestimmten Format]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#step-1-configure-your-identity-provider). Unter **Parameters** sollten die von Braze unterstützten Attribute bereits vorausgefüllt sein. Überprüfen Sie, ob sie korrekt sind.![Braze-SAML-Parameter in OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Kopieren Sie das **Certificate** und den **SAML 2.0 Endpoint (HTTP)**, die zum Einrichten des Braze-Dashboards benötigt werden, aus dem **SSO**-Tab.![Zertifikate, die aus dem SSO-Tab der Braze-App in OneLogin kopiert werden.]({% image_buster /assets/img/onelogin_6.jpg %})

### Schritt 2: OneLogin in Braze konfigurieren {#step-2-configure-onelogin-within-braze}

Nachdem Sie Braze in Ihrem OneLogin eingerichtet haben, erhalten Sie eine Ziel-URL (`SAML 2.0 Endpoint (HTTP)`) und ein `x.509`-Zertifikat, die Sie in Ihrem Braze-Konto eingeben müssen.

Nachdem Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und schalten Sie den Bereich SAML SSO auf **EIN**.

Geben Sie auf dieser Seite Folgendes ein:

| Anforderung | Details |
|---|---|
| `SAML Name` | Dieser Name wird als Button-Text auf dem Anmeldebildschirm angezeigt. In der Regel ist dies der Name Ihres Identity Providers, z. B. „OneLogin“. |
| `Target URL` | Dies ist die von OneLogin bereitgestellte `SAML 2.0 Endpoint (HTTP)`-URL. |
| `Certificate` | Das PEM-kodierte `x.509`-Zertifikat wird von Ihrem OneLogin bereitgestellt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: OneLogin in Braze konfigurieren" }

Falls Ihr IdP eine unternehmensspezifische Entity-ID erfordert, aktivieren Sie **Custom Entity ID** in den **Sicherheitseinstellungen**, kopieren Sie den generierten Wert und fügen Sie ihn in das Entity-ID-Feld von OneLogin ein. Weitere Informationen finden Sie unter [Benutzerdefinierte Entity-ID]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#custom-entity-id) im Artikel zur SAML-SSO-Einrichtung.

![SAML-SSO-Einstellungen mit aktiviertem Umschalter.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Wenn Sie möchten, dass sich Nutzer:innen Ihres Braze-Kontos ausschließlich über SAML SSO anmelden, können Sie die [Single-Sign-on-Authentifizierung einschränken]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) unter **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen**.
{% endalert %}

## Nächste Schritte {#next-steps}

Nachdem OneLogin SSO funktioniert:

- [SAML SSO-only-Anmeldung erzwingen]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction), wenn die Passwort-Anmeldung deaktiviert werden soll.
- [SAML Just-in-Time-Bereitstellung einrichten]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning), um Dashboard-Nutzer:innen bei der ersten IdP-Anmeldung automatisch zu erstellen.
- [Einen SAML-Trace abrufen]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#obtaining-a-saml-trace), wenn Nutzer:innen Anmeldefehler haben.