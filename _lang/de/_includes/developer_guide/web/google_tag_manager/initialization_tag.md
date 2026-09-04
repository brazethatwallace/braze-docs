### Voraussetzungen {#prerequisites}

Bevor Sie diese Integrationsmethode verwenden können, müssen Sie [ein Konto und einen Container für Google Tag Manager erstellen](https://support.google.com/tagmanager/answer/14842164).

### 1. Schritt: Tag-Template-Galerie öffnen {#step-1-open-the-tag-template-gallery}

Wählen Sie im [Google Tag Manager](https://tagmanager.google.com/) Ihren Workspace aus und wählen Sie dann **Templates**. Wählen Sie im Bereich **Tag Template** die Option **Search Gallery**.

![Die Template-Seite für einen Beispiel-Workspace im Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### 2. Schritt: Initialisierungs-Tag-Template hinzufügen {#step-2-add-the-initialization-tag-template}

Suchen Sie in der Template-Galerie nach `braze-inc` und wählen Sie dann **Braze Initialization Tag** aus.

![Die Template-Galerie mit den verschiedenen „braze-inc“-Templates.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Wählen Sie **Add to workspace** > **Add**.

![Die Seite „Braze Initialization Tag“ im Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### 3. Schritt: Tag konfigurieren {#step-3-configure-the-tag}

Wählen Sie im Abschnitt **Templates** Ihr neu hinzugefügtes Template aus.

![Die Seite „Templates“ im Google Tag Manager mit dem Braze Initialization Tag Template.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Wählen Sie das Bleistift-Symbol, um das Dropdown-Menü **Tag Configuration** zu öffnen.

![Die Kachel „Tag Configuration“ mit dem Bleistift-Symbol.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Geben Sie die erforderlichen Mindestinformationen ein:

| Feld         | Beschreibung |
| ------------- | ----------- |
| **API Key**   | Ihr [Braze-API-Schlüssel]({{site.baseurl}}/api/basics#about-rest-api-keys), den Sie im Braze-Dashboard unter **Settings** > **App Settings** finden. |
| **API Endpoint** | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
| **SDK Version**  | Die aktuellste `MAJOR.MINOR`-Version des Web Braze SDK, die im [Changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web) aufgeführt ist. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Weitere Informationen finden Sie unter [Über die SDK-Versionsverwaltung]({{site.baseurl}}/developer_guide/sdk_integration/version_management). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3. Schritt: Tag konfigurieren" }

Für zusätzliche Initialisierungseinstellungen wählen Sie **Braze Initialization Options** und wählen die gewünschten Optionen aus.

![Die Liste der Braze Initialization Options unter „Tag Configuration“.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### 4. Schritt: Initialisierungsoptionen auswählen {#step-4-choose-initialization-options}

Das Braze Initialization Tag bietet die folgenden Optionen. Die meisten davon lassen sich direkt den [Web SDK `InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) zuordnen, und einige entsprechen Web-SDK-Methoden, die das Tag während der Initialisierung aufruft. Wählen Sie die Optionen aus, die Ihren Integrationsanforderungen entsprechen:

| GTM-Option | Web-SDK-Konfiguration oder -Methode | Beschreibung |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | Aktiviert HTML-In-App-Nachrichten, Banner und von Nutzer:innen bereitgestellte JavaScript-Klickaktionen. Erforderlich für [HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) und [Banner]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web), die angepasstes HTML verwenden. Aktivieren Sie diese Option nur, wenn Sie dem HTML- und JavaScript-Inhalt vertrauen, da sie die Ausführung von benutzerdefiniertem JavaScript ermöglicht. |
| **App Version Number** | `appVersion`, `appVersionNumber` | App-Version für die Segmentierung (zum Beispiel `1.2.3.4`). |
| **Automatically Open New Session** | `braze.openSession()` | Öffnet eine neue Sitzung, nachdem das SDK initialisiert wurde, indem diese Methode automatisch aufgerufen wird. |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | Zeigt neue In-App-Nachrichten automatisch an, wenn sie vom Server eintreffen, indem diese Methode nach der Initialisierung aufgerufen wird. |
| **Disable Automatic Push-Token Maintenance** | `disablePushTokenMaintenance` | Verhindert, dass das SDK Push-Token bei neuen Sitzungen mit dem Braze-Backend synchronisiert. |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | Verwenden Sie diese Option, wenn Sie den Service Worker selbst registrieren und verwalten. |
| **Disable Cookies** | `noCookies` | Verwendet localStorage anstelle von Cookies für Nutzer:innen- und Sitzungsdaten. Verhindert die subdomainübergreifende Erkennung. |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | Verhindert, dass das SDK Font Awesome aus dem CDN lädt. Verwenden Sie diese Option, wenn Ihre Website bereits über eine eigene Font-Awesome-Version verfügt. |
| **Enable SDK Authentication** | `enableSdkAuthentication` | Aktiviert die [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication). |
| **Enable Web SDK Logging** | `enableLogging` | Aktiviert die Konsolenprotokollierung für das Debugging. Entfernen Sie diese Option vor dem Produktivbetrieb. |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | Mindestzeit in Sekunden zwischen getriggerten Aktionen (Standard: 30). |
| **Open Cards in New Tab** | `openCardsInNewTab` | Öffnet Content-Card-Links in einem neuen Tab, wenn die Standard-Feed-UI verwendet wird. |
| **Service Worker Location** | `serviceWorkerLocation` | Benutzerdefinierter Pfad für die Service-Worker-Datei (Standard: `/service-worker.js`). |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | Sitzungszeitlimit in Sekunden (Standard: 1800). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="4. Schritt: Initialisierungsoptionen auswählen" }

{% alert note %}
Um [angepasste HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) bei Verwendung des Google Tag Manager Braze Initialization Tag zu aktivieren, wählen Sie **Allow HTML In-App Messages** in den **Braze Initialization Options** aus. Dieses Kontrollkästchen entspricht der Initialisierungsoption `allowUserSuppliedJavascript` in `braze.initialize()` und setzt sie auf `true`. Das Google Tag Manager Braze Initialization Tag verwendet dieses Label anstelle des Optionsnamens.
{% endalert %}

Für Optionen, die nicht im GTM-Template verfügbar sind (wie `contentSecurityNonce`, `localization` oder `devicePropertyAllowlist`), verwenden Sie stattdessen die [Laufzeitinitialisierung]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

### 5. Schritt: Auf *allen Seiten* triggern {#step-5-set-to-trigger-on-all-pages}

Das Initialisierungs-Tag sollte auf allen Seiten Ihrer Website ausgeführt werden. So können Sie die Braze-SDK-Methoden nutzen und Web-Push-Analytics erfassen.

{% alert important %}
**Tag-Reihenfolge:** Das Braze Initialization Tag muss vor allen anderen Tags ausgelöst werden, die Braze-SDK-Methoden aufrufen (wie `braze.getUser()` oder `braze.logCustomEvent()`). Wenn angepasste Events, Nutzer:innen-Attribute oder andere Braze-Methodenaufrufe vor der SDK-Initialisierung ausgelöst werden, können Fehler wie `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')` auftreten. Um die richtige Reihenfolge sicherzustellen, konfigurieren Sie Ihr Braze Initialization Tag als Setup-Tag oder verwenden Sie die Tag-Sequenzierungsfunktion von GTM, um sicherzustellen, dass es zuerst ausgelöst wird. Weitere Informationen finden Sie unter [Tag-Sequenzierung für Braze-Action-Tags]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/?sdktab=web#web_tag-sequencing-for-braze-action-tags).
{% endalert %}

### 6. Schritt: Integration überprüfen {#step-6-verify-your-integration}

Sie können Ihre Integration mit einer der folgenden Optionen überprüfen:

- **Option 1:** Mit dem [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager können Sie prüfen, ob das Braze Initialization Tag auf Ihren konfigurierten Seiten oder bei Ihren konfigurierten Ereignissen korrekt getriggert wird.
- **Option 2:** Prüfen Sie, ob von Ihrer Webseite Netzwerk-Anfragen an Braze gesendet werden. Darüber hinaus sollte die globale `window.braze`-Bibliothek nun definiert sein.