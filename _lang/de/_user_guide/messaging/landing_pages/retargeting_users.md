---
nav_title: Nutzer:innen retargeten
article_title: Nutzer:innen retargeten
description: "Erfahren Sie, wie Sie Nutzer:innen retargeten, die ein Formular über eine Landing-Page eingereicht haben."
page_order: 3
---

# Nutzer:innen über eine Landing-Page retargeten {#retarget-users-through-a-landing-page}

> Erfahren Sie, wie Sie Nutzer:innen retargeten, die ein Formular über eine Landing-Page eingereicht haben, indem Sie ein dediziertes Segment erstellen oder eine Nachricht triggern, wenn das Formular eingereicht wird.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, erstellen Sie eine [Landing-Page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Retargeting von Nutzer:innen {#retargeting-users}

Braze erfasst automatisch, wenn Nutzer:innen ein Landing-Page-Formular absenden. Sie können die Gesamtzahl der Einreichungen für ein Formular unter [Landing-Page-Analytics]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics) einsehen. Für nutzerspezifisches Retargeting können Sie Nutzer:innen über Ihr Landing-Page-Formular mit einer der folgenden Methoden erneut ansprechen:

{% tabs local %}
{% tab Segment verwenden %}

Erstellen Sie ein neues Segment, um automatisch Nutzer:innen zu identifizieren, die ein Landing-Page-Formular eingereicht haben oder nicht. Wenn Sie [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), wählen Sie unter der Gruppe „Retargeting“ die Option **Submitted Form on Landing Page** aus.

![Segment-Erstellung mit der Filtergruppe „Submitted Form on Landing Page“.]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

Von hier aus können Sie Nutzer:innen danach segmentieren, ob sie ein Landing-Page-Formular für Ihre Landing-Page eingereicht haben oder nicht.
{% endtab %}

{% tab Nachrichten-Trigger verwenden %}

Richten Sie einen Nachrichten-Trigger ein, um Nutzer:innen nach dem Absenden des Formulars automatisch eine Nachricht zu senden oder sie in einen Canvas aufzunehmen. Wenn Sie die Zustellungsoption für Ihre [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) oder Ihren [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) auswählen, wählen Sie **Action Based Delivery** und dann **Submitted a Landing Page form**.

Alle Nutzer:innen, die ein Formular über dieses Landing-Page-Formular absenden, erhalten entweder eine Nachricht über den gewählten Messaging-Kanal oder werden in den gewählten Canvas aufgenommen.

![Landing-Page-Trigger-Aktion im Messaging.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
Die Option für aktionsbasierte Zustellung für Landing-Pages ist für In-App-Nachrichten nicht verfügbar. Um Nutzer:innen, die ein Formular auf einer Landing-Page eingereicht haben, mit einer In-App-Nachricht anzusprechen, wählen Sie den Filter **Submitted Form on Landing Page** in den **Targeting Options** Ihrer Campaign aus.
{% endalert %}

{% endtab %}
{% endtabs %}

### Mehrstufiges Formular {#multi-step-form}

Bei einem [mehrstufigen Formular]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) basieren beide Retargeting-Methoden auf dem Ereignis **Submitted a Landing Page form**, das erst protokolliert wird, nachdem Nutzer:innen jeden Schritt abgeschlossen haben. Nutzer:innen, die einige, aber nicht alle Schritte absenden, werden in ihrem Profil gespeichert, sind jedoch in keiner der beiden Methoden enthalten, bis sie das gesamte Formular abgeschlossen haben. Weitere Informationen finden Sie unter [Daten aus teilweise ausgefüllten Formularen erfassen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms#track-data-from-partially-completed-forms).