---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie Braze für die Verwendung von Okta für Single Sign-on konfigurieren."

---

# Okta

> Okta verbindet jede Person mit jeder Anwendung auf jedem Gerät. Es handelt sich um einen Identitätsverwaltungsdienst für Unternehmen, der für die Cloud entwickelt wurde, aber mit vielen lokalen Anwendungen kompatibel ist. Mit Okta kann Ihr IT-Team den Zugriff jeder Mitarbeiterin und jedes Mitarbeiters auf jede Anwendung oder jedes Gerät verwalten.

{% alert note %}
Die vorgefertigte Braze-Okta-Marketplace-App verwendet die gemeinsame Entity-ID `braze_dashboard`. Wenn Sie eine eindeutige Entity-ID für dieses Dashboard benötigen – zum Beispiel, um mehrere Braze-Dashboards über Okta zu verbinden –, richten Sie statt der Marketplace-App eine benutzerdefinierte SAML-App ein und folgen Sie dann der Anleitung unter [Eine benutzerdefinierte Entity-ID verwenden]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id).
{% endalert %}

## Voraussetzungen {#requirements}

| Voraussetzung | Details |
| ----------- | ------- |
| Okta für Ihr Konto aktiviert | Wenden Sie sich an Ihren Braze Account Manager, um dies für Ihr Konto aktivieren zu lassen. |
| Okta-Administratorrechte | Stellen Sie sicher, dass Sie über Administratorrechte verfügen, bevor Sie Okta einrichten. |
| Braze-Administratorrechte | Stellen Sie sicher, dass Sie über Administratorrechte verfügen, bevor Sie Okta einrichten. |
| RelayState-API-Schlüssel | Um die IdP-Anmeldung zu aktivieren, gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Schritt 1: Braze konfigurieren {#step-1-configure-braze}

### Schritt 1a: Zu den Sicherheitseinstellungen in Braze navigieren {#step-1a-navigate-to-security-settings-in-braze}

Nachdem Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**.

![Okta SAML SSO aktiviert auf der Seite „Sicherheitseinstellungen“.]({% image_buster/assets/img/Okta/okta1.png %})

### Schritt 1b: SAML-SSO-Einstellungen bearbeiten {#step-1b-edit-saml-sso-settings}

Über Ihr Okta-Admin-Dashboard stellt Ihnen Okta eine Ziel-URL (Anmelde-URL) und ein `x.509`-Zertifikat zur Verfügung, die Sie auf der Seite **Sicherheitseinstellungen** Ihres Braze-Kontos eingeben müssen.

![Screenshot zu Schritt 1b: SAML-SSO-Einstellungen bearbeiten.]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Anforderung | Details |
|---|---|
| `SAML Name` | Dies wird als Button-Text auf dem Anmeldebildschirm angezeigt. In der Regel ist dies der Name Ihres Identitätsanbieters, zum Beispiel „Okta“. |
| `Target URL` | Dies ist die Anmelde-URL, die über das Okta-Admin-Dashboard bereitgestellt wird. Sie finden sie unter **Applications** > Ihre Anwendung > Tab **General** > **App Embed Link** > **Embed Link**. |
| `Certificate` | Das PEM-codierte `x.509`-Zertifikat wird von Ihrem Identitätsanbieter bereitgestellt. Sie müssen es kopieren und in dieses Feld einfügen. Rufen Sie es in Okta ab, indem Sie zu **SAML Signing Certificates** gehen und **Actions** > **Download certificate** auswählen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1b: SAML-SSO-Einstellungen bearbeiten" }

Wählen Sie unten auf der Seite **Save Changes** aus, wenn Sie fertig sind.

## Schritt 2: Okta konfigurieren {#step-2-configure-okta}

Wählen Sie in Okta den Tab **Sign On** für die Braze-SAML-App aus und klicken Sie dann auf **Edit**.

Geben Sie als Nächstes den RelayState-API-Schlüssel mit der Berechtigung `sso.saml.login` in das Feld **Default Relay State** ein.

![Okta Default RelayState im Tab „Sign On“.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Stellen Sie sicher, dass Sie diese neuen Einstellungen speichern.

{% alert tip %}
Wenn Sie möchten, dass sich Nutzer:innen Ihres Braze-Kontos nur mit SAML SSO anmelden, können Sie die [Single-Sign-on-Authentifizierung einschränken]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction) auf der Seite **Unternehmenseinstellungen**.
{% endalert %}

## Schritt 3: Anmeldung {#step-3-log-in}

Sie sollten sich jetzt mit Okta bei Braze anmelden können!

![Braze-Dashboard-Anmeldung mit aktiviertem Okta SSO.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}