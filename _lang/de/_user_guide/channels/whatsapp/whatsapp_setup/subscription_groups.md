---
nav_title: "Abo-Gruppen"
article_title: "Abo-Gruppen"
page_order: 4
description: "Dieser Artikel beschreibt WhatsApp-Abo-Gruppen, welche Abo-Status verfügbar sind und wie Abo-Gruppen eingerichtet werden."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp

---

# WhatsApp-Abo-Gruppen {#whatsapp-subscription-groups}

> WhatsApp-Abo-Gruppen werden bei der Integration von WhatsApp in Ihre App über das **Technology Partner Portal** erstellt.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## WhatsApp-Abo-Status {#whatsapp-subscription-states}

Es gibt zwei Abo-Status für WhatsApp-Nutzer:innen: `subscribed` und `unsubscribed`.

| Status | Definition |
| --- | --- |
| Abonniert | Nutzer:in hat ausdrücklich bestätigt, dass sie WhatsApp-Nachrichten von einem bestimmten Unternehmen erhalten möchte. Nutzer:innen können abonniert werden, indem ihr Abo-Status über die Braze-Abo-API aktualisiert wird oder indem eine Opt-in-Strategie gemäß den WhatsApp-Richtlinien implementiert wird. |
| Abgemeldet | Nutzer:in hat entweder nicht ausdrücklich dem Opt-in zugestimmt oder der Opt-in-Status wurde ausdrücklich entfernt. <br><br> Nutzer:innen, die sich von einer WhatsApp-Abo-Gruppe abgemeldet haben, erhalten keine WhatsApp-Nachrichten mehr von Telefonnummern, die zu dieser Abo-Gruppe gehören. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp-Abo-Status" }

### WhatsApp-Abo-Gruppen von Nutzer:innen festlegen {#setting-users-whatsapp-subscription-groups}

- **REST API:** Nutzerprofile können programmatisch über den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) mithilfe der Braze REST API festgelegt werden.
- **Web SDK:** Nutzer:innen können einer E-Mail-, SMS- oder WhatsApp-Abo-Gruppe mit der Methode `addToSubscriptionGroup` für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) oder [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) hinzugefügt werden.
- **Nutzerimport:** Nutzer:innen können über **Nutzer:innen importieren** zu E-Mail- oder SMS-Abo-Gruppen hinzugefügt werden. Beim Aktualisieren des Abo-Gruppenstatus müssen diese zwei Spalten in Ihrer CSV-Datei vorhanden sein: `subscription_group_id` und `subscription_state`. Weitere Informationen finden Sie unter [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

### WhatsApp-Abo-Gruppe von Nutzer:innen überprüfen {#checking-a-users-whatsapp-subscription-group}

- **Nutzerprofil:** Auf einzelne Nutzerprofile kann über das Braze-Dashboard unter **Zielgruppe** > **Nutzer:innen suchen** zugegriffen werden. Hier können Sie Nutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Nutzer-ID suchen. Innerhalb eines Nutzerprofils können Sie unter dem Tab **Engagement** die WhatsApp-Abo-Gruppe und den Status der Nutzer:innen einsehen.

- **REST API:** Die Abo-Gruppe einzelner Nutzerprofile kann über den [Endpunkt „Abo-Gruppen von Nutzer:innen auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) oder den [Endpunkt „Abo-Gruppenstatus von Nutzer:innen auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) mithilfe der Braze REST API eingesehen werden.

## Abo-Gruppen archivieren {#archive-subscription-groups}

Wenn Sie eine WhatsApp-Abo-Gruppe nicht mehr verwenden müssen, können Sie sie archivieren, um sie als inaktiv zu markieren.

Das Archivieren einer Abo-Gruppe markiert sie als inaktiv, löscht sie jedoch nicht aus Ihrem Workspace. Wenn Sie eine WhatsApp-Telefonnummer oder Abo-Gruppe vollständig entfernen möchten, müssen Sie die Abo-Gruppe zunächst in der Abo-Gruppen-Verwaltung archivieren, bevor Sie die Löschung beim Braze-Support beantragen.

So archivieren Sie eine Abo-Gruppe:

1. Navigieren Sie zu **Zielgruppe** > **Abo-Gruppen-Verwaltung**.
2. Suchen Sie die WhatsApp-Abo-Gruppe, die Sie archivieren möchten.
3. Bewegen Sie den Mauszeiger über den Status der Abo-Gruppe und wählen Sie <i class="fa-solid fa-box-archive"></i> **Archivieren**.

## WhatsApp-Opt-in- und Opt-out-Prozess {#whatsapp-opt-in-and-opt-out-process}

Derzeit können sich Nutzer:innen auf verschiedene Weise für WhatsApp-Nachrichten anmelden und [Opt-in und Opt-out]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) durchführen, darunter per [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), über eine Website, einen WhatsApp-Thread, telefonisch oder persönlich. Beachten Sie, dass Opt-ins erforderlich sind.

Opt-in-Schlüsselwörter werden derzeit für den WhatsApp-Kanal nicht unterstützt, sodass Sie selbst eine Nutzerliste pflegen müssen. WhatsApp verfolgt einen retrospektiven Ansatz bei Opt-ins und Rate-Limits: Wenn Nutzer:innen Sie melden oder blockieren, wird Ihr Rate-Limit gesenkt.

## Abo-Status von Nutzer:innen für einen WhatsApp-Canvas aktualisieren {#update-subscription-status}

Unabhängig davon, welche Opt-in- und Opt-out-Methoden Sie verwenden, können Sie den Abo-Status von Nutzerprofilen mit einer der folgenden Aktualisierungsmethoden ändern:

- Erstellen Sie einen [Braze-zu-Braze-Webhook]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#considerations), der den Abo-Status über die REST API aktualisiert, wie im folgenden Beispiel:

![Webhook-Composer mit einer Nachricht, die die POST-Methode verwendet.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Um Race-Conditions zu vermeiden, sollte jedes Folge-Messaging nach dem Webhook in einem zweiten Canvas enthalten sein, der durch Ergebnisse des ersten Canvas getriggert wird (z. B. wenn Nutzer:innen eine Canvas-Variante betreten haben und sich in einer WhatsApp-Abo-Gruppe befinden).

- Verwenden Sie den erweiterten JSON-Editor, um das Nutzerprofil mit dem folgenden Template zu aktualisieren:

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![Nutzeraktualisierungsschritt mit einem erweiterten JSON-Editor-Schritt.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
Aktualisierungen des Abo-Status von Nutzer:innen können bis zu 60 Sekunden dauern.
{% endalert %}