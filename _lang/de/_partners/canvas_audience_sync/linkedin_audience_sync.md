---
nav_title: LinkedIn
article_title: Canvas-Zielgruppen-Synchronisierung mit LinkedIn
alias: /linkedin_audience_sync/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync mit LinkedIn verwenden, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen."
tool:
  - Canvas
page_order: 4

---

# Zielgruppen-Synchronisierung mit LinkedIn {#audience-sync-to-linkedin}

Mit der Braze Audience Sync mit LinkedIn können Marken Nutzerdaten aus ihrer Braze-Integration zu LinkedIn-Kundenlisten hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt eine Anzeige an diese Nutzer:innen in Ihren LinkedIn-Kundenlisten triggern.

**Zu den häufigen Anwendungsfällen für Audience Syncing gehören**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit LinkedIn geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

## Voraussetzungen {#prerequisites}

Sie müssen sicherstellen, dass die folgenden Elemente erstellt, abgeschlossen oder akzeptiert wurden, bevor Sie Ihren LinkedIn Audience Sync-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Audience Sync Pro | Braze | LinkedIn ist ein [Audience Sync Pro]({{site.baseurl}}/partners/canvas_audience_sync/overview#audience-sync-pro)-Partner. Wählen Sie LinkedIn in Ihren Audience Sync Pro-Kontingenten auf der Seite **Technologie-Partner** aus, bevor Sie ein Anzeigenkonto verknüpfen. Wenden Sie sich an Ihren Braze Account Manager, um Informationen zum Kauf zu erhalten. |
| LinkedIn-Anzeigenkonto | [LinkedIn](https://www.linkedin.com/campaignmanager) | Ein aktives LinkedIn-Anzeigenkonto, das mit Ihrer Marke verknüpft ist.<br><br>Stellen Sie sicher, dass Sie alle relevanten LinkedIn-Geschäftsbedingungen akzeptiert haben, um auf dieses Konto zugreifen und es nutzen zu können. Ihr LinkedIn-Admin muss Ihnen eine der folgenden Anzeigenkonto-Rollen zuweisen: Account Billing Admin, Account Manager, Campaign Manager oder Creative Manager. |
| LinkedIn-Geschäftsbedingungen und -Richtlinien | LinkedIn | Stimmen Sie der Einhaltung aller von LinkedIn geforderten Geschäftsbedingungen, Richtlinien, Leitlinien und Dokumentationen im Zusammenhang mit Ihrer Nutzung von LinkedIn Audience Sync zu, einschließlich aller darin durch Verweis einbezogenen Geschäftsbedingungen, Richtlinien, Leitlinien und Dokumentationen, darunter möglicherweise: Services Terms, Ads Agreement, Data Processing Agreement und Professional Community Guidelines von LinkedIn. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Mit LinkedIn verbinden {#step-1-connect-to-linkedin}

{% alert important %}
Sie müssen die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) haben, um LinkedIn mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Technologie-Partner** und wählen Sie **LinkedIn** aus. Wählen Sie im Bereich **LinkedIn Audience Sync** die Option **Connect LinkedIn** aus.

Sie werden dann auf die LinkedIn-OAuth-Seite weitergeleitet, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync-Integration zu autorisieren. Nachdem Sie **Bestätigen** gewählt haben, werden Sie zurück zu Braze geleitet, um auszuwählen, mit welchen LinkedIn-Anzeigenkonten Sie synchronisieren möchten.

![„Braze Self Service“ ist als das zu verbindende Anzeigenkonto ausgewählt.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Sobald Sie sich erfolgreich verbunden haben, werden Sie auf die Partnerseite zurückgebracht, wo Sie sehen können, welche Konten verbunden sind, und bestehende Konten trennen können.

![Ein erfolgreich verbundenes LinkedIn-Konto.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Ihre LinkedIn-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr LinkedIn-Administrator Sie aus Ihrem LinkedIn-Anzeigenkonto entfernt, erkennt Braze ein ungültiges Token. Dies hat zur Folge, dass Ihre aktiven Canvases, die LinkedIn verwenden, Fehler anzeigen und Braze nicht in der Lage ist, Nutzer:innen zu synchronisieren.

### Schritt 2: Canvas-Eingangskriterien konfigurieren {#step-2-configure-your-canvas-entry-criteria}

Beim Aufbau von Zielgruppen für das Ad Tracking möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen und Datenschutzgesetze einhalten, wie z. B. das Recht „Nicht verkaufen oder weitergeben“ gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen.

Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection) erfasst haben, können Sie den Filter **Ads Tracking Enabled** verwenden. Wählen Sie den Wert `true` aus, um Nutzer:innen nur in Audience Sync-Ziele zu senden, für die sie ein Opt-in gesetzt haben. iOS-Werbe-IDs werden nicht als Abgleichsfelder für LinkedIn Audience Sync unterstützt.

![Eine Entry-Zielgruppe mit dem Filter „Ad Tracking Enabled ist true“.]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute erfassen, sollten Sie diese in Ihre Canvas-Eingangskriterien als Filter einbeziehen:

![Ein Canvas mit einer Entry-Zielgruppe, bei der „opted_in_marketing“ gleich „true“ ist.]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance).

### Schritt 3: Einen Audience Sync-Schritt mit LinkedIn hinzufügen {#step-3-add-an-audience-sync-step-with-linkedin}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie Audience Sync. Klicken Sie auf den Button **Custom Audience**, um den Komponenteneditor zu öffnen.

### Schritt 4: Sync-Einrichtung {#step-4-sync-setup}

1. Wählen Sie **LinkedIn** als den gewünschten Audience Sync-Partner aus.
2. Wählen Sie das gewünschte LinkedIn-Anzeigenkonto aus.
3. Geben Sie in der Dropdown-Liste **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

#### Eine neue Zielgruppe erstellen {#create-a-new-audience}

Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Add Users to Audience** und wählen Sie aus, welche Felder Sie mit LinkedIn synchronisieren möchten. Für diese Integration unterstützt Braze derzeit Folgendes:
- E-Mail
- Vor- und Nachname (beide sind erforderlich, wenn Sie den Namensabgleich verwenden)
- Android-GAID

iOS-Werbe-IDs werden nicht als Abgleichsfelder für LinkedIn unterstützt.

Speichern Sie anschließend Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Create Audience** klicken.

![Ein Beispiel für eine „Leads“-Zielgruppe mit dem ausgewählten Braze-Anzeigenkonto, der „Leads“-Zielgruppe, der Aktion zum Hinzufügen von Nutzer:innen zur Zielgruppe und E-Mail, Android-GAID sowie Vor- und Nachname als abzugleichende Felder.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze zeigt am oberen Rand des Schritteditors eine Benachrichtigung an, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn Fehler auftreten. Sie können diese Zielgruppe referenzieren, um Nutzer:innen später in der Canvas-Journey zu entfernen, nachdem Sie sie im Schritteditor gespeichert haben.

![Bestätigung, dass die „Leads“-Zielgruppe erstellt wurde.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen, sobald sie den Audience Sync-Schritt erreichen, vorbehaltlich [Batching und Latenz]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}

#### Mit einer bestehenden Zielgruppe synchronisieren {#sync-with-an-existing-audience}

Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden LinkedIn-Zielgruppen hinzuzufügen oder daraus zu entfernen, um sicherzustellen, dass diese Zielgruppen aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und wählen Sie dann **Add to the Audience** oder **Remove from the Audience**. Braze synchronisiert die Nutzer:innen, sobald sie den Audience Sync-Schritt erreichen, vorbehaltlich [Batching und Latenz]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten {#step-5-launch-canvas}

Sobald Sie Ihre Audience Sync mit LinkedIn konfiguriert haben, starten Sie das Canvas! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Audience Sync-Schritt durchlaufen, werden in diese Zielgruppe auf LinkedIn weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangebracht.

Sie können die Zielgruppe auf LinkedIn einsehen, indem Sie in Ihr Anzeigenkonto gehen und **Audiences** unter dem Abschnitt **Assets** in der Navigation auswählen. Auf der Seite **Audiences** können Sie die Größe jeder Zielgruppe sehen, sobald sie mehr als 300 Mitglieder erreicht hat.

![LinkedIn-Seite mit den folgenden Metriken für die angegebene Zielgruppe.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Überlegungen zur Nutzersynchronisierung und zu Rate-Limits {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, stellt Braze sie für die Stapelverarbeitung in eine Warteschlange, bevor sie an LinkedIn gesendet werden. Unter [Stapelverarbeitung und Latenz]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency) erfahren Sie, wie Braze Stapel versendet.

Braze sendet bis zu 2.000 Nutzer:innen pro Anfrage an LinkedIn. Wenn die API-Rate-Limits von LinkedIn Ihr Konto einschränken, versucht Braze die Synchronisierung bis zu ca. 13 Stunden lang erneut. Ist die Synchronisierung dann immer noch nicht möglich, werden diese Nutzer:innen unter der Metrik „Users Errored“ aufgeführt.

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| METRIK | BESCHREIBUNG |
| ------ | ----------- |
| Eingetreten | Anzahl der Nutzer:innen, die in diese Komponente eingetreten sind, um mit LinkedIn synchronisiert zu werden. |
| Zum nächsten Schritt fortgefahren | Wie viele Nutzer:innen sind zur nächsten Komponente weitergegangen, falls eine vorhanden ist? Alle Nutzer:innen gehen automatisch weiter, wenn dies der letzte Schritt im Canvas-Branch ist. |
| Synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die erfolgreich mit LinkedIn synchronisiert wurden. |
| Nicht synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund fehlender Abgleichsfelder nicht synchronisiert wurden. |
| Ausstehende Nutzer:innen | Anzahl der Nutzer:innen, die derzeit von Braze verarbeitet werden, um mit LinkedIn synchronisiert zu werden. |
| Fehlerhafte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit LinkedIn synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges LinkedIn-Token oder eine auf LinkedIn gelöschte Zielgruppe sein. |
| Canvas verlassen | Anzahl der Nutzer:innen, die das Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

{% alert important %}
Beachten Sie, dass es bei der Berichterstattung zu Verzögerungen bei den Metriken für synchronisierte Nutzer:innen und fehlerhafte Nutzer:innen kommt, die auf die Batchverarbeitung bzw. die 13-stündige Wiederholungsphase zurückzuführen sind.
{% endalert %}

{% alert important %}
LinkedIn stellt zusätzliche Metriken zu Übereinstimmungsraten innerhalb ihrer Plattform bereit. Um die Übereinstimmung Ihrer spezifischen Audience Sync zu überprüfen, wählen Sie die Audience Sync-Schrittmetriken aus, um zur Seite **Canvas-Schrittdetails** zu gelangen.
<br><br>
Wählen Sie den Partner als **LinkedIn**, Ihr Werbekonto und die Zielgruppe aus, um die Zielgruppengröße und Übereinstimmungsrate von LinkedIn zu sehen.

![Beispiel für Audience Sync-Schrittmetriken mit 10.000 eingetretenen Nutzer:innen.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert es, bis die Zielgruppengrößen in LinkedIn angezeigt werden? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Es kann bis zu 48 Stunden dauern, bis die Zielgruppen in Ihrem LinkedIn-Konto angezeigt werden.

### Welche Mindestgröße muss eine Zielgruppe haben, damit LinkedIn sie in Ihrem Werbekonto anzeigt? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

Die Zielgruppe muss mindestens 300 Mitglieder umfassen, damit die Zielgruppengröße in Ihrem LinkedIn-Konto angezeigt wird.

### Was sollte ich tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Sie können Ihr LinkedIn-Konto auf der LinkedIn-Partnerseite trennen und erneut verbinden. Bestätigen Sie mit Ihrem LinkedIn-Administrator, dass Sie über die entsprechenden Berechtigungen für das Werbekonto verfügen, mit dem Sie synchronisieren möchten.

### Warum darf mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

Stellen Sie sicher, dass Ihr LinkedIn-Werbekonto auf der LinkedIn-Partnerseite erfolgreich mit Braze verbunden wurde. Vergewissern Sie sich anschließend, dass Sie ein Werbekonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und Felder zum Abgleich ausgewählt haben.

### Wie erfahre ich, ob Nutzer:innen nach der Übertragung an LinkedIn abgeglichen wurden? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn stellt in seinem Dashboard Informationen zu Abgleichquoten bereit. Sie können diese in LinkedIn im Bereich **Audiences** einsehen. Die Abgleichquote für Ihre LinkedIn-Zielgruppe können Sie in den Canvas-Schritt-Details Ihres Audience-Sync-Schritts überprüfen.

### Wie viele Zielgruppen kann LinkedIn unterstützen? {#how-many-audiences-can-linkedin-support}

Derzeit gibt es keine Begrenzung der Anzahl von Zielgruppen in Ihrem LinkedIn-Werbekonto.

### Warum bleibt ein Segment im Status BUILDING hängen und wird nicht aktualisiert? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Ein Segment gilt als ungenutzt und wird auf ARCHIVED gesetzt, wenn es 30 Tage lang nicht durchgängig in einer Entwurfs- oder aktiven Campaign verwendet wird. Aus diesem Grund kann ein Segment scheinbar im Status BUILDING „hängen bleiben“, wenn Aktualisierungen an ein ARCHIVED-Segment gestreamt werden, es dadurch in den Status BUILDING versetzt wird und kurz bevor es erneut archiviert wird, neue Aktualisierungen an das ungenutzte Segment gestreamt werden.