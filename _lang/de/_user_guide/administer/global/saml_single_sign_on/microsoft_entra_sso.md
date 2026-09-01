---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 2
page_type: tutorial
description: "Dieser Artikel führt Sie durch die Einrichtung der Microsoft Entra Single Sign-on-Funktionen mit Braze."

---

# Microsoft Entra SSO {#microsoft-entra-sso}

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) ist der cloudbasierte Identitäts- und Zugriffsverwaltungsdienst von Microsoft, der Ihren Mitarbeitenden hilft, sich anzumelden und auf Ressourcen zuzugreifen. Sie können Entra SSO verwenden, um den Zugriff auf Ihre Apps und Ihre App-Ressourcen basierend auf Ihren Geschäftsanforderungen zu steuern.

## Anforderungen {#requirements}

Bei der Einrichtung werden Sie aufgefordert, eine Assertion Consumer Service (ACS)-URL anzugeben.

| Anforderung | Details |
|---|---|
| Assertion Consumer Service (ACS)-URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Bei einigen Identitätsanbietern wird diese auch als Antwort-URL, Zielgruppen-URL oder Zielgruppen-URI bezeichnet. |
| Entity-ID | Standardmäßig `braze_dashboard`. <br><br> Um diesem Dashboard eine eindeutige Entity-ID zuzuweisen, aktivieren Sie eine angepasste Entity-ID und verwenden Sie den generierten Wert (`braze_dashboard_<COMPANY_ID>`). Die Schritte finden Sie unter [Angepasste Entity-ID verwenden]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id). |
| RelayState-API-Schlüssel | Um die Anmeldung über den Identitätsanbieter zu aktivieren, gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Vom Service Provider (SP) initiierte Anmeldung mit Microsoft Entra SSO {#service-provider-sp-initiated-login-within-microsoft-entra-sso}

### Schritt 1: Braze aus dem Katalog hinzufügen {#step-1-add-braze-from-the-gallery}

1. Navigieren Sie in Ihrem Microsoft Entra Admin Center zu **Identity** > **Applications** > **Enterprise Applications** und wählen Sie dann **New application** aus.
2. Suchen Sie im Suchfeld nach **Braze**, wählen Sie es im Ergebnisbereich aus und wählen Sie dann **Add** aus.

### Schritt 2: Microsoft Entra SSO konfigurieren {#step-2-configure-microsoft-entra-sso}

1. Navigieren Sie in Ihrem Microsoft Entra Admin Center zur Braze-Anwendungsintegrationsseite und wählen Sie **Single sign-on** aus.
2. Wählen Sie auf der Seite **Select a single sign-on method** die Option **SAML** als Ihre Methode aus.
3. Wählen Sie auf der Seite **Set up Single Sign-On with SAML** das Bearbeitungssymbol für **Basic SAML Configuration** aus.
4. Konfigurieren Sie die Anwendung im IdP-initiierten Modus, indem Sie eine **Reply URL** eingeben, die Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) mit dem folgenden Muster kombiniert: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Lassen Sie im selben Abschnitt **Basic SAML Configuration** den **Identifier (Entity ID)** auf `braze_dashboard` eingestellt, es sei denn, Sie verwenden eine [angepasste Entity ID]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id). Geben Sie in diesem Fall den von Ihrem Dashboard generierten Wert (`braze_dashboard_<COMPANY_ID>`) ein, damit er mit dem in Ihren Braze-Sicherheitseinstellungen angezeigten Wert übereinstimmt.
6. Konfigurieren Sie den RelayState, indem Sie Ihren generierten Relay-State-API-Schlüssel in das Feld **Relay State** eingeben.

{% alert important %}
Füllen Sie das Feld **Sign-On URL** **nicht** aus. Lassen Sie dieses Feld leer, um Probleme mit Ihrem IdP-initiierten SAML SSO zu vermeiden.
{% endalert %}

{: start="7"}
7. Formatieren Sie SAML-Assertions in dem spezifischen Format, das Braze erwartet. In den folgenden Tabs zu Nutzerattributen und Nutzer:innen-Claims erfahren Sie, wie diese Attribute und Werte formatiert sein müssen.

{% tabs %}
{% tab Nutzerattribute %}
Sie können die Werte dieser Attribute im Abschnitt **User Attributes** auf der Seite **Application Integration** verwalten.

Verwenden Sie die folgenden Attributzuordnungen:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
Das E-Mail-Feld muss mit dem übereinstimmen, was für Ihre Nutzer:innen in Braze eingerichtet ist. In den meisten Fällen ist dies dasselbe wie `user.userprincipalname`. Wenn Sie jedoch eine andere Konfiguration haben, arbeiten Sie mit Ihrem Systemadministrator zusammen, um sicherzustellen, dass diese Felder exakt übereinstimmen.
{% endalert %}

{% endtab %}
{% tab Nutzer:innen-Claims %}

Wählen Sie auf der Seite **Set up Single Sign-On with SAML** die Option **Edit** aus, um das Dialogfeld **User Attributes** zu öffnen. Bearbeiten Sie dann die Nutzer:innen-Claims gemäß dem richtigen Format.

Verwenden Sie die folgenden Claim-Namenszuordnungen:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
Das E-Mail-Feld muss mit dem übereinstimmen, was für Ihre Nutzer:innen in Braze eingerichtet ist. In den meisten Fällen ist dies dasselbe wie `user.userprincipalname`. Wenn Sie jedoch eine andere Konfiguration haben, arbeiten Sie mit Ihrem Systemadministrator zusammen, um sicherzustellen, dass diese Felder exakt übereinstimmen.
{% endalert %}

Sie können diese Nutzer:innen-Claims und -Werte im Abschnitt **Manage claim** verwalten.

{% endtab %}
{% endtabs %}

{: start="8"}
8. Navigieren Sie zur Seite **Set up Single Sign-On with SAML**, scrollen Sie dann zum Abschnitt **SAML Signing Certificate** und laden Sie das entsprechende **Certificate (Base64)** basierend auf Ihren Anforderungen herunter.
9. Navigieren Sie zum Abschnitt **Set up Braze** und kopieren Sie die entsprechenden URLs zur Verwendung in der [Braze-Konfiguration](#step-3).

### Schritt 3: Microsoft Entra SSO in Braze konfigurieren {#step-3}

Nachdem Sie Braze im Microsoft Entra Admin Center eingerichtet haben, stellt Microsoft Entra eine Ziel-URL (Anmelde-URL) und ein **x.509**-Zertifikat bereit, die Sie in Ihr Braze-Konto eingeben.

Nachdem Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie wie folgt vor:

1. Navigieren Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**.
2. Fügen Sie auf derselben Seite Folgendes hinzu:

| Anforderung | Details |
|---|---|
| `SAML Name` | Dies wird als Button-Text auf dem Anmeldebildschirm angezeigt. Dies ist in der Regel der Name Ihres Identitätsanbieters, z. B. „Microsoft Entra“. |
| `Target URL` | Dies ist die von Microsoft Entra bereitgestellte Anmelde-URL. |
| `Certificate` | Das `x.509`-PEM-kodierte Zertifikat wird von Ihrem Identitätsanbieter bereitgestellt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Microsoft Entra SSO in Braze konfigurieren" }

{% alert tip %}
Wenn Sie möchten, dass sich Ihre Braze-Kontonutzer:innen ausschließlich mit SAML SSO anmelden, können Sie die [Single-Sign-on-Authentifizierung einschränken]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) auf der Seite **Sicherheitseinstellungen** unter **Authentifizierungsregeln**.
{% endalert %}