---
nav_title: Facebook
article_title: Facebook Audience Export
alias: /partners/facebook/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Facebook, einer führenden sozialen Plattform, über die Marken ihre Kund:innen erreichen und mit ihnen in Kontakt treten können."
page_type: partner
search_tag: Partner
---

# Facebook Audience exportieren {#facebook-audience-export}

> Die Integration von Braze und Facebook ermöglicht es Ihnen, Ihre Braze-Segmente manuell nach Facebook zu exportieren, um Facebook Custom Audiences zu erstellen. Dies ist ein einmaliger, statischer Zielgruppenexport und erstellt nur neue Facebook Custom Audiences.

Häufige Anwendungsfälle für den Export von Facebook Custom Audiences sind:
- Retargeting von Nutzer:innen zu bestimmten Zeitpunkten in ihrem Lebenszyklus
- Erstellen von Listen für das Ausschluss-Targeting
- Erstellen von [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) zur effizienteren Gewinnung neuer Nutzer:innen
<br><br>

{% alert note %}
Der Facebook Audience Export verwendet das **User Access Token / Textbaustein**, um Anfragen zu autorisieren.<br><br>
Wenn Sie dieses Feature zusammen mit dem Feature [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook) verwenden, verwendet Braze standardmäßig das zuverlässigere **System User Token / Textbaustein**, das Sie bereits erstellt haben, um Anfragen zu autorisieren.
{% endalert %}

{% alert note %}
Wenn Sie an den Beta-Tests für Meta Work Accounts teilnehmen, stellen Sie sicher, dass Sie Ihr Konto von der [Facebook-Partnerseite]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync#step-1-connect-to-facebook) trennen und erneut verbinden.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Voraussetzung | Beschreibung |
| ----------- | ----------- |
| [Facebook Business Manager:in](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (zum Beispiel Werbekonten, Seiten, Apps). |
| [Facebook-Werbekonto](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Ein aktives Facebook-Werbekonto, das mit dem Business Manager:in Ihrer Marke verknüpft ist und das Sie mit Custom Audiences von Braze verwenden möchten.<br><br>Stellen Sie sicher, dass Ihr Facebook Business Manager:in-Administrator Ihnen Administratorberechtigungen für die Facebook-Werbekonten erteilt hat, die Sie mit Braze verwenden möchten, und dass Sie die Geschäftsbedingungen Ihres Werbekontos akzeptiert haben. Andernfalls können Sie in Braze auf keine Facebook-Werbekonten zugreifen. |
| [Facebook Custom Audiences-Nutzungsbedingungen](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Sie müssen die Custom Audiences-Nutzungsbedingungen von Facebook für die Facebook-Werbekonten akzeptieren, die Sie mit Braze verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Mit Facebook verbinden {#step-1-connect-to-facebook}

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Facebook** aus.

{: start="2"}
2. Wählen Sie im Modul „Facebook Audience Export“ die Option **Connect Facebook** aus. <br><br>![Technologie-Partnerseite von Facebook auf der Braze-Plattform.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. Autorisieren Sie im Facebook-oAuth-Dialogfenster Braze, Custom Audiences in Ihren Facebook-Werbekonten zu erstellen. <br><br>![Das erste Facebook-Dialogfeld mit der Aufforderung „Verbinden als X“, wobei X Ihr Facebook-Benutzername ist.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![Das zweite Facebook-Dialogfeld, in dem Sie um die Erlaubnis gebeten werden, Anzeigen für Ihre Werbekonten zu verwalten.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Nachdem Braze mit Ihrem Facebook-Konto verknüpft ist, wählen Sie aus, welche Werbekonten Sie in Ihrem Braze-Workspace synchronisieren möchten. <br><br>![Eine Liste der verfügbaren Werbekonten, die Sie mit Facebook verbinden können.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Nachdem Sie die Verbindung hergestellt haben, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind, und bestehende Konten trennen können. <br><br> ![Eine aktualisierte Version der Technologie-Partnerseite von Facebook, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Ihre Facebook-Verbindung wird auf der Ebene des Braze-Workspace angewendet. Wenn Ihr Facebook-Administrator Sie aus Ihrem Facebook Business Manager:in oder dem Zugriff auf die verbundenen Facebook-Konten entfernt, erkennt Braze ein ungültiges Token / Textbaustein. Infolgedessen zeigen Ihre aktiven Canvases, die Facebook-Audience-Schritte verwenden, Fehler an, und Braze kann keine Nutzer:innen synchronisieren.

{% alert important %}
Für Kund:innen, die bereits den Facebook-App-Überprüfungsprozess für [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) und [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) durchlaufen haben, ist Ihr System User Token / Textbaustein für den Facebook-Audience-Schritt weiterhin gültig. Sie können das Facebook System User Token / Textbaustein nicht über die Facebook-Partnerseite bearbeiten oder widerrufen. Stattdessen können Sie Ihr Facebook-Konto verbinden, um Ihr Facebook System User Token / Textbaustein in Ihrem Braze-Workspace zu ersetzen.

<br><br>Die neue Facebook-oAuth-Konfiguration gilt auch für [Facebook-Exporte über Segmente]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Schritt 2: Ihre Nutzer:innen nach Facebook exportieren {#step-2-export-your-users-into-facebook}

In Braze ist der Facebook Audience Export über die Seite **Segments** zugänglich.

1. Wählen Sie auf der Seite **Segments** das Segment aus, das Sie exportieren möchten.
2. Wählen Sie **User Data** und dann **Export as Facebook Audience**. <br><br>![Der Abschnitt „Segmentdetails“ eines Segments, in dem „User Data“ ausgewählt ist und eine Dropdown-Liste mit Optionen angezeigt wird, die „Export as Facebook Audience“ enthält.]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Wenn Sie Facebook in Braze noch nicht aktiviert haben, werden Sie aufgefordert, die Facebook-Technologie-Partnerseite im Dashboard aufzurufen. Wenn Sie Facebook bereits über **Technologie-Partner** > **Facebook** aktiviert haben, können Sie Ihr Facebook-Werbekonto und die zu exportierenden Nutzer:innen-Felder auswählen. <br><br> Sie können die folgenden Felder exportieren:
- Geräte-IDFA
- Telefonnummer
- E-Mail

{% alert note %}
Sie können in einem einzelnen Export nur ein Nutzer:innen-Feld auswählen. Wenn Sie mehr als einen Datentyp auswählen, erstellt Braze für jeden eine eigene Custom Audience.
{% endalert %}

{: start="4"}
4. Nachdem Sie das Nutzer:innen-Feld ausgewählt haben, wählen Sie **Export Segment**. Wie beim CSV-Export erhalten Sie eine E-Mail, wenn der Export des Segments nach Facebook abgeschlossen ist.
5. Sehen Sie sich die Custom Audience im [Facebook Ads Manager:in](https://www.facebook.com/ads/manager/audiences/manage/) an.

{% alert important %}
Aus Datenschutzgründen erlaubt Facebook es Ihnen nicht, Folgendes zu sehen:

- Die genauen Nutzer:innen, die erfolgreich zu einer Custom Audience hinzugefügt wurden. [Erfahren Sie, warum Facebook einzelne Zielgruppenmitglieder ausblendet](https://www.facebook.com/business/help/112061095610075).
- Die Größe der Custom Audience. [Erfahren Sie mehr über die Änderungen bei der Schätzung der Zielgruppengröße durch Facebook](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923).
{% endalert %}

#### Konfigurieren Sie Ihren Zielgruppenexport {#configuring-your-audience-export}

Beim Aufbau von Facebook-Zielgruppen können Sie bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, wie z. B. das Recht „Nicht verkaufen oder teilen“ gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen.

- Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection) erfasst haben, können Sie den Filter **Ads Tracking Enabled** verwenden. Wählen Sie den Wert `true` aus, um Nutzer:innen nur in Audience-Sync-Ziele zu senden, für die sie ein Opt-in gegeben haben.

![Canvas-Eingangsfilter, bei dem „Ads Tracking Enabled“ auf „true“ gesetzt ist.]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Wenn Sie Opt-ins, Opt-outs, `Do Not Sell Or Share` oder andere angepasste Attribute erfassen, sollten Sie diese als Filter in Ihre Canvas-Eingangskriterien aufnehmen:

![Ein Canvas mit einer Entry-Zielgruppe, bei der „opted_in_marketing“ gleich „true“ ist.]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Lookalike Audiences

Sobald Sie ein Segment erfolgreich als Facebook Audience exportiert haben, können Sie mit Facebook [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) weitere Gruppen erstellen. Dieses Feature betrachtet die demografischen Daten, Interessen und anderen Attribute der von Ihnen gewählten Zielgruppe und erstellt eine neue Zielgruppe mit ähnlichen Attributen.

## Fehlerbehebung {#troubleshooting}

### Fehler bei der Validierung des Zugriffstokens {#error-validating-access-token}

Bei Verwendung des Facebook-Exports erscheint der Fehler `Error Validating Access Token`, wenn:
- Sie Ihr Passwort geändert haben, wodurch Ihre aktuelle Sitzung ungültig wird
- Facebook Sie als Sicherheitsmaßnahme abgemeldet hat

Um diesen Fehler zu beheben, führen Sie die folgenden Schritte aus:
1. Melden Sie sich bei Facebook ab und dann wieder an.
2. Entfernen Sie in Braze Ihre Facebook-Zugangsdaten und speichern Sie. Bestätigen Sie, dass die Zugangsdaten entfernt wurden, indem Sie versuchen, ein Segment zu exportieren (das Exportsymbol sollte deaktiviert sein).
3. Fügen Sie Ihre Facebook-Zugangsdaten erneut hinzu und speichern Sie.
4. Versuchen Sie erneut zu exportieren.

Wenn der Export nicht funktioniert, gehen Sie wie folgt vor:
1. Entfernen Sie Ihre Zugangsdaten erneut und speichern Sie.
2. Fügen Sie Ihre Zugangsdaten erneut hinzu und speichern Sie.
3. Trennen Sie die Facebook-Integration auf der **Technologie-Partnerseite** und verbinden Sie sie erneut.

### Fehler beim Exportieren einer Facebook Audience {#error-when-exporting-a-facebook-audience}

Wenn beim Exportieren eines Segments als Facebook Audience ein Fehler auftritt, nennt die Entwicklerdokumentation von Facebook die folgenden häufigen Ursachen:

1. **Das Zugriffstoken stammt von einer Person, die kein Admin der App und des Werbekontos ist:** Die Facebook-Nutzer:innen, deren Zugangsdaten mit Braze verbunden sind, müssen über die richtigen Berechtigungen verfügen.
2. **Das Werbekonto, in das Sie exportieren, ist nicht mit Ihrer App verknüpft:** Das Facebook-Werbekonto muss in den Facebook-Einstellungen mit Ihrer App verknüpft sein.

Verwenden Sie die folgenden Prüfungen, um Ihre Einrichtung zu überprüfen:

- **Prüfen Sie, ob Sie Admin der App sind:** Gehen Sie zu [developers.facebook.com](https://developers.facebook.com/), öffnen Sie **My Apps** und wählen Sie die App Ihres Unternehmens aus. Wenn Sie die App nicht sehen, muss Ihr Entwicklungsteam Sie möglicherweise hinzufügen. Gehen Sie im Dashboard der App zu **Roles**, um Ihre Rolle zu bestätigen (Admin, Developer, Tester oder Analytics User).
- **Prüfen Sie, ob Ihr Werbekonto mit Ihrer App verknüpft ist:** Gehen Sie im Facebook App Dashboard zu **Settings** > **Advanced**, scrollen Sie zu **Advertising Accounts** und fügen Sie die Facebook-Werbekonto-ID hinzu, die Sie für Braze-Zielgruppenexporte verwenden möchten, falls sie noch nicht aufgeführt ist.
- **Prüfen Sie, ob Sie Admin des Werbekontos sind:** Gehen Sie zu [business.facebook.com](https://business.facebook.com/), öffnen Sie **Business Settings** über das Hauptmenü und navigieren Sie dann zu **Accounts** > **Ad accounts**. Wählen Sie das Werbekonto aus. Bestätigen Sie Ihren Zugriff und dass Sie über die erforderlichen Berechtigungen zum Erstellen von Custom Audiences verfügen.

Weitere Details finden Sie in der [Custom-Audience-API-Dokumentation von Facebook](https://developers.facebook.com/docs/) und im [Business-Hilfecenter-Leitfaden von Facebook zu Custom Audiences](https://www.facebook.com/business/help).