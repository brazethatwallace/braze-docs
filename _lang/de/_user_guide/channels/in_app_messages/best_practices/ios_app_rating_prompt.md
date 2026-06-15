---
nav_title: In-App-Bewertungsaufforderung für iOS
article_title: In-App-Bewertungsaufforderung für iOS
page_order: 6
description: "Dieser Artikel beschreibt Ansätze und Auswirkungen der Verwendung von Braze, um Nutzer:innen zu bitten, Ihre App zu bewerten."
channel:
  - in-app messages

---

# In-App-Bewertungsaufforderung für iOS {#in-app-rating-prompt-for-ios}

> Dieser Artikel beschreibt Ansätze und Auswirkungen der Verwendung von Braze, um Nutzer:innen zu bitten, Ihre App zu bewerten. Tipps für eine effektive App-Bewertungs-Campaign finden Sie unter [Die Dos und Don'ts von Kund:innen-App-Bewertungen](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

Apple bietet eine native Aufforderung an, die mit iOS 10.3 eingeführt wurde und es Nutzer:innen ermöglicht, Apps direkt innerhalb der App zu bewerten. Wenn Sie App-Bewertungen von Nutzer:innen über eine In-App-Nachricht auf iOS anfordern möchten, müssen Sie die native Aufforderung verwenden, da Apple benutzerdefinierte Bewertungsaufforderungen untersagt (siehe [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), Abschnitt 5.6.1).

Gemäß den Apple-Richtlinien können App-Bewertungsaufforderungen Nutzer:innen bis zu dreimal pro Jahr angezeigt werden, daher sollten App-Bewertungs-Campaigns [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) nutzen. Nutzer:innen können auch in ihren App-Einstellungen die Anzeige von App-Bewertungsaufforderungen vollständig deaktivieren. Weitere Informationen zu App-Store-Bewertungen finden Sie in Apples Artikel zu [Ratings, Reviews, and Responses](https://developer.apple.com/app-store/ratings-and-reviews/).

## Braze verwenden, um Nutzer:innen um App-Bewertungen zu bitten {#using-braze-to-ask-users-for-app-reviews}

Obwohl Apple die Verwendung der nativen Aufforderung vorschreibt, können Sie dennoch Braze-Campaigns nutzen, um Nutzer:innen zum richtigen Zeitpunkt zu bitten, Ihre App zu bewerten und eine Rezension zu schreiben. Es gibt zwei Hauptansätze, die Sie verfolgen können.

### Ansatz 1: Deeplinking zum App Store {#approach-1-deep-linking-to-the-app-store}

Bei diesem Ansatz möchten Sie Nutzer:innen ermutigen, den App Store zu besuchen, um eine Bewertung abzugeben. Erstellen Sie dazu eine In-App-Nachrichten-Campaign, die einen [Deeplink]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) zum App Store enthält.

![Zwei mobile Bildschirme nebeneinander. Der erste zeigt eine In-App-Nachricht, die Nutzer:innen bittet, die App im App Store zu bewerten. Der zweite zeigt die iOS-App-Store-Seite für diese App.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Ansatz 2: Sanftes Vorbereiten {#approach-2-soft-priming}

Wenn Sie nicht möchten, dass Nutzer:innen Ihre App verlassen, können Sie sie zunächst mit einer separaten In-App-Nachricht vorbereiten. Dieses Vorbereiten ist eine Methode, Nutzer:innen um Erlaubnis zu bitten, bevor Sie ihnen die native App-Store-Bewertungsaufforderung senden. Erstellen Sie dazu eine In-App-Nachrichten-Campaign und fügen Sie einen angepassten Deeplink hinzu, der beim Klicken die `requestReview`-Methode aufruft.

Detaillierte Schritte finden Sie unter [Angepasste App-Store-Bewertungsaufforderung]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt).

![Zwei In-App-Nachrichten nebeneinander. Die erste bereitet Nutzer:innen auf die Bewertung der App vor, indem sie fragt, ob sie einen Moment Zeit haben, die App zu bewerten. Die zweite ist die native iOS-App-Store-Bewertungsnachricht, die eine Skala von fünf Sternen anzeigt, die Nutzer:innen auswählen können, um die App zu bewerten.]({% image_buster /assets/img_archive/prime_app_review.png %})

Nutzer:innen geben eine Bewertung über die native App-Store-Bewertungsaufforderung ab und können eine Rezension schreiben und einreichen, ohne die App zu verlassen.

### Überlegungen {#considerations}

Als Alternative zum sanften Vorbereiten könnten Sie die iOS-App-Bewertungsaufforderung auch direkt anzeigen, ohne vorher eine Braze-Vorbereitungsnachricht einzublenden. Der Vorteil dabei ist: Wenn Nutzer:innen App-Bewertungsaufforderungen deaktiviert haben, entsteht nicht die suboptimale Nutzererfahrung, dass sie versuchen, die App zu bewerten, aber keine Aufforderung dafür erscheint.

{% alert important %}
Erstellen Sie keine angepassten HTML-In-App-Nachrichten, die eine native iOS-App-Bewertungsaufforderung imitieren, da dies gegen die Apple-Richtlinien verstößt.
{% endalert %}