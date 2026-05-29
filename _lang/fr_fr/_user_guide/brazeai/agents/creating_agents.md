---
nav_title: Créer des agents
article_title: Créer des agents personnalisés
description: "Découvrez comment créer des agents, ce qu'il convient de préparer avant de commencer et comment les mettre en œuvre dans les domaines de l'envoi de messages, de la prise de décision et de la gestion des données."
page_order: 1
alias: /creating-agents/
---

# Créer des agents personnalisés {#create-custom-agents}

> Découvrez comment créer des agents personnalisés, ce qu'il convient de préparer avant de commencer et comment les mettre en œuvre dans les domaines de l'envoi de messages, de la prise de décision et de la gestion des données. Pour des informations plus générales, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

- [L'autorisation]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) d'accéder à la **Console des agents** dans votre espace de travail. Vérifiez auprès de vos administrateurs Braze si cette option n'apparaît pas.
- L'autorisation de créer et de modifier des agents d'intelligence artificielle personnalisés.
- Une idée de ce que vous souhaitez que l'agent accomplisse. Les agents Braze peuvent prendre en charge les actions suivantes :
   - **Envoi de messages personnalisés :** Générer des lignes d'objet, des titres, des textes intégrés au produit ou tout autre contenu.
   - **Routage des utilisateurs :** Diriger les utilisateurs dans Canvas en fonction de leur comportement, de leurs préférences ou d'attributs personnalisés.
   - **Gestion des données :** Calculer des valeurs, enrichir les entrées du catalogue ou actualiser les champs du profil.

## Fonctionnement {#how-it-works}

Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous quant à son comportement. Une fois en production, l'agent peut être déployé dans Braze pour générer des textes personnalisés, prendre des décisions en temps réel ou mettre à jour les champs du catalogue. Pendant la création de votre agent, vous pouvez l'enregistrer en tant que brouillon, et vous pouvez suspendre ou mettre à jour un agent à tout moment depuis le tableau de bord.

Les cas d'utilisation suivants illustrent quelques façons de tirer parti des agents personnalisés.

| Cas d'utilisation | Description |
| --- | --- |
| Gestion des commentaires clients | Transmettez les commentaires des utilisateurs à un agent afin qu'il analyse le sentiment et génère des messages de suivi empathiques. Pour les utilisateurs à forte valeur, l'agent peut escalader la réponse ou inclure des avantages. |
| Localisation du contenu | Traduisez le texte du catalogue dans une autre langue pour les campagnes internationales, ou ajustez le ton et la longueur pour les canaux spécifiques à chaque région. Par exemple, traduisez « Classic Clubmaster Sunglasses » en espagnol par « Gafas de sol Classic Clubmaster », ou raccourcissez les descriptions pour les campagnes SMS. |
| Résumé des avis ou commentaires | Résumez le sentiment ou les commentaires dans un nouveau champ, par exemple en attribuant des scores de sentiment tels que Positif, Neutre ou Négatif, ou en rédigeant un bref résumé tel que « La plupart des clients mentionnent une excellente coupe, mais soulignent la lenteur de la livraison. » |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnement" }

## Créer un agent {#create-an-agent}

### Étape 1 : Choisir un type d'agent {#step-1-choose-an-agent-type}

Pour créer votre agent personnalisé :

1. Rendez-vous dans **Console des agents** > **Gestion des agents** dans le tableau de bord de Braze.
2. Sélectionnez **Créer un agent**.
3. Choisissez de créer un agent Canvas ou un agent catalogue.

### Étape 2 : Configurer les détails {#step-2-set-up-details}

Configurez ensuite les détails de votre agent :

1. Saisissez un nom et une description afin d'aider votre équipe à comprendre son objectif.
2. (Facultatif) Ajoutez des étiquettes pour filtrer votre agent.
3. Choisissez le [modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) que votre agent devra utiliser.
4. Si vous n'utilisez pas le modèle **Braze Auto**, sélectionnez le [niveau de réflexion]({{site.baseurl}}/user_guide/brazeai/agents/reference/#thinking-levels) du modèle. Vous avez le choix entre minimal, faible, moyen ou élevé. Nous vous recommandons de commencer par **Minimal**, de tester les réponses de votre agent, puis d'ajuster ce paramètre si nécessaire.
5. Définissez une limite d'invocations quotidienne. Par défaut, cette valeur est fixée à 250 000, mais elle peut être augmentée jusqu'à 1 000 000. Si vous souhaitez dépasser 1 000 000, contactez votre gestionnaire de la satisfaction client pour en savoir plus.

![Interface de la Console des agents pour la création d'un agent personnalisé dans Braze. L'écran affiche des champs permettant de saisir le nom et la description de l'agent, de sélectionner un modèle et de définir une limite d'invocations quotidienne.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Étape 3 : Rédiger les instructions {#agent-instructions}

Donnez des instructions à l'agent. Nous recommandons d'inclure des consignes sur la conduite à tenir dans des situations imprévues ou ambiguës, afin de minimiser le risque d'erreurs liées à la confusion de l'agent. Par exemple, plutôt que de demander à l'agent uniquement des valeurs de sentiment « positives » ou « négatives », demandez-lui de renvoyer « incertain » s'il ne parvient pas à se prononcer.

Consultez la section [Rédaction des instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) pour les bonnes pratiques et les [Exemples]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) pour trouver l'inspiration sur la manière de guider votre agent.

{% alert tip %}
Pour les agents Canvas, vous pouvez utiliser Liquid dans vos instructions afin de faire référence aux attributs utilisateur, tels que le prénom et le nom, ou à des attributs personnalisés. Toute variable Liquid présente dans les instructions de l'agent est automatiquement transmise à l'étape Agent lorsqu'un utilisateur y accède.
{% endalert %}

#### Ajouter du contexte {#add-resources}

Sélectionnez **+ Contexte de l'agent** pour choisir les éléments auxquels votre agent peut se référer. Cela inclut :

- [Champs du catalogue]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields) : Donnez à l'agent accès aux données de votre catalogue pour des réponses plus précises.
- [Appartenance à un segment]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context) : Permettez à l'agent de personnaliser les réponses en fonction des segments auxquels appartient l'utilisateur. Vous pouvez sélectionner jusqu'à cinq segments.
- [Directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) : Référencez les directives relatives au ton et au style de la marque que l'agent doit respecter. Par exemple, si vous souhaitez que votre agent génère un SMS pour encourager les utilisateurs à s'inscrire à une salle de sport, vous pouvez utiliser ce champ pour faire référence à votre directive prédéfinie, audacieuse et motivante.
- [Contexte Canvas complet]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) : Analysez toutes les données de contexte Canvas pour un utilisateur lorsque cet agent est invoqué, y compris les variables qui ne sont pas référencées dans la section **Instructions**.
- [Données d'interaction utilisateur]({{site.baseurl}}/user_guide/brazeai/agents/reference/#user-history) : Fournissez à l'agent les données récentes d'ouvertures, de clics et de conversions des Campaigns et Canvas de chaque utilisateur.

### Étape 4 : Sélectionner la sortie {#select-output}

Dans la section **Sortie**, vous pouvez organiser et définir la [sortie]({{site.baseurl}}/user_guide/brazeai/agents/reference/#outputs) de l'agent à l'aide de schémas de base ou de schémas avancés.

Pour obtenir les meilleurs résultats, assurez-vous que ce que vous spécifiez dans la section **Sortie** correspond aux instructions de l'agent saisies à l'[étape 3](#agent-instructions). Par exemple, si vous avez indiqué dans les instructions de l'agent que vous souhaitez un objet avec deux chaînes de caractères, veillez à spécifier un objet avec deux chaînes de caractères dans la section **Sortie**. Si les instructions de votre agent ne correspondent pas à la sortie spécifiée, l'agent risque d'être désorienté, d'expirer ou de générer des résultats indésirables.

{% alert tip %}
Lorsque vous utilisez un [schéma de sortie avancé]({{site.baseurl}}/user_guide/brazeai/agents/reference/#advanced-schemas), ajoutez un champ de type chaîne de caractères nommé `explanation` si vous souhaitez que l'agent renvoie son raisonnement en plus de ses autres sorties. Indiquez à l'agent dans vos [instructions](#agent-instructions) de renseigner `explanation` lorsque cela vous aide à vérifier ou déboguer les réponses.
{% endalert %}

### Étape 5 : Tester et créer l'agent {#step-5-test-and-create-the-agent}

Le volet **Prévisualisation** est une instance de l'agent qui s'affiche sous la forme d'un panneau côte à côte dans l'interface de configuration. Vous pouvez l'utiliser pour tester l'agent pendant que vous le créez ou le mettez à jour, afin de le découvrir de la même manière que les utilisateurs finaux. Cette étape vous permet de vérifier que tout fonctionne comme prévu et vous donne l'occasion d'effectuer des ajustements avant la mise en production.

1. Dans le champ **Testez votre agent**, saisissez des exemples de données clients ou de réponses clients — tout ce qui reflète des scénarios réels auxquels votre agent sera confronté.
2. Prévisualisez la réponse de l'agent pour un utilisateur aléatoire, un utilisateur existant ou un utilisateur personnalisé.
3. Sélectionnez **Simuler la réponse**. L'agent s'exécutera en fonction de votre configuration et affichera sa réponse.

{% alert note %}
Les essais comptent dans votre limite d'invocations quotidienne.
{% endalert %}

![Console des agents affichant le volet Prévisualisation pour tester un agent personnalisé. L'interface affiche un champ d'exemples d'entrées contenant des données clients, un bouton Lancer le test et une zone de réponse où s'affiche la sortie de l'agent.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Examinez attentivement le résultat. Posez-vous les questions suivantes :

- Le texte correspond-il à l'image de marque ?
- La logique décisionnelle oriente-t-elle les clients comme prévu ?
- Les valeurs calculées sont-elles exactes ?

Si quelque chose ne semble pas correct, mettez à jour la configuration de l'agent et réessayez. Testez plusieurs entrées différentes afin d'observer comment l'agent s'adapte à différents scénarios, en particulier les cas limites tels que l'absence de données ou les réponses non valides.

{% alert tip %}
Évitez d'indiquer à l'agent précisément ce que vous ne souhaitez pas qu'il fasse. Les LLM peuvent tout de même générer ce contenu si vous le mentionnez dans les instructions.
{% endalert %}

### Étape 6 : Utiliser votre agent {#step-6-use-your-agent}

Votre agent est désormais prêt à l'emploi ! Pour plus de détails, consultez [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Ressources connexes {#related-resources}

- [Article de référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Questions fréquentes]({{site.baseurl}}/user_guide/brazeai/agents/faq/)
- [Webinaire Braze sur l'intelligence artificielle en action : 3 nouveaux cas d'utilisation pour la personnalisation 1:1](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)