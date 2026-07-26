---
nav_title: Shopify-Segmentsynchronisierung
article_title: Shopify-Segmentsynchronisierung
alias: /shopify_segments_sync/
page_order: 8
description: "Dieser Referenzartikel erklärt, wie Sie Shopify-Segmente als Kohorten in Braze synchronisieren, um Zielgruppen einheitlich zu verwalten und gezielt anzusprechen."
---

# Shopify-Segmentsynchronisierung {#shopify-segments-sync}

> Die Shopify-Segmentsynchronisierung erweitert Ihren Shopify-Shop in Braze und gibt Ihrem Marketing-Team direkten Zugang zu umfangreicheren Nutzerdaten, die in Shopify vorliegen – einschließlich Signalen, die von der Standard-Braze-Shopify-Integration nicht erfasst werden. Durch die Synchronisierung von Shopify-Segmenten als Kohorten stimmen Sie Zielgruppendefinitionen plattformübergreifend ab und bieten konsistente, koordinierte Nutzererlebnisse – unabhängig davon, ob Nutzer:innen in Shopify angesprochen oder über eine Braze-Campaign erreicht werden.

{% alert important %}
Die Shopify-Segmentsynchronisierung befindet sich derzeit in der Beta-Phase. Um Zugang zu erhalten, wenden Sie sich an Ihren geschäftskunden-Success-Manager.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Braze-Shopify-Integration | Die Braze-Shopify-App muss in Ihrem Shopify-Shop installiert und mit einem Braze-Workspace verbunden sein. Eine Einrichtungsanleitung finden Sie unter [Shopify-Standardintegration einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) oder [Benutzerdefinierte Shopify-Integration einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/). |
| Shopify-Nutzerberechtigung | Die Shopify-Nutzer:in, die die Segmentsynchronisierung initiiert, muss über die Berechtigung **Exportieren** verfügen, um Kundendaten zu exportieren. Weitere Informationen zu Shopify-Berechtigungen finden Sie in der [Shopify-Dokumentation zu Shop-Berechtigungen](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Funktionsweise {#how-it-works}

Die Shopify-Segmentsynchronisierung funktioniert in zwei Phasen.

1. Wenn Sie ein Segment zum ersten Mal synchronisieren, füllt Braze alle aktuellen Mitglieder nach und erstellt eine entsprechende Kohorte in Braze. Das Backfill läuft asynchron und kann einige Augenblicke dauern.
2. Während der initialen Synchronisierung füllt Braze die aktuellen Mitglieder nach und abonniert Shopify-Webhooks, damit die Mitgliedschaft nahezu in Echtzeit synchron bleibt.

| Webhook-Thema | Auswirkung in Braze |
| --- | --- |
| `customer.joined_segment` | Die Nutzer:in wird der entsprechenden Braze-Kohorte hinzugefügt. |
| `customer.left_segment` | Die Nutzer:in wird aus der entsprechenden Braze-Kohorte entfernt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook-Thema" }

Falls eine Synchronisierung fehlschlägt, zeigt das Aktionserweiterungs-Modal ein Fehlerbanner mit einer empfohlenen Aktion an. Wählen Sie **Sync with Braze**, um es erneut zu versuchen.

## Datenimport-Integration {#data-import-integration}

### 1. Schritt: Ein Shopify-Segment zur Synchronisierung auswählen {#step-1-select-a-shopify-segment-to-sync}

Gehen Sie in Shopify zu **Customers** > **Segments** und wählen Sie das Segment aus, das Sie mit Braze synchronisieren möchten. Sie können jedes Segment synchronisieren, das mit der nativen Shopify-Segmentierung erstellt wurde, einschließlich Segmenten basierend auf Bestellverlauf, Produktkäufen, Kund:innen-Tags, Lifetime-Ausgaben und Metafeldern.

![Segment-Panel mit einer Liste von Shopify-Segmenten.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### 2. Schritt: Die Synchronisierung starten {#step-2-initiate-the-sync}

1. Öffnen Sie auf der Shopify-Segmentdetailseite das Dropdown **Use segment** und wählen Sie **Braze Segment Sync**.

![Segmentdetailseite mit einem „Use segment“-Dropdown, das die Option „Braze Segment Sync“ enthält.]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Im sich öffnenden Braze-Aktionserweiterungs-Modal werden der Segmentname und die Zielgruppengröße angezeigt. Wählen Sie **Sync with Braze**, um den Import zu starten.

![Modal mit einem Button zur Synchronisierung mit Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. Wählen Sie **Done**.

![Modal, das bestätigt, dass die Synchronisierung aktiv ist.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### 3. Schritt: Ein Braze-Segment mit dem Kohortenmitgliedschafts-Filter erstellen {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Gehen Sie in Braze zu **Audience** > **Segments** und erstellen Sie ein neues Segment. Wählen Sie unter **Add Filter** den Filter **Cohort Membership** und wählen Sie Ihr synchronisiertes Shopify-Segment aus dem Dropdown. Nach dem Speichern können Sie dieses Braze-Segment beim Targeting von Nutzer:innen in einer Campaign oder einem Canvas referenzieren.

![Segment-Builder mit dem Filter „Shopify Cohorts“.]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Nutzer:innen-Zuordnung {#user-matching}

Nutzer:innen, die aus Shopify-Segmenten synchronisiert werden, werden anhand des `shopify_customer_id`-Alias, der im Rahmen der Braze-Shopify-Integration gesetzt wird, mit Braze-Nutzerprofilen abgeglichen. Nutzer:innen ohne ein passendes Braze-Nutzerprofil werden bei der Synchronisierung übersprungen.

Einzelheiten dazu, wie die Shopify-Integration Nutzer:innen identifiziert und Aliase zuweist, finden Sie unter [Shopify-Daten-Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

## Einschränkungen {#limitations}

- **Einweg-Synchronisierung.** Die Segmentmitgliedschaft fließt nur von Shopify zu Braze. Änderungen an der Kohortenmitgliedschaft, die direkt in Braze vorgenommen werden, werden nicht an Shopify zurückgespielt.
- **Keine Profilerstellung.** Nur Shopify-Kund:innen, die bereits ein Braze-Nutzerprofil haben, werden der Kohorte hinzugefügt.
- **Synchronisierungen können nicht rückgängig gemacht werden.** Sobald ein Shopify-Segment synchronisiert wurde, kann dies nicht rückgängig gemacht werden.