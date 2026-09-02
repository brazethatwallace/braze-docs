---
nav_title: Multi-Domain-Integration
article_title: Multi-Domain-Integration für das Braze Web SDK or Software-Development-Kit
platform: Web
page_order: 23
page_type: reference
description: "Erfahren Sie, wie Sie das Braze Web SDK or Software-Development-Kit über mehrere Domains hinweg implementieren, einschließlich API-Schlüssel-Strategie, Push-Einrichtung und Session-Verhalten."
---

# Multi-Domain-Integration {#multi-domain-integration}

> Erfahren Sie, wie Sie das Braze Web SDK or Software-Development-Kit über mehrere Web-Domains hinweg integrieren.

Wenn Ihre Implementierung mehrere Domains umfasst, beeinflussen Browser-Origin-Grenzen, wie das Braze Web SDK or Software-Development-Kit den Nutzerstatus speichert und liest.

## App- und API-Schlüssel-Strategie wählen {#choose-an-app-and-api-key-strategy}

Sie können einen Web-SDK or Software-Development-Kit-API-Schlüssel über mehrere Domains hinweg verwenden, aber in den meisten Fällen bieten separate API-Schlüssel, die separaten Apps im selben Workspace zugeordnet sind, eine bessere Kontrolle.

| Strategie | Empfohlen, wenn | Kompromisse |
|---|---|---|
| **Separate Apps (empfohlen)** | Sie unabhängiges Targeting, Reporting und Campaign-Steuerung pro Domain wünschen | Erfordert die Verwaltung von zwei App-Integrationen |
| **Einzelne App** | Sie beide Domains operativ als eine Einheit behandeln | Session-Trigger or triggern und Reporting auf Domain-Ebene sind schwieriger zu trennen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Optionen für App- und API-Schlüssel-Strategien" }

Mit separaten Apps in einem Workspace können Sie App-Filter für eine sauberere Segmentierung und Nachrichten-Targeting nach Domain verwenden.

## Push-Benachrichtigungen auf einer Domain konfigurieren {#configure-push-notifications-on-one-domain}

Bei separaten Root-Domains ist die Web-Push-Registrierung pro Domain isoliert.

- Wählen Sie eine Domain als Ihre Push-Benachrichtigungs-Domain.
- Registrierung or registrieren Sie Push nicht auf beiden Root-Domains für dieselbe User Journey, da dies zu widersprüchlichem Prompt- und Abo-Verhalten führen kann.

## Nutzer:innen konsistent über Domains hinweg identifizieren {#identify-users-consistently-across-domains}

Standardmäßig speichert jede Root-Domain ihren eigenen SDK or Software-Development-Kit-Status. Um Aktivitäten demselben Braze-Kundenprofil or Nutzerprofil über Domains hinweg zuzuordnen:

- Rufen Sie [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) mit derselben `external_id` auf jeder Domain nach der Anmeldung auf.
- Behalten Sie beide Apps im selben Workspace, wenn Sie separate API-Schlüssel verwenden.

Allgemeine Hinweise zu Nutzer-IDs finden Sie unter [Nutzer-IDs über das Braze SDK or Software-Development-Kit festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## Event- und Trigger or triggern-Verhalten nach Domain planen {#plan-event-and-trigger-behavior-by-domain}

Wie Sie Events und Trigger or triggern modellieren, hängt von Ihrer App-Strategie ab:

- **Einzelne App über Domains hinweg:** Protokollieren Sie domainspezifische angepasste Events, damit Sie das Verhalten nach Website in der Segmentierung und beim Trigger or triggern or triggern unterscheiden können.
- **Separate Apps:** Bevorzugen Sie App-Filter für domainspezifisches Targeting und Analytics.

## Session-Verhalten über Domains hinweg verstehen {#understand-session-behavior-across-domains}

Standardmäßig beträgt das Session-Timeout des Web SDK or Software-Development-Kit 30 Minuten Inaktivität. Bei separaten Root-Domains mit einem App-/API-Schlüssel:

- Jede Domain startet und beendet Sessions unabhängig.
- Nutzer:innen, die zwischen beiden Domains wechseln, können überlappende Sessions erzeugen.
- Session-Start-Trigger or triggern können auf beiden Domains ausgelöst werden.

Grundlegende Details zum Session-Lebenszyklus finden Sie unter [Sessions über das Braze SDK or Software-Development-Kit tracken]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).