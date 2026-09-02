---
nav_title: EmailShepherd
article_title: EmailShepherd
alias: /partners/emailshepherd/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und EmailShepherd, einer agentenbasierten E-Mail-Erstellungsplattform, die auf Ihrem E-Mail-Design-System aufbaut und genehmigte E-Mails in Ihrem Braze-Workspace veröffentlicht."
page_type: partner
search_tag: Partner
---

# EmailShepherd

> [EmailShepherd](https://emailshepherd.com/) ist eine agentenbasierte E-Mail-Erstellungsplattform, die auf Ihrem E-Mail-Design-System aufbaut und es Ihrem gesamten Marketing-Team – und KI or künstliche Intelligenz-Agenten – ermöglicht, markenkonforme, produktionsreife E-Mails ohne Engpässe zu erstellen. Die Braze-Integration veröffentlicht genehmigte E-Mails direkt in Ihrem Braze-Workspace, sodass Marketer die E-Mail-Produktion in Braze skalieren können, ohne die Markenkonsistenz zu beeinträchtigen.

_Diese Integration wird von EmailShepherd gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und EmailShepherd ermöglicht es Ihnen, E-Mails auf Ihrem E-Mail-Design-System in EmailShepherd zu erstellen und als E-Mail-Templates nach Braze zu exportieren. Ihr Team erstellt und genehmigt E-Mails in EmailShepherd und veröffentlicht dann produktionsreife Templates in Braze – ohne manuellen HTML-Übergabeprozess.

## Voraussetzungen {#prerequisites}

Folgendes ist für die Nutzung dieser Integration erforderlich:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| EmailShepherd-Konto | Ein EmailShepherd-Konto ist erforderlich, um diese Integration zu nutzen. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit vollständigen „Templates“-Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre Braze-[Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) entspricht Ihrem Braze-Dashboard und Representational State Transfer-Endpunkt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

EmailShepherd ist für Teams konzipiert, die die E-Mail-Produktion skalieren und gleichzeitig jeden Versand markenkonform halten möchten. Es eignet sich besonders, wenn Sie Folgendes erreichen möchten:

- **Markenkonsistenz im großen Maßstab sicherstellen:** Ihr E-Mail-Design-System definiert die genehmigten Komponenten, Farben und Layouts. Jede in Braze veröffentlichte E-Mail ist konstruktionsbedingt markenkonform.
- **E-Mail-Produktion für Ihr gesamtes Team öffnen:** Ein Drag-and-Drop-Builder, der auf Ihrem E-Mail-Design-System basiert, ermöglicht es jedem, produktionsreife E-Mails zu erstellen.
- **Agentenbasierte Campaign-Erstellung nutzen:** KI or künstliche Intelligenz-Agenten arbeiten innerhalb der Leitplanken Ihres E-Mail-Design-Systems, sodass die von ihnen erstellten Campaigns markenkonform und versandbereit sind.

## Integration

### 1. Schritt: EmailShepherd-Konnektor erstellen {#step-1-create-your-emailshepherd-connector}

{% alert note %}
Dies ist eine einmalige Einrichtung. Nachdem Sie den Konnektor erstellt haben, verwendet EmailShepherd diese Zugangsdaten für alle zukünftigen Exporte nach Braze.
{% endalert %}

1. Gehen Sie in EmailShepherd zu **Connectors** > **Add connector**.
2. Wählen Sie **Braze** aus und geben Sie einen Konnektor-Namen ein.
3. Geben Sie Ihren API-Schlüssel ein und wählen Sie Ihre Braze-Instanz aus.
4. Wählen Sie **Create Connector**, um die Verbindung zu speichern.

![EmailShepherd-Konnektor-Formular mit Feldern für Braze-Instanz und API-Schlüssel]({% image_buster /assets/img_archive/emailshepherd_step1.png %}){: style="max-width:60%;"}

### 2. Schritt: E-Mail aus EmailShepherd exportieren {#step-2-export-an-email-from-emailshepherd}

Suchen Sie in EmailShepherd eine E-Mail, die Sie nach Braze exportieren möchten. Stellen Sie sicher, dass sie veröffentlicht ist, und wählen Sie dann **Export**.

![EmailShepherd-E-Mail-Editor mit der Export-Aktion]({% image_buster /assets/img_archive/emailshepherd_step2.png %}){: style="max-width:60%;"}

### 3. Schritt: Konfigurieren und in Braze veröffentlichen {#step-3-configure-and-publish-to-braze}

1. Wählen Sie auf der Export-Seite Ihren Braze-Konnektor unter **Connectors** aus (zum Beispiel **Braze Prod**).
2. Wählen Sie eine **Image hosting**-Option für Bilder aus Ihrer EmailShepherd-Bildbibliothek. Bilder, die per URL eingegeben wurden, werden beim Export nicht verändert.
3. Bestätigen Sie die **Locale** und geben Sie einen **Template name** für die E-Mail in Braze ein.
4. Wählen Sie **Start export**.

![EmailShepherd-Export-Seite mit Feldern für Braze-Konnektor, Image-Hosting und Template-Name]({% image_buster /assets/img_archive/emailshepherd_step3.png %}){: style="max-width:60%;"}

## Die Integration verwenden {#use-the-integration}

Finden Sie Ihre exportierten E-Mails in Braze unter **Content** > **Email**. Sie können diese Templates in Braze-Campaigns und Canvase verwenden.

## Support

Weitere Informationen zu EmailShepherd-Integrationen finden Sie in der [EmailShepherd-Dokumentation](https://emailshepherd.com/docs/).