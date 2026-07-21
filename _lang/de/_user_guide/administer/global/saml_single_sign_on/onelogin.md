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

Bei der Einrichtung werden Sie aufgefordert, eine Anmelde-URL und eine ACS-URL (Assertion Consumer Service) anzugeben.

| Anforderung | Details |
|---|---|
| Braze-Domain | Sie benötigen Ihre Braze-Domain, um Braze in OneLogin einzurichten. Wenn Ihre Instanz `US-01` ist, müssen Sie Ihre Dashboard-URL in das Dashboard von OneLogin eingeben. <br><br> Wenn Ihre Dashboard-URL z. B. `https://dashboard-01.braze.com` lautet, geben Sie `dashboard-01.braze.com` ein.  |
| RelayState-API-Schlüssel | Um die IdP-Anmeldung zu aktivieren, gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## IdP-initiierte Anmeldung bei OneLogin {#idp-initiated-login-within-onelogin}

### Schritt 1: Konfigurieren Sie die Braze-App {#step-1-configure-the-braze-app}

1. Melden Sie sich bei [OneLogin](https://app.onelogin.com/login) an. Klicken Sie auf **Administration**.![OneLogin-Verwaltungsseite.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Gehen Sie zu **Apps** > **Add Apps** in der oberen Navigationsleiste. Suchen Sie nach „Braze“ und wählen Sie die Braze-App aus.![Suchergebnisse für Braze in OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Speichern Sie die Braze-App in Ihrem Unternehmen.![Speichern der Braze-App im Unternehmen in OneLogin.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Gehen Sie nach dem Speichern zu **Configuration** und fügen Sie Ihre **Braze Domain** und den **RelayState**-API-Schlüssel hinzu.![OneLogin-Konfigurationsreiter für die Braze-App.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze erwartet die SAML-Assertions in einem [bestimmten Format]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#step-1-configure-your-identity-provider). Unter **Parameters** sollten die von Braze unterstützten Attribute bereits vorausgefüllt sein. Überprüfen Sie, ob sie korrekt sind.![Braze-SAML-Parameter in OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Kopieren Sie das **Certificate** und den **SAML 2.0 Endpoint (HTTP)**, die für die Einrichtung des Braze-Dashboards benötigt werden, aus dem **SSO**-Tab.![Zertifikate zum Kopieren aus dem SSO-Tab der Braze-App in OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Schritt 2: OneLogin in Braze konfigurieren {#step-2-configure-onelogin-within-braze}

Nachdem Sie Braze in OneLogin eingerichtet haben, erhalten Sie eine Ziel-URL (`SAML 2.0 Endpoint (HTTP)`) und ein `x.509`-Zertifikat, die Sie in Ihrem Braze-Konto eingeben.

Nachdem Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**.

Geben Sie auf dieser Seite Folgendes ein:

| Anforderung | Details |
|---|---|
| `SAML Name` | Dieser Name wird als Button-Text auf dem Anmeldebildschirm angezeigt. In der Regel ist dies der Name Ihres Identitätsanbieters, z. B. „OneLogin“. |
| `Target URL` | Dies ist die `SAML 2.0 Endpoint (HTTP)`-URL, die von OneLogin bereitgestellt wird.|
| `Certificate` | Das PEM-kodierte `x.509`-Zertifikat wird von OneLogin bereitgestellt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: OneLogin in Braze konfigurieren" }

![SAML-SSO-Einstellungen mit aktiviertem Schalter.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Wenn Sie möchten, dass sich Ihre Braze-Kontonutzer:innen ausschließlich über SAML SSO anmelden, können Sie die [Single-Sign-on-Authentifizierung einschränken]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) – über die Seite **Unternehmenseinstellungen**.
{% endalert %}