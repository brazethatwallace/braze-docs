---
nav_title: Google
article_title: Canvas Audience Sync mit Google
alias: /google_audience_sync/
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Audience Sync für Google verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
tool:
  - Canvas
page_order: 3

---

# Audience Sync mit Google {#audience-sync-to-google}

{% alert important %}
Google aktualisiert seine [EU-Richtlinie zur Einwilligung der Nutzer:innen](https://www.google.com/about/company/user-consent-policy/) als Reaktion auf die Änderungen des [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), der ab dem 6. März 2024 in Kraft tritt. Diese neue Änderung erfordert, dass Werbetreibende bestimmte Informationen an ihre Endnutzer:innen im EWR, in Großbritannien und in der Schweiz weitergeben und die notwendige Zustimmung von ihnen einholen. Weitere Informationen finden Sie in der folgenden Dokumentation.
{% endalert %}

Die Braze Audience Sync to Google Integration ermöglicht es Marken, die Reichweite ihrer kanalübergreifenden Customer Journeys auf Google Search, Google Shopping, Gmail, YouTube und Google Display auszudehnen. Mithilfe Ihrer First-Party-Kundendaten können Sie Anzeigen auf der Grundlage von dynamischen Verhaltenstriggern, Segmentierung und mehr sicher zustellen. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (z. B. Push, E-Mail oder SMS) im Rahmen eines Braze-Canvas verwenden, kann verwendet werden, um eine Anzeige für diese Nutzer:innen über Googles [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) zu triggern.

{% alert note %}
Die Braze Audience Sync to Google Integration wird für Google Ads unterstützt, nicht für Google Ads Manager.
{% endalert %}

Google Ads generiert keine ähnlichen Zielgruppen, auch bekannt als „Lookalike Audiences“, mehr für Targeting und Reporting. Lesen Sie die [Dokumentation von Google Ads](https://support.google.com/google-ads/answer/12463119?), um mehr zu erfahren.

**Häufige Anwendungsfälle für die Synchronisierung von angepassten Zielgruppen sind:**
- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern.
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind.
- Erstellen von Unterdrückungs-Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten.

{% alert note %}
Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit Google geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, genauestens geprüft. Erfahren Sie mehr über unsere [Braze-Datenschutzrichtlinie](https://www.braze.com/privacy).
{% endalert %}

## Voraussetzungen {#prerequisites}

Vergewissern Sie sich, dass die folgenden Punkte erstellt und abgeschlossen sind, bevor Sie Ihren Google Audience-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Google Ads-Konto | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Ein aktives Google Ads-Konto für Ihre Marke.<br><br>Wenn Sie eine Zielgruppe für mehrere verwaltete Konten freigeben möchten, können Sie Ihre Zielgruppen in Ihr [Manager-Konto](https://support.google.com/google-ads/answer/6139186) hochladen. |
| Google Ads-Bedingungen und Google Ads-Richtlinien | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Bei der Nutzung von Braze Audience Sync müssen Sie die [Google-Anzeigenbedingungen](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) und die [Google-Anzeigenrichtlinien](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC) akzeptieren und sicherstellen, dass Sie diese einhalten, einschließlich der [EU-Richtlinie zur Einwilligung der Nutzer:innen](https://www.google.com/about/company/user-consent-policy/), soweit auf Sie zutreffend.<br><br>Informieren Sie sich bei Ihrem Rechtsteam über die neue Richtlinie von Google zur Einwilligung von Nutzer:innen in der EU, um sicherzustellen, dass Sie eine angemessene Einwilligung einholen, um die Dienste von Google Ads für Ihre Endnutzer:innen im EWR, in Großbritannien und in der Schweiz zu nutzen. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) | Customer Match ist nicht für alle Werbetreibenden verfügbar.<br><br>**Um Customer Match zu verwenden, muss Ihr Konto über Folgendes verfügen:**<br>• Einen guten Verlauf bei der Einhaltung der Richtlinien<br>• Einen guten Zahlungsverlauf<br>• Mindestens 90 Tage Verlauf in Google Ads<br>• Mehr als 50.000 USD Gesamtausgaben auf Lebenszeit. Für Werbetreibende, deren Konten in anderen Währungen als USD geführt werden, wird Ihr Ausgabenbetrag anhand der durchschnittlichen monatlichen Konversionsrate für diese Währung in USD umgerechnet.<br><br>Wenn Ihr Konto diese Kriterien nicht erfüllt, ist Ihr Konto derzeit nicht berechtigt, Customer Match zu verwenden.<br><br>Wenden Sie sich an Ihre Google Ads-Vertretung, um weitere Informationen zur Verfügbarkeit von Customer Match für Ihr Konto zu erhalten. |
| Google-Zustimmungssignale | [Google](https://support.google.com/google-ads/answer/14310715) | Wenn Sie mit dem Dienst Customer Match von Google Anzeigen für Endnutzer:innen im EWR schalten möchten, müssen Sie Braze die folgenden angepassten Attribute (boolesch) als Teil der EU-Zustimmungsrichtlinie von Google übergeben. Weitere Einzelheiten finden Sie unter [Einholung der Zustimmung für Endnutzer:innen aus dem EWR, Großbritannien und der Schweiz](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

### Erforderliche SDK-Versionen {#required-sdk-versions}

Wenn Sie Braze SDKs zum Sammeln von Zustimmungssignalen verwenden, stellen Sie sicher, dass Sie die folgenden Mindestversionen erfüllen:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Einholung der Zustimmung für Endnutzer:innen aus dem EWR, Großbritannien und der Schweiz {#collecting-consent-for-eea-uk-and-switzerland-end-users}

Die Richtlinie von Google zur Einwilligung der Nutzer:innen in der EU verlangt von den Werbetreibenden, dass sie ihren Endnutzer:innen im EWR, in Großbritannien und in der Schweiz die folgenden Informationen zur Verfügung stellen und deren Einwilligung einholen:

* Die Verwendung von Cookies oder anderer lokaler Speicherung, sofern dies gesetzlich vorgeschrieben ist; und
* Die Erfassung, Weitergabe und Verwendung ihrer persönlichen Daten für die Personalisierung von Anzeigen.

Dies betrifft weder US-amerikanische Endnutzer:innen noch andere Endnutzer:innen, die sich außerhalb des EWR, Großbritanniens oder der Schweiz befinden. Wenden Sie sich an Ihr Rechtsteam, um sich über die neue EU-Zustimmungsrichtlinie von Google zu informieren und sicherzustellen, dass Sie eine angemessene Zustimmung für die Nutzung der Dienste von Google Ads für Ihre Endnutzer:innen im EWR, in Großbritannien und in der Schweiz einholen.

Gemäß dem Digital Markets Act (DMA), der am 6. März 2024 in Kraft tritt, müssen Werbetreibende die Zustimmung der Endnutzer:innen aus dem EWR, Großbritannien und der Schweiz einholen, wenn sie Daten mit Google teilen. Im Rahmen dieser Änderung können Sie beide Zustimmungssignale in Braze als die folgenden booleschen angepassten Attribute erfassen:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze wird die Daten aus diesen angepassten Attributen mit den entsprechenden [Einwilligungsfeldern in Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A) synchronisieren.

#### Verwaltung widerrufener Einwilligungen {#managing-revoked-consent}

Um Ihre Zielgruppenlisten auf dem neuesten Stand zu halten, falls Endnutzer:innen im EWR zur Zielgruppenliste hinzugefügt wurden und anschließend eine der beiden Zustimmungen (`$google_ad_user_data` oder `$google_ad_personalization`) zurückgezogen haben, müssen Sie ein Canvas einrichten, um Nutzer:innen aus den bestehenden Zielgruppenlisten zu entfernen, indem Sie einen Audience Sync-Schritt verwenden.

{% alert note %}
Wenn Endnutzer:innen im EWR zuvor ihre Zustimmung für beide Signale gegeben haben, werden diese Daten weiterhin für Googles Customer Match verwendet, bis die Liste abläuft oder der Zustimmungsstatus explizit über Google Audience Sync aktualisiert wird, oder beides.
{% endalert %}

#### Tipps {#tips}

* Senden Sie den Wert als booleschen Typ, nicht als String-Typ.
* Stellen Sie dem Namen des Attributs das Dollarzeichen ($) voran. Braze verwendet ein Dollarzeichen am Anfang des Namens eines Attributs, um zu verdeutlichen, dass es sich um einen speziellen und reservierten Schlüssel handelt.
* Geben Sie den Namen des Attributs in Kleinbuchstaben ein.
* Sie können Nutzer:innen zwar nicht explizit als nicht spezifiziert festlegen, aber wenn Sie einen Wert `null` oder `nil` oder einen anderen Wert als `true` oder `false` senden, wird Braze diese Nutzer:innen als `UNSPECIFIED` an Google weitergeben.
* Neu hinzugefügte oder aktualisierte Nutzer:innen ohne Angabe eines der beiden Einwilligungsattribute werden mit Google synchronisiert, wobei diese Attribute als nicht spezifiziert markiert sind.

Wenn Sie versuchen, Nutzer:innen aus dem EWR zu synchronisieren, ohne die erforderlichen Einwilligungsfelder und den erteilten Status zu haben, wird Google dies ablehnen und keine Anzeigen für diese Nutzer:innen schalten. Wenn Nutzer:innen im EWR ohne deren ausdrückliche Zustimmung eine Anzeige geschaltet wird, können Sie außerdem haftbar gemacht werden und ein finanzielles Risiko eingehen. Um dies zu vermeiden, empfehlen wir, Campaigns mit Segmentfiltern zu versenden, die nur Nutzer:innen aus dem EWR, Großbritannien und der Schweiz mit den Google-Einwilligungsattributen `true` einschließen. Weitere Einzelheiten zur EU-Richtlinie über die Zustimmung der Nutzer:innen für Customer Match Upload-Partner finden Sie in den [FAQ](https://support.google.com/google-ads/answer/14310715) von Google.

### Einrichten Ihres Canvas {#setting-up-your-canvas}

Nach der Synchronisierung mit Braze stehen Ihnen die folgenden Einwilligungsattribute in Ihren Nutzerprofilen und für die Segmentierung zur Verfügung:

- `$google_ad_user_data`
- `$google_ad_personalization`

In jedem Canvas, in dem Sie Endnutzer:innen aus dem EWR, Großbritannien und der Schweiz mithilfe eines Google Audience Sync zu einer Zielgruppe hinzufügen, müssen Sie diese Nutzer:innen ausschließen, wenn beide Einwilligungsattribute einen Wert haben, der nicht `true` ist. Sie können dies tun, indem Sie diese Nutzer:innen segmentieren, wenn die Einwilligungswerte auf `true` eingestellt sind. Dadurch wird auch sichergestellt, dass die genaueren Analytics der Nutzer:innen synchronisiert werden, da wir wissen, dass Google diese Nutzer:innen aus den Zielgruppen ausschließt. Wenn Sie Google Audience Sync verwenden, um Nutzer:innen aus einer Zielgruppe zu entfernen, sind die Einwilligungsattribute nicht erforderlich.

## Integration

### Schritt 1: Google-Konto verbinden {#step-1-connect-google-account}

{% alert important %}
Sie müssen die [Berechtigung „Admin“]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) haben, um Google Ads mit Ihrem Braze-Konto zu verbinden.
{% endalert %}

Um loszulegen, gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** > **Google Ads** und wählen Sie **Google Ads verbinden**. Sie werden in einem Modal aufgefordert, die mit Ihrem Google Ads-Konto verknüpfte E-Mail auszuwählen und dann Braze Zugriff auf Ihr Google Ads-Konto zu gewähren.

Nachdem Sie Ihr Google Ads-Konto erfolgreich verbunden haben, werden Sie zu Ihrer Google Ads-Partnerseite weitergeleitet. Sie werden dann aufgefordert, die Anzeigenkonten auszuwählen, auf die Sie im Braze Workspace zugreifen möchten.

![Ein GIF, das den Workflow einer erfolgreichen Verbindung eines Google Ads-Kontos mit Braze zeigt.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exportieren von iOS IDFA oder Google Advertising IDs {#export-ios-idfa-or-google-advertising-ids}

Wenn Sie iOS IDFA oder Google Advertising IDs in Ihre Zielgruppen-Synchronisierung exportieren möchten, benötigt Google Ihre iOS App ID und Android App ID in den Anfragen. Wählen Sie unter Google Audience Sync die Option **Add Mobile Advertising IDs**, geben Sie die ID Ihrer iOS-App und Android-App (Name des App-Pakets) ein und speichern Sie beide.

<br><br>
![Die aktualisierte Seite zur Google Ads-Technologie zeigt die verbundenen Anzeigenkonten an und ermöglicht eine erneute Synchronisierung der Konten sowie das Hinzufügen von IDs für mobile Werbung.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Wenn Sie mehrere Apps in einem Workspace haben, können Sie bei der Einrichtung jede Ihrer App IDs eingeben, da die mobilen Anzeigen-IDs für Ihre Nutzer:innen in allen Apps gleich sind. Das liegt daran, dass sowohl der Android GAID als auch der iOS IDFA universelle Bezeichner für Anzeigen auf dem Gerät sind und nicht App-spezifisch. Um mobile Anzeigen-IDs für Nutzer:innen einer bestimmten App zu synchronisieren, können Sie Segmentfilter („Zuletzt verwendete bestimmte App“ oder „Neueste App-Version“) verwenden, um diese Nutzer:innen gezielt anzusprechen.

### Schritt 2: Google Audience-Schritt in Canvas hinzufügen {#step-2-add-a-google-audience-step-in-canvas}

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie dann **Audience Sync**.

![Das Menü zum Auswählen einer Canvas-Komponente im Editor.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Der Audience Sync-Schritt wurde zur User Journey hinzugefügt.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung {#step-3-sync-setup}

1. Wählen Sie **Custom Audience**, um den Komponenteneditor zu öffnen.
2. Wählen Sie **Google** als Audience Sync-Partner aus.

![Die Einstellungen des Audience Sync-Schritts mit der Option, einen Partner auszuwählen, um die Synchronisierung zu starten.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Wählen Sie das gewünschte Google-Anzeigenkonto aus.
4. Geben Sie in der Dropdown-Liste **Choose a New or Existing Audience** den Namen einer neuen oder bestehenden Zielgruppe ein.

{% tabs %}
{% tab Neue Zielgruppe erstellen %}

1. Geben Sie einen Namen für die neue angepasste Zielgruppe ein.
2. Wählen Sie **Add Users to Audience**.
3. Wählen Sie die First-Party-Nutzerdaten aus, die Sie an Ihre Zielgruppe senden möchten. Sie können wählen zwischen:

- **Customer Contact Info**: Enthält die E-Mail-Adressen oder Telefonnummern Ihrer Nutzer:innen, oder beides, wenn sie in Braze vorhanden sind. Google verlangt, dass es sich dabei um ein einziges Feld handelt, das synchronisiert wird, und nicht um separate Bezeichner. Sie können dieses einzelne Feld auch verwenden, wenn Sie nur einen der Bezeichner haben.
- **Mobile Advertiser ID**: Wählen Sie entweder iOS IDFA oder Android GAID. Aufgrund der Google Customer Match-Anforderungen können Sie nicht beide IDs für mobile Werbetreibende in denselben Kundenlisten haben.

{% alert note %}
**Über das Banner „Missing Mobile Ad IDs? Let's fix that.“:** Wenn Sie mit einer Zielgruppe synchronisieren, die iOS IDFA oder Android GAID als abzugleichendes Feld verwendet, kann diese Nachricht im Schritteditor erscheinen. Es handelt sich um eine **Information, nicht um einen Fehler**. Es erinnert Sie daran, zu bestätigen, dass das Feld für die mobile Anzeigen-ID, die Sie abgleichen möchten, in Ihren Zielgruppendaten vorhanden ist (zum Beispiel, dass Nutzer:innen im Canvas-Pfad den entsprechenden Bezeichner erfasst haben). Sie können es schließen, nachdem Sie Ihre Daten überprüft haben.
{% endalert %}

{: start="4"}
4. Als Nächstes speichern Sie Ihre Zielgruppe, indem Sie den Button **Create Audience** unten im Schritteditor auswählen.

![Erweiterte Ansicht der Komponente „Custom Audience“ in Canvas. Hier wird das gewünschte Anzeigenkonto ausgewählt, eine neue Zielgruppe erstellt und das Kontrollkästchen „Customer Contact Info“ aktiviert.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Nutzer:innen werden im oberen Bereich des Schritteditors benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn dabei Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um sie später in der Canvas Journey zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde.

![Eine Benachrichtigung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, erstellt Braze beim Start des Canvas eine neue angepasste Zielgruppe und synchronisiert anschließend die Nutzer:innen nahezu in Echtzeit, sobald sie den Google Audience-Schritt betreten.

{% alert important %}
Aufgrund der Anforderungen von Google Customer Match können Sie keine Kundenkontaktinformationen und IDs von mobilen Werbetreibenden in denselben Kundenlisten haben. Google Customer Match verwendet dann diese Informationen, um zu bestimmen, wer innerhalb von Google Search, Google Display, YouTube und Gmail als Targeting geeignet ist. Weitere Einzelheiten zu den Anforderungen von Google Customer Match finden Sie in der [Dokumentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Mit bestehender Zielgruppe synchronisieren %}

Braze bietet auch die Möglichkeit, Nutzer:innen aus bestehenden Google-Kundenlisten hinzuzufügen oder zu entfernen, um sicherzustellen, dass diese Zielgruppen aktuell sind. Zum Synchronisieren mit einer bestehenden Zielgruppe:

1. Wählen Sie eine bestehende angepasste Zielgruppe für die Synchronisierung aus.
2. Wählen Sie, ob Sie **Add to the audience** oder **Remove from the audience** möchten.
3. Braze fügt Nutzer:innen nahezu in Echtzeit hinzu oder entfernt sie, sobald sie den Google Audience-Schritt betreten.
4. Nachdem Sie Ihren Google Audience-Schritt konfiguriert haben, wählen Sie **Done**. Ihr Google Audience-Schritt enthält Details über die neue Zielgruppe.

![Erweiterte Ansicht der Komponente „Custom Audience“ in Canvas. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt sowie der Radiobutton „Add user to Audience“.]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten {#step-4-launch-canvas}

Vervollständigen Sie den Rest Ihrer User Journey in Canvas und starten Sie dann! Wenn Sie sich für die Erstellung einer neuen Zielgruppe entschieden haben, erstellt Braze die Zielgruppe innerhalb von Google und fügt dann Nutzer:innen hinzu, wenn sie diesen Schritt in Ihrem Canvas erreichen. Wenn Sie ausgewählt haben, Nutzer:innen einer bestehenden Zielgruppe hinzuzufügen oder zu entfernen, wird Braze Nutzer:innen entweder hinzufügen oder entfernen, wenn sie diesen Schritt in ihrer User Journey erreichen.

Die Nutzer:innen gehen dann zur nächsten Komponente des Canvas über, wenn es eine gibt, oder verlassen den Canvas, wenn es der letzte Schritt der User Journey ist.

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen die Audience Sync-Komponente erreichen, wird Braze diese Nutzer:innen nahezu in Echtzeit synchronisieren und dabei die Rate-Limits der Google Ads API beachten. In der Praxis bedeutet dies, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer:innen wie möglich zu verarbeiten, bevor diese an Google weitergeleitet werden.

Sobald Kund:innen kurz davor sind, das Rate-Limit der Google Ads API zu erreichen, gibt Google Braze eine Rückmeldung zu den Empfehlungen für Wiederholungsversuche. Erreichen Braze-Kund:innen ihr Rate-Limit, wird Braze Canvas die Synchronisierung für bis zu &#126;13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metrik „Users Errored“ aufgeführt.

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihres Audience Sync-Schrittes besser zu verstehen.

| Metrik | Beschreibung |
| ------ | ----------- |
| *Entered* | Anzahl der Nutzer:innen, die diesen Schritt betreten haben, um mit Google synchronisiert zu werden. |
| *Proceeded to Next Step* | Wie viele Nutzer:innen zur nächsten Komponente weitergeleitet wurden, falls es eine gibt. Alle Nutzer:innen werden automatisch weitergeleitet. Wenn dies der letzte Schritt in der Canvas-Verzweigung ist, wird diese Metrik 0 sein. |
| *Users Synced* | Anzahl der Nutzer:innen, die erfolgreich mit Google synchronisiert wurden. |
| *User Not Synced* | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen oder das Einwilligungsattribut auf `false` gesetzt wurde. |
| *Users Errored* | Anzahl der Nutzer:innen, die aufgrund eines Fehlers nicht mit Google synchronisiert wurden, nach &#126;13 Stunden Wiederholungsversuchen. Bei bestimmten Fehlern, wie z. B. Unterbrechungen der Google Ads API-Dienste, wird Canvas die Synchronisierung für bis zu &#126;13 Stunden wiederholen. Wenn die Synchronisierung zu diesem Zeitpunkt immer noch nicht möglich ist, wird das Feld *User Not Synced* ausgefüllt. |
| *Users Pending* | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Google verarbeitet werden. |
| *Exited Canvas* | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas ein Google-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum kann ich in meiner Google Audience-Schritt-Konfiguration nicht mehrere Felder für die Übereinstimmung auswählen? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google Customer Match stellt strenge Anforderungen an die Formatierung dieser Zielgruppen und die darin enthaltenen Kundeninformationen. Insbesondere müssen die IDs der mobilen Werbetreibenden getrennt von den Kundenkontaktinformationen (wie E-Mail und Telefonnummer) hochgeladen werden. Weitere Einzelheiten finden Sie in der [Dokumentation von Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Wie lange dauert es, bis meine Zielgruppen in Google synchronisiert sind? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Es kann zwischen 6 und 12 Stunden dauern, bis eine Zielgruppe mit Google synchronisiert ist.

### Ich habe eine Zielgruppe synchronisiert. Warum ist die Größe der Zielgruppe in Google gleich null? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Aus Datenschutzgründen wird die Größe der Nutzerliste auf null gesetzt, bis die Liste mindestens 1.000 Mitglieder hat. Danach wird die Größe auf die zwei höchstwertigen Stellen gerundet.

### Warum ist meine abgeglichene Zielgruppengröße in Google kleiner als die Anzahl der von Braze synchronisierten Nutzer:innen? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Obwohl Braze eine bestimmte Anzahl von Nutzer:innen an Google synchronisieren kann, kann die tatsächliche abgeglichene Zielgruppengröße, die Sie in Google Ads sehen, deutlich kleiner sein. Das liegt daran, dass Google die von Ihnen bereitgestellten Nutzerdaten (wie E-Mail-Adressen oder Telefonnummern) mit tatsächlichen Google-Konten auf ihrer Plattform abgleichen muss.

Selbst wenn Ihre Braze-Nutzerprofile gültige Abgleichsfelder enthalten, erscheinen Nutzer:innen nur dann in Ihrer angepassten Google-Zielgruppe, wenn sie ein Google-Konto mit übereinstimmenden Informationen haben.

Um Ihre Abgleichsrate zu verbessern:
- Stellen Sie sicher, dass Sie [Ihre Daten korrekt formatieren](https://support.google.com/google-ads/answer/7659867).
- Geben Sie nach Möglichkeit mehrere Bezeichner an (z. B. sowohl E-Mail als auch Telefonnummer).
- Beachten Sie, dass es 48 bis 72 Stunden dauern kann, bis Google Nutzer:innen verarbeitet und abgleicht, in einigen Fällen kann es jedoch mehrere Tage dauern.

Die endgültige abgeglichene Zielgruppengröße hängt vollständig vom Abgleichsprozess von Google ab. Braze hat keinen Einblick in den Abgleich von Google, sobald die Daten an deren Plattform übergeben wurden.

### Ich habe eine Zielgruppe mit Google synchronisiert, aber meine Anzeigen werden nicht geschaltet. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Vergewissern Sie sich, dass Ihre Zielgruppen mindestens 5.000 Nutzer:innen enthalten, damit die Anzeigenschaltung beginnen kann.

### Wie kann ich den Fehler „Mobile App IDs Deleted“ beheben? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Wenn Sie Zielgruppen mit Google synchronisieren, wird dieser Fehler ausgelöst, wenn Sie die Synchronisierung von mobilen Bezeichnern als Teil Ihrer Synchronisierungen ausgewählt haben, aber die IDs Ihrer mobilen Apps von der Google-Partnerseite gelöscht haben. Um dieses Problem zu beheben, stellen Sie sicher, dass Sie die entsprechenden IDs für mobile Apps für iOS und Android auf der Google-Partnerseite hinzugefügt haben.

### Warum habe ich eine E-Mail über ungültige Google Ads-Zugangsdaten erhalten, obwohl das Dashboard weiterhin als verbunden angezeigt wird? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Braze sendet diese E-Mail automatisch, wenn die Google API einen Autorisierungsfehler zurückgibt. Das kann auch dann passieren, wenn **Google Ads** im Dashboard weiterhin als verbunden angezeigt wird und Zielgruppen scheinbar synchronisiert werden – zum Beispiel, wenn das verbundene Google-Konto keine Berechtigung für eine bestimmte von Google angeforderte Aktion hat oder wenn die Google Ads-Nutzungsbedingungen für das Konto noch akzeptiert werden müssen.

Einige Autorisierungsfehler lösen sich von selbst. Überprüfen Sie die **Audience Sync**-Analytics Ihres Canvas (z. B. *Users Synced* und *Users Errored*), um zu bestätigen, ob Nutzer:innen weiterhin synchronisiert werden. Wenn Probleme bestehen bleiben, gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** > **Google Ads**, suchen Sie **Google Audience Sync** und verwenden Sie **Change Account**, um sich erneut mit einem Google Ads-Konto zu verbinden, das über den erforderlichen Zugriff und die abgeschlossene Einrichtung verfügt.