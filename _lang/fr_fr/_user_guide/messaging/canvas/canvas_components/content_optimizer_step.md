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

## Créer une étape Optimiseur de contenu {#create-a-content-optimizer-step}

Pour de meilleurs résultats, utilisez l'Optimiseur de contenu dans des Canvas où les utilisateurs entrent dans l'étape progressivement au fil du temps. Si tous les utilisateurs entrent dans l'étape en même temps, l'Optimiseur de contenu n'aura pas le temps d'apprendre des premiers résultats.

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez-déposez le composant **Content Optimizer** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Content Optimizer**.

### Étape 2 : Créer votre message de base {#step-2-create-your-base-message}

Le message de base est le point de départ de votre étape. Les variantes de chaque composant de contenu sont insérées dynamiquement en fonction des combinaisons définies dans l'onglet **Content Optimizer Settings**.

{% alert note %}
Pendant la période bêta, les canaux pris en charge sont l'e-mail, les notifications push et les SMS/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab E-mail %}

Depuis l'onglet **Messaging Channels**, sélectionnez **Email** et créez votre message e-mail de base. Consultez notre section dédiée [E-mail]({{site.baseurl}}/user_guide/channels/email) pour obtenir de l'aide.

L'Optimiseur de contenu utilise les paramètres d'envoi (tels que le domaine d'e-mail et l'adresse de réponse) spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Notifications push %}

Depuis l'onglet **Messaging Channels**, sélectionnez **Push notifications** et créez votre notification push de base. Consultez notre section dédiée [Push]({{site.baseurl}}/user_guide/channels/push) pour obtenir de l'aide.

L'Optimiseur de contenu utilise les plateformes push sélectionnées dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Title
- Message

{% endtab %}
{% tab SMS/MMS/RCS %}

Depuis l'onglet **Messaging Channels**, sélectionnez **SMS/MMS/RCS** et créez votre message de base. Consultez notre section dédiée [SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) pour obtenir de l'aide.

L'Optimiseur de contenu utilise les détails de **Content** et de **Message** spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définissez à l'[étape 4](#step-4).

Les composants pris en charge pour l'optimisation incluent :

- Hook
- Body
- CTA

{% endtab %}
{% endtabs %}

### Étape 3 : Spécifier les paramètres de distribution {#step-3-specify-delivery-settings}

Dans l'onglet **Delivery Settings**, vous pouvez indiquer si l'étape doit utiliser le timing intelligent ou les validations de distribution. Pour plus de détails, consultez [Modifier les paramètres de distribution]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) dans l'étape Message.

### Étape 4 : Ajouter des composants de contenu et des variantes {#step-4}

Les composants de contenu sont les éléments individuels de votre message que vous souhaitez tester, comme différentes lignes d'objet ou titres. Ces composants vous permettent de générer plusieurs versions d'un message et d'optimiser automatiquement en fonction des performances au fil du temps.

- **E-mail :** vous pouvez ajouter jusqu'à trois composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 125 combinaisons de contenu uniques.
- **Notifications push :** vous pouvez ajouter jusqu'à deux composants par étape et jusqu'à cinq variantes par composant, pour un total de 25 combinaisons de contenu uniques.
- **SMS/MMS/RCS :** vous pouvez ajouter jusqu'à deux composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 25 combinaisons de contenu uniques.

Lorsque vous utilisez **Generate AI suggestions**, Braze envoie le contenu à OpenAI pour générer des idées de variantes. L'allocation du trafic au moment de l'envoi n'utilise pas OpenAI. Pour en savoir plus sur les données envoyées et leur utilisation, consultez [OpenAI et l'Optimiseur de contenu]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer).

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
  - Utiliser des suggestions générées par l'IA pour explorer rapidement de nouvelles options.

![Interface Content Optimizer Settings montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des e-mails. Chaque composant dispose de champs de saisie pour entrer différentes variantes. Le texte visible inclut les noms des composants et les champs pour saisir le texte des variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notifications push %}

Choisissez les composants que vous souhaitez optimiser pour les notifications push. Les options prises en charge sont :
- Title
- Message

Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela aide l'Optimiseur de contenu à identifier plus efficacement les meilleures performances. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser des suggestions générées par l'IA pour explorer rapidement de nouvelles options.

![Paramètres de l'Optimiseur de contenu montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des notifications push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab SMS/MMS/RCS %}

Après avoir sélectionné votre groupe d'abonnement et le type de message (le cas échéant), choisissez les composants que vous souhaitez optimiser pour les SMS/MMS/RCS. Les options prises en charge sont :
- Hook
- Body
- CTA
{% alert note %}
Une fois qu'une étape Optimiseur de contenu SMS/MMS/RCS est lancée, vous ne pouvez plus modifier le groupe d'abonnement ni le type de message.
{% endalert %}
Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela aide l'Optimiseur de contenu à identifier plus efficacement les meilleures performances. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser des suggestions générées par l'IA pour explorer rapidement de nouvelles options.

![Paramètres de l'Optimiseur de contenu montrant les options pour ajouter et configurer des composants de contenu pour l'optimisation des SMS/MMS/RCS.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### Étape 4.2 : Ajouter du Liquid à votre message {#step-42-add-liquid-to-your-message}

Après avoir défini au moins deux variantes pour chaque composant, copiez l'étiquette Liquid associée à chacun et collez-la à l'emplacement correspondant dans votre message de base.

- Par exemple, si vous optimisez la ligne d'objet, collez l'étiquette {% raw %}`{% message_component "Subject" %}`{% endraw %} dans le champ objet du compositeur d'e-mail.
- Vous pouvez également inclure des étiquettes de composant dans un texte plus long pour ne tester qu'une partie du composant. Par exemple : {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Options pour ajouter et configurer des composants de contenu tels que Subject, Body Header, Body Content et Primary CTA. Chaque composant dispose de champs pour saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si vous n'ajoutez pas d'étiquette Liquid pour un composant de contenu sélectionné, vous verrez un avertissement dans l'onglet **Content Optimizer Settings** et une erreur dans l'onglet **Messaging Channels**. Le Canvas ne peut pas être lancé tant que tous les composants sélectionnés ne sont pas correctement ajoutés à votre message de base.

Au fur et à mesure que le Canvas s'exécute, l'Optimiseur de contenu mélange et associe les variantes entre les composants pour générer différentes combinaisons de contenu. Au fil du temps, les combinaisons les plus performantes sont priorisées pour la distribution, ce qui vous permet d'améliorer les performances sans intervention manuelle.

#### Références Liquid {#liquid-references}

| Canal | Composant | Extrait de code Liquid |
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

### Étape 5 : Sélectionner l'événement d'optimisation {#step-5-select-optimization-event}

L'événement d'optimisation détermine comment l'Optimiseur de contenu évalue les performances et répartit le trafic entre les combinaisons de contenu au fil du temps.

L'événement d'optimisation sélectionné s'applique à tous les composants de contenu de cette étape.

{% tabs local %}
{% tab E-mail %}

Pour l'e-mail, vous pouvez optimiser pour l'un des événements suivants. L'Optimiseur de contenu utilise les ouvertures et les clics enregistrés dans les 7 jours suivant l'envoi d'un message pour orienter la distribution vers les combinaisons de contenu les plus performantes.

| Événement | Description | Cas d'usage |
| --- | --- | --- |
| Ouvertures | Optimise les combinaisons qui incitent les destinataires à ouvrir l'e-mail. | Test des lignes d'objet ou objectif d'augmentation de la visibilité |
| Clics | Optimise les combinaisons qui génèrent de l'engagement avec les liens. N'inclut pas les clics de bots ni les clics de désabonnement reconnus par Braze. | Génération de trafic, d'engagement ou de conversion à partir des liens |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 5 : Sélectionner l'événement d'optimisation" }

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
Pour le moment, la messagerie RCS avec l'Optimiseur de contenu ne prend pas en charge les replis SMS.
{% endalert %}
{% endtab %}
{% endtabs %}

## États de l'étape {#step-states}

Lorsqu'une étape Optimiseur de contenu s'exécute, Braze évalue les performances des variantes de contenu et attribue à l'étape l'un des trois états suivants, visible dans le Canvas.

| État | Signification |
| --- | --- |
| Apprentissage | L'Optimiseur de contenu collecte encore des données de performance sur vos variantes de contenu et n'a pas encore trouvé de gagnant fiable et constant. |
| Optimisation | L'Optimiseur de contenu a identifié des variantes qui surpassent régulièrement les autres et oriente la distribution vers les combinaisons gagnantes. |
| Action recommandée | L'étape s'exécute depuis un certain temps sans qu'un gagnant clair ne se dégage. Vérifiez la configuration de votre étape pour aider l'Optimiseur de contenu à en trouver un. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États de l'étape Optimiseur de contenu" }

### Actions à envisager {#actions-to-consider}

Si votre étape passe à l'état Action recommandée, envisagez les mesures suivantes :

- Augmentez le nombre d'utilisateurs qui entrent dans le Canvas, si possible. Plus d'envois donnent à l'Optimiseur de contenu davantage de données pour apprendre.
- De manière générale, testez plus de combinaisons plutôt que moins (voir [Bonnes pratiques](#best-practices)). Cela donne à l'Optimiseur de contenu un signal plus clair sur ce qui fonctionne. Si le volume de votre audience est faible (en moyenne moins d'environ 3 000 envois par jour), envisagez plutôt de réduire légèrement le nombre de variantes, car trop de combinaisons par rapport à votre volume peut ralentir l'apprentissage.
- Rendez vos variantes de contenu plus clairement distinctes les unes des autres en termes de ton, de structure ou de contenu.
- Si vous ne pouvez pas augmenter votre audience et que le nombre de variantes et la diversité du contenu semblent déjà corrects, votre étape a peut-être simplement besoin de plus de temps pour identifier les gagnants.

## Modifier une étape lancée {#edit-a-launched-step}

Une fois votre Canvas lancé, vous pouvez mettre à jour une étape Optimiseur de contenu en cours d'exécution en l'ouvrant dans l'éditeur Canvas. Vous pouvez :

- Ajouter de nouvelles variantes à n'importe quel composant existant, manuellement ou à l'aide de suggestions générées par l'IA, dans la limite de cinq variantes par composant.
- Désactiver des variantes pour arrêter de les envoyer aux utilisateurs.
- Réactiver des variantes précédemment désactivées, à condition que cela maintienne le composant à cinq variantes ou moins.

Lorsque vous publiez des modifications, l'optimiseur se réinitialise et commence à réallouer le trafic à partir de zéro entre toutes les variantes et combinaisons actives. Évitez de mettre à jour les variantes lorsque l'étape est à l'état Apprentissage. Les données historiques antérieures à la modification sont conservées et restent consultables dans l'onglet **Content Analytics**.

Les paramètres suivants ne peuvent pas être modifiés après le lancement :

- Le contenu des variantes actives existantes
- Les composants testés
- L'événement d'optimisation

Pour les étapes SMS/MMS/RCS, le groupe d'abonnement et le type de message ne peuvent pas non plus être modifiés après le lancement.

## Bonnes pratiques {#best-practices}

- De manière générale, testez davantage de composants plutôt que moins pour l'étape Optimiseur de contenu. Par exemple, au lieu de tester deux composants pour l'e-mail, testez-en trois.
- Tester au moins 10 combinaisons au total donne généralement de meilleurs résultats.
- Si c'est la première fois que vous utilisez l'Optimiseur de contenu, envisagez d'utiliser une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) afin que seule une partie de votre audience entre dans la branche contenant l'étape Optimiseur de contenu. Par exemple, vous pourriez envoyer la moitié de vos utilisateurs sur un chemin avec l'étape Optimiseur de contenu et l'autre moitié sur un chemin de contrôle qui envoie l'étape Message avec votre contenu habituel. Ensuite, collectez des données pendant 2 à 3 semaines et comparez les indicateurs clés de performance (KPI) ou les contre-indicateurs avant d'augmenter le trafic vers les chemins avec les étapes Optimiseur de contenu.
  - Pour une comparaison efficace en tête-à-tête, incluez votre contenu habituel comme l'une des variantes pour chaque composant dans votre étape Optimiseur de contenu.
- Lorsque vous êtes prêt à mettre à jour après que votre étape Optimiseur de contenu a été à l'état Optimisation pendant un certain temps, désactivez les variantes peu performantes et ajoutez-en de nouvelles qui s'appuient sur les caractéristiques de vos meilleures variantes.

## Considérations {#considerations}

- Les paramètres multilingues ne sont pas pris en charge dans les étapes Optimiseur de contenu. Utilisez plutôt une étape Optimiseur de contenu par langue et créez des chemins distincts individuellement.
- Les étiquettes Liquid pour les composants de l'Optimiseur de contenu ne sont pas prises en charge dans les étapes Message, le Liquid est donc interrompu dans les étapes Message.
- Une fois qu'une étape Optimiseur de contenu est lancée, vous ne pouvez plus modifier les composants testés, le contenu des variantes actives existantes ni l'événement d'optimisation. Pour les étapes SMS/MMS/RCS, le groupe d'abonnement et le type de message ne peuvent pas non plus être modifiés.

## Analytique {#analytics}

Pour examiner les performances, ouvrez le panneau d'analytique au niveau de l'étape afin de consulter les indicateurs par variante de contenu et les performances globales des combinaisons. L'étape Optimiseur de contenu utilise la [même analytique que l'étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Si vous avez mis à jour l'étape après le lancement, le graphique d'allocation des envois indique le moment où chaque modification de contenu a eu lieu. Les données des variantes désactivées sont conservées et restent consultables dans le panneau d'analytique, ce qui vous permet de comparer les performances sur toute la durée de vie de l'étape.

![Analytique de l'Optimiseur de contenu pour trois boutons et le pourcentage d'allocation des envois, qui tend à la hausse.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Performances par composant {#performance-by-component}

La section **Performances par composant** affiche les performances de chaque composant dans l'étape Optimiseur de contenu. La colonne **Composant** correspond au composant de contenu que vous testez (par exemple, **Subject line** ou **Primary CTA**). La colonne **Identifiant** correspond à l'identifiant de cette variante dans l'onglet **Content Optimizer Settings**.

Les ouvertures uniques et les clics sont enregistrés dans les sept jours suivant l'envoi d'un message. Les colonnes affichées dépendent de votre canal et de l'événement d'optimisation sélectionné.

| Indicateur | Description |
| --- | --- |
| Envois | Le nombre d'envois attribués à cette variante pour ce composant dans cette étape, en utilisant le même comptage d'envois au niveau de l'étape que [*Envois*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) dans le tableau [Performances par combinaison](#performance-by-combination). |
| Ouvertures | Lorsque cette colonne apparaît pour votre canal, le nombre d'ouvertures **uniques** pour cette variante dans les sept jours suivant l'envoi. Voir [*Ouvertures uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taux d'ouverture | Lorsque cette colonne apparaît, le pourcentage d'envois pour cette variante ayant enregistré au moins une ouverture unique qualifiante dans les sept jours. |
| Clics | Le nombre de clics **uniques** pour cette variante dans les sept jours suivant l'envoi. Voir [*Total des clics*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Clics uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks) et [Étape 5 : Sélectionner l'événement d'optimisation](#step-5-select-optimization-event). |
| Taux de clics | Le pourcentage d'envois pour cette variante ayant enregistré au moins un clic unique qualifiant dans les sept jours, en utilisant la même fenêtre d'étape que le tableau [Performances par combinaison](#performance-by-combination). Pour plus d'informations, voir [Pourquoi l'analytique de l'étape diffère de l'analytique générale](#why-step-analytics-differ-from-general-analytics). |
| Lectures | Lorsque cette colonne apparaît (par exemple, pour les RCS lorsque vous optimisez pour les lectures), comptabilise le moment où un consommateur lit le message avec les accusés de lecture activés. Voir [*Lectures*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Taux de lecture | Le pourcentage d'envois pour cette variante ayant abouti à une lecture parmi les utilisateurs avec les accusés de lecture activés. Voir [*Taux de lecture*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs de performances par composant" }

![Analytique des performances par composant de l'Optimiseur de contenu avec des tableaux distincts par composant, listant les envois, les clics et le taux de clics pour chaque variante.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Performances par combinaison {#performance-by-combination}

La section **Performances par combinaison** affiche les performances de chaque combinaison dans l'étape Optimiseur de contenu. Les combinaisons sont le mélange de variantes qui définissent cette ligne — une variante sélectionnée pour chaque composant de contenu que vous testez (par exemple, une ligne d'objet associée à un CTA principal).

Les ouvertures uniques et les clics sont enregistrés dans les sept jours suivant l'envoi d'un message. Les colonnes affichées dépendent de votre canal et de l'événement d'optimisation sélectionné.

| Indicateur | Description |
| --- | --- |
| Envois | Le nombre total de messages envoyés depuis cette étape en utilisant cette combinaison. Le comptage suit la même signification générale que [*Envois*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), limité à chaque combinaison. |
| Ouvertures | Le nombre d'ouvertures uniques pour cette combinaison dans les sept jours suivant l'envoi. Pour la définition des ouvertures uniques pour l'e-mail, voir [*Ouvertures uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Taux d'ouverture | Le pourcentage d'envois pour cette combinaison ayant enregistré au moins une ouverture unique qualifiante dans les sept jours. |
| Clics | Le nombre de clics uniques pour cette combinaison dans les sept jours suivant l'envoi. Pour la définition des clics par canal selon Braze, voir [*Total des clics*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) et [*Clics uniques*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Taux de clics | Le pourcentage d'envois pour cette combinaison ayant enregistré au moins un clic unique qualifiant dans les sept jours. Étant donné que l'Optimiseur de contenu utilise les comptages dédupliqués sur sept jours de l'étape, ce taux peut ne pas correspondre aux taux de clics dans l'analytique générale des campagnes. Pour plus d'informations, voir [Pourquoi l'analytique de l'étape diffère de l'analytique générale](#why-step-analytics-differ-from-general-analytics). |
| [Lectures]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Lorsque cette colonne apparaît (par exemple, pour les RCS lorsque vous optimisez pour les lectures), comptabilise le moment où un consommateur lit le message avec les accusés de lecture activés. |
| [Taux de lecture]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Lorsque cette colonne apparaît, le pourcentage d'envois pour cette combinaison ayant abouti à une lecture parmi les utilisateurs avec les accusés de lecture activés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Indicateurs de performances par combinaison" }

![Tableau d'analytique des performances par combinaison de l'Optimiseur de contenu avec les envois, les clics et le taux de clics pour chaque combinaison de contenu.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

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