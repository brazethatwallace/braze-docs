---
nav_title: Créer des blocs de formulaire personnalisés
article_title: Créer des blocs de formulaire personnalisés sur les pages de destination
page_order: 6
page_type: reference
description: "Découvrez comment créer des champs de formulaire interactifs personnalisés sur les pages de destination Braze afin que leurs valeurs soient validées et soumises avec les blocs de formulaire standard."
---

# Créer des blocs de formulaire personnalisés sur les pages de destination {#create-custom-form-blocks-on-landing-pages}

> Les [blocs de formulaire]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) des pages de destination Braze capturent des champs standard, tels que les champs de texte, les cases à cocher et les listes déroulantes. Les blocs de formulaire personnalisés élargissent les possibilités en vous permettant de créer vos propres éléments interactifs, comme une notation par étoiles, un sélecteur de sentiment par emoji ou une carte à gratter.

Lorsqu'un visiteur soumet le formulaire personnalisé, la valeur sélectionnée est validée et enregistrée avec vos champs standard, puis envoyée à Braze en tant qu'attribut personnalisé utilisateur. Cela vous permet de collecter des données plus riches et plus engageantes sans quitter l'éditeur de pages de destination.

Vous créez des blocs de formulaire personnalisés avec un seul helper JavaScript, `window.brazeHelpers.forms.registerFormInput`, que vous appelez depuis un bloc **Custom Code** sur la page de destination.

{% alert note %}
Les enquêtes et les messages in-app disposent de leurs propres blocs de formulaire, mais `registerFormInput` — l'API JavaScript permettant de connecter une interface personnalisée à un bloc de formulaire — n'est disponible que sur les pages de destination.
{% endalert %}

## Fonctionnement {#how-it-works}

Un champ de formulaire personnalisé est tout élément de votre page de destination dont vous souhaitez capturer et soumettre la valeur avec le formulaire. Vous connectez cet élément au système de formulaire Braze en l'enregistrant. L'enregistrement indique à Braze quel élément surveiller, comment lire sa valeur actuelle et quoi faire de cette valeur lors de la soumission du formulaire.

1. Créez votre interface personnalisée dans un bloc **Custom Code** sur la page de destination et attribuez-lui un sélecteur CSS stable, tel qu'un `id`.
2. Enregistrez l'élément en appelant `window.brazeHelpers.forms.registerFormInput` avec un objet de configuration.
3. Braze appelle votre fonction `getValue` pour lire la valeur actuelle lorsqu'il en a besoin.
4. Si le champ est obligatoire, ou si vous fournissez une fonction `onValidate`, Braze bloque la soumission tant que la valeur ne passe pas la validation, et signale un élément invalide avec une classe CSS que vous pouvez styliser. Voir [Validation et champs obligatoires](#validation-and-required-fields).
5. Lorsque le formulaire est soumis et que la validation réussit, Braze appelle votre fonction `onSubmit`, dans laquelle vous pouvez appeler le SDK Braze pour enregistrer des informations telles qu'un attribut personnalisé utilisateur.

Comme c'est vous qui fournissez les fonctions de lecture, de validation et de soumission de la valeur, cette approche fonctionne avec pratiquement n'importe quel élément de formulaire personnalisé, et vous n'êtes pas limité aux types de champs standard de l'éditeur.

## Structure de base {#basic-framework}

L'enregistrement le plus simple cible un seul élément, le traite comme obligatoire, lit sa valeur depuis un attribut data et écrit cette valeur dans un attribut personnalisé utilisateur lors de la soumission du formulaire. Encapsulez l'appel dans un écouteur `DOMContentLoaded`, comme dans les exemples de cette page, afin que l'élément existe avant l'exécution de `registerFormInput` :

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

Appelez `registerFormInput` une fois pour chaque champ personnalisé de la page. Les champs de formulaire standard placés via l'éditeur de pages de destination n'ont pas besoin d'être enregistrés ; l'enregistrement ne concerne que les champs personnalisés que vous créez dans un bloc **Custom Code**.

## Référence de configuration {#configuration-reference}

`registerFormInput` accepte un seul objet de configuration. Exprimée sous forme de signature de fonction, la structure complète est :

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

Au minimum, vous devez fournir un moyen de localiser l'élément (`selector` ou `element`) et une fonction `getValue`. Tout le reste est optionnel.

| Propriété | Type | Obligatoire | Description |
| --- | --- | --- | --- |
| `selector` | `string` | Oui (ou `element`) | Un sélecteur CSS correspondant à votre élément personnalisé, par exemple `"#scratch-card"`. Braze le résout de manière différée avec `querySelector` au moment de la validation et de la soumission, il peut donc correspondre à un élément ajouté au DOM après l'exécution de `registerFormInput`. |
| `element` | `HTMLElement` | Oui (ou `selector`) | Une référence directe à l'élément, utilisée à la place de `selector`. Elle n'est utilisée que tant que l'élément reste attaché à la page, et elle prend le pas sur `selector` lorsque les deux sont fournis. |
| `isRequired` | `boolean \| Promise<boolean>` | Non | Lorsque la valeur est `true`, le formulaire ne peut pas être soumis tant que le champ n'a pas une valeur non vide — `null`, `undefined`, les chaînes vides (y compris celles ne contenant que des espaces) et les tableaux vides sont tous considérés comme vides. Peut également être une promesse qui se résout en booléen, que Braze réévalue à chaque validation du champ, ce qui vous permet de décider de l'état obligatoire au moment de l'exécution. La valeur par défaut est `false`. Voir [Validation et champs obligatoires](#validation-and-required-fields) pour l'ordre complet de validation. |
| `getValue` | `function` | Oui | Renvoie la valeur actuelle du champ. Braze passe l'élément correspondant en argument, ce qui vous permet de lire la valeur depuis le DOM, par exemple `element.dataset.sentiment`, ou depuis une variable de votre propre code. Renvoyez `null` lorsqu'il n'y a pas encore de valeur. |
| `onValidate` | `function` | Non | Reçoit la valeur actuelle et l'élément correspondant, et doit renvoyer `boolean \| Promise<boolean>` — le même type de retour que `isRequired` — où `true` signifie que la valeur est valide et `false` qu'elle ne l'est pas. Utilisez-la pour appliquer des règles au-delà de la simple présence d'une valeur, par exemple vérifier que la valeur fait partie d'un ensemble autorisé. Si omise, seuls `isRequired` et la validation native des contraintes sont appliqués. |
| `onSubmit` | `function` | Non | S'exécute lorsque le formulaire est soumis et que la validation réussit. Reçoit la valeur actuelle et l'élément correspondant. C'est ici que vous enregistrez la valeur dans Braze, généralement avec `setCustomUserAttribute`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Référence de configuration" }

### Agir sur la valeur dans onSubmit {#act-on-the-value-in-onsubmit}

`onSubmit` est un simple rappel JavaScript, vous pouvez donc agir sur la valeur capturée selon les besoins de votre intégration. Comme `onSubmit` s'exécute dans le cadre de la soumission du formulaire, les appels `brazeBridge` effectués à l'intérieur fonctionnent comme prévu, même pour un visiteur ayant ouvert la page de destination de manière anonyme. Voir [Disponibilité du pont]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#bridge-availability) pour l'autre situation où les appels au pont fonctionnent.

Le schéma le plus courant consiste à écrire la valeur capturée dans le profil utilisateur avec le [pont JavaScript Braze]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) disponible sur les pages de destination :

```js
window.brazeBridge.getUser().setCustomUserAttribute("attribute_name", value);
```

Utilisez un nom d'attribut personnalisé qui existe déjà, ou que vous souhaitez créer, dans votre espace de travail. La valeur que vous transmettez est stockée dans le profil de l'utilisateur et peut ensuite être utilisée pour la segmentation, la personnalisation et le déclenchement de messages de suivi.

Vous n'êtes pas limité aux attributs personnalisés. Depuis le même rappel, vous pouvez appeler n'importe quelle [méthode `brazeBridge.getUser()`]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#supported-methods). Par exemple, pour ajouter l'utilisateur à un groupe d'abonnement, définir un attribut standard, enregistrer un événement personnalisé ou envoyer la valeur à votre propre endpoint API.

{% alert note %}
Vous n'avez pas besoin d'appeler `requestImmediateDataFlush` dans `onSubmit`. Le processus de soumission du formulaire envoie automatiquement toutes les données à Braze une fois votre rappel `onSubmit` terminé.
{% endalert %}

## Exemples {#examples}

Les exemples suivants sont complets et autonomes. Chacun est un bloc unique contenant du balisage, une balise `<script>` et une balise `<style>` que vous collez dans un seul bloc **Custom Code** (HTML) sur votre page de destination. L'appel `registerFormInput` vers la fin de chaque script connecte le champ personnalisé au formulaire Braze. Survolez un exemple de code et sélectionnez l'icône de copie pour le copier.

{% alert important %}
Ces exemples s'exécutent entièrement dans le navigateur du visiteur. Pour l'exemple de la carte à gratter, le « prix » est choisi par JavaScript dans le navigateur du visiteur, un visiteur techniquement averti pourrait donc modifier ce code pour obtenir le résultat de son choix. Ne vous fiez pas à ce modèle pour des récompenses, des remises ou d'autres résultats nécessitant une application stricte par visiteur. Validez tout ce qui est sensible en termes de sécurité ou de revenus sur vos propres serveurs.
{% endalert %}

<div class="scrollable-code-examples" markdown="1">

{% tabs local %}
{% tab Sélecteur de sentiment %}

**Objectif :** Le visiteur sélectionne un visage content ou mécontent, et son choix est écrit dans un attribut personnalisé de type chaîne nommé `feedback_sentiment`.

Collez le code suivant dans un seul bloc **Custom Code** (HTML) :

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

**Fonctionnement :** La sélection d'un bouton stocke sa valeur `data-sentiment` sur l'élément conteneur. `getValue` relit cette valeur depuis l'élément conteneur que Braze transmet. Comme `isRequired` est `true`, le formulaire ne se soumet pas tant que le visiteur n'a pas choisi un visage, et le conteneur est signalé avec la classe `bz-validation-error` tant qu'il est vide. Lors de la soumission, la valeur choisie (`"positive"` ou `"negative"`) est écrite dans `feedback_sentiment`.

{% endtab %}
{% tab Carte à gratter %}

**Objectif :** Le visiteur gratte une carte pour révéler l'une des trois remises (10% Off, 20% Off ou 25% Off), et la remise est écrite dans un attribut personnalisé de type chaîne nommé `scratch_off_reward`.

Cet exemple dessine une carte à gratter sur un Canvas HTML. Une récompense est choisie aléatoirement au chargement de la page et est cachée sous une couche opaque que le visiteur gratte. Vous pouvez remplacer l'approche Canvas par n'importe quel widget de grattage de votre choix ; seul l'appel `registerFormInput` le connecte à Braze. Collez le code suivant dans un seul bloc **Custom Code** (HTML) :

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

**Fonctionnement :** Au chargement de la page, le script choisit aléatoirement l'une des trois récompenses et peint une couche opaque par-dessus sur le Canvas. Lorsque le visiteur fait glisser son curseur sur le Canvas, le mode composite `"destination-out"` efface cette couche et révèle la récompense en dessous. Au `pointerup`, la récompense révélée est écrite dans l'attribut `data-reward` de la carte. `getValue` la relit depuis cet attribut, `onValidate` confirme qu'il s'agit bien de l'une des trois récompenses définies, et `isRequired` empêche la soumission tant que la carte n'a pas été grattée. Lors de la soumission, la remise révélée (par exemple, `"20% Off"`) est écrite dans `scratch_off_reward`.

{% endtab %}
{% tab Attribution de Campaign %}

**Objectif :** Capturer la Campaign qui a dirigé le visiteur vers la page de destination et l'enregistrer en tant que propriété d'événement personnalisé pour le reporting et l'attribution en aval.

Cet exemple montre comment attribuer la soumission d'un formulaire de page de destination à une Campaign spécifique. En ajoutant une variable Liquid comme {% raw %}`{{campaign.${api_id}}}`{% endraw %} à l'URL de votre page de destination dans les messages e-mail, SMS ou WhatsApp, vous pouvez transmettre l'identifiant de la Campaign à la page de destination. Le bloc de formulaire personnalisé lit ensuite ce paramètre depuis l'URL et l'enregistre en tant qu'événement personnalisé avec l'ID API de la Campaign comme propriété d'événement, ce qui facilite le suivi des Campaigns qui génèrent des soumissions de formulaire.

Collez le code suivant dans un seul bloc **Custom Code** (HTML) :

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

**Fonctionnement :** Lorsque vous créez un message e-mail, SMS ou WhatsApp qui renvoie vers votre page de destination, ajoutez l'identifiant de la Campaign à l'URL à l'aide du templating Liquid : {% raw %}`https://your-landing-page.com?campaign_api_id={{campaign.${api_id}}}`{% endraw %}. Lorsqu'un visiteur arrive sur la page de destination depuis ce message, le script lit le paramètre `campaign_api_id` depuis l'URL et le stocke dans un champ de saisie masqué. Lors de la soumission du formulaire, si un ID de Campaign est présent, le rappel `onSubmit` enregistre un événement personnalisé nommé `landing_page_form_submitted` avec l'ID API de la Campaign comme propriété d'événement. Cet événement apparaît dans Currents et peut être utilisé pour le reporting, la segmentation et l'analyse d'attribution.

{% alert tip %}
Vous pouvez étendre ce modèle pour capturer des paramètres d'URL supplémentaires tels que la variante de message, l'étape Canvas ou toute autre variable Liquid que vous souhaitez transmettre à la page de destination à des fins d'attribution.
{% endalert %}

{% endtab %}
{% endtabs %}

</div>

## Validation et champs obligatoires {#validation-and-required-fields}

Un champ doit passer toutes les couches de validation applicables avant que le formulaire puisse être soumis :

1. **`isRequired`** conditionne la soumission à la présence d'une valeur non vide. Renvoyez `null` depuis `getValue` lorsque le champ n'a pas encore de valeur afin que Braze puisse détecter qu'il est vide. Les chaînes vides (y compris celles ne contenant que des espaces) et les tableaux vides sont également traités comme vides, tandis que `0` et `false` comptent comme des valeurs présentes. `isRequired` peut être un booléen ou une promesse qui se résout en booléen, et il est réévalué à chaque validation du champ.
2. **Validation native des contraintes.** Si l'élément correspondant prend en charge l'API standard HTML `checkValidity()`, par exemple un `<input>` natif avec `required`, `pattern`, `min` ou `max`, Braze l'exécute et bloque la soumission en cas d'échec. Pour les éléments entièrement personnalisés et non natifs (un `div`, un `canvas`, etc.), cette vérification réussit toujours, elle n'interfère donc jamais avec votre propre logique.
3. **`onValidate`** conditionne la soumission à vos propres règles. Elle reçoit la valeur actuelle et l'élément correspondant, et doit renvoyer `boolean \| Promise<boolean>` — le même type de retour que `isRequired` — où `true` signifie que la valeur est valide et `false` qu'elle ne l'est pas. Utilisez-la pour les vérifications de valeurs autorisées, de format, de plages ou toute logique exprimable en JavaScript.

### Style d'erreur {#error-styling}

Chaque fois qu'un champ échoue à la validation, Braze ajoute la classe CSS `bz-validation-error` à l'élément correspondant à votre `selector` ou `element`, et supprime la classe lorsque le champ redevient valide. Stylisez l'état invalide comme vous le souhaitez, par exemple avec un contour ou une bordure qui attire l'attention sur le champ en erreur, en ajoutant une règle ciblant votre élément combiné avec la classe `bz-validation-error` :

```css
#my-custom-input.bz-validation-error {
  outline: 3px solid #f94144;
  outline-offset: 4px;
}
```

Styliser l'état d'erreur est optionnel mais recommandé, afin que les visiteurs puissent voir quel champ personnalisé bloque la soumission. Chaque [exemple](#examples) de cette page inclut une règle `bz-validation-error`.

## Bonnes pratiques {#best-practices}

- Utilisez un sélecteur stable et unique. Un `id` est le choix le plus sûr. Évitez les sélecteurs susceptibles de correspondre à plusieurs éléments.
- Renvoyez `null`, et non une chaîne vide ou `undefined`, lorsqu'il n'y a pas de valeur, afin que les vérifications de champs obligatoires se comportent de manière prévisible. Les chaînes vides et les tableaux vides sont également traités comme vides, mais `null` est le signal le plus clair pour « pas de valeur ».
- Gardez `getValue` peu coûteux et synchrone. Braze peut l'appeler plusieurs fois, il doit donc lire et renvoyer la valeur actuelle plutôt que d'effectuer un traitement lourd.
- Stylisez l'état `bz-validation-error` afin que les visiteurs puissent voir quel champ personnalisé bloque la soumission.
- Définissez vos noms d'attributs personnalisés à l'avance et gardez-les cohérents pour pouvoir segmenter de manière fiable sur ces données par la suite.
- Testez la soumission complète. Confirmez que l'attribut apparaît sur le profil utilisateur après la soumission, et que les règles de champs obligatoires et de validation bloquent la soumission comme prévu.

## Résolution des problèmes {#troubleshooting}

### Le formulaire se soumet même si rien n'a été sélectionné {#the-form-submits-even-though-nothing-was-selected}
Assurez-vous que `isRequired` est défini sur `true`. Braze traite `null`, `undefined`, les chaînes vides (y compris celles ne contenant que des espaces) et les tableaux vides comme une absence de valeur — si `getValue` renvoie autre chose (par exemple, une valeur par défaut non vide ou une marque substitutive) lorsque rien n'a été sélectionné, la vérification de champ obligatoire ne le détectera pas.

### La valeur n'apparaît pas sur le profil {#the-value-doesnt-appear-on-the-profile}
Confirmez que `onSubmit` appelle `window.brazeBridge.getUser().setCustomUserAttribute` avec le bon nom d'attribut, et que le bloc **Custom Code** se trouve sur la même page de destination que le formulaire.

### L'enregistrement ne semble rien faire {#registration-seems-to-do-nothing}
Vérifiez que le sélecteur correspond à un élément existant dans le DOM lorsque `registerFormInput` s'exécute, et que le script s'exécute après le rendu de cet élément. Ensuite, ouvrez la console de développement de votre navigateur : `registerFormInput` valide sa configuration et, en cas de problème (par exemple, un `getValue` manquant, un sélecteur qui n'est pas un sélecteur CSS valide ou une propriété du mauvais type), il ignore l'enregistrement et affiche un avertissement préfixé par `[brazeHelpers.forms.registerFormInput]` décrivant ce qui était invalide.

## Contenu associé {#related-content}

- [Pont JavaScript pour les pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) couvre la référence complète de `brazeBridge` utilisée dans `onSubmit`.
- [Créer des pages de destination]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)