---
nav_title: "Playable"
article_title: "Playable"
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Playable, einer Videoplattform, die es Ihnen ermöglicht, Videoinhalte zu Ihren E-Mail-Campaigns in Braze hinzuzufügen."
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> [Playable](https://playable.video) ermöglicht es Ihnen, automatisch abspielbare Videoinhalte zu Ihren E-Mail-Campaigns in Braze hinzuzufügen.

_Diese Integration wird von Playable gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Playable ermöglicht es Ihnen, Ihre besten Inhalte (hochwertige Videos) an Ihre beste Zielgruppe (E-Mail) zu liefern und Ihre Click-through- und Postklick-Metriken mit spannenden, hochwertigen Inhalten, die automatisch im Posteingang abgespielt werden, zu steigern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Playable-Konto | Um diese Partnerschaft zu nutzen, ist ein Playable-Konto erforderlich. Wenn Sie noch kein Playable-Konto haben, [registrieren Sie sich für ein Playable-Konto](https://signup.playable.video). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }
| Videoinhalte | Laden Sie Videodateien auf Playable hoch oder stellen Sie Video-URLs von Websites wie Facebook, Instagram, YouTube, X (ehemals Twitter), TikTok und weiteren bereit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Implementierung {#implementation}

### Schritt 1: Ihr Video zu Playable hinzufügen {#step-1-add-your-video-to-playable}

Auf der Playable-Plattform können Sie Videodateien hochladen oder Videos hinzufügen, indem Sie eine URL Ihres Videos auf Facebook, Instagram, YouTube, X (ehemals Twitter), TikTok und weiteren Plattformen angeben.

### Schritt 2: Den Einbettungscode von Playable kopieren {#step-2-copy-the-embed-code-from-playable}

Nach dem Hochladen generiert Playable einen Code, der, wenn er in Ihre Braze-Campaign eingefügt wird, das Video in Ihre E-Mail einbettet und bei Öffnung automatisch abspielt. Wenn Ihre E-Mail geöffnet wird, stellen die Playable-Server die bestmögliche Version Ihres Videos bereit – abhängig von E-Mail-Client, Gerät, Bildschirmgröße und Netzwerkbedingungen.

{% alert tip %}
Videos werden in über 98 % der Posteingänge automatisch abgespielt, darunter iPhone Mail, Gmail, Apple Mail, Outlook für iOS, Outlook für Android, Outlook für Mac und neuere Versionen von Outlook 365 für Windows. Nutzer:innen älterer Outlook-Versionen für Windows sehen stattdessen ein statisches Bild.
{% endalert %}

### Schritt 3: Den Einbettungscode in Braze einfügen {#step-3-paste-the-embed-code-into-braze}

Fügen Sie den Code abschließend in Ihre Braze-E-Mail-Campaign ein und fahren Sie dann mit dem Entwerfen, Testen und Veröffentlichen Ihrer E-Mail-Campaign fort.