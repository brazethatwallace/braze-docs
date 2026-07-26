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

Die Braze Audience Sync to Google Integration ermöglicht es Marken, die Reichweite ihrer kanalübergreifenden geschäftskunden Journeys auf Google Search, Google Shopping, Gmail, YouTube und Google Display auszudehnen. Mithilfe Ihrer First-Party-Kundendaten können Sie Anzeigen auf der Grundlage von dynamischen Verhaltenstriggern, Segmentierung und mehr sicher zustellen. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (z. B. Push, E-Mail oder SMS) im Rahmen eines Braze-Canvas verwenden, kann verwendet werden, um eine Anzeige für diese Nutzer:innen über Googles [geschäftskunden Match](https://support.google.com/google-ads/answer/6379332?hl=en) zu triggern.

{% alert note %}
Die Braze Audience Sync to Google Integration wird für Google Ads unterstützt, nicht für Google Ads Manager.
{% endalert %}

Google Ads generiert keine ähnlichen Zielgruppen, auch bekannt als „Lookalike Audiences“, mehr für Targeting und Reporting. Lesen Sie die [Dokumentation von Google Ads](https://support.google.com/google-ads/answer/12463119?), um mehr zu erfahren.

**Häufige Anwendungsfälle für die Synchronisierung von angepassten Zielgruppen sind:**
{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

{% alert note %}
Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit Google geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, genauestens geprüft. Erfahren Sie mehr über unsere [Braze-Datenschutzrichtlinie](https://www.braze.com/privacy).
{% endalert %}

## Voraussetzungen {#prerequisites}

Stellen Sie sicher, dass die folgenden Punkte erstellt und abgeschlossen sind, bevor Sie Ihren Google Audience-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Google Ads-Konto | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Ein aktives Google Ads-Konto für Ihre Marke.<br><br>Wenn Sie eine Zielgruppe über mehrere verwaltete Konten hinweg teilen möchten, können Sie Ihre Zielgruppen in Ihr [Verwaltungskonto](https://support.google.com/google-ads/answer/6139186) hochladen. |
| Google Ads-Nutzungsbedingungen und Google Ads-Richtlinien | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Sie müssen die [Google Ads-Nutzungsbedingungen](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) und die [Google Ads-Richtlinien](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC) akzeptieren und deren Einhaltung sicherstellen, einschließlich der [EU-Richtlinie zur Nutzereinwilligung](https://www.google.com/about/company/user-consent-policy/), soweit für Sie zutreffend, bei Ihrer Nutzung von Braze Audience Sync.<br><br>Wenden Sie sich an Ihr Rechtsteam bezüglich Googles neuer EU-Richtlinie zur Nutzereinwilligung, um sicherzustellen, dass Sie die entsprechende Einwilligung einholen, um die Dienste von Google Ads für Ihre Endnutzer:innen im EWR, in Großbritannien und in der Schweiz zu nutzen. |
| Google geschäftskunden Match | [Google](https://support.google.com/google-ads/answer/6299717) | geschäftskunden Match ist nicht für alle Werbetreibenden verfügbar.<br><br>**Um geschäftskunden Match zu nutzen, muss Ihr Konto folgende Voraussetzungen erfüllen:**<br>• Eine gute Richtlinien-Compliance-Historie<br>• Eine gute Zahlungshistorie<br>• Mindestens 90 Tage Historie in Google Ads<br>• Mehr als 50.000 USD Gesamtausgaben über die gesamte Lifetime. Für Werbetreibende, deren Konten in anderen Währungen als USD geführt werden, wird Ihr Ausgabenbetrag anhand des durchschnittlichen monatlichen Wechselkurses für diese Währung in USD umgerechnet.<br><br>Wenn Ihr Konto diese Kriterien nicht erfüllt, ist Ihr Konto derzeit nicht berechtigt, geschäftskunden Match zu nutzen.<br><br>Wenden Sie sich an Ihre Google Ads-Vertretung, um weitere Informationen zur Verfügbarkeit von geschäftskunden Match für Ihr Konto zu erhalten. |
| Google-Einwilligungssignale | [Google](https://support.google.com/google-ads/answer/14310715) | Wenn Sie Endnutzer:innen im EWR über Googles geschäftskunden Match-Dienst Werbung ausspielen möchten, müssen Sie Braze die folgenden angepassten Attribute (Boolean) im Rahmen von Googles EU-Richtlinie zur Nutzereinwilligung übergeben. Weitere Details finden Sie unter [Einwilligung für Endnutzer:innen im EWR, in Großbritannien und in der Schweiz einholen](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

### Erforderliche SDK-Versionen {#required-sdk-versions}

Wenn Sie Braze-SDKs verwenden, um Einwilligungssignale zu erfassen, stellen Sie sicher, dass Sie die folgenden Mindestversionen einsetzen:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Einwilligung für Endnutzer:innen im EWR, in Großbritannien und in der Schweiz einholen {#collecting-consent-for-eea-uk-and-switzerland-end-users}

Googles EU-Richtlinie zur Nutzereinwilligung verlangt von Werbetreibenden, ihren Endnutzer:innen im EWR, in Großbritannien und in der Schweiz Folgendes offenzulegen und deren Einwilligung dafür einzuholen:

* Die Verwendung von Cookies oder anderen lokalen Speichermethoden, sofern gesetzlich vorgeschrieben; und
* Die Erhebung, Weitergabe und Nutzung ihrer personenbezogenen Daten zur Personalisierung von Werbung.

Dies betrifft keine Endnutzer:innen in den USA oder andere Endnutzer:innen außerhalb des EWR, Großbritanniens oder der Schweiz. Wenden Sie sich an Ihr Rechtsteam bezüglich Googles neuer EU-Richtlinie zur Nutzereinwilligung, um sicherzustellen, dass Sie die entsprechende Einwilligung einholen, um die Dienste von Google Ads für Ihre Endnutzer:innen im EWR, in Großbritannien und in der Schweiz zu nutzen.

Gemäß den Anforderungen des Digital Markets Act (DMA), die seit dem 6. März 2024 gelten, müssen Werbetreibende die Einwilligung für Endnutzer:innen im EWR, in Großbritannien und in der Schweiz übermitteln, wenn sie Daten mit Google teilen. Im Rahmen dieser Änderung können Sie beide Einwilligungssignale in Braze als die folgenden angepassten Boolean-Attribute erfassen:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze synchronisiert die Daten aus diesen angepassten Attributen mit den entsprechenden [Einwilligungsfeldern bei Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Widerrufene Einwilligung verwalten {#managing-revoked-consent}

Um Ihre Zielgruppenlisten aktuell zu halten, falls Endnutzer:innen im EWR zur Zielgruppenliste hinzugefügt wurden und anschließend eine der beiden Einwilligungen (`$google_ad_user_data` oder `$google_ad_personalization`) widerrufen haben, müssen Sie einen Canvas einrichten, um Nutzer:innen mithilfe eines Audience Sync-Schritts aus den bestehenden Zielgruppenlisten zu entfernen.

{% alert note %}
Wenn Endnutzer:innen im EWR zuvor die Einwilligung für beide Signale erteilt haben, werden diese Daten weiterhin für Googles geschäftskunden Match verwendet, bis die Liste abläuft, der Einwilligungsstatus explizit über Google Audience Sync aktualisiert wird, oder beides.
{% endalert %}

#### Tipps {#tips}

* Senden Sie den Wert als Boolean-Typ, nicht als String-Typ.
* Stellen Sie dem Attributnamen ein Dollarzeichen ($) voran. Braze verwendet ein Dollarzeichen am Anfang eines Attributnamens, um anzuzeigen, dass es sich um einen speziellen und reservierten Schlüssel handelt.
* Geben Sie den Attributnamen in Kleinbuchstaben ein.
* Sie können zwar nicht explizit festlegen, dass eine Nutzer:in als „nicht angegeben“ gilt, aber wenn Sie einen `null`- oder `nil`-Wert oder einen Wert senden, der weder `true` noch `false` ist, übergibt Braze diese Nutzer:in an Google als `UNSPECIFIED`.
* Neue Nutzer:innen, die hinzugefügt oder aktualisiert werden, ohne dass eines der Einwilligungsattribute angegeben wird, werden mit diesen Einwilligungsattributen als „nicht angegeben“ an Google synchronisiert.

Wenn Sie versuchen, Nutzer:innen im EWR ohne die erforderlichen Einwilligungsfelder und den gewährten Status zu synchronisieren, wird Google dies ablehnen und diesen Nutzer:innen keine Werbung ausspielen. Darüber hinaus können Sie haftbar gemacht werden und einem finanziellen Risiko ausgesetzt sein, wenn Werbung an Endnutzer:innen im EWR ohne deren ausdrückliche Einwilligung ausgespielt wird. Um dies zu vermeiden, empfehlen wir, Campaigns mit Segment-Filtern zu senden, die nur Nutzer:innen im EWR, in Großbritannien und in der Schweiz mit `true` Google-Einwilligungsattributen einschließen. Weitere Details zur EU-Richtlinie zur Nutzereinwilligung für geschäftskunden Match-Upload-Partner finden Sie in Googles [FAQs](https://support.google.com/google-ads/answer/14310715).

### Ihren Canvas einrichten {#setting-up-your-canvas}

Nachdem Sie die Synchronisierung mit Braze durchgeführt haben, stehen die folgenden Einwilligungsattribute in Ihren Nutzerprofilen und für die Segmentierung zur Verfügung:

- `$google_ad_user_data`
- `$google_ad_personalization`

In jedem Canvas, in dem Sie Endnutzer:innen im EWR, in Großbritannien und in der Schweiz über einen Google Audience Sync ansprechen, um Nutzer:innen zu einer Zielgruppe hinzuzufügen, müssen Sie diese Nutzer:innen ausschließen, wenn eines der beiden Einwilligungsattribute einen anderen Wert als `true` hat. Sie können dies tun, indem Sie diese Nutzer:innen segmentieren, wenn die Einwilligungswerte auf `true` gesetzt sind. Dies stellt auch sicher, dass die Analytics der synchronisierten Nutzer:innen genauer sind, da wir wissen, dass Google diese Nutzer:innen aus den Zielgruppen ablehnen wird. Beachten Sie, dass Einwilligungsattribute nicht erforderlich sind, wenn Sie Google Audience Sync verwenden, um Nutzer:innen aus einer Zielgruppe zu entfernen.

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

- **geschäftskunden Contact Info**: Enthält die E-Mail-Adressen oder Telefonnummern Ihrer Nutzer:innen, oder beides, wenn sie in Braze vorhanden sind. Google verlangt, dass es sich dabei um ein einziges Feld handelt, das synchronisiert wird, und nicht um separate Bezeichner. Sie können dieses einzelne Feld auch verwenden, wenn Sie nur einen der Bezeichner haben.
- **Mobile Advertiser ID**: Wählen Sie entweder iOS IDFA oder Android GAID. Aufgrund der Google geschäftskunden Match-Anforderungen können Sie nicht beide IDs für mobile Werbetreibende in denselben Kundenlisten haben.

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
Aufgrund der Anforderungen von Google geschäftskunden Match können Sie keine Kundenkontaktinformationen und IDs von mobilen Werbetreibenden in denselben Kundenlisten haben. Google geschäftskunden Match verwendet dann diese Informationen, um zu bestimmen, wer innerhalb von Google Search, Google Display, YouTube und Gmail als Targeting geeignet ist. Weitere Einzelheiten zu den Anforderungen von Google geschäftskunden Match finden Sie in der [Dokumentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
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

## Synchronisierung von Nutzer:innen und Überlegungen zu Rate-Limits {#user-syncing-and-rate-limit-considerations}

Wenn Nutzer:innen die Audience-Sync-Komponente erreichen, synchronisiert Braze diese Nutzer:innen nahezu in Echtzeit und berücksichtigt dabei die Rate-Limits der Google Ads API. In der Praxis bedeutet dies, dass Braze versucht, alle 5 Sekunden so viele Nutzer:innen wie möglich zu bündeln und zu verarbeiten, bevor sie an Google gesendet werden.

Sobald ein:e geschäftskunden kurz davor ist, das Rate-Limit der Google Ads API zu erreichen, gibt Google Braze Rückmeldungen zu Wiederholungsempfehlungen. Wenn ein:e Braze-geschäftskunden das Rate-Limit erreicht, versucht Braze im Canvas die Synchronisierung bis zu &#126;13 Stunden lang erneut. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metrik „Fehlerhafte Nutzer:innen“ aufgeführt.

## Analytics verstehen {#understanding-analytics}

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihres Audience-Sync-Schritts besser zu verstehen.

| Metrik | Beschreibung |
| ------ | ----------- |
| *Eingetreten* | Anzahl der Nutzer:innen, die diesen Schritt betreten haben, um mit Google synchronisiert zu werden. |
| *Zum nächsten Schritt fortgefahren* | Wie viele Nutzer:innen zur nächsten Komponente vorgerückt sind, falls eine vorhanden ist. Alle Nutzer:innen rücken automatisch vor. Wenn dies der letzte Schritt im Canvas-Zweig ist, beträgt diese Metrik 0. |
| *Synchronisierte Nutzer:innen* | Anzahl der Nutzer:innen, die erfolgreich mit Google synchronisiert wurden. |
| *Nicht synchronisierte Nutzer:innen* | Anzahl der Nutzer:innen, die aufgrund fehlender Abgleichfelder oder weil das Einwilligungsattribut auf `false` gesetzt war, nicht synchronisiert wurden. |
| *Fehlerhafte Nutzer:innen* | Anzahl der Nutzer:innen, die nach &#126;13 Stunden Wiederholungsversuchen aufgrund eines Fehlers nicht mit Google synchronisiert wurden. Bei bestimmten Fehlern, wie Unterbrechungen des Google-Ads-API-Dienstes, wiederholt Canvas die Synchronisierung bis zu &#126;13 Stunden lang. Wenn die Synchronisierung zu diesem Zeitpunkt immer noch nicht möglich ist, wird *Nicht synchronisierte Nutzer:innen* befüllt. |
| *Ausstehende Nutzer:innen* | Anzahl der Nutzer:innen, die derzeit von Braze zur Synchronisierung mit Google verarbeitet werden. |
| *Canvas verlassen* | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies tritt auf, wenn der letzte Schritt in einem Canvas ein Google-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics verstehen" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum kann ich in meiner Google Audience-Schritt-Konfiguration nicht mehrere Felder zum Abgleich auswählen? {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google geschäftskunden Match hat strenge Anforderungen an die Formatierung dieser Zielgruppen und die enthaltenen Kundeninformationen. Insbesondere müssen mobile Werbe-IDs getrennt von Kundenkontaktinformationen (wie E-Mail und Telefonnummer) hochgeladen werden. Weitere Einzelheiten finden Sie in der [Google geschäftskunden Match-Dokumentation](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Wie lange dauert es, bis meine Zielgruppen in Google synchronisiert sind? {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Es kann zwischen 6 und 12 Stunden dauern, bis eine Zielgruppe in Google synchronisiert ist.

### Ich habe eine Zielgruppe synchronisiert – warum zeigt Google die Zielgruppengröße als null an? {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

Aus Datenschutzgründen wird die Größe der Nutzerliste als null angezeigt, bis die Liste mindestens 1.000 Mitglieder hat. Danach wird die Größe auf die zwei signifikantesten Stellen gerundet.

### Warum ist meine abgeglichene Zielgruppengröße in Google niedriger als die Anzahl der von Braze synchronisierten Nutzer:innen? {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Obwohl Braze eine bestimmte Anzahl von Nutzer:innen an Google synchronisieren kann, kann die tatsächliche abgeglichene Zielgruppengröße, die Sie in Google Ads sehen, deutlich niedriger sein. Das liegt daran, dass Google die von Ihnen bereitgestellten Nutzerdaten (wie E-Mail-Adressen oder Telefonnummern) mit tatsächlichen Google-Konten auf ihrer Plattform abgleichen muss.

Selbst wenn Ihre Braze-Nutzerprofile gültige Abgleichfelder enthalten, erscheinen Nutzer:innen nur in Ihrer Google Custom Audience, wenn sie ein Google-Konto mit übereinstimmenden Informationen haben.

So verbessern Sie Ihre Abgleichrate:
- Stellen Sie sicher, dass Sie [Ihre Daten korrekt formatieren](https://support.google.com/google-ads/answer/7659867).
- Geben Sie nach Möglichkeit mehrere Bezeichner an (zum Beispiel sowohl E-Mail als auch Telefonnummer).
- Beachten Sie, dass es 48 bis 72 Stunden dauern kann, bis Google Nutzer:innen verarbeitet und abgleicht, wobei es in einigen Fällen mehrere Tage dauern kann.

Die endgültige abgeglichene Zielgruppengröße hängt vollständig vom Abgleichprozess von Google ab. Braze hat keinen Einblick in den Abgleich von Google, sobald die Daten an deren Plattform übergeben wurden.

### Ich habe eine Zielgruppe in Google synchronisiert, aber meine Anzeigen werden nicht ausgeliefert. {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

Überprüfen Sie, ob Ihre Zielgruppen mindestens 5.000 Nutzer:innen enthalten, damit Anzeigen ausgeliefert werden können.

### Wie behebe ich den Fehler „Mobile App IDs Deleted“? {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Wenn Sie Zielgruppen mit Google synchronisieren, wird dieser Fehler ausgelöst, wenn Sie mobile Bezeichner als Teil Ihrer Synchronisierungen ausgewählt, aber Ihre mobilen App-IDs von der Google-Partnerseite gelöscht haben. Um dieses Problem zu beheben, stellen Sie sicher, dass Sie die entsprechenden mobilen App-IDs für iOS und Android auf der Google-Partnerseite hinzugefügt haben.

### Warum habe ich eine E-Mail über ungültige Google Ads-Zugangsdaten erhalten, obwohl das Dashboard die Verbindung noch als aktiv anzeigt? {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Braze sendet diese E-Mail automatisch, wenn die Google-API einen Autorisierungsfehler zurückgibt. Das kann auch dann passieren, wenn **Google Ads** im Dashboard weiterhin als verbunden angezeigt wird und Zielgruppen scheinbar synchronisiert werden – zum Beispiel, wenn das verbundene Google-Konto keine Berechtigung für eine bestimmte von Google angeforderte Aktion hat oder wenn die Google Ads-Nutzungsbedingungen für das Konto noch akzeptiert werden müssen.

Einige Autorisierungsfehler lösen sich von selbst. Überprüfen Sie Ihre Canvas-**Audience Sync**-Analytics (zum Beispiel *Users Synced* und *Users Errored*), um zu bestätigen, ob Nutzer:innen weiterhin synchronisiert werden. Wenn die Probleme weiterhin bestehen, gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** > **Google Ads**, suchen Sie **Google Audience Sync** und verwenden Sie **Change Account**, um sich erneut mit einem Google Ads-Konto zu verbinden, das über den erforderlichen Zugriff und eine abgeschlossene Einrichtung verfügt.