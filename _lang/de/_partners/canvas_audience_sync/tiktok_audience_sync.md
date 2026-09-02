---
nav_title: TikTok
article_title: Canvas Audience Sync mit TikTok
alias: /tiktok_audience_sync/
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Audience Sync für TikTok verwenden, um Werbung auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
tool:
  - Canvas
page_order: 8

---

# Audience Sync mit TikTok {#audience-sync-to-tiktok}

Mit Braze Audience Sync to TikTok können Marken wahlweise Nutzerdaten aus ihrer eigenen Braze-Integration zu TikTok Audiences hinzufügen, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen. Alle Kriterien, die Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas verwenden würden.

**Zu den häufigen Anwendungsfällen für Audience Syncing gehören**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit TikTok geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro – Haftungsausschluss**<br>
Braze Audience Sync to TikTok ist eine Integration von Audience Sync Pro. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager:in.
{% endalert %}

## Voraussetzungen {#prerequisites}

Sie müssen sicherstellen, dass die folgenden Punkte erstellt, abgeschlossen und/oder akzeptiert wurden, bevor Sie Ihren TikTok-Zielgruppen-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| TikTok for Business Center-Konto | [TikTok](https://business.tiktok.com/) | Ein zentrales Tool zur Verwaltung der TikTok-Assets Ihrer Marke (z. B. Werbekonten, Seiten, Apps). |
| TikTok-Werbekonto | [TikTok](https://ads.tiktok.com/) | Ein aktives TikTok-Werbekonto, das mit dem Business Center-Konto Ihrer Marke verknüpft ist.<br><br>Stellen Sie sicher, dass Ihnen der Admin-Manager:in Ihres TikTok Business Centers Administratorberechtigungen für die TikTok-Werbekonten erteilt hat, die Sie mit Braze verwenden möchten. |
| TikTok-Nutzungsbedingungen und -Richtlinien | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Stimmen Sie zu, alle erforderlichen Nutzungsbedingungen, Richtlinien, Leitlinien und Dokumentationen von TikTok einzuhalten, die sich auf Ihre Nutzung von TikTok Audience Sync beziehen, einschließlich aller darin durch Verweis einbezogenen Nutzungsbedingungen, Richtlinien, Leitlinien und Dokumentationen, die unter anderem Folgendes umfassen können: die Commercial Terms of Service, Advertising Terms, Privacy Policy, Custom Audience Terms, Developer Terms of Service, Developer Data Sharing Agreement, Advertising Policies, Brand Guidelines und Community Guidelines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Mit TikTok verbinden {#step-1-connect-to-tiktok}

{% alert important %}
Sie müssen die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) haben, um TikTok mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **TikTok** aus. Wählen Sie unter TikTok Audience Sync die Option **TikTok verbinden** aus.

![Die TikTok-Technologie-Seite in Braze enthält einen Übersichtsabschnitt und einen Abschnitt „TikTok Audience Sync“ mit dem Button „Connected TikTok“.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Sie werden dann auf die TikTok-OAuth-Seite weitergeleitet, um Braze für die Verwaltung von Anzeigenkonten und Zielgruppen zu autorisieren. Nachdem Sie **Bestätigen** ausgewählt haben, werden Sie zurück zu Braze geleitet, um auszuwählen, mit welchen TikTok-Anzeigenkonten Sie synchronisieren möchten.

![TikTok-OAuth-Autorisierungsseite mit Zugriffsanfrage für die Braze-Zielgruppenverwaltung.]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Sobald die Verbindung erfolgreich hergestellt wurde, kehren Sie zur Partnerseite zurück. Hier können Sie sehen, welche Konten verbunden sind, und die Verbindung zu bestehenden Konten trennen.

![Braze-TikTok-Partnerseite mit verbundenen TikTok-Anzeigenkonten.]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Ihre TikTok-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr TikTok-Administrator Sie aus Ihrem TikTok Business Center oder dem Zugriff auf die verbundenen TikTok-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die TikTok Audience-Komponenten verwenden, Fehler anzeigen, und Braze wird die Nutzer:innen nicht synchronisieren können.

### Schritt 2: Eine TikTok Audience-Komponente in Canvas hinzufügen {#step-2-add-a-tiktok-audience-component-in-canvas}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync** aus.

![Canvas-Schrittauswahl mit der Option „Audience Sync“-Komponente.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Audience Sync-Komponentenkarte, die einem Canvas-Pfad hinzugefügt wurde.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung {#step-3-sync-setup}

Klicken Sie auf den Button **Custom Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **TikTok** als gewünschten Audience Sync-Partner aus.

![Audience Sync-Komponenteneditor mit TikTok als ausgewähltem Sync-Partner.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie dann das gewünschte TikTok-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

![TikTok Audience Sync-Editor mit Anzeigenkontoauswahl und Zielgruppen-Dropdown.]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Add Users to Audience** und wählen Sie die Felder aus, die Sie mit TikTok synchronisieren möchten. Speichern Sie anschließend Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Create Audience** klicken.

![Formular zum Erstellen einer neuen Zielgruppe im TikTok Audience Sync-Schritt mit ausgewählten Abgleichfeldern.]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Braze zeigt am oberen Rand des Schritteditors eine Benachrichtigung an, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um Nutzer:innen später im Canvas-Verlauf zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Erfolgsbenachrichtigung im Audience Sync-Schritt nach dem Erstellen einer neuen TikTok-Zielgruppe.]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie den Zielgruppen-Schritt betreten.

{% endtab %}
{% tab Mit bestehender Zielgruppe synchronisieren %}

**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden TikTok-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und wählen Sie **Add to the Audience**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie den TikTok Audience-Schritt betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten {#step-4-launch-canvas}

Sobald Sie Ihre TikTok Audience-Komponente konfiguriert haben, starten Sie den Canvas! Es wird eine neue Zielgruppe erstellt, und Nutzer:innen, die die TikTok Audience-Komponente durchlaufen, werden in diese Zielgruppe auf TikTok übertragen. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangebracht.

Sie können die Zielgruppe in TikTok einsehen, indem Sie Ihr **Ads Manager:in Account** aufrufen und **Audiences** aus dem Dropdown-Menü **Assets** auswählen. Auf der Seite **Audience** sehen Sie die Größe jeder Zielgruppe, sobald sie &#126;1.000 erreicht hat.

![TikTok-Seite mit den folgenden Metriken für die angegebene Zielgruppe.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Überlegungen zur Nutzersynchronisierung und zu Rate-Limits {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Audience-Sync-Schritt erreichen, synchronisiert Braze sie nahezu in Echtzeit unter Berücksichtigung der Rate-Limits der TikTok-Marketing-API. Braze fasst alle 5 Sekunden so viele Nutzer:innen wie möglich in Batches zusammen und verarbeitet sie, bevor sie an TikTok gesendet werden.

Das Rate-Limit der TikTok-Segment-API erlaubt maximal 50 Abfragen pro Sekunde und 10.000 Nutzer:innen pro Anfrage. Wenn ein:e Kund:in dieses Limit erreicht, versucht Braze die Synchronisierung bis zu &#126;13 Stunden lang erneut. Wenn die Synchronisierung weiterhin nicht möglich ist, listet Braze diese Nutzer:innen unter der Metrik „Users Errored“ auf.

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience-Sync-Komponente besser zu verstehen.

| Metrik | Beschreibung |
| ------ | ----------- |
| Entered | Anzahl der Nutzer:innen, die diese Komponente betreten haben, um mit TikTok synchronisiert zu werden. |
| Proceeded to Next Step | Anzahl der Nutzer:innen, die zur nächsten Komponente vorgerückt sind, sofern eine vorhanden ist. Alle Nutzer:innen rücken automatisch vor, wenn dies der letzte Schritt im Canvas-Branch ist. |
| Users Synced | Anzahl der Nutzer:innen, die erfolgreich mit TikTok synchronisiert wurden. Beachten Sie, dass dies nicht der Anzahl der auf TikTok abgeglichenen Nutzer:innen entspricht. |
| Users Not Synced | Anzahl der Nutzer:innen, die aufgrund fehlender Abgleichsfelder nicht synchronisiert wurden. |
| Users Pending | Anzahl der Nutzer:innen, die derzeit von Braze verarbeitet werden, um mit TikTok synchronisiert zu werden. |
| Users Errored | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit TikTok synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges TikTok-Token oder eine auf TikTok gelöschte Zielgruppe sein. |
| Exited Canvas | Anzahl der Nutzer:innen, die das Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas eine Audience-Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

{% alert important %}
Beachten Sie, dass es bei den Metriken für synchronisierte Nutzer:innen und fehlerhafte Nutzer:innen zu Verzögerungen bei der Berichterstattung kommt – aufgrund des Bulk-Flushers bzw. der 13-stündigen Wiederholungsversuche.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was sollte ich tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Sie können Ihr TikTok-Konto auf der TikTok-Partnerseite trennen und erneut verbinden. Stellen Sie gemeinsam mit Ihrem TikTok Business Center-Admin sicher, dass Sie über die entsprechenden Berechtigungen für das Anzeigenkonto verfügen, das Sie synchronisieren möchten.

### Warum darf mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

Vergewissern Sie sich, dass Ihr TikTok-Konto auf der TikTok-Partnerseite erfolgreich mit Braze verbunden ist. Stellen Sie anschließend sicher, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und Felder zum Abgleich ausgewählt haben.

### Wie erfahre ich, ob Nutzer:innen nach der Übergabe an TikTok abgeglichen wurden? {#how-do-i-know-if-users-have-matched-after-passing-users-to-tiktok}

TikTok stellt diese Informationen aufgrund seiner Datenschutzrichtlinien nicht zur Verfügung.

### Wie lange dauert es, bis meine Zielgruppen in TikTok befüllt sind? {#how-long-will-it-take-for-my-audiences-to-populate-in-tiktok}

Die Zielgruppengröße wird innerhalb von 24–48 Stunden auf der Zielgruppenseite im TikTok Ads Manager:in aktualisiert.

### Wie viele Zielgruppen kann ich maximal in meinem TikTok-Anzeigenkonto haben? {#what-is-the-maximum-number-of-audiences-i-can-have-in-my-tiktok-ad-account}

Sie können bis zu 400 Zielgruppen pro TikTok-Anzeigenkonto haben.

### Warum ist meine Zielgruppengröße oder Übereinstimmungsrate in TikTok höher als die in Braze mit Audience Sync synchronisierten Nutzer:innen? {#why-is-my-audience-size-or-match-rate-in-tiktok-higher-than-the-users-synced-in-braze-with-audience-sync}

Das liegt daran, dass in TikTok eine ID mit mehreren TikTok-Nutzer:innen verknüpft sein kann. Dies tritt am häufigsten auf, wenn Clients mobile Werbe-IDs (iOS IDFA und Android GAID) verwenden, da auf einem Gerät mehrere TikTok-Nutzer:innen angemeldet sein können.

Darüber hinaus zählt TikTok auch Pangle-Nutzer:innen als abgeglichene Nutzer:innen, was in einigen Fällen zu einer erhöhten Übereinstimmungsrate führen kann. Wenn Sie die Zielgruppe jedoch für die Anzeigenauslieferung verwenden, ist die tatsächlich erreichbare Zielgruppengröße möglicherweise nicht so hoch wie die Anzahl der abgeglichenen Nutzer:innen, da sie von der Platzierung und anderen Einflussfaktoren abhängt.

### Warum erhalte ich eine E-Mail mit dem Betreff „Audience Does Not Exist For Canvas“? {#why-am-i-receiving-an-email-with-the-subject-audience-does-not-exist-for-canvas}

Dies kann auftreten, wenn die Zielgruppe, die Sie für die Synchronisierung ausgewählt haben, keine Streaming-Zielgruppe ist (z. B. wenn es sich um eine Lookalike-Zielgruppe oder eine Nutzer:innendatei-Zielgruppe handelt). Versuchen Sie, eine neue Zielgruppe über den Braze Audience Sync Canvas-Schritt zu erstellen.