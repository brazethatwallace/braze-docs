---
nav_title: "Ads That Click to WhatsApp"
article_title: "Ads That Click to WhatsApp"
page_order: 1
description: "Dieser Referenzartikel bietet eine Schritt-für-Schritt-Anleitung zum Einrichten und Verwenden von Ads That Click to WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Ads That Click to WhatsApp {#ads-that-click-to-whatsapp}

> Diese Seite bietet eine Schritt-für-Schritt-Anleitung zum Einrichten und Verwenden von Ads That Click to WhatsApp, damit Sie und Ihr Team Ihr WhatsApp-Programm auf das nächste Level heben können.

Ads That Click to WhatsApp sind eine effiziente Möglichkeit, sowohl neue als auch bestehende Kund:innen über Meta-Anzeigen auf Facebook, Instagram oder anderen Plattformen zu erreichen. Nutzen Sie diese Anzeigen, um Ihre Produkte und Dienste zu bewerben und gleichzeitig Nutzer:innen auf Ihre WhatsApp-Präsenz aufmerksam zu machen.

![Eine Facebook-Anzeige von Calorie Rocket, die kostenlose Lieferung bewirbt, und die entsprechende WhatsApp-Konversation, die stattfindet, wenn ein:e Nutzer:in den Button der Anzeige auswählt.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Einrichten von Ads That Click to WhatsApp {#setting-up-ads-that-click-to-whatsapp}

1. Erstellen Sie im Meta Ads Manager eine Anzeige auf Facebook, Instagram oder anderen Plattformen, indem Sie der Schritt-für-Schritt-Anleitung [How to create Ads That Click to WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp) folgen. Richten Sie **keine** automatisierten Antworten ein – Sie werden die Antworten stattdessen in Braze einrichten.

![Ads Manager mit einem Editor zum Erstellen einer Engagement-Anzeige.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Wenn Sie die vorausgefüllte Nachricht einrichten, die von den Nutzer:innen an Ihr WhatsApp Business-Konto gesendet wird, fügen Sie ein bestimmtes Wort oder eine bestimmte Phrase ein, die Sie verwenden werden, um eine für die jeweilige Anzeige spezifische Antwort auszulösen. In diesem Beispiel verwendet eine Essenslieferungs-App „free delivery“, weil dies in der Anzeige beworben wird.

![Ads Manager Template-Editor mit einer vorausgefüllten Nachricht „I want free delivery“.]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Machen Sie in der Anzeigenbeschreibung deutlich, dass ein Klick auf die Anzeige eine Konversation mit Ihrer Marke startet, indem Sie Formulierungen wie „Jetzt auf WhatsApp chatten“ verwenden.
{% endalert %}

{: start="2"}
2. Richten Sie in Braze ein aktionsbasiertes Canvas ein, bei dem die aktionsbasierte Option **Eingehende WhatsApp-Nachricht senden** lautet und der Nachrichtentext „IHR_TRIGGER_WORT“ enthält. In diesem Beispiel verwendet eine Essenslieferungs-App „free delivery“.

![Entry-Zeitplan für ein aktionsbasiertes Braze-Canvas mit dem Trigger-Ereignis „Eingehende WhatsApp-Nachricht senden“ und einem Nachrichtentext, der dem Regex „free delivery“ entspricht.]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. Richten Sie im Canvas eine Antwortnachricht ein, die sofort gesendet wird, nachdem die Kund:innen das Canvas betreten (z. B. ohne Verzögerung). Obwohl das Klicken auf die Anzeige technisch gesehen ein Opt-in darstellt, empfehlen wir, Ihre Antwortnachricht so einzurichten, dass die Nutzer:innen gefragt werden, ob sie zukünftig Marketing-Nachrichten von Ihnen auf WhatsApp erhalten möchten.

{% alert tip %}
Richten Sie Ihre Antwortnachricht mit Schnellantworten ein (z. B. „Ja“ oder „Nein danke“), damit Nutzer:innen schnell angeben können, ob sie ein Opt-in wünschen.
{% endalert %}

Vergessen Sie nicht, auch Rabattcodes, Angebote oder andere in der Anzeige versprochene Informationen bereitzustellen!

![WhatsApp-Nachrichten-Editor mit Button-Antworten „Yes“ und „No Thanks“.]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![Canvas-Schritt mit einer „Opting in“-Gruppe mit dem Trigger-Ereignis „Eingehende WhatsApp-Nachricht an Abo-Gruppe gesendet“ und dem Trigger-Wort „YES“.]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. Führen Sie das Opt-in der Nutzer:innen durch, indem Sie den Abo-Status der Nutzerprofile mit einer der folgenden Aktualisierungsmethoden ändern:
    - Erstellen Sie einen Braze-zu-Braze-Webhook, der den Abo-Status über die REST API aktualisiert.
    - Verwenden Sie den erweiterten JSON-Editor, um das Nutzerprofil mit dem Template zum [Aktualisieren des Abo-Status eines Nutzers/einer Nutzerin für ein WhatsApp-Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process) zu aktualisieren.

![Canvas-Schritt „Nutzer:in aktualisieren“, der den erweiterten JSON-Editor zur Aktualisierung des Nutzerprofils verwendet.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![Canvas mit dem Workflow zum Senden von Ads That Click to WhatsApp, einschließlich drei Aktionspfaden: Opt-in, Opt-out und Alle anderen.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Überlegungen {#considerations}

Konversationen, die über eine Anzeige mit Klick zu WhatsApp beginnen, sind kostenlos, wenn die folgenden Bedingungen erfüllt sind:

- Wenn Ihnen eine Nutzer:in über einen [Free Entry Point](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations) eine Nachricht sendet, z. B. über eine Anzeige mit Klick zu WhatsApp, öffnet sich ein 24-stündiges [Kundenservice-Fenster](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows), in dem Sie dieser Nutzer:in jede Art von Nachricht senden können.
- Wenn Sie innerhalb des Kundenservice-Fensters antworten (innerhalb von 24 Stunden), öffnet sich ein Free Entry Point für 72 Stunden, und alle Nachrichten innerhalb des 72-Stunden-Fensters sind kostenlos.