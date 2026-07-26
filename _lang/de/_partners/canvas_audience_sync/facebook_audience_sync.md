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

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen den Schritt Audience Sync erreichen, synchronisiert Braze sie nahezu in Realtime und respektiert dabei die Rate-Limits der Facebook Marketing API. Braze stapelt und verarbeitet alle 5 Sekunden so viele Nutzer:innen wie möglich, bevor es sie an Facebook weiterleitet.

Das Rate-Limit der Facebook Marketing API erlaubt nicht mehr als &#126;190.000 API-Anfragen pro Anzeigenkonto in einem Zeitraum von einer Stunde. Erreicht eine geschäftskunden dieses Limit, wiederholt Braze die Synchronisierung für bis zu &#126;13 Stunden. Wenn die Synchronisierung immer noch nicht möglich ist, listet Braze diese Nutzer:innen in der Metrik „Fehlerhafte Nutzer:innen“ auf.

## Voraussetzungen {#prerequisites}

Bevor Sie den Facebook-Audience-Schritt in Canvas einrichten, müssen Sie sicherstellen, dass die folgenden Punkte erstellt und abgeschlossen sind.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten und Apps). |
| Facebook-Anzeigenkonto | [Facebook](https://www.facebook.com/business/help/910137316041095) | Ein aktives Facebook-Anzeigenkonto, das an den Business Manager Ihrer Marke gebunden ist.<br><br>Stellen Sie sicher, dass Ihr Facebook-Business-Manager-Administrator Ihnen entweder die Berechtigung „Kampagnen verwalten“ oder „Anzeigenkonten verwalten“ für die Facebook-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. Stellen Sie außerdem sicher, dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. |
| Facebook-Bedingungen für angepasste Zielgruppen | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Akzeptieren Sie die Facebook-Bedingungen für angepasste Zielgruppen für Ihre Facebook-Anzeigenkonten, die Sie mit Braze verwenden möchten. |
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
| Zum nächsten Schritt fortgefahren | Wie viele Nutzer:innen zur nächsten Komponente vorgerückt sind, falls eine vorhanden ist. Alle Nutzer:innen rücken automatisch vor, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit Facebook synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. Die Felder werden mit einem „OR“-Operator abgeglichen, d. h. solange Nutzer:innen eines der Felder in Facebook haben, wird Facebook die Nutzer:innen abgleichen, auch wenn es keine Übereinstimmung bei allen anderen Feldern gibt. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Facebook verarbeitet werden. |
| Fehlerhafte Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Facebook synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Facebook-Token oder das Löschen der angepassten Zielgruppe auf Facebook sein. |
| Canvas verlassen | Anzahl der Nutzer:innen, die das Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas ein Facebook-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

{% alert important %}
Es gibt eine Verzögerung bei der Berichterstattung für die Metriken „Nutzer:innen synchronisiert“ und „Fehlerhafte Nutzer:innen“ aufgrund der internen Verarbeitung.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert es, bis meine Zielgruppen in meinem Audience-Sync-Partner-Dashboard angezeigt werden? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

Wie lange es dauert, eine Zielgruppe zu befüllen, hängt vom jeweiligen Partner ab. Alle Netzwerke verarbeiten die Anfragen von Braze und versuchen, Nutzer:innen abzugleichen. Es kann bis zu 24 Stunden dauern, bis die angepassten Zielgruppen aktualisiert sind.

### Was sollte ich als Nächstes tun, wenn ich einen Fehler wegen eines ungültigen Tokens erhalte? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Sie können Ihr Facebook-Konto auf der Facebook-Partnerseite einfach trennen und wieder verbinden. Vergewissern Sie sich bei Ihrem Facebook-Business-Manager-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.

### Warum darf mein Canvas nicht gestartet werden? {#why-is-my-canvas-not-allowed-to-launch}

- Stellen Sie sicher, dass Ihr System User Token authentifiziert ist und Zugriff auf die gewünschten Anzeigenkonten im Facebook Business Manager hat.
- Stellen Sie sicher, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue angepasste Zielgruppe eingegeben und die entsprechenden Felder zum Abgleich ausgewählt haben.
- Möglicherweise haben Sie das Limit von 500 angepassten Zielgruppen auf Facebook erreicht. Gehen Sie zum Facebook Audience Manager, um einige nicht benötigte Zielgruppen zu löschen, bevor Sie neue angepasste Zielgruppen mit Canvas erstellen.

### Woher weiß ich, ob Nutzer:innen abgeglichen wurden, nachdem ich sie an Facebook weitergegeben habe? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebook stellt diese Informationen aus Datenschutzgründen nicht zur Verfügung.

### Unterstützt Braze wertbasierte angepasste Zielgruppen? {#does-braze-support-value-based-custom-audiences}

Derzeit werden wertbasierte angepasste Zielgruppen von Braze nicht unterstützt. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### Hasht Braze Daten, bevor sie an Audience-Sync-Partner gesendet werden? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Sobald die E-Mail-Daten normalisiert sind, hasht Braze sie mit SHA256.

**IDFA/AAID/Telefon:** Braze hasht mit SHA256. Die Zielgruppentypen, die wir synchronisieren, sind immer einer der folgenden:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

Was die Häufigkeit betrifft, hasht Braze personenbezogene Daten (PII) von Nutzer:innen nur dann, wenn diese den Audience-Sync-Schritt in der User Journey zur Vorbereitung der Synchronisierung betreten.

### Wie löse ich ein Problem bei der Synchronisierung einer wertbasierten Lookalike-Zielgruppe? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

Derzeit werden wertbasierte Lookalike-Zielgruppen von Braze nicht unterstützt. Wenn Sie versuchen, mit dieser Zielgruppe zu synchronisieren, kann dies zu Fehlern bei Ihrem Audience-Sync-Schritt führen. Führen Sie die folgenden Schritte aus, um dieses Problem zu lösen:

1. Gehen Sie zu Ihrem Facebook Ad Manager Dashboard und wählen Sie **Audiences**.
2. Wählen Sie **Create audience** > **Custom audience**.
3. Wählen Sie **geschäftskunden list** aus.
4. Laden Sie Ihre CSV-Datei oder Liste ohne die Spalte **Value** hoch. Wählen Sie **No, continue with a geschäftskunden list that doesn't include geschäftskunden value**.
5. Schließen Sie die Erstellung Ihrer angepassten Zielgruppe ab.
6. Aktualisieren Sie in Braze den Facebook-Audience-Sync-Schritt mit der angepassten Zielgruppe, die Sie erstellt haben.

### Ich habe eine E-Mail zu den Nutzungsbedingungen für angepasste Facebook-Zielgruppen erhalten. Was sollte ich tun, um dieses Problem zu lösen? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Um Audience Sync mit Facebook nutzen zu können, müssen Sie diese Nutzungsbedingungen akzeptieren.

- Wenn Ihr Anzeigenkonto direkt mit Ihrem persönlichen Facebook-Konto verknüpft ist, können Sie die Nutzungsbedingungen in Ihrem persönlichen Konto hier akzeptieren: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Wenn Ihr Anzeigenkonto mit dem Business-Manager-Konto Ihres Unternehmens verknüpft ist, müssen Sie die Nutzungsbedingungen in Ihrem Facebook-Business-Manager-Konto hier akzeptieren: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Nachdem Sie die Nutzungsbedingungen für Ihre angepasste Facebook-Zielgruppe akzeptiert haben, gehen Sie wie folgt vor:

1. Aktualisieren Sie Ihr Facebook-Zugriffstoken mit Braze, indem Sie die Verbindung zu Ihrem Facebook-Konto trennen und erneut herstellen.
2. Aktivieren Sie Ihren Facebook-Audience-Sync-Schritt wieder, indem Sie Ihr Canvas bearbeiten und aktualisieren.

Dann kann Braze die Nutzer:innen synchronisieren, sobald sie den Facebook-Audience-Sync-Schritt erreichen.

### Was ist mit den Filtern „Connected Facebook“ und „Number of Facebook Friends Using App“ passiert? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Die Braze-Segmentierungsfilter **Number of Facebook Friends Using App** und **Connected Facebook** sind veraltet. Facebook und die Braze-SDKs erfassen die zugrunde liegenden Daten, auf die sich diese Filter stützten, nicht mehr.

Ersetzen Sie die veralteten Filter durch angepasste Attribute, angepasste Events oder Engagement-basierte Segmente – zum Beispiel Facebook-Login oder Social Linking anstelle von **Connected Facebook**, oder Empfehlungen, Einladungen und Shares anstelle von **Number of Facebook Friends Using App**.

Für Canvas-Retargeting gleichen Sie Nutzer:innen mit E-Mail, Telefon, Vorname und Nachname ab, wie in [Schritt 4: Sync-Einrichtung](#step-4-sync-setup) gezeigt. Um die Reichweite zu erweitern, synchronisieren Sie ein hochwertiges Segment mit Facebook und erstellen Sie eine Lookalike-Zielgruppe im Meta Ads Manager.

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
      <th>Schritte zur Behebung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Ungültiges Token</b></td>
      <td>Typische Ursachen sind, wenn die Nutzer:innen, die die Integration verbunden haben, ihr Passwort ändern, Zugangsdaten ablaufen und mehr.</td>
      <td>Gehen Sie zu <b>Partnerintegrationen</b> > <b>Facebook</b> und trennen Sie die Verbindung zu Ihrem Konto und verbinden Sie es erneut. In <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a> finden Sie weitere Schritte zur Überprüfung Ihres Facebook-Kontos.</td>
    </tr>
    <tr>
      <td><b>Zielgruppe zu klein</b></td>
      <td>Dieser Fehler kann auftreten, wenn Sie einen Audience-Sync-Schritt erstellt haben, der Nutzer:innen aus Ihren Zielgruppen entfernt. Wenn die Größe Ihrer Zielgruppe gegen Null geht, kann das Netzwerk feststellen, dass die Zielgruppe zu klein ist, um bedient zu werden.</td>
      <td>Verwenden Sie eine Audience-Sync-Strategie, die regelmäßig Nutzer:innen hinzufügt und entfernt, ohne die Zielgruppengröße vollständig zu erschöpfen.</td>
    </tr>
    <tr>
      <td><b>Zielgruppe existiert nicht</b></td>
      <td>Der Audience-Sync-Schritt verwendet eine Zielgruppe, die nicht existiert oder gelöscht wurde. Dies kann auch ausgelöst werden, wenn Sie nicht mehr über die erforderliche Berechtigung zum Zugriff auf die Zielgruppe verfügen.</td>
      <td>Lassen Sie einen Administrator auf der Partner-Plattform prüfen, ob die Zielgruppe noch existiert. <br><br>Falls vorhanden, prüfen Sie, ob die Nutzer:innen, die die Integration verbunden haben, über die Berechtigung für die Zielgruppe verfügen. Ist dies nicht der Fall, muss den Nutzer:innen der Zugang zu dieser Zielgruppe gewährt werden. <br><br>Wenn die Zielgruppe absichtlich entfernt wurde, fügen Sie eine aktive Zielgruppe hinzu und erstellen Sie eine neue Zielgruppe im Schritt.</td>
    </tr>
    <tr>
      <td><b>Zugriffsversuch auf Anzeigenkonto</b></td>
      <td>Sie haben keine Berechtigung für das von Ihnen ausgewählte Anzeigenkonto oder die Zielgruppe.</td>
      <td>Arbeiten Sie mit den Administratoren Ihres Anzeigenkontos zusammen, um den richtigen Zugang und die richtigen Berechtigungen zu erhalten.</td>
    </tr>
    <tr>
      <td><b>Nutzungsbedingungen nicht akzeptiert</b></td>
      <td>Bei einigen Audience-Sync-Zielen wie Facebook ist es vom Werbenetzwerk erforderlich, bestimmte Nutzungsbedingungen zu akzeptieren, um das Audience-Sync-Feature nutzen zu können. Dieser Fehler wird ausgelöst, wenn Sie die entsprechenden Bedingungen nicht akzeptiert haben. Daher haben Sie möglicherweise auch eine E-Mail mit diesem Betreff von Braze erhalten: „Your authorization credentials for Facebook are invalid.“</td>
      <td>Prüfen Sie, ob Sie die erforderlichen Nutzungsbedingungen von Facebook akzeptiert haben.</td>
    </tr>
    <tr>
      <td><b>Alle Nutzer:innen sind fehlerhaft</b></td>
      <td>Wenn alle Nutzer:innen bei einem Schritt Fehler aufweisen, obwohl Sie bestätigt haben, dass diese Nutzer:innen Werte für die ausgewählten Felder des Schritts haben, könnte dies auf ein Problem mit Ihrem Facebook-Konto hinweisen.</td>
      <td>Folgen Sie den Schritten in <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a>, um Ihr Konto auf Probleme zu überprüfen.
      </td>
    </tr>
    <tr>
      <td><b>Zielgruppe konnte nicht erstellt werden</b></td>
      <td>Auf der Facebook-Technologie-Partnerseite sehen Sie „Verbunden“, aber im Facebook-Audience-Sync-Schritt beim Synchronisieren einer Zielgruppe erscheint die Fehlermeldung „Zielgruppe ‚Zielgruppenname' konnte nicht erstellt werden“. Die Autorisierung Ihres Facebook-Kontos ist fehlgeschlagen. Besuchen Sie die Technologie-Partnerseite, um Ihr Konto erneut zu verbinden.</td>
      <td>Folgen Sie den Schritten in <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a>, um Ihr Konto auf Probleme zu überprüfen.
      </td>
    </tr>
    <tr>
      <td><b>Anzeigenkonto fehlt in der Dropdown-Liste</b></td>
      <td>Wenn Sie den Facebook-Audience-Schritt konfigurieren, wird ein erwartetes Anzeigenkonto nicht in der Anzeigenkonto-Auswahl angezeigt.</td>
      <td>Vergewissern Sie sich, dass Ihre Facebook-App die <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">App-Überprüfung</a> für <code>ads_management</code> mit der von Facebook für die Marketing-API-Nutzung erforderlichen Zugriffsebene abgeschlossen hat. Bestätigen Sie im <a href="https://business.facebook.com/">Facebook Business Manager</a>, dass das System User Token die richtigen Berechtigungen hat und den Anzeigenkonten zugeordnet ist, die Sie in Braze verwenden, und dass die Nutzungsbedingungen für das Anzeigenkonto akzeptiert wurden. <br><br>Wenn die Dropdown-Liste in einem neuen Canvas funktioniert, aber nicht in einem bereits bearbeiteten Canvas, versuchen Sie, Ihren Browser hart zu aktualisieren (oder den Cache zu leeren), und bestätigen Sie, dass Sie als Nutzer:in angemeldet sind, die noch Zugriff auf diese Anzeigenkonten hat.</td>
    </tr>
    <tr>
      <td><b>Fehler bei der Validierung des Zugriffstokens</b></td>
      <td>Beim Verbinden von Braze mit Facebook oder beim Synchronisieren von Zielgruppen wird ein Fehler bei der Validierung des Facebook-Zugriffstokens angezeigt.</td>
      <td>Melden Sie sich in Ihrem Browser von Facebook ab. Gehen Sie in Braze zu <b>Partnerintegrationen</b> &gt; <b>Facebook</b>, entfernen Sie die gespeicherten Facebook-Zugangsdaten und verbinden Sie Facebook erneut. Trennen und verbinden Sie auf der Facebook-Technologie-Partnerseite für Braze die Integration erneut, falls die Option verfügbar ist. <br><br>Wenn die Probleme weiterhin bestehen, folgen Sie den Schritten unter <a href="#audit-your-facebook-account">Ihr Facebook-Konto überprüfen</a>.</td>
    </tr>
    <tr>
      <td><b>Berechtigungsfehler beim Zielgruppenexport oder bei der Synchronisierung</b></td>
      <td>Der Export oder die Synchronisierung einer Facebook-Zielgruppe schlägt mit Autorisierungs-, Admin- oder Anzeigenkontofehlern fehl.</td>
      <td>Öffnen Sie in <a href="https://developers.facebook.com/">Meta for Developers</a> Ihre App und bestätigen Sie, dass Ihre Nutzer:innen unter <b>App roles</b> eine <b>Admin</b>-Rolle haben. Bestätigen Sie unter <b>App settings</b> &gt; <b>Advanced</b>, dass <b>Advertising accounts</b> die Konten enthält, die Sie mit Braze verwenden. Bestätigen Sie in den <a href="https://business.facebook.com/latest/settings">Business-Einstellungen</a>, dass die verbindenden Nutzer:innen oder das System User Token Zugriff auf das richtige Anzeigenkonto haben.</td>
    </tr>
  </tbody>
</table>

### Ihr Facebook-Konto überprüfen {#audit-your-facebook-account}

Wenn Sie weitere Probleme mit Ihrer Integration haben, lesen Sie die folgenden Abschnitte und Schritte zur Überprüfung Ihres Facebook-Kontos.

#### Kontoberechtigungen überprüfen {#review-account-permissions}

1. Lesen Sie [in der Dokumentation von Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) nach, wie Sie diese Berechtigungen auf der Plattform verwalten können. Für Facebook Business Manager benötigen Sie mindestens die Rolle **Admin** oder **Employee** im Business Manager mit Zugriff auf die erforderlichen Anzeigenkonten.
2. Bestätigen Sie als **Employee**, dass der Administrator Ihnen für jedes Anzeigenkonto die volle Berechtigung **Manage Ad Account** erteilt hat, um Zielgruppen zu erstellen oder Nutzer:innen mit der Zielgruppe zu synchronisieren.
3. Danach müssen Sie die Verbindung zu Ihrem Konto trennen und erneut herstellen.

#### Nutzungsbedingungen akzeptieren {#terms}

Akzeptieren Sie alle ausstehenden Nutzungsbedingungen von Facebook. Facebook fordert Sie (die Nutzer:innen) und den Business Manager regelmäßig auf, die Nutzungsbedingungen erneut zu genehmigen.

1. Die verbundenen Nutzer:innen müssen alle Nutzungsbedingungen für jedes ihrer Anzeigenkonten akzeptieren:
- Nutzungsbedingungen für angepasste Zielgruppen für Ihr persönliches Facebook-Konto:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Ein Konto mit voller Kontrollberechtigung zur Verwaltung eines Anzeigenkontos.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Um Ihre Konto- und Unternehmens-ID zu finden, gehen Sie folgendermaßen vor:

1. Gehen Sie zu Ihrem [Facebook Ads Manager-Konto](https://adsmanager.facebook.com/).
2. Überprüfen Sie, ob Sie das richtige Anzeigenkonto verwenden, indem Sie es im Dropdown-Menü verifizieren.
3. Suchen Sie in der URL die Konto-ID nach `act=` und die Unternehmens-ID nach `business_id=`.

![Die URL mit der hervorgehobenen Konto-ID und Unternehmens-ID.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lesen Sie die Bedingungen für angepasste Zielgruppen und wählen Sie **Accept** aus. Wir empfehlen, über die Dropdown-Liste oben in den Bedingungen zu bestätigen, für welches Konto die Nutzungsbedingungen unterzeichnet werden.

![Das Dropdown-Menü, das das Konto anzeigt, das die Nutzungsbedingungen unterzeichnet.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Sie müssen **Accept** für die Nutzungsbedingungen auswählen. Danach sehen Sie diese Nachricht: „You have accepted these terms of service on behalf of Braze“.
6. Aktualisieren Sie Ihr Facebook-Zugriffstoken mit Braze, indem Sie die Verbindung zu Ihrem Facebook-Konto trennen und erneut herstellen.
7. Aktivieren Sie Ihren Facebook-Audience-Sync-Schritt wieder, indem Sie Ihr Canvas bearbeiten und aktualisieren. Braze kann dann Nutzer:innen synchronisieren, sobald sie den Facebook-Audience-Schritt erreichen.
8. Wenn das Problem weiterhin besteht, versuchen Sie, separate Nutzer:innen mit Administratorrechten zu verwenden, um die Bedingungen manuell über den Ads Manager zu akzeptieren.

#### Ausstehende Aufgaben erledigen {#complete-any-pending-tasks}

Prüfen Sie, ob Sie ausstehende Aufgaben bei Facebook haben, die Sie daran hindern könnten, die Facebook-Ads-Dienste zu nutzen:

1. [Melden Sie sich beim Facebook Ads Manager an](https://adsmanager.facebook.com/).
2. Wählen Sie das Anzeigenkonto aus, mit dem Sie Probleme haben.
3. Wählen Sie in der Navigation Ihre **Account Overview** aus. <br> ![Die Navigation mit ausgewählter „Account Overview“.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Prüfen Sie, ob es Warnmeldungen gibt, die behoben werden müssen. <br> ![Ein Konto mit einer abgelaufenen Kreditkarte.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Prüfen Sie, ob es Setup-Aufgaben gibt, die erledigt werden müssen. <br> ![Ein Konto mit einer teilweise abgeschlossenen Kontoeinrichtung.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Mit anderen Nutzer:innen verbinden {#connect-with-a-different-user}

Als weiteren Schritt zur Fehlerbehebung empfehlen wir, dass andere Nutzer:innen mit Administratorrechten versuchen, ihr Konto zu verbinden, indem sie Folgendes tun:

1. Trennen Sie die aktuelle Integration.
2. Separate Nutzer:innen mit Administratorrechten verbinden ihr Facebook-Benutzerkonto.