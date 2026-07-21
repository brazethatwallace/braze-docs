---
page_order: 0
nav_title: Home
article_title: Technologie-Partner
alias: /partners/partners/
layout: dev_guide
search_tag: Partner
description: "Entdecken Sie Braze-Technologie-Partner (Alloys) nach Kategorie. Finden Sie Integrationsdokumentation für Personalisierung, Orchestrierung, Daten, E-Commerce, Audience Sync und mehr."

guide_top_header: "Technologie-Partner"
guide_top_text: "Willkommen bei der Dokumentation der Braze-Technologie-Partner (Alloys). Durchsuchen Sie die Partnerkategorien nach technischen Integrationsleitfäden.<br><br>Eine vollständige, durchsuchbare und filterbare Liste aller Braze-Technologie-Partner finden Sie im <a href='https://marketplace.braze.com/t/type/technology-partner'>Braze Marketplace</a>. Möchten Sie unserer Community von Kund:innen beitreten, die Braze nutzen, um ihr Kundenerlebnis zu modernisieren? Besuchen Sie unser <a href='https://brazefirebrands.splashthat.com/'>Customer Champions Program</a>."

guide_featured_title: "Partnerkategorien"
guide_featured_list:
  - name: Nachrichtenpersonalisierung
    link: /docs/partners/message_personalization
    image: /assets/img/braze_icons/magic-wand-02.svg
  - name: Nachrichtenorchestrierung
    link: /docs/partners/message_orchestration
    image: /assets/img/braze_icons/send-01.svg
  - name: Daten und Analytics
    link: /docs/partners/data_and_analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Canvas Audience Sync
    link: /docs/partners/canvas_audience_sync
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: E-Commerce
    link: /docs/partners/ecommerce
    image: /assets/img/braze_icons/shopping-cart-03.svg
  - name: Zusätzliche Kanäle und Erweiterungen
    link: /docs/partners/additional_channels_and_extensions
    image: /assets/img/braze_icons/puzzle-piece-01.svg
  - name: KI-Modellanbieter
    link: /docs/partners/ai_model_providers
    image: /assets/img/braze_icons/stars-01.svg
---

## Fehlerbehebung bei Partnerverbindungen {#troubleshooting-partner-connections}

Wenn die Integration eine Einrichtung auf der Braze-Seite erfordert, melden Sie sich in Ihrem Braze-Dashboard an und navigieren Sie zu **Partnerintegrationen** > **Technologie-Partner**.

{% alert note %}
Vollständig vom Partner verwaltete Integrationen sind hier möglicherweise nicht aufgeführt. Lesen Sie die partnerspezifische Dokumentation, um die Zuständigkeit für die Integration und die Konfigurationsschritte zu überprüfen.
{% endalert %}

Wenn bei einem Partner in Braze **Ungültige Zugangsdaten** angezeigt wird, die Integration im Dashboard des Partners aber korrekt aussieht, trennen Sie die Integration auf der Technologie-Partnerseite und verbinden Sie sie erneut. Überprüfen Sie API-Schlüssel, OAuth-Token und Berechtigungen auf der Partnerseite.

Einige externe Dashboards (z. B. Tools zur Zustellbarkeits- oder Posteingangsüberwachung) können einen anderen Verbindungs- oder Verifizierungsstatus anzeigen als die Braze-Technologie-Partnerseite. Verwenden Sie die Partner-Kachel in Braze für den Verbindungsstatus, auf den sich Braze für Synchronisierung und Versand stützt.