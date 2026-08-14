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
Die Shopify-Segmentsynchronisierung befindet sich derzeit in der Beta-Phase. Um Zugang zu erhalten, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Braze-Shopify-Integration | Die Braze-Shopify-App muss in Ihrem Shopify-Shop installiert und mit einem Braze-Workspace verbunden sein. Eine Einrichtungsanleitung finden Sie unter [Shopify-Standardintegration einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) oder [Benutzerdefinierte Shopify-Integration einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). |
| Shopify-Nutzerberechtigung | Die Shopify-Nutzer:innen, die die Segment-Synchronisierung initiieren, müssen über die Berechtigung **Export** verfügen, um Nutzerdaten zu exportieren. Weitere Informationen zu Shopify-Berechtigungen finden Sie in der [Shopify-Dokumentation zu Shop-Berechtigungen](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## So funktioniert es {#how-it-works}

Die Shopify-Segmentsynchronisierung arbeitet in zwei Phasen.

1. **Initiales Backfill:** Wenn Sie ein Segment zum ersten Mal synchronisieren, füllt Braze alle aktuellen Mitglieder nach und erstellt eine entsprechende Kohorte in Braze. Das Backfill läuft asynchron und kann einige Augenblicke dauern.
2. **Laufende Synchronisierung:** Nach dem initialen Backfill abonniert Braze auch Shopify-Webhooks, damit die Mitgliedschaft nahezu in Realtime synchron bleibt.

| Webhook-Thema | Auswirkung in Braze |
| --- | --- |
| `customer.joined_segment` | Die Nutzer:in wird der entsprechenden Braze-Kohorte hinzugefügt. |
| `customer.left_segment` | Die Nutzer:in wird aus der entsprechenden Braze-Kohorte entfernt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook-Thema" }

Wenn eine Synchronisierung fehlschlägt, zeigt das Modal der Aktionserweiterung ein Fehlerbanner an, das erklärt, was passiert ist und wie Sie vorgehen können. Einige Fehler bieten eine Aktion **Synchronisierung wiederholen** an. Andere erfordern eine Änderung durch eine:n Administrator:in oder an der Konfiguration.

## Datenimport-Integration {#data-import-integration}

### Schritt 1: Ein Shopify-Segment zum Synchronisieren auswählen {#step-1-select-a-shopify-segment-to-sync}

Gehen Sie in Shopify zu **Customers** > **Segments** und wählen Sie das Segment aus, das Sie mit Braze synchronisieren möchten. Sie können jedes Segment synchronisieren, das mit der nativen Segmentierung von Shopify erstellt wurde, einschließlich Segmente basierend auf Bestellverlauf, Produktkäufen, Kund:innen-Tags, Lifetime-Ausgaben und Metafeldern.

![Segments-Panel mit einer Liste von Shopify-Segmenten.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Schritt 2: Die Synchronisierung starten {#step-2-initiate-the-sync}

1. Öffnen Sie auf der Segment-Detailseite in Shopify das Dropdown **Use segment** und wählen Sie **Braze Segment Sync** aus.

![Segment-Detailseite mit einem „Use segment“-Dropdown, das die Option „Braze Segment Sync“ enthält.]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Das Braze-Action-Extension-Modal öffnet sich und zeigt den Segmentnamen und die Zielgruppengröße an. Wählen Sie **Sync with Braze** aus, um den Import zu starten.

![Modal mit einem Button zum Synchronisieren mit Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. Das Modal wechselt in den Synchronisierungsstatus und zeigt ein Fortschrittsbanner an, während Braze die Mitglieder importiert.

![Modal, das die laufende Synchronisierung anzeigt.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. Wählen Sie **Close** aus. Die Synchronisierung wird im Hintergrund fortgesetzt. Das Schließen des Modals stoppt sie nicht.

Um zu prüfen, ob die Synchronisierung abgeschlossen ist, schließen Sie das Modal und öffnen Sie es erneut. Wenn die Synchronisierung abgeschlossen ist, wird das Modal mit einem Erfolgsbanner geöffnet.

![Modal, das bestätigt, dass die Synchronisierung aktiv ist.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Schritt 3: Ein Braze-Segment mit dem Kohorten-Mitgliedschaftsfilter erstellen {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Gehen Sie in Braze zu **Audience** > **Segments** und erstellen Sie ein neues Segment. Wählen Sie unter **Add Filter** den Filter **Cohort Membership** aus und wählen Sie Ihr synchronisiertes Shopify-Segment aus dem Dropdown. Nach dem Speichern können Sie dieses Braze-Segment beim Targeting von Nutzer:innen in einer Campaign oder einem Canvas referenzieren.

![Segment-Builder mit dem Filter „Shopify Cohorts“.]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Erneutes Synchronisieren eines Segments {#re-syncing-a-segment}

Nachdem ein Segment synchronisiert wurde, können Sie die Kohorten-Mitgliedschaft jederzeit über dieselbe Aktionserweiterung aktualisieren.

1. Öffnen Sie in Shopify das synchronisierte Segment und wählen Sie **Use segment** > **Braze Segment Sync**.
2. Wählen Sie im Modal **Sync now** aus.
3. Wählen Sie im Bestätigungsdialog **Sync now** aus, um die erneute Synchronisierung zu starten.

Die erneute Synchronisierung ist additiv: Nutzer:innen, die dem aktuellen Shopify-Segment entsprechen, werden der Kohorte hinzugefügt, aber Nutzer:innen, die nicht mehr übereinstimmen, verbleiben in der Kohorte.

## Segment-Aktualisierungen in Shopify {#segment-updates-in-shopify}

### Ein Segment umbenennen {#renaming-a-segment}

Wenn Sie ein Shopify-Segment umbenennen, aktualisiert Braze den Anzeigenamen der entsprechenden Kohorte automatisch. Eine erneute Synchronisierung ist nicht erforderlich.

### Segment-Kriterien ändern {#changing-segment-criteria}

Änderungen an den Kriterien eines Shopify-Segments werden nicht automatisch übernommen. Um Nutzer:innen zu erfassen, die neu den Kriterien entsprechen, synchronisieren Sie das Segment über die Action Extension erneut. Nutzer:innen, die den Kriterien nicht mehr entsprechen, verbleiben in der Kohorte, da eine erneute Synchronisierung keine Mitglieder entfernt. Weitere Informationen finden Sie unter [Ein Segment erneut synchronisieren](#re-syncing-a-segment).

## Nutzer:innen-Zuordnung {#user-matching}

Nutzer:innen, die aus Shopify-Segmenten synchronisiert werden, werden anhand des `shopify_customer_id`-Alias mit Braze-Nutzerprofilen abgeglichen. Dieser Alias wird im Rahmen der Braze-Shopify-Integration gesetzt. Nutzer:innen ohne ein übereinstimmendes Braze-Nutzerprofil werden bei der Synchronisierung übersprungen.

Weitere Informationen dazu, wie die Shopify-Integration Nutzer:innen identifiziert und Aliase zuweist, finden Sie unter [Shopify-Daten-Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

Braze gleicht synchronisierte Nutzer:innen mit bestehenden Braze-Nutzerprofilen ab – unabhängig davon, wie diese Profile erstellt wurden, einschließlich durch den historischen Shopify-Backfill, Ihre eigene Datenplattform (wie Snowflake oder ein anderes Data Warehouse) oder direkte API-Importe. Wenn Ihre Kohorte kleiner ist als Ihr Shopify-Segment, bedeutet dies, dass einige Segment-Mitglieder noch kein übereinstimmendes Braze-Profil haben. Um die Zuordnungsabdeckung zu erhöhen, befüllen Sie Braze-Nutzerprofile über Ihre bevorzugte Methode, bevor Sie die Synchronisierung starten.

## Einschränkungen {#limitations}

- **Einweg-Synchronisierung.** Die Segment-Zugehörigkeit fließt nur von Shopify zu Braze. Änderungen an der Kohorten-Zugehörigkeit, die direkt in Braze vorgenommen werden, werden nicht an Shopify zurückübertragen.
- **Keine Profilerstellung.** Nur Shopify-Kund:innen, die bereits ein Braze-Nutzerprofil haben, werden der Kohorte hinzugefügt.
- **Synchronisierungen können nicht rückgängig gemacht werden.** Wenn ein Shopify-Segment synchronisiert wurde, kann dies nicht rückgängig gemacht werden.
- **Erneute Synchronisierung fügt nur Mitglieder hinzu.** Bei einer erneuten Synchronisierung eines Segments werden neu übereinstimmende Nutzer:innen zur Kohorte hinzugefügt, aber Nutzer:innen, die nicht mehr im Shopify-Segment enthalten sind, werden nicht entfernt.