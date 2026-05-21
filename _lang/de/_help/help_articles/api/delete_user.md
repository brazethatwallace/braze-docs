---
nav_title: "Nutzer:innen über API entfernen"
article_title: "Nutzer:innen über API entfernen"
page_order: 0

page_type: reference
description: "Dieser Hilfeartikel beschreibt die Auswirkungen des Entfernens eines Nutzerprofils über die Braze REST API."
tool: Dashboard
platform: API
---

# Nutzer:innen über API entfernen {#remove-users-via-api}

Wenn Sie [eine:n Nutzer:in über die Braze REST API entfernen]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), werden die folgenden Daten gelöscht (auf null gesetzt):
- Alle Attribute, die der/die Nutzer:in hatte
- E-Mail-Adresse
- Telefonnummer
- Externe Nutzer-ID
- Geschlecht
- Land
- Sprache

Wenn Sie [eine:n Nutzer:in über die Braze REST API entfernen]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), treten die folgenden Ereignisse ein:
- Das Nutzerprofil wird gelöscht (auf null gesetzt).
- Die Anzahl der [Lifetime-Nutzer:innen]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users) wird aktualisiert, um die neu entfernten Nutzer:innen zu berücksichtigen.
- Die entfernten Nutzer:innen werden weiterhin in den aggregierten Conversion-Prozentsatz einbezogen. Angepasste Event-Zähler und Kauf-Zähler werden für entfernte Nutzer:innen nicht aktualisiert.

## Mehrere Profile mit einer gemeinsamen E-Mail-Adresse {#multiple-profiles-with-a-shared-email-address}

Angenommen, Sie möchten mehrere Nutzerprofile zusammenführen, die dieselbe E-Mail-Adresse haben.

So führen Sie diese Nutzerprofile zusammen:

 1. Identifizieren Sie alle Nutzer:innen mit doppelten E-Mail-Adressen.
 2. Exportieren Sie alle Attribute eines einzelnen Profils.
 3. Importieren Sie diese Attribute in das Nutzerprofil entweder über die API oder per CSV.
 4. Entfernen Sie die Nutzer:innen über die API und löschen Sie damit diese doppelten Nutzer:innen und die oben genannten Daten.

_Zuletzt aktualisiert am 13. September 2023_