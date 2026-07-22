---
page_order: 2.2
nav_title: Content Cards
article_title: Content Cards im Braze SDK
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards {#content-cards}

> Erfahren Sie mehr über Content Cards für das Braze SDK, einschließlich der verschiedenen Datenmodelle und kartenspezifischen Eigenschaften, die für Ihre Anwendung verfügbar sind.

{% multi_lang_include banners/content_card_alert.md %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/content_cards.md %}
{% endsdktab %}

{% sdktab android %}
## Voraussetzungen {#prerequisites}

Bevor Sie Braze Content Cards verwenden können, müssen Sie das [Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) in Ihre App integrieren. Es ist jedoch kein zusätzliches Setup erforderlich.

## Google Fragments {#google-fragments}

In Android wird der Content-Cards-Feed als [Fragment](https://developer.android.com/guide/components/fragments.html) implementiert, das im Braze Android UI-Projekt verfügbar ist. Die Klasse [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) aktualisiert und zeigt automatisch den Inhalt der Content Cards an und protokolliert Nutzungsanalysen. Die Karten, die im `ContentCards`-Feed von Nutzer:innen erscheinen können, werden im Braze-Dashboard erstellt.

Informationen zum Hinzufügen eines Fragments zu einer Activity finden Sie in der [Google-Dokumentation zu Fragments](https://developer.android.com/guide/fragments#Adding).

## Kartentypen und Eigenschaften {#card-types-and-properties}

Das Content-Cards-Datenmodell ist im Android SDK verfügbar und bietet die folgenden einzigartigen Content-Card-Typen. Jeder Typ teilt ein Basismodell, das es ihnen ermöglicht, gemeinsame Eigenschaften vom Basismodell zu erben und zusätzlich eigene spezifische Eigenschaften zu besitzen. Die vollständige Referenzdokumentation finden Sie unter [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Basis-Kartenmodell {#base-card-for-android}

Das [Basis-Kartenmodell](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) bietet grundlegendes Verhalten für alle Karten.

| Eigenschaft | Beschreibung |
|---|---|
| `getId()` | Gibt die von Braze festgelegte Karten-ID zurück.|
| `getViewed()` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte von den Nutzer:innen gelesen oder ungelesen ist.|
| `getExtras()` | Gibt eine Map mit Schlüssel-Wert-Extras für diese Karte zurück.|
| `getCreated()` | Gibt den Unix-Zeitstempel der Erstellungszeit der Karte von Braze zurück.|
| `isPinned` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte angepinnt ist.|
| `getOpenUriInWebView()` | Gibt einen booleschen Wert zurück, der angibt, ob URIs für diese Karte <br> im Braze WebView geöffnet werden sollen oder nicht.|
| `getExpiredAt()` | Gibt das Ablaufdatum der Karte zurück.|
| `isRemoved()` | Gibt einen booleschen Wert zurück, der angibt, ob die Endnutzer:innen diese Karte verworfen haben.|
| `isDismissibleByUser()` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte von den Nutzer:innen geschlossen werden kann.|
| `isClicked()` | Gibt einen booleschen Wert zurück, der den Klickstatus dieser Karte widerspiegelt.|
| `isDismissed` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte geschlossen wurde. Setzen Sie den Wert auf `true`, um die Karte als geschlossen zu markieren. Wenn eine Karte bereits als geschlossen markiert ist, kann sie nicht erneut als geschlossen markiert werden.|
| `isControl()` | Gibt einen booleschen Wert zurück, wenn diese Karte eine Kontrollkarte ist und nicht gerendert werden soll.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Basis-Kartenmodell" }

### Nur Bild {#banner-image-card-for-android}

[Nur-Bild-Karten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) sind klickbare, vollformatige Bilder.

| Eigenschaft | Beschreibung |
|---|---|
| `getImageUrl()` | Gibt die URL des Kartenbilds zurück.|
| `getUrl()` | Gibt die URL zurück, die nach dem Klicken auf die Karte geöffnet wird. Es kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
| `getDomain()` | Gibt den Linktext für die Eigenschafts-URL zurück.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nur Bild" }

### Bild mit Beschriftung {#captioned-image-card-for-android}

[Karten mit beschriftetem Bild](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sind klickbare, vollformatige Bilder mit begleitendem Beschreibungstext.

| Eigenschaft | Beschreibung |
|---|---|
| `getImageUrl()` | Gibt die URL des Kartenbilds zurück.|
| `getTitle()` | Gibt den Titeltext der Karte zurück.|
| `getDescription()` | Gibt den Textkörper der Karte zurück.|
| `getUrl()` | Gibt die URL zurück, die nach dem Klicken auf die Karte geöffnet wird. Es kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
| `getDomain()` | Gibt den Linktext für die Eigenschafts-URL zurück. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bild mit Beschriftung" }

### Klassisch {#text-Announcement-card-for-android}

Eine klassische Karte ohne Bild ergibt eine [Textankündigungskarte](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Wenn ein Bild enthalten ist, erhalten Sie eine [Kurznachrichtenkarte](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

| Eigenschaft | Beschreibung |
|---|---|
| `getTitle()` | Gibt den Titeltext der Karte zurück. |
| `getDescription()` | Gibt den Textkörper der Karte zurück. |
| `getUrl()` | Gibt die URL zurück, die nach dem Klicken auf die Karte geöffnet wird. Es kann eine HTTP(s)-URL oder eine Protokoll-URL sein. |
| `getDomain()` | Gibt den Linktext für die Eigenschafts-URL zurück. |
| `getImageUrl()` | Gibt die URL des Kartenbilds zurück, gilt nur für die klassische Kurznachrichtenkarte. |
| `isDismissed` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte geschlossen wurde. Setzen Sie den Wert auf `true`, um die Karte als geschlossen zu markieren. Wenn eine Karte bereits als geschlossen markiert ist, kann sie nicht erneut als geschlossen markiert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klassisch" }

## Kartenmethoden {#card-methods}

Alle [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)-Datenmodellobjekte bieten die folgenden Analytics-Methoden zum Protokollieren von Nutzerereignissen an Braze-Server.

| Methode | Beschreibung |
|---|---|
| `logImpression()` | Protokolliert manuell eine Impression bei Braze für eine bestimmte Karte. |
| `logClick()` | Protokolliert manuell einen Klick bei Braze für eine bestimmte Karte. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kartenmethoden" }

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/content_cards.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/content_cards.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/content_cards.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/content_cards.md %}
{% endsdktab %}

{% sdktab tvos %}
## Voraussetzungen

Bevor Sie Content Cards verwenden können, integrieren Sie das [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) in Ihre App. Führen Sie dann die Schritte zur Einrichtung Ihrer tvOS-App aus.

{% alert important %}
Implementieren Sie Ihre eigene angepasste UI, da Content Cards über eine Headless-UI mit dem Swift SDK unterstützt werden&#8212;das keine Standard-UI oder Views für tvOS enthält.
{% endalert %}

## Einrichtung Ihrer tvOS-App {#setting-up-your-tvos-app}

### Schritt 1: Neue iOS-App erstellen {#step-1-create-a-new-ios-app}

Wählen Sie in Braze **Settings** > **App Settings** und dann **Add App**. Geben Sie einen Namen für Ihre tvOS-App ein, wählen Sie **iOS**&#8212;_nicht tvOS_&#8212;und dann **Add App**.

![Dialog „App hinzufügen“ in Braze mit ausgewählter iOS-Plattform zur Registrierung einer tvOS-App.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Wenn Sie das Kontrollkästchen **tvOS** aktivieren, können Sie Content Cards für tvOS nicht anpassen.
{% endalert %}

### Schritt 2: API-Schlüssel Ihrer App abrufen {#step-2-get-your-apps-api-key}

Wählen Sie in Ihren App-Einstellungen Ihre neue tvOS-App aus und notieren Sie sich den API-Schlüssel Ihrer App. Verwenden Sie diesen Schlüssel, um Ihre App in Xcode zu konfigurieren.

![App-Einstellungen für eine tvOS-App mit dem API-Schlüssel für die SDK-Integration.]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Schritt 3: BrazeKit integrieren {#step-3-integrate-brazekit}

Verwenden Sie den API-Schlüssel Ihrer App, um das [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) in Ihr tvOS-Projekt in Xcode zu integrieren. Sie müssen nur BrazeKit aus dem Braze Swift SDK integrieren.

### Schritt 4: Eigene UI erstellen {#step-4-create-your-custom-ui}

Da Braze keine Standard-UI für Content Cards auf tvOS bereitstellt, passen Sie diese selbst an. Eine vollständige Anleitung finden Sie in unserem Schritt-für-Schritt-Tutorial: [Content Cards für tvOS anpassen](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). Ein Beispielprojekt finden Sie unter [Braze Swift SDK Beispiele](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}