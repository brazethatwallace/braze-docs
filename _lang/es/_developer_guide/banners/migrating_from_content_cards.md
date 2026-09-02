---
nav_title: "Migrar desde Content Cards"
article_title: "Migrar de Content Cards a banners"
description: "Aprende a realizar la migración de Content Cards a banners, incluyendo ejemplos de código para todos los SDK or kit de desarrollo de software compatibles, limitaciones y ventajas."
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Migrar de Content Cards a banners {#migrate-from-content-cards-to-banners}

> Esta guía te ayuda en la migración de Content Cards a banners para casos de uso de mensajería tipo banner. Los banners son ideales para mensajes en línea, persistentes dentro de la aplicación y en la Web que aparecen en ubicaciones específicas de tu aplicación.

## ¿Por qué migrar a Banners? {#why-migrate-to-banners}

- Si tu equipo de ingeniería está construyendo o manteniendo Content Cards personalizadas, migrar a Banners puede reducir esa inversión continua. Banners permite a los especialistas en marketing controlar la interfaz de usuario directamente, liberando a los desarrolladores para otro trabajo.
- Si estás lanzando nuevos mensajes en la página de inicio, flujos de incorporación o anuncios persistentes, comienza con Banners en lugar de construir sobre Content Cards. Puedes beneficiarte de la personalización en tiempo real, sin expiración de 30 días, sin límite de tamaño y priorización nativa desde el primer día.
- Si estás buscando soluciones alternativas al límite de expiración de 30 días, gestionando lógica compleja de reelegibilidad o frustrado por la personalización obsoleta, Banners resuelve estos problemas de forma nativa.

Banners ofrece varias ventajas sobre Content Cards para mensajería de tipo banner:

### Producción acelerada {#accelerated-production}

- **Menor soporte de ingeniería continuo requerido**: Los especialistas en marketing pueden crear mensajes personalizados usando un editor de arrastrar y soltar y HTML personalizado sin necesidad de asistencia del desarrollador para la personalización.
- **Opciones de personalización flexibles**: Diseña directamente en el editor, usa HTML o aprovecha modelos de datos existentes con propiedades personalizadas.

### Mejor experiencia de usuario {#better-ux}

- **Actualizaciones de contenido dinámico**: Banners actualiza la lógica Liquid y la elegibilidad en cada actualización, asegurando que los usuarios siempre vean el contenido más relevante.
- **Soporte nativo de ubicación**: Los mensajes aparecen en contextos específicos en lugar de una fuente, proporcionando mejor relevancia contextual.
- **Priorización nativa**: Control sobre el orden de visualización sin lógica personalizada, lo que facilita la gestión de la jerarquía de mensajes.

### Persistencia {#persistence}

- **Sin límite de expiración**: Las Campaigns de Banners no tienen un límite de expiración de 30 días como Content Cards, lo que permite una verdadera persistencia de los mensajes.

## Cuándo migrar {#when-to-migrate}

Considera migrar a Banners si estás usando Content Cards para:

- Héroes de página de inicio, promociones de páginas de producto, ofertas en el proceso de pago
- Anuncios persistentes de navegación o mensajes en la barra lateral
- Mensajes siempre activos que se ejecutan durante más de 30 días
- Mensajes en los que deseas personalización y elegibilidad en tiempo real

## Cuándo seguir usando Content Cards {#when-to-keep-content-cards}

Sigue usando Content Cards si necesitas:

- **Experiencias de fuente:** Cualquier ejemplo que implique múltiples mensajes desplazables o un "buzón de entrada" basado en tarjetas.
- **Características específicas:** Mensajes que requieren códigos promocionales, ya que los banners no los admiten de forma nativa. Los banners admiten [contenido conectado]({{site.baseurl}}/developer_guide/banners#connected-content) en acceso anticipado.
- **Entrega desencadenada:** Ejemplos que requieren estrictamente entrega activada por API o entrega basada en acciones. Aunque los banners no admiten la entrega activada por API ni la entrega basada en acciones, la evaluación de elegibilidad en tiempo real significa que los usuarios califican o dejan de calificar instantáneamente en función de la pertenencia a un segmento en cada actualización.

## Guía de migración {#migration-guide}

### Requisitos previos {#prerequisites}

Antes de migrar, asegúrate de que tu SDK or kit de desarrollo de software de Braze cumple con los requisitos mínimos de versión:

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

Los descartes y la reelegibilidad requieren las siguientes versiones mínimas del SDK or kit de desarrollo de software:

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### Suscribirse a actualizaciones {#subscribe-to-updates}

#### Enfoque de Content Cards {#content-cards-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### Enfoque de banners {#banners-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("sample_placement_id").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### Mostrar contenido {#display-content}

{% alert note %}
Las Content Cards se pueden renderizar manualmente con lógica de interfaz personalizada, mientras que los banners solo se pueden renderizar con los métodos del SDK or kit de desarrollo de software incluidos de serie.
{% endalert %}

#### Enfoque de Content Cards

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getCachedContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### Enfoque de banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### Registrar análisis (implementaciones personalizadas) {#log-analytics-custom-implementations}

{% alert note %}
Tanto Content Cards como los banners rastrean análisis automáticamente cuando se utilizan sus componentes de interfaz predeterminados. Los siguientes ejemplos son para implementaciones personalizadas en las que construyes tu propia interfaz.
{% endalert %}

#### Enfoque de Content Cards

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
  card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
  card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
  braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### Enfoque de banners

{% tabs %}
{% tab Web %}

{% alert important %}
Los análisis se rastrean automáticamente cuando se usa `insertBanner()`. No se debe usar el registro manual cuando se utiliza `insertBanner()`.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
Los análisis se rastrean automáticamente cuando se usa BannerView. No se debe usar el registro manual cuando se utiliza BannerView.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
Los análisis se rastrean automáticamente cuando se usa BannerUIView. No se debe usar el registro manual para el BannerUIView predeterminado.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
Los análisis se rastrean automáticamente cuando se usa BrazeBannerView. No se requiere registro manual.
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
Los análisis se rastrean automáticamente cuando se usa BrazeBannerView. No se requiere registro manual.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Obtener propiedades {#getting-properties}

#### Enfoque de Content Cards

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### Enfoque de banners

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### Gestión de grupos de control {#handling-control-groups}

#### Enfoque de Content Cards

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### Enfoque de banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## Limitaciones {#limitations}

Al migrar de Content Cards a Banners, ten en cuenta las siguientes limitaciones:

### Migración de mensajes desencadenados {#migrating-triggered-messages}

Los Banners solo admiten Campaigns de entrega programada. Para migrar un mensaje que anteriormente se activaba mediante API o era basado en acciones, conviértelo a segmentación basada en Segment:

- **Ejemplo:** En lugar de desencadenar una tarjeta "Completar perfil" con la API, crea un Segment para usuarios que se registraron en los últimos 7 días pero no han completado su perfil.
- **Elegibilidad en tiempo real:** Los usuarios califican o dejan de calificar para el Banner instantáneamente en cada actualización según su pertenencia al Segment.

### Diferencias de características {#feature-differences}

| Característica | Content Cards | Banners |
|---------|--------------|---------|
| **Estructura de contenido** |
| Múltiples tarjetas en la fuente | ✅ Compatible | ✅ Puedes crear múltiples ubicaciones para lograr una implementación tipo carrusel. Solo se devuelve un banner por ubicación. |
| Múltiples ubicaciones | N/A | ✅ Múltiples ubicaciones compatibles |
| Tipos de tarjeta (Clásica, Con subtítulo, Solo imagen) | ✅ Múltiples tipos predefinidos | ✅ Un solo banner basado en HTML (más flexible) |
| **Gestión de contenido** |
| Editor de arrastrar y soltar | ❌ Requiere un desarrollador para la personalización | ✅ Los especialistas en marketing pueden crear/actualizar sin ingeniería |
| HTML/CSS personalizado | ❌ Limitado a la estructura de la tarjeta | ✅ Compatibilidad total con HTML/CSS |
| Pares clave-valor para personalización | ✅ Necesarios para personalización avanzada | ✅ Pares clave-valor fuertemente tipados llamados "propiedades" para personalización avanzada |
| Extras de mensaje | ✅ Compatible | ❌ No compatible actualmente |
| **Persistencia y expiración** |
| Expiración de tarjeta | ✅ Compatible (límite de 30 días) | ✅ Compatible (sin límite de expiración) |
| Persistencia real | ❌ Máximo de 30 días | ✅ Persistencia ilimitada |
| **Visualización y segmentación** |
| Interfaz de fuente | ✅ Fuente predeterminada disponible | ❌ Solo basado en ubicaciones |
| Ubicación contextual específica | ❌ Basado en fuente | ✅ Compatibilidad nativa con ubicaciones |
| Priorización | ❌ Requiere lógica personalizada | ✅ Priorización nativa |
| **Interacción del usuario** |
| Descarte manual | ✅ Compatible | ✅ Compatible |
| Reelegibilidad después del descarte | ❌ Requiere filtros personalizados o lógica de Campaign | ✅ Período de espera predeterminado |
| Tarjetas ancladas | ✅ Compatible | N/A |
| **Análisis** |
| Análisis automáticos (interfaz predeterminada) | ✅ Compatible | ✅ Compatible |
| Ordenación por prioridad | ❌ No compatible | ✅ Compatible |
| **Actualizaciones de contenido** |
| Actualización de plantillas Liquid | ❌ Una vez por tarjeta al enviar/lanzar | ✅ Se actualiza en cada actualización |
| Actualización de elegibilidad | ❌ Una vez por tarjeta al enviar/lanzar | ✅ Se actualiza en cada sesión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Diferencias de características" }

### Limitaciones del producto {#product-limitations}

- Hasta 25 mensajes activos por ubicación.
- Hasta 10 ID de ubicación por solicitud de actualización; las solicitudes que superen este límite se truncan.

### Limitaciones del SDK or kit de desarrollo de software {#sdk-limitations}

- Los Banners no son compatibles actualmente con .NET MAUI (Xamarin), Cordova, Unity, Vega ni plataformas de TV.
- Asegúrate de que estás utilizando las versiones mínimas del SDK or kit de desarrollo de software indicadas en los requisitos previos.

## Artículos relacionados {#related-articles}

- [Ubicaciones de banners]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutorial: Mostrar un banner por ID de ubicación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Análisis de banners]({{site.baseurl}}/developer_guide/banners/analytics)
- [Preguntas frecuentes sobre banners]({{site.baseurl}}/developer_guide/banners/faq)