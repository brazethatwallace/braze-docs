---
nav_title: "Mehrere Geschäftskonten"
article_title: "Mehrere Geschäftskonten"
page_order: 5
description: "Dieser Referenzartikel behandelt die Schritte zum Hinzufügen von WhatsApp-Geschäftskonten und Telefonnummern."
page_type: reference
channel:
  - WhatsApp
---

# Mehrere WhatsApp-Geschäftskonten und Telefonnummern {#multiple-whatsapp-business-accounts-and-phone-numbers}

> Sie können mehrere WhatsApp-Geschäftskonten und Abo-Gruppen (und Telefonnummern) zu jedem Workspace hinzufügen. <br><br>Jede Abo-Gruppe ist mit einer eindeutigen Telefonnummer verbunden, sodass Sie dieselbe Telefonnummer nicht mit mehreren Abo-Gruppen verbinden oder mehrere Telefonnummern mit einer Abo-Gruppe verbinden können.

## Mehrere WhatsApp-Geschäftskonten {#multiple-whatsapp-business-accounts}

Mehrere WhatsApp-Geschäftskonten sind nützlich, wenn Sie WhatsApp-Nachrichten an Nutzer:innen in einem Braze-Workspace senden möchten, der mehrere Marken umfasst. Das liegt daran, dass jedes Geschäftskonto innerhalb von WhatsApp separat betrieben wird und über eine eigene Telefonnummer, eigene Nachrichtentemplates und eine eigene Qualitätsbewertung verfügt.

Geschäftskonten, die innerhalb desselben Meta Business Managers verschachtelt sind, teilen sich auch die Verwaltung der Nutzerzugriffsberechtigungen und Kataloge (noch nicht in Braze unterstützt).

![Diagramm des Braze- und WhatsApp-Ökosystems, das zeigt, wie Workspaces und WhatsApp-Geschäftskonten miteinander verbunden sind: Sie können eine Abo-Gruppe mit einer Telefonnummer, mehrere WhatsApp-Geschäftskonten mit einem Workspace und einen Workspace mit mehreren Meta Business Portfolios verbinden.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

### Ein WhatsApp-Geschäftskonto hinzufügen {#adding-a-whatsapp-business-account}

Sie können bis zu 10 WhatsApp-Geschäftskonten pro Workspace hinzufügen. Die Geschäftskonten können in verschiedenen Meta Business Managern verschachtelt sein. So fügen Sie ein Konto hinzu:

1. Gehen Sie zu **Technologie-Partner** > **WhatsApp** und wählen Sie **Add WhatsApp Business Account** aus.

![Abschnitt „WhatsApp Messaging Integration“ mit Optionen zum Hinzufügen eines Geschäftskontos oder einer Abo-Gruppe und Nummer.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Durchlaufen Sie den Registrierungs-Workflow. Eine detaillierte Schritt-für-Schritt-Anleitung finden Sie unter [WhatsApp Embedded Signup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

{% alert important %}
Ihre Telefonnummer muss alle Anforderungen einer WhatsApp-Telefonnummer erfüllen, einschließlich der Bedingung, dass sie nicht bei anderen WhatsApp-Konten registriert sein darf.
{% endalert %}

## Mehrere Abo-Gruppen und Telefonnummern {#multiple-subscription-groups-and-phone-numbers}

Nachrichtentemplates werden von allen Telefonnummern innerhalb desselben WhatsApp-Geschäftskontos gemeinsam genutzt. Weitere Informationen zu WhatsApp-Abo-Gruppen finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

Jede WhatsApp-Telefonnummer wird den Nutzer:innen als separater WhatsApp-Chat angezeigt. Jede Telefonnummer innerhalb eines WhatsApp-Geschäftskontos arbeitet unabhängig voneinander, sodass sie für Folgendes dieselben oder unterschiedliche Werte haben können:
- Anzeigename
- Status
- Qualitätsbewertung
- Nachrichtenlimit

### Eine Abo-Gruppe und Telefonnummer hinzufügen {#adding-a-subscription-group-and-phone-number}

Sie können bis zu 20 Abo-Gruppen (und Sende-Telefonnummern) pro WhatsApp-Geschäftskonto hinzufügen. So fügen Sie eine Abo-Gruppe und Telefonnummer hinzu:

1. Gehen Sie zu **Technologie-Partner** > **WhatsApp** und wählen Sie **Add Subscription Group and Number** aus.

![Abschnitt „WhatsApp Messaging Integration“ mit Optionen zum Hinzufügen eines Geschäftskontos oder einer Abo-Gruppe und Nummer.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. Durchlaufen Sie den Registrierungs-Workflow. <br><br> Wählen Sie im Schritt **Select your WhatsApp Business Account** Ihr bestehendes WhatsApp-Geschäftskonto aus und fügen Sie eine neue Telefonnummer hinzu. Diese Nummer muss alle Anforderungen einer WhatsApp-Telefonnummer erfüllen, einschließlich der Bedingung, dass sie nicht bei anderen WhatsApp-Konten registriert sein darf.

### Eine Abo-Gruppe und Telefonnummer entfernen {#removing-a-subscription-group-and-phone-number}

1. Gehen Sie zu **Zielgruppe** > **Abos** und archivieren Sie die Abo-Gruppe.
2. Gehen Sie zu Ihrem Meta Business Manager und löschen Sie die Telefonnummer.