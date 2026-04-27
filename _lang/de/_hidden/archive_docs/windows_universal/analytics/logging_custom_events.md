---
nav_title: Tracking angepasster Events
article_title: Tracking angepasster Events für Windows Universal
platform: Windows Universal
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Events auf der Windows Universal Plattform tracken können."
hidden: true
---

# Tracking angepasster Events {#track-custom-events}
{% multi_lang_include archive/windows_deprecation.md %}

Sie können angepasste Events in Braze aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Nutzer:innen anhand ihrer Aktionen im Dashboard zu segmentieren. Wir empfehlen Ihnen außerdem, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/) vertraut zu machen.

Alle Events werden mithilfe des `EventLogger` protokolliert, einer Eigenschaft, die in IAppboy bereitgestellt wird. Um eine Referenz auf den `EventLogger` zu erhalten, rufen Sie `Appboy.SharedInstance.EventLogger` auf. Sie können die folgenden Methoden verwenden, um wichtige Nutzer:innen-Aktionen und angepasste Events zu verfolgen:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
