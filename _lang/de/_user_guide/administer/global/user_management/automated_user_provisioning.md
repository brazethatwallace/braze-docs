---
nav_title: "Automatisierte Bereitstellung von Nutzer:innen"
article_title: "Automatisierte Bereitstellung von Nutzer:innen"
page_order: 3
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, welche Informationen Sie für die automatisierte Bereitstellung von Nutzer:innen bereitstellen müssen und wie und wo Sie Ihr generiertes System for Cross-domain Identity Management (SCIM) Token verwenden."
alias: /scim/automated_user_provisioning/

---

# Automatisierte Bereitstellung von Nutzer:innen {#automated-user-provisioning}

> Die automatisierte Bereitstellung von Nutzer:innen ermöglicht es Ihnen, Braze-Nutzer:innen über eine API zu erstellen und zu verwalten, anstatt dies manuell im Dashboard zu tun. Braze unterstützt dies über das System for Cross-domain Identity Management (SCIM). In diesem Artikel erfahren Sie, welche Informationen Sie angeben müssen, wie Sie Ihr SCIM-Token generieren und wo Sie Ihren SCIM-API-Endpunkt finden.

## Zugriff auf die SCIM-Bereitstellungseinstellungen {#accessing-scim-provisioning-settings}

1. Navigieren Sie im Braze-Dashboard zu **Einstellungen** > **Admin-Einstellungen** > **SCIM-Bereitstellung** und wählen Sie anschließend **SCIM-Integration konfigurieren**.
2. Wählen Sie im Schritt **Braze-Konfiguration** eine Bereitstellungsmethode aus und geben Sie die Zugriffseinstellungen an.

![Eine Seite zur Einrichtung der SCIM-Integration mit Abschnitten zur Auswahl einer Bereitstellungsmethode und zur Angabe von Zugriffseinstellungen.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. Befolgen Sie im Schritt **IdP-Konfiguration** die Anweisungen innerhalb der Plattform für die von Ihnen ausgewählte Bereitstellungsmethode.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Verwenden Sie die Option **Okta – Braze-App**, wenn Sie die Braze-App für SAML SSO in Okta eingerichtet haben. Wenn Sie eine benutzerdefinierte App für SSO eingerichtet haben, folgen Sie den Anweisungen im Tab [Okta – Benutzerdefinierte App-Integration]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

## 1. Schritt: SCIM-Bereitstellung einrichten {#step-1-set-up-scim-provisioning}

### Schritt 1.1: SCIM aktivieren {#step-11-enable-scim}

1. Navigieren Sie in Okta zu **Applications** > **Applications** und wählen Sie dann **Create App Integration**. Wählen Sie **SAML 2.0** als Anmeldemethode.
2. Füllen Sie die folgenden Details aus (die sich im [Schritt **IdP-Konfiguration**](#accessing-scim-provisioning-settings) von Braze befinden), um eine benutzerdefinierte App zu erstellen:
- App-Logo
- Single Sign-on URL
- Audience URL (SP Entity ID)
3. Wählen Sie **Finish**.
4. Wählen Sie den Tab **General**.
5. Wählen Sie im Abschnitt **App Settings** die Option **Edit**.
6. Wählen Sie im Feld **Provisioning** die Option **SCIM**.

### Schritt 1.2: Anwendungssichtbarkeit deaktivieren {#step-12-disable-application-visibility}

1. Aktivieren Sie im Feld **Application visibility** das Kontrollkästchen **Do not display application icon to user**. Dadurch wird verhindert, dass Nutzer:innen über die App auf SSO zugreifen, da diese ausschließlich für SCIM vorgesehen ist.
2. Wählen Sie **Save**.

### Schritt 1.3: SCIM-Integration einrichten {#step-13-set-up-the-scim-integration}

1. Wählen Sie den Tab **Provisioning**.
2. Navigieren Sie unter **Settings** > **Integration** > **SCIM Connection** zu **Edit** und füllen Sie die Feldwerte aus, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

### Schritt 1.4: API-Zugangsdaten testen {#step-14-test-the-api-credentials}

Wählen Sie **Test API Credentials**. Bei erfolgreicher Integration wird eine Bestätigungsmeldung angezeigt und Sie können speichern.

### Schritt 1.5: Bereitstellung für die App aktivieren {#step-15-enable-provisioning-to-the-app}

1. Navigieren Sie unter **Provisioning** > **Settings** > **To App** > **Provisioning to App** zu **Edit**.
2. Aktivieren Sie Folgendes:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping** mit den Zuordnungen, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

## 2. Schritt: Nutzer:innen der App zuweisen {#step-2-assign-users-to-the-app}

1. Wählen Sie den Tab **Assignment**.
2. Wählen Sie **Assign** und wählen Sie eine Option.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Wählen Sie **Done**, wenn Sie die Zuweisung abgeschlossen haben.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Verwenden Sie die Option **Okta – Benutzerdefinierte App-Integration**, wenn Sie eine benutzerdefinierte App für SSO eingerichtet haben. Wenn Sie die Braze-App für SAML SSO in Okta eingerichtet haben, folgen Sie den Anweisungen im Tab [Okta – Braze-App]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

## 1. Schritt: SCIM-Bereitstellung einrichten

### Schritt 1.1: SCIM aktivieren

1. Navigieren Sie in Okta zu Ihrer Braze-App.
2. Wählen Sie den Tab **General**.
3. Wählen Sie im Abschnitt **App Settings** die Option **Edit**.
4. Wählen Sie im Feld **Provisioning** die Option **SCIM**.
5. Wählen Sie **Save**.

### Schritt 1.2: SCIM-Integration einrichten {#step-12-set-up-scim-integration}

1. Wählen Sie den Tab **Provisioning**.
2. Navigieren Sie unter **Settings** > **Integration** > **SCIM Connection** zu **Edit** und füllen Sie die Feldwerte aus, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.
3. Testen Sie die API-Zugangsdaten, indem Sie **Test API Credentials** auswählen.
4. Wählen Sie **Save**.

### Schritt 1.3: Bereitstellung für die App aktivieren {#step-13-enable-provisioning-to-the-app}

1. Navigieren Sie unter **Provisioning** > **Settings** > **To App** > **Provisioning to App** zu **Edit**.
2. Aktivieren Sie Folgendes:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping** mit den Zuordnungen, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

## 2. Schritt: Nutzer:innen der App zuweisen

1. Wählen Sie den Tab **Assignment**.
2. Wählen Sie **Assign** und wählen Sie eine Option.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Wählen Sie **Done**.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Entra ID integration' %}

## 1. Schritt: SCIM-Bereitstellungs-App einrichten {#step-1-set-up-scim-provisioning-app}

### Schritt 1.1: Beim Microsoft Entra Admin Center anmelden {#step-11-log-into-microsoft-entra-admin-center}

Melden Sie sich bei Ihrem Microsoft Entra Admin Center an.

### Schritt 1.2: SCIM-App erstellen und einrichten {#step-12-create-and-set-up-your-scim-app}

1. Navigieren Sie im Navigationsmenü zu **Entra ID** > **Enterprise apps**.
2. Wählen Sie **New application**.
3. Wählen Sie **Create your own application**.
4. Geben Sie im Panel einen Namen für Ihre App ein.
5. Wählen Sie im Abschnitt **What are you looking to do with your application?** die Option **Integrate application you don't find in the gallery (Non-gallery)**.
6. Wählen Sie **Create**.

### Schritt 1.3: SCIM-Integration einrichten {#step-13-set-up-scim-integration}

1. Navigieren Sie zum Abschnitt **Manage** > **Provisioning** Ihrer SCIM-Anwendung.
2. Wählen Sie **Connect your application** oder **New configuration** und füllen Sie die Feldwerte aus, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

### Schritt 1.4: Bereitstellung für die App aktivieren {#step-14-enable-provisioning-to-the-app}

1. Navigieren Sie zum Abschnitt **Manage** > **Attribute mapping (Preview)** Ihrer SCIM-Anwendung.
2. Wählen Sie **Provision Microsoft Entra ID Users**.
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping**, damit er mit den Attributen übereinstimmt, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.
4. Schließen Sie die Seite **Attribute Mapping**.

## 2. Schritt: Nutzer:innen der App zuweisen

1. Navigieren Sie zu **Manage** > **Users and Groups**.
2. Wählen Sie **Add user/group**.
3. Wählen Sie **None Selected**, um Nutzer:innen der App zuzuweisen.
4. Wählen Sie den Button **Select**, um die Zuweisung zu bestätigen.

{% endtab %}
{% tab Custom %}

## 1. Schritt: SCIM-Einstellungen konfigurieren {#step-1-configure-your-scim-settings}

- **Standard-Workspace:** Wählen Sie den Workspace aus, dem neue Nutzer:innen standardmäßig hinzugefügt werden sollen. Wenn Sie in Ihrer [SCIM-API-Anfrage]({{site.baseurl}}/post_create_user_account) keinen Workspace angeben, weist Braze Nutzer:innen diesem Workspace zu.
- **Dienst-Herkunft:** Geben Sie die Herkunfts-Domain Ihrer SCIM-Anfragen ein. Braze verwendet diese im `X-Request-Origin`-Header, um zu überprüfen, woher die Anfragen stammen.
- **IP-Zulassungsliste (optional):** Sie können SCIM-Anfragen auf bestimmte IP-Adressen beschränken. Geben Sie eine kommagetrennte Liste oder einen Bereich von IP-Adressen ein, die zugelassen werden sollen. Der `X-Request-Origin`-Header in jeder Anfrage wird verwendet, um die IP-Adresse der Anfrage mit der Zulassungsliste abzugleichen.

## 2. Schritt: SCIM-Token generieren {#step-2-generate-a-scim-token}

Nachdem Sie die erforderlichen Felder ausgefüllt haben, klicken Sie auf **SCIM-Token generieren**, um ein SCIM-Token zu generieren und Ihren SCIM-API-Endpunkt anzuzeigen. Stellen Sie sicher, dass Sie das SCIM-Token kopieren, bevor Sie die Seite verlassen. **Dieses Token wird nur einmal angezeigt.**

![SCIM-API-Endpunkt- und SCIM-Token-Felder mit maskierten Werten und Kopier-Buttons. Unterhalb des Token-Feldes befindet sich ein Button „Token zurücksetzen“.]({% image_buster /assets/img/scim.png %})

Braze erwartet, dass alle SCIM-Anfragen das SCIM-API-Bearer-Token enthalten, das über einen HTTP-`Authorization`-Header angehängt wird.

{% endtab %}
{% endtabs %}