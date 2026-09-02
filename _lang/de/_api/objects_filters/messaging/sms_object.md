---
nav_title: "SMS-Objekt"
article_title: SMS-Messaging-Objekt
page_order: 10
page_type: reference
channel: SMS
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Braze SMS-Objekts."

---
# SMS-Objekt {#sms-object}

> Mit dem `sms`-Objekt können Sie über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) SMS-Nachrichten ändern oder erstellen.

```json
{
    "subscription_group_id": (required, string) the ID of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
    "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
    "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.
}
```

- [App-Bezeichner]({{site.baseurl}}/api/identifier_types)
  - Jede gültige `app_id` von einer in Ihrem Workspace konfigurierten App funktioniert für alle Nutzer:innen in Ihrem Workspace, unabhängig davon, ob die jeweilige Person die spezifische App in ihrem Profil hat oder nicht.