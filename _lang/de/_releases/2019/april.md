---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für April 2019."
---

# April 2019

## Neue Currents-Events und -Felder {#new-currents-events-fields}

Zusätzlich zu einigen Korrekturen des Abschnitts wurde ein neues [Abo-Event]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) auf der Seite „Message Engagement Events“ hinzugefügt.

Sie können jetzt Daten zur Änderung des Zustands von Abo-Gruppen aus Braze nach [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) und [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/) exportieren sowie diese Daten und Install-Attribution-Events nach [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

Außerdem wurde die Eigenschaft `canvas_step_id` zu den verfügbaren [Konversions-Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events) hinzugefügt.

{% alert important %}
Um von diesen Updates zu profitieren, müssen Sie die Einstellungen Ihres Currents-Konnektors bearbeiten und die Events aktivieren, die Sie verwenden möchten. Kontaktieren Sie Ihren Account Manager, wenn Sie Fragen haben.
{% endalert %}

## Abo-Gruppen archivieren {#subscription-groups-archiving}

Sie können jetzt [Abo-Gruppen archivieren]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Archivierte Abo-Gruppen können nicht bearbeitet werden und erscheinen nicht mehr in den Segment-Filtern. Wenn Sie versuchen, eine Gruppe zu archivieren, die in einer E-Mail, einer Campaign oder einem Canvas als Segment-Filter verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen der Gruppe entfernt haben.