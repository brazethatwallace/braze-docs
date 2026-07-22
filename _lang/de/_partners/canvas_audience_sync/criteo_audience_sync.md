---
nav_title: Criteo
article_title: Canvas Zielgruppen-Synchronisation mit Criteo
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Audience Sync mit Criteo verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr auszuliefern."
page_order: 1
alias: /audience_sync_criteo/

tool:
  - Canvas
---

# Zielgruppen-Synchronisation mit Criteo {#audience-sync-to-criteo}

Mit Braze Audience Sync to Criteo können Marken wahlweise Nutzerdaten aus ihrer eigenen Braze-Integration zu Criteo-Kundenlisten hinzufügen, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt verwendet werden, um eine Anzeige für diese Nutzer:innen in Ihren Criteo-Kundenlisten zu triggern.

**Zu den üblichen Anwendungsfällen für die Zielgruppen-Synchronisation gehören:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Dieses Feature gibt Marken die Möglichkeit zu kontrollieren, welche spezifischen First-Party-Daten mit Criteo geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro – Haftungsausschluss**<br>
Braze Audience Sync to Criteo ist eine Audience Sync Pro-Integration. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager. <br>
{% endalert %}

## Voraussetzungen {#prerequisites}

Sie müssen sicherstellen, dass die folgenden Punkte erstellt und/oder abgeschlossen sind, bevor Sie Ihre Zielgruppen-Synchronisation mit Criteo einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Criteo-Werbekonto | [Criteo](https://marketing.criteo.com/) | Ein aktives Criteo-Werbekonto, das mit Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Ihr Criteo-Administrator Ihnen die entsprechenden Berechtigungen für den Zugriff auf Zielgruppen erteilt hat. |
| [Criteo-Werberichtlinien](https://www.criteo.com/advertising-guidelines/)<br>und<br>[Criteo-Richtlinien zur Markensicherheit](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Als aktive Criteo-Kund:in müssen Sie sicherstellen, dass Sie die Criteo-Richtlinien für Werbung und Markensicherheit einhalten können, bevor Sie Criteo-Kampagnen starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Mit Criteo verbinden {#step-1-connect-to-criteo}

{% alert important %}
Sie müssen über die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) verfügen, um Criteo mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Criteo** aus. Wählen Sie unter Criteo Audience Export die Option **Connect Criteo** aus.

![Criteo-Technologieseite in Braze mit einem Übersichtsbereich und einem Criteo-Bereich mit dem Button „Connect Criteo“.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Es erscheint eine Criteo-oAuth-Seite, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync-Integration zu autorisieren.

Nachdem Sie bestätigt haben, werden Sie zurück zu Braze geleitet, um die Criteo-Werbekonten auszuwählen, mit denen Sie synchronisieren möchten.

![Eine Liste der verfügbaren Werbekonten, die Sie mit Criteo verbinden können.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Nachdem Sie die Verbindung erfolgreich hergestellt haben, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind, und bestehende Konten trennen können.

![Eine aktualisierte Version der Criteo-Technologie-Partnerseite, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Ihre Criteo-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr Criteo-Administrator Sie aus Ihrem Criteo-Werbekonto entfernt, erkennt Braze ein ungültiges Token. Dies hat zur Folge, dass Ihre aktiven Canvases, die Criteo verwenden, Fehler anzeigen und Braze nicht in der Lage ist, Nutzer:innen zu synchronisieren.

### Schritt 2: Canvas-Eingangskriterien konfigurieren {#step-2-configure-your-canvas-entry-criteria}

Beim Aufbau von Zielgruppen für das Ad Tracking möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen einbeziehen oder ausschließen, um Datenschutzgesetze einzuhalten, wie z. B. das Recht „Nicht verkaufen oder weitergeben“ gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen.

Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection) erfasst haben, können Sie den Filter „Ads Tracking Enabled“ verwenden. Wählen Sie den Wert „true“ aus, um Nutzer:innen nur in Audience Sync-Ziele zu senden, für die sie ein Opt-in gesetzt haben.

![Canvas-Eingangsfilter mit „Ads Tracking Enabled“ auf „true“ gesetzt.]({% image_buster /assets/img/criteo/criteo11.png %})

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute erfassen, sollten Sie diese in Ihre Canvas-Eingangskriterien als Filter einbeziehen:

![Canvas-Eingangsfilter mit angepassten Opt-in-Attributen für die Zielgruppeneignung.]({% image_buster /assets/img/criteo/criteo12.png %})

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance).

### Schritt 3: Audience Sync-Schritt mit Criteo hinzufügen {#step-3-add-an-audience-sync-step-with-criteo}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![Arbeitsablauf der vorherigen Schritte zum Hinzufügen einer Criteo Audience-Komponente in Canvas.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Arbeitsablauf der vorherigen Schritte zum Hinzufügen einer Criteo Audience-Komponente in Canvas.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Schritt 4: Sync-Einrichtung {#step-4-sync-setup}

Klicken Sie auf den Button **Custom Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **Criteo** als den gewünschten Audience Sync-Partner aus.

![Audience Sync-Schritteditor mit Criteo als ausgewähltem Partner.]({% image_buster /assets/img/criteo/criteo6.png %})

Wählen Sie dann Ihr gewünschtes Criteo-Werbekonto aus. Geben Sie in der Dropdown-Liste **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}
**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Add Users to Audience**, und wählen Sie aus, welche Felder Sie mit Criteo synchronisieren möchten. Speichern Sie anschließend Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Create Audience** klicken.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier wird das gewünschte Werbekonto ausgewählt und eine neue Zielgruppe erstellt.]({% image_buster /assets/img/criteo/criteo3.png %})

Braze zeigt am oberen Rand des Schritteditors eine Benachrichtigung an, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um sie später in der Canvas-Journey zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Eine Warnung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/criteo/criteo1.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie die Audience Sync-Komponente betreten.
{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}
**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden Criteo-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und wählen Sie **Add to the Audience**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Werbekonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten {#step-5-launch-canvas}

Sobald Sie Ihre Zielgruppen-Synchronisation mit Criteo konfiguriert haben, starten Sie einfach das Canvas! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Audience Sync-Schritt durchlaufen, werden in diese Zielgruppe auf Criteo übertragen. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangebracht.

Sie können die Zielgruppe in Criteo ansehen, indem Sie in Ihr Ads-Manager-Konto gehen und dann Segmente aus der **Audience Library** in der Navigation auswählen. Auf der Seite **Segments** sehen Sie die Größe der einzelnen Zielgruppen, nachdem sie ~1.000 erreicht haben.

![Die Audience Library mit Segment, ID, Quelle, Typ, Größe, aktueller Verwendung und letztem Update.]({% image_buster /assets/img/criteo/criteo.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, synchronisiert Braze sie nahezu in Realtime und respektiert dabei die Rate-Limits der Criteo-API. Braze verarbeitet alle fünf Sekunden so viele Nutzer:innen wie möglich, bevor sie an Criteo gesendet werden.

Das Rate-Limit der Criteo-API erlaubt nicht mehr als 250 Anfragen pro Minute. Erreicht eine Kund:in dieses Limit, wiederholt Braze die Synchronisierung für bis zu ~13 Stunden. Wenn die Synchronisierung immer noch nicht möglich ist, listet Braze diese Nutzer:innen in der Metrik „Fehler bei Nutzer:innen“ auf.

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrik | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente betreten haben, um mit Criteo synchronisiert zu werden. |
| Zum nächsten Schritt fortgefahren | Wie viele Nutzer:innen zum nächsten Schritt vorangebracht wurden, falls einer vorhanden ist. Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit Criteo synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Criteo verarbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Criteo synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Criteo-Token oder eine auf Criteo gelöschte Zielgruppe sein. |
| Canvas verlassen | Anzahl der Nutzer:innen, die das Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

{% alert important %}
Denken Sie daran, dass es bei den Metriken „Nutzer:innen synchronisiert“ und „Fehler bei Nutzer:innen“ aufgrund des Bulk-Flush und der 13-stündigen Wiederholung zu einer Verzögerung bei der Berichterstattung kommt.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was sollte ich als Nächstes tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}
Sie können die Verbindung zu Ihrem Criteo-Konto auf der Criteo-Partnerseite einfach trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Criteo-Administrator, dass Sie die entsprechenden Berechtigungen für das Werbekonto haben, mit dem Sie synchronisieren möchten.

### Warum kann mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

Bestätigen Sie auf der Criteo-Partnerseite, dass Ihr Criteo-Werbekonto erfolgreich mit Braze verbunden wurde. Überprüfen Sie als Nächstes, ob Sie ein Werbekonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und passende Felder ausgewählt haben.

### Woher weiß ich, ob Nutzer:innen übereinstimmen, nachdem ich Nutzer:innen an Criteo weitergegeben habe? {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}

Criteo stellt diese Informationen aufgrund eigener Datenschutzrichtlinien nicht zur Verfügung.

### Wie viele Zielgruppen kann Criteo unterstützen? {#how-many-audiences-can-criteo-support}

Zurzeit können Sie nur 1.000 Zielgruppen in Ihrem Criteo-Konto haben. Wenn Sie dieses Limit überschreiten, benachrichtigt Braze Sie, dass keine neuen Zielgruppen erstellt werden können. Sie müssen Zielgruppen, die Sie nicht mehr verwenden, aus Ihrem Criteo-Werbekonto entfernen.