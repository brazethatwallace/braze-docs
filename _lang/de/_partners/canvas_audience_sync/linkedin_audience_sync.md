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

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## Voraussetzungen {#prerequisites}

Sie müssen sicherstellen, dass die folgenden Punkte erstellt, abgeschlossen oder akzeptiert wurden, bevor Sie Ihren LinkedIn Audience Sync-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| --- | --- | --- |
| LinkedIn-Werbekonto | [LinkedIn](https://www.linkedin.com/campaignmanager) | Ein aktives LinkedIn-Werbekonto, das mit Ihrer Marke verknüpft ist.<br><br>Stellen Sie sicher, dass Sie alle relevanten LinkedIn-Geschäftsbedingungen akzeptiert haben, um auf dieses Konto zuzugreifen und es zu nutzen, und dass Ihr LinkedIn-Administrator Ihnen die entsprechenden Berechtigungen zur Verwaltung von Zielgruppen erteilt hat. |
| LinkedIn-Nutzungsbedingungen und -Richtlinien | LinkedIn | Stimmen Sie zu, alle erforderlichen Nutzungsbedingungen, Richtlinien, Leitlinien und Dokumentationen von LinkedIn einzuhalten, die sich auf Ihre Nutzung des LinkedIn Audience Sync beziehen, einschließlich aller darin durch Verweis einbezogenen Nutzungsbedingungen, Richtlinien, Leitlinien und Dokumentationen, wie z. B. die LinkedIn-Servicebedingungen, die Werbevereinbarung, die Datenverarbeitungsvereinbarung und die Richtlinien für die professionelle Community. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Mit LinkedIn verbinden {#step-1-connect-to-linkedin}

{% alert important %}
Sie müssen die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) haben, um LinkedIn mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Technologie-Partner** und wählen Sie **LinkedIn** aus. Wählen Sie im Bereich **LinkedIn Audience Sync** die Option **Connect LinkedIn** aus.

![Die LinkedIn-Technologieseite in Braze enthält einen Übersichtsbereich und einen Bereich „LinkedIn Audience Sync“ mit dem Button „Connected LinkedIn“.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Sie werden dann auf die LinkedIn-OAuth-Seite weitergeleitet, um Braze für die Berechtigungen im Zusammenhang mit Ihrer Audience Sync-Integration zu autorisieren. Nachdem Sie **Bestätigen** gewählt haben, werden Sie zurück zu Braze geleitet, um auszuwählen, mit welchen LinkedIn-Anzeigenkonten Sie synchronisieren möchten.

![„Braze Self Service“ ist als das zu verbindende Anzeigenkonto ausgewählt.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Sobald Sie sich erfolgreich verbunden haben, werden Sie auf die Partnerseite zurückgebracht, wo Sie sehen können, welche Konten verbunden sind, und bestehende Konten trennen können.

![Ein erfolgreich verbundenes LinkedIn-Konto.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Ihre LinkedIn-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr LinkedIn-Administrator Sie aus Ihrem LinkedIn-Anzeigenkonto entfernt, erkennt Braze ein ungültiges Token / Textbaustein. Dies hat zur Folge, dass Ihre aktiven Canvases, die LinkedIn verwenden, Fehler anzeigen und Braze nicht in der Lage ist, Nutzer:innen zu synchronisieren.

### Schritt 2: Canvas-Eingangskriterien konfigurieren {#step-2-configure-your-canvas-entry-criteria}

Beim Aufbau von Zielgruppen für das Ad Tracking möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen und Datenschutzgesetze einhalten, wie z. B. das Recht „Nicht verkaufen oder weitergeben“ gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen.

Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection) erfasst haben, können Sie den Filter **Ads Tracking Enabled** verwenden. Wählen Sie den Wert `true` aus, um Nutzer:innen nur in Audience Sync-Ziele zu senden, für die sie ein Opt-in gesetzt haben.

![Eine Entry-Zielgruppe mit dem Filter „Ad Tracking Enabled ist true“.]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante angepasste Attribute erfassen, sollten Sie diese in Ihre Canvas-Eingangskriterien als Filter einbeziehen:

![Ein Canvas mit einer Entry-Zielgruppe, bei der „opted_in_marketing“ gleich „true“ ist.]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance).

### Schritt 3: Einen Audience Sync-Schritt mit LinkedIn hinzufügen {#step-3-add-an-audience-sync-step-with-linkedin}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie Audience Sync. Klicken Sie auf den Button **Custom Audience**, um den Komponenteneditor zu öffnen.

![Der Canvas-Editor mit der Liste der verfügbaren Komponenten.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![Die ausgewählte Audience Sync-Komponente.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Schritt 4: Sync-Einrichtung {#step-4-sync-setup}

Wählen Sie **LinkedIn** als den gewünschten Audience Sync-Partner aus.

![Die Details zu „Audience Sync einrichten“ mit den verschiedenen Partnern zur Auswahl.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Wählen Sie dann das gewünschte LinkedIn-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

![Audience Sync mit LinkedIn, wobei Braze als Anzeigenkonto ausgewählt ist.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

**Eine neue Zielgruppe erstellen**<br>
Geben Sie einen Namen für die neue Zielgruppe ein, wählen Sie **Add Users to Audience** und wählen Sie aus, welche Felder Sie mit LinkedIn synchronisieren möchten. Für diese Integration unterstützen wir derzeit Folgendes:
- E-Mail
- Vor- und Nachname
- Android-GAID

Speichern Sie anschließend Ihre Zielgruppe, indem Sie unten im Schritteditor auf den Button **Create Audience** klicken.

![Ein Beispiel für eine „Leads“-Zielgruppe mit dem ausgewählten Braze-Anzeigenkonto, der „Leads“-Zielgruppe, der Aktion zum Hinzufügen von Nutzer:innen zur Zielgruppe und E-Mail, Android-GAID sowie Vor- und Nachname als abzugleichende Felder.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze zeigt am oberen Rand des Schritteditors eine Benachrichtigung an, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um Nutzer:innen später in der Canvas-Journey zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Bestätigung, dass die „Leads“-Zielgruppe erstellt wurde.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, synchronisiert Braze die Nutzer:innen nahezu in Realtime, sobald sie die Audience Sync-Komponente betreten.

{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}

**Mit einer bestehenden Zielgruppe synchronisieren**<br>
Braze bietet auch die Möglichkeit, Nutzer:innen zu bestehenden LinkedIn-Zielgruppen hinzuzufügen, um sicherzustellen, dass diese Zielgruppen aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und wählen Sie **Add to the Audience**. Braze fügt dann Nutzer:innen nahezu in Realtime hinzu, sobald sie die Audience Sync-Komponente betreten.

![Erweiterte Ansicht des Custom Audience Canvas-Schrittes. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten {#step-5-launch-canvas}

Sobald Sie Ihre Audience Sync mit LinkedIn konfiguriert haben, starten Sie das Canvas! Die neue Zielgruppe wird erstellt, und Nutzer:innen, die den Audience Sync-Schritt durchlaufen, werden in diese Zielgruppe auf LinkedIn weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vorangebracht.

Sie können die Zielgruppe auf LinkedIn einsehen, indem Sie in Ihr Anzeigenkonto gehen und **Audiences** unter dem Abschnitt **Assets** in der Navigation auswählen. Auf der Seite **Audiences** können Sie die Größe jeder Zielgruppe sehen, sobald sie mehr als 300 Mitglieder erreicht hat.

![LinkedIn-Seite mit den folgenden Metriken für die angegebene Zielgruppe.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Synchronisierung von Nutzer:innen und Rate-Limit-Überlegungen {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Audience-Sync-Schritt erreichen, synchronisiert Braze sie nahezu in Echtzeit und berücksichtigt dabei die API-Rate-Limits von LinkedIn. Braze fasst so viele Nutzer:innen wie möglich in Batches zusammen und verarbeitet sie alle 5 Sekunden, bevor sie an LinkedIn gesendet werden.

Das API-Rate-Limit von LinkedIn erlaubt nicht mehr als zehn Anfragen pro Sekunde und 100.000 Nutzer:innen pro Anfrage. Wenn ein:e Kund:in dieses Limit erreicht, versucht Braze die Synchronisierung bis zu etwa 13 Stunden lang erneut. Wenn die Synchronisierung weiterhin nicht möglich ist, listet Braze diese Nutzer:innen unter der Metrik „Users Errored“ auf.

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience-Sync-Komponente besser zu verstehen.

| METRIK | BESCHREIBUNG |
| ------ | ----------- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente betreten haben, um mit LinkedIn synchronisiert zu werden. |
| Zum nächsten Schritt fortgefahren | Wie viele Nutzer:innen sind zur nächsten Komponente weitergegangen, falls eine vorhanden ist? Alle Nutzer:innen werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Branch ist. |
| Synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die erfolgreich mit LinkedIn synchronisiert wurden. |
| Nicht synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund fehlender Abgleichfelder nicht synchronisiert wurden. |
| Ausstehende Nutzer:innen | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit LinkedIn verarbeitet werden. |
| Fehlerhafte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit LinkedIn synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges LinkedIn-Token / Textbaustein oder eine auf LinkedIn gelöschte Zielgruppe sein. |
| Canvas verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas eine Audience-Sync-Komponente ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

{% alert important %}
Beachten Sie, dass es bei den Metriken für synchronisierte Nutzer:innen und fehlerhafte Nutzer:innen zu Verzögerungen bei der Berichterstattung kommt, bedingt durch den Bulk-Flusher bzw. die 13-stündige Wiederholungsphase.
{% endalert %}

{% alert important %}
LinkedIn stellt zusätzliche Metriken zu Übereinstimmungsraten innerhalb ihrer Plattform bereit. Um die Übereinstimmung Ihrer spezifischen Audience Sync zu überprüfen, wählen Sie die Metriken des Audience-Sync-Schritts aus, um zur Seite **Canvas-Schrittdetails** zu gelangen.
<br><br>
Wählen Sie den Partner als **LinkedIn**, Ihr Werbekonto und die Zielgruppe aus, um die Zielgruppengröße und Übereinstimmungsrate von LinkedIn zu sehen.

![Ein Beispiel für Audience-Sync-Schrittmetriken mit 10.000 eingetretenen Nutzer:innen.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert es, bis die Zielgruppengrößen in LinkedIn angezeigt werden? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Es kann bis zu 48 Stunden dauern, bis die Zielgruppen in Ihrem LinkedIn-Konto angezeigt werden.

### Welche Mindestzielgruppengröße ist erforderlich, damit LinkedIn die Zielgruppengröße in Ihrem Werbekonto anzeigt? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

Die Zielgruppe muss mindestens 300 Mitglieder umfassen, damit die Zielgruppengröße in Ihrem LinkedIn-Konto angezeigt wird.

### Was sollte ich tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Sie können Ihr LinkedIn-Konto auf der LinkedIn-Partnerseite trennen und erneut verbinden. Bestätigen Sie mit Ihrem LinkedIn-Administrator, dass Sie über die entsprechenden Berechtigungen für das Werbekonto verfügen, mit dem Sie synchronisieren möchten.

### Warum darf mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

Vergewissern Sie sich, dass Ihr LinkedIn-Werbekonto auf der LinkedIn-Partnerseite erfolgreich mit Braze verbunden wurde. Stellen Sie außerdem sicher, dass Sie ein Werbekonto ausgewählt, einen Namen für die neue Zielgruppe eingegeben und Felder zum Abgleich ausgewählt haben.

### Wie erfahre ich, ob Nutzer:innen nach der Übergabe an LinkedIn abgeglichen wurden? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn stellt Informationen zu Übereinstimmungsraten in ihrem Dashboard bereit. Sie können diese auf LinkedIn im Bereich **Audiences** einsehen. Sie können die Übereinstimmungsrate für Ihre LinkedIn-Zielgruppe in den Canvas-Schritt-Details Ihres Audience-Sync-Schritts überprüfen.

### Wie viele Zielgruppen kann LinkedIn unterstützen? {#how-many-audiences-can-linkedin-support}

Derzeit gibt es keine Begrenzung für die Anzahl der Zielgruppen in Ihrem LinkedIn-Werbekonto.

### Warum bleibt ein Segment im Status BUILDING hängen und wird nicht aktualisiert? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Ein Segment gilt als ungenutzt und wird auf ARCHIVED gesetzt, wenn es 30 Tage lang nicht kontinuierlich in einer Entwurfs- oder aktiven Campaign verwendet wird. Aus diesem Grund kann ein Segment im Status BUILDING „hängen bleiben“, wenn Aktualisierungen an ein archiviertes (ARCHIVED) Segment gestreamt werden, wodurch es in den Status BUILDING versetzt wird, und kurz bevor es erneut archiviert wird, neue Aktualisierungen an das ungenutzte Segment gestreamt werden.