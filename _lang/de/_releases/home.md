---
nav_title: Home
article_title: Was ist neu in Braze
description: "Die Braze-Versionshinweise werden monatlich veröffentlicht, damit Sie immer auf dem neuesten Stand sind, was wichtige Produktveröffentlichungen, laufende Produktverbesserungen, Braze-Partnerschaften, grundlegende SDK-Änderungen und veraltete Features betrifft."
page_order: 0
search_rank: 1
page_type: reference

---

# Was ist neu in Braze {#whats-new-in-braze}

{% alert tip %}
Weitere Informationen zu den auf dieser Seite aufgeführten Updates erhalten Sie von Ihrem Account Manager oder [öffnen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support/). In unseren [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs/) finden Sie weitere Informationen über unsere monatlichen SDK-Versionen, Verbesserungen und grundlegenden Änderungen.
{% endalert %}

{% details 28. Mai 2026 %}

## Veröffentlichung am 28. Mai 2026 {#may-28-2026-release}

### Daten und Berichterstattung {#data-reporting}

#### Push-Performance-Dashboard

Das [Push-Performance-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) bietet Ihnen eine einzige, kanalübergreifende Ansicht des Push-Engagements, einschließlich Sendungen, Bounces, Zustellungen sowie direkter, beeinflusster und gesamter Öffnungsraten über ein konfigurierbares Zeitfenster. Nutzen Sie es, um den allgemeinen Zustand Ihres Push-Kanals zu verstehen, ohne Daten aus einzelnen Kampagnen oder Canvases zusammenfassen zu müssen.

#### Geolocation-Felder in Katalogselektionen {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

Kataloge unterstützen jetzt entfernungsbasierte Filterung mit dem neuen Geolocation-Feldtyp und Katalogselektions-Operatoren. Dies hilft Ihnen, relevantere standortbezogene Erlebnisse zu schaffen, z. B. jedem/jeder Nutzer:in das nächstgelegene Restaurant anzuzeigen, offene Immobilien innerhalb von 50 km für eine Immobilienkampagne zu filtern oder Geschäfte in der Nähe eines bestimmten Events zu targetieren. Anstatt geografisches Targeting mit Stadt- oder Regionscodes zu approximieren, können Sie Katalogelemente nach Nähe zu einem Mittelpunkt filtern, einschließlich eines Liquid-Nutzerattributs wie dem letzten Standort eines Nutzers bzw. einer Nutzerin. Weitere Informationen finden Sie unter [Selektionen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#how-it-works).

#### Banner und RCS für den Berichts-Builder {#banner-and-rcs-for-report-builder}

Der [Berichts-Builder]({{site.baseurl}}/report_builder/) unterstützt Banner als Kanal und RCS als Unterkategorie unter SMS, sodass Sie die Performance für beide direkt in Ihren angepassten Berichten neben jedem anderen Braze-Kanal messen können.

#### Event-Aktionen für `ecommerce.cart_updated` {#ecommercecart_updated-event-actions}

Das [`ecommerce.cart_updated`-Event]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples) unterstützt die Aktionen `add` und `remove` neben `replace`, sodass Sie inkrementelle Warenkorbänderungen senden können, anstatt bei jedem Update einen vollständigen Warenkorb-Snapshot zu senden.

### BrazeAI<sup>TM</sup>

#### Content Optimizer für SMS-, MMS- und RCS-Nachrichten {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

Sie können den [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/) verwenden, um Hooks, Textkörper und CTAs für SMS-, MMS- und RCS-Nachrichten zu optimieren. Content Optimizer ist ein Agent, der Ihnen hilft, Nachrichteninhalte im großen Maßstab zu testen und zu optimieren, indem er KI nutzt, um automatisch große Mengen an Inhaltsvarianten zu generieren und zu bewerten.

### Orchestrierung {#orchestration}

#### Workspace-Zeitzonen {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

Verwenden Sie [Workspace-Zeitzonen]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone/), um bestimmte Zeitzonen für einzelne Workspaces zu definieren. Dadurch werden geplante Kampagnen und Canvases (die keine Ortszeit oder intelligentes Timing verwenden) gemäß der festgelegten Zeitzone des Workspace gesendet, anstatt der übergeordneten Unternehmens-Zeitzone.

Workspace-Zeitzonen für den Nachrichtenversand werden schrittweise eingeführt, sodass Sie diese Einstellungen möglicherweise noch nicht in Ihrem Dashboard sehen.

### Kanäle und Touchpoints {#channels-touchpoints}

#### WhatsApp `inbound_profile_name`

Sie können den WhatsApp-Anzeigenamen eines Nutzers bzw. einer Nutzerin automatisch aus dem Inbound-Messaging-Webhook von Meta erfassen und in das Braze-Profil schreiben. Wenn eine eingehende WhatsApp-Nachricht empfangen wird, stellt Braze den Profilnamen als neues WhatsApp-Liquid-Attribut bereit, [{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/), das Sie in einem Canvas-User-Update-Schritt referenzieren können, um es in einem Profilfeld zu speichern.

#### Verwaiste SMS-Abo-Status {#orphaned-sms-subscription-states}

Braze [verwaltet automatisch verwaiste Abo-Status-Datensätze]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#how-braze-handles-orphaned-subscription-states) (Abo-Daten, die für eine Telefonnummer oder E-Mail-Adresse gespeichert sind, die keinem Nutzerprofil zugeordnet ist), um eine unbeabsichtigte Vererbung des Abo-Status zu verhindern. Dies schützt Nutzer:innen vor Szenarien, in denen ein neu erstelltes Nutzerprofil fälschlicherweise den Abo-Status eines zuvor gelöschten oder nicht verwandten Nutzers bzw. einer Nutzerin erbt.

### Partnerschaften {#partnerships}

#### Chord – Customer Data Platform

[Chord](https://www.chord.co/) bietet eine Customer Data Platform, die Events aus Ihrem E-Commerce-Storefront erfasst und standardisiert. Wenn Sie Chord mit Braze verbinden, fließen Kaufaktivitäten, Verhaltens-Events und Identitätsupdates in Braze, sodass Sie Kampagnen triggern und Profile aktuell halten können, ohne diese Pipelines selbst aufbauen zu müssen.

Weitere Informationen finden Sie unter [Chord]({{site.baseurl}}/partners/chord/).

#### Better Email – Templates

[Better Email](https://www.betteremail.dev) ist eine kollaborative Plattform zur E-Mail-Erstellung, die auf einem E-Mail-Design-System basiert. Teams können produktionsreife E-Mails aus einem gemeinsamen System von Blöcken und Stilen entwerfen, verwalten und exportieren, um Markenkonsistenz im großen Maßstab sicherzustellen, ohne auf Entwickler:innen oder Agenturen angewiesen zu sein.

Weitere Informationen finden Sie unter [Better Email]({{site.baseurl}}/partners/better_email/).

#### DailyPlay – Dynamische Inhalte {#dailyplay-dynamic-content}

[DailyPlay](https://dailyplay.ai/) ist eine Gamification-Plattform. Nutzen Sie sie, um personalisierte, markengerechte Spiele und integrierte Belohnungssysteme zu starten, die das Engagement vertiefen und die Bindung verbessern.

Weitere Informationen finden Sie unter [DailyPlay]({{site.baseurl}}/partners/dailyplay/).

### SDK

#### Grundlegende SDK-Updates {#sdk-breaking-updates}

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Flutter SDK 19.0.0](https://pub.dev/packages/braze_plugin/changelog#1900)
    - Die minimal unterstützte Dart-Version ist `2.17.0`.
    - Das SDK-Logging wird jetzt auf der Dart-Ebene gesteuert.
    - Aktualisiert die nativen SDK-Bindungen, einschließlich der nativen Android-Bridge von [Braze Android SDK 41.1.1 auf 42.2.0](https://github.com/braze-inc/braze-android-sdk/compare/v41.1.1...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Behebt einen Absturz.
- [Cordova 16.0.1](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/16.0.1)
    - Behebt die iOS-Initialisierung bei Verwendung von `cordova-ios` 8 mit dem `SwiftDelegate`-Template.
- [Unity SDK 11.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Aktualisiert die nativen SDK-Bindungen, einschließlich der nativen iOS-Bridge von Braze [Swift SDK 13.2.0 auf 14.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Aktualisiert die native Android-Bridge von [Braze Android SDK 36.0.0 auf 42.2.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Die minimal erforderliche Android SDK-Version ist 23. Weitere Informationen finden Sie unter [Braze Android SDK-Versionsinformationen](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
    - Die minimal erforderliche Unity-Version wurde auf Unity 6 ([6000.0.66f2](https://unity.com/releases/editor/whats-new/6000.0.66f2) oder höher) aktualisiert.
    - News Feed wurde entfernt.
        - `RequestFeedRefresh()`, `RequestFeedRefreshFromCache()`, `LogFeedDisplayed()`, `LogCardImpression(string)`, `LogCardClicked(string)` wurden entfernt.
    - Behebt kleinere Fehler.
- [React Native 20.1.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/20.1.0)
    - Aktualisiert die Android SDK-Bindungen.
    - Behebt ein Problem mit Push-Benachrichtigungs-Deeplinking.
- [Segment Swift 8.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#800)
    - Aktualisiert die Braze Swift SDK-Bindungen, um Versionen der `14.0.0+` SemVer-Bezeichnung zu erfordern.
        - Dies ermöglicht die Kompatibilität mit jeder Version des Braze SDK von `14.0.0` bis, aber nicht einschließlich, `15.0.0`.
        - Weitere Informationen zu möglichen grundlegenden Änderungen finden Sie im [Changelog-Eintrag für `14.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1400).
    - Fügt Unterstützung für SDK-Authentifizierung hinzu.

{% enddetails %}
{% details 30. April 2026 %}

## Veröffentlichung am 30. April 2026 {#april-30-2026-release}

### Daten und Berichterstattung

#### Schnelle Nutzer:innen-Erstellung für individuelle Profilerstellung {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

Sie können jetzt ein individuelles Nutzerprofil über **Import Users** erstellen, indem Sie **Quick User Add** auswählen und eine E-Mail-Adresse oder externe ID eingeben.

Zuvor erforderte die Erstellung von Nutzer:innen über diesen Workflow einen CSV-Upload oder eine automatisierte Aufnahmemethode.

Weitere Informationen finden Sie unter [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).

#### Null-Kopie-CDI-Synchronisierungen für Canvas-Trigger {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

CDI unterstützt jetzt den Datentyp `Canvas triggers` für die Null-Kopie-Personalisierung. Sie können Canvases aus Warehouse- oder S3-Daten triggern und Kontextfelder übergeben, ohne diese Felder auf Braze-Nutzerprofilen persistent zu speichern.

Zuvor erforderten CDI-Synchronisierungen, dass Daten für diese Art von Personalisierungs-Workflow auf Braze-Profile geschrieben wurden.

Weitere Informationen finden Sie unter [Null-Kopie-Personalisierung mit CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/).

#### Empfohlene E-Commerce-Events {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

[Empfohlene E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) decken sechs Schritte der Kaufreise ab: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` und `order_refunded`. Wenn Sie diese Events erfolgreich senden, validiert Braze die Daten und stellt sie einer wachsenden Anzahl von Plattform-Features zur Verfügung.

### Currents und Datashare {#currents-and-datashare}

#### Neue Banner- und WhatsApp-Currents-Updates {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

Currents und Datashare enthalten jetzt ein neues `Banner.Dismiss`-Event und zusätzliche Felder für bestehende WhatsApp-Events.

Zuvor waren diese Banner-Dismiss-Events und WhatsApp-Felder in den Exportdaten nicht verfügbar.

Weitere Informationen finden Sie im [Currents Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/).

### Orchestrierung

#### Mehrsprachige Übersetzungen {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

Erstellen Sie [mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) mit einer schnellen, einmaligen Gebietsschema-Einrichtung, die keinen komplexen Code erfordert und es Ihnen ermöglicht, mit Zuversicht an alle Ihre Märkte zu senden.

#### Migration zu granularen Berechtigungen {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

Die Verwaltung, wer auf Ihr Konto zugreifen und bestimmte Aktionen ausführen kann, ist sowohl für die Sicherheit als auch für die betriebliche Effizienz entscheidend. Um Ihnen mehr Kontrolle zu geben, führt Braze [granulare Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration/) ein, eine flexiblere und präzisere Möglichkeit, den Nutzerzugang in Ihrem Konto zu verwalten.

#### Canvas-Komponente „An Ziel senden“ {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

Der [Schritt „An Ziel senden“]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination/) ermöglicht es Ihnen, Nutzer:innen von einem Canvas in ein anderes zu senden. Wenn Sie beispielsweise zwei Canvases haben, die Messaging für Werbeangebote teilen, können Sie „An Ziel senden“ verwenden, um diese Canvases zu verbinden.

#### Canvas-Context-Verbesserungen {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

In Canvas können Sie jetzt Kontextvariablen referenzieren, um Folgendes festzulegen:

- Ein Entfernungs-Event für Content Cards
- Den Ablauf von Content Cards

Weitere Details finden Sie unter [Kartenerstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas).

#### Zustellvalidierungs-Fortschrittsverhalten für Nachrichten-Schritte {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

[Zustellvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations) bieten eine zusätzliche Prüfung, um zu bestätigen, dass Ihre Zielgruppe die Zustellkriterien beim Nachrichtenversand erfüllt. Wenn ein:e Nutzer:in die festgelegten Zustellvalidierungen für einen Nachrichten-Schritt nicht erfüllt, können Sie die Einstellung **Zustellvalidierungs-Fortschrittsverhalten** verwenden, um festzulegen, ob der/die Nutzer:in zum nächsten Schritt fortschreiten oder das Canvas verlassen soll.

#### Workspace-Messaging-Rate-Limits

{% multi_lang_include release_type.md release="General availability" %}

Verwenden Sie [Workspace-Messaging-Rate-Limits]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits/), um die Zustellrate Ihrer ausgehenden Nachrichten von Ihrer Plattform zu regulieren und sicherzustellen, dass Ihre Nutzer:innen die Nachrichten erhalten, die sie benötigen. Workspace-Messaging-Rate-Limits werden schrittweise eingeführt, sodass Sie diese Einstellungen möglicherweise noch nicht in Ihrem Dashboard sehen.

### Kanäle und Touchpoints

#### WhatsApp Template Builder

{% multi_lang_include release_type.md release="Early access" %}

Der [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/) ermöglicht es Ihnen, WhatsApp-Nachrichten-Templates direkt in Braze zu erstellen und einzureichen – ohne zwischen Braze und dem Meta Business Manager wechseln zu müssen. Nachdem Meta Ihr Template genehmigt hat, können Sie es in beliebig vielen Kampagnen und Canvases verwenden.

#### Shopify-Produkt-Tags, Metafelder und Sammlungen {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

Sie können jetzt [Shopify-Produkt-Tags, Sammlungen und Metafelder]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/) aus Ihrem Shopify-Shop in Ihren Braze-Katalog synchronisieren. Dies bietet reichhaltigere Produktdaten für Personalisierung, Segmentierung und katalogbasiertes Messaging ohne angepasste Workarounds.

### Partnerschaften

#### GRAVITY – Daten und Analytics – Kundenbindung {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/) ist eine Enterprise-Kundenbindungsplattform von Loyalty Juggernaut Inc. (LJI), die es Marken in den Bereichen Einzelhandel, Reisen, Gastronomie (einschließlich Schnellrestaurants) und Finanzdienstleistungen ermöglicht, Programme der nächsten Generation zu entwerfen, zu verwalten und zu skalieren – und so messbares Wachstum bei Engagement, Bindung und Customer Lifetime Value durch personalisierte, datengestützte Erlebnisse zu erzielen.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

Die folgenden SDK-Updates wurden veröffentlicht. Weitere Details finden Sie in den [SDK Changelogs]({{site.baseurl}}/releases/sdk_changelogs/).

#### Grundlegende SDK-Updates

{% multi_lang_include release_type.md release="General availability" %}

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [React Native SDK 19.2.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.2.0)
    - Unterstützung für verzögerte Initialisierung.
- [Android SDK 42.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.0.0)
    - Fehlerbehebungen für In-App-Nachrichten und Banner.
- [Swift SDK 14.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.1.0)
    - Unterstützung für Banner-Dismissals.
- [Web SDK 6.7.0](https://github.com/braze-inc/braze-web-sdk/releases/tag/v6.7.0)
    - Unterstützung für Banner-Dismissals.
- [Android SDK 42.1.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.1.0)
    - Unterstützung für Banner-Dismissals.
- [Braze Segment Android 17.0.0](https://github.com/braze-inc/braze-segment-android/releases/tag/v17.0.0)
    - Dies ist die letzte Version des Braze Segment Android-Plugins, da es Analytics-Android verwendet, das im März 2026 das Ende des Supports erreicht hat. Migrieren Sie zum [Braze Segment Kotlin-Plugin](https://github.com/braze-inc/braze-segment-kotlin), das [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) verwendet.
    - Aktualisiert die nativen SDK-Versionen.

{% enddetails %}
{% details 2. April 2026 %}

## Veröffentlichung am 2. April 2026 {#april-2-2026-release}

### Daten und Berichterstattung

#### Neue Banner-Kanalfelder in Currents- und Datashare-Events {#new-banner-channel-fields-in-currents-and-datashare-events}

Braze hat Felder für bestehende Banner-Kanal-Events in Currents- und Datashare-Exporten hinzugefügt. Eine Liste dieser Event- und Feld-Updates finden Sie unter [Änderungen in Version 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage).

#### Mixpanel EU- und Indien-Rechenzentrumsunterstützung für Currents {#mixpanel-eu-and-india-data-center-support-for-currents}

Die Currents-Mixpanel-Integration unterstützt jetzt die EU- und Indien-Rechenzentren von Mixpanel. Wenn Sie eine Mixpanel-Integration konfigurieren, können Sie auswählen, an welche Mixpanel-Region Braze Ihre Daten sendet. Dieses Update unterstützt die wachsende internationale Präsenz von Mixpanel für gemeinsame Kunden. Weitere Informationen finden Sie unter [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

#### Wiederverwendbare Cloud-Datenaufnahme-Quellen und -Synchronisierungen (CDI) {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

Die Cloud-Datenaufnahme (CDI) hat ein neues Design, das Quellen und Synchronisierungen trennt, sodass Sie eine Quelle für mehrere Synchronisierungen wiederverwenden können. Bestehende Synchronisierungen werden automatisch und ohne Ausfallzeit zum neuen Quellen-und-Synchronisierungen-Modell migriert. Gehen Sie zu **Cloud Data Ingestion** > **Sources**, um Quellen anzuzeigen, zu bearbeiten oder zu erstellen, und wählen Sie dann beim Erstellen einer Synchronisierung eine Quelle aus dem Dropdown aus. Diese Änderung reduziert die wiederholte Einrichtung und schafft eine Grundlage für zukünftige Verbesserungen. Weitere Informationen finden Sie unter [Einrichten von Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### Support-Tickets über BrazeAI Operator<sup>TM</sup> einreichen {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) enthält jetzt einen Flow zum Einreichen von Braze-Support-Tickets, ohne das Dashboard zu verlassen. Schritte, automatisch enthaltenen Kontext und Tipps für eine schnellere Lösung finden Sie unter [Support-Tickets mit BrazeAI Operator einreichen]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/).

### Orchestrierung

#### Mehrsprachige Übersetzungen

{% multi_lang_include release_type.md release="General availability" %}

Nachdem Sie Ihrem Workspace Gebietsschemata hinzugefügt haben, verwenden Sie [mehrsprachige Übersetzungen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/), um Nutzer:innen in verschiedenen Sprachen innerhalb einer einzigen Push-Benachrichtigung, E-Mail, eines Banners, einer In-App-Nachricht oder eines Content Blocks anzusprechen.

![Vorschau der Gebietsschemata]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Canvas-Context-Verbesserungen

{% multi_lang_include release_type.md release="General availability" %}

In Canvas können Sie jetzt Kontextvariablen referenzieren, um Folgendes festzulegen:

- Einen [Ablauf]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#set-an-expiration) für Banner und In-App-Nachrichten in einem Nachrichten-Schritt
- [Personalisierte Verzögerungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-delays) für Aktionspfad-Schritte

Im Feld für den Kontextvariablennamen können Sie auch den Namen der Kontextvariable eingeben oder ihn aus dem Dropdown im Schritt-Editor auswählen. Weitere Details finden Sie unter [Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/) und [Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

### Kanäle und Touchpoints

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk/) ist ein Messaging-Kanal, der Broadcast-Messaging und 1:1-Chat mit Nutzer:innen ermöglicht. Erstellen Sie ein personalisiertes Nutzererlebnis, indem Sie Liquid und andere dynamische Inhalte verwenden, um eine Umgebung zu schaffen, die ein reichhaltiges Nutzererlebnis mit Ihrer Marke fördert und verbessert.

![Eine KakaoTalk-Listenelementnachricht.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Banner in Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Sie können [Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/) als Messaging-Kanal in Canvas-[Nachrichten-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) verwenden. Banner ermöglichen es Ihnen, App- oder Website-Inhalte dynamisch zu personalisieren und die Berechtigung und das Verhalten der Nutzer:innen in Echtzeit widerzuspiegeln.

### Partnerschaften

#### CataBoom – Nachrichtenpersonalisierung – Visuelle und interaktive Inhalte {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom/) ist eine Gamification-Plattform. Marken nutzen sie, um interaktive digitale Erlebnisse zu erstellen und zu starten, darunter Glücksrad-Spiele, Quizze und Sofortgewinnspiele. Diese Erlebnisse vertiefen das Engagement und sammeln First-Party-Daten.

#### Denada – Nachrichtenorchestrierung – Templates {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada/) ist eine KI-gestützte Marketing-Kreativplattform, die es Fachexperten ermöglicht, markengerechte Marketingmaterialien durch natürliche Konversation zu erstellen. Mit Denada können Teams von der Ideenfindung bis zum fertigen E-Mail-Inhalt gelangen, ohne Design-Expertise zu benötigen.

#### Poq – E-Commerce – Mobile-App-Plattform {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq/) ermöglicht es Unternehmen, schnell vollständig native iOS- und Android-Apps zu starten, zu verwalten und zu skalieren – und so leistungsstarke mobile Erlebnisse zu liefern, die den Handel vorantreiben und Ihr Markenversprechen zum Leben erwecken.

#### The Trade Desk – Canvas Audience Sync

Mit der [Braze Audience Sync zu The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/) können Sie Ihre First-Party-Nutzerdaten dynamisch von Braze direkt in The Trade Desk synchronisieren – für Anzeigen-Retargeting, Lookalike-Modellierung und Unterdrückung.

### SDK

#### Verbinden Sie Ihre integrierte Entwicklungsumgebung (IDE) mit dem Docs MCP {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

Verwenden Sie KI-Codierungsassistenten, um Ihren Braze-Integrations-Workflow zu beschleunigen, indem Sie Ihre integrierte Entwicklungsumgebung (IDE) über Context7 mit dem Braze Docs MCP verbinden. Dies gibt Ihrem Assistenten direkten Zugriff auf die aktuelle Braze-Dokumentation, sodass er genauere SDK-Anleitungen, Codebeispiele und Fehlerbehebungshilfen in Ihrer Entwicklungsumgebung generieren kann. Einrichtungsschritte für Cursor, Claude Desktop und VS Code finden Sie unter [Entwickeln mit einem LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp).

#### Grundlegende SDK-Updates

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Cordova 15.0.0](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/15.0.0)
    - Update der nativen Android-Bridge [von Braze Android SDK 39.0.0 auf 41.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen iOS-Bridge [von Braze Swift SDK 13.2.0 auf 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Behebt ein Problem mit `subscribeToInAppMessage` im Zusammenhang mit dem Erfolgs-Callback.
- [Roku SDK 2.2.1](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.2.1)
    - Behebt einen Absturz bei der Verarbeitung einer fehlgeschlagenen HTTP-Anfrage für Template-basierte In-App-Nachrichten, wenn das Gerät eine intermittierende oder keine Verbindung hat.
- [Web SDK 6.6.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#660)
    - Fügt die Initialisierungsoption `cookieExpiryInDays` hinzu, um die Cookie-Dauer ab dem Standard von 400 Tagen zu konfigurieren.
- [Flutter SDK 18.0.0](https://pub.dev/packages/braze_plugin/changelog#1800)
    - Fügt Unterstützung für verzögerte Initialisierung hinzu.
    - Vereinfacht den iOS-Integrationsprozess, sodass kein nativer Code mehr geschrieben werden muss, um Content Cards, Banner, Feature-Flags, In-App-Nachrichten oder Push-Benachrichtigungs-Updates vom nativen SDK weiterzuleiten.
        - Das SDK richtet diese Abonnements jetzt automatisch ein, wenn die Braze-Instanz erstellt wird.
        - Dies entspricht dem bestehenden Verhalten auf Android.
        - Entfernen Sie zur Migration alle manuellen Aufrufe von `braze.contentCards.subscribeToUpdates()`, `braze.banners.subscribeToUpdates()`, `braze.notifications.subscribeToUpdates`, `braze.featureFlags.subscribeToUpdates` und `braze.inAppMessagePresenter` im `AppDelegate`.
        - Standardmäßig werden In-App-Nachrichten angezeigt. Um dies zu überschreiben, setzen Sie einen angepassten In-App-Nachrichten-Presenter mit dem `postInitialization`-Closure in `BrazePlugin.configure(_:postInitialization:)`.
- [Swift SDK 14.0.4](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1404)
    - Behebt einen Fehler mit der Push-Automatisierung bei SDK-Neuinitialisierung.
    - Behebt ein Problem, bei dem ungültige Bilder in Push Stories nicht herausgefiltert wurden.
- [Swift SDK 14.0.3](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1403)

{% enddetails %}

{% details 5. März 2026 %}

## Veröffentlichung am 5. März 2026 {#march-5-2026-release}

### Daten und Berichterstattung

#### Neues Rechenzentrum {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Braze hat ein neues [Rechenzentrum]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/) gestartet: JP-01. Sie können sich bei der Einrichtung Ihres Braze-Kontos für regionsspezifische Rechenzentren anmelden.

#### Kontextvariablen {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

[Kontextvariablen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) sind temporäre Daten, die Sie innerhalb der Journey eines Nutzers bzw. einer Nutzerin durch ein bestimmtes Canvas erstellen und verwenden können. Jedes Mal, wenn ein:e Nutzer:in das Canvas betritt – auch wenn er/sie es zuvor betreten hat – werden die Kontextvariablen basierend auf den neuesten Eintrittsdaten und der Canvas-Konfiguration neu definiert. Dieser Ansatz ermöglicht es jedem Canvas-Eintritt, seinen eigenen unabhängigen Kontext beizubehalten, sodass Nutzer:innen mehrere aktive Zustände innerhalb derselben Journey haben können, während der spezifische Kontext für jeden Zustand erhalten bleibt.

#### Cloud-Datenaufnahme-Quellen {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

Die [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) hat eine neue Benutzeroberfläche, die Quellen von Synchronisierungen trennt, sodass Sie eine einzelne Quelle für beliebig viele Synchronisierungen wiederverwenden können. Dies reduziert doppelte Konfigurationen und vereinfacht die Einrichtung, wenn Sie mehrere Synchronisierungen haben. Wenn Sie bestehende Synchronisierungen haben, werden diese automatisch und ohne Ausfallzeit zur neuen Quellen-und-Synchronisierungen-Struktur migriert. Um zu beginnen, gehen Sie zu **Cloud Data Ingestion** > **Sources**, um Quellen anzuzeigen, zu bearbeiten oder zu erstellen, und wählen Sie dann beim Erstellen einer Synchronisierung eine Quelle aus dem Dropdown aus.

#### Zusätzliche Felder für Currents- und Data-Share-Events {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

[Currents- und Data-Share-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04) enthalten jetzt die folgenden neuen Felder, um die für Analytics und nachgelagerte Systeme verfügbaren Daten zu vertiefen:

- `agentconsole.AgentExecuted`: `error` (String) hinzugefügt – eine Beschreibung eines aufgetretenen Fehlers.
- `agentconsole.ToolInvocation`: `request_id` (String) hinzugefügt – eine eindeutige ID für die gesamte LLM-Anfrage und vollständige Ausführung.
- `users.messages.rcs.InboundReceive`: `canvas_variation_name` (String) hinzugefügt – der Name der Canvas-Variante, die der/die Nutzer:in erhalten hat.

#### Kampagnen- und Canvas-Felder für Snowflake Data Share {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) enthält jetzt zusätzliche Felder mit Kampagnen- und Canvas-Informationen in 66 bestehenden Tabellen, darunter:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV-Vorimportvalidierung und Fehlerberichterstattung {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

[CSV-Nutzerimporte]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/) unterstützen jetzt Vorimportvalidierung und detaillierte Fehlerberichterstattung. Wählen Sie vor dem Import auf der Seite **Import Users** die Option **Validate file before importing** – Braze scannt Ihre Datei und erstellt einen Bericht, der Zeilen identifiziert, die vollständig fehlschlagen (Fehler), und Zeilen, die mit einigen übersprungenen Werten erfolgreich sind (Warnungen). Sie können den Bericht herunterladen, Ihre CSV korrigieren und erneut hochladen oder wie vorhanden fortfahren. Nach Abschluss des Imports ist auch ein herunterladbarer Bericht über fehlgeschlagene Zeilen mit dem genauen Grund für jedes Problem verfügbar.

#### Messaging-Diagnose-Dashboard {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="Early access" %}

Das [Messaging-Diagnose-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/) bietet eine Aufschlüsselung der Ergebnisse des Nachrichtenversands auf hoher Ebene, mit der Sie Trends erkennen und potenzielle Probleme in Ihrer Messaging-Konfiguration diagnostizieren können. Dieses Dashboard kann Ihnen helfen zu verstehen, warum Nachrichten aus Ihren Kampagnen oder Canvases möglicherweise nicht wie erwartet gesendet wurden.

### BrazeAI<sup>TM</sup>

#### Braze-Agenten in der Agentenkonsole {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

[Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/) sind KI-gestützte Helfer, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, sodass Sie personalisiertere Kundenerlebnisse zustellen können. Wenn Sie einen Agenten erstellen, definieren Sie seinen Zweck und legen Leitplanken fest, wie er sich verhalten soll. Sobald er aktiv ist, kann der Agent in Braze [eingesetzt]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/) werden, um personalisierte Texte zu generieren, Echtzeit-Entscheidungen zu treffen oder Katalogfelder zu aktualisieren.

### Orchestrierung

#### Granulare Nutzerberechtigungen {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze führt [granulare Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) ein, eine flexiblere Möglichkeit, den Nutzerzugang zu verwalten. Unter [Migration zu granularen Berechtigungen]({{site.baseurl}}/granular_permissions_migration/) erfahren Sie mehr über den Migrationsprozess, einschließlich der Zuordnung von Legacy-Berechtigungen zu granularen Berechtigungen.

#### Kanalbasiertes Rate-Limiting {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

Wenn Sie ein Rate-Limit für die Zustellgeschwindigkeit einer Multichannel-Kampagne oder eines Canvas festlegen, können Sie entweder ein gemeinsames Rate-Limit oder ein [kanalbasiertes Limit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases) wählen. Wenn eine Multichannel-Kampagne oder ein Canvas kanalbasiertes Rate-Limiting verwendet, gilt das Rate-Limit für jeden der ausgewählten Kanäle. Sie können Ihre Kampagne oder Ihr Canvas beispielsweise so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die Kampagne oder das Canvas gesendet werden.

#### Canvas-Context-Schritt {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

[Canvas-Context-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) ermöglichen es Ihnen, eine oder mehrere Variablen für eine:n Nutzer:in zu erstellen und zu aktualisieren, während er/sie sich durch ein Canvas bewegt. Wenn Sie beispielsweise ein Canvas haben, das saisonale Rabatte verwaltet, können Sie eine Kontextvariable verwenden, um bei jedem Eintritt eines Nutzers bzw. einer Nutzerin in das Canvas einen anderen Rabattcode zu speichern.

### Kanäle und Touchpoints

#### Lokalisierungen in Content Blocks übersetzen {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

Nachdem Sie Ihrem Workspace Gebietsschemata hinzugefügt haben, können Sie [Nutzer:innen in verschiedenen Sprachen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) innerhalb eines Content Blocks ansprechen.

### Partnerschaften

#### Algolia – Suche und Empfehlungen {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia/) ist eine Such- und Discovery-Plattform, die Entwicklern hilft, schnelle, relevante und skalierbare Sucherlebnisse zu erstellen. Mit einem leistungsstarken API-First-Ansatz kombiniert Algolia fortschrittliche Ranking-Algorithmen mit KI-gestützten Insights für nahtlose Website-Suche, Navigation und personalisierte Content-Entdeckung.

#### Anthropic – KI-Modellanbieter {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic/) ist ein KI-Sicherheits- und Forschungsunternehmen, das Claude entwickelt, einen KI-Assistenten der nächsten Generation, der hilfreich, ehrlich und sicher für eine Vielzahl von Sprachaufgaben konzipiert ist.

#### Canva – Nachrichtenpersonalisierung – Creative Studio {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva/) synchronisiert Ihre Bilder in Canva direkt mit der Braze-Medienbibliothek, optimiert Ihren kreativen Workflow und hält Ihre visuellen Assets über alle Ihre Messaging-Kanäle hinweg aktuell.

#### DOTS.ECO – Rewards

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco/) ermöglicht es Ihnen, Nutzer:innen mit realen Umweltauswirkungen durch nachverfolgbare digitale Zertifikate zu belohnen. Jedes Zertifikat kann Metadaten wie eine teilbare Zertifikats-URL und Bild-URL enthalten, sodass Nutzer:innen ihren Wirkungsnachweis einsehen (und erneut aufrufen) können.

#### Figma – Nachrichtenpersonalisierung – Creative Studio {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma/) ist eine kollaborative Designplattform, mit der Sie Produkte erstellen, gestalten und prototypisieren können. Verwenden Sie diese Integration, um Bilder und visuelle Assets von Figma direkt in die Braze-Medienbibliothek zu senden.

#### Flybuy – Nachrichtenpersonalisierung – Standort {#flybuy-message-personalization-location}

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy/) von Radius Networks ist die führende Omnichannel-Standortplattform, die KI-gestützte Technologie nutzt, um die Servicegeschwindigkeit bei Abholung, Lieferung, Drive-Thru und Dine-In zu optimieren. Über die integrierte Marketing Suite ermöglicht Flybuy Marken auch die Zustellung hyper-zielgerichteter, momentbasierter Nachrichten, die das Engagement fördern, den Bestellwert erhöhen und breitere Kundenbindungsinitiativen unterstützen.

#### Google Gemini – KI-Modellanbieter {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini/) ist Googles Familie von KI-Modellen, die fortschrittliches Reasoning über Text, Code und Bilder hinweg kombiniert, um Marken bei der Bereitstellung intelligenterer, personalisierterer Erlebnisse zu unterstützen.

#### Limbik – Nachrichtenpersonalisierung – Personalisierungs-Engines {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik/) ist Ihre KI-Resonanzschicht – sie prognostiziert, wie reale Zielgruppen Nachrichten, Konzepte und KI-Ausgaben interpretieren und darauf reagieren, bevor sie den Markt erreichen. Basierend auf kontinuierlicher Primärforschung in über 60 Ländern und 25+ Sprachen liefert Limbik menschlich validierte synthetische Zielgruppen – digitale Populationen, die reale Zielgruppenreaktionen mit Maschinengeschwindigkeit und forschungsgerechter Genauigkeit simulieren (95 % Konfidenz, 1,5 % bis 3 % Fehlermarge). Limbik gibt Ihnen die Möglichkeit, sofort sicherzustellen, dass Ihre Nachrichten mit dem übereinstimmen, was Ihre Zielgruppe glaubt und fühlt.

#### Linkrunner – Nachrichtenorchestrierung – Attribution {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner/) ist eine mobile Attribution- und Analytics-Plattform, die Ihnen hilft, Ihre Nutzerakquisitionskampagnen zu verfolgen und zu analysieren.

#### Mailizio – Nachrichtenorchestrierung – Templates {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio/) ist eine Plattform zur Erstellung und Verwaltung von E-Mails, mit der Sie wiederverwendbare, markensichere Inhalte mit einem intuitiven visuellen Editor erstellen können. Mit der Integration von Mailizio in Braze können Sie Ihre Content Blocks und E-Mail-Templates exportieren und dann automatisch In-App-Nachrichten aus denselben Assets generieren, was eine schnelle und vollständig kontrollierte Kampagnenbereitstellung ermöglicht.

#### Open Loyalty – Daten und Analytics – Kundenbindung {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty/) ist eine cloudbasierte Plattform für Kundenbindungsprogramme, mit der Sie Kundenbindungs- und Rewards-Programme erstellen und verwalten können. Die Integration von Braze und Open Loyalty synchronisiert Loyalitätsdaten – wie Punktestand, Tier-Änderungen und Ablaufwarnungen – direkt in Echtzeit mit Braze. Damit können Sie personalisierte Nachrichten (E-Mail, Push, SMS) triggern, wenn sich der Treuestatus eines Nutzers bzw. einer Nutzerin ändert.

#### OpenAI – KI-Modellanbieter {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai/) entwickelt fortschrittliche KI-Modelle wie GPT, die natürliches Sprachverständnis und -generierung ermöglichen und Marken befähigen, bedeutungsvolle Kundeninteraktionen aufzubauen und zu skalieren.

#### Shopgate – Kanäle {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate/) ist eine Mobile-Commerce- und Omnichannel-Plattform, die Händlern hilft, Shopping-Apps zu erstellen und die Effizienz stationärer Geschäfte durch Fulfillment-Tools und Clienteling zu verbessern, also personalisierte Kundenbetreuung im Geschäft basierend auf Kundendaten.

#### Splio – Daten und Analytics – Kohortenimport {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio/) ist ein Tool zur Zielgruppenerstellung, mit dem Sie die Anzahl der Kampagnen und den Umsatz steigern können, ohne das Kundenerlebnis zu beeinträchtigen, und das Analytics zur Verfolgung der Performance von CRM-Kampagnen sowohl online als auch offline bietet.

### SDK

#### Grundlegende SDK-Updates

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Update der Android-Bindung von [Braze Android SDK 37.0.0 auf 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der iOS-Bindung von [Braze Swift SDK 13.3.0 auf 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Neue transitive NuGet-Abhängigkeiten hinzugefügt, die vom Braze Android SDK benötigt werden:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib wurde von 2.0.21.3 auf 2.3.0.1 aktualisiert. Wenn Ihr Projekt dieses Paket explizit auf eine ältere Version fixiert, müssen Sie es aktualisieren, um Wiederherstellungsfehler zu vermeiden.
    - Das News-Feed-Feature wurde entfernt.
        - Dieses Feature wurde im nativen Android SDK in Version [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0) entfernt.
        - Dieses Feature wurde im nativen Swift SDK in Version [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0) entfernt.
    - Der Enum-Fall BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData wurde in BRZInAppMessageDismissalReason.WipeData umbenannt.
- [Expo Plugin 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - Diese Version erfordert 19.0.0 des Braze React Native SDK.
    - (Android) Ein Speicherleck in der Datenpersistenzschicht wurde behoben.
    - (Android) Unterstützung für `Braze.getInitialPushPayload()` hinzugefügt, um Push-Benachrichtigungs-Deeplinks zu verarbeiten, wenn die App aus einem beendeten Zustand gestartet wird. Dies behebt ein Problem, bei dem Deeplinks aus Push-Benachrichtigungen auf Android nicht verarbeitet wurden, wenn die App kalt gestartet wurde.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Update der nativen Swift SDK-Versionsbindungen von Braze Swift SDK 13.3.0 auf 14.0.1.
    - Update der nativen Android SDK-Versionsbindungen von Braze Android SDK 40.0.2 auf 41.0.0.

{% enddetails %}

{% details 5. Februar 2026 %}

## Veröffentlichung am 5. Februar 2026 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### Content Optimizer

{% multi_lang_include release_type.md release="Beta" %}

[Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/) ist ein kontinuierlicher Canvas-Schritt zum Testen hochvariabler Inhalte, der eine automatisierte Optimierung des Engagements liefert. Über eine Drag-and-Drop-Oberfläche, ähnlich wie beim Nachrichten-Schritt, können Sie die zu testenden Komponenten definieren, mithilfe von KI Varianten generieren (oder sie manuell eingeben) und diese Komponenten mithilfe von Liquid-Tags auf den Inhalt Ihrer Nachricht abbilden.

Basierend auf einem kontextlosen Multi-Armed-Bandit-Optimierer sendet Content Optimizer eine einzelne Nachricht pro Nutzer:in und bestimmt anhand von Prognosen, welche Kombination von Komponentenvarianten zugestellt werden soll. Da der Schritt im Laufe der Zeit Daten sammelt, steigt die Sendezuweisung für leistungsstarke Varianten natürlich an, während leistungsschwache Varianten abnehmen. Content Optimizer funktioniert am besten mit Canvases, die wiederholt versendet werden und ein konstantes tägliches Nutzer:innen-Volumen aufweisen (mindestens einige tausend Nutzer:innen pro Tag), um eine kontinuierliche Optimierung zu ermöglichen.

### Daten und Berichterstattung

#### Empfohlene E-Commerce-Events

{% multi_lang_include release_type.md release="Early access" %}

Um die empfohlenen E-Commerce-Events mit dem bestehenden Kauf-Event abzustimmen, haben wir das [Konversions-Event „Places Order“]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report) hinzugefügt, das dem Event „Makes Purchase“ ähnelt.

### Kanäle und Touchpoints

#### Lokalisierungen in Bannern übersetzen {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

Nachdem Sie Ihrem Workspace Gebietsschemata hinzugefügt haben, können Sie [Nutzer:innen in verschiedenen Sprachen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#translating-locales) innerhalb eines einzigen Banners ansprechen.

#### Breite für Drag-and-Drop Content Blocks konfigurieren {#configure-width-for-drag-and-drop-content-blocks}

[Passen Sie die Breite Ihres Content Blocks an]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/#using-the-editor-to-add-a-content-block), indem Sie den Button im Navigationsmenü auswählen. Die Standardbreite beträgt 100 %, wenn in Ihren globalen E-Mail-Stileinstellungen nichts angegeben ist; andernfalls werden die globalen Einstellungen beachtet.

![Ein doppelseitiger Pfeil mit einer Option zur Bearbeitung der Breite.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Automatisiertes IP-Warming verwenden {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

Mit [automatisiertem IP-Warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/#automated-ip-warming) können Sie Ihr tägliches Sendevolumen allmählich erhöhen, sodass Posteingangsanbieter Ihre Sendemuster lernen und ihnen vertrauen können. Braze sendet zuerst an Ihre am stärksten engagierten Abonnent:innen, sodass das tägliche Volumen in einem Tempo wachsen kann, das den Best Practices entspricht.

### Partnerschaften

#### LinkedIn – Canvas Audience Sync

Mit der [Braze Audience Sync zu LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) können Sie Nutzerdaten aus Ihrer Braze-Integration zu LinkedIn-Kundenlisten hinzufügen, um Anzeigen basierend auf Verhaltenstriggern, Segmentierung und mehr zuzustellen. Alle Kriterien, die Sie normalerweise zum Triggern einer Nachricht (z. B. Push, E-Mail, SMS und Webhook) in einem Braze-Canvas basierend auf Ihren Nutzerdaten verwenden, können jetzt eine Anzeige an diesen Nutzer bzw. diese Nutzerin in Ihren LinkedIn-Kundenlisten triggern.

#### Oracle Crowdtwist – Daten und Analytics {#oracle-crowdtwist-data-analytics}

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist/) ist eine führende Cloud-native Lösung zur Kundenbindung, mit der Marken personalisierte Kundenerlebnisse anbieten können. Die Lösung bietet mehr als 100 sofort einsatzbereite Engagement-Pfade, die Marketern eine schnellere Wertschöpfung ermöglichen, um eine umfassendere Sicht auf den Kunden zu entwickeln.

#### Fullstory – Dynamische Inhalte {#fullstory-dynamic-content}

Die [Plattform für Verhaltensdaten von Fullstory]({{site.baseurl}}/partners/fullstory/) hilft Technologieführern, bessere und fundiertere Entscheidungen zu treffen. Durch das Einspeisen digitaler Verhaltensdaten in ihren Analytics-Stack erschließt die patentierte Technologie von Fullstory die Leistungsfähigkeit hochwertiger Verhaltensdaten im großen Maßstab und verwandelt jeden digitalen Besuch in umsetzbare Insights.

#### Open Loyalty – Daten und Analytics {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty/) ist eine cloudbasierte Plattform für Kundenbindungsprogramme, mit der Sie Kundenbindungs- und Rewards-Programme erstellen und verwalten können. Die Integration von Braze und Open Loyalty synchronisiert Loyalitätsdaten – wie Punktestand, Tier-Änderungen und Ablaufwarnungen – direkt in Echtzeit mit Braze. Damit können Sie personalisierte Nachrichten (E-Mail, Push, SMS) triggern, wenn sich der Treuestatus eines Nutzers bzw. einer Nutzerin ändert.

#### DOTS.ECO – Erweiterungen {#dotseco-extensions}

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) ermöglicht es Ihnen, Nutzer:innen mit realen Umweltauswirkungen durch nachverfolgbare digitale Zertifikate zu belohnen. Jedes Zertifikat kann Metadaten wie eine teilbare Zertifikats-URL und Bild-URL enthalten, sodass Nutzer:innen ihren Wirkungsnachweis einsehen (und erneut aufrufen) können.

#### Mailizio – Nachrichtenorchestrierung {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio/) ist eine Plattform zur Erstellung und Verwaltung von E-Mails, mit der Sie wiederverwendbare, markensichere Inhalte mit einem intuitiven visuellen Editor erstellen können. Mit der Integration von Mailizio in Braze können Sie Ihre Content Blocks und E-Mail-Templates exportieren und dann automatisch In-App-Nachrichten aus denselben Assets generieren, was eine schnelle und vollständig kontrollierte Kampagnenbereitstellung ermöglicht.

### APIs

#### Medienbibliothek-POST-APIs {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

Assets aus der Medienbibliothek können jetzt über APIs hinzugefügt werden, sodass Kunden, Partner und Agenturen einen größeren Teil ihrer Workflows zur Nachrichtenerstellung automatisieren können. Verwenden Sie die [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/), um eine Asset-Datei direkt hochzuladen oder eine Datei von einer bestehenden URL zu kopieren. Dieses Feature schaltet Integrations- und Automatisierungsfunktionen frei.

### Currents und Datashare

#### Agentenkonsole-Events für Speicherziele und Datashare {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

Zwei neue [Events](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) sind jetzt für Speicherziele (AWS S3, GCS und Azure Blob Storage) und Snowflake Datashare verfügbar: `agentconsole.AgentExecuted` und `agentconsole.ToolInvocation`. Anhand dieser Events können Sie die Nutzung der Agentenkonsole und die Details in Ihren nachgelagerten Systemen analysieren, sodass Sie Ihre Agentennutzung besser verstehen und optimal nutzen können. Agenten ermöglichen es Ihnen, intelligente Agenten zu erstellen und einzusetzen, die bestimmte Aufgaben in Braze ausführen können, z. B. die Generierung von Inhalten in Canvases oder Katalogen und die Weiterleitung von Nutzer:innen auf der Grundlage intelligenter Entscheidungen. Weitere Informationen finden Sie im [Changelog zu Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Neue Wiederholungs-Events für einzelne Kanäle {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

Neue [Wiederholungs-Events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) sind jetzt für E-Mail, LINE, Push-Benachrichtigungen, SMS, Webhooks und WhatsApp-Kanäle verfügbar. Diese Events geben Aufschluss darüber, wann Frequency-Capping dazu führt, dass eine geplante Nachricht verzögert und nicht abgebrochen wird. Wenn eine Nachricht depriorisiert oder mit einem Frequency-Capping versehen wird, kann sie jetzt innerhalb eines konfigurierten Wiederholungsfensters erneut versucht werden. So erhalten Sie einen besseren Einblick in die Zustellmuster von Nachrichten und die Auswirkungen des Frequency-Cappings. Weitere Informationen finden Sie im [Changelog zu Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Neues Feld `time_ms` zum Event TokenStateChange hinzufügen {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

Dem Event [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) wurde ein neues `time_ms`-Feld hinzugefügt, das das Tracking von Änderungen des Push-Token-Status auf Millisekunden-Ebene ermöglicht. Diese verbesserte Präzision hilft Ihnen, den neuesten Status eines Push-Tokens zu verstehen, wenn innerhalb derselben Sekunde mehrere Änderungen auftreten. So können Sie sich in nachgelagerten Systemen darauf verlassen, dass Sie den korrekten Abo-Status haben. Weitere Informationen finden Sie im [Changelog zu Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Anonyme Nutzer:innen an Tealium-Ziele senden {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

Events, für die keine externe Nutzer-ID definiert wurde, können jetzt zu [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents)-Zielen gestreamt werden. Wenn Sie in Ihrer Currents-Integration das Kontrollkästchen „Events von anonymen Nutzer:innen einschließen“ auswählen, werden Events ohne externe Nutzer-ID an das Ziel gesendet, anstatt unterdrückt zu werden. Diese Fähigkeit ist entscheidend für nachgelagerte Analytics und Anwendungsfälle mit nicht identifizierten und anonymen Nutzer:innen.

##### Anonyme Nutzer:innen an CustomHTTP-Ziele senden {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

Events, für die keine externe Nutzer-ID definiert wurde, können jetzt zu CustomHTTP-Zielen gestreamt werden. Wenn Sie in Ihrer Currents-Integration das Kontrollkästchen „Events von anonymen Nutzer:innen einschließen“ auswählen, werden Events ohne externe Nutzer-ID an das Ziel gesendet, anstatt unterdrückt zu werden. Diese Fähigkeit ist entscheidend für nachgelagerte Analytics und Anwendungsfälle mit nicht identifizierten und anonymen Nutzer:innen.

#### Event „E-Mail-Öffnung“ – Feld „machine_open“ {#email-open-event-machine_open-field}

Das [Event „E-Mail-Öffnung“]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#email-open-events) generiert jetzt den Feldwert „machine_open“, um über die Metrik [_Maschinenöffnungen_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens) zu berichten.

### SDK

Die folgenden SDK-Updates wurden veröffentlicht. Swift SDK v14.0.1 behebt ein Problem mit der Handhabung von universellen Links. Android SDK v40.2.0 behebt ein potenzielles Speicherleck und behebt ein Problem mit mehreren geöffneten Sitzungen, wenn transparente Aktivitäten vorhanden sind. Expo SDK v3.2.0 fügt die Option `forwardUniversalLinks` hinzu (Standard: false), um die native Swift SDK-Handhabung von universellen Links zu konfigurieren.

#### Grundlegende SDK-Updates

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - `BrazeConfig.Builder.setIsLocationCollectionEnabled()` wurde in `setIsAutomaticLocationCollectionEnabled()` umbenannt.
    - `BrazeConfig.isLocationCollectionEnabled` wurde in `isAutomaticLocationCollectionEnabled` umbenannt.
    - `BrazeConfigurationProvider.isLocationCollectionEnabled` wurde in `isAutomaticLocationCollectionEnabled` umbenannt.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details 8. Januar 2026 %}
## Veröffentlichung am 8. Januar 2026 {#january-8-2026-release}

### Daten und Berichterstattung

#### Updates zu Currents-Events {#updates-to-currents-events}

{% multi_lang_include release_type.md release="General availability" %}

Die folgenden Änderungen wurden an Currents in Version 4 vorgenommen:

* Feldänderungen zum Event-Typ `users.behaviors.pushnotification.TokenStateChange`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Events
* Feldänderungen zum Event-Typ `users.messages.pushnotification.Bounce`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Events
* Feldänderungen zum Event-Typ `users.messages.pushnotification.Send`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Events
* Feldänderungen zum Event-Typ `users.messages.rcs.Click`:
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die dieser/diese Nutzer:in erhalten hat
    * Das Feld `user_phone_number` ist jetzt *optional*.
* Feldänderungen zum Event-Typ `users.messages.rcs.InboundReceive`:
    * Das Feld `user_id` ist jetzt *optional*.
* Feldänderungen zum Event-Typ `users.messages.rcs.Rejection`:
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Nutzer erhalten hat

Im [Currents Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/) finden Sie die Event-Änderungen für jede Version.

#### Synchronisationsprotokolle nach allen Zeilen exportieren {#export-sync-logs-by-all-rows}

{% multi_lang_include release_type.md release="Early access" %}

Im [Dashboard Cloud-Datenaufnahme **Sync Log**]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs) können Sie wählen, ob Sie die Protokolle auf Zeilenebene für einen Synchronisierungslauf exportieren möchten:

* **Zeilen mit Fehlern:** Lädt eine Datei herunter, die nur die Zeilen enthält, die einen **Error**-Status hatten.
* **Alle Zeilen:** Lädt eine Datei herunter, die alle in diesem Lauf verarbeiteten Zeilen enthält.

### Kanäle und Touchpoints

#### Bring Your Own (BYO) WhatsApp-Konnektor {#bring-your-own-byo-whatsapp-connector}

Der [Bring Your Own (BYO) WhatsApp-Konnektor]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector/) bietet eine Partnerschaft zwischen Braze und Infobip, bei der Sie Braze Zugriff auf Ihren Infobip WhatsApp Business Manager (WABA) geben. Dies ermöglicht es Ihnen, die Messaging-Kosten direkt mit Infobip zu verwalten und zu bezahlen, während Sie Braze für Segmentierung, Personalisierung und Kampagnenorchestrierung nutzen.

#### Banner in Canvas

{% multi_lang_include release_type.md release="Early access" %}

Wählen Sie **Banner** als Messaging-Kanal in einem [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) für Canvas. Verwenden Sie den Drag-and-Drop-Editor, um personalisierte Inline-Nachrichten zu erstellen, die nicht aufdringliche, kontextuell relevante Erlebnisse bieten, die zu Beginn jeder Nutzer:innen-Sitzung automatisch aktualisiert werden.

#### Dynamische BCC {#dynamic-bcc}

{% multi_lang_include release_type.md release="General availability" %}

Mit [dynamischem BCC]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc) können Sie Liquid in Ihrer BCC-Adresse verwenden. Beachten Sie, dass dieses Feature nur in den **E-Mail-Präferenzen** verfügbar ist und nicht in der Kampagne selbst eingestellt werden kann. Pro E-Mail-Empfänger:in ist nur eine BCC-Adresse zulässig.

#### Kanalbasierte Rate-Limits {#channel-based-rate-limits}

Als Alternative zu einem Rate-Limit, das für die gesamte Multichannel-Kampagne oder das Canvas gilt, können Sie ein bestimmtes Rate-Limit pro Kanal auswählen. In diesem Fall gilt das Rate-Limit für jeden Ihrer ausgewählten Kanäle. Sie können Ihre Kampagne oder Ihr Canvas beispielsweise so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die Kampagne oder das Canvas gesendet werden. Weitere Details finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Partnerschaften

#### LILT – Lokalisierung {#lilt-localization}

[LILT]({{site.baseurl}}/partners/lilt/) ist die komplette KI-Lösung für die Übersetzung und Inhaltserstellung in Unternehmen. Mit KI-Agenten und vollautomatisierten Workflows ermöglicht LILT globalen Unternehmen die Skalierung und Optimierung ihres Inhalts-, Produkt-, Kommunikations- und Supportbetriebs.

### Grundlegende SDK-Updates

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Entfernt News Feed.
        - Dadurch werden alle UI-Elemente, Datenmodelle und Aktionen, die mit News Feed verbunden sind, vollständig entfernt.
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 9. Dezember 2025 %}

## 9. Dezember 2025 {#december-9-2025}

### Daten und Berichterstattung

#### Google Tag Manager zu einer Landing-Page hinzufügen {#adding-google-tag-manager-to-a-landing-page}

Um Google Tag Manager zu Ihren Landing-Pages hinzuzufügen, fügen Sie Ihrer Landing-Page im Drag-and-Drop-Editor einen Custom-Code-Block hinzu und [fügen Sie dann den Tag-Manager-Code]({{site.baseurl}}/user_guide/messaging/landing_pages/#adding-google-tag-manager-to-a-landing-page) in den Block ein.

### Orchestrierung

#### SMS-Liquid-Anwendungsfall {#sms-liquid-use-case}

Der Anwendungsfall [Reagieren Sie mit verschiedenen Nachrichten basierend auf eingehenden SMS-Schlüsselwörtern]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/#sms-keyword-response) beinhaltet eine dynamische SMS-Schlüsselwortverarbeitung, um auf bestimmte eingehende Nachrichten mit unterschiedlichen Nachrichtentexten zu reagieren. Sie können beispielsweise unterschiedliche Antworten senden, wenn jemand „START“ oder „JOIN“ schreibt.

#### Allowlisting für Connected Content {#allowlisting-for-connected-content}

Sie können bestimmte URLs für die Verwendung mit [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) auf eine Allowlist setzen. Um auf dieses Feature zuzugreifen, wenden Sie sich an Ihren Customer-Success-Manager.

### Kanäle und Touchpoints

#### SMS-Zeichenkodierung {#sms-character-encoding}

Unser [SMS-Segmentrechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator) verfügt jetzt über eine Zeichenkodierung! Wählen Sie **Display Character Encoding**, um zu identifizieren, welche Zeichen als GSM-7 oder UCS-2 kodiert sind.

![SMS-Segmentrechner mit einer in das Textfeld eingegebenen Beispiel-SMS-Nachricht und eingeschalteter Zeichenkodierung.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### WhatsApp-Nachrichten mit Optimierung {#whatsapp-messages-with-optimization}

Da die MM API für WhatsApp keine 100%ige Zustellbarkeit bietet, ist es wichtig zu verstehen, wie Sie Nutzer:innen, die Ihre Nachricht möglicherweise nicht erhalten haben, auf anderen Kanälen retargeten können.

Für das Retargeting von Nutzer:innen empfehlen wir die Erstellung eines Segments von Nutzer:innen, die eine bestimmte Nachricht nicht erhalten haben. Filtern Sie dazu nach dem Fehlercode `131049`, der anzeigt, dass eine Marketing-Template-Nachricht aufgrund der WhatsApp-Durchsetzung des Marketing-Template-Limits pro Nutzer:in nicht gesendet wurde. Sie können dies mit [Braze-Currents oder SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/#retargeting-users-on-other-braze-channels) tun.

### Partnerschaften

#### OtherLevels – Dynamische Inhalte {#otherlevels-dynamic-content}

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) ist eine Erlebnisplattform, die generative KI einsetzt, um die Art und Weise zu verändern, wie Sportmarken, Verlage und Betreiber mit ihren Kunden in Kontakt treten, indem sie herkömmliche Inhalte in markengerechte, personalisierte Video- und Rich-Media-Erlebnisse im großen Maßstab umwandelt.

### SDK

#### Grundlegende SDK-Updates

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 11. November 2025 %}

## 11. November 2025 {#november-11-2025}

### Flexibilität der Daten {#data-flexibility}

#### Segmentierungsfilter `Live Activities Push to Start Registered for App` {#live-activities-push-to-start-registered-for-app-segmentation-filter}

Der Filter `Live Activities Push to Start Registered for App` segmentiert Ihre Nutzer:innen danach, ob sie für den Start einer Live-Aktivität über iOS-Push-Benachrichtigungen für eine bestimmte App registriert sind.

#### RFM-SQL-Segmenterweiterung {#rfm-sql-segment-extension}

Sie können eine [RFM-Segmenterweiterung (Recency, Frequency, Monetary)]({{site.baseurl}}/rfm_segments/) erstellen, um Ihre besten Nutzer:innen durch Messung ihrer Kaufgewohnheiten zu targetieren.

Die RFM-Analyse ist eine Marketing-Technik, die Ihre besten Nutzer:innen identifiziert, indem sie Nutzer:innen auf einer Skala von 0–3 für jede Kategorie (Recency, Frequency, Monetary) bewertet, wobei 3 der beste Wert und 0 der schlechteste ist. Recency-, Frequency- und Monetary-Werte basieren alle auf Daten aus einem von Ihnen gewählten Zeitraum.

#### Angepasste Attribute – Werte {#custom-attributes-values}

Wählen Sie beim Anzeigen eines Nutzungsberichts den [Tab **Werte**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) aus, um die Spitzenwerte der ausgewählten angepassten Attribute basierend auf einer Stichprobe von ca. 250.000 Nutzer:innen zu sehen.

#### Sync-Protokolle und Beobachtbarkeit für die Cloud-Datenaufnahme {#sync-logs-and-observability-for-cloud-data-ingestion}

{% multi_lang_include release_type.md release="General availability" %}

Mit dem [Sync-Log-Dashboard]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) der Cloud-Datenaufnahme (CDI) können Sie alle von CDI verarbeiteten Daten überwachen, überprüfen, ob die Daten erfolgreich synchronisiert wurden, und eventuelle Probleme mit „falschen“ oder fehlenden Daten diagnostizieren.

#### Multi-Regel-Feature-Flag-Rollouts {#multi-rule-feature-flag-rollouts}

Verwenden Sie [Multi-Regel-Feature-Flag-Rollouts]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts), um eine Abfolge von Regeln für die Bewertung von Nutzer:innen zu definieren, was eine präzise Segmentierung und kontrollierte Feature-Freigaben ermöglicht. Diese Methode ist ideal für die Bereitstellung desselben Features für verschiedene Zielgruppen.

#### Zuordnung zu Katalogfeldern für Drag-and-Drop-Produktblöcke {#mapping-to-catalog-fields-for-drag-and-drop-product-blocks}

In Ihren Katalogeinstellungen können Sie den Schalter **Produktblöcke** auswählen, um [bestimmte Felder]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/#catalog-setup) und Informationen in Ihrem Katalog zuzuordnen. Hier können Sie auswählen, welche Felder als Produkttitel, Produkt-URL und Bild-URL verwendet werden sollen.

#### Frequency-Capping-Abbruch-Events in Currents {#frequency-capping-abort-events-in-currents}

Bei der Verwendung von Currents können Sie jetzt `abort_type` in den Kanalabbruch-Events referenzieren. Dies identifiziert, dass eine Nachricht aufgrund von Frequency-Capping abgebrochen wurde, und gibt an, welche Frequency-Capping-Regel den Abbruch verursacht hat. Dies hilft Ihnen bei der Festlegung Ihrer Frequency-Capping-Regeln. Weitere Informationen zu Currents-Events finden Sie unter [Engagement-Events bei Nachrichten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

### Robuste Kanäle {#robust-channels}

#### Hintergrundbilder für Zeilen {#background-row-images}

{% multi_lang_include release_type.md release="General availability" %}

Im Panel **Zeileneigenschaften** können Sie einer In-App-Nachricht oder Landing-Page [ein Hintergrundbild für die Zeile hinzufügen]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#background-image). Schalten Sie **Hintergrundbild** ein und geben Sie eine Bild-URL an oder wählen Sie ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Konfigurieren Sie schließlich Ihren Alt-Text, die Größe, die Position und ob das Bild wiederholt werden soll, um Muster in der Zeile zu erzeugen.

![Ein Zeilenhintergrundbild einer Pizza mit einem horizontalen Wiederholungsmuster.]({% image_buster /assets/img_archive/background_row.png %})

#### Vorschau-Link kopieren {#copy-preview-link}

Verwenden Sie **Vorschau-Link kopieren** in Ihren [Bannern]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-5-test-your-message-optional), [angepassten E-Mail-Fußzeilen]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/#creating-your-custom-footer) und [E-Mail-Opt-in- und Abmeldeseiten]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=custom%20footer#subscription-pages-and-footers), um einen teilbaren Link zu generieren, der zeigt, wie Ihre Inhalte für eine:n zufällige:n Nutzer:in aussehen werden.

#### WhatsApp-Nachrichten mit optimierter Zustellung {#whatsapp-messages-with-optimized-delivery}

Nutzen Sie die fortschrittlichen KI-Systeme von Meta, um Ihre Marketing-Nachrichten mehr Nutzer:innen zuzustellen, die sich am ehesten damit beschäftigen, und so die Zustellbarkeit und das Nachrichten-Engagement deutlich zu steigern.

[WhatsApp-Nachrichten mit optimierter Zustellung]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/) werden über die neue [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) von Meta versendet, die im Vergleich zur herkömmlichen Cloud API eine bessere Performance bietet. Mit dieser neuen Sendepipeline können Sie Nutzer:innen besser erreichen, die Ihre Nachrichten wertschätzen und empfangen möchten.

#### WhatsApp Flows

Wenn Sie eine WhatsApp-Flow-Nachricht in ein Braze-Canvas oder eine Kampagne einbinden, möchten Sie möglicherweise bestimmte Informationen, die Nutzer:innen über den Flow übermitteln, erfassen und nutzen. Braze benötigt zusätzliche Informationen über die Struktur der Nutzer:innen-Antwort, insbesondere die erwartete Form der JSON-Antwort, um das erforderliche Schema für verschachtelte angepasste Attribute (NCA) zu erstellen.

Jetzt können Sie Braze die Informationen über die Antwortstruktur geben, indem Sie [die Flow-Antwort als angepasstes Attribut speichern]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) und einen Testversand durchführen.

#### Bearbeitbare Nutzer:innen-Vorschau {#editable-user-preview}

Sie können [einzelne Felder eines zufälligen oder bestehenden Nutzers bearbeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook#customizing-an-existing-user), um dynamische Inhalte in Ihrer Nachricht zu testen. Wählen Sie **Bearbeiten**, um den ausgewählten Nutzer bzw. die Nutzerin in einen angepassten Nutzer umzuwandeln, den Sie ändern können.

![Der Tab „Vorschau als Nutzer:in“ mit einem Button „Bearbeiten“.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### KI und ML-Automatisierung {#ai-and-ml-automation}

#### BrazeAI Decisioning Studio™ Go

Sie können nun Ihre Integration mit [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/) einrichten, indem Sie sich auf diese Konfigurationsartikel beziehen für:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)

#### Neue Features für Braze-Agenten {#new-features-for-braze-agents}

{% multi_lang_include release_type.md release="Beta" %}

Sie können Ihren [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) jetzt anpassen, indem Sie:

- [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) anwenden, an die sich Ihr Agent bei seiner Antwort halten muss.
- Auf einen Katalog verweisen, um Ihre Nachricht weiter zu personalisieren.
- Die Ausgabe eines Agenten durch Angabe des [Ausgabeformats]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format) strukturieren.
- Die [Temperatur]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) für den Grad der Abweichung der Agentenausgabe justieren.

### ChatGPT-Modelle mit BrazeAI Operator<sup>TM</sup> {#chatgpt-models-with-brazeai-operatortm}

{% multi_lang_include release_type.md release="Beta" %}

Sie können aus diesen GPT-Modellen auswählen, um sie für verschiedene Anforderungstypen mit [Operator]({{site.baseurl}}/user_guide/brazeai/operator/) zu verwenden:

- GPT-5 nano
- GPT-5 mini (Standard)
- GPT-5

### Neue Braze-Partnerschaften {#new-braze-partnerships}

#### StackAdapt – Werbung {#stackadapt-advertising}

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) ist eine KI-gestützte Marketing-Plattform, die zielgerichtete, Performance-gesteuerte Werbung zustellt. Sie ermöglicht es Ihnen, Nutzerprofildaten aus Braze mit dem StackAdapt Data Hub zu synchronisieren. Durch die Verbindung der beiden Plattformen können Sie eine einheitliche Sicht auf Ihre Kund:innen schaffen und First-Party-Daten aktivieren, um die Anzeigen-Performance zu verbessern.

#### Cloudinary – Dynamische Inhalte {#cloudinary-dynamic-content}

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) ist eine Bild- und Videoplattform, mit der Sie Bilder und Videos in großem Umfang für jede Kampagne über alle Kanäle und Customer Journeys hinweg verwalten, bearbeiten, optimieren und zustellen können. Nach der Integration und dem Enablement wird das Medienmanagement von Cloudinary die dynamische, kontextuelle und personalisierte Zustellung von Assets für Ihre Braze-Kampagnen und -Canvases ermöglichen.

#### Kameleoon – A/B-Tests {#kameleoon-ab-testing}

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) ist eine Optimierungslösung mit experimentellen, KI-gestützten Personalisierungs- und Feature-Management-Funktionen in einer einzigen, einheitlichen Plattform.

### SDK-Updates

Die folgenden SDK-Updates wurden veröffentlicht. Grundlegende Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Korrigiert den Typescript-Typ für den Callback von `subscribeToInAppMessage` und `addListener` für `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Diese Listener geben jetzt korrekt einen Callback mit dem neuen Typ `InAppMessageEvent` zurück. Zuvor wurden die Methoden so annotiert, dass sie einen Typ `BrazeInAppMessage` zurückgeben, aber tatsächlich wurde ein `String` zurückgegeben.
         - Wenn Sie eine der beiden Abo-APIs verwenden, stellen Sie sicher, dass das Verhalten Ihrer In-App-Nachrichten nach dem Update auf diese Version unverändert bleibt. Sehen Sie sich unseren Beispielcode in `BrazeProject.tsx` an.
    - Die APIs `logInAppMessageClicked`, `logInAppMessageImpression` und `logInAppMessageButtonClicked` akzeptieren jetzt nur noch ein `BrazeInAppMessage`-Objekt, um der bestehenden öffentlichen Schnittstelle zu entsprechen.
        - Zuvor akzeptierte es sowohl ein `BrazeInAppMessage`-Objekt als auch einen `String`.
    - `BrazeInAppMessage.toString()` gibt jetzt einen menschenlesbaren String anstelle der JSON-String-Darstellung zurück.
        - Um die JSON-String-Darstellung einer In-App-Nachricht zu erhalten, verwenden Sie `BrazeInAppMessage.inAppMessageJsonString`.
    - Unter iOS wurde `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` nach `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]` verschoben.
        - Diese neue Methode ist jetzt eine Klassenmethode anstelle einer Instanzmethode.
    - Fügt Nullbarkeits-Annotationen zu `BrazeReactUtils`-Methoden hinzu.
    - Entfernt die folgenden veralteten Methoden und Eigenschaften aus der API:
        - `getInstallTrackingId(callback:)` zugunsten von `getDeviceId`.
        - `registerAndroidPushToken(token:)` zugunsten von `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` zugunsten von `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` zugunsten von `payload_type`.
        - `PushNotificationEvent.deeplink` zugunsten von `url`.
        - `PushNotificationEvent.content_text` zugunsten von `body`.
        - `PushNotificationEvent.raw_android_push_data` zugunsten von `android`.
        - `PushNotificationEvent.kvp_data` zugunsten von `braze_properties`.
    - Update der nativen Android SDK-Versionsbindungen [von Braze Android SDK 39.0.0 auf 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [.NET MAUI (Xamarin) SDK Version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Update der iOS-Bindung [von Braze Swift SDK 12.1.0 auf 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Dazu gehört auch die Unterstützung von Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Update der nativen Android-Bridge [von Braze Android SDK 39.0.0 auf 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}