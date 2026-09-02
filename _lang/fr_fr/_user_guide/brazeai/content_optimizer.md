---
nav_title: Optimiseur de contenu
article_title: Optimiseur de contenu
alias: "/content_optimizer/"
description: "L'Optimiseur de contenu vous aide à tester et à optimiser le contenu de vos messages à grande échelle, en utilisant l'IA pour générer et évaluer automatiquement de grands volumes de variantes de contenu."
page_type: reference
page_order: 3
---

# Optimiseur de contenu {#content-optimizer}

> L'Optimiseur de contenu vous aide à tester et à optimiser le contenu de vos messages à grande échelle, en utilisant l'IA pour générer et évaluer automatiquement de grands volumes de variantes de contenu.

{% alert important %}
L'Optimiseur de contenu est actuellement en version bêta et n'est disponible que pour les canaux suivants : e-mail, notifications push et messages SMS/MMS/RCS. Pour obtenir de l'aide pour démarrer, contactez votre gestionnaire du succès des clients.
{% endalert %}

## À propos de l'Otimisateur de Contenu {#about-content-optimizer}

L'Optimisateur de Contenu s'exécute dans une étape du Canvas. Il vous aide à définir les composants de message à tester, à générer des variantes à l'aide de l'IA générative ou d'une saisie manuelle, et à optimiser automatiquement les combinaisons de contenu envoyées aux utilisateurs. Cette fonctionnalité vous permet de :

- Optimiser les lignes d'objet, les en-têtes de corps, le contenu du corps ou le CTA principal pour les e-mails.
- Optimiser les titres et les messages pour les notifications push.
- Optimiser les accroches, les corps de message et les CTA pour les messages SMS, MMS et RCS.
- Améliorer continuellement les performances des messages sans configuration manuelle de tests A/B.
- Tester rapidement de grands volumes de variantes de contenu, en s'appuyant sur l'IA pour l'idéation.
- Retirer automatiquement le contenu peu performant et amplifier les variantes gagnantes.

Découvrez comment créer une [étape d'Optimisateur de Contenu]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

{% multi_lang_include brazeai/generative_ai/policy.md %}

### OpenAI et l'Optimisateur de Contenu {#openai-and-content-optimizer}

L'Optimisateur de Contenu utilise OpenAI uniquement lorsque vous demandez explicitement des suggestions de variantes générées par l'IA. Il n'utilise pas OpenAI pour choisir quelle variante chaque utilisateur reçoit ni pour répartir le trafic d'envoi.

- **Utilise OpenAI :** Lorsque vous sélectionnez **Générer des suggestions IA** pour un composant de contenu, Braze envoie votre variante initiale, vos instructions, une [directive de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) optionnelle, et (pour les étapes lancées avec suffisamment de données d'envoi) un contexte de performance agrégé à OpenAI afin de générer des idées de variantes.
- **Optimisation par bandit :** L'algorithme propriétaire de bandit multi-bras de Braze gère la répartition du trafic, la sélection de la variante au moment de l'envoi et l'optimisation basée sur les performances. Voir [Comment ça fonctionne](#how-it-works).
- **Saisie manuelle :** Vous pouvez définir des variantes en les saisissant vous-même sans envoyer de contenu à OpenAI.

## Cas d'usage {#use-cases}

### E-mail {#email}

| Cas d'usage d'optimisation | Objectif | Description |
| --- | --- | --- |
| Variations de la ligne d'objet | Augmenter le taux d'ouverture | Testez le ton, l'urgence, la personnalisation et l'utilisation d'emojis. |
| Styles de communication dans l'en-tête | Stimuler l'engagement | Comparez des messages émotionnels, axés sur la valeur et clairs dans l'en-tête du corps. |
| Format du contenu du corps | Améliorer la lisibilité et l'engagement | Testez le storytelling par rapport aux listes de fonctionnalités, les puces par rapport aux paragraphes et la longueur du contenu. |
| Texte et ton du CTA | Augmenter les clics | Comparez des formulations de CTA orientées action, axées sur les bénéfices et à la première personne. |
| Combinaisons de contenu thématique | Découvrir les combinaisons les plus performantes | Mélangez et associez des composants thématiques d'objet, de corps et de CTA pour trouver la meilleure combinaison globale. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="E-mail" }

### Notifications push {#push-notifications}

| Cas d'usage d'optimisation | Objectif | Description |
| --- | --- | --- |
| Variations du titre | Augmenter le taux d'ouverture | Testez la clarté, l'urgence, la personnalisation et le ton dans le titre de la notification push. |
| Styles du texte du corps | Améliorer l'engagement | Comparez des messages concis, axés sur les bénéfices et orientés action dans le corps de la notification push. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notifications push" }

### Messages SMS, MMS et RCS {#sms-mms-and-rcs-messages}

| Cas d'usage d'optimisation | Objectif | Description |
| --- | --- | --- |
| Variations de l'accroche | Augmenter l'engagement | Testez l'urgence, la personnalisation et le ton dans la première ligne affichée dans les aperçus SMS, les légendes MMS ou les introductions RCS. |
| Styles du texte du corps | Améliorer l'engagement | Comparez des messages concis et orientés action dans le corps, y compris le texte accompagnant les médias sur MMS et RCS. |
| Variations du texte du CTA | Augmenter les clics | Comparez des formulations de CTA orientées action et conversationnelles pour les liens et les invites d'étape suivante dans les SMS, MMS et RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages SMS, MMS et RCS" }

## Fonctionnement {#how-it-works}

L'algorithme bandit de Braze gère l'optimisation décrite dans cette section.

L'Optimiseur de contenu utilise un algorithme [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) non contextuel pour attribuer davantage d'envois aux variantes les plus performantes et réduire l'attribution aux variantes moins performantes. Au fil du temps, cela se traduit par une amélioration continue du contenu de vos messages, avec une intervention manuelle minimale.

L'algorithme d'optimisation bandit propriétaire de Braze est spécialement conçu pour la nature combinatoire de l'étape d'Optimiseur de contenu. Étant donné que chaque message est composé de plusieurs composants, l'algorithme apprend simultanément les performances de chaque composant (tel que la ligne d'objet, le corps du message, le CTA) ainsi que leurs interactions lorsqu'ils sont combinés dans un message. Plus concrètement, lorsqu'une combinaison donnée est envoyée, toutes les combinaisons partageant les mêmes composants bénéficient des données de cet envoi. Cela permet à l'algorithme d'apprendre beaucoup plus rapidement à partir d'une même quantité de données, par rapport à un algorithme bandit standard.

Lorsque l'étape est lancée pour la première fois, l'Optimiseur de contenu envoie des variantes de manière aléatoire afin de collecter des données de performance initiales. Après cette période d'exploration initiale, l'algorithme commence à rediriger le trafic vers les combinaisons de contenus les plus performantes, réduisant progressivement l'allocation aux options moins performantes. Pendant la période d'exploration, le trafic est généralement réparti entre les variantes disponibles afin de permettre à l'algorithme d'évaluer leurs performances relatives.

L'Optimiseur de contenu est similaire à l'étape Message dans Canvas, avec des fonctionnalités telles que les heures calmes, le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) et la journalisation des événements. Vous pouvez configurer une étape d'Optimiseur de contenu en créant un message de base et en définissant les composants de contenu (tels que la ligne d'objet, le corps du texte ou l'appel à l'action) à optimiser. Les variantes de chaque composant peuvent être générées par l'IA ou saisies manuellement, et des étiquettes Liquid doivent être ajoutées au message de base pour associer les composants au contenu du message.

Chaque utilisateur reçoit un seul message par entrée dans l'étape d'Optimiseur de contenu. Les réentrées sont traitées comme de nouvelles entrées, sans mémoire des variantes précédentes.

Pour attribuer les comportements en aval dans vos propres outils d'analyse, ajoutez une étiquette Liquid à votre message qui enregistre la combinaison reçue par chaque utilisateur. Pour en savoir plus, consultez [Jeton de combinaison]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#combination-token).

## Configuration de l'entrée Canvas {#canvas-entry-setup}

Pour de meilleurs résultats, utilisez l'Optimiseur de Contenu dans des Canvas où les utilisateurs entrent dans l'étape progressivement et régulièrement au fil du temps, comme dans des Canvas récurrents ou toujours actifs avec un volume quotidien constant. Si tous les utilisateurs entrent dans l'étape en même temps, l'Optimiseur de Contenu n'aura pas le temps d'apprendre des premiers résultats. L'étape se comportera davantage comme un test A/B statique que comme un moteur d'optimisation en direct or en ligne/en production/instantané.

L'Optimiseur de Contenu est idéal pour les Canvas à entrée récurrente quotidienne, ainsi que pour les Canvas déclenchés par événement et déclenchés par API avec des entrées utilisateur quotidiennes relativement constantes. Si vous utilisez l'Optimiseur de Contenu dans des Canvas à envoi unique ou des Canvas à entrée « irrégulière » (comme les récurrents mensuels), envisagez d'utiliser les [Contrôles d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) pour lisser les entrées utilisateur sur plusieurs jours.

### Concepts clés {#key-concepts}

| Terme                    | Description |
|-------------------------|-------------|
| Message de base   | Le modèle de message principal à partir duquel les variantes sont construites, incluant tous les paramètres d'envoi. |
| Composants de contenu  | Éléments au sein d'un message (par exemple, ligne d'objet ou CTA principal) qui peuvent être testés et optimisés. Les marketeurs doivent insérer l'étiquette Liquid correspondante dans le message à l'endroit où le composant doit apparaître. |
| Variantes de contenu    | Les différentes valeurs qu'un composant de contenu peut prendre. |
| Combinaisons de contenu | Messages uniques créés en mélangeant et associant des variantes de contenu. |
| Événement d'optimisation       | Détermine comment l'Optimiseur de Contenu évalue les performances et alloue le trafic aux combinaisons de contenu au fil du temps, comme les clics ou les ouvertures pour les e-mails. S'applique à tous les composants de contenu d'une étape. L'Optimiseur de Contenu apprend continuellement de cet événement et oriente automatiquement la distribution vers les combinaisons de contenu les plus performantes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Concepts clés" }

## Considérations {#considerations}

- L'Otimisateur de Contenu est actuellement en version bêta et n'est disponible que pour les canaux suivants : e-mail, notifications push et messages SMS/MMS/RCS.
- Pour les e-mails, l'Optimisateur de Contenu peut générer jusqu'à 125 combinaisons par étape :
   - Jusqu'à 3 composants par étape
   - Jusqu'à 5 variantes pour chaque composant
- Pour les notifications push, l'Optimisateur de Contenu peut générer jusqu'à 25 combinaisons par étape :
   - Jusqu'à 2 composants par étape
   - Jusqu'à 5 variantes pour chaque composant
- Pour les messages SMS, MMS et RCS, l'Optimisateur de Contenu peut générer jusqu'à 25 combinaisons par étape :
   - Jusqu'à 2 composants par étape
   - Jusqu'à 5 variantes pour chaque composant
- Un seul message est envoyé par utilisateur et par entrée. Il n'y a pas de mémoire des envois précédents pour les réentrées.
- Les marketeurs doivent insérer manuellement les étiquettes Liquid pour chaque composant dans le compositeur de messages, à l'endroit où les variantes de contenu définies doivent s'afficher.

## Étapes suivantes {#next-steps}

- Contactez votre gestionnaire du succès des clients pour rejoindre la bêta ou obtenir une assistance à l'onboarding.
- Découvrez comment créer une [étape d'Optimisation de contenu]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).