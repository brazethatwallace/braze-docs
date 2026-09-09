---
nav_title: Amazon SES einrichten
article_title: Amazon SES einrichten
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Amazon SES als Ihren E-Mail-Anbieter einrichten."
channel: email
---

# Amazon SES einrichten {#amazon-ses-setup}

> Braze verwendet Amazon Simple Email Service (SES) als Standard-E-Mail-Anbieter bei der Einrichtung neuer E-Mail-Konfigurationen. Wenn Ihre gewünschte Einrichtung nicht mit den Features von Amazon SES übereinstimmt, kontaktieren Sie den Braze Support, um die Einrichtung in SparkPost oder SendGrid abzuschließen.

## Voraussetzungen {#prerequisites}

Bevor Sie mit der Einrichtung von Amazon SES beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

- Namen der Versand-Domains
- Namen der IP-Pools (z. B. Marketing, Transaktion, Staging)
- Die Anzahl der IP-Adressen für jeden IP-Pool
- Bevorzugter Anhang für Klick-Tracking-Domains (z. B. „clicks“ oder „click“, „links“ oder „link“)

## Einrichtungsbeispiel {#setup-example}

Eine typische Amazon-SES-Einrichtung sieht wie folgt aus:

- **Sub-Account-Name:** braze
- **Cluster:** eu-02

| IP-Pool | Anzahl der IPs | Konfigurationssatz | Versand-Domain | Klick-Tracking-Domain |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Einrichtungsbeispiel" }

{% alert note %}
Der Cluster- und Sub-Account-Name werden automatisch an die IP-Pools und Konfigurationssätze angehängt.
{% endalert %}

## Konfigurationsbeispiele für Klick-Tracking-Domains {#click-tracking-domain-configuration-examples}

Die folgenden Tabellen zeigen Beispiele möglicher Klick-Tracking-Domain-Konfigurationen, abhängig von Ihren Branding-Präferenzen.

### Eine Klick-Tracking-Domain pro Versand-Domain {#one-click-tracking-domain-for-each-sending-domain}

| Marketing-IP-Pool | Konfigurationsset | Versand-Subdomains | Klick-Tracking-Domains |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eine Klick-Tracking-Domain pro Versand-Domain" }

### Eine Klick-Tracking-Domain für alle Versand-Domains {#one-click-tracking-domain-for-all-sending-domains}

Dies basiert auf der Regel, dass die Klick-Tracking-Domain mit mindestens einer Versand-Domain aus dem Konfigurationsset übereinstimmen muss.

| Marketing-IP-Pool | Konfigurationsset | Versand-Subdomains | Klick-Tracking-Domains |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eine Klick-Tracking-Domain für alle Versand-Domains" }

## Überlegungen {#considerations}

- IP-Pools bei Amazon SES hosten nur die IP-Adresse selbst, während die Konfigurationssätze die Versanddomains und die Klick-Tracking-Domain hosten.
- Jedem Konfigurationssatz kann jeweils nur ein IP-Pool zugewiesen sein, aber es können mehrere Konfigurationssätze erstellt werden, die denselben IP-Pool mit unterschiedlichen Versanddomains verwenden.
- Amazon SES verwaltet rDNS- und A-Einträge intern, da sie enge Beziehungen zu Posteingangsanbietern pflegen, um IP-Adressen erkennen zu können.
- Jeder Versanddomain ist ein MAIL FROM-Bezeichner zugeordnet, der bei SPF-Validierungen hilft.
    - Der Wert für jede Versanddomain ist „e“.
    - Der MAIL FROM-Wert ändert nicht die Absenderadresse, die Ihre Kund:innen sehen.
- Die Optionen für Beginn und Ende des Trap-Nachrichtenzeitraums sind nicht verfügbar, wenn Sie Amazon SES als Ihren E-Mail-Anbieter verwenden.

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: SSL einrichten
  link: /docs/user_guide/channels/email/email_setup/ssl
{% endarticle_tiles %}