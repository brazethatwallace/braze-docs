---
nav_title: "Automatisierte Bereitstellung von Nutzer:innen"
article_title: "Automatisierte Bereitstellung von Nutzer:innen"
page_order: 3
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, welche Informationen Sie für die automatisierte Bereitstellung von Nutzer:innen bereitstellen müssen und wie und wo Sie Ihr generiertes System for Cross-domain Identity Management (SCIM) Token / Textbaustein verwenden."
alias: /scim/automated_user_provisioning/

---

# Automatisierte Bereitstellung von Nutzer:innen {#automated-user-provisioning}

> Die automatisierte Bereitstellung von Nutzer:innen ermöglicht es Ihnen, Braze-Nutzer:innen über eine API zu erstellen und zu verwalten, anstatt dies manuell im Dashboard zu tun. Braze unterstützt dies über das System for Cross-domain Identity Management (SCIM). In diesem Artikel erfahren Sie, welche Informationen Sie angeben müssen, wie Sie Ihr SCIM-Token / Textbaustein generieren und wo Sie Ihren SCIM-API-Endpunkt finden.

{% multi_lang_include scim/scim_alerts.md alert='one_integration' %}

## Zugriff auf die SCIM-Bereitstellungseinstellungen {#accessing-scim-provisioning-settings}

{% alert important %}
Die Verfügbarkeit der SCIM-Bereitstellung hängt von Ihrer Plattform-Edition ab. Wenn dieses Feature nicht in Ihrem Workspace verfügbar ist, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in für weitere Informationen.
{% endalert %}

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **SCIM-Bereitstellung** und wählen Sie dann **SCIM-Integration konfigurieren** aus.
2. Wählen Sie im Schritt **Braze-Konfiguration** eine Bereitstellungsmethode aus und geben Sie die Zugriffseinstellungen an.

![Eine Seite zum Einrichten der SCIM-Integration mit Abschnitten zur Auswahl einer Bereitstellungsmethode und zur Angabe von Zugriffseinstellungen.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. Folgen Sie im Schritt **IdP-Konfiguration** den Schritten innerhalb der Plattform für Ihre ausgewählte Bereitstellungsmethode.

{% tabs %}
{% tab Okta – Braze-App %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Verwenden Sie die Option **Okta – Braze-App**, wenn Sie die Braze-App für SAML Single Sign-on in Okta eingerichtet haben. Wenn Sie eine benutzerdefinierte App für Single Sign-on eingerichtet haben, folgen Sie den Anweisungen im Tab [Okta – Benutzerdefinierte App-Integration]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Okta' %}

## Schritt 1: SCIM-Bereitstellung einrichten {#step-1-set-up-scim-provisioning}

### Schritt 1.1: SCIM aktivieren {#step-11-enable-scim}

1. Gehen Sie in Okta zu **Applications** > **Applications** und wählen Sie dann **Create App Integration** aus. Wählen Sie **SAML 2.0** als Anmeldemethode.
2. Füllen Sie die folgenden Details aus (die sich im Braze-Schritt [**IdP-Konfiguration**](#accessing-scim-provisioning-settings) befinden), um eine benutzerdefinierte App zu erstellen:
- App-Logo
- Single-Sign-on-URL
- Audience-URL (SP-Entity-ID)
3. Wählen Sie **Finish** aus.
4. Wählen Sie den Tab **General** aus.
5. Wählen Sie im Abschnitt **App Settings** die Option **Edit** aus.
6. Wählen Sie im Feld **Provisioning** die Option **SCIM** aus.

### Schritt 1.2: Anwendungssichtbarkeit deaktivieren {#step-12-disable-application-visibility}

1. Aktivieren Sie im Feld **Application visibility** das Kontrollkästchen **Do not display application icon to user**. Dies verhindert, dass Nutzer:innen über die App auf Single Sign-on zugreifen, da diese ausschließlich für SCIM vorgesehen ist.
2. Wählen Sie **Save** aus.

### Schritt 1.3: SCIM-Integration einrichten {#step-13-set-up-the-scim-integration}

1. Wählen Sie den Tab **Provisioning** aus.
2. Wählen Sie unter **Settings** > **Integration** > **SCIM Connection** die Option **Edit** aus und füllen Sie die Feldwerte aus, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

### Schritt 1.4: API-Zugangsdaten testen {#step-14-test-the-api-credentials}

Wählen Sie **Test API Credentials** aus. Bei erfolgreicher Integration erscheint eine Bestätigungsmeldung und Sie können speichern.

### Schritt 1.5: Bereitstellung für die App aktivieren {#step-15-enable-provisioning-to-the-app}

1. Wählen Sie unter **Provisioning** > **Settings** > **To App** > **Provisioning to App** die Option **Edit** aus.
2. Aktivieren Sie Folgendes:
    - Create Users
    - Update or aktualisieren Users Attributes
    - Deactivate Users
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping** mit den Zuordnungen, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

## Schritt 2: Nutzer:innen der App zuweisen {#step-2-assign-users-to-the-app}

1. Wählen Sie den Tab **Assignment** aus.
2. Wählen Sie **Assign** aus und wählen Sie eine Option.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Wählen Sie **Done** aus, wenn Sie die Zuweisung abgeschlossen haben.

{% endtab %}
{% tab Okta – Benutzerdefinierte App-Integration %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Verwenden Sie die Option **Okta – Benutzerdefinierte App-Integration**, wenn Sie eine benutzerdefinierte App für Single Sign-on eingerichtet haben. Wenn Sie die Braze-App für SAML Single Sign-on in Okta eingerichtet haben, folgen Sie den Anweisungen im Tab [Okta – Braze-App]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Okta' %}

## Schritt 1: SCIM-Bereitstellung einrichten

### Schritt 1.1: SCIM aktivieren

1. Gehen Sie in Okta zu Ihrer Braze-App.
2. Wählen Sie den Tab **General** aus.
3. Wählen Sie im Abschnitt **App Settings** die Option **Edit** aus.
4. Wählen Sie im Feld **Provisioning** die Option **SCIM** aus.
5. Wählen Sie **Save** aus.

### Schritt 1.2: SCIM-Integration einrichten {#step-12-set-up-scim-integration}

1. Wählen Sie den Tab **Provisioning** aus.
2. Wählen Sie unter **Settings** > **Integration** > **SCIM Connection** die Option **Edit** aus und füllen Sie die Feldwerte aus, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.
3. Testen Sie die API-Zugangsdaten, indem Sie **Test API Credentials** auswählen.
4. Wählen Sie **Save** aus.

### Schritt 1.3: Bereitstellung für die App aktivieren {#step-13-enable-provisioning-to-the-app}

1. Wählen Sie unter **Provisioning** > **Settings** > **To App** > **Provisioning to App** die Option **Edit** aus.
2. Aktivieren Sie Folgendes:
    - Create Users
    - Update or aktualisieren Users Attributes
    - Deactivate Users
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping** mit den Zuordnungen, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

## Schritt 2: Nutzer:innen der App zuweisen

1. Wählen Sie den Tab **Assignment** aus.
2. Wählen Sie **Assign** aus und wählen Sie eine Option.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Wählen Sie **Done** aus.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Entra ID integration' %}

{% multi_lang_include scim/scim_alerts.md alert='idp_integration' idp='Entra ID' %}

## Schritt 1: SCIM-Bereitstellungs-App einrichten {#step-1-set-up-scim-provisioning-app}

### Schritt 1.1: Beim Microsoft Entra Admin Center anmelden {#step-11-log-into-microsoft-entra-admin-center}

Melden Sie sich bei Ihrem Microsoft Entra Admin Center an.

### Schritt 1.2: SCIM-App erstellen und einrichten {#step-12-create-and-set-up-your-scim-app}

1. Gehen Sie im Navigationsmenü zu **Entra ID** > **Enterprise apps**.
2. Wählen Sie **New application** aus.
3. Wählen Sie **Create your own application** aus.
4. Geben Sie im Panel einen Namen für Ihre App ein.
5. Wählen Sie im Abschnitt **What are you looking to do with your application?** die Option **Integrate application you don't find in the gallery (Non-gallery)** aus.
6. Wählen Sie **Create** aus.

### Schritt 1.3: SCIM-Integration einrichten {#step-13-set-up-scim-integration}

1. Gehen Sie zum Abschnitt **Manage** > **Provisioning** Ihrer SCIM-Anwendung.
2. Wählen Sie **Connect your application** oder **New configuration** aus und füllen Sie die Feldwerte aus, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.

### Schritt 1.4: Bereitstellung für die App aktivieren {#step-14-enable-provisioning-to-the-app}

1. Gehen Sie zum Abschnitt **Manage** > **Attribute mapping (Preview)** Ihrer SCIM-Anwendung.
2. Wählen Sie **Provision Microsoft Entra ID Users** aus.
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping**, damit er mit den Attributen übereinstimmt, die in der Tabelle auf der Seite **Setup SCIM provisioning** angezeigt werden.
4. Schließen Sie die Seite **Attribute Mapping**.

{% alert important %}
Das Attribut `userName` muss exakt mit der E-Mail-Adresse der Nutzer:innen in Braze übereinstimmen, damit SCIM Nutzer:innen korrekt identifizieren und verwalten kann. Nutzer:innen, die vor der Aktivierung von SCIM manuell in Braze bereitgestellt wurden, werden nicht automatisch in IdP-verwaltete Nutzer:innen umgewandelt, selbst wenn sie der SCIM-Anwendung hinzugefügt werden. Ihre Bereitstellungsmethode bleibt manuell.
{% endalert %}

## Schritt 2: Nutzer:innen der App zuweisen

1. Gehen Sie zu **Manage** > **Users and Groups**.
2. Wählen Sie **Add user/group** aus.
3. Wählen Sie **None Selected** aus, um Nutzer:innen der App zuzuweisen.
4. Wählen Sie den Button **Select** aus, um die Zuweisung zu bestätigen.

{% endtab %}
{% tab Benutzerdefiniert %}

## Schritt 1: SCIM-Einstellungen konfigurieren {#step-1-configure-your-scim-settings}

- **Standard-Workspace:** Wählen Sie den Workspace aus, in dem neue Nutzer:innen standardmäßig hinzugefügt werden sollen. Wenn Sie in Ihrer [SCIM-API-Anfrage]({{site.baseurl}}/post_create_user_account) keinen Workspace angeben, weist Braze Nutzer:innen diesem Workspace zu.
- **Dienst-Herkunft:** Geben Sie die Herkunfts-Domain Ihrer SCIM-Anfragen ein. Braze verwendet diese im `X-Request-Origin`-Header, um zu überprüfen, woher Anfragen stammen.
- **IP-Allowlisting (optional):** Sie können SCIM-Anfragen auf bestimmte IP-Adressen beschränken. Geben Sie eine kommagetrennte Liste oder einen Bereich von IP-Adressen ein, die zugelassen werden sollen. Der `X-Request-Origin`-Header in jeder Anfrage wird verwendet, um die Anfrage-IP-Adresse mit der Allowlist abzugleichen.

## Schritt 2: SCIM-Token / Textbaustein generieren {#step-2-generate-a-scim-token}

Nachdem Sie die erforderlichen Felder ausgefüllt haben, klicken Sie auf **SCIM-Token / Textbaustein generieren**, um ein SCIM-Token / Textbaustein zu generieren und Ihren SCIM-API-Endpunkt anzuzeigen. Stellen Sie sicher, dass Sie das SCIM-Token / Textbaustein kopieren, bevor Sie die Seite verlassen. **Dieses Token / Textbaustein wird nur einmal angezeigt.**

![Felder für SCIM-API-Endpunkt und SCIM-Token mit maskierten Werten und Kopier-Buttons. Unterhalb des Token-Felds befindet sich ein Button „Token zurücksetzen“.]({% image_buster /assets/img/scim.png %})

Braze erwartet, dass alle SCIM-Anfragen das SCIM-API-Bearer-Token / Textbaustein enthalten, das über einen HTTP-`Authorization`-Header angehängt wird.

{% endtab %}
{% endtabs %}