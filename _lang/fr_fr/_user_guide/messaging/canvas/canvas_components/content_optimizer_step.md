---
nav_title: Optimiseur de contenu
article_title: Étape d'agent Optimiseur de contenu
alias: "/content_optimizer_step/"
page_order: 5
description: "L'étape d'agent Optimiseur de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu au sein d'une même étape. Elle vous aide à expérimenter des variations de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps."
page_type: reference

---

# Étape d'agent Optimiseur de contenu {#content-optimizer-agent-step}

> L'étape d'agent Optimiseur de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu au sein d'une même étape. Elle vous aide à expérimenter des variations de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps. Pour une introduction, consultez [Optimiseur de contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
L'Optimiseur de contenu est actuellement en version bêta. Pour obtenir de l'aide pour démarrer, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Créer une étape Optimiseur de contenu {#creating-a-content-optimizer-step}

Pour de meilleurs résultats, utilisez l'agent Optimiseur de contenu dans des Canvas où les utilisateurs entrent dans l'étape progressivement au fil du temps. Si tous les utilisateurs entrent dans l'étape en même temps, l'agent n'aura pas le temps d'apprendre des premiers résultats.

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez-déposez le composant **Content Optimizer** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Content Optimizer**.

### Étape 2 : Créer votre message de base {#step-2-create-your-base-message}

Le message de base est le point de départ de votre étape. Les variantes de chaque composant de contenu sont insérées dynamiquement en fonction des combinaisons définies dans l'onglet **Content Optimizer Settings**.

{% alert note %}
Pendant la période bêta, les canaux pris en charge sont l'e-mail et les notifications push.
{% endalert %}

{% tabs local %}
{% tab E-mail %}

Depuis l'onglet **Messaging Channels**, sélectionnez **Email** et créez votre message e-mail de base. Consultez notre section dédiée [E-mail]({{site.baseurl}}/user_guide/channels/email/) pour obtenir de l'aide.

L'agent Optimiseur de contenu utilise les paramètres d'envoi (tels que le domaine d'e-mail et l'adresse de réponse) spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Notifications push %}

Depuis l'onglet **Messaging Channels**, sélectionnez **Push notifications** et créez votre notification push de base. Consultez notre section dédiée [Push]({{site.baseurl}}/user_guide/channels/push/) pour obtenir de l'aide.

L'agent Optimiseur de contenu utilise les plateformes push sélectionnées dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Title
- Message

{% endtab %}
{% endtabs %}

### Étape 3 : Spécifier les paramètres de distribution {#step-3-specify-delivery-settings}

Dans l'onglet **Delivery Settings**, vous pouvez indiquer si l'étape doit utiliser le timing intelligent ou les validations de distribution. Pour plus de détails, consultez [Modifier les paramètres de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) dans l'étape Message.

### Étape 4 : Ajouter des composants de contenu et des variantes {#step-4}

Les composants de contenu sont les éléments individuels de votre message que vous souhaitez tester, comme différentes lignes d'objet ou titres. Ces composants vous permettent de générer plusieurs versions d'un message et d'optimiser automatiquement en fonction des performances au fil du temps.

- **E-mail :** Vous pouvez ajouter jusqu'à trois composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 125 combinaisons de contenu uniques.
- **Notifications push :** Vous pouvez ajouter jusqu'à deux composants par étape et jusqu'à cinq variantes par composant, pour un total de 25 combinaisons de contenu uniques.

![Options pour ajouter et configurer des composants de contenu dans l'interface de l'Optimiseur de contenu. L'interface affiche des composants sélectionnables tels que Subject, Body Header, Body Content et Primary CTA, chacun avec des champs pour saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Étape 4.1 : Configurer les composants de contenu {#step-41-configure-content-components}

Pour configurer les composants, accédez à l'onglet **Content Optimizer Settings**.

{% tabs local %}
{% tab E-mail %}

Choisissez les composants que vous souhaitez optimiser pour les messages e-mail. Les options prises en charge sont :

- Subject
- Body Header
- Body Content
- Primary CTA

Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela aide l'Optimiseur de contenu à identifier plus efficacement les meilleures performances. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser des suggestions générées par l'intelligence artificielle pour explorer rapidement de nouvelles options.

![Interface Content Optimizer Settings montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des e-mails. Chaque composant dispose de champs de saisie pour entrer différentes variantes. Le texte visible inclut les noms des composants et les champs pour saisir le texte des variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notifications push %}

Choisissez les composants que vous souhaitez optimiser pour les notifications push. Les options prises en charge sont :
- Title
- Message

Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela aide l'Optimiseur de contenu à identifier plus efficacement les meilleures performances. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser des suggestions générées par l'intelligence artificielle pour explorer rapidement de nouvelles options.

![Paramètres de l'Optimiseur de contenu montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des notifications push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% endtabs %}

#### Étape 4.2 : Ajouter du Liquid à votre message {#step-42-add-liquid-to-your-message}

Après avoir défini au moins deux variantes pour chaque composant, copiez l'étiquette Liquid associée à chacun et collez-la à l'emplacement correspondant dans votre message de base.

- Par exemple, si vous optimisez la ligne d'objet, collez l'étiquette {% raw %}`{% message_component "Subject" %}`{% endraw %} dans le champ objet du compositeur d'e-mail.
- Vous pouvez également inclure des étiquettes de composant dans un texte plus long pour ne tester qu'une partie du composant. Par exemple : {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Options pour ajouter et configurer des composants de contenu tels que Subject, Body Header, Body Content et Primary CTA. Chaque composant dispose de champs pour saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si vous n'ajoutez pas d'étiquette Liquid pour un composant de contenu sélectionné, vous verrez un avertissement dans l'onglet **Content Optimizer Settings** et une erreur dans l'onglet **Messaging Channels**. Le Canvas ne peut pas être lancé tant que tous les composants sélectionnés ne sont pas correctement ajoutés à votre message de base.

Au fur et à mesure que le Canvas s'exécute, l'agent mélange et associe les variantes entre les composants pour générer différentes combinaisons de contenu. Au fil du temps, les combinaisons les plus performantes sont priorisées pour la distribution, ce qui vous permet d'améliorer les performances sans intervention manuelle.

#### Références Liquid {#liquid-references}

| Canal | Composant | Extrait de code Liquid |
| --- | --- | --- |
| E-mail | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-mail | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-mail | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-mail | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Références Liquid" }

### Étape 5 : Sélectionner l'événement d'optimisation {#step-5-select-optimization-event}

L'événement d'optimisation détermine comment l'agent Optimiseur de contenu évalue les performances et répartit le trafic entre les combinaisons de contenu au fil du temps.

L'événement d'optimisation sélectionné s'applique à tous les composants de contenu de cette étape.

{% tabs local %}
{% tab E-mail %}

Pour l'e-mail, vous pouvez optimiser pour l'un des événements suivants. L'agent utilise les ouvertures et les clics enregistrés dans les 7 jours suivant l'envoi d'un message pour orienter la distribution vers les combinaisons de contenu les plus performantes.

| Événement | Description | Cas d'utilisation |
| --- | --- | --- |
| Ouvertures | Optimise les combinaisons qui incitent les destinataires à ouvrir l'e-mail. | Test des lignes d'objet ou objectif d'augmentation de la visibilité |
| Clics | Optimise les combinaisons qui génèrent de l'engagement avec les liens. N'inclut pas les clics de bots ni les clics de désabonnement reconnus par Braze. | Génération de trafic, d'engagement ou de conversion à partir des liens |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 5 : Sélectionner l'événement d'optimisation" }

{% endtab %}
{% tab Notifications push %}

Pour les notifications push, vous pouvez optimiser les **ouvertures**. Cela optimise les combinaisons qui incitent les destinataires à ouvrir la notification push. Vous pouvez utiliser cet événement d'optimisation pour tester des variations de titre ou de texte du message.

{% endtab %}
{% endtabs %}

## Bonnes pratiques {#best-practices}

- De manière générale, nous recommandons de tester plus d'un composant pour l'étape Optimiseur de contenu.
- Si vous optimisez pour les clics, incluez les lignes d'objet dans vos tests, car des lignes d'objet plus percutantes peuvent contribuer à augmenter les ouvertures et créer davantage d'opportunités de clics.
- Si vous optimisez pour les ouvertures, concentrez vos tests sur la ligne d'objet.

## Analytique {#analytics}

Pour examiner les performances, ouvrez le panneau d'analytique au niveau de l'étape afin de consulter les indicateurs par variante de contenu et les performances globales des combinaisons. L'étape Optimiseur de contenu utilise la [même analytique que l'étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#analytics).

![Analytique de l'Optimiseur de contenu pour trois boutons et le pourcentage d'allocation des envois, qui tend à la hausse.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Pourquoi l'analytique de l'étape diffère de l'analytique générale {#why-step-analytics-differ-from-general-analytics}

Voici les raisons pour lesquelles l'analytique de l'étape Optimiseur de contenu diffère de la section **Analytics** :

- Les envois push sont dédupliqués pour les envois au même utilisateur sur différents appareils.
- De manière générale, les clics et les ouvertures sont dédupliqués pour être uniques par utilisateur.
- Seuls les clics et les ouvertures survenant dans les sept jours suivant l'envoi d'un message sont comptabilisés dans l'étape Optimiseur de contenu.

## Résolution des problèmes {#troubleshooting}

| Problème | Description | Solution |
| --- | --- | --- |
| Étiquettes Liquid manquantes | Si vous ajoutez un composant de contenu (comme Subject ou CTA) mais n'insérez pas l'étiquette Liquid correspondante dans votre message de base, vous verrez : <br>- Un avertissement dans l'onglet **Content Optimizer Settings** <br>- Une erreur dans l'onglet **Messaging Channels** | Copiez l'extrait de code Liquid affiché sous chaque composant dans l'onglet **Content Optimizer Settings** et collez-le dans la partie appropriée de votre message. |
| Étiquettes Liquid orphelines | Si vous supprimez un composant de contenu mais laissez son étiquette Liquid dans le message de base, le message risque de ne pas s'afficher correctement lors de l'envoi. | Supprimez toutes les étiquettes `message_component` inutilisées de votre message de base avant le lancement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Résolution des problèmes" }