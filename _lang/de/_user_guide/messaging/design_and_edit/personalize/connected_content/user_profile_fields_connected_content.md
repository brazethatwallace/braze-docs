---
nav_title: Abrufen von Nutzerprofildaten
article_title: Nutzerprofildaten in Connected-Content-Aufrufen abrufen
page_order: 3
description: "Dieser Artikel beschreibt, wie Sie Nutzerprofile in Ihre Connected-Content-Aufrufe einbinden und welche Best Practices für Liquid-Templating gelten."
toc_headers: h2
---

# Nutzerprofildaten in Connected-Content-Aufrufen abrufen {#pull-user-profile-data-in-connected-content-calls}

> Auf dieser Seite erfahren Sie, wie Sie Nutzerprofile in Ihre Connected-Content-Aufrufe einbinden und welche Best Practices für Liquid-Templating gelten.

## Voraussetzungen {#prerequisites}

Wenn eine Connected-Content-Antwort Nutzerprofilfelder enthält (innerhalb eines Liquid-Personalisierungs-Tags), müssen diese Werte zuvor in der Nachricht mit Liquid definiert werden – und zwar vor dem Connected-Content-Aufruf –, damit der Liquid-Passback korrekt dargestellt wird. Ebenso muss das `:rerender`-Flag in der Anfrage enthalten sein. Beachten Sie, dass das `:rerender`-Flag nur eine Ebene tief wirkt, d. h. es wird nicht auf verschachtelte Connected-Content-Tags angewendet.

## Liquid-Templating in Connected-Content-Aufrufen {#liquid-templating-in-connected-content-calls}

Für die Personalisierung ruft Braze Nutzerprofilfelder ab, bevor dieses Feld an Liquid übergeben wird. Wenn die Antwort von Connected Content also Nutzerprofilfelder enthält, müssen diese vorher definiert werden.

Wenn dies beispielsweise der Connected-Content-Aufruf wäre:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

Die Connected-Content-Antwort ist {% raw %}`Your language is ${language}`{% endraw %}. Der in diesem Beispiel angezeigte Inhalt ist `Hi Jon, your language is`.

Die Sprache selbst wird nicht als Template verarbeitet. Das liegt daran, dass Braze wissen muss, welche Felder von der Nutzerin oder dem Nutzer abgerufen werden sollen, bevor der Connected-Content-Aufruf erfolgt.

Um den Liquid-Passback korrekt darzustellen, müssen Sie das {% raw %}`${language}`{% endraw %}-Tag an einer beliebigen Stelle in der Anfrage einfügen, wie im folgenden Code-Snippet gezeigt. Der Liquid-Präprozessor erkennt dann, dass das Attribut „language“ abgerufen werden muss, damit es für das Templating der Antwort bereitsteht.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Beachten Sie, dass die `:rerender`-Flag-Option nur eine Ebene tief wirkt. Wenn die Connected-Content-Antwort selbst weitere Connected-Content-Tags oder Katalog-Tags enthält, wird Braze diese zusätzlichen Tags nicht erneut rendern.
{% endalert %}

## Best Practices

### `json_escape` mit Liquid-Tags verwenden, die das JSON-Format beschädigen könnten {#use-jsonescape-with-liquid-tags-that-could-break-the-json-format}

Wenn Sie `:rerender` verwenden, fügen Sie den `json_escape`-Filter zu jedem Liquid-Tag hinzu, das potenziell das JSON-Format beschädigen könnte. Wenn Ihre Liquid-Tags Zeichen enthalten, die das JSON-Format beschädigen, wird die gesamte Connected-Content-Antwort als Text interpretiert und in die Nachricht eingefügt, und keine der Variablen wird gespeichert.

Wenn beispielsweise die `message`-Ereigniseigenschaft im folgenden Beispiel Zeichen enthält, die das JSON-Format beschädigen könnten, fügen Sie den `json_escape`-Filter wie in diesem Beispiel hinzu:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}