## Über .NET MAUI Content Cards {#about-net-maui-content-cards}

Das Braze .NET MAUI (ehemals Xamarin) SDK enthält einen Standard-Karten-Feed, der Ihnen den Einstieg in Content Cards erleichtert. Der im Braze SDK enthaltene Standard-Kartenfeed verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content Cards von Nutzer:innen.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Kartentypen und Eigenschaften {#card-types-and-properties}

Das Braze .NET MAUI SDK verfügt über drei eigene Content-Card-Kartentypen, die ein Basismodell gemeinsam haben: [Banner](#xamarin_banner), [Bild mit Bildunterschrift](#xamarin_captioned-image) und [Klassisch](#xamarin_classic). Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell und hat die folgenden zusätzlichen Eigenschaften.

### Basis-Kartenmodell {#base-card-model}

| Eigenschaft | Beschreibung |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| `idString` | Die von Braze festgelegte ID der Karte. |
| `created` | Der Unix-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `expiresAt` | Der Unix-Zeitstempel des Verfallszeitpunkts der Karte. Wenn der Wert kleiner als 0 ist, bedeutet dies, dass die Karte nie abläuft. |
| `viewed` | Ob die Karte von Nutzer:innen gelesen oder ungelesen ist. Damit werden keine Analytics protokolliert. |
| `clicked` | Ob die Karte von Nutzer:innen angeklickt wurde. |
| `pinned` | Ob die Karte angeheftet ist. |
| `dismissed` | Ob Nutzer:innen diese Karte ausgeblendet haben. Eine bereits ausgeblendete Karte erneut als ausgeblendet zu markieren, ist ein No-op. |
| `dismissible` | Ob die Karte von Nutzer:innen ausgeblendet werden kann. |
| `urlString` | (Optional) Der URL-String, der mit der Kartenklick-Aktion verknüpft ist. |
| `openUrlInWebView` | Ob die URLs für diese Karte in der Braze WebView geöffnet werden sollen oder nicht. |
| `isControlCard` | Ob diese Karte eine Kontrollkarte ist. Kontrollkarten sollten Nutzer:innen nicht angezeigt werden. |
| `extras` | Die Map der Key-Value-Extras für diese Karte. |
| `isTest` | Ob diese Karte eine Testkarte ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Basis-Kartenmodell" }

Eine vollständige Referenz der Basiskarte finden Sie in der [Android-](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) und [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Banner

Bannerkarten sind anklickbare Bilder in voller Größe.

| Eigenschaft | Beschreibung |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | Die URL des Bildes der Karte. |
| `imageAspectRatio` | Das Seitenverhältnis des Bildes der Karte. Es dient als Hinweis, bevor der Ladevorgang des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Banner" }

Eine vollständige Referenz der Bannerkarte finden Sie in der Dokumentation für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (jetzt umbenannt in „Nur Bild“).

### Bild mit Bildunterschrift {#captioned-image}

Karten mit Bildunterschrift sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

| Eigenschaft | Beschreibung |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | Die URL des Bildes der Karte. |
| `imageAspectRatio` | Das Seitenverhältnis des Bildes der Karte. Es dient als Hinweis, bevor der Ladevorgang des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
| `title` | Der Titeltext für die Karte. |
| `cardDescription` | Der Beschreibungstext für die Karte. |
| `domain` | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Er kann auf der UI der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bild mit Bildunterschrift" }

Eine vollständige Referenz zu Karten des Typs „Bild mit Bildunterschrift“ finden Sie in der [Android-](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) und [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Klassisch {#classic}

Klassische Karten haben einen Titel, eine Beschreibung und ein optionales Bild vor dem Text.

| Eigenschaft | Beschreibung |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | (Optional) Die URL des Bildes der Karte. |
| `title` | Der Titeltext für die Karte. |
| `cardDescription` | Der Beschreibungstext für die Karte. |
| `domain` | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Er kann auf der UI der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klassisch" }

Eine vollständige Referenz der klassischen Content-Card (Textankündigung) finden Sie in der Dokumentation für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Eine vollständige Referenz der klassischen Bildkarte (Kurznachrichten) finden Sie in der Dokumentation für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Karten-Methoden {#card-methods}

Mit diesen zusätzlichen Methoden können Sie einen angepassten Content-Card-Feed in Ihrer App erstellen:

| Methode | Beschreibung |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()` | Fordert die neuesten Content Cards vom Braze SDK-Server an. |
| `getContentCards()` | Ruft Content Cards aus dem Braze SDK ab. Dies gibt die neueste Liste der Karten vom Server zurück. |
| `logContentCardClicked(cardId)` | Protokolliert einen Klick für die angegebene Content-Card-ID. Diese Methode wird nur zu Analytics-Zwecken verwendet. |
| `logContentCardImpression(cardId)` | Protokolliert eine Impression für die angegebene Content-Card-ID. |
| `logContentCardDismissed(cardId)` | Protokolliert eine Ausblendung für die angegebene Content-Card-ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Karten-Methoden" }