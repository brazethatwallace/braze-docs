---
nav_title: Facebook Lead Ads über Zapier
article_title: Facebook Lead Ads über Zapier
description: "Dieser Referenzartikel beschreibt die Integration zwischen Braze und Facebook Lead Ads über Zapier, um die Übertragung von Lead-Daten von Facebook an Braze zu automatisieren und so Engagement in Realtime und personalisierte Folgeaktionen zu ermöglichen."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Facebook Lead Ads über Zapier – Integration {#facebook-lead-ads-via-zapier-integration}

> Mit der Facebook Lead Ads Integration über <a href="https://zapier.com/" target="_blank">Zapier</a> können Sie Ihre Leads aus Facebook in Braze importieren und ein angepasstes Event verfolgen, wenn Leads erfasst werden.

Facebook Lead Ads ist ein Anzeigenformat, das es Unternehmen erlaubt, Lead-Informationen direkt in Facebook zu sammeln. Diese Anzeigen wurden entwickelt, um den Prozess der Lead-Generierung einfach und nahtlos zu gestalten. Indem Sie eine Zapier-Integration und Braze nutzen, können Sie die Übertragung von Lead-Daten von Facebook zu Braze automatisieren und so Engagement in Realtime und personalisierte Folgeaktionen ermöglichen.

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| Zapier-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zapier-Konto. Diese Integration erfordert die Verwendung von <a href="https://zapier.com/app/pricing/" target="_blank">Premium-Apps von Zapier</a>. Stellen Sie also sicher, dass Ihr Zapier-Tarif Zugang zu Premium-Apps hat. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebook-Leads-Zugang</a> | Der Zugang zu Facebook Leads ist für jedes Anzeigenkonto erforderlich, das Sie mit Braze verwenden möchten. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | Im Rahmen dieser Integration verwenden Sie den Facebook Business Manager, ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten und Apps). |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook-Anzeigenkonto</a> | Sie benötigen ein aktives Facebook-Anzeigenkonto, das mit dem Business Manager Ihrer Marke verknüpft ist. <br><br>Stellen Sie sicher, dass Sie die Berechtigung „Anzeigenkonten verwalten“ für jedes Anzeigenkonto haben, das Sie mit Braze verwenden möchten, und dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Facebook-Seite</a> | Sie benötigen eine aktive Facebook-Seite, die mit dem Business Manager Ihrer Marke verknüpft ist. <br><br>Stellen Sie sicher, dass Sie die Berechtigung „Seiten verwalten“ für jede Facebook-Seite haben, die Sie mit Braze verwenden möchten. |
| Braze-REST-Endpunkt | Stellen Sie sicher, dass Sie die [URL Ihres REST-Endpunkts]({{site.baseurl}}/api/basics#api-definitions) kennen. Ihr API-Endpunkt entspricht der Dashboard-URL für Ihre Braze-Instanz. <br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`. |
| Braze-REST-API-Schlüssel | Stellen Sie sicher, dass Sie über einen Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen verfügen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Erstellen Sie eine Lead-Ads-Campaign mit einem Sofortformular {#step-1-create-a-lead-ads-campaign-with-an-instant-form}

Erstellen Sie im Facebook Ads Manager eine <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebook-Leads-Campaign und ein Facebook-Lead-Ads-Formular</a>.

Sie können entweder eine E-Mail-Adresse oder eine Telefonnummer verwenden, wenn Sie eine Anfrage an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) stellen, um das Nutzerprofil zu aktualisieren oder zu erstellen. Fügen Sie daher ein **Kontaktfeld** für **E-Mail** oder **Telefon** in Ihr Lead-Anzeigenformular ein. Wenn Sie Vornamen oder Nachnamen erfassen, sammeln Sie diese separat in Ihrem Formular, anstatt vollständige Namen zu verwenden.

### Schritt 2: Verbinden Sie Ihr Facebook-Konto mit Zapier {#step-2-connect-your-facebook-account-to-zapier}

#### Schritt 2a: Wählen Sie Ihre Verbindungsmethode in Zapier aus {#step-2a-select-your-connection-method-in-zapier}

Gehen Sie in Zapier auf **Apps**, um nach verfügbaren Facebook-Apps zu suchen. Wählen Sie entweder **Facebook Lead Ads** oder **Facebook Lead Ads (for Business admins)**.

Weitere Informationen zu diesen beiden Methoden, um Ihr Facebook-Konto mit Zapier zu verbinden, finden Sie hier:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![Zapier-App-Suche mit Verbindungsoptionen für Facebook Lead Ads.]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Schritt 2b: Zapier zum Leads-Zugang im Facebook Business Manager hinzufügen {#step-2b-add-zapier-to-leads-access-in-facebook-business-manager}

Gehen Sie in Ihrem Facebook Business Manager im Navigationsmenü auf **Integrations** > **Leads Access**. Wählen Sie Ihre Facebook-Seite aus und klicken Sie dann auf **CRMs**. Auf dem CRM-Tab wählen Sie **Assign CRMs** und fügen **Zapier** hinzu.

![Facebook Business Manager Leads-Access-Seite mit Zapier als zugewiesener CRM-Integration.]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Die Schritte zur Zuweisung von Zapier als CRM-Integration finden Sie in der <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">Dokumentation</a> von Facebook.

### Schritt 3: Erstellen Sie Ihren Zap {#step-3-create-your-zap}

#### Schritt 3a: Erstellen Sie den Trigger {#step-3a-create-the-trigger}

Sobald Sie Ihr Facebook-Konto verbunden haben, können Sie mit der Erstellung eines Zap fortfahren. Wählen Sie als **Trigger** **Facebook Lead Ads** oder **Facebook Lead Ads (for Business Admins)**, je nachdem, was Sie in Schritt 2 ausgewählt haben.

![Zapier-Trigger-Schritt mit ausgewähltem Facebook Lead Ads.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

Wählen Sie für das **Event** die Option **New Leads** > **Continue**.

![Zapier-Trigger-Event-Auswahl mit „New Leads“.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Wählen Sie Ihr Facebook-Konto aus und klicken Sie auf **Continue**.

![Zapier-Schritt zur Verbindung des Facebook-Kontos für den Trigger.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Wählen Sie Ihre Facebook-Seite und das zuvor erstellte Sofortformular aus und klicken Sie auf **Continue**.

![Zapier-Trigger-Konfiguration mit Auswahl einer Facebook-Seite und eines Sofortformulars.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

Testen Sie nun diesen Trigger. Nachdem Sie Ihre Formularausgabe validiert haben, wählen Sie **Continue with selected record**.

#### Schritt 3b: Eine Aktion erstellen {#step-3b-create-an-action}

Fügen Sie einen neuen Schritt hinzu und wählen Sie dann **Webhooks by Zapier**. Wählen Sie als Nächstes für das Feld **Event** die Option **Custom Request** aus und klicken Sie dann auf **Continue**.

![Zapier-Aktionsschritt konfiguriert mit „Webhooks by Zapier“ und „Custom Request“.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Zum Schluss richten Sie Ihre angepasste Anfrage ein, indem Sie Felder in Ihre Nutzlast einfügen. Das folgende Code-Snippet zeigt eine Beispiel-Nutzlast.

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Hier sehen Sie ein Beispiel dafür, wie dies in Zapier aussieht:

![Beispiel für die Webhook-Nutzlast-Zuordnung in Zapier zum Senden von Facebook-Lead-Feldern an Braze.]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

Nachdem Sie Ihren Webhook konfiguriert haben, wählen Sie **Continue and test**. Wenn der Test erfolgreich ist, können Sie Ihren Zap veröffentlichen.

### Schritt 4: Testen Sie Ihren Facebook-Lead-Ads-Zap {#step-4-test-your-facebook-lead-ads-zap}

Um dies End-to-End zu testen, verwenden Sie das Lead-Ads-Testing-Tool von Facebook in Ihrer Facebook-Entwicklungskonsole. Weitere Informationen finden Sie unter <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testen und Fehlerbehebung</a>.

## Verwaltung der Nutzer:innen-Identität {#user-identity-management}

Diese Integration ermöglicht es Ihnen, Ihre Facebook-Leads per E-Mail über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number) zu attributieren.

* Wenn die E-Mail mit einem bestehenden Nutzerprofil übereinstimmt, aktualisiert Braze das Profil mit den Facebook-Lead-Daten.
* Wenn es mehrere Nutzerprofile mit derselben E-Mail gibt, gibt Braze dem zuletzt aktualisierten Profil mit einer externen ID bei Updates den Vorrang.
* Wenn die externe ID nicht existiert, gibt Braze dem zuletzt aktualisierten Profil mit der passenden E-Mail den Vorrang.
* Wenn für die angegebene E-Mail kein Profil existiert, erstellt Braze ein neues Profil und ein neues Alias-Nutzerprofil wird angelegt. Um die neu erstellten Alias-Nutzerprofile zu identifizieren, verwenden Sie den [`/users/identify`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

{% alert note %}
Sie können auch eine Telefonnummer oder eine externe ID als Teil der Anfrage an Braze verwenden, wenn diese Felder verfügbar sind und der primäre Bezeichner sind, den Sie für die Integration nutzen möchten. Ändern Sie dazu die Nutzlast Ihrer Anfrage wie im [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) angegeben.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

{% details Ich habe den Trigger und die Aktion erfolgreich getestet – warum kann ich meinen Zapier-Zap nicht veröffentlichen? %}
Um diese Integration nutzen zu können, müssen Sie über einen <a href="https://zapier.com/app/pricing/" target="_blank">Zapier-Tarif</a> verfügen, der Premium-Apps unterstützt.
{% enddetails %}

{% details Warum werden Facebook-Leads nicht mit Braze synchronisiert? %}
1. Stellen Sie sicher, dass Sie Administrator-Zugriff auf Ihre Facebook-Seite, Ihr Anzeigenkonto und Ihren Lead-Zugang haben. Verbinden Sie dann Ihr Konto in Zapier erneut.
2. Überprüfen Sie, ob das von Ihnen in Facebook erstellte Sofortformular mit dem in Ihrem Trigger-Schritt ausgewählten Formular übereinstimmt.
3. Stellen Sie sicher, dass Sie Zapier den Leads-Zugang zugewiesen haben, indem Sie zu **Facebook Business Manager** > **Integrations** > **Leads Access** gehen.
{% enddetails %}

{% details Warum sehe ich doppelte Nutzerprofile mit derselben E-Mail? %}
Es gibt verschiedene Möglichkeiten, Nutzerprofile in Braze auf der Grundlage ihres [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle) zu erstellen und zu verwalten.

Abhängig von Ihren internen Prozessen und dem Zeitpunkt, zu dem Sie die Erstellung von Kund:innen in Braze triggern, kann es aufgrund einer Race-Condition zu doppelten Nutzerprofilen kommen – nämlich wenn das Nutzerprofil durch die Integration erstellt wird und gleichzeitig die Nutzer:in von Ihrem System angelegt wird. Sie können [Nutzerprofile zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) in Braze.
{% enddetails %}

{% details Ich habe kein Zapier-Konto. Wie kann ich Facebook-Lead-Ads-Webhooks an Braze senden? %}
Wenn Sie Zapier nicht verwenden und auch nicht vorhaben, Zapier zu verwenden, können Sie die Integration direkt von Facebook in Braze erstellen. Weitere Informationen finden Sie in der <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">Lead-Ads-Dokumentation</a>.

Um Leads von Facebook abzurufen, verwenden Sie <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">Webhooks</a>. Lesen Sie die <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">Webhooks-Dokumentation</a>, um mit Webhooks in Facebook zu beginnen.

Nachdem Sie die Webhook-URL in Facebook eingerichtet haben, arbeiten Sie mit Ihrem Team zusammen, um den besten Weg zur Weiterleitung der Daten an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) zu finden. Ähnlich wie beim Zapier-Ansatz empfehlen wir, eine [Anfrage per E-Mail]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number) über den `users/track`-Endpunkt zu stellen.
{% enddetails %}

{% alert tip %}
Weitere Tipps zur Fehlerbehebung finden Sie in der <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Anleitung zur Fehlerbehebung für Facebook-Leads</a> von Zapier.
{% endalert %}