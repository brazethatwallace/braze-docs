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

Die Integration von Braze und Playable ermöglicht es Ihnen, Ihre besten Inhalte (hochwertige Videos) an Ihre beste Zielgruppe (E-Mail) zu liefern und so Ihre Klick, der or klicken-through- und Post-Klick, der or klicken-Metriken mit hochwertigen Videoinhalten zu steigern, die automatisch im Posteingang abgespielt werden.

{% alert important %}
Eingebettete Videos werden von vielen E-Mail-Clients nicht nativ unterstützt und können die E-Mail-Größe erheblich erhöhen, was dazu führen kann, dass Nachrichten als Spam markiert werden. Playable löst dieses Problem, indem optimierte Videoinhalte bereitgestellt werden, die über verschiedene E-Mail-Clients hinweg funktionieren. Weitere Informationen zu Videos in E-Mails finden Sie unter [Kann ich Videos in E-Mails einbetten?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-embed-videos-in-emails)
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Playable-Konto | Ein Playable-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. Wenn Sie noch kein Playable-Konto haben, [Registrierung or registrieren Sie sich für ein Playable-Konto](https://signup.playable.video). |
| Video-Inhalte | Laden Sie Videodateien bei Playable hoch oder geben Sie Video-URLs von Websites wie Facebook, Instagram, YouTube, X (ehemals Twitter), TikTok und weiteren an. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Implementierung {#implementation}

### Schritt 1: Video zu Playable hinzufügen {#step-1-add-your-video-to-playable}

Laden Sie in der Playable-Plattform Videodateien hoch oder fügen Sie Videos hinzu, indem Sie eine URL Ihres Videos auf Facebook, Instagram, YouTube, X (ehemals Twitter), TikTok und weiteren Plattformen angeben.

### Schritt 2: Einbettungscode von Playable kopieren {#step-2-copy-the-embed-code-from-playable}

Nachdem Sie ein Video hochgeladen haben, generiert Playable einen Code, der – wenn er in Ihre Braze-Campaign eingefügt wird – das Video in Ihre E-Mail einbettet, sodass es beim Öffnen automatisch abgespielt wird. Wenn Ihre E-Mail geöffnet wird, liefern die Playable-Server die bestmögliche Version Ihres Videos – abhängig vom E-Mail-Client, Gerät, der Bildschirmgröße und den Netzwerkbedingungen.

{% alert tip %}
Videos werden in über 98 % der Posteingänge automatisch abgespielt, darunter iPhone Mail, Gmail, Apple Mail, Outlook für iOS, Outlook für Android, Outlook für Mac und neuere Versionen von Outlook 365 für Windows. Nutzer:innen von älteren Outlook-Versionen für Windows sehen stattdessen ein statisches Bild.
{% endalert %}

### Schritt 3: Einbettungscode in Braze einfügen {#step-3-paste-the-embed-code-into-braze}

Fügen Sie den Code in Ihre Braze-E-Mail-Campaign ein und fahren Sie dann mit dem Design, dem Testen und dem Veröffentlichen Ihrer E-Mail-Campaign fort.