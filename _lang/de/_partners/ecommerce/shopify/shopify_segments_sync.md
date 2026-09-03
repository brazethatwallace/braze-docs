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
| Braze-Shopify-Integration | Die Braze-Shopify-App muss in Ihrem Shopify-Shop installiert und mit einem Braze-Workspace verbunden sein. Anweisungen zur Einrichtung finden Sie unter [Shopify-Standardintegration einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) oder [Benutzerdefinierte Shopify-Integration einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). |
| Shopify-Nutzerberechtigung | Die Shopify-Nutzer:innen, die die Segment-Synchronisierung initiieren, müssen über die Berechtigung **Export** verfügen, um Nutzerdaten zu exportieren. Weitere Informationen zu Shopify-Berechtigungen finden Sie in der [Shopify-Dokumentation zu Shop-Berechtigungen](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## So funktioniert es {#how-it-works}

Die Shopify-Segment-Synchronisation arbeitet in zwei Phasen.

1. **Erstmaliges Backfill:** Wenn Sie ein Segment zum ersten Mal synchronisieren, führt Braze ein Backfill aller aktuellen Mitglieder durch und erstellt eine entsprechende Kohorte in Braze. Das Backfill läuft asynchron und kann einige Augenblicke dauern.
2. **Laufende Synchronisation:** Nach dem erstmaligen Backfill abonniert Braze auch Shopify-Webhooks, damit die Mitgliedschaft nahezu in Echtzeit synchron bleibt.

| Webhook-Thema | Auswirkung in Braze |
| --- | --- |
| `customer.joined_segment` | Die Nutzer:in wird der entsprechenden Braze-Kohorte hinzugefügt. |
| `customer.left_segment` | Die Nutzer:in wird aus der entsprechenden Braze-Kohorte entfernt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook-Thema" }

Wenn eine Synchronisation fehlschlägt, zeigt das Action-Extension-Modal ein Fehlerbanner an, das erklärt, was passiert ist und wie Sie vorgehen können. Bei einigen Fehlern wird die Aktion **Synchronisation wiederholen** angeboten. Bei anderen ist eine Änderung durch eine:n Administrator:in oder an der Konfiguration erforderlich.

## Datenimport-Integration {#data-import-integration}

### Schritt 1: Ein Shopify-Segment zum Synchronisieren auswählen {#step-1-select-a-shopify-segment-to-sync}

Gehen Sie in Shopify zu **Customers** > **Segments** und wählen Sie das Segment aus, das Sie mit Braze synchronisieren möchten. Sie können jedes Segment synchronisieren, das mit der nativen Segmentierung von Shopify erstellt wurde, einschließlich Segmente basierend auf Bestellverlauf, Produktkäufen, Kund:innen-Tags, Lifetime-Ausgaben und Metafeldern.

![Panel „Segments“ mit einer Liste von Shopify-Segmenten.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Schritt 2: Die Synchronisierung starten {#step-2-initiate-the-sync}

1. Öffnen Sie auf der Segment-Detailseite von Shopify das Dropdown **Use segment** und wählen Sie **Braze Segment Sync** aus.

![Segment-Detailseite mit einem „Use segment“-Dropdown, das die Option „Braze Segment Sync“ enthält.]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Das Braze-Aktionserweiterungs-Modal öffnet sich und zeigt den Segmentnamen sowie die Zielgruppengröße an. Wählen Sie **Sync with Braze** aus, um den Import zu starten.

![Modal mit einem Button zur Synchronisierung mit Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. Das Modal wechselt in den Synchronisierungsstatus und zeigt ein Fortschrittsbanner an, während Braze die Mitglieder importiert.

![Modal, das die laufende Synchronisierung anzeigt.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. Wählen Sie **Close** aus. Die Synchronisierung läuft im Hintergrund weiter. Das Schließen des Modals stoppt sie nicht.

Um zu prüfen, ob die Synchronisierung abgeschlossen ist, schließen Sie das Modal und öffnen Sie es erneut. Wenn die Synchronisierung abgeschlossen ist, wird das Modal mit einem Erfolgsbanner geöffnet.

![Modal, das bestätigt, dass die Synchronisierung aktiv ist.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Schritt 3: Ein Braze-Segment mit dem Kohortenzugehörigkeitsfilter erstellen {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Gehen Sie in Braze zu **Audience** > **Segments** und erstellen Sie ein neues Segment. Wählen Sie unter **Add Filter** den Filter **Cohort Membership** aus und wählen Sie Ihr synchronisiertes Shopify-Segment aus dem Dropdown. Nach dem Speichern können Sie dieses Braze-Segment beim Targeting von Nutzer:innen in einer Campaign oder einem Canvas referenzieren.

![Segment-Builder mit dem Filter „Shopify Cohorts“.]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Erneutes Synchronisieren eines Segments {#re-syncing-a-segment}

Nachdem ein Segment synchronisiert wurde, können Sie die Kohorten-Mitgliedschaft jederzeit über dieselbe Aktionserweiterung aktualisieren.

1. Öffnen Sie in Shopify das synchronisierte Segment und wählen Sie **Use segment** > **Braze Segment Sync**.
2. Wählen Sie im Modal **Sync now** aus.
3. Wählen Sie im Bestätigungsdialog **Sync now**, um die erneute Synchronisierung zu starten.

Die erneute Synchronisierung ist additiv: Nutzer:innen, die dem aktuellen Shopify-Segment entsprechen, werden der Kohorte hinzugefügt, aber Nutzer:innen, die nicht mehr übereinstimmen, verbleiben in der Kohorte.

## Synchronisierte Segmente in Braze verwalten {#managing-synced-segments-in-braze}

Sie können jedes synchronisierte Segment über das Braze-Dashboard verwalten. Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner**, wählen Sie Ihre Shopify-Integration aus und öffnen Sie den Tab **Nutzer:innen verwalten**.

### Synchronisierungsstatus {#sync-status}

Jedes synchronisierte Segment hat einen Synchronisierungsstatus.

| Status | Beschreibung |
| --- | --- |
| **Syncing** | Braze importiert die Mitglieder des Segments. |
| **Queued** | Das Segment wartet auf einen freien Synchronisierungs-Slot. |
| **Active** | Das Segment ist synchronisiert und die Mitgliedschaft wird nahezu in Realtime aktualisiert. |
| **Paused** | Mitgliedschafts-Updates für dieses Segment sind pausiert. |
| **Error** | Der letzte Synchronisierungsversuch ist fehlgeschlagen. Wählen Sie **Retry sync** aus, um es erneut zu versuchen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Synchronisierungsstatus" }

### Segmente in großen Mengen synchronisieren {#syncing-segments-in-bulk}

Um zusätzliche Segmente zu synchronisieren, bearbeiten Sie die Integration, gehen Sie zum Schritt **Nutzer:innen verwalten** und wählen Sie **Edit segments** im Abschnitt **Sync segments** aus. Im Auswahl-Modal:

- Wählen Sie eine beliebige Anzahl von Segmenten aus. 25 Segmente werden gleichzeitig synchronisiert; die übrigen werden automatisch in die Warteschlange eingereiht.
- Segmente, die bereits synchronisiert werden, sind gesperrt. Um ein Segment zu entfernen, löschen Sie es in Shopify.

Speichern Sie Ihre Änderungen, um die Synchronisierungen zu starten.

### Ein einzelnes Segment pausieren {#pausing-a-single-segment}

Um die Synchronisierung für ein Segment zu pausieren, wählen Sie **Pause sync** in der entsprechenden Zeile der Segmenttabelle aus und bestätigen Sie. Wenn die Synchronisierung eines Segments pausiert ist:

- Die Kohorte und ihre Mitglieder bleiben in Braze und sind weiterhin für Targeting verfügbar. Campaigns und Canvases, die die Kohorte verwenden, senden weiterhin an die aktuellen Mitglieder der Kohorte.
- Mitgliedschafts-Updates werden gestoppt.
- Das Umbenennen des Segments in Shopify aktualisiert weiterhin den Anzeigenamen der Kohorte.
- Das Löschen des Segments in Shopify beendet weiterhin das Tracking.
- **Sync now**-Anfragen über die Shopify-Aktionserweiterung werden abgelehnt.

Um fortzufahren, wählen Sie **Resume sync** in der Zeile aus. Braze nimmt Mitgliedschafts-Updates wieder auf und führt eine Aufhol-Synchronisierung durch. Nutzer:innen, die das Shopify-Segment verlassen haben, während die Synchronisierung pausiert war, bleiben in der Braze-Kohorte.

### Alle Segmentsynchronisierungen pausieren {#pausing-all-segment-syncing}

Um die Synchronisierung für alle Segmente gleichzeitig zu pausieren, bearbeiten Sie die Integration, wählen Sie **Pause sync** im Abschnitt **Sync segments** des Schritts **Nutzer:innen verwalten** aus und speichern Sie Ihre Einstellungen. Während alle Segmentsynchronisierungen pausiert sind:

- Die Segmenttabelle zeigt nur Segmentnamen an, mit dem Status **Paused** neben der Überschrift.
- Aktionen auf Zeilenebene sind nicht verfügbar, bis Sie fortfahren.
- Braze aktualisiert keine Kohortennamen bei Shopify-Umbenennungen. Kohortennamen werden aktualisiert, wenn Sie fortfahren.
- **Sync now**-Anfragen über die Aktionserweiterung werden abgelehnt. Die Erweiterung zeigt weiterhin den zuletzt bekannten Status jedes Segments an, und das Auswählen von **Sync now** startet keine Synchronisierung.

Um fortzufahren, wählen Sie **Resume sync** im selben Abschnitt aus und speichern Sie. Braze synchronisiert automatisch jedes zuvor ausgewählte Segment mit einer Aufhol-Synchronisierung erneut. Sie müssen sie nicht erneut auswählen. Segmente, die Sie einzeln pausiert haben, bleiben pausiert, bis Sie sie über ihre Zeile in der Segmenttabelle wieder aufnehmen.

## Segment-Aktualisierungen in Shopify {#segment-updates-in-shopify}

### Umbenennung eines Segments {#renaming-a-segment}

Wenn Sie ein Shopify-Segment umbenennen, aktualisiert Braze den Anzeigenamen der entsprechenden Kohorte automatisch. Eine erneute Synchronisierung ist nicht erforderlich. Braze aktualisiert den Kohortennamen auch dann, wenn die Synchronisierung eines Segments einzeln pausiert ist. Wenn die gesamte Segment-Synchronisierung pausiert ist, aktualisiert Braze die Kohortennamen, sobald Sie die Synchronisierung fortsetzen.

### Änderung der Segment-Kriterien {#changing-segment-criteria}

Braze aktualisiert die Kohortenzugehörigkeit nicht automatisch, wenn Sie die Kriterien eines Shopify-Segments ändern. Um Nutzer:innen zu erfassen, die die Kriterien neu erfüllen, synchronisieren Sie das Segment über die Action Extension erneut. Nutzer:innen, die die Kriterien nicht mehr erfüllen, verbleiben in der Kohorte, da eine erneute Synchronisierung keine Mitglieder entfernt. Weitere Informationen finden Sie unter [Erneute Synchronisierung eines Segments](#re-syncing-a-segment).

## Nutzer:innen-Zuordnung {#user-matching}

Nutzer:innen, die aus Shopify-Segmenten synchronisiert werden, werden anhand des `shopify_customer_id`-Alias, der im Rahmen der Braze-Shopify-Integration gesetzt wird, mit Braze-Nutzerprofilen abgeglichen. Nutzer:innen ohne ein übereinstimmendes Braze-Nutzerprofil werden bei der Synchronisierung übersprungen.

Weitere Informationen darüber, wie die Shopify-Integration Nutzer:innen identifiziert und Aliase zuweist, finden Sie unter [Shopify-Daten-Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

Braze gleicht synchronisierte Nutzer:innen mit bestehenden Braze-Nutzerprofilen ab – unabhängig davon, wie diese Profile erstellt wurden, einschließlich durch den historischen Shopify-Backfill, Ihre eigene Datenplattform (wie Snowflake oder ein anderes Data Warehouse) oder direkte API-Importe. Wenn Ihre Kohorte kleiner ist als Ihr Shopify-Segment, bedeutet das, dass einige Segment-Mitglieder noch kein übereinstimmendes Braze-Profil haben. Um die Zuordnungsabdeckung zu erhöhen, befüllen Sie Braze-Nutzerprofile über Ihre bevorzugte Methode, bevor Sie die Synchronisierung starten.

## Einschränkungen {#limitations}

- **Einseitige Synchronisierung.** Die Segment-Mitgliedschaft fließt nur von Shopify zu Braze. Änderungen an der Kohorte, die direkt in Braze vorgenommen werden, werden nicht an Shopify zurückgesendet.
- **Keine Profilerstellung.** Nur Shopify-Kund:innen, die bereits ein Braze-Nutzerprofil haben, werden der Kohorte hinzugefügt.
- **Keine Möglichkeit, die Synchronisierung über Braze zu stoppen.** Um die Synchronisierung eines Segments zu stoppen, löschen Sie es in Shopify. Die Kohorte und ihre Mitglieder bleiben in Braze erhalten und werden nicht mehr aktualisiert.
- **Erneute Synchronisierung fügt nur Mitglieder hinzu.** Bei einer erneuten Synchronisierung eines Segments werden neu passende Nutzer:innen zur Kohorte hinzugefügt, aber Nutzer:innen, die nicht mehr im Shopify-Segment sind, werden nicht entfernt.