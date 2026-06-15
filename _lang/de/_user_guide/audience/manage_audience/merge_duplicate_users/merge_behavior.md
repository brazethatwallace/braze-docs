---
nav_title: Zusammenführungsverhalten
article_title: Zusammenführungsverhalten von Nutzer:innen
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Braze die Zusammenführung von Nutzer:innen handhabt – für zum Löschen markierte Nutzer:innen, Testnutzer:innen und Nutzer:innen der Globalen Kontrollgruppe."
---

# Zusammenführungsverhalten von Nutzer:innen {#user-merge-behavior}

> Erfahren Sie, wie Braze die Zusammenführung von Nutzer:innen handhabt, einschließlich der drei Nutzertypen, bei denen das Standardverhalten nicht gilt: zum Löschen markierte Nutzer:innen, Testnutzer:innen und Nutzer:innen der Globalen Kontrollgruppe.

Dieses Verhalten gilt für alle Zusammenführungen, unabhängig davon, ob Sie die [individuelle Zusammenführung]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#individual-merging), die [Massenzusammenführung]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#bulk-merging) oder den [API-Endpunkt „Nutzer:innen zusammenführen“]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) verwenden.

## Allgemeines Zusammenführungsverhalten {#general-merge-behavior}

Wenn Sie zwei Nutzerprofile zusammenführen, füllt Braze leere Felder im beizubehaltenden Profil mit Werten aus dem zusammenzuführenden Profil. Wenn ein Feld in beiden Profilen einen Wert hat, behält Braze den Wert des beizubehaltenden Profils bei.

Wenn ein Wert beispielsweise nur in einem der beiden Profile vorhanden ist, behält Braze ihn bei:

| Feld | Zusammenzuführendes Profil | Beizubehaltendes Profil | Resultierendes Profil |
|---|---|---|---|
| `first_name` | Alex | (leer) | Alex |
| `last_name` | (leer) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Wenn beide Profile einen Wert für dasselbe Feld haben, behält Braze den Wert des beizubehaltenden Profils bei:

| Feld | Zusammenzuführendes Profil | Beizubehaltendes Profil | Resultierendes Profil |
|---|---|---|---|
| `first_name` | Alex | Al | Al |
| `last_name` | (leer) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Dieses Verhalten funktioniert gut für Standard- und angepasste Attribute. Braze behandelt die folgenden Nutzertypen jedoch anders.

## Zusammenfassung des Verhaltens {#behavior-summary}

| Nutzertyp | Verhalten | Grund |
|---|---|---|
| Zum Löschen markierte Nutzer:innen | Keine Zusammenführung | Zum Löschen markierte Profile werden innerhalb von 7 Tagen gelöscht, sodass ihre Daten nicht erhalten bleiben müssen. |
| Testnutzer:innen | Zusammenführung, Testnutzer:innen-Status bleibt erhalten | Die Beibehaltung des Testnutzer:innen-Status hilft Ihnen, nach einer Zusammenführung eine nutzbare Testpopulation zu behalten. |
| Nutzer:innen der Globalen Kontrollgruppe | Keine Zusammenführung | Eine Zusammenführung würde die zufälligen Bucket-Nummern ändern, was Experimente und Berichte beeinflussen würde. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Zum Löschen markierte Nutzer:innen {#users-marked-for-deletion}

Wenn Sie das [Massenlöschungs-Tool]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/) verwenden, um ein Segment zu löschen, markiert Braze diese Nutzerprofile zur Löschung innerhalb der nächsten 7 Tage. Braze führt keine Profile zusammen, die zum Löschen markiert sind – weder als beizubehaltendes noch als zusammenzuführendes Profil.

Wenn Sie ein zum Löschen markiertes Profil zusammenführen müssen, [stornieren Sie zunächst die Segment-Löschung]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/#cancel) oder entfernen Sie die Nutzer:in aus der Löschung, damit das Profil nicht mehr markiert ist.

## Testnutzer:innen {#test-users}

Braze erlaubt die Zusammenführung von Testnutzer:innen-Profilen und behält den Testnutzer:innen-Status im resultierenden Profil bei. Dies unterscheidet sich vom [allgemeinen Zusammenführungsverhalten](#general-merge-behavior), das ansonsten den Wert des beizubehaltenden Profils beibehalten würde.

Die folgende Tabelle zeigt den resultierenden Testnutzer:innen-Status für jede Kombination:

| Zusammenzuführendes Profil | Beizubehaltendes Profil | Resultierendes Profil |
|---|---|---|
| Keine Testnutzer:in | Keine Testnutzer:in | Keine Testnutzer:in |
| Testnutzer:in | Testnutzer:in | Testnutzer:in |
| Testnutzer:in | Keine Testnutzer:in | Testnutzer:in |
| Keine Testnutzer:in | Testnutzer:in | Testnutzer:in |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Informationen zu Testnutzer:innen finden Sie unter [Interne Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/).

## Nutzer:innen der Globalen Kontrollgruppe {#global-control-group-users}

Braze führt keine Nutzerprofile in einer [Globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group/) zusammen – weder als beizubehaltendes noch als zusammenzuführendes Profil.

Die Zugehörigkeit zur Globalen Kontrollgruppe wird durch die [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) einer Nutzer:in bestimmt. Eine Zusammenführung würde ändern, welche Nutzer:innen zur Gruppe gehören, was Ihre Experimente und Berichte beeinflussen würde.

## Verwandte Artikel {#related-articles}

- [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/)
- [POST: Nutzer:innen zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [Nutzer:innen löschen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)
- [Globale Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group/)
- [Zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)
- [Interne Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/)