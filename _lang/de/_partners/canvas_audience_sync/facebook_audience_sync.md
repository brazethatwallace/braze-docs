---
nav_title: Facebook
article_title: Canvas Audience Sync mit Facebook
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Audience Sync mit Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr auszuliefern."
page_order: 2
alias: /audience_sync_facebook/

tool:
  - Canvas

---

# Audience Sync mit Facebook {#audience-sync-to-facebook}

> Mit Braze Audience Sync mit Facebook können Sie die Daten Ihrer Nutzer:innen aus Ihrer Braze-Integration zu angepassten Facebook-Zielgruppen hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern.

Alle Kriterien, die Sie normalerweise verwenden, um eine Nachricht (Push, E-Mail, SMS oder Webhook) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten auszulösen, können jetzt verwendet werden, um mit angepassten Zielgruppen eine Anzeige für diese Nutzer:innen in Facebook auszulösen. Wenn Sie beispielsweise eine Audience Sync mit Facebook konfigurieren, können Sie eine Vielzahl von First-Party-Feldern wie E-Mail, Telefon, Vorname und Nachname verwenden.

**Zu den häufigen Anwendungsfällen für die Synchronisierung angepasster Zielgruppen gehören**:

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern.
- Retargeting von Nutzer:innen, die auf andere Marketingkanäle weniger responsiv sind.
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer:innen Werbung erhalten, wenn sie bereits treue Verbraucher:innen Ihrer Marke sind.
- Erstellen von Lookalike-Zielgruppen, um neue Nutzer:innen effizienter zu gewinnen.

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit Facebook geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

## Synchronisierung von Nutzer:innen und Rate-Limit-Überlegungen {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Audience Sync-Schritt erreichen, synchronisiert Braze sie nahezu in Echtzeit und berücksichtigt dabei die Rate-Limits der Facebook Marketing API. Braze fasst so viele Nutzer:innen wie möglich in Batches zusammen und verarbeitet sie alle 5 Sekunden, bevor sie an Facebook gesendet werden.

Das Rate-Limit der Facebook Marketing API erlaubt nicht mehr als &#126;190.000 API-Anfragen pro Werbekonto in einem Zeitraum von einer Stunde. Wenn ein:e Kund:in dieses Limit erreicht, versucht Braze die Synchronisierung bis zu &#126;13 Stunden lang erneut. Wenn die Synchronisierung dann immer noch nicht möglich ist, listet Braze diese Nutzer:innen unter der Metrik „Users Errored“ auf.

## Voraussetzungen {#prerequisites}

Sie müssen sicherstellen, dass die folgenden Elemente erstellt und abgeschlossen sind, bevor Sie Ihren Facebook Audience-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z. B. Werbekonten, Seiten und Apps). |
| Facebook-Werbekonto | [Facebook](https://www.facebook.com/business/help/910137316041095) | Ein aktives Facebook-Werbekonto, das mit dem Business Manager Ihrer Marke verknüpft ist.<br><br>Stellen Sie sicher, dass Ihr Facebook Business Manager-Admin Ihnen entweder die Berechtigung „Manage Campaigns“ oder „Manage ad accounts“ für die Facebook-Werbekonten erteilt hat, die Sie mit Braze verwenden möchten. Stellen Sie außerdem sicher, dass Sie die Geschäftsbedingungen Ihres Werbekontos akzeptiert haben. |
| Facebook Custom Audiences-Nutzungsbedingungen | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Akzeptieren Sie die Facebook Custom Audiences-Nutzungsbedingungen für Ihre Facebook-Werbekonten, die Sie mit Braze verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Mit Facebook verbinden {#step-1-connect-to-facebook}

{% alert important %}
Sie müssen die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) haben, um Facebook mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Facebook** aus. Wählen Sie unter Facebook Audience Export die Option **Connect Facebook**.

![Facebook-Technologieseite in Braze mit einem Übersichtsabschnitt und einem Abschnitt für den Facebook Audience Export mit dem Button „Connect Facebook“.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Ein Facebook-oAuth-Dialogfenster erscheint, um Braze zu autorisieren, angepasste Zielgruppen in Ihren Facebook-Anzeigenkonten zu erstellen.

![Das erste Facebook-Dialogfeld mit der Aufforderung „Verbinden als X“, wobei X Ihr Facebook-Benutzername ist.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![Das zweite Facebook-Dialogfeld, in dem Sie um die Erlaubnis gebeten werden, Anzeigen für Ihre Anzeigenkonten zu verwalten.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Nachdem Sie Braze mit Ihrem Facebook-Konto verknüpft haben, wählen Sie die Anzeigenkonten aus, die Sie in Ihrem Braze-Workspace synchronisieren möchten. Wenn Sie verbunden sind, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind, und bestehende Konten trennen können.

![Eine aktualisierte Version der Facebook-Technologie-Partnerseite, auf der die erfolgreich verbundenen Anzeigenkonten angezeigt werden.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Ihre Facebook-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr Facebook-Administrator Sie von Ihrem Facebook Business Manager oder dem Zugriff auf die verbundenen Facebook-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die Facebook-Audience-Komponenten verwenden, Fehler anzeigen, und Braze kann die Nutzer:innen nicht synchronisieren.

{% alert important %}
Für Kund:innen, die zuvor den Facebook-App-Review-Prozess für [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) und [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) durchlaufen haben, ist Ihr System User Token weiterhin für die Facebook-Audience-Komponente gültig. Sie können das Facebook System User Token nicht über die Facebook-Partnerseite bearbeiten oder widerrufen. Stattdessen können Sie Ihr Facebook-Konto verbinden, um Ihr Facebook System User Token innerhalb Ihres Braze-Workspace zu ersetzen.

<br><br>Die Facebook-oAuth-Konfiguration gilt auch für [Facebook-Exporte mit Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Schritt 2: Bedingungen für angepasste Zielgruppen akzeptieren {#step-2-accept-custom-audiences-terms-of-service}

Bevor Sie Ihr Canvas einrichten, müssen Sie die folgenden Facebook-Nutzungsbedingungen unter den folgenden Links akzeptieren:

- **Kundenliste – Bedingungen für angepasste Zielgruppen für Ihr persönliches Konto:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Facebook Business Tools – Bedingungen für Ihr Geschäftskonto:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Ein Beispiel für die Bedingungen, die für angepasste Kundenlisten-Zielgruppen akzeptiert werden müssen.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Ein Beispiel für die Bedingungen, die für Facebook Business Tools akzeptiert werden müssen.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Weitere Einzelheiten zur Überprüfung Ihres Facebook-Kontos bei der Integration finden Sie im [FAQ-Abschnitt](#terms).

### Schritt 3: Facebook-Audience-Komponente in Canvas hinzufügen {#step-3-add-a-facebook-audience-component-in-canvas}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Facebook Audience** aus.

![Eine Liste von Komponenten, die dem Canvas hinzugefügt werden können.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Die Audience-Sync-Komponente.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 4: Sync-Einrichtung {#step-4-sync-setup}

Wählen Sie den Button **Custom Audience** aus, um den Komponenteneditor zu öffnen. Wählen Sie dann **Facebook** als Audience-Sync-Partner aus.

![„Audience Sync einrichten“ mit Optionen zur Auswahl eines Partners.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie das gewünschte Facebook-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Neue Zielgruppe erstellen %}

1. Geben Sie einen Namen für die neue angepasste Zielgruppe ein.
2. Wählen Sie **Add Users to Audience** und wählen Sie die Felder aus, die Sie mit Facebook synchronisieren möchten.
3. Wählen Sie dann **Create Audience**, um Ihre Zielgruppe zu speichern.

![Audience-Sync-Einrichtung für eine Zielgruppe mit den passenden Informationen zu E-Mail, Telefon, Vorname und Nachname.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Sie werden oben im Schritt-Editor benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn während dieses Vorgangs ein Fehler auftritt. Sie können diese Zielgruppe auch referenzieren, wenn Nutzer:innen später in der Canvas-Journey entfernt werden, da die Zielgruppe im Entwurfsmodus erstellt wurde.

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, erstellt Braze die neue angepasste Zielgruppe beim Start des Canvas und synchronisiert die Nutzer:innen anschließend nahezu in Realtime, wenn sie den Audience-Sync-Schritt betreten.

Jeder Audience-Sync-Schritt ist der Facebook-Zielgruppe zugeordnet, die in diesem Schritt konfiguriert wurde. Wenn das Canvas erneut ausgeführt wird (z. B. nach einem wiederkehrenden Zeitplan), synchronisiert Braze berechtigte Nutzer:innen mit derselben Zielgruppe – es wird nicht bei jedem Canvas-Durchlauf eine neue Facebook-Zielgruppe erstellt.

{% endtab %}
{% tab Mit bestehender Zielgruppe synchronisieren %}

Braze bietet die Möglichkeit, Nutzer:innen aus bestehenden angepassten Facebook-Zielgruppen hinzuzufügen oder zu entfernen, um sicherzustellen, dass diese Zielgruppen aktuell sind. Um mit einer bestehenden Zielgruppe zu synchronisieren, gehen Sie wie folgt vor:

1. Geben Sie den Namen der bestehenden Zielgruppe in die Dropdown-Liste ein.
2. Wählen Sie, ob Sie **Add to the Audience** oder **Remove from the Audience** möchten.
3. Braze fügt Nutzer:innen nahezu in Realtime hinzu oder entfernt sie, sobald sie den Facebook-Audience-Schritt betreten.

![Audience-Sync-Einrichtung zum Entfernen der Informationen zu E-Mail, Telefon, Vorname und Nachname.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook verbietet es, Nutzer:innen aus angepassten Zielgruppen zu entfernen, wenn die Zielgruppengröße zu klein ist (in der Regel weniger als 1.000 Nutzer:innen). Infolgedessen ist Braze nicht in der Lage, Nutzer:innen für eine Entfernung aus dem Audience-Sync-Schritt zu synchronisieren, bis die Zielgruppe die entsprechende Größe erreicht hat.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten {#step-5-launch-canvas}

Nachdem Sie Ihre Facebook-Audience-Komponente konfiguriert haben, ist es an der Zeit, das Canvas zu starten! Die neue angepasste Zielgruppe wird erstellt, und Nutzer:innen, die den Facebook-Audience-Schritt durchlaufen, werden in diese angepasste Zielgruppe auf Facebook weitergeleitet. Wenn Ihr Canvas nachfolgende Schritte enthält, rücken Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey vor.

Der Tab **History** der angepassten Zielgruppe im Facebook Audience Manager zeigt die Anzahl der Nutzer:innen an, die von Braze an die Zielgruppe gesendet wurden. Wenn Nutzer:innen den Schritt erneut betreten, werden sie erneut an Facebook gesendet.

![Zielgruppendetails und der Tab „History“ für eine bestimmte Facebook-Zielgruppe mit einer Tabelle „Audience History“ mit Spalten für die Aktivität, Aktivitätsdetails, geänderte Elemente sowie Datum und Uhrzeit.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience-Sync-Komponente besser zu verstehen.

| Metrik | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente betreten haben, um mit Facebook synchronisiert zu werden. |
| Zum nächsten Schritt fortgefahren | Wie viele Nutzer:innen zur nächsten Komponente weitergeleitet wurden, falls eine vorhanden ist. Alle Nutzer:innen werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Branch ist. |
| Synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die erfolgreich mit Facebook synchronisiert wurden. |
| Nicht synchronisierte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund fehlender Abgleichfelder nicht synchronisiert wurden. Felder werden mit einem „ODER“-Operator abgeglichen, d. h. solange ein:e Nutzer:in eines der Felder in Facebook hat, wird Facebook die:den Nutzer:in zuordnen, auch wenn bei allen anderen Feldern keine Übereinstimmung besteht. |
| Ausstehende Nutzer:innen | Anzahl der Nutzer:innen, die derzeit von Braze verarbeitet werden, um mit Facebook synchronisiert zu werden. |
| Fehlerhafte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Facebook synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Facebook-Token oder eine gelöschte Custom Audience auf Facebook sein. |
| Canvas verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas ein Facebook-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

{% alert important %}
Aufgrund interner Verarbeitung gibt es eine Verzögerung bei der Berichterstattung für die Metriken „Synchronisierte Nutzer:innen“ und „Fehlerhafte Nutzer:innen“.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert es, bis meine Zielgruppen im Dashboard meines Audience-Sync-Partners angezeigt werden? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

Die Zeit, die zum Aufbau einer Zielgruppe benötigt wird, hängt vom jeweiligen Partner ab. Alle Netzwerke verarbeiten die Anfragen von Braze und versuchen, Nutzer:innen zuzuordnen. Es kann bis zu 24 Stunden dauern, bis Custom Audiences aktualisiert werden.

### Was sollte ich tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Sie können Ihr Facebook-Konto auf der Facebook-Partnerseite einfach trennen und erneut verbinden. Bestätigen Sie mit Ihrem Facebook Business Manager-Administrator, dass Sie über die entsprechenden Berechtigungen für das Werbekonto verfügen, mit dem Sie synchronisieren möchten.

### Warum darf mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

- Stellen Sie sicher, dass Ihr System-Nutzer-Token authentifiziert ist und Zugriff auf die gewünschten Werbekonten im Facebook Business Manager hat.
- Stellen Sie sicher, dass Sie ein Werbekonto ausgewählt, einen Namen für die neue Custom Audience eingegeben und Felder zum Abgleich ausgewählt haben.
- Möglicherweise haben Sie das Limit von 500 Custom Audiences auf Facebook erreicht. Gehen Sie zum Facebook Audience Manager, um einige nicht benötigte Zielgruppen zu löschen, bevor Sie neue Custom Audiences mit Canvas erstellen.

### Wie erfahre ich, ob Nutzer:innen nach der Übermittlung an Facebook zugeordnet wurden? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebook stellt diese Informationen aus Datenschutzgründen nicht zur Verfügung.

### Unterstützt Braze wertbasierte Custom Audiences? {#does-braze-support-value-based-custom-audiences}

Derzeit werden wertbasierte Custom Audiences von Braze nicht unterstützt. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### Hasht Braze Daten, bevor sie an Audience-Sync-Partner gesendet werden? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Sobald E-Mail-Daten normalisiert sind, hasht Braze sie mit SHA256.

**IDFA/AAID/Telefon:** Braze hasht mit SHA256. Die Zielgruppentypen, die wir synchronisieren, sind immer einer der folgenden:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

Was die Häufigkeit betrifft, hasht Braze personenbezogene Daten (PII) von Nutzer:innen nur dann, wenn diese den Audience-Sync-Schritt in der User Journey erreichen, als Vorbereitung für die Synchronisierung.

### Wie löse ich ein Problem bei der Synchronisierung einer wertbasierten Lookalike Custom Audience? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

Derzeit werden wertbasierte Lookalike Custom Audiences von Braze nicht unterstützt. Wenn Sie versuchen, mit dieser Zielgruppe zu synchronisieren, kann dies zu Fehlern in Ihrem Audience-Sync-Schritt führen. Um dies zu beheben, führen Sie die folgenden Schritte aus:

1. Gehen Sie zu Ihrem Facebook Ad Manager-Dashboard und wählen Sie **Audiences** aus.
2. Wählen Sie **Create audience** > **Custom audience** aus.
3. Wählen Sie **Customer list** aus.
4. Laden Sie Ihre CSV-Datei oder Liste ohne die Spalte **Value** hoch. Wählen Sie **No, continue with a customer list that doesn't include customer value** aus.
5. Schließen Sie die Erstellung Ihrer Custom Audience ab.
6. Aktualisieren Sie in Braze den Facebook-Audience-Sync-Schritt mit der von Ihnen erstellten Custom Audience.

### Ich habe eine E-Mail zu den Nutzungsbedingungen für Facebook Custom Audiences erhalten. Was sollte ich tun, um dies zu klären? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Um Audience Sync zu Facebook zu verwenden, müssen Sie diese Nutzungsbedingungen akzeptieren.

- Wenn Ihr Werbekonto direkt mit Ihrem persönlichen Facebook-Konto verknüpft ist, können Sie die Nutzungsbedingungen in Ihrem persönlichen Konto hier akzeptieren: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Wenn Ihr Werbekonto mit dem Business Manager-Konto Ihres Unternehmens verknüpft ist, müssen Sie die Nutzungsbedingungen in Ihrem Facebook Business Manager-Konto hier akzeptieren: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Nachdem Sie die Nutzungsbedingungen für Facebook Custom Audiences akzeptiert haben, gehen Sie wie folgt vor:

1. Aktualisieren Sie Ihr Facebook-Zugriffstoken bei Braze, indem Sie Ihr Facebook-Konto trennen und erneut verbinden.
2. Aktivieren Sie Ihren Facebook-Audience-Sync-Schritt erneut, indem Sie Ihr Canvas bearbeiten und aktualisieren.

Anschließend kann Braze Nutzer:innen synchronisieren, sobald sie den Facebook-Audience-Sync-Schritt erreichen.

### Was ist mit den Filtern **Connected Facebook** und **Number of Facebook Friends Using App** passiert? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Die Braze-Segmentierungsfilter **Number of Facebook Friends Using App** und **Connected Facebook** sind veraltet. Facebook und die Braze-SDKs erfassen die zugrunde liegenden Daten, auf die sich diese Filter stützten, nicht mehr.

Ersetzen Sie die veralteten Filter durch angepasste Attribute, angepasste Events oder Engagement-basierte Segmente – zum Beispiel Facebook-Anmeldung oder Social Linking anstelle von **Connected Facebook**, oder Empfehlungen, Einladungen und Shares anstelle von **Number of Facebook Friends Using App**.

Für Canvas-Retargeting ordnen Sie Nutzer:innen anhand von E-Mail, Telefon, Vorname und Nachname zu, wie in [Schritt 4: Sync-Einrichtung](#step-4-sync-setup) gezeigt. Um die Reichweite zu erhöhen, synchronisieren Sie ein hochwertiges Segment mit Facebook und erstellen Sie eine Lookalike Audience im Meta Ads Manager.

## Fehlerbehebung {#troubleshooting}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table aria-label="Fehlerbehebung">
  <thead>
    <tr>
      <th>Fehler</th>
      <th>Beschreibung</th>
      <th>Lösungsschritte</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Invalid Token</b></td>
      <td>Typische Ursachen sind unter anderem, dass die Person, die die Integration verbunden hat, ihr Passwort ändert oder Zugangsdaten ablaufen.</td>
      <td>Gehen Sie zu <b>Partnerintegrationen</b> > <b>Facebook</b> und trennen Sie Ihr Konto und verbinden Sie es erneut. Weitere Schritte zur Überprüfung Ihres Facebook-Kontos finden Sie in <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a>.</td>
    </tr>
    <tr>
      <td><b>Audience Size Too Low</b></td>
      <td>Dieser Fehler kann auftreten, wenn Sie einen Audience-Sync-Schritt erstellt haben, der Nutzer:innen aus Ihren Zielgruppen entfernt. Wenn Ihre Zielgruppengröße gegen null geht, kann das Netzwerk melden, dass die Zielgruppe zu klein ist, um ausgeliefert zu werden.</td>
      <td>Verwenden Sie eine Audience-Sync-Strategie, die regelmäßig Nutzer:innen hinzufügt und entfernt, sodass die Zielgruppengröße nicht vollständig aufgebraucht wird.</td>
    </tr>
    <tr>
      <td><b>Audience Does Not Exist</b></td>
      <td>Der Audience-Sync-Schritt verwendet eine Zielgruppe, die nicht existiert oder gelöscht wurde. Dies kann auch ausgelöst werden, wenn Sie nicht mehr über die erforderlichen Berechtigungen für den Zugriff auf die Zielgruppe verfügen.</td>
      <td>Lassen Sie eine:n Administrator:in auf der Partnerplattform prüfen, ob die Zielgruppe noch existiert. <br><br>Falls sie existiert, überprüfen Sie, ob die Person, die die Integration verbunden hat, Zugriff auf die Zielgruppe hat. Falls nicht, muss dieser Person der Zugriff auf die Zielgruppe gewährt werden. <br><br>Falls die Zielgruppe absichtlich entfernt wurde, fügen Sie eine aktive Zielgruppe hinzu und erstellen Sie eine neue Zielgruppe im Schritt.</td>
    </tr>
    <tr>
      <td><b>Ad Account Access Attempt</b></td>
      <td>Sie haben keine Berechtigungen für das Werbekonto oder die Zielgruppe, die Sie ausgewählt haben.</td>
      <td>Arbeiten Sie mit den Administrator:innen Ihres Werbekontos zusammen, um die richtigen Zugriffsrechte und Berechtigungen zu erhalten.</td>
    </tr>
    <tr>
      <td><b>Terms of Service Not Accepted</b></td>
      <td>Für einige Audience-Sync-Ziele, wie Facebook, ist es vom Werbenetzwerk erforderlich, bestimmte Nutzungsbedingungen zu akzeptieren, um das Audience-Sync-Feature nutzen zu können. Dieser Fehler wird ausgelöst, wenn Sie die entsprechenden Bedingungen nicht akzeptiert haben. Möglicherweise haben Sie auch eine E-Mail von Braze mit folgendem Betreff erhalten: „Your authorization credentials for Facebook are invalid.“</td>
      <td>Stellen Sie sicher, dass Sie die erforderlichen Nutzungsbedingungen von Facebook akzeptiert haben.</td>
    </tr>
    <tr>
      <td><b>All Users Are Erroring Out</b></td>
      <td>Wenn bei allen Nutzer:innen in einem Schritt Fehler auftreten, obwohl bestätigt wurde, dass diese Nutzer:innen Werte für die ausgewählten Felder im Schritt haben, könnte dies auf ein Problem mit Ihrem Facebook-Konto hinweisen.</td>
      <td>Folgen Sie den Schritten in <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a>, um Ihr Konto auf Probleme zu überprüfen.
      </td>
    </tr>
    <tr>
      <td><b>Failed to create audience</b></td>
      <td>Auf der Facebook-Technologie-Partnerseite wird „Connected“ angezeigt, aber es gibt einen Fehler im Facebook-Audience-Sync-Schritt beim Synchronisieren einer Zielgruppe: „Failed to create audience ‚audience name'“. Die Autorisierung Ihres Facebook-Kontos ist fehlgeschlagen. Besuchen Sie die Technologie-Partnerseite, um Ihr Konto erneut zu verbinden.</td>
      <td>Folgen Sie den Schritten in <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a>, um Ihr Konto auf Probleme zu überprüfen.
      </td>
    </tr>
    <tr>
      <td><b>Ad account missing from dropdown</b></td>
      <td>Wenn Sie den Facebook-Audience-Schritt konfigurieren, wird ein erwartetes Werbekonto nicht in der Werbekonto-Auswahl angezeigt.</td>
      <td>Bestätigen Sie, dass Ihre Facebook-App die <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">App-Überprüfung</a> für <code>ads_management</code> mit der von Facebook für die Marketing-API-Nutzung erforderlichen Zugriffsebene abgeschlossen hat. Bestätigen Sie im <a href="https://business.facebook.com/">Facebook Business Manager</a>, dass das System-Nutzer-Token die richtigen Berechtigungen hat und mit den Werbekonten verknüpft ist, die Sie in Braze verwenden, und dass die Nutzungsbedingungen des Werbekontos akzeptiert wurden. <br><br>Wenn das Dropdown in einem neuen Canvas funktioniert, aber nicht in einem bereits bearbeiteten Canvas, versuchen Sie einen Hard-Refresh Ihres Browsers (oder leeren Sie Ihren Cache) und bestätigen Sie, dass Sie als Nutzer:in angemeldet sind, die noch Zugriff auf diese Werbekonten hat.</td>
    </tr>
    <tr>
      <td><b>Error validating access token</b></td>
      <td>Beim Verbinden von Braze mit Facebook oder beim Synchronisieren von Zielgruppen wird ein Fehler bei der Validierung des Facebook-Zugriffstokens angezeigt.</td>
      <td>Melden Sie sich in Ihrem Browser von Facebook ab. Gehen Sie in Braze zu <b>Partnerintegrationen</b> &gt; <b>Facebook</b>, entfernen Sie die gespeicherten Facebook-Zugangsdaten und verbinden Sie Facebook erneut. Trennen und verbinden Sie auf der Facebook-Technologie-Partnerseite für Braze die Integration erneut, falls die Option verfügbar ist. <br><br>Falls die Probleme weiterhin bestehen, folgen Sie den Schritten unter <a href="#audit-your-facebook-account">Facebook-Konto überprüfen</a>.</td>
    </tr>
    <tr>
      <td><b>Audience export or sync permission errors</b></td>
      <td>Der Export oder die Synchronisierung einer Facebook-Zielgruppe schlägt mit Autorisierungs-, Admin- oder Werbekonto-Fehlern fehl.</td>
      <td>Öffnen Sie in <a href="https://developers.facebook.com/">Meta for Developers</a> Ihre App und bestätigen Sie, dass Ihre Nutzer:in eine <b>Admin</b>-Rolle unter <b>App roles</b> hat. Bestätigen Sie unter <b>App settings</b> &gt; <b>Advanced</b>, dass <b>Advertising accounts</b> die Konten enthält, die Sie mit Braze verwenden. Bestätigen Sie in den <a href="https://business.facebook.com/latest/settings">Business-Einstellungen</a>, dass die verbindende Person oder der System-Nutzer Zugriff auf das richtige Werbekonto hat.</td>
    </tr>
  </tbody>
</table>

### Facebook-Konto überprüfen {#audit-your-facebook-account}

Wenn bei Ihrer Integration weitere Probleme auftreten, lesen Sie die folgenden Abschnitte und Schritte zur Überprüfung Ihres Facebook-Kontos.

#### Kontoberechtigungen überprüfen {#review-account-permissions}

1. Lesen Sie die [Facebook-Dokumentation](https://www.facebook.com/business/help/186007118118684?id=829106167281625) zur Verwaltung dieser Berechtigungen auf der Plattform. Für den Facebook Business Manager benötigen Sie mindestens eine **Admin**- oder **Employee**-Rolle im Business Manager mit Zugriff auf die erforderlichen Werbekonten.
2. Bestätigen Sie als **Employee**, dass Ihnen die Admin-Person die vollständigen **Manage Ad Account**-Berechtigungen für jedes Werbekonto gewährt, um eine Zielgruppe zu erstellen oder Nutzer:innen mit der Zielgruppe zu synchronisieren.
3. Nachdem dies gewährt wurde, müssen Sie Ihr Konto trennen und erneut verbinden.

#### Nutzungsbedingungen akzeptieren {#terms}

Akzeptieren Sie alle ausstehenden Nutzungsbedingungen (TOS) von Facebook. Facebook verlangt regelmäßig, dass Sie (als Nutzer:in) und der Business Manager die Nutzungsbedingungen erneut genehmigen.

1. Die verbundene Person muss alle Nutzungsbedingungen für jedes ihrer Werbekonten akzeptieren:
- Custom Audience TOS für Ihr persönliches Facebook-Konto:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Ein Konto mit vollständigen Kontrollberechtigungen zur Verwaltung eines Werbekontos.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Um Ihre Konto- und Business-ID zu finden, führen Sie die folgenden Schritte aus:

1. Gehen Sie zu Ihrem [Facebook Ads Manager-Konto](https://adsmanager.facebook.com/).
2. Bestätigen Sie, dass Sie das richtige Werbekonto verwenden, indem Sie es im Dropdown-Menü überprüfen.
3. Finden Sie in der URL die Konto-ID nach `act=` und die Business-ID nach `business_id=`

![Die URL mit hervorgehobener Konto-ID und Business-ID.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lesen Sie die Custom-Audience-Bedingungen und wählen Sie **Accept**. Wir empfehlen, über das Dropdown oben in den Bedingungen zu bestätigen, für welches Konto die Nutzungsbedingungen unterzeichnet werden.

![Das Dropdown, das das Konto anzeigt, das die Nutzungsbedingungen unterzeichnet.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Sie müssen **Accept** für die Nutzungsbedingungen auswählen. Danach sehen Sie diese Nachricht: „You have accepted these terms of service on behalf of Braze“.
6. Aktualisieren Sie Ihr Facebook-Zugriffstoken bei Braze, indem Sie Ihr Facebook-Konto trennen und erneut verbinden.
7. Aktivieren Sie Ihren Facebook-Audience-Sync-Schritt erneut, indem Sie Ihren Canvas bearbeiten und aktualisieren. Braze kann dann Nutzer:innen synchronisieren, sobald sie den Facebook-Audience-Schritt erreichen.
8. Falls das Problem weiterhin besteht, versuchen Sie, eine:n separate:n Nutzer:in mit Admin-Berechtigungen zu verwenden, um die Bedingungen manuell über den Ads Manager zu akzeptieren.

#### Ausstehende Aufgaben abschließen {#complete-any-pending-tasks}

Prüfen Sie, ob Sie ausstehende Aufgaben bei Facebook haben, die Sie daran hindern könnten, Facebook Ads-Dienste zu nutzen:

1. [Melden Sie sich beim Facebook Ads Manager an](https://adsmanager.facebook.com/).
2. Wählen Sie das Werbekonto aus, bei dem Probleme auftreten.
3. Wählen Sie in der Navigation Ihre **Kontoübersicht** aus. <br> ![Die Navigation mit ausgewählter Kontoübersicht.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Prüfen Sie, ob es Warnungen gibt, die bearbeitet werden müssen. <br> ![Ein Konto mit einer abgelaufenen Kreditkarte.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Prüfen Sie, ob es Setup-Aufgaben gibt, die abgeschlossen werden müssen. <br> ![Ein Konto mit einer teilweise abgeschlossenen Kontoeinrichtung.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Mit einer anderen Person verbinden {#connect-with-a-different-user}

Als weiteren Schritt zur Fehlerbehebung empfehlen wir, dass eine andere Person mit Admin-Berechtigungen versucht, ihr Konto zu verbinden, indem sie Folgendes tut:

1. Trennen Sie die aktuelle Integration.
2. Eine separate Person mit Admin-Berechtigungen verbindet ihr Facebook-Nutzerkonto.