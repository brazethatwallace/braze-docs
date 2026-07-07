---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Certona, einer Realtime-Omnichannel-Personalisierungslösung, die Personalisierung über den gesamten Kundenlebenszyklus hinweg bietet. Verwenden Sie Certona mit dem Braze-Connected-Content-Partner, um auf einfache Weise Inhaltsempfehlungen in Multichannel-Campaigns einzufügen."
page_type: partner
search_tag: Partner

---

# Certona

> Die Plattform von [Certona](https://www.certona.com/) fördert die Personalisierung über den gesamten Kundenlebenszyklus hinweg. Von hochgradig individualisierten E-Mail-Campaigns bis hin zu durch maschinelles Lernen gestützten Produktempfehlungen – Certona sorgt dafür, dass Sie die leistungsstarke Personalisierung voll ausschöpfen.

_Diese Integration wird von Certona gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Certona nutzt die auf maschinellem Lernen basierenden Produktempfehlungen von Certona in Braze-Campaigns und Canvases über Connected-Content.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| [Certona-Konto](https://manage.certona.com/) | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Certona-Konto. |
| [Certona-REST-API-Endpunkt](https://manage.certona.com/) | Dieser Endpunkt wird direkt in der Nachricht Ihrer Braze-Campaign verwendet, um empfohlene Inhalte auf der Grundlage der Nutzer-ID abzurufen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Nutzen Sie die REST API von Certona, um personalisierte Inhalte in Ihre Nachrichten einzufügen. Dazu fügen Sie die folgende Connected-Content-Vorlage in Ihren Braze-Nachrichten-Editor zusammen mit Ihrem Certona-REST-API-Endpunkt ein.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Als Nächstes definieren Sie den Inhalt, den Sie aufrufen möchten, z. B. relevante Texte oder Bilder. Zum Beispiel: `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Ein Bild einer Push-Campaign mit Connected-Content von Certona im Nachrichtentext.]({% image_buster /assets/img/certona.png %})

Sobald Sie diese Nachricht in den Nachrichten-Editor eingefügt haben, zeigen Sie eine Vorschau Ihres Connected-Content-Aufrufs an, um sicherzustellen, dass die richtigen Informationen angezeigt werden.

![Ein Bild, das den Tab „Test“ zeigt und Nutzer:innen dazu anregt, ihre Nachricht vor dem Versand gründlich zu testen.]({% image_buster /assets/img/certona2.png %})