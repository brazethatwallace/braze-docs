---
nav_title: Domainübergreifende Web-SDK-Nutzer:innen verknüpfen
article_title: Domainübergreifende Web-SDK-Nutzer:innen über die Geräte-ID verknüpfen
page_order: 1
page_type: reference
description: "Übergeben Sie die Geräte-ID des Braze Web SDK von der Marketing-Website von Kitchenerie an eine separate Shop-Domain, damit anonyme Aktivitäten ein gemeinsames Nutzerprofil verwenden."
---

# Domainübergreifende Web-SDK-Nutzer:innen über die Geräte-ID verknüpfen {#link-cross-domain-web-sdk-users-through-device-id}

> Übergeben Sie die Geräte-ID des Braze Web SDK über die Ziel-URL, wenn zwei Domains keine Cookies teilen können, damit anonyme Sitzungen auf beiden Websites demselben Braze-Nutzerprofil zugeordnet werden.

## Über dieses Beispiel {#about-this-example}

Kitchenerie, ein fiktiver Einzelhändler für Küchenartikel, betreibt eine Marketing-Website (`kitchenerie.com`) und einen Shop (`kitchenerie.shop`). Jede Domain hat eine eigene Braze Web SDK-Integration. Browser-Cookies werden nicht domainübergreifend geteilt, sodass Braze separate Geräte-IDs – und separate anonyme Profile – zuweist, wenn dieselbe Person von der Marketing-Website zum Shop wechselt.

Dieses Muster:

1. Liest die Geräte-ID auf der Quell-Domain mit `getDeviceId` nach der SDK-Initialisierung aus
2. Hängt sie als Query-Parameter an ausgehende Links an (zum Beispiel `brazeDeviceId`)
3. Liest auf der Ziel-Domain diesen Parameter aus und übergibt ihn über die Option `deviceId` an `braze.initialize`

Die Übergabe ist vor allem für anonyme Nutzer:innen relevant. Nachdem sich die Person im Shop anmeldet, wird `changeUser` mit einer `external_id` zum dauerhaften Bezeichner über Geräte hinweg. Siehe [Nutzer-IDs festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).

Beide Domains sollten denselben Braze-Workspace-API-Schlüssel und SDK-Endpunkt verwenden, damit Ereignisse in einem Profil landen.

## Überlegungen {#considerations}

- Die Geräte-ID ist browserspezifisch. Dieses Muster verknüpft keine Aktivitäten über verschiedene Browser, Geräte oder Profile hinweg. Verwenden Sie `external_id` über `changeUser` für authentifizierte, geräteübergreifende Identität.
- Rufen Sie die Geräte-ID erst ab, nachdem das Web SDK auf der Quell-Domain initialisiert wurde. Ein Aufruf von `getDeviceId` vor `initialize` gibt keinen Wert zurück.
- Das Web SDK liest `deviceId` einmalig bei `initialize`. Es gibt kein nachträgliches `setDeviceId`, das die aktive Geräte-ID ändert. Lesen Sie den URL-Parameter auf der Ziel-Domain aus, bevor Sie `initialize` aufrufen.
- Direktbesuche, Lesezeichen oder Verweise von Drittanbietern auf den Shop ohne `brazeDeviceId` sollten auf die standardmäßige Geräte-ID-Zuweisung zurückfallen – das ist zu erwarten, wenn keine Quell-Domain-ID vorhanden ist.
- Query-Parameter erscheinen im Browserverlauf und in Server-Logs.
- Query-Parameter können über Referrer-Header weitergegeben werden. Die Geräte-ID ist für sich genommen keine PII, aber entfernen Sie den Parameter nach der Verarbeitung, wenn Ihr Datenschutzteam dies verlangt (siehe Schritt 2).
- Testen Sie End-to-End. Bestätigen Sie mit der Netzwerkinspektion, dass Ereignisse von Domain 2 die erwartete Geräte-ID verwenden.
- Passen Sie Hostnamen, Link-Selektoren und Fehlerbehandlung an Ihre Website an. Testen Sie in Ihrer Entwicklungsumgebung, bevor Sie in die Produktion gehen.

## Einrichtung {#setup}

### Schritt 1: Geräte-ID an domainübergreifende Links auf der Quell-Domain anhängen {#step-1-append-the-device-id-to-cross-domain-links-on-the-source-domain}

Initialisieren Sie auf `kitchenerie.com` (Domain 1) das Web SDK wie gewohnt und hängen Sie dann die aktuelle Geräte-ID an Links an, die auf `kitchenerie.shop` (Domain 2) verweisen.

Wählen Sie einen Query-Parameter-Namen, der nicht mit Ihrer Website kollidiert (dieses Beispiel verwendet `brazeDeviceId`). Dieselbe Idee gilt für serverseitig gerenderte Links, clientseitige Navigation oder `src`-Werte von iframes, die Sie kontrollieren.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});
braze.openSession();

const destinationHost = "kitchenerie.shop";

braze.getDeviceId(function (deviceId) {
  if (!deviceId) {
    return;
  }

  const links = document.querySelectorAll('a[href*="' + destinationHost + '"]');

  links.forEach(function (link) {
    try {
      const url = new URL(link.href);
      url.searchParams.set("brazeDeviceId", deviceId);
      link.href = url.toString();
    } catch (e) {
      // Skip malformed hrefs (for example, javascript:, mailto:, or unparsable relative paths).
    }
  });
});
```

Wenn Ihre SDK-Version `getDeviceId` synchron bereitstellt (ohne Callback), rufen Sie es stattdessen nach der Initialisierung auf:

```javascript
const deviceId = braze.getDeviceId();
```

Siehe [Web SDK Repository-Leitfaden – Geräte-ID abrufen]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#get-device-id) und [Initialisierungsoptionen – `deviceId`]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#initialization-options).

### Schritt 2: Geräte-ID auslesen und Web SDK auf der Ziel-Domain initialisieren {#step-2-read-the-device-id-and-initialize-the-web-sdk-on-the-destination-domain}

Lesen Sie auf `kitchenerie.shop` (Domain 2) `brazeDeviceId` aus dem Query-String aus, bevor Sie `initialize` aufrufen, und übergeben Sie den Wert in den Initialisierungsoptionen, wenn er vorhanden ist.

```javascript
import * as braze from "@braze/web-sdk";

const urlParams = new URLSearchParams(window.location.search);
const passedDeviceId = urlParams.get("brazeDeviceId");

const initOptions = {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
};

if (passedDeviceId) {
  initOptions.deviceId = passedDeviceId;
}

braze.initialize("YOUR-API-KEY-HERE", initOptions);
braze.openSession();

// Optional: remove the parameter from the visible URL after consumption.
if (passedDeviceId) {
  const cleanUrl = new URL(window.location.href);
  cleanUrl.searchParams.delete("brazeDeviceId");
  window.history.replaceState({}, document.title, cleanUrl.toString());
}
```

Wenn sich die Person anmeldet, rufen Sie `changeUser` mit ihrer `external_id` auf, damit zukünftige Aktivitäten dem identifizierten Profil zugeordnet werden.

### Schritt 3: Übergabe überprüfen {#step-3-verify-the-handoff}

1. Öffnen Sie Domain 1 in einem Browser, in dem Sie nicht angemeldet sind.
2. Folgen Sie einem domainübergreifenden Link zu Domain 2.
3. Bestätigen Sie im Netzwerk-Tab des Browsers, dass Domain 2 Ereignisse mit derselben Geräte-ID sendet, die Domain 1 verwendet hat.
4. Wiederholen Sie den Vorgang mit einem Direktbesuch auf Domain 2 (ohne Query-Parameter) und bestätigen Sie, dass eine neue Geräte-ID zugewiesen wird.

## Verwandte Artikel {#related-articles}

- [Web SDK Repository-Leitfaden]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)
- [Multi-Domain-Integration für das Braze Web SDK]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)
- [Nutzer-IDs über das Braze SDK festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)
- [Anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)
- [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Web SDK-Speicher]({{site.baseurl}}/developer_guide/storage)