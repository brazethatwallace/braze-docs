---
nav_title: Pinterest
article_title: Canvas-Zielgruppensynchronisierung mit Pinterest
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Audience Sync to Pinterest verwenden, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern."
page_order: 5
alias: "/audience_sync_pinterest/"

tool:
  - Canvas

---

# Audience Sync to Pinterest

Mit Braze Audience Sync to Pinterest können Marken wahlweise Nutzerdaten aus ihrer eigenen Braze-Integration zu Pinterest Audiences hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt zum Triggern einer Anzeige für diese Nutzer:innen in Ihren Pinterest Audiences verwendet werden.

**Zu den üblichen Anwendungsfällen für die Zielgruppensynchronisierung gehören:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit Pinterest geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro – Haftungsausschluss**<br>
Braze Audience Sync to Pinterest ist eine Audience Sync Pro-Integration. Für weitere Informationen zu dieser Integration wenden Sie sich bitte an Ihren Braze Account Manager:in.
{% endalert %}

## Voraussetzungen {#prerequisites}
Sie müssen sicherstellen, dass die folgenden Punkte erstellt, abgeschlossen und/oder akzeptiert wurden, bevor Sie Ihren Pinterest Audience-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Ein zentrales Tool zur Verwaltung der Pinterest-Assets Ihrer Marke (z. B. Werbekonten, Seiten, Apps). |
| Pinterest-Werbekonto | [Pinterest](https://ads.pinterest.com/) | Ein aktives Pinterest-Werbekonto, das mit dem Pinterest Business Hub Ihrer Marke verknüpft ist.<br><br>Stellen Sie sicher, dass Ihnen der Admin Ihres Pinterest Business Hub Admin-Berechtigungen für die Pinterest-Werbekonten erteilt hat, die Sie mit Braze verwenden möchten. |
| Pinterest-Bedingungen und -Richtlinien | Pinterest | Stimmen Sie der Einhaltung aller erforderlichen Bedingungen, Richtlinien, Leitlinien und Dokumentationen von Pinterest zu, die sich auf Ihre Nutzung von Pinterest Audience Sync beziehen, einschließlich aller darin durch Verweis einbezogenen Bedingungen, Richtlinien, Leitlinien und Dokumentationen, die unter anderem Folgendes umfassen können: die Nutzungsbedingungen, die geschäftlichen Nutzungsbedingungen, die Datenschutzrichtlinie, die Entwickler- und API-Nutzungsbedingungen, die Werbedatenbedingungen, die Werberichtlinien, die Werbedienstleistungsvereinbarung, die Community-Richtlinien und die Markenrichtlinien. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Mit Pinterest verbinden {#step-1-connect-to-pinterest}

{% alert important %}
Sie müssen die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) haben, um Pinterest mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Pinterest** aus. Wählen Sie unter Pinterest Audience Sync die Option **Connect Pinterest** aus.

![Pinterest-Technologieseite in Braze mit einem Übersichtsabschnitt und einem Abschnitt „Pinterest Audience Sync“ mit dem Button „Connect Pinterest“.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

Sie werden dann auf die Pinterest-OAuth-Seite weitergeleitet, um Braze für Ad Account Management und Audience Management zu autorisieren.

Nachdem Sie **Bestätigen** ausgewählt haben, werden Sie zurück zu Braze geleitet, um die Pinterest-Anzeigenkonten auszuwählen, die Sie synchronisieren möchten.

![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Pinterest verbinden können.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Wenn die Verbindung erfolgreich hergestellt wurde, kehren Sie zur Partnerseite zurück, wo Sie sehen können, welche Konten verbunden sind, und bestehende Konten trennen können.

![Eine aktualisierte Version der Pinterest-Technologiepartnerseite, auf der die erfolgreich verbundenen Anzeigenkonten angezeigt werden.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Ihre Pinterest-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr Pinterest-Administrator Sie aus Ihrem Pinterest Business Hub oder dem Zugriff auf die verbundenen Pinterest-Konten entfernt, erkennt Braze ein ungültiges Token / Textbaustein. Infolgedessen werden Ihre aktiven Canvases, die Pinterest Audience-Komponenten verwenden, Fehler anzeigen, und Braze wird die Nutzer:innen nicht synchronisieren können.

### Schritt 2: Einen Audience Sync-Schritt mit Pinterest hinzufügen {#step-2-add-an-audience-sync-step-with-pinterest}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Audience Sync**.

![Canvas-Schrittauswahl mit der Option „Audience Sync“-Komponente.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Audience Sync-Komponentenkarte, die einem Canvas-Pfad hinzugefügt wurde.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung {#step-3-sync-setup}

Klicken Sie auf den Button **Custom Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **Pinterest** als gewünschten Audience Sync-Partner aus.

![Audience Sync-Komponenteneditor mit Pinterest als ausgewähltem Sync-Partner.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie dann Ihr gewünschtes Pinterest-Anzeigenkonto aus. Geben Sie im Dropdown **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Add Users to Audience** und wählen Sie aus, welche Felder Sie mit Pinterest synchronisieren möchten. Speichern Sie anschließend Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Create Audience** klicken.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier wird das gewünschte Anzeigenkonto ausgewählt und eine neue Zielgruppe erstellt.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Braze zeigt oben im Schritteditor eine Benachrichtigung an, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um später in der Canvas-Journey Nutzer:innen zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Ein Hinweis, der erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie den Audience Sync-Schritt erreichen.
{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}
**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden Pinterest-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen auf dem neuesten Stand sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe im Dropdown ein und fügen Sie sie hinzu. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie den Audience Sync-Schritt erreichen.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten {#step-4-launch-canvas}

Sobald Sie Ihre Audience Sync to Pinterest konfiguriert haben, starten Sie das Canvas! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Audience Sync-Schritt durchlaufen, werden in diese Zielgruppe auf Pinterest übertragen. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangebracht.

Sie können die Zielgruppe auf Pinterest einsehen, indem Sie sich in Ihrem Ads-Manager:in-Konto anmelden und im Ads-Dropdown **Audiences** auswählen. Auf der Audience-Seite sehen Sie die Größe jeder Zielgruppe, sobald sie ~100 erreicht hat.

![Zielgruppendetails für eine bestimmte Pinterest-Zielgruppe, einschließlich Zielgruppenname, Zielgruppen-ID, Zielgruppentyp und Zielgruppengröße.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Synchronisierung von Nutzer:innen und Rate-Limit-Überlegungen {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Audience-Sync-Schritt erreichen, synchronisiert Braze sie nahezu in Echtzeit und berücksichtigt dabei die Rate-Limits der Pinterest Marketing API. Braze fasst so viele Nutzer:innen wie möglich in Batches zusammen und verarbeitet sie alle 5 Sekunden, bevor sie an Pinterest gesendet werden.

Das Rate-Limit der Pinterest Segment API erlaubt nicht mehr als sieben Anfragen pro Sekunde pro Nutzer:in und 1.900 Nutzer:innen pro Anfrage. Wenn ein:e Kund:in dieses Limit erreicht, versucht Braze die Synchronisierung bis zu ca. 13 Stunden lang erneut. Wenn die Synchronisierung weiterhin nicht möglich ist, listet Braze diese Nutzer:innen unter der Metrik „Users Errored“ auf.

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience-Sync-Komponente besser zu verstehen.

| Metrik | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente betreten haben, um mit Pinterest synchronisiert zu werden. |
| Zum nächsten Schritt fortgefahren | Wie viele Nutzer:innen sind zur nächsten Komponente weitergegangen, falls eine vorhanden ist? Alle Nutzer:innen fahren automatisch fort, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die erfolgreich mit Pinterest synchronisiert wurden. |
| Nicht synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund fehlender Abgleichsfelder nicht synchronisiert wurden. |
| Ausstehende Nutzer:innen | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Pinterest verarbeitet werden. |
| Fehlerhafte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Pinterest synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Pinterest-Token / Textbaustein oder eine auf Pinterest gelöschte Zielgruppe sein. |
| Canvas verlassen | Anzahl der Nutzer:innen, die das Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas eine Audience-Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

{% alert important %}
Beachten Sie, dass es bei der Berichterstattung zu Verzögerungen bei synchronisierten Nutzer:innen und Fehlermetriken kommt – aufgrund des Bulk-Flushers bzw. der 13-stündigen Wiederholungsversuche.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert es, bis meine Zielgruppen in Pinterest befüllt sind? {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

Die Zielgruppengröße wird innerhalb von 24–48 Stunden auf der Seite **Audiences** im Ads Manager:in von Pinterest aktualisiert.

### Wie erfahre ich, ob Nutzer:innen nach der Übergabe an Pinterest zugeordnet wurden? {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

Pinterest stellt diese Informationen aufgrund eigener Datenschutzrichtlinien nicht zur Verfügung.

### Was sollte ich tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Bestätigen Sie mit dem Admin Ihres Pinterest Business Hub, dass Sie über die entsprechenden Berechtigungen für das Werbekonto verfügen, das Sie synchronisieren möchten. Sie können Ihr Pinterest-Konto auch auf der Pinterest-Partnerseite trennen und erneut verbinden.

### Warum darf mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

Stellen Sie sicher, dass Ihr Pinterest-Konto auf der Pinterest-Partnerseite erfolgreich mit Braze verbunden ist. Vergewissern Sie sich, dass Sie ein Werbekonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und Felder zum Abgleich ausgewählt haben.

### Warum kann ich mein Werbekonto für meinen Audience-Sync-Schritt nicht auswählen? {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

Überprüfen Sie, ob Ihr Token / Textbaustein mit den richtigen Kontoberechtigungen generiert wurde. Beachten Sie, dass bei zu vielen Zielgruppen in Ihrem Pinterest-Werbekonto das Dropdown zur Auswahl Ihres Werbekontos möglicherweise eine Zeitüberschreitung verursacht. In diesem Fall empfehlen wir, die Anzahl der Zielgruppen in Ihrem Werbekonto zu reduzieren.