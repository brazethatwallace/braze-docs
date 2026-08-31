---
nav_title: Custom Objects
article_title: Custom-Objects-Endpunkte
search_tag: Endpoint
page_order: 9.5
layout: dev_guide
page_type: landing
description: "Diese Landing-Page listet die Braze Custom-Objects-Endpunkte auf."
needs_mermaid: true

guide_top_header: "Custom-Objects-Endpunkte"
guide_top_text: "Verwenden Sie diese Endpunkte, um angepasste Objekttypen aufzulisten, angepasste Objektdatensätze zu verwalten und Objekt- sowie Nutzer:innen-Beziehungen zu verwalten."
guide_top_alert: "Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Custom-Objects-API-Schlüsselberechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden."

guide_featured_title: "Typ-Endpunkte"
guide_featured_list:
  - name: "GET: Angepasste Objekttypen auflisten"
    link: /docs/api/endpoints/custom_objects/types/get_list_custom_object_types
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Angepassten Objekttyp abrufen"
    link: /docs/api/endpoints/custom_objects/types/get_custom_object_type
    image: /assets/img/braze_icons/search-md.svg
  - name: "GET: Nutzer:innen-Beziehungstypen auflisten"
    link: /docs/api/endpoints/custom_objects/types/get_list_user_relationship_types
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Objekt-Beziehungstypen auflisten"
    link: /docs/api/endpoints/custom_objects/types/get_list_object_relationship_types
    image: /assets/img/braze_icons/link-external-01.svg

guide_menu_title: "Objekt-Endpunkte"
guide_menu_list:
  - name: "GET: Angepasste Objekte auflisten"
    link: /docs/api/endpoints/custom_objects/objects/get_list_custom_objects
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Angepasstes Objekt abrufen"
    link: /docs/api/endpoints/custom_objects/objects/get_custom_object
    image: /assets/img/braze_icons/search-md.svg
  - name: "POST: Angepasstes Objekt erstellen"
    link: /docs/api/endpoints/custom_objects/objects/post_create_custom_object
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Angepasstes Objekt ersetzen"
    link: /docs/api/endpoints/custom_objects/objects/put_replace_custom_object
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Angepasstes Objekt aktualisieren"
    link: /docs/api/endpoints/custom_objects/objects/patch_update_custom_object
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Angepasstes Objekt löschen"
    link: /docs/api/endpoints/custom_objects/objects/delete_custom_object
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title2: "Objekt-Beziehungs-Endpunkte"
guide_menu_list2:
  - name: "GET: Objekt-Beziehungen auflisten"
    link: /docs/api/endpoints/custom_objects/object_relationships/get_list_object_relationships
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Objekt-Beziehung erstellen"
    link: /docs/api/endpoints/custom_objects/object_relationships/post_create_object_relationship
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Objekt-Beziehung ersetzen"
    link: /docs/api/endpoints/custom_objects/object_relationships/put_replace_object_relationship
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Objekt-Beziehung aktualisieren"
    link: /docs/api/endpoints/custom_objects/object_relationships/patch_update_object_relationship
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Objekt-Beziehung löschen"
    link: /docs/api/endpoints/custom_objects/object_relationships/delete_object_relationship
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title3: "Nutzer:innen-Beziehungs-Endpunkte"
guide_menu_list3:
  - name: "GET: Nutzer:innen-Beziehungen auflisten"
    link: /docs/api/endpoints/custom_objects/user_relationships/get_list_user_relationships
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Nutzer:innen-Beziehung erstellen"
    link: /docs/api/endpoints/custom_objects/user_relationships/post_create_user_relationship
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Nutzer:innen-Beziehung ersetzen"
    link: /docs/api/endpoints/custom_objects/user_relationships/put_replace_user_relationship
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Nutzer:innen-Beziehung aktualisieren"
    link: /docs/api/endpoints/custom_objects/user_relationships/patch_update_user_relationship
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Nutzer:innen-Beziehung löschen"
    link: /docs/api/endpoints/custom_objects/user_relationships/delete_user_relationship
    image: /assets/img/braze_icons/edit-05.svg
---

## Basis-URL und Authentifizierung {#base-url-and-authentication}

Verwenden Sie Ihren Workspace-REST-Endpunkt und senden Sie `Authorization: Bearer YOUR_REST_API_KEY`. Dieser Abschnitt erklärt, wo Custom-Objects-Endpunkte gehostet werden und wie Anfragen authentifiziert werden.

- Informationen zu Endpunkt-Hosts finden Sie in der [Braze-API-Übersicht]({{site.baseurl}}/api/basics#endpoints).
- Alle Anfrage- und Antwort-Payloads sind JSON.
- Anfragen sind auf den Workspace beschränkt, der den API-Schlüssel besitzt.
- Wenn der Schlüssel eine IP-Zulassungsliste hat, geben nicht zugelassene IP-Adressen `403` zurück.

## API-Schlüsselberechtigungen {#api-key-permissions}

Dieser Abschnitt ordnet jeden Endpunkt seiner erforderlichen Berechtigung zu, damit Sie API-Schlüssel sicher einschränken können.

| Berechtigung | Endpunkt-Gruppe |
|---|---|
| `custom_objects.read` | Typ- und Objekt-Lesevorgänge sowie Objekt-Beziehungs-Lesevorgänge |
| `custom_objects.create` | Objekt erstellen |
| `custom_objects.update` | Objekt ersetzen und aktualisieren |
| `custom_objects.delete` | Objekt löschen |
| `custom_objects.user_relationships.read` | Nutzer:innen-Beziehungs-Lesevorgänge |
| `custom_objects.user_relationships.create` | Nutzer:innen-Beziehung erstellen |
| `custom_objects.user_relationships.update` | Nutzer:innen-Beziehung ersetzen und aktualisieren |
| `custom_objects.user_relationships.delete` | Nutzer:innen-Beziehung löschen |
| `custom_objects.object_relationships.create` | Objekt-Beziehung erstellen |
| `custom_objects.object_relationships.update` | Objekt-Beziehung ersetzen und aktualisieren |
| `custom_objects.object_relationships.delete` | Objekt-Beziehung löschen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom-Objects-Berechtigungsgruppen" }

{% alert note %}
Objekt-Beziehungs-Lesevorgänge verwenden `custom_objects.read`. Es gibt keine Berechtigung `custom_objects.object_relationships.read`.
{% endalert %}

## Rate-Limits

Dieser Abschnitt erklärt die Standard-Anfragekontingente und Antwort-Header für Lese- und Schreibverkehr.

| Bucket | Standardlimit |
|---|---|
| Custom-Objects-Lesevorgänge | 50 Anfragen pro Minute |
| Custom-Objects-Schreibvorgänge | 50 Anfragen pro Minute |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom-Objects-Standard-Rate-Limits" }

Jede Antwort enthält `X-RateLimit-Limit`, `X-RateLimit-Remaining` und `X-RateLimit-Reset`.

Für gedrosselte Anfragen gibt Braze `429` und ein Fehler-Payload mit `id` und `message` zurück.

```json
{
  "errors": [
    {
      "id": "rate-limit-exceeded",
      "message": "You have exceeded your limit of 50 requests per minute."
    }
  ]
}
```

## Grundlegende Konzepte {#core-concepts}

Dieser Abschnitt definiert die wichtigsten Bezeichner, die über alle Custom-Objects-Endpunkte hinweg verwendet werden.

- `type_name`: Der Maschinenname des angepassten Objekttyps, eindeutig innerhalb eines Workspace.
- `external_id`: Ihr Objektbezeichner, eindeutig innerhalb eines Typs.
- `braze_id`: Die Braze-Nutzer:innen-ID, die auf Nutzer:innen-Beziehungs-Endpunkten verwendet wird.
- `attributes`: Feldname-basiertes Objekt oder Beziehungsdaten, die gegen das konfigurierte Schema validiert werden.

## Wie Beziehungen funktionieren {#how-relationships-work}

Dieser Abschnitt erklärt Beziehungstypen, Beziehungskanten und das `anchor`-Verhalten, bevor Sie die Endpunkt-Referenzseiten verwenden.

### Beziehungsmodell auf einen Blick {#relationship-model-at-a-glance}

Verwenden Sie dieses Diagramm, um zu sehen, wie Typen, Datensätze und Beziehungen zusammenpassen und was deren Verknüpfung in Braze ermöglicht. Sie definieren die Typen im Dashboard und erstellen dann die Datensätze und die Verknüpfungen zwischen ihnen über diese Endpunkte.

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 400}} }%%
flowchart LR
  subgraph define["Set up in the dashboard"]
    objtype["Custom object types define<br/>the fields a record has"]
    reltype["Relationship types determine<br/>which links are allowed"]
  end

  subgraph write["Write with the API"]
    person["A person you<br/>send messages to"]
    record["A business record<br/>they belong to"]
    related["Another record<br/>connected to it"]
    person -- "A user relationship links<br/>a person to a record" --> record
    record -- "An object relationship links<br/>one record to another" --> related
  end

  subgraph unlock["What it unlocks"]
    segment["Segment people by the<br/>records they belong to"]
    liquid["Personalize messages with<br/>data from those records"]
  end

  define -- "decides what you<br/>are allowed to link" --> write
  write -- "makes these<br/>possible" --> unlock
```

### Typen und Kanten sind getrennt {#types-and-edges-are-separate}

- Beziehungstypen definieren, welche Verknüpfungen zulässig sind, und werden im Dashboard verwaltet.
- Beziehungskanten sind die tatsächlichen Verknüpfungen zwischen Datensätzen und werden über diese API-Endpunkte erstellt, aktualisiert und gelöscht.
- Bevor Sie Beziehungen schreiben, listen Sie gültige `rel_kind`-Werte auf mit:
  - `GET /custom_objects/types/{type_name}/user_relationship_types`
  - `GET /custom_objects/types/{type_name}/object_relationship_types`

### Warum Objekt-Beziehungen `related_type_name` erfordern {#why-object-relationships-require-related_type_name}

- `rel_kind` ist nicht global eindeutig über alle Objekttyppaare hinweg. Zum Beispiel kann `rel_kind` für ein Paar von Objekttypen `subaccount` und für ein anderes `partner_account` sein.
- Objekt-Beziehungs-Schreibvorgänge erfordern daher sowohl `rel_kind` als auch `related_type_name`, um den beabsichtigten Beziehungstyp zusammen mit dem anderen Objekttyp in der Zuordnung zu identifizieren.
- Wenn `related_type_name` nicht zum Beziehungstyp für diesen `rel_kind` passt, gibt die Anfrage `400` zurück.

### `anchor` steuert die Beziehungsrichtung {#anchor-controls-relationship-direction}

Objekt-Beziehungen sind gerichtet. Das URL-Objekt wird basierend auf `anchor` interpretiert.

| `anchor` | Rolle des URL-Objekts | Schlüssel des verwandten Objekts in Antworten |
|---|---|---|
| `source` (Standard) | Von-Seite (ausgehende Kante) | `to_custom_object` |
| `target` | Zu-Seite (eingehende Kante) | `from_custom_object` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anchor-Verhalten für Objekt-Beziehungen" }

Das Erstellen derselben Kante aus der entgegengesetzten Anchor-Perspektive zielt weiterhin auf eine zugrunde liegende Beziehung ab. Ein zweiter Erstellungsaufruf für dieselbe Kante gibt `409` (`duplicate-object-relationship`) zurück.

### Pfad-Asymmetrie bei Nutzer:innen-Beziehungen {#path-asymmetry-for-user-relationships}

Lese- und Schreibvorgänge für Nutzer:innen-Beziehungen verwenden absichtlich unterschiedliche Endpunkt-Pfade:

- Lesen: `GET /custom_objects/objects/{type_name}/{external_id}/user_relationships`
- Schreiben: `POST|PUT|PATCH|DELETE /custom_objects/objects/{type_name}/{external_id}/users`

### Beziehungsattribute sind getrennt von Objektattributen {#relationship-attributes-are-separate-from-object-attributes}

- Beziehungs-Endpunkte geben Attribute auf Kantenebene im Top-Level-Feld `attributes` zurück.
- Objektattribute bleiben verschachtelt unter `to_custom_object` oder `from_custom_object`.
- `PUT` ersetzt Beziehungs-`attributes`, und `PATCH` führt Beziehungs-`attributes` zusammen.

### Praxisbeispiel {#worked-example}

Dieses Beispiel zeigt einen typischen Konto-Workflow:

1. Erstellen Sie `account/acct-123`.
2. Erstellen Sie `account/acct-456` als Unterkonto.
3. Verknüpfen Sie eine Nutzer:in mit `acct-123` über `rel_kind: account_user`.
4. Verknüpfen Sie `acct-123` mit `acct-456` über `rel_kind: subaccount`.

Um die Verknüpfungen zurückzulesen:

- `GET /custom_objects/objects/account/acct-123/user_relationships` für verknüpfte Nutzer:innen
- `GET /custom_objects/objects/account/acct-123/object_relationships` für ausgehende Objekt-Verknüpfungen
- `GET /custom_objects/objects/account/acct-456/object_relationships?anchor=target` für eingehende Objekt-Verknüpfungen

{% alert note %}
Die `DELETE`-Endpunkte für Objekt-Beziehungen und Nutzer:innen-Beziehungen erfordern einen JSON-Anfragekörper.
{% endalert %}

## Paginierung und Datenaktualität {#pagination-and-data-freshness}

Dieser Abschnitt behandelt das Paginierungsverhalten bei Listenabfragen und die erwartete Sichtbarkeit von Daten nach Schreibvorgängen.

- Listen-Endpunkte unterstützen `limit` und `offset`.
- `limit` ist standardmäßig `100` und wird auf `1` bis `250` begrenzt.
- `offset` ist standardmäßig `0`, und negative Werte werden auf `0` gesetzt.
- Schreibvorgänge sind sofort für Lesevorgänge und Liquid-Personalisierung sichtbar.
- Segment-Mitgliedschaften basierend auf Custom Objects können bis zu einer Stunde verzögert sein, da berechnete Filter stündlich aktualisiert werden.

## Fehlerverhalten {#error-behavior}

Dieser Abschnitt fasst Status- und Fehlerantwortmuster zusammen, die über die Custom-Objects-Endpunkte hinweg verwendet werden.

- `404`, `409`, `422` und `429` geben ein `errors`-Array mit `id` und `message` zurück.
- `400`, `401` und `403` geben einen einzelnen `error`-String zurück.
- Vertragsbasierte `422`-Limits variieren je nach Unternehmen.