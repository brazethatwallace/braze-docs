---
nav_title: Optimiseur de contenu
article_title: Étape Optimiseur de contenu
alias: "/content_optimizer_step/"
page_order: 5
description: "L'étape Optimiseur de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu au sein d'une même étape. Elle vous aide à expérimenter des variations de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps."
page_type: reference

---

# Étape Optimiseur de contenu {#content-optimizer-step}

> L'étape Optimiseur de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu au sein d'une même étape. Elle vous aide à expérimenter des variations de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps. Pour une introduction, consultez [Optimiseur de contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer).

{% alert important %}
L'Optimiseur de contenu est actuellement en version bêta. Pour obtenir de l'aide pour démarrer, contactez votre CSM.
{% endalert %}

## Créer une étape Otimisateur de Contenu {#create-a-content-optimizer-step}

Pour de meilleurs résultats, utilisez l'Otimisateur de Contenu dans des Canvas où les utilisateurs entrent dans l'étape progressivement au fil du temps. Si tous les utilisateurs entrent dans l'étape en même temps, l'Otimisateur de Contenu n'aura pas le temps d'apprendre des premiers résultats.

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez et déposez le composant **Otimisateur de Contenu** depuis la barre latérale, ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> en bas d'une étape et sélectionnez **Otimisateur de Contenu**.

### Étape 2 : Créer votre message de base {#step-2-create-your-base-message}

Le message de base est le point de départ de votre étape. Les variantes de chaque composant de contenu sont insérées dynamiquement en fonction des combinaisons définies dans l'onglet **Content Optimizer Settings**.

{% alert note %}
Pendant la période bêta, les canaux pris en charge sont l'e-mail, les notifications push et les SMS/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab E-mail %}

Depuis l'onglet **Messaging Channels**, sélectionnez **Email** et créez votre message e-mail de base. Consultez notre section dédiée [E-mail]({{site.baseurl}}/user_guide/channels/email) pour obtenir de l'aide.

L'Otimisateur de Contenu utilise les paramètres d'envoi (tels que le domaine e-mail et l'adresse de réponse) spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Notifications push %}

Depuis l'onglet **Messaging Channels**, sélectionnez **Push notifications** et créez votre notification push de base. Consultez notre section dédiée [Push]({{site.baseurl}}/user_guide/channels/push) pour obtenir de l'aide.

L'Otimisateur de Contenu utilise les plateformes push sélectionnées et spécifiées dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Title
- Message

{% endtab %}
{% tab SMS/MMS/RCS %}

Depuis l'onglet **Messaging Channels**, sélectionnez **SMS/MMS/RCS** et créez votre message de base. Consultez notre section dédiée [SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) pour obtenir de l'aide.

L'Otimisateur de Contenu utilise les détails de **Content** et de **Message** spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Hook
- Body
- CTA

{% endtab %}
{% endtabs %}

### Étape 3 : Spécifier les paramètres de distribution {#step-3-specify-delivery-settings}

Dans l'onglet **Delivery Settings**, vous pouvez indiquer si l'étape doit utiliser le timing intelligent ou les validations de distribution. Pour plus de détails, consultez [Modifier les paramètres de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) dans l'étape Message.

### Étape 4 : Ajouter des composants de contenu et des variantes {#step-4}

Les composants de contenu sont les éléments individuels de votre message que vous souhaitez tester, tels que différentes lignes d'objet ou titres. Ces composants vous permettent de générer plusieurs versions d'un message et d'optimiser automatiquement en fonction des performances au fil du temps.

- **E-mail :** vous pouvez ajouter jusqu'à trois composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 125 combinaisons de contenu uniques.
- **Notifications push :** vous pouvez ajouter jusqu'à deux composants par étape et jusqu'à cinq variantes par composant, pour un total de 25 combinaisons de contenu uniques.
- **SMS/MMS/RCS :** vous pouvez ajouter jusqu'à deux composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 25 combinaisons de contenu uniques.

Lorsque vous utilisez **Generate AI suggestions**, Braze envoie le contenu à OpenAI pour générer des idées de variantes. L'allocation du trafic au moment de l'envoi n'utilise pas OpenAI. Pour plus de détails sur les données envoyées et leur utilisation, consultez [OpenAI et l'Otimisateur de Contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer).

![Options pour ajouter et configurer des composants de contenu dans l'interface de l'Otimisateur de Contenu. L'interface affiche des composants sélectionnables tels que Subject, Body Header, Body Content et Primary CTA, chacun avec des champs pour saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Étape 4.1 : Configurer les composants de contenu {#step-41-configure-content-components}

Pour configurer les composants, accédez à l'onglet **Content Optimizer Settings**.

{% tabs local %}
{% tab E-mail %}

Choisissez les composants que vous souhaitez optimiser pour les messages e-mail. Les options prises en charge sont :

- Subject
- Body Header
- Body Content
- Primary CTA

Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela aide l'Otimisateur de Contenu à identifier les meilleures performances plus efficacement. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser des suggestions générées par l'IA pour explorer rapidement de nouvelles options.

![Interface des paramètres de l'Otimisateur de Contenu montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des e-mails. Chaque composant dispose de champs de saisie pour entrer différentes variantes. Le texte visible inclut les noms des composants et les champs pour saisir le texte des variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notifications push %}

Choisissez les composants que vous souhaitez optimiser pour les notifications push. Les options prises en charge sont :
- Title
- Message

Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela aide l'Otimisateur de Contenu à identifier les meilleures performances plus efficacement. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser des suggestions générées par l'IA pour explorer rapidement de nouvelles options.

![Paramètres de l'Otimisateur de Contenu montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des notifications push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab SMS/MMS/RCS %}

Après avoir sélectionné votre groupe d'abonnement et le type de message (le cas échéant), choisissez les composants que vous souhaitez optimiser pour les SMS/MMS/RCS. Les options prises en charge sont :
- Hook
- Body
- CTA
{% alert note %}
Une fois qu'une étape Otimisateur de Contenu SMS/MMS/RCS est lancée, vous ne pouvez plus modifier le groupe d'abonnement ou le type de message.
{% endalert %}
Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela aide l'Otimisateur de Contenu à identifier les meilleures performances plus efficacement. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser des suggestions générées par l'IA pour explorer rapidement de nouvelles options.

![Paramètres de l'Otimisateur de Contenu montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des SMS/MMS/RCS.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### Étape 4.2 : Ajouter du Liquid à votre message {#step-42-add-liquid-to-your-message}

Après avoir défini au moins deux variantes pour chaque composant, copiez l'étiquette Liquid associée à chacun et collez-la à l'emplacement correspondant dans votre message de base.

- Par exemple, si vous optimisez la ligne d'objet, collez l'étiquette {% raw %}`{% message_component "Subject" %}`{% endraw %} dans le champ objet du compositeur d'e-mail.
- Vous pouvez également inclure des étiquettes de composant à l'intérieur d'un texte plus long pour tester seulement une portion du composant. Par exemple : {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Options pour ajouter et configurer des composants de contenu tels que Subject, Body Header, Body Content et Primary CTA. Chaque composant dispose de champs pour saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si vous n'ajoutez pas d'étiquette Liquid pour un composant de contenu sélectionné, vous verrez un avertissement dans l'onglet **Content Optimizer Settings** et une erreur dans l'onglet **Messaging Channels**. Le Canvas ne peut pas être lancé tant que tous les composants sélectionnés ne sont pas correctement ajoutés à votre message de base.

Au fur et à mesure que le Canvas s'exécute, l'Otimisateur de Contenu mélange et associe les variantes entre les composants pour générer différentes combinaisons de contenu. Au fil du temps, les combinaisons les plus performantes sont priorisées pour la distribution, vous aidant à améliorer les performances sans intervention manuelle.

#### Références Liquid {#liquid-references}

| Canal | Composant | Extrait Liquid |
| --- | --- | --- |
| E-mail | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| E-mail | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| E-mail | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| E-mail | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| SMS/MMS/RCS | Hook | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| SMS/MMS/RCS | Body | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| SMS/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Références Liquid" }

#### Jeton de combinaison {#combination-token}

Utilisez le jeton de combinaison pour enregistrer quelle combinaison de variantes un utilisateur a reçue. Ajoutez l'étiquette Liquid {% raw %}`{{component_combination_token}}`{% endraw %} à un lien dans votre message de base, puis utilisez la valeur dans vos propres outils d'analyse pour attribuer le comportement en aval à une combinaison spécifique.

Par exemple, ajoutez le jeton à un lien en tant que paramètre UTM :

{% raw %}
```liquid
https://www.example.com/summer-sale?utm_content={{component_combination_token}}
```
{% endraw %}

L'étiquette génère une chaîne de nombres séparés par des underscores, telle que `3_2_8` :

- Chaque position correspond à un composant de contenu, dans l'ordre d'apparition des composants dans l'onglet **Content Optimizer Settings**.
- Chaque nombre est l'index de la variante que l'utilisateur a reçue pour ce composant. Les index commencent à 0, donc `0` est la première variante créée pour ce composant, `1` est la deuxième, et ainsi de suite.

Braze attribue un index à une variante lorsque vous la créez et conserve cet index pendant toute la durée de vie de l'étape. Vous pouvez désactiver une variante, mais vous ne pouvez pas la supprimer, et les index ne sont jamais réutilisés ou renumérotés. Un index ne reflète pas la position de la variante parmi les variantes actuellement actives.

Pour cette raison, les index peuvent dépasser la limite de cinq variantes par composant. Cette limite s'applique uniquement aux variantes actives, donc si vous désactivez plusieurs variantes et en ajoutez de nouvelles, les nouvelles variantes peuvent avoir des index tels que 5, 6, 7 et 8.

Par exemple, une étape e-mail optimise une ligne d'objet et un CTA principal. Le composant objet a été lancé avec cinq variantes. Trois ont été désactivées ultérieurement et trois nouvelles ont été ajoutées :

| Variante d'objet | Index | Statut |
| --- | --- | --- |
| Your summer sale starts now | 0 | Désactivée |
| Summer sale: 20% off | 1 | Désactivée |
| 20% off, this week only | 2 | Désactivée |
| Save 20% on summer picks | 3 | Active |
| Your 20% off code is inside | 4 | Active |
| Summer picks, 20% off | 5 | Active |
| Don't miss 20% off | 6 | Active |
| Last chance: 20% off summer | 7 | Active |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Index des variantes d'objet" }

Le composant CTA principal possède deux variantes, avec les index 0 et 1. Dans cette étape, un jeton de `6_1` signifie que l'utilisateur a reçu la variante d'objet avec l'index 6 (« Don't miss 20% off ») et la variante de CTA principal avec l'index 1.

### Étape 5 : Sélectionner l'événement d'optimisation {#step-5-select-optimization-event}

L'événement d'optimisation détermine comment l'Otimisateur de Contenu évalue les performances et alloue le trafic aux combinaisons de contenu au fil du temps.

L'événement d'optimisation sélectionné s'applique à tous les composants de contenu de cette étape.

{% tabs local %}
{% tab E-mail %}

Pour l'e-mail, vous pouvez optimiser pour l'un des événements suivants. L'Otimisateur de Contenu utilise les ouvertures et les clics enregistrés dans les 7 jours suivant l'envoi d'un message pour orienter la distribution vers les combinaisons de contenu les plus performantes.

| Événement | Description | Cas d'usage |
| --- | --- | --- |
| Ouvertures | Optimise pour les combinaisons qui incitent les destinataires à ouvrir l'e-mail. | Tester les lignes d'objet ou chercher à augmenter la visibilité |
| Clics | Optimise pour les combinaisons qui favorisent l'engagement avec les liens. N'inclut pas les clics de bots ni les clics de désabonnement reconnus par Braze. | Générer du trafic, de l'engagement ou des conversions à partir des liens |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 5 : sélectionner l'événement d'optimisation" }

#### Exclure des liens de l'optimisation {#exclude-links-from-optimization}

Lorsque vous optimisez pour les clics, vous pouvez exclure un ou plusieurs liens de l'optimisation. Utilisez cette option pour les liens qui ne signalent pas un engagement avec le contenu que vous testez, comme un centre de préférences ou un localisateur de magasins.

Pour exclure un lien, accédez à l'onglet **Content Optimizer Settings** et ajoutez l'URL du lien. Braze effectue une correspondance sur le préfixe, donc un clic sur n'importe quelle URL de votre message commençant par l'URL que vous spécifiez est exclu.

Les clics exclus ne comptent pas dans l'événement d'optimisation, ils n'influencent donc pas les combinaisons que l'Otimisateur de Contenu favorise. Ils sont toutefois comptabilisés dans les analyses globales de l'étape, et ils ne sont pas comptés dans les tableaux [Performance par composant](#performance-by-component) ou [Performance par combinaison](#performance-by-combination).

{% endtab %}
{% tab Notifications push %}

Pour les notifications push, vous pouvez optimiser les **ouvertures**. Cela optimise les combinaisons qui incitent les destinataires à ouvrir la notification push. Vous pouvez utiliser cet événement d'optimisation pour tester des variations de titre ou de texte du message.

{% endtab %}
{% tab SMS/MMS/RCS %}

Pour les messages SMS et MMS, vous pouvez optimiser les **clics**. Pour les messages RCS, vous pouvez optimiser les **lectures** ou les **clics**.

Pour que l'étape dispose d'un événement à optimiser :
- Les messages SMS et MMS doivent contenir un lien.
- Les messages RCS doivent contenir un lien ou une réponse suggérée.

{% alert note %}
À l'heure actuelle, la messagerie RCS avec l'Otimisateur de Contenu ne prend pas en charge les replis SMS.
{% endalert %}
{% endtab %}
{% endtabs %}

## États des étapes {#step-states}

Lorsqu'une étape Content Optimizer s'exécute, Braze évalue les performances des variantes de contenu et attribue à l'étape l'un des trois états suivants, visibles dans le Canvas.

| État | Signification |
| --- | --- |
| Apprentissage | Content Optimizer collecte encore des données de performance sur vos variantes de contenu et n'a pas encore trouvé de gagnant fiable et cohérent. |
| Optimisation | Content Optimizer a identifié des variantes qui surpassent régulièrement les autres et oriente la distribution vers les combinaisons gagnantes. |
| Action recommandée | L'étape s'exécute depuis un moment sans qu'un gagnant clair ne se dégage. Vérifiez la configuration de votre étape pour aider Content Optimizer à en trouver un. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États des étapes Content Optimizer" }

### Actions à envisager {#actions-to-consider}

Si votre étape passe à l'état Action recommandée, envisagez les actions suivantes :

- Augmentez le nombre d'utilisateurs qui entrent dans le Canvas, si possible. Plus d'envois donnent à Content Optimizer davantage de données pour apprendre.
- En général, testez plus de combinaisons plutôt que moins (voir [Bonnes pratiques](#best-practices)). Cela donne à Content Optimizer un signal plus clair sur ce qui fonctionne. Si le volume de votre audience est faible (en moyenne moins d'environ 3 000 envois par jour), envisagez plutôt de réduire légèrement le nombre de variantes, car trop de combinaisons par rapport à votre volume peut ralentir l'apprentissage.
- Rendez vos variantes de contenu plus clairement distinctes les unes des autres en termes de ton, de structure ou de contenu.
- Si vous ne pouvez pas augmenter votre audience et que le nombre de variantes et la diversité du contenu semblent déjà appropriés, votre étape a peut-être simplement besoin de plus de temps pour identifier les gagnants.

## Modifier une étape lancée {#edit-a-launched-step}

Une fois votre Canvas lancé, vous pouvez mettre à jour une étape Otimisateur de Contenu en cours d'exécution en l'ouvrant dans l'éditeur de Canvas. Vous pouvez :

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

{% alert note %}
Braze attribue à chaque utilisateur une combinaison de contenu lorsqu'il entre dans l'étape Otimisateur de Contenu. Si son envoi est retardé par des contrôles de distribution tels que la limitation du débit, le timing intelligent ou les heures calmes, il peut tout de même recevoir une variante que vous avez désactivée. Pour arrêter ces envois de manière urgente, suivez les mêmes étapes que pour une étape Message. Pour en savoir plus, consultez la section [Arrêter des Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).
{% endalert %}

Lorsque vous publiez des modifications, l'optimiseur se réinitialise et commence à réallouer le trafic depuis le début entre toutes les variantes et combinaisons actives. Évitez de mettre à jour les variantes lorsque l'étape est en phase d'apprentissage. Les données historiques antérieures à la modification sont conservées et consultables dans l'onglet **Content Analytics**.

Les paramètres suivants ne peuvent pas être modifiés après le lancement :

- Le contenu des variantes actives existantes
- Les composants testés
- L'événement d'optimisation

Pour les étapes SMS/MMS/RCS, le groupe d'abonnement et le type de message ne peuvent pas non plus être modifiés après le lancement.

## Bonnes pratiques {#best-practices}

- De manière générale, testez davantage de composants plutôt que moins pour l'étape Content Optimizer. Par exemple, au lieu de tester deux composants pour l'e-mail, testez-en trois.
- Tester au moins 10 combinaisons au total donne généralement de meilleurs résultats.
- Pour l'e-mail, les étapes qui optimisent pour les clics ont tendance à surpasser celles qui optimisent pour les ouvertures. Lorsque les clics correspondent à votre cas d'usage, choisissez les clics comme événement d'optimisation.
- Si c'est la première fois que vous utilisez Content Optimizer, envisagez d'utiliser une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) afin que seule une partie de votre audience entre dans la branche contenant l'étape Content Optimizer. Par exemple, vous pourriez envoyer la moitié de vos utilisateurs sur un chemin avec l'étape Content Optimizer et l'autre moitié sur un chemin de contrôle qui envoie l'étape de message avec votre contenu habituel. Ensuite, recueillez des données pendant 2 à 3 semaines et comparez les indicateurs clés de performance (KPI) ou les contre-indicateurs avant d'augmenter le trafic vers les chemins comportant des étapes Content Optimizer.
  - Pour une comparaison efficace en tête-à-tête, incluez votre contenu habituel comme l'une des variantes pour chaque composant dans votre étape Content Optimizer.
- Lorsque vous êtes prêt à effectuer des mises à jour après que votre étape Content Optimizer est restée dans l'état d'optimisation pendant un certain temps, désactivez les variantes peu performantes et ajoutez-en de nouvelles qui s'appuient sur les caractéristiques de vos meilleures variantes.

## Considérations {#considerations}

- Les paramètres multilingues ne sont pas pris en charge dans les étapes Content Optimizer. Utilisez plutôt une étape Content Optimizer par langue et créez des chemins de branchement individuels.
- Les étiquettes Liquid pour les composants Content Optimizer ne sont pas prises en charge dans les étapes Message, de sorte que le Liquid s'interrompt dans les étapes Message.
- Une fois qu'une étape Content Optimizer est lancée, vous ne pouvez pas modifier les composants testés, le contenu des variantes actives existantes ni l'événement d'optimisation. Pour les étapes SMS/MMS/RCS, le groupe d'abonnement et le type de message ne peuvent pas non plus être modifiés.

## Analyse {#analytics}

Pour examiner les performances, ouvrez le panneau d'analyse au niveau de l'étape afin de consulter les indicateurs par variante de contenu et les performances globales des combinaisons. L'étape Content Optimizer utilise les [mêmes analyses que l'étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Si vous avez mis à jour l'étape après le lancement, le graphique d'allocation des envois indique le moment où chaque modification de contenu a eu lieu. Les données des variantes désactivées sont conservées et restent consultables dans le panneau d'analyse, ce qui vous permet de comparer les performances sur toute la durée de vie de l'étape.

![Analyse du Content Optimizer pour trois boutons et le pourcentage d'allocation des envois, avec une tendance à la hausse.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Performances par composant {#performance-by-component}

La section **Performances par composant** affiche les performances de chaque composant dans l'étape Content Optimizer. La colonne **Composant** correspond au composant de contenu que vous testez (par exemple, **Ligne d'objet** ou **CTA principal**). La colonne **Identifiant** correspond à l'identifiant de cette variante dans l'onglet **Paramètres du Content Optimizer**.

Les ouvertures et clics uniques sont comptabilisés dans les sept jours suivant l'envoi d'un message. Les colonnes affichées dépendent de votre canal et de l'événement d'optimisation sélectionné.

| Indicateur | Description |
| --- | --- |
| Envois | Le nombre d'envois attribués à cette variante pour ce composant dans cette étape, en utilisant le même comptage des envois au niveau de l'étape que [*Envois*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) dans le tableau [Performances par combinaison](#performance-by-combination). |
| Ouvertures | Lorsque cette colonne apparaît pour votre canal, le nombre d'ouvertures **uniques** pour cette variante dans les sept jours suivant l'envoi. Voir [*Ouvertures uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taux d'ouverture | Lorsque cette colonne apparaît, le pourcentage d'envois pour cette variante ayant enregistré au moins une ouverture unique qualifiée dans les sept jours. |
| Clics | Le nombre de clics **uniques** pour cette variante dans les sept jours suivant l'envoi. Voir [*Clics totaux*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Clics uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks), et [Étape 5 : Sélectionner l'événement d'optimisation](#step-5-select-optimization-event). |
| Taux de clics | Le pourcentage d'envois pour cette variante ayant enregistré au moins un clic unique qualifié dans les sept jours, en utilisant la même fenêtre d'étape que le tableau [Performances par combinaison](#performance-by-combination). Pour en savoir plus, consultez [Pourquoi les analyses de l'étape diffèrent des analyses générales](#why-step-analytics-differ-from-general-analytics). |
| Lectures | Lorsque cette colonne apparaît (par exemple, pour le RCS lorsque vous optimisez pour les lectures), comptabilise le moment où un consommateur lit le message avec les accusés de lecture activés. Voir [*Lectures*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Taux de lecture | Le pourcentage d'envois pour cette variante ayant abouti à une lecture parmi les utilisateurs dont les accusés de lecture sont activés. Voir [*Taux de lecture*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs de performances par composant" }

![Analyse des performances par composant du Content Optimizer avec des tableaux distincts par composant, indiquant les envois, les clics et le taux de clics pour chaque variante.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Performances par combinaison {#performance-by-combination}

La section **Performances par combinaison** affiche les performances de chaque combinaison dans l'étape Content Optimizer. Les combinaisons correspondent à l'ensemble de variantes qui définissent cette ligne — une variante sélectionnée pour chaque composant de contenu que vous testez (par exemple, une ligne d'objet associée à un CTA principal).

Les ouvertures et clics uniques sont comptabilisés dans les sept jours suivant l'envoi d'un message. Les colonnes affichées dépendent de votre canal et de l'événement d'optimisation sélectionné.

| Indicateur | Description |
| --- | --- |
| Envois | Le nombre total de messages envoyés depuis cette étape en utilisant cette combinaison. Le comptage suit la même signification générale que [*Envois*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), limité à chaque combinaison. |
| Ouvertures | Le nombre d'ouvertures uniques pour cette combinaison dans les sept jours suivant l'envoi. Pour savoir comment les ouvertures uniques sont définies pour l'e-mail, consultez [*Ouvertures uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taux d'ouverture | Le pourcentage d'envois pour cette combinaison ayant enregistré au moins une ouverture unique qualifiée dans les sept jours. |
| Clics | Le nombre de clics uniques pour cette combinaison dans les sept jours suivant l'envoi. Pour savoir comment Braze définit les clics par canal, consultez [*Clics totaux*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) et [*Clics uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Taux de clics | Le pourcentage d'envois pour cette combinaison ayant enregistré au moins un clic unique qualifié dans les sept jours. Étant donné que le Content Optimizer utilise les comptages dédupliqués sur sept jours de l'étape, ce taux peut ne pas correspondre aux taux de clics dans les analyses générales de Campaign. Pour en savoir plus, consultez [Pourquoi les analyses de l'étape diffèrent des analyses générales](#why-step-analytics-differ-from-general-analytics). |
| [Lectures]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Lorsque cette colonne apparaît (par exemple, pour le RCS lorsque vous optimisez pour les lectures), comptabilise le moment où un consommateur lit le message avec les accusés de lecture activés. |
| [Taux de lecture]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Lorsque cette colonne apparaît, le pourcentage d'envois pour cette combinaison ayant abouti à une lecture parmi les utilisateurs dont les accusés de lecture sont activés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs de performances par combinaison" }

![Tableau d'analyse des performances par combinaison du Content Optimizer avec les envois, les clics et le taux de clics pour chaque combinaison de contenu.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### Pourquoi les analyses de l'étape diffèrent des analyses générales {#why-step-analytics-differ-from-general-analytics}

Voici pourquoi les analyses de l'étape Content Optimizer diffèrent de la section **Analytics** :

- Les envois push sont dédupliqués pour les envois au même utilisateur sur différents appareils.
- De manière générale, les clics et les ouvertures sont dédupliqués pour être uniques par utilisateur.
- Seuls les clics et les ouvertures survenant dans les sept jours suivant l'envoi d'un message sont comptabilisés dans l'étape Content Optimizer.
- Les clics sur les liens exclus sont comptabilisés dans les analyses totales de l'étape, mais ne sont pas comptabilisés dans les tableaux **Performances par composant** ou **Performances par combinaison**. Pour en savoir plus, consultez [Exclure des liens de l'optimisation](#exclude-links-from-optimization).

### Consulter les variantes sur un profil utilisateur {#view-variants-on-a-user-profile}

Pour voir quelles variantes un utilisateur individuel a reçues, ouvrez son profil utilisateur et accédez à l'onglet **Historique des messages**. Sur la ligne de l'événement d'envoi correspondant à une étape Content Optimizer, le tableau affiche les variantes de composant envoyées à cet utilisateur. Pour en savoir plus, consultez [Onglet Historique des messages]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab).

### Comparer les étapes dans le générateur de rapports {#compare-steps-in-report-builder}

Pour comparer les performances de plusieurs étapes Content Optimizer, créez un rapport et sélectionnez **Canvas Step with Canvas Optimizer**. Le rapport affiche les performances de l'étape par composant et par combinaison pour les étapes que vous incluez, que ces étapes se trouvent dans le même Canvas ou dans des Canvas différents. Pour en savoir plus, consultez [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

## Résolution des problèmes {#troubleshooting}

| Problème | Description | Solution |
| --- | --- | --- |
| Étiquettes Liquid manquantes | Si vous ajoutez un composant de contenu (tel que l'objet ou le CTA) sans insérer l'étiquette Liquid correspondante dans votre message de base, vous verrez : <br>- Un avertissement dans l'onglet **Content Optimizer Settings** <br>- Une erreur dans l'onglet **Messaging Channels** | Copiez l'extrait Liquid affiché sous chaque composant dans l'onglet **Content Optimizer Settings** et collez-le dans la partie appropriée de votre message. |
| Étiquettes Liquid orphelines | Si vous supprimez un composant de contenu mais laissez son étiquette Liquid dans le message de base, le message peut ne pas s'afficher comme prévu lors de l'envoi. | Supprimez toutes les étiquettes `message_component` inutilisées de votre message de base avant le lancement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Résolution des problèmes" }