---
nav_title: Nutzer:innen retargeten
article_title: Nutzer:innen retargeten
description: "Erfahren Sie, wie Sie Nutzer:innen retargeten, die ein Formular über eine Landing-Page eingereicht haben."
page_order: 3
---

# Nutzer:innen über eine Landing-Page retargeten {#retarget-users-through-a-landing-page}

> Erfahren Sie, wie Sie Nutzer:innen retargeten, die ein Formular über eine Landing-Page eingereicht haben, indem Sie ein dediziertes Segment erstellen oder eine Nachricht triggern, wenn das Formular eingereicht wird.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, müssen Sie eine [Landing-Page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/) erstellen.

## Nutzer:innen retargeten {#retargeting-users}

Braze erfasst automatisch, wenn Nutzer:innen ein Landing-Page-Formular einreichen. Sie können die Gesamtzahl der Einreichungen für ein Formular unter [Landing-Page-Analytics]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#viewing-analytics) einsehen. Für nutzerspezifisches Retargeting müssen Sie Nutzer:innen jedoch über Ihr Landing-Page-Formular mit einer der folgenden Methoden retargeten:

- **Über ein Segment:** Sie können ein neues Segment erstellen, um automatisch Nutzer:innen zu identifizieren, die ein Landing-Page-Formular eingereicht haben oder nicht.
- **Über einen Nachrichtentrigger:** Sie können einen Nachrichtentrigger einrichten, um Nutzer:innen nach dem Einreichen des Formulars automatisch eine Nachricht zu senden oder sie in einen Canvas aufzunehmen.

{% tabs local %}
{% tab Über ein Segment %}
Wenn Sie [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), wählen Sie unter der Gruppe „Retargeting“ die Option **Submitted form on Landing Page**.

![Segment-Erstellung mit der ausgewählten Filtergruppe „Submitted Form on Landing Page“.]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

Von hier aus können Sie Nutzer:innen danach segmentieren, ob sie ein Landing-Page-Formular für Ihre Landing-Page eingereicht haben oder nicht.
{% endtab %}

{% tab Über einen Nachrichtentrigger %}
Wenn Sie die Zustellungsoption für Ihre [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/) oder Ihren [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) auswählen, wählen Sie **Action Based Delivery** und dann **Submitted Landing Page form**.

Alle Nutzer:innen, die ein Formular über dieses Landing-Page-Formular einreichen, erhalten entweder eine Nachricht über den gewählten Messaging-Kanal oder werden in den gewählten Canvas aufgenommen.

![Landing-Page-Triggeraktion im Messaging.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
Die Option für aktionsbasierte Zustellung für Landing-Pages ist für In-App-Nachrichten nicht verfügbar. Um Nutzer:innen, die ein Formular auf einer Landing-Page eingereicht haben, mit einer In-App-Nachricht anzusprechen, wählen Sie den Filter **Submitted Form on Landing Page** in den **Targeting-Optionen** Ihrer Campaign.
{% endalert %}

{% endtab %}
{% endtabs %}