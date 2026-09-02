---
nav_title: Vizbee
article_title: Vizbee für TV-Deeplinking
alias: /partners/vizbee/
page_type: partner
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Vizbee und wie Sie diese nutzen können, um TV-Deeplinking zu unterstützen."
search_tag: Partner

---
# Vizbee {#vizbee}

> [Vizbee](https://vizbee.tv/) ermöglicht es allen Smartphones und Smart-TVs in Ihrem Zuhause, als ein nahtloses Gerät zusammenzuarbeiten und so großartige Nutzererlebnisse zu schaffen. Vizbee hilft Ihnen, bestehende Kanäle für das Mobile-App-Marketing wie Benachrichtigungen, Deeplinks und E-Mails zu nutzen, um nahtlos Zuschauer:innen für alle Connected-TV-Geräte (CTV) (wie Roku, FireTV, Samsung TV, LG TV usw.) zu gewinnen und zu binden.

_Diese Integration wird von Vizbee gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Vizbee ermöglicht es Ihnen, über eine einzige Konsole Ihre Marketingkampagnen zur Gewinnung und Bindung von Zuschauer:innen in Streaming-Apps sowohl auf mobilen als auch auf CTV-Geräten zu planen. Mit dieser Integration können Sie:
- Eine mobile Benachrichtigung für gezielte Nutzer:innen planen, die beim Antippen entweder die Wiedergabe in der mobilen App starten oder nahtlos die Wiedergabe auf einem nahegelegenen Streaming-Gerät oder Fernseher auslösen kann.
- Eine E-Mail-Marketingkampagne für gezielte Nutzer:innen planen, die beim Antippen zu einer automatischen CTV-App-Installation und Anmeldung der Nutzer:innen auf einem CTV-Gerät wie Roku oder FireTV führen kann.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Vizbee-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Vizbee](https://vizbee.tv/)-Konto erforderlich. Sie müssen Ihre App bei Vizbee Registrierung und eine zugewiesene Vizbee-ID erhalten. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. |
| Vizbee SDK | Zusätzlich zum erforderlichen Braze SDK müssen Sie auch das Vizbee SDK installieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

Folgen Sie der [SDK-Integrationsanleitung](https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity) von Vizbee, um die Integration von Vizbee und Braze einzurichten. Dort finden Sie Anleitungen zum Deeplinking von Mobilgeräten zu Fernsehern, zur Installation von TV-Apps und zur Attribution der Zuschauerzahlen.

### Anzeigen von Installations- und Attributionsberichten {#vizbee-tv-app-installs-viewership-attribution}

Vizbee und Braze ermöglichen es Ihnen außerdem, die ganzheitliche Performance Ihrer Kampagnen über mobile und CTV-Geräte hinweg einzusehen. Das Vizbee SDK sendet angepasste Events an das Braze SDK, die in Ihren Campaign-Berichten im Braze-Dashboard angezeigt werden können.