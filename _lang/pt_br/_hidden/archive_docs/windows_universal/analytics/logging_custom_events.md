---
nav_title: Rastreamento de eventos personalizados
article_title: Rastreamento de eventos personalizados para o Windows Universal
platform: Windows Universal
page_order: 2
description: "Este artigo de referência aborda como rastrear eventos personalizados na plataforma Windows Universal."
hidden: true
---

# Rastreamento de eventos personalizados {#track-custom-events}
{% multi_lang_include archive/windows_deprecation.md %}

Você pode registrar eventos personalizados na Braze para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard. Recomendamos também que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/).

Todos os eventos são registrados usando o `EventLogger`, que é uma propriedade exposta no IAppboy. Para obter uma referência ao `EventLogger`, chame `Appboy.SharedInstance.EventLogger`. Você pode usar os seguintes métodos para rastrear ações importantes do usuário e eventos personalizados:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
