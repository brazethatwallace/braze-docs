---
nav_title: Mention Me
article_title: Integration von Mention Me mit Braze
description: Anleitung zur Einrichtung der Mention Me Integration
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> Gemeinsam können [Mention Me](https://www.mention-me.com/) und Braze Ihr Tor zur Gewinnung von Premium-Kund:innen und zur Förderung einer unerschütterlichen Markentreue sein. Durch die nahtlose Integration von First-Party-Empfehlungsdaten in Braze können Sie hoch personalisierte Omnichannel-Erlebnisse liefern, die auf Ihre Markenfans zugeschnitten sind.

_Diese Integration wird von Mention Me gepflegt._

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Mention Me-Konto   | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Mention Me-Konto](https://mention-me.com/login).                                                                     |
| Ein Braze REST-API-Schlüssel  | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track` und `templates.email.create`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

* Senden Sie Kontaktdaten und Opt-ins von über Mention Me empfohlenen Kund:innen in Echtzeit an Braze
* Verwenden Sie Empfehlungsdaten, um E-Mail-Erinnerungen für Gutscheine zu erstellen
* Verbessern Sie die Performance anderer Marketingkanäle, indem Sie Empfehlungsdaten nutzen, um hochwertige Kund:innen zu segmentieren und gezielt anzusprechen

## Welche Daten werden von Mention Me an Braze gesendet? {#what-data-is-sent-from-mention-me-to-braze}

Wenn Sie diese Integration einrichten, erstellt Mention Me automatisch Ihre angepassten Attribute und Events – Sie müssen dies also nicht im Voraus tun.

Die E-Mail-Adressen Ihrer Kund:innen in Braze werden verwendet, um relevante Events und angepasste Attribute zu verknüpfen. Mention Me sendet Events und Kontaktprofilattribute für alle Interessent:innen oder bestehenden Kund:innen, die dieses Event über Mention Me triggern, unabhängig von ihrem Opt-in-Status.

Weitere Einzelheiten finden Sie unter [Kontaktprofilattribute und Events](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Integration von Mention Me {#integrating-mention-me}

{% alert tip %}
Eine vollständige Schritt-für-Schritt-Anleitung finden Sie in der [Dokumentation zur Einrichtung von Braze mit Mention Me](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

So integrieren Sie Mention Me mit Braze:

1. Gehen Sie in Mention Me auf die [Braze-Integrationsseite](https://mention-me.com/merchant/~/integrations/braze) und wählen Sie dann **Connect**.
2. Wählen Sie **Create New Authorization**, fügen Sie dann den [zuvor erstellten API-Schlüssel](#prerequisites) hinzu und wählen Sie Ihre Braze-Instanz aus.
3. Wählen Sie ein oder mehrere Länder aus, die Sie synchronisieren möchten.
4. Wenn Sie fertig sind, wählen Sie **Connect**.