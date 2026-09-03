---
nav_title: Wissensquellen
article_title: Wissensquellen
description: "Dieser Referenzartikel beschreibt, wie Sie Wissensquellen für Ihre BrazeAI-Agenten erstellen und verwalten."
page_type: reference
page_order: 3.5
---

# Wissensquellen {#knowledge-sources}

> Wissensquellen helfen Ihren KI-Agenten, Katalogdaten zu interpretieren und die richtigen Informationen abzurufen, um Ihre Ziele zu erreichen. Eine Einführung in Braze Agents finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). Informationen zum Hinzufügen von Wissen zu einem Agenten finden Sie unter [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources).

{% alert important %}
Wissensquellen für die Agentenkonsole befinden sich derzeit im Early Access. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an diesem Early Access teilnehmen möchten.
{% endalert %}

## So funktioniert es {#how-it-works}

Wissensquellen sind eine Art von Agentenkontext. Ein KI-Agent kann eine Wissensquelle referenzieren, um Daten aus dem Katalog genauer abzurufen, als wenn der Katalog direkt in den Anweisungen des Agenten referenziert wird.

Nehmen wir an, Sie erstellen einen Agenten, der Restaurants in New York City basierend auf der Lieblingsküche einer Nutzerin oder eines Nutzers empfiehlt – einem angepassten Attribut. Dieser Agent referenziert die Wissensquelle für den Katalog „nyc_restaurants“. Wenn Sie diese Wissensquelle erstellen, nehmen Sie nur die Felder auf, die der Agent benötigt – wie Restaurantname, Standort und Küche – und schließen andere Katalogspalten aus, die keine Empfehlungen unterstützen.

Die Anweisungen des Agenten beschreiben seine Rolle und Einschränkungen klar:

{% raw %}
```
You are a restaurant recommendation agent. Use your knowledge to help find restaurants for the user. Only include filters in your knowledge source query. Don't ask any followup questions. The user's favorite cuisine is {{custom_attribute.${favorite_cuisine}}}
```
{% endraw %}

Wenn die Lieblingsküche einer Nutzerin oder eines Nutzers Pizza ist, kann der Agent basierend auf der Wissensquelle die folgende Antwort zurückgeben:

```
Here are some pizza recommendations for you:
- Dale's Pizza (Greenwich Village, Manhattan): Dale's Pizza invites you to savor the taste of authentic New York. Nestled in the heart of Manhattan, this iconic pizzeria offers a warm and inviting atmosphere perfect for any occasion.
- Pizza Palace (Carroll Gardens, Brooklyn): Pizza Palace is a highly-rated culinary gem renowned for its exquisite pizza. This inviting spot offers a warm and modern dining experience.
```

## Eine Wissensquelle erstellen {#create-a-knowledge-source}

So erstellen Sie eine Wissensquelle:

1. Gehen Sie zu **Agentenkonsole** > **Wissensquellen**.
2. Wählen Sie **Wissensquelle hinzufügen** aus. Wählen Sie im Dropdown-Menü **Katalog** aus.
3. Wählen Sie den Katalog aus dem Dropdown-Menü aus.
4. Überprüfen Sie die Katalogfelder und deaktivieren Sie alle, die für den Anwendungsfall Ihres Agenten nicht relevant sind. Wir empfehlen, Katalogfelder auszuschließen, die für den Abruf oder die Generierung nicht nützlich sind – beschränken Sie die Wissensquelle auf die Felder, die Ihr Agent benötigt.
5. (Optional) Fügen Sie eine Beschreibung hinzu, die den Inhalt der Wissensquelle beschreibt.
6. Wählen Sie **Wissensquelle hinzufügen** aus.

Das Einbeziehen aller Katalogfelder kann unnötigen Kontext hinzufügen und die Ausgabequalität verringern. Das Deaktivieren von Feldern, die für Ihren Anwendungsfall nicht relevant sind, hilft dem Agenten, sich auf die wichtigen Daten zu konzentrieren.

![Eine Wissensquelle „nyc_restaurants“, die den Katalog „nyc_restaurants“ referenziert.]({% image_buster /assets/img/ai_agent/knowledge_source_example.png %})

Sie können auch eine Wissensquelle erstellen, während Sie einen Agenten aufbauen, indem Sie zum Abschnitt **Anweisungen** Ihres Agenten gehen. Wählen Sie **Wissen hinzufügen** > **Wissensquelle erstellen** aus.

## Eine Wissensquelle in Ihrem KI-Agenten verwenden {#use-a-knowledge-source-in-your-ai-agent}

Sie können Wissensquellen im Abschnitt **Wissensquellen** verwalten. Hier sehen Sie Details wie z. B. welche Wissensquellen aktiv sind und wann sie zuletzt synchronisiert wurden. Beachten Sie, dass der Name der Wissensquelle mit dem Namen des als Quelle verwendeten Katalogs übereinstimmt.

So verwenden Sie eine Wissensquelle in Ihrem KI-Agenten:

1. Gehen Sie zum Abschnitt **Anweisungen** Ihres Agenten.
2. Wählen Sie **+ Agentenkontext** > **Wissen hinzufügen** aus.
3. Wählen Sie im Dropdown-Menü die Wissensquelle aus.

Jetzt kann Ihr Agent die Wissensquelle referenzieren und die relevanten Katalogdaten abrufen.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie funktionieren Wissensquellen? {#how-do-knowledge-sources-work}

Die Umwandlung eines Katalogs in eine Wissensquelle hilft Braze Agents, die tatsächliche Bedeutung hinter den Wörtern und Phrasen im Katalog zu verstehen, sodass Agenten effektiver aussagekräftige Daten finden können, um bessere Ergebnisse zu erzielen.

### Wann sollte ich eine Wissensquelle erstellen? {#when-should-i-create-a-knowledge-source}

Erstellen Sie eine Wissensquelle, wenn Sie einen angepassten Agenten (Canvas-Schritt-Agent oder Katalog-Agent) einrichten, der Katalogdaten als Kontext benötigt. Wissensquellen helfen Agenten, Katalogdaten genauer abzurufen, als wenn der Katalog direkt in den Anweisungen des Agenten referenziert wird.

### Muss ich auch den ursprünglichen Katalog als Kontext zuweisen, wenn einem Agenten eine Wissensquelle als Kontext zugewiesen wurde? {#if-an-agent-has-been-given-a-knowledge-source-as-context-do-i-also-need-to-assign-the-original-catalog-as-context}

Nein. Die Wissensquelle ersetzt den Katalog als Agentenkontext – Sie müssen nicht beides zuweisen. Wenn Sie die Wissensquelle erstellen, nehmen Sie nur die Katalogfelder auf, die Ihr Agent benötigt.

### Wie sollte ich die Effektivität einer Wissensquelle bewerten? {#how-should-i-evaluate-the-effectiveness-of-a-knowledge-source}

Duplizieren Sie einen vorhandenen Agenten, der einen regulären Katalog referenziert, und ändern Sie ihn so, dass er stattdessen die entsprechende Wissensquelle referenziert. Führen Sie einige Testaufrufe in der Agentenkonsole durch, um die Genauigkeit sicherzustellen, und erwägen Sie dann, entweder den vorhandenen Agenten dort zu ersetzen, wo er eingesetzt wird, oder den alten Agenten gegen den neuen Agenten per A/B-Test zu vergleichen (mithilfe des Experiment-Path-Schritts), um die Auswirkungen auf die Performance zu verstehen.