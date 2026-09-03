---
nav_title: Anwendungsfall
article_title: "Anwendungsfall: Entdeckung von Inhalten nach dem Ansehen fördern"
description: "Dieses Beispiel veranschaulicht, wie eine fiktive Marke KI-Artikelempfehlungen von Braze nutzt, um personalisierte Inhalte und Produktempfehlungen in wichtigen Kundenmomenten bereitzustellen."
page_type: tutorial
---

# Anwendungsfall: Entdeckung von Inhalten nach dem Ansehen fördern {#use-case-drive-content-discovery-after-viewing}

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke KI-Artikelempfehlungen von Braze nutzt, um personalisierte Inhalte und Produktempfehlungen in wichtigen Kundenmomenten bereitzustellen. Erfahren Sie, wie Empfehlungslogik das Engagement verbessern, Conversions steigern und den manuellen Aufwand reduzieren kann.

Nehmen wir an, Camila ist CRM-Manager:in bei MovieCanon, einer Streaming-Plattform, die kuratierte Filme und Serien anbietet.

Camilas Ziel ist es, das Engagement der Zuschauer:innen auch nach dem Anschauen eines Inhalts aufrechtzuerhalten. In der Vergangenheit basierten die „Das könnte Ihnen auch gefallen“-Nachrichten von MovieCanon auf einer groben Genre-Zuordnung und wurden zu beliebigen Zeitpunkten versendet – häufig Stunden oder Tage nach einer Sitzung. Das Engagement war gering, und ihr Team war sich bewusst, dass es besser geht.

Mithilfe von [KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai) richtet Camila ein System ein, das automatisch neue Titel basierend auf dem Verlauf jeder Zuschauer:in empfiehlt. Diese Empfehlungen werden unmittelbar nach Beendigung eines Films oder einer Episode zugestellt. Dies ist eine intelligentere und persönlichere Methode, um Nutzer:innen dabei zu helfen, Inhalte zu entdecken, die sie tatsächlich als Nächstes sehen möchten, und sie auf der Plattform zu halten.

![In-App-Nachricht mit dem Text „Als Nächstes, speziell für Sie. Da Sie „Nomads of the Sun“ angesehen haben", mit einem Bild, dem Titelnamen, einer Beschreibung und den CTAs „Jetzt ansehen“ oder „Überspringen“ zur nächsten Empfehlung.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Dieses Tutorial führt Sie durch die Vorgehensweise von Camila:

- Eine personalisierte Nachricht, die ausgelöst wird, wenn eine Nutzer:in das Ansehen eines Inhalts beendet hat
- Empfehlungen, die auf die Präferenzen der Zuschauer:in zugeschnitten sind – automatisch aus dem Katalog von MovieCanon abgerufen und in die Nachricht eingefügt

## 1. Schritt: Empfehlung erstellen {#step-1-create-a-churn-prediction-model}

Camila beginnt damit, eine Empfehlung zu erstellen, die relevante Titel anzeigt, sobald eine Nutzer:in etwas fertig angesehen hat. Sie möchte eine dynamische Lösung, sodass Nutzer:innen verschiedene Vorschläge erhalten, die auf ihren zuletzt angesehenen Inhalten basieren.

1. Im Braze-Dashboard navigiert Camila zu **KI-Artikelempfehlungen**.
2. Sie erstellt eine neue Empfehlung und benennt sie „Vorschläge nach dem Anschauen“.
3. Für den Empfehlungstyp wählt sie **AI Personalized**, sodass jede Nutzer:in auf der Grundlage ihres bisherigen Verhaltens personalisierte Empfehlungen erhält.
4. Sie wählt **Do not recommend items users have previously interacted with**, damit Nutzer:innen keine Empfehlungen für Inhalte erhalten, die sie bereits angesehen haben.
5. Sie wählt den Katalog aus, der die aktuelle Inhaltsbibliothek von MovieCanon enthält. Camila fügt keine Katalogauswahl hinzu, da sie möchte, dass alle Artikel im Katalog für Empfehlungen in Frage kommen.
6. Camila verknüpft die Empfehlung mit dem angepassten Event `Watched Content`, das abgeschlossene Aufrufe nachverfolgt, und legt den **Property Name** auf den Titel des Inhalts fest.
7. Sie erstellt die Empfehlung.

## 2. Schritt: In-App-Nachricht einrichten {#step-2-set-up-an-in-app-message}

Nachdem die Empfehlung trainiert wurde, erstellt Camila einen Messaging-Fluss, der die Nutzer:in zum richtigen Zeitpunkt erreicht: unmittelbar nachdem sie einen Titel abgeschlossen hat. Die Nachricht enthält eine Liste mit drei personalisierten Vorschlägen, die direkt aus dem Katalog stammen.

1. Camila erstellt eine In-App-Nachricht-Campaign mithilfe des Drag-and-Drop-Editors.
2. Sie stellt den Auslöser auf ihr angepasstes Event ein: `Watched Content`.
3. Sie entwirft eine mehrseitige In-App-Nachricht mit Titelbildern, Namen und einem CTA „Jetzt ansehen“.

![Modal „Personalisierung hinzufügen“ im Braze-Editor geöffnet, mit „Artikelempfehlung“ als ausgewähltem Personalisierungstyp.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. Im Nachrichtentext verwendet Camila das [Modal „Personalisierung hinzufügen“]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-pre-formatted-variables), um Variablen wie den Namen, die Beschreibung und die Miniaturansicht des empfohlenen Titels mithilfe von Liquid hinzuzufügen, wodurch Inhalte aus dem Katalog dynamisch eingefügt werden. Sie erstellt ein Template mit einem angepassten Attribut für `Last Watched Movie`, um Nutzer:innen darüber zu informieren, dass diese Empfehlung auf ihrem Verlauf basiert.

![In-App-Nachrichteneditor mit unverarbeitetem Liquid zur Erstellung von Templates in bestimmten Feldern aus Katalogartikeln aus der Empfehlung.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Verwendetes Liquid im Bild anzeigen %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. Anschließend dupliziert Camila ihre Seite und erhöht das Liquid-Array {% raw %} (`{{ items[0]}}` zu `{{items[1]}}`) {% endraw %} in jeder Variablen, um das nächste Element in der Empfehlungsliste in das Template einzufügen.

## 3. Schritt: Messen und optimieren {#step-3-measure-and-optimize}

Während die Campaign läuft, überwacht Camila die Öffnungsraten, Klickraten und das nachfolgende Betrachtungsverhalten. Sie vergleicht die Performance mit früheren statischen Empfehlungs-Campaigns und stellt ein höheres Engagement sowie mehr Content-Sitzungen pro Nutzer:in fest.

Sie plant außerdem einen A/B-Test:

- Zeitpunkt (unmittelbar nach dem Betrachten versus 10 Minuten danach)
- Inhaltslayout (Karussell versus Liste)
- CTA-Varianten („Jetzt ansehen“ versus „Zur Warteschlange hinzufügen“)

Durch die Kombination von ereignisgesteuerten Nachrichten mit KI-Artikelempfehlungen verwandelt Camila die Entdeckung von Inhalten in ein automatisches, personalisiertes Erlebnis. MovieCanon sorgt dafür, dass Nutzer:innen ohne Spekulationen engagiert bleiben – indem relevante Inhalte zum richtigen Zeitpunkt bereitgestellt werden, um die Sitzungstiefe zu erhöhen und Churn zu verringern.