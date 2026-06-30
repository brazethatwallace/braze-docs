---
nav_title: "Anonyme Nutzer:innen"
article_title: "Anonyme Nutzer:innen"
page_order: 0
page_type: reference
description: "Dieser Artikel bietet eine Übersicht über anonyme Nutzer:innen und Nutzer-Aliase. Er erläutert ihre Bedeutung und wie Sie sie in Ihren Nachrichten nutzen können."

---

# Anonyme Nutzer:innen {#anonymous-users}

> Nutzer:innen, die Ihre Website oder Anwendung besuchen, ohne sich anzumelden – wie Gastbesucher:innen –, werden als anonyme Nutzer:innen erkannt. Diese Nutzer:innen verfügen nicht über `external_ids`, die zum Aktualisieren von Nutzerprofilen mit der Braze API verwendet werden, aber ihnen sind dennoch [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points) zugeordnet und sie können in Ihren Segmenten gezielt angesprochen werden.

Wenn anonyme Nutzer:innen Ihre Website oder Anwendung besuchen, erstellt das Braze SDK ein „anonymes“ Nutzerprofil und ordnet es ihnen zu. Während die Nutzer:innen surfen, erfasst das SDK automatisch Daten für ihr anonymes Nutzerprofil, z. B. Nutzungsinformationen, Geräteinformationen und mehr, wenn Sie angepasste Attribute und angepasste Events eingerichtet haben.

Mit erfassten anonymen Nutzer:innen können Sie Folgendes tun:

- Nutzer:innen Nachrichten senden, bevor sie sich anmelden
- Das Profil von Nutzer:innen erfassen, bevor sie sich anmelden, damit Ihnen keine relevanten Daten entgehen
- Die Vervollständigung des Profils mit einer Nachricht fördern, wenn Nutzer:innen ihr Profil nur teilweise ausgefüllt haben
- Das Profil von Nutzer:innen vervollständigen, wenn sie sich anmelden, damit Sie Messaging auf anderen Plattformen abbrechen können (z. B. keine Nachricht „Kostenloser Versand bei der 1. App-Bestellung“ senden, wenn die Nutzer:innen bereits App-Bestellungen getätigt haben)
- Nutzer:innen ansprechen, die eine Absicht zum Verlassen zeigen, indem Sie sie ermutigen, ein Profil zu erstellen, ihren Warenkorb abzuschließen oder eine andere Aktion durchzuführen

## Funktionsweise {#how-it-works}

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## Nutzer-Aliase zuweisen {#assigning-user-aliases}

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## Anonyme Nutzer:innen zusammenführen {#merging-anonymous-users}

Manchmal handelt es sich bei anonymen Nutzerprofilen um Duplikate, die dieselbe Telefonnummer oder E-Mail-Adresse wie andere Nutzerprofile haben. Eines der Duplikate kann sogar ein identifiziertes Nutzerprofil sein. Diese Duplikate können mit dem [POST: Nutzer:innen zusammenführen-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) oder einem der Zusammenführungs-Tools auf der Braze-Plattform, wie z. B. der [regelbasierten Zusammenführung]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#rules-based-merging), zu einem Nutzerprofil zusammengeführt werden.

## Anonyme Nutzer:innen nachschlagen {#looking-up-an-anonymous-user}

Da anonyme Nutzer:innen keine `external_id` haben, können Sie eine Geräte-ID verwenden, um ein bestimmtes Profil zu suchen. Die folgenden Schritte zeigen, wie Sie die Geräte-ID für die aktuellen Nutzer:innen in Ihrer Web-SDK-Integration abrufen:

1. Öffnen Sie die Entwicklertools Ihres Browsers (z. B. in Chrome: **Command + Option + J** auf Mac oder **Strg + Umschalt + I** unter Windows).
2. Führen Sie im Tab **Console** Folgendes aus:

```javascript
console.log(braze.getDeviceId());
```

{:start="3"}
3. Verwenden Sie im Braze-Dashboard die [Nutzersuche]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search), um nach der zurückgegebenen Geräte-ID zu suchen.

## Anwendungsfälle {#use-cases}

### Anonyme Nutzer:innen in Ihrem Segment ansprechen {#target-anonymous-users-in-your-segment}

Da anonyme Nutzer:innen keine `external_id` haben, können Sie sie in großen Mengen mit dem Segmentierungsfilter **Externe Nutzer-ID ist leer** ansprechen. Für eine höhere Genauigkeit können Sie den anonymen Nutzer:innen, die Sie ansprechen möchten, ein angepasstes Attribut hinzufügen und danach filtern.

Nehmen wir an, Sie weisen jedem anonymen Nutzerprofil das angepasste Attribut „is_lead_profile“ zu. Sie könnten diese Profile mit einem oder beiden der folgenden Filter ansprechen:

- **Externe Nutzer-ID ist leer**
- „is_lead_profile“ **ist wahr**

![Segmentfilter für eine leere externe Nutzer-ID und ein angepasstes Attribut „is_lead_profile“ mit dem Wert „wahr“.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### Checkout-Daten von anonymen Nutzer:innen erfassen {#capture-checkout-data-from-an-anonymous-user}

Sie können Checkout-Daten von anonymen Nutzer:innen (oder Gastbesucher:innen) erfassen, indem Sie während des Bestellvorgangs ein Nutzer-Alias-Profil erstellen. Wenn anonyme Nutzer:innen über ein Web-Capture-Formular auschecken, lassen Sie einen API-Aufruf triggern, um ein Nutzer-Alias-Profil zu erstellen und ein Kauf-Event zu protokollieren. Anschließend können Sie das erstellte Nutzerprofil über die Braze API aktualisieren.

Hier ist ein Beispiel für eine Payload, die generiert wird, wenn das Web-Capture-Formular übermittelt wird:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}