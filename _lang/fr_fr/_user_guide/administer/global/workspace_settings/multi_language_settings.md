---
nav_title: Paramètres de localisation
article_title: Paramètres de localisation
alias: "/multi_language_support/"
page_order: 4
description: "Cet article donne un aperçu des paramètres multilingues du tableau de bord de Braze et explique comment utiliser les paramètres régionaux dans vos messages."
---

# Paramètres de localisation {#localization-settings}

> La fonctionnalité multilingue vous permet d'utiliser des [étiquettes de traduction]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) pour cibler des utilisateurs de différentes langues et provenant de différents emplacements, le tout dans un seul message.

## Conditions préalables {#prerequisites}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

## Ajouter un paramètre régional {#add-a-locale}

1. Accédez à **Paramètres** > **Paramètres de localisation**.
2. Sélectionnez **Add locale**, puis choisissez **Default locale** ou **Custom Attributes**.
3. Saisissez un nom pour le paramètre régional.
4. [Sélectionnez une langue pour l'accessibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility). Ce paramètre permet aux technologies d'assistance, comme les lecteurs d'écran, de prononcer correctement le texte.
5. Sélectionnez les attributs utilisateur correspondant à l'option de paramètre régional que vous avez choisie. Lors de la configuration d'un paramètre régional, vous pouvez sélectionner des langues à partir des attributs utilisateur par défaut ou des attributs personnalisés. Vous ne pouvez pas sélectionner les deux à la fois.

{% tabs %}
{% tab Paramètres régionaux par défaut %}

Pour les **paramètres régionaux par défaut**, utilisez les listes déroulantes pour sélectionner la langue à ajouter et, éventuellement, le pays à associer à la langue.

![Une fenêtre intitulée « Add locale - Default Language and Country » pour spécifier la langue et le pays.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Attributs personnalisés %}

Pour les **attributs personnalisés**, utilisez la liste déroulante pour sélectionner l'attribut personnalisé associé, puis saisissez la valeur dans le champ de texte.

![Une fenêtre intitulée « Add locale - Custom Attributes » pour spécifier l'attribut personnalisé et la valeur.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Sélectionnez **Add locale**.

Pour savoir comment utiliser ces paramètres régionaux dans vos messages, consultez [Utiliser les paramètres régionaux]({{site.baseurl}}/locales_in_messages).

## Points à prendre en compte {#considerations}

- Vous pouvez sélectionner jusqu'à deux attributs personnalisés dans un seul paramètre régional, ou jusqu'à deux langues d'attributs utilisateur par défaut. Dans les deux cas, le second attribut est facultatif.
- Lorsque vous modifiez les valeurs traduites dans le fichier CSV, évitez de modifier les valeurs par défaut du fichier.
- La clé du paramètre régional dans votre fichier importé doit correspondre à celle de vos paramètres multilingues.

### Assistance et priorisation {#support-and-prioritization}

- Si un utilisateur correspond à la fois à un paramètre régional défini par des attributs personnalisés et à un paramètre régional défini par des attributs utilisateur par défaut, le paramètre régional basé sur les attributs personnalisés est prioritaire.
- Les attributs personnalisés prennent en charge les valeurs textuelles (chaînes de caractères) avec correspondance exacte.
- Si un attribut personnalisé est supprimé ou si son type est modifié, l'utilisateur ne peut plus correspondre à ce paramètre régional et sera soit redirigé vers le paramètre régional suivant dans la liste de priorité, soit recevra les traductions marketing par défaut.
- Si un paramètre régional est invalide (l'attribut personnalisé a été modifié ou supprimé), l'erreur apparaîtra sur la page **Prise en charge multilingue**.

## Foire aux questions {#frequently-asked-questions}

### Combien de paramètres régionaux puis-je ajouter ? {#how-many-locales-can-i-add}

Vous pouvez ajouter jusqu'à 200 paramètres régionaux.

### Où les fichiers de traduction sont-ils stockés dans Braze ? {#where-are-the-translation-files-stored-in-braze}

Les fichiers de traduction sont stockés au niveau de la campagne, ce qui signifie que chaque variante de message doit disposer de traductions importées. Les traductions peuvent également être stockées dans des Content Blocks. Lorsqu'un bloc est ajouté à un message, ses traductions sont automatiquement incluses.

### Le nom du paramètre régional doit-il suivre un format ou un modèle spécifique ? {#does-the-locale-name-have-to-follow-a-specific-pattern-or-format}

Non. Vous pouvez utiliser la convention de nommage de votre choix. Le nom du paramètre régional est utilisé lors de la sélection du paramètre régional dans l'éditeur et apparaîtra dans les en-têtes du fichier que vous téléchargez avec les ID de traduction.