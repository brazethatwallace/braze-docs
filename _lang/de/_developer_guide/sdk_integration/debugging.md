---
page_order: 1.3
nav_title: Fehlersuche
article_title: Fehlersuche im Braze SDK
description: "Erfahren Sie, wie Sie den Braze SDK-Debugger verwenden, damit Sie Probleme in Ihren SDK-gestützten Kanälen beheben können, ohne die ausführliche Protokollierung in Ihrer App aktivieren zu müssen."
---

# Fehlersuche im Braze SDK {#debugging-the-braze-sdk}

> Erfahren Sie, wie Sie den integrierten Debugger des Braze SDK verwenden, damit Sie Probleme in Ihren SDK-gestützten Kanälen beheben können, ohne die ausführliche Protokollierung in Ihrer App aktivieren zu müssen.

{% alert tip %}
Für eine eingehendere Untersuchung können Sie auch [die ausführliche Protokollierung aktivieren]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), um detaillierte SDK-Ausgaben zu erfassen, und [erfahren, wie Sie ausführliche Protokolle lesen]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) – für bestimmte Kanäle.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um den Braze SDK-Debugger zu verwenden, benötigen Sie die Berechtigungen „View PII“ und „View User Profiles (PII Redacted)“. Um Ihre Debugging-Sitzungsprotokolle herunterzuladen, benötigen Sie außerdem die Berechtigung „Export User Data“. Zusätzlich muss Ihr Braze SDK die folgenden Mindestversionen erfüllen oder darauf verweisen:

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

Um Debugger-Protokolle zu erfassen, wenn `Braze.configuration.logger.level` auf `.disabled` gesetzt ist, verwenden Sie Swift SDK 11.9.0 oder höher. Weitere Informationen finden Sie in den [Swift Changelogs]({{site.baseurl}}/developer_guide/changelogs#swift_fixed-12).

## Debugging des Braze SDK

{% alert tip %}
Um das Debugging für das Braze Web SDK zu aktivieren, können Sie [einen URL-Parameter verwenden]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#logging).
{% endalert %}

### Schritt 1: Schließen Sie Ihre App {#step-1-close-your-app}

Bevor Sie Ihre Debugging-Sitzung starten, schließen Sie die App, bei der derzeit Probleme auftreten. Sie können die App zu Beginn Ihrer Sitzung erneut starten.

### Schritt 2: Erstellen Sie eine Debugging-Sitzung {#step-2-create-a-debugging-session}

Gehen Sie in Braze zu **Einstellungen** und wählen Sie dann unter **Einrichtung und Tests** die Option **SDK Debugger** aus.

![Der Bereich „Einrichtung und Tests“ mit hervorgehobenem „SDK Debugger“.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Wählen Sie **Debugging-Sitzung erstellen** aus.

![Die Seite „SDK Debugger“.]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Schritt 3: Wählen Sie eine Nutzer:in aus {#step-3-select-a-user}

Suchen Sie nach einer Nutzer:in anhand ihrer E-Mail-Adresse, `external_id`, ihres Nutzer-Alias oder Push-Tokens. Wenn Sie bereit sind, Ihre Sitzung zu starten, wählen Sie **Nutzer:in auswählen** aus.

![Die Debugging-Seite für die ausgewählte Nutzer:in.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Schritt 4: Starten Sie die App erneut {#step-4-relaunch-the-app}

Starten Sie zunächst die App und bestätigen Sie, dass Ihr Gerät gekoppelt ist. Wenn die Kopplung erfolgreich war, starten Sie Ihre App erneut – so wird sichergestellt, dass die Initialisierungsprotokolle der App vollständig erfasst werden.

### Schritt 5: Führen Sie die Reproduktionsschritte durch {#step-5-complete-the-reproduction-steps}

Folgen Sie nach dem erneuten Starten Ihrer App den Schritten, um den Fehler zu reproduzieren.

{% alert tip %}
Wenn Sie den Fehler reproduzieren, achten Sie darauf, die Reproduktionsschritte so genau wie möglich zu befolgen, damit Sie [qualitativ hochwertige Protokolle](#step-6-export-your-session-logs-optional) erstellen können.
{% endalert %}

### Schritt 6: Beenden Sie Ihre Sitzung {#step-6-end-your-session}

Wenn Sie mit Ihren Reproduktionsschritten fertig sind, wählen Sie **Sitzung beenden** > **Schließen** aus.

![Die Debugging-Sitzung mit dem Button „Sitzung beenden“.]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Je nach Sitzungslänge und Netzwerkverbindung kann es einige Minuten dauern, bis Ihre Protokolle generiert sind.
{% endalert %}

### Schritt 7: Teilen oder exportieren Sie Ihre Sitzung (optional) {#step-7-share-or-export-your-session-optional}

Nach Ihrer Sitzung können Sie Ihre Sitzungsprotokolle als CSV-Datei exportieren. Außerdem können andere Ihre **Sitzungs-ID** verwenden, um nach Ihrer Debug-Sitzung zu suchen, sodass Sie ihnen Ihre Protokolle nicht direkt senden müssen.

![Die Debugging-Seite mit den Optionen „Protokolle exportieren“ und „Sitzungs-ID kopieren“ nach der Sitzung.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})