---
nav_title: Snapchat
article_title: Canvas Audience Sync mit Snapchat
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync mit Snapchat verwenden, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern."
page_order: 6
alias: "/audience_sync_snapchat/"

tool:
  - Canvas

---

# Audience Sync mit Snapchat {#audience-sync-to-snapchat}

Mit Braze Audience Sync mit Snapchat können Marken Nutzerdaten aus ihrer Braze-Integration zu Snapchat-Kundenlisten hinzufügen, um Werbung auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt verwendet werden, um eine Anzeige für diese Nutzer:innen in Ihren Snapchat-Kundenlisten zu triggern.

**Zu den üblichen Anwendungsfällen für die Synchronisierung von Zielgruppen gehören:**

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten
- Erstellen ähnlicher Zielgruppen zur effizienteren Gewinnung neuer Nutzer:innen

Mit diesem Feature können Nutzer:innen kontrollieren, welche spezifischen First-Party-Daten mit Snapchat geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro – Haftungsausschluss**<br>
Braze Audience Sync mit Snapchat ist eine Audience Sync Pro-Integration. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager.
{% endalert %}

## Voraussetzungen {#prerequisites}

Sie müssen sicherstellen, dass die folgenden Punkte erstellt, abgeschlossen und/oder akzeptiert wurden, bevor Sie Ihren Snapchat-Zielgruppen-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | Ein zentrales Tool zur Verwaltung der Snapchat-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten, Apps). |
| Snapchat-Anzeigenkonto | Snapchat | Ein aktives Snapchat-Anzeigenkonto, das mit dem Snapchat Business Manager Ihrer Marke verknüpft ist.<br><br>Vergewissern Sie sich, dass Ihr Snapchat Business Manager-Admin Ihnen Administratorrechte für die Snapchat-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. |
| Snapchat-Bedingungen und -Richtlinien | [Snapchat](https://www.snap.com/en-US/policies) | Sie erklären sich damit einverstanden, alle erforderlichen Bedingungen, Richtlinien, Leitlinien und Dokumentationen von Snapchat in Bezug auf Ihre Nutzung von Snapchat Audience Sync einzuhalten, einschließlich aller Bedingungen, Richtlinien, Leitlinien und Dokumentationen, auf die darin verwiesen wird, wie z. B. die Allgemeinen Geschäftsbedingungen, die Geschäftsbedingungen für Serviceleistungen, die Entwicklerbedingungen, Audience Match, die Werberichtlinien, die Richtlinien für kommerzielle Inhalte, die Community-Richtlinien und die Verantwortung der Anbieter. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### 1. Schritt: Mit Snapchat verbinden {#step-1-connect-to-snapchat}

{% alert important %}
Sie müssen die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) haben, um Snapchat mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Snapchat** aus. Wählen Sie unter Snapchat Audience Sync die Option **Connect Snapchat** aus.

![Snapchat-Technologieseite in Braze mit einem Übersichtsabschnitt und einem Snapchat Audience Sync-Abschnitt mit dem Button „Connect Snapchat“.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

Sie werden dann auf die Snapchat-OAuth-Seite weitergeleitet, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync-Integration zu autorisieren.

Sobald Sie „Bestätigen“ gewählt haben, werden Sie zurück zu Braze geleitet, um die Snapchat-Anzeigenkonten auszuwählen, die Sie synchronisieren möchten.

![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Snapchat verbinden können.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Nach erfolgreicher Verbindung kehren Sie zur Partnerseite zurück, wo Sie sehen können, welche Konten verbunden sind, und bestehende Konten trennen können.

![Eine aktualisierte Version der Snapchat-Technologie-Partnerseite, auf der die erfolgreich verbundenen Anzeigenkonten angezeigt werden.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Ihre Snapchat-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr Snapchat-Admin Sie aus Ihrem Snapchat Business Manager oder dem Zugriff auf die verbundenen Snapchat-Anzeigenkonten entfernt, erkennt Braze ein ungültiges Token. Dies hat zur Folge, dass Ihre aktiven Canvases, die Snapchat verwenden, Fehler anzeigen und Braze nicht in der Lage ist, Nutzer:innen zu synchronisieren.

### 2. Schritt: Einen Audience Sync-Schritt mit Snapchat hinzufügen {#step-2-add-an-audience-sync-step-with-snapchat}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3. Schritt: Sync-Einrichtung {#step-3-sync-setup}

Klicken Sie auf den Button **Custom Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **Snapchat** als den gewünschten Audience Sync-Partner aus.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie dann Ihr gewünschtes Snapchat-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Add Users to Audience** und wählen Sie aus, welche Felder Sie mit Snapchat synchronisieren möchten. Speichern Sie anschließend Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Create Audience** klicken.

![Erweiterte Ansicht des Canvas-Schrittes „Custom Audience“. Hier wird das gewünschte Anzeigenkonto ausgewählt und eine neue Zielgruppe erstellt.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Braze zeigt am oberen Rand des Schritteditors eine Benachrichtigung an, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um Nutzer:innen später in der Canvas-Journey zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Ein Hinweis, der erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie die Audience Sync-Komponente betreten.

{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}
**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden Snapchat-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und wählen Sie **Add to the Audience**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Canvas-Schrittes „Custom Audience“. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### 4. Schritt: Canvas starten {#step-4-launch-canvas}

Sobald Sie Ihre Audience Sync mit Snapchat konfiguriert haben, starten Sie das Canvas! Es wird eine neue Zielgruppe erstellt, und Nutzer:innen, die den Audience Sync-Schritt durchlaufen, werden in diese Zielgruppe auf Snapchat übertragen. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangebracht.

Sie können die Zielgruppen in Snapchat einsehen, indem Sie Ihr Ads-Manager-Konto aufrufen und im Navigationsbereich „Assets“ die Option **Audiences** auswählen. Auf der Seite **Audiences** können Sie die Größe jeder Zielgruppe sehen, sobald sie ~1.000 erreicht hat.

![Details zur Zielgruppe einer bestimmten Snapchat-Zielgruppe, einschließlich Name der Zielgruppe, Art der Zielgruppe, Größe der Zielgruppe und Bindung der Zielgruppe in Tagen.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, synchronisiert Braze sie nahezu in Realtime und respektiert dabei die Rate-Limits der Snapchat-API. Braze stapelt und verarbeitet alle 5 Sekunden so viele Nutzer:innen wie möglich, bevor es sie an Snapchat sendet.

Das Rate-Limit der Snapchat-API erlaubt nicht mehr als zehn Abfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Erreicht eine Kund:in dieses Limit, wiederholt Braze die Synchronisierung für bis zu ~13 Stunden. Wenn die Synchronisierung immer noch nicht möglich ist, listet Braze diese Nutzer:innen in der Metrik „Fehlerhafte Nutzer:innen“ auf.

### Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrik | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente betreten haben, um mit Snapchat synchronisiert zu werden. |
| Zum nächsten Schritt fortgefahren | Wie viele Nutzer:innen sind zur nächsten Komponente weitergegangen, falls eine vorhanden ist? Alle Nutzer:innen werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit Snapchat synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Snapchat verarbeitet werden. |
| Fehlerhafte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Snapchat synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Snapchat-Token oder eine auf Snapchat gelöschte Zielgruppe sein. |
| Canvas verlassen | Anzahl der Nutzer:innen, die das Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas eine Audience Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk-Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei der Berichterstattung über synchronisierte Nutzer:innen und fehlerhafte Metriken kommen wird.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie viele Zielgruppen kann Snapchat unterstützen? {#how-many-audiences-can-snapchat-support}

Zurzeit können Sie nur 1.000 Zielgruppen in Ihrem Snapchat-Konto haben.

Wenn Sie dieses Limit überschreiten, wird Braze Sie darüber informieren, dass keine neuen Zielgruppen erstellt werden können. Sie müssen Zielgruppen, die Sie nicht mehr verwenden, aus Ihrem Snapchat-Anzeigenkonto entfernen.

### Woher weiß ich, ob Nutzer:innen übereinstimmen, nachdem ich Nutzer:innen an Snapchat übergeben habe? {#how-do-i-know-if-users-have-matched-after-passing-users-to-snapchat}

Snapchat stellt diese Informationen aufgrund seiner Datenschutzrichtlinien nicht zur Verfügung.

### Was sollte ich als Nächstes tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Sie können die Verbindung zu Ihrem Snapchat-Konto auf der Snapchat-Partnerseite trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Snapchat Business Manager-Admin, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.

### Warum darf mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

Stellen Sie sicher, dass Ihr Snapchat-Anzeigenkonto auf der Snapchat-Partnerseite erfolgreich mit Braze verbunden ist. Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und die passenden Felder ausgewählt haben.