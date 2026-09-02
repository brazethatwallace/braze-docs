---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Apteligent, einer mobilen Anwendung, die detaillierte Absturzberichte liefert und es Ihnen ermöglicht, kritische Daten in Ihrer bestehenden Braze-Lösung zu protokollieren."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) ist eine Plattform für die Performance von mobilen Anwendungen, die Entwickler:innen und Produktmanager:innen Tools und Insights bietet.

_Diese Integration wird von Apteligent gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Apteligent bietet detaillierte iOS-Absturzberichte, die es Ihnen ermöglichen, kritische Daten in Ihrer bestehenden Braze-Lösung zu protokollieren sowie Nutzer:innen, bei denen es zu Anwendungsabstürzen gekommen ist, zu segmentieren, zu verstehen und mit ihnen in Kontakt zu treten.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| TestDrive-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein TestDrive-Konto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert warning %}
Diese Integration wird derzeit nur auf iOS unterstützt.
{% endalert %}

## Integration {#apteligent-ios-integration}

### 1. Schritt: Einen Observer Registrierung {#step-1-register-an-observer}

Zunächst müssen Sie einen Observer Registrierung. Stellen Sie sicher, dass dies geschieht, bevor Sie Apteligent initialisieren.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### 2. Schritt: Angepasste Absturz-Analytics protokollieren {#step-2-log-custom-crash-analytics}

Das Apteligent SDK löst eine Benachrichtigung aus, wenn Nutzer:innen die Anwendung nach einem Absturz laden. Die Benachrichtigung enthält den Namen des Absturzes, den Grund und das Datum des Vorkommens.

Nach Erhalt der Benachrichtigung protokollieren Sie ein angepasstes Absturz-Event und aktualisieren die Nutzerattribute mit den Absturzberichten von Apteligent:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Nach Abschluss können Sie die leistungsstarken Segmentierungs- und Engagement-Analytics von Braze nutzen, indem Sie die Absturzinformationen der Apteligent-Plattform verwenden.