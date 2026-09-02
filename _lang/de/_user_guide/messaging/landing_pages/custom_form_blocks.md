---
nav_title: Angepasste Formularblöcke erstellen
article_title: Angepasste Formularblöcke auf Landing-Pages erstellen
page_order: 6
page_type: reference
description: "Erfahren Sie, wie Sie angepasste interaktive Formulareingaben auf Braze Landing-Pages erstellen, damit deren Werte zusammen mit Standard-Formularblöcken validiert und übermittelt werden."
---

# Angepasste Formularblöcke auf Landing-Pages erstellen {#create-custom-form-blocks-on-landing-pages}

> [Formularblöcke]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) auf Braze Landing-Pages erfassen Standardeingaben wie Textfelder, Checkboxen und Dropdowns. Angepasste Formularblöcke erweitern die Möglichkeiten, indem Sie eigene interaktive Elemente erstellen können – zum Beispiel eine Sternebewertung, eine Emoji-Stimmungsauswahl oder eine Rubbelkarte.

Wenn Besucher:innen das angepasste Formular absenden, wird der ausgewählte Wert validiert und zusammen mit Ihren Standardfeldern gespeichert und dann als angepasstes Attribut an Braze gesendet. So können Sie reichhaltigere, ansprechendere Eingaben erfassen, ohne den Landing-Page-Editor verlassen zu müssen.

Angepasste Formularblöcke erstellen Sie mit einem einzigen JavaScript-Helfer, `window.brazeHelpers.forms.registerFormInput`, den Sie aus einem **Custom Code**-Block auf der Landing-Page aufrufen.

{% alert note %}
Umfragen und In-App Messages haben eigene Formularblöcke, aber `registerFormInput` – die JavaScript-API zur Verbindung einer selbst programmierten UI mit einem Formularblock – ist nur auf Landing-Pages verfügbar.
{% endalert %}

## Funktionsweise {#how-it-works}

Eine angepasste Formulareingabe ist jedes Element auf Ihrer Landing-Page, dessen Wert Sie erfassen und mit dem Formular übermitteln möchten. Sie verbinden dieses Element mit dem Braze-Formularsystem, indem Sie es Registrierung or registrieren. Die Registrierung teilt Braze mit, welches Element überwacht werden soll, wie der aktuelle Wert gelesen wird und was mit diesem Wert bei der Formularübermittlung geschehen soll.

1. Erstellen Sie Ihre angepasste UI in einem **Custom Code**-Block auf der Landing-Page und geben Sie ihr einen stabilen CSS-Selektor, z. B. eine `id`.
2. Registrierung or registrieren Sie das Element, indem Sie `window.brazeHelpers.forms.registerFormInput` mit einem Konfigurationsobjekt aufrufen.
3. Braze ruft Ihre `getValue`-Funktion auf, um den aktuellen Wert bei Bedarf zu lesen.
4. Wenn das Feld erforderlich ist oder Sie eine `onValidate`-Funktion bereitstellen, blockiert Braze die Übermittlung, bis der Wert gültig ist, und kennzeichnet ein ungültiges Element mit einer CSS-Klasse, die Sie stylen können. Siehe [Validierung und Pflichtfelder](#validation-and-required-fields).
5. Wenn das Formular übermittelt wird und die Validierung bestanden ist, ruft Braze Ihre `onSubmit`-Funktion auf, in der Sie das Braze SDK or Software-Development-Kit aufrufen können, um Informationen wie ein angepasstes Attribut zu protokollieren.

Da Sie die Funktionen bereitstellen, die den Wert lesen, validieren und übermitteln, funktioniert dieser Ansatz mit nahezu jedem angepassten Formularelement – Sie sind also nicht auf die Standard-Feldtypen im Editor beschränkt.

## Grundgerüst {#basic-framework}

Die einfachste Registrierung zielt auf ein Element ab, behandelt es als Pflichtfeld, liest seinen Wert aus einem Data-Attribut und schreibt diesen Wert bei der Formularübermittlung in ein angepasstes Attribut. Umschließen Sie den Aufruf mit einem `DOMContentLoaded`-Listener, wie in den Beispielen auf dieser Seite, damit das Element existiert, bevor `registerFormInput` ausgeführt wird:

```js
document.addEventListener("DOMContentLoaded", () => {
  window.brazeHelpers.forms.registerFormInput({
    selector: "#my-custom-input",
    isRequired: true,
    getValue: (element) => element.dataset.value ?? null,
    onSubmit: (value) => {
      window.brazeBridge.getUser().setCustomUserAttribute("my_attribute", value);
    },
  });
});
```

Rufen Sie `registerFormInput` einmal für jede angepasste Eingabe auf der Seite auf. Standard-Formularfelder, die über den Landing-Page-Editor platziert werden, müssen nicht registriert werden; die Registrierung ist nur für die angepassten Eingaben erforderlich, die Sie in einem **Custom Code**-Block erstellen.

## Konfigurationsreferenz {#configuration-reference}

`registerFormInput` akzeptiert ein einzelnes Konfigurationsobjekt. Als Funktionssignatur ausgedrückt sieht die vollständige Struktur so aus:

```js
window.brazeHelpers.forms.registerFormInput({
  // Provide exactly one of `selector` or `element` to identify the input.
  selector?: string,
  element?: HTMLElement,
  isRequired?: boolean | Promise<boolean>,
  getValue: (element: HTMLElement) => value,
  onValidate?: (value, element: HTMLElement) => boolean | Promise<boolean>,
  onSubmit?: (value, element: HTMLElement) => void | Promise<void>,
});
```

Sie müssen mindestens eine Möglichkeit zur Identifizierung des Elements (`selector` oder `element`) und eine `getValue`-Funktion angeben. Alles andere ist optional.

| Eigenschaft | Typ | Erforderlich | Beschreibung |
| --- | --- | --- | --- |
| `selector` | `string` | Ja (oder `element`) | Ein CSS-Selektor, der Ihr angepasstes Element trifft, z. B. `"#scratch-card"`. Braze löst ihn verzögert mit `querySelector` zum Zeitpunkt der Validierung und Übermittlung auf, sodass er auch ein Element treffen kann, das erst nach dem Aufruf von `registerFormInput` zum DOM hinzugefügt wurde. |
| `element` | `HTMLElement` | Ja (oder `selector`) | Eine direkte Referenz auf das Element, die anstelle von `selector` verwendet wird. Sie wird nur verwendet, solange das Element an die Seite angehängt ist, und hat Vorrang vor `selector`, wenn beide angegeben werden. |
| `isRequired` | `boolean \| Promise<boolean>` | Nein | Wenn `true`, kann das Formular nicht übermittelt werden, bis die Eingabe einen nicht-leeren Wert hat – `null`, `undefined`, leere Strings (einschließlich Strings, die nur aus Leerzeichen bestehen) und leere Arrays gelten als leer. Kann auch ein Promise sein, das zu einem Boolean aufgelöst wird und das Braze bei jeder Validierung der Eingabe neu auswertet, sodass Sie den Pflichtfeld-Status zur Laufzeit bestimmen können. Standardwert ist `false`. Siehe [Validierung und Pflichtfelder](#validation-and-required-fields) für die vollständige Validierungsreihenfolge. |
| `getValue` | `function` | Ja | Gibt den aktuellen Wert der Eingabe zurück. Braze übergibt das gefundene Element als Argument, sodass Sie den Wert aus dem DOM lesen können, z. B. `element.dataset.sentiment`, oder aus einer Variablen in Ihrem eigenen Code. Geben Sie `null` zurück, wenn noch kein Wert vorhanden ist. |
| `onValidate` | `function` | Nein | Empfängt den aktuellen Wert und das gefundene Element und muss `boolean \| Promise<boolean>` zurückgeben – denselben Rückgabetyp wie `isRequired` – wobei `true` bedeutet, dass der Wert gültig ist, und `false`, dass er ungültig ist. Verwenden Sie es, um Regeln durchzusetzen, die über das bloße Vorhandensein eines Werts hinausgehen, z. B. dass der Wert aus einer zulässigen Menge stammt. Wenn weggelassen, werden nur `isRequired` und die native Constraint-Validierung durchgesetzt. |
| `onSubmit` | `function` | Nein | Wird ausgeführt, wenn das Formular übermittelt wird und die Validierung bestanden ist. Empfängt den aktuellen Wert und das gefundene Element. Hier protokollieren Sie den Wert an Braze, typischerweise mit `setCustomUserAttribute`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Konfigurationsreferenz" }

### Den Wert in onSubmit verarbeiten {#act-on-the-value-in-onsubmit}

`onSubmit` ist ein einfacher JavaScript-Callback, sodass Sie den erfassten Wert so verarbeiten können, wie es Ihre Integration erfordert. Da `onSubmit` als Teil der Formularübermittlung ausgeführt wird, funktionieren `brazeBridge`-Aufrufe darin wie erwartet, auch für Besucher:innen, die die Landing-Page anonym geöffnet haben. Siehe [Bridge-Verfügbarkeit]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#bridge-availability) für die andere Situation, in der Bridge-Aufrufe funktionieren.

Das häufigste Muster ist das Schreiben des erfassten Werts in das Kundenprofil or Nutzerprofil mit der [Braze JavaScript Bridge]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge), die auf Landing-Pages verfügbar ist:

```js
window.brazeBridge.getUser().setCustomUserAttribute("attribute_name", value);
```

Verwenden Sie einen Namen für ein angepasstes Attribut, der bereits in Ihrem Workspace existiert oder den Sie erstellen möchten. Der übergebene Wert wird im Profil der Nutzer:innen gespeichert und kann dann für Segmentierung, Personalisierung und das Trigger or triggern or triggern von Folgenachrichten verwendet werden.

Sie sind nicht auf angepasste Attribute beschränkt. Aus demselben Callback können Sie jede [`brazeBridge.getUser()`-Methode]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#supported-methods) aufrufen. Zum Beispiel, um Nutzer:innen zu einer Abo-Gruppe hinzuzufügen, ein Standardattribut zu setzen, ein angepasstes Event zu protokollieren oder den Wert an Ihren eigenen API-Endpunkt zu senden.

{% alert note %}
Sie müssen `requestImmediateDataFlush` nicht innerhalb von `onSubmit` aufrufen. Der Formularübermittlungsprozess sendet automatisch alle Daten an Braze, nachdem Ihr `onSubmit`-Callback abgeschlossen ist.
{% endalert %}

## Beispiele {#examples}

Die folgenden Beispiele sind vollständig und eigenständig. Jedes ist ein einzelner Block mit Markup, einem `<script>`-Tag und einem `<style>`-Tag, den Sie in einen einzelnen **Custom Code** (HTML)-Block auf Ihrer Landing-Page einfügen. Der `registerFormInput`-Aufruf am Ende jedes Skripts verbindet die angepasste Eingabe mit dem Braze-Formular. Bewegen Sie den Mauszeiger über ein Codebeispiel und wählen Sie das Kopiersymbol, um es zu kopieren.

{% alert important %}
Diese Beispiele laufen vollständig im Browser der Besucher:innen. Beim Rubbelkarten-Beispiel wird der „Gewinn“ durch JavaScript im Browser der Besucher:innen ausgewählt, sodass technisch versierte Besucher:innen diesen Code ändern könnten, um ein beliebiges Ergebnis zu erhalten. Verlassen Sie sich bei Rewards, Rabatten oder anderen Ergebnissen, die eine strikte Durchsetzung pro Besucher:in erfordern, nicht auf dieses Muster. Validieren Sie alles, was sicherheits- oder umsatzrelevant ist, stattdessen auf Ihren eigenen Servern.
{% endalert %}

<div class="scrollable-code-examples" markdown="1">

{% tabs local %}
{% tab Stimmungsauswahl %}

**Ziel:** Die Besucher:innen wählen ein fröhliches oder unzufriedenes Gesicht, und ihre Auswahl wird in ein angepasstes String-Attribut namens `feedback_sentiment` geschrieben.

Fügen Sie Folgendes in einen einzelnen **Custom Code** (HTML)-Block ein:

```html
<div id="sentiment-picker" class="sentiment-picker">
  <button type="button" data-sentiment="positive" aria-label="Happy">🙂</button>
  <button type="button" data-sentiment="negative" aria-label="Unhappy">🙁</button>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const picker = document.getElementById("sentiment-picker");

    picker.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => {
        picker.dataset.sentiment = button.dataset.sentiment;
        picker.querySelectorAll("button").forEach((b) => b.classList.remove("selected"));
        button.classList.add("selected");
      });
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#sentiment-picker",
      isRequired: true,
      getValue: (element) => element.dataset.sentiment ?? null,
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("feedback_sentiment", value);
      },
    });
  });
</script>

<style>
  .sentiment-picker {
    display: flex;
    gap: 16px;
    justify-content: center;
    font-size: 40px;
  }

  .sentiment-picker button {
    background: none;
    border: 2px solid transparent;
    border-radius: 12px;
    cursor: pointer;
    line-height: 1;
    padding: 8px;
  }

  .sentiment-picker button.selected {
    border-color: #1f2933;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .sentiment-picker.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**Funktionsweise:** Durch Auswahl eines Buttons wird dessen `data-sentiment`-Wert im Container-Element gespeichert. `getValue` liest diesen Wert aus dem Container-Element zurück, das Braze übergibt. Da `isRequired` auf `true` gesetzt ist, wird das Formular erst übermittelt, wenn die Besucher:innen ein Gesicht gewählt haben, und der Container wird mit der Klasse `bz-validation-error` gekennzeichnet, solange er leer ist. Bei der Übermittlung wird der gewählte Wert (`"positive"` oder `"negative"`) in `feedback_sentiment` geschrieben.

{% endtab %}
{% tab Rubbelkarte %}

**Ziel:** Die Besucher:innen rubbeln eine Karte frei, um einen von drei Rabatten (10 % Rabatt, 20 % Rabatt oder 25 % Rabatt) aufzudecken, und der Rabatt wird in ein angepasstes String-Attribut namens `scratch_off_reward` geschrieben.

Dieses Beispiel zeichnet eine Rubbelkarte auf einem HTML Canvas. Ein Gewinn wird beim Laden der Seite zufällig ausgewählt und unter einer undurchsichtigen Schicht verborgen, die die Besucher:innen freirubbeln. Sie können den Canvas-Ansatz durch jedes beliebige Rubbelwidget ersetzen; nur der `registerFormInput`-Aufruf verbindet es mit Braze. Fügen Sie Folgendes in einen einzelnen **Custom Code** (HTML)-Block ein:

```html
<div id="scratch-card" class="scratch-card" data-reward="">
  <span class="scratch-card__reward"></span>
  <canvas class="scratch-card__surface" width="300" height="150"></canvas>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const rewards = ["10% Off", "20% Off", "25% Off"];

    const card = document.getElementById("scratch-card");
    const label = card.querySelector(".scratch-card__reward");
    const canvas = card.querySelector(".scratch-card__surface");
    const ctx = canvas.getContext("2d");

    // Randomly assign which reward this visitor will reveal.
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    label.textContent = reward;

    // Paint the opaque scratch layer over the reward.
    ctx.fillStyle = "#b3b3b3";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = "destination-out";

    let isScratching = false;

    function scratchAt(event) {
      const rect = canvas.getBoundingClientRect();
      ctx.beginPath();
      ctx.arc(event.clientX - rect.left, event.clientY - rect.top, 18, 0, Math.PI * 2);
      ctx.fill();
    }

    canvas.addEventListener("pointerdown", () => { isScratching = true; });
    canvas.addEventListener("pointermove", (event) => {
      if (isScratching) scratchAt(event);
    });
    canvas.addEventListener("pointerup", () => {
      isScratching = false;
      // The visitor has scratched the card, so record the revealed reward.
      card.dataset.reward = reward;
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#scratch-card",
      isRequired: true,
      getValue: (element) => element.dataset.reward || null,
      onValidate: (value) => rewards.includes(value),
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("scratch_off_reward", value);
      },
    });
  });
</script>

<style>
  .scratch-card {
    position: relative;
    width: 300px;
    height: 150px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }

  /* The reward sits underneath and is revealed as the canvas is scratched away. */
  .scratch-card__reward {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    color: #1f2933;
  }

  .scratch-card__surface {
    position: absolute;
    inset: 0;
    border-radius: 12px;
    cursor: pointer;
    touch-action: none;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .scratch-card.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**Funktionsweise:** Beim Laden der Seite wählt das Skript zufällig einen der drei Gewinne aus und malt eine undurchsichtige Schicht darüber auf das Canvas. Wenn die Besucher:innen über das Canvas ziehen, löscht der Kompositmodus `"destination-out"` diese Schicht und enthüllt den darunter liegenden Gewinn. Bei `pointerup` wird der enthüllte Gewinn in das `data-reward`-Attribut der Karte geschrieben. `getValue` liest ihn von dort zurück, `onValidate` bestätigt, dass es sich um einen der drei definierten Gewinne handelt, und `isRequired` verhindert die Übermittlung, bis die Karte freigerubbelt wurde. Bei der Übermittlung wird der enthüllte Rabatt (z. B. `"20% Off"`) in `scratch_off_reward` geschrieben.

{% endtab %}
{% tab Campaign-Attribution %}

**Ziel:** Die Campaign erfassen, die die Besucher:innen auf die Landing-Page geführt hat, und sie als angepasste Event-Eigenschaft für nachgelagerte Berichterstattung und Attribution protokollieren.

Dieses Beispiel zeigt, wie Sie eine Landing-Page-Formularübermittlung einer bestimmten Campaign zuordnen. Indem Sie eine Liquid-Variable wie {% raw %}`{{campaign.${api_id}}}`{% endraw %} zur URL Ihrer Landing-Page in E-Mail-, Kurzmitteilungsdienst or SMS- oder WhatsApp-Nachrichten hinzufügen, können Sie den Campaign-Bezeichner an die Landing-Page übergeben. Der angepasste Formularblock liest dann diesen Parameter aus der URL und protokolliert ihn als angepasstes Event mit der Campaign-API-ID als Event-Eigenschaft, was es einfacher macht, nachzuverfolgen, welche Campaigns Formularübermittlungen auslösen.

Fügen Sie Folgendes in einen einzelnen **Custom Code** (HTML)-Block ein:

```html
<input type="hidden" id="campaign-attribution" value="" />

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const hiddenInput = document.getElementById("campaign-attribution");
    const campaignApiId = new URLSearchParams(window.location.search).get("campaign_api_id");

    if (campaignApiId) {
      hiddenInput.value = campaignApiId;
    }

    window.brazeHelpers.forms.registerFormInput({
      selector: "#campaign-attribution",
      isRequired: false,
      getValue: (element) => element.value || null,
      onSubmit: async (value) => {
        if (!value) {
          return;
        }

        await window.brazeBridge.logCustomEvent("landing_page_form_submitted", {
          campaign_api_id: value,
        });
      },
    });
  });
</script>
```

**Funktionsweise:** Wenn Sie eine E-Mail-, Kurzmitteilungsdienst or SMS- oder WhatsApp-Nachricht erstellen, die auf Ihre Landing-Page verlinkt, hängen Sie den Campaign-Bezeichner mithilfe von Liquid-Templating an die URL an: {% raw %}`https://your-landing-page.com?campaign_api_id={{campaign.${api_id}}}`{% endraw %}. Wenn Besucher:innen über diese Nachricht auf der Landing-Page ankommen, liest das Skript den Parameter `campaign_api_id` aus der URL und speichert ihn in einem versteckten Eingabefeld. Bei der Formularübermittlung protokolliert der `onSubmit`-Callback, sofern eine Campaign-ID vorhanden ist, ein angepasstes Event namens `landing_page_form_submitted` mit der Campaign-API-ID als Event-Eigenschaft. Dieses Event erscheint in Currents und kann für Berichterstattung, Segmentierung und Attributionsanalyse verwendet werden.

{% alert tip %}
Sie können dieses Muster erweitern, um zusätzliche URL-Parameter wie Nachrichtenvariante, Canvas-Schritt oder jede andere Liquid-Variable zu erfassen, die Sie für Attributionszwecke an die Landing-Page übergeben möchten.
{% endalert %}

{% endtab %}
{% endtabs %}

</div>

## Validierung und Pflichtfelder {#validation-and-required-fields}

Eine Eingabe muss alle folgenden Ebenen bestehen, die auf sie zutreffen, bevor das Formular übermittelt werden kann:

1. **`isRequired`** blockiert die Übermittlung, bis ein nicht-leerer Wert vorhanden ist. Geben Sie `null` von `getValue` zurück, wenn die Eingabe noch keinen Wert hat, damit Braze erkennen kann, dass sie leer ist. Leere Strings (einschließlich Strings, die nur aus Leerzeichen bestehen) und leere Arrays werden ebenfalls als leer behandelt, während `0` und `false` als vorhandene Werte gelten. `isRequired` kann ein Boolean oder ein Promise sein, das zu einem Boolean aufgelöst wird, und wird bei jeder Validierung der Eingabe neu ausgewertet.
2. **Native Constraint-Validierung.** Wenn das gefundene Element die Standard-HTML-API `checkValidity()` unterstützt, z. B. ein natives `<input>` mit `required`, `pattern`, `min` oder `max`, führt Braze sie aus und blockiert die Übermittlung bei Fehlschlag. Bei vollständig angepassten, nicht-nativen Elementen (ein `div`, ein `canvas` usw.) besteht diese Prüfung immer, sodass sie Ihre eigene Logik nie beeinträchtigt.
3. **`onValidate`** blockiert die Übermittlung basierend auf Ihren eigenen Regeln. Es empfängt den aktuellen Wert und das gefundene Element und muss `boolean \| Promise<boolean>` zurückgeben – denselben Rückgabetyp wie `isRequired` – wobei `true` bedeutet, dass der Wert gültig ist, und `false`, dass er ungültig ist. Verwenden Sie es für Prüfungen auf zulässige Werte, Formatprüfungen, Bereiche oder jede Logik, die Sie in JavaScript ausdrücken können.

### Fehlerstyling {#error-styling}

Immer wenn eine Eingabe die Validierung nicht besteht, fügt Braze die CSS-Klasse `bz-validation-error` zum Element hinzu, das durch Ihren `selector` oder `element` gefunden wurde, und entfernt die Klasse, wenn die Eingabe wieder gültig wird. Stylen Sie den ungültigen Zustand nach Belieben, z. B. mit einer Umrandung, die die Aufmerksamkeit auf die fehlerhafte Eingabe lenkt, indem Sie eine Regel hinzufügen, die Ihr Element in Kombination mit der Klasse `bz-validation-error` anspricht:

```css
#my-custom-input.bz-validation-error {
  outline: 3px solid #f94144;
  outline-offset: 4px;
}
```

Das Styling des Fehlerzustands ist optional, wird aber empfohlen, damit Besucher:innen sehen können, welche angepasste Eingabe die Übermittlung blockiert. Jedes [Beispiel](#examples) auf dieser Seite enthält eine `bz-validation-error`-Regel.

## Best Practices {#best-practices}

- Verwenden Sie einen stabilen, eindeutigen Selektor. Eine `id` ist die sicherste Wahl. Vermeiden Sie Selektoren, die mehr als ein Element treffen könnten.
- Geben Sie `null` zurück, nicht einen leeren String oder `undefined`, wenn kein Wert vorhanden ist, damit Pflichtfeldprüfungen vorhersehbar funktionieren. Leere Strings und leere Arrays werden ebenfalls als leer behandelt, aber `null` ist das klarste Signal für „kein Wert“.
- Halten Sie `getValue` schlank und synchron. Braze kann es mehrfach aufrufen, daher sollte es den aktuellen Wert lesen und zurückgeben, anstatt aufwendige Operationen durchzuführen.
- Stylen Sie den `bz-validation-error`-Zustand, damit Besucher:innen sehen können, welche angepasste Eingabe die Übermittlung blockiert.
- Definieren Sie Ihre Namen für angepasste Attribute im Voraus und halten Sie sie konsistent, damit Sie die Daten später zuverlässig für die Segmentierung nutzen können.
- Testen Sie die vollständige Übermittlung. Bestätigen Sie, dass das Attribut nach der Übermittlung im Kundenprofil or Nutzerprofil erscheint und dass Pflichtfeld- und Validierungsregeln die Übermittlung wie erwartet blockieren.

## Fehlerbehebung {#troubleshooting}

### Das Formular wird übermittelt, obwohl nichts ausgewählt wurde {#the-form-submits-even-though-nothing-was-selected}
Stellen Sie sicher, dass `isRequired` auf `true` gesetzt ist. Braze behandelt `null`, `undefined`, leere Strings (einschließlich Strings, die nur aus Leerzeichen bestehen) und leere Arrays als keinen Wert – wenn `getValue` etwas anderes zurückgibt (z. B. einen nicht-leeren Standard- oder Platzhalterwert), wenn nichts ausgewählt wurde, greift die Pflichtfeldprüfung nicht.

### Der Wert erscheint nicht im Profil {#the-value-doesnt-appear-on-the-profile}
Bestätigen Sie, dass `onSubmit` `window.brazeBridge.getUser().setCustomUserAttribute` mit dem korrekten Attributnamen aufruft und dass sich der **Custom Code**-Block auf derselben Landing-Page wie das Formular befindet.

### Die Registrierung scheint nichts zu bewirken {#registration-seems-to-do-nothing}
Prüfen Sie, ob der Selektor ein Element trifft, das im DOM existiert, wenn `registerFormInput` ausgeführt wird, und ob das Skript nach dem Rendern dieses Elements ausgeführt wird. Öffnen Sie dann die Entwicklerkonsole Ihres Browsers: `registerFormInput` validiert seine Konfiguration und ignoriert die Registrierung bei Fehlern (z. B. fehlendes `getValue`, ein Selektor, der kein gültiger CSS-Selektor ist, oder eine Eigenschaft des falschen Typs) und protokolliert eine Warnung mit dem Präfix `[brazeHelpers.forms.registerFormInput]`, die beschreibt, was ungültig war.

## Verwandte Inhalte {#related-content}

- [JavaScript Bridge für Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) behandelt die vollständige `brazeBridge`-Referenz, die in `onSubmit` verwendet wird.
- [Landing-Pages erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)