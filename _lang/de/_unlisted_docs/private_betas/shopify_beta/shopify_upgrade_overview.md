---
nav_title: Shopify-Upgrade – Übersicht
article_title: Shopify-Upgrade – Übersicht
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre Shopify-Integration auf die neueste Version upgraden."
page_type: partner
search_tag: Partner
permalink: "/shopify_upgrade_overview/"
hidden: true
---

# Shopify-Upgrade – Übersicht {#shopify-upgrade-overview}

> Im Rahmen unseres Engagements, Ihnen die bestmögliche Erfahrung zu bieten, verlangen wir, dass alle Shopify-Integrationen bis zum 28. August 2025 auf die [neueste Version upgraden]({{site.baseurl}}/shopify/). Dieses Upgrade ist unerlässlich, da wesentliche Änderungen in der Shopify-Technologie die Funktionsweise unserer Integration beeinflussen werden.

## Wichtige Termine {#key-dates}

- **Ende Februar bis April:** Sie erhalten Benachrichtigungen darüber, wann Ihre spezifische Gruppe (Kohorte) für das Upgrade bereit ist. Achten Sie auf diese wichtigen Informationen.
- **Upgrade-Frist:** Alle Kund:innen müssen das Upgrade bis zum **28. August 2025** abschließen.

{% multi_lang_include shopify_alerts.md alert='breaking' %}

## Was ändert sich an der Shopify-Integration? {#whats-changing-in-the-shopify-integration}

Im Rahmen von Shopifys Plänen zur Verbesserung der Checkout-Erweiterbarkeit stehen wesentliche Änderungen an der Integration mit Braze bevor. Hier ist, was Sie wissen müssen:

- **Einstellung von Script Tags und `checkout.liquid`:** Shopify stellt Script Tags und `checkout.liquid` schrittweise ein. Nach August 2025 wird das Braze Web SDK nicht mehr über Script Tags auf Checkout-Seiten geladen, es sei denn, Sie migrieren auf die neueste Version der Integration.
- **Allgemeine Verbesserungen der Integration:**
    - **Einführung empfohlener Events:** Wir fügen der Integration empfohlene E-Commerce-Events hinzu, die gängige E-Commerce-Anwendungsfälle durch vorgefertigte Templates in Braze vereinfachen.
    - **Optimiertes Identitätsmanagement:** Wir verbessern unseren Ansatz zur Verwaltung von Nutzeridentitäten, was das Tracking und die Attribution anonymer Nutzerdaten verbessern wird. Weitere Informationen zur Verarbeitung des Identitätsmanagements finden Sie unter [Nutzer- und Datensynchronisierung]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
    - **E-Mail- und SMS-Abonnent:innenlisten:** Wenn Sie derzeit E-Mail- und SMS-Abonnent:innen erfassen, werden im Rahmen des Upgrades automatisch Standard-Abo-Gruppen für jeden Kanal erstellt. Wenn Braze E-Mail- und SMS-Opt-ins synchronisiert, wird Braze den globalen Abo-Status im Nutzerprofil nicht mehr überschreiben, sondern nur noch das Opt-in der Abo-Gruppe aktualisieren.
    - Alle Details zu den Änderungen von der aktuellen zur neuen Version finden Sie im [Changelog](#full-changelog).

{% alert important %}
Dieses Upgrade ist unerlässlich, um die Funktionalität Ihrer Integration zwischen Shopify und Braze aufrechtzuerhalten. Wir empfehlen, eng mit Ihrem Entwicklerteam zusammenzuarbeiten, um den Umfang und die Auswirkungen dieser Änderungen zu bewerten und einen reibungslosen Übergang zu ermöglichen.
{% endalert %}

## Upgrade-Voraussetzungen {#upgrade-requirements}

Bevor Sie den Upgrade-Prozess auf der Shopify-Integrationsseite starten, erfüllen Sie die folgenden Voraussetzungen mit Ihrem Entwicklerteam:

- **SDK-Anpassungen prüfen:** Wenn Sie Ihre Braze- und Shopify-Integration angepasst haben (z. B. durch das Protokollieren angepasster Events oder Attribute), stellen Sie sicher, dass diese Anpassungen nach dem Upgrade korrekt funktionieren. Wenn Sie eigene Browser-Events für Aktionen wie „Produkt angesehen“ oder „Warenkorb aktualisiert“ erstellt haben, koordinieren Sie mit Ihren Entwickler:innen, um diese vor dem Upgrade zu entfernen, da sie die Funktionalität des neuen Konnektors duplizieren würden.

{% alert important %}
Wenn Sie einen Shopify-Onlineshop betreiben und Ihre Entwickler:innen die Braze SDKs direkt in Ihre Shopify-Website oder über Google Tag Manager oder eine Customer Data Platform (CDP) implementiert haben, müssen Sie planen, deren Nutzung einzustellen, wenn Sie auf den neuen Shopify-Konnektor upgraden.
{% endalert %}

- **Identitätsmanagement überprüfen:** Wenn Sie eine externe Braze-ID verwenden, arbeiten Sie mit Ihrem Entwicklerteam zusammen, um sicherzustellen, dass sie mit der neuen Integration kompatibel ist. Wenn Sie die externe ID innerhalb Ihres Shopify-Shop-Erlebnisses setzen, lassen Sie Ihre Entwickler:innen diese anpassen, um Konflikte mit dem [neuen Identitätsmanagement-Prozess]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing) zu vermeiden.
- **Betroffene Campaigns, Canvases und Segmente vorbereiten:** Während des geführten Upgrade-Prozesses können Sie alle Campaigns, Canvases und Segmente anzeigen und exportieren, die auf Shopify-Daten basieren. Wir empfehlen, die neuen erforderlichen Shopify-Events und -Attribute mit einem „ODER“-Operator hinzuzufügen, um ein reibungsloses Upgrade für Ihre aktiven Nachrichten zu ermöglichen.
- **Warenkorb-Abbruch- und Checkout-Abbruch-Journeys erstellen:** Die Warenkorb-Abbruch-Journey muss jetzt den Trigger „Performed Cart Updated“ als Teil der Eintrittskriterien in Ihrem Canvas verwenden. Zusätzlich müssen Sie den neuen Warenkorb-Liquid-Tag sowohl für Warenkorb-Abbruch- als auch für Checkout-Abbruch-Journeys verwenden. Sie können unsere neuen [Canvas-Templates]({{site.baseurl}}/using_shopify_with_braze/#create-your-canvas-user-journeys) nutzen, um loszulegen.

Das Abschließen dieser Schritte hilft, ein erfolgreiches Upgrade auf die neueste Version der Shopify-Integration zu ermöglichen.

## Integrationsoptionen {#integration-options}

Braze bietet zwei Integrationsoptionen für Shopify-Händler:innen, die auf die vielfältigen Anforderungen von E-Commerce-Unternehmen zugeschnitten sind: **Standard-Integration** und **Angepasste Integration**.

{% tabs local %}
{% tab Standard %}
Die Standard-Integration ist auf Shopify-Onlineshops zugeschnitten und bietet einen nahtlosen und unkomplizierten Einrichtungsprozess. Mit dieser Option können Sie Ihren Shopify-Shop schnell mit Braze verbinden und leistungsstarke Customer-Engagement-Tools nutzen, ohne umfangreiche technische Expertise zu benötigen. Mit dieser Integrationsoption können Sie Kundendaten synchronisieren, personalisiertes Messaging automatisieren und Ihre Marketingmaßnahmen durch umfassende Braze-Features verbessern.

Um Ihre bestehende Shopify-Integration über den Standard-Upgrade-Pfad zu upgraden, lesen Sie [Upgrade Ihrer Shopify-Integration (Standard)]({{site.baseurl}}/shopify_standard_upgrade/).
{% endtab %}

{% tab Angepasst %}
Die angepasste Integration bietet eine flexiblere und modularere Lösung, wenn Sie Shopify Hydrogen verwenden oder einen Headless-Shop betreiben. Diese Option ermöglicht es Ihnen, Braze SDKs direkt in Ihre Shopify-Umgebung zu implementieren, was eine tiefere Integration und maßgeschneiderte Funktionalitäten ermöglicht. Ob Sie einzigartige Kundenerlebnisse schaffen oder bestimmte Workflows optimieren möchten – die angepasste Integration bietet die notwendigen Tools, um die Möglichkeiten von Braze in einem Headless-Setup voll auszuschöpfen.

Um Ihre bestehende Shopify-Integration über den angepassten Upgrade-Pfad zu upgraden, lesen Sie [Upgrade Ihrer Shopify-Integration (angepasst)]({{site.baseurl}}/shopify_custom_upgrade/).
{% endtab %}
{% endtabs %}

## Changelog {#changelog}

{% alert important %}
Diese Integration verwendet Shopify als maßgebliche Datenquelle für unterstützte Attribute und Events. Daher kann Shopify bereits vorhandene Werte, wie Standard- oder angepasste Attribute, in einem Nutzerprofil bei der Datensynchronisierung überschreiben.
{% endalert %}

### Standard-Integration

| Vorherige Version | Neueste Version |
| --- | --- |
| {::nomarkdown}<ul><li>Script-Tag-Unterstützung</li><li>Nur Braze Web SDK</li><li>Shopify-Webhooks für Events und Produkte</li></ul>{:/} | {::nomarkdown}<ul><li>Web Pixel API-Unterstützung</li><li>Neues Braze-App-Embed</li><li>Braze Web SDK und JavaScript SDK</li><li>Shopify-Webhooks für Events und Produkte</ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-Integration" }

### Von der Integration unterstützte Nutzerbezeichner {#user-identifiers-supported-by-the-integration}

| Nutzerbezeichner | Vorherige Version | Neueste Version |
| --- | --- | --- |
| Braze-Geräte-ID |  {::nomarkdown}<ul><li>Eine zufällig generierte ID, die im Browser gespeichert wird</li></ul>{:/} | {::nomarkdown} <ul><li>Eine zufällig generierte ID, die im Browser gespeichert wird</li></ul>{:/}|
| Braze-Aliase | {::nomarkdown}<ul><li>Shopify-Kunden-ID</li><li>Shopify-E-Mail</li></ul>{:/} | {::nomarkdown}<ul><li>Shopify-Warenkorb-Token</li><li>Shopify-Checkout-Token</li></ul>{:/}|
| Externe Braze-ID | {::nomarkdown}<ul><li>Nicht zutreffend</li></ul>{:/}| {::nomarkdown}<ul><li>Shopify-Kunden-ID</li><li>E-Mail</li><li>Gehashte E-Mail (SHA-256, SHA-1, MD5)</li><li>Angepasste externe ID</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Von der Integration unterstützte Nutzerbezeichner" }

Weitere Details zur Nutzersynchronisierung und ID-Verwaltung finden Sie unter [Nutzerdaten und Synchronisierung]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).

{% alert note %}
Standardmäßig konvertiert Braze E-Mails von Shopify automatisch in Kleinbuchstaben, bevor sie als externe ID verwendet werden. Wenn Sie E-Mail oder gehashte E-Mail als externe ID verwenden, stellen Sie sicher, dass Ihre E-Mail-Adressen ebenfalls in Kleinbuchstaben konvertiert werden, bevor Sie sie als externe ID zuweisen oder bevor Sie sie aus anderen Datenquellen hashen. Dies hilft, Diskrepanzen bei externen IDs zu vermeiden und die Erstellung doppelter Nutzerprofile in Braze zu verhindern.
{% endalert %}

### Unterstützte Shopify-Events {#supported-shopify-events}

| Events oder Attribute | Vorherige Version | Neueste Version |
| --- | --- | --- |
| Events |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=product%20viewed">shopify_product_viewed</a></li></ul>{:/} | {::nomarkdown}<ul><li>Ersetzt durch <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=product%20viewed">ecommerce.product_viewed</a></li><li>Neues <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-browse">Canvas-Template für abgebrochenes Browsen</a> hinzugefügt</li></ul>{:/} |
| Events |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?tab=example%20payload">shopify_product_clicked</a></li></ul>{:/} | {::nomarkdown}<ul><li>Eingestelltes Event</li></ul>{:/} |
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20cart&tab=example%20payload">shopify_abandoned_cart</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Timer-Einstellung für Warenkorb-Abbruch</a></li></ul>{:/} | {::nomarkdown}<ul><li>Ersetzt durch <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=cart%20updated">ecommerce.cart_updated</a></li><li>Timer-Einstellung für Warenkorb-Abbruch eingestellt</li><li>Neues <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-cart">Canvas-Template für Warenkorb-Abbruch</a> hinzugefügt</li></ul>{:/} |
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20checkout&tab=example%20payload">shopify_abandoned_checkout</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Timer-Einstellung für Checkout-Abbruch</a></li></ul>{:/}| {::nomarkdown}<ul><li>Ersetzt durch <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=checkout%20started">ecommerce.checkout_started</a></li><li>Timer-Einstellung für Checkout-Abbruch eingestellt</li><li>Neues <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-checkout">Canvas-Template für Checkout-Abbruch</a> hinzugefügt</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20order&tab=example%20payload">shopify_created_order</a></li></ul>{:/} | {::nomarkdown}<ul><li>Ersetzt durch <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a></li><li>Neues <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#order-confirmation-and-feedback-survey">Canvas-Template für Bestellbestätigung und Nachkauf-Umfrage</a> hinzugefügt</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="https://braze.com/unlisted_docs/using_shopify_with_braze/?tab=order%20confirmation">Braze-Kauf-Event</a></li></ul>{:/}| {::nomarkdown}<ul><li>Eingestelltes Event. Verwenden Sie <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a>.</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=paid%20order&tab=example%20payload">shopify_paid_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=partially%20fulfilled%20order&tab=example%20payload">shopify_partially_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=fulfilled%20order&tab=example%20payload">shopify_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=cancelled%20order&tab=example%20payload">shopify_cancelled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Ersetzt durch <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20cancelled">ecommerce.order_cancelled</a></li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20refund&tab=example%20payload">shopify_created_refund</a></li></ul>{:/}| {::nomarkdown}<ul><li>Ersetzt durch <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20refunded">ecommerce.order_refunded</a></li></ul>{:/}|
| Events| {::nomarkdown}<ul><li>Kein Shopify-Konto-Login-Event</li></ul>{:/}| {::nomarkdown}<ul><li>Neues <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=account%20login#tracked-shopify-events">shopify_account_login</a> hinzugefügt</li></ul>{:/}|
| Attribute | {::nomarkdown}<ul><li>shopify_total_spent</li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Attribute | {::nomarkdown}<ul><li>shopify_order_count</li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Attribute | {::nomarkdown}<ul><li>shopify_last_order_id</li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Attribute | {::nomarkdown}<ul><li>shopify_last_order_name</li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Attribute | {::nomarkdown}<ul><li>shopify_zipcode</li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
| Attribute | {::nomarkdown}<ul><li>shopify_province</li></ul>{:/}| {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Shopify-Events" }

### Abonnent:innenerfassung {#subscriber-collection}

| Erfassungstyp | Vorherige Version | Neueste Version |
| --- | --- | --- |
| E-Mail-Abonnent:innenerfassung |  {::nomarkdown}<ul><li>Überschreibung des globalen E-Mail-Abo-Status</li><li>Möglichkeit, eine oder mehrere Abo-Gruppen zuzuweisen</li><li>Keine Standard-Abo-Gruppe für die Integration des verbundenen Shopify-Shops</li></ul>{:/} | {::nomarkdown}<ul><li>Überschreibungsfunktion eingestellt</li><li>Eine Standard-Abo-Gruppe wird im Rahmen des Upgrades erstellt</li><li>Möglichkeit, zusätzliche Abo-Gruppen zuzuweisen</li></ul>{:/} |
| SMS-Abonnent:innenerfassung |  {::nomarkdown}<ul><li>Erforderlich, eine oder mehrere Abo-Gruppen zuzuweisen</li><li>Keine Standard-Abo-Gruppe für die Integration des verbundenen Shopify-Shops</li></ul>{:/} | {::nomarkdown}<ul><li>Eine Standard-Abo-Gruppe wird im Rahmen des Upgrades erstellt</li><li>Möglichkeit, zusätzliche Abo-Gruppen zuzuweisen</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Abonnent:innenerfassung" }

{% alert note %}
Wenn Sie derzeit E-Mail- oder SMS-Abonnent:innen erfassen, wird nach Abschluss des Upgrades eine neue Standard-Abo-Gruppe erstellt. Die Standard-Abo-Gruppe trägt den Namen Ihres Shopify-Storefronts. Dieser Vorgang kann bis zu 5 Stunden dauern. <br><br>Nachdem die Abo-Gruppen verfügbar sind, stellen Sie sicher, dass Sie sie in Ihre aktiven Campaigns, Segmente oder Canvases einbinden, um Ihre abonnierten Käufer:innen effektiv zu erreichen.
{% endalert %}

### Produktsynchronisierung {#product-sync}

| Synchronisierungstyp | Vorherige Version | Neueste Version |
| --- | --- | --- |
| Initiale Produktsynchronisierung | {::nomarkdown}<ul><li>Wenn die Produktsynchronisierung aktiviert ist, initialer Import aller Produkte in Ihrem Storefront</li><li>Möglichkeit, nur aktive Produkte zu importieren</li></ul>{:/} | {::nomarkdown}<ul><li>Keine&nbsp;Änderungen</li></ul>{:/} |
| Realtime-Produktsynchronisierungen | {::nomarkdown}<ul><li>Realtime-Synchronisierungen, wenn Produkte in Ihrem Shop erstellt, aktualisiert oder gelöscht werden</li></ul>{:/} | {::nomarkdown}<ul><li>Keine&nbsp;Änderungen</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Produktsynchronisierung" }

### Kanäle {#channels}

| Kanal | Vorherige Version | Neueste Version |
| --- | --- | --- |
| In-App-Nachrichten |  {::nomarkdown}<ul><li>In Standard-Integrationen für Shopify-Onlineshops enthalten</li></ul>{:/} | {::nomarkdown}<ul><li>Keine Änderungen</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kanäle" }