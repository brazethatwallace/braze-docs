---
nav_title: "Nutzer:innen-Opt-ins erfassen"
article_title: Best Practices für die Erfassung von SMS-Opt-ins der Nutzer:innen
page_order: 3
description: "Dieser Referenzartikel behandelt drei Best Practices für die Erfassung von Nutzer:innen-Opt-ins."
page_type: reference
channel:
  - SMS

---

# Nutzer:innen-Opt-ins erfassen {#collect-user-opt-ins}

> Der folgende Artikel listet einige gängige SMS-Opt-in-Methoden auf.

## Option 1: Nutzer:innen bitten, eine SMS an Ihren Kurz- oder Langcode zu senden {#option-1-ask-users-to-text-your-short-or-long-code}

Bitten Sie Nutzer:innen, „START“, „UNSTOP“, „YES“ oder ein angepasstes Opt-in-Schlüsselwort an Ihre Nummer zu senden, um sie automatisch zu Ihrer Abo-Gruppe hinzuzufügen. Auf Ihrer Website, in Ihrer mobilen App oder sogar in der Werbung können Sie Nutzer:innen dazu auffordern, um sich anzumelden, und Sie können einen Anreiz anbieten, wenn dies hilfreich ist.

## Option 2: Nutzer:innen melden sich per In-App-Nachricht an {#option-2-users-opt-in-via-in-app-message}

Um Nutzer:innen die Möglichkeit zu geben, sich über eine In-App-Nachricht für SMS anzumelden, verwenden Sie das von Braze bereitgestellte [Formular zur Erfassung von Telefonnummern]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture), um ein markengerechtes Formular zu erstellen, mit dem Sie Telefonnummern sammeln und Ihre SMS-Liste erweitern können.

![In-App-Nachrichten-Editor mit einem Template zur Erfassung von Telefonnummern.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze empfiehlt, zusätzlich das Feature [SMS-Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) zu nutzen. Dieses Feature funktioniert automatisch mit dem Formular zur Erfassung von Telefonnummern in In-App-Nachrichten und fordert Nutzer:innen auf, ihre Absicht zu bestätigen, nachdem sie ihre Telefonnummer über das Formular übermittelt haben.

## Option 3: Registrierungsablauf {#option-3-sign-up-flow}

Wenn sich neue Nutzer:innen auf der Website oder in der App registrieren, fragen Sie nach deren Telefonnummer und E-Mail-Adresse. Fügen Sie ein Kontrollkästchen hinzu, um Werbe-E-Mails und SMS zu erhalten.

Nachdem sich die Nutzer:innen registriert haben, gehen Sie wie folgt vor:

1. Verwenden Sie den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status), um die Nutzer:innen zu erstellen und deren Attribute zu speichern.

{% raw %}
```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```
{% endraw %}

{: start="2"}
2. Verwenden Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um die Nutzer:innen für SMS zu abonnieren.

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```
{% endraw %}

{% alert note %}
Um Nutzer:innen beim Abonnieren über die REST API in den [SMS-Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)-Workflow aufzunehmen, setzen Sie `use_double_opt_in_logic` in Ihrer Anfrage auf `true`. Dieser Parameter wird von [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status), [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2) und [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) unterstützt.
<br><br>
Abo-Aktualisierungen über die REST API lösen nicht automatisch Willkommensnachrichten aus. Um eine Willkommensnachricht zu senden, erstellen Sie eine aktionsbasierte Campaign mit dem Trigger [Abo-Gruppenstatus aktualisieren]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#update-subscription-group-status) und setzen Sie die Aktualisierungsquelle auf **REST API**.
{% endalert %}