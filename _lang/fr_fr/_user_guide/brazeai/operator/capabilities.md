---
nav_title: Fonctionnalités
article_title: Ce que vous pouvez faire avec Operator
page_order: 1
page_type: reference
toc_headers: h2
description: "Cet article de référence couvre ce que BrazeAI Operator™ peut faire dans le tableau de bord, notamment créer des Campaigns, des Canvas, des Segments, des rapports, des tableaux de bord et des agents ; générer du texte, des messages, du Liquid et des images ; transformer des données ; vérifier la qualité du contenu ; et rechercher des informations."
---

# Ce que vous pouvez faire avec Operator {#operator-capabilities}

> [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) est un assistant IA intégré au tableau de bord de Braze. Il répond aux questions, compose des messages et agit sur les pages prises en charge — décrivez ce que vous souhaitez en langage naturel et Operator s'en charge dans le contexte.

Parce qu'Operator comprend votre espace de travail — vos directives de marque, attributs personnalisés, contenu connecté et la page sur laquelle vous travaillez — ses résultats sont plus contextuels que ce que les assistants autonomes peuvent produire. Lorsqu'Operator propose une modification à une Campaign, un Canvas, un Segment ou un autre objet, il affiche la modification sous forme de diff visuel dans une [carte d'action]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) que vous vérifiez et approuvez avant que quoi que ce soit ne soit enregistré.

Vous pouvez animer la conversation avec des messages de suivi. Operator se souvient des messages précédents jusqu'à ce que vous effaciez votre historique de conversation.

## Prérequis {#prerequisites}

Operator dispose des mêmes permissions que vous, de sorte que certaines actions nécessitent la permission correspondante pour cette surface. Par exemple, la génération d'une image nécessite la permission *Modifier les ressources de la bibliothèque multimédia*. Si vous ne voyez pas de point d'entrée, vérifiez vos permissions auprès de votre administrateur. Pour plus d'informations, consultez la [Liste des permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## Naviguer dans le tableau de bord {#navigate-the-dashboard}

Operator ne se limite pas à agir uniquement sur la page que vous consultez actuellement. Lorsqu'une requête nécessite une autre partie du tableau de bord, Operator identifie la destination, propose la navigation et vous y conduit avant de poursuivre son travail.

Cela signifie qu'Operator peut enchaîner plusieurs étapes à partir d'une seule requête. Par exemple, si vous demandez à Operator depuis la page d'accueil de vous aider à configurer les paramètres de votre éditeur par glisser-déposer pour qu'ils correspondent à vos directives de marque, il vous dirige vers les paramètres d'e-mail concernés et continue à vous accompagner à partir de là. Décrivez le résultat souhaité en langage courant, et Operator peut vous conduire aux paramètres ou à la fonctionnalité appropriés pour commencer.

Par défaut, Operator vous demande d'approuver une navigation proposée avant de vous diriger vers une nouvelle page, de la même manière qu'il le fait pour les autres actions proposées. Pour permettre à Operator de naviguer sans attendre votre approbation à chaque fois, activez l'option [Approbation automatique des actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions).

## Ce qu'Operator peut créer {#what-operator-can-create}

Au-delà de la génération de texte et de Liquid, Operator peut vous aider à créer plusieurs autres objets dans le tableau de bord, notamment :

- Campaigns
- Canvas
- Content Blocks
- Agents personnalisés
- Attributs personnalisés et événements personnalisés
- Tableaux de bord
- Images
- Messages et modèles de messages (voir [Générer des messages](#generate-messages) et [Créer des modèles de messages](#create-message-templates))
- Prédictions
- Rapports
- Segments
- Extensions de segments

{% alert note %}
Les fonctionnalités d'Operator dans le tableau de bord s'étendent régulièrement. **Demandez directement à Operator** pour obtenir la réponse la plus à jour sur ce qu'il peut faire.
{% endalert %}

## Campaigns et audiences {#campaigns-and-audiences}

Operator peut vous aider à passer d'une idée à un brouillon de Campaign ou d'audience, et à affiner l'un ou l'autre une fois qu'il existe. Toute modification qu'Operator propose à une Campaign ou un Segment apparaît sous forme de carte d'action que vous vérifiez avant qu'elle ne soit enregistrée.

Pour commencer, recherchez l'option **Créer avec Operator** lorsque vous créez une Campaign ou un Segment.

![Les menus Créer une Campaign et Créer un Segment, chacun affichant l'option Créer avec Operator.]({% image_buster /assets/img/operator/operator_create_with_operator.png %}){:style="max-width:90%"}

- **Créer et modifier des Campaigns :** lorsque vous démarrez une Campaign, Operator peut vous aider à la rédiger de bout en bout à partir d'un seul brief en langage naturel. Cela inclut l'audience, le contenu et les paramètres de distribution. Vous pouvez également demander à Operator de vous aider à modifier une Campaign existante, par exemple en ajustant le ciblage ou en actualisant le contenu du message.
- **Du brief à la Campaign :** décrivez un brief de Campaign complet, et Operator vous aide à créer un brouillon incluant le texte, les images, la personnalisation, le ciblage et les recommandations d'heure d'envoi. Vérifiez le brouillon dans l'éditeur de Campaign et affinez-le avec des prompts de suivi avant de le lancer.
- **Créer et modifier des Segments :** lorsque vous démarrez un Segment, décrivez l'audience souhaitée et Operator vous aide à construire la logique de filtrage, y compris les conditions d'attributs, l'historique des événements et les recherches dans les catalogues. Operator peut également vous aider à modifier les filtres d'un Segment existant lorsque votre stratégie de ciblage évolue.
- **Créer des extensions de segments :** Operator peut vous aider à créer une [extension de segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension) définie par SQL en rédigeant la requête qui la définit. Décrivez la logique d'audience souhaitée, et Operator rédige la requête pour que vous la vérifiiez avant de l'enregistrer. Vous pouvez également demander l'aide d'Operator depuis l'aperçu des extensions de segments. Pour en savoir plus sur Operator et SQL, consultez [Écrire des requêtes SQL](#write-sql-queries).
- **Importer et gérer des utilisateurs :** sur les pages d'audience prises en charge, Operator peut vous aider à [importer des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users), [supprimer des utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) et [fusionner des profils en double]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users). Vérifiez chaque action proposée avant qu'elle ne soit enregistrée.

## Canvas {#canvases}

Operator peut vous aider à passer d'une idée de parcours à un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) à l'état de brouillon, et à affiner un Canvas existant. Toutes les modifications proposées par Operator apparaissent sous forme de carte d'action que vous examinez avant qu'elles ne soient enregistrées.

Décrivez le parcours en langage naturel. Operator assemble un brouillon qui peut inclure des critères d'entrée, des étapes, des délais et des messages. Vous pouvez également demander à Operator de modifier un Canvas existant, par exemple en ajoutant une étape ou en mettant à jour le contenu d'un message. Examinez le brouillon dans le générateur de Canvas et affinez-le avec des instructions de suivi avant de le lancer.

Par exemple, demandez à Operator de créer un parcours d'abandon de panier qui attend une heure après l'abandon du panier, envoie un e-mail de rappel, puis une notification push après 24 heures si l'utilisateur n'a toujours pas effectué d'achat.

Vous pouvez lancer cette action depuis n'importe quelle page du tableau de bord. Si vous n'êtes pas déjà sur Canvas, Operator [y navigue](#navigate-the-dashboard) pour traiter la demande.

## Agents {#agents}

![Le menu Créer un agent, affichant l'option Agent personnalisé et les modèles d'agents créés avec Operator.]({% image_buster /assets/img/operator/operator_create_agent.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

Operator peut vous aider à créer et affiner des agents dans la [console d'agents]({{site.baseurl}}/user_guide/brazeai/agents). Toute modification qu'Operator propose à un agent apparaît sous forme de carte d'action que vous vérifiez avant qu'elle ne soit enregistrée.

- **Créer un agent de zéro :** Operator a accès à tous les champs de la console d'agents, vous pouvez donc décrire l'agent souhaité et Operator vous aide à le configurer. Cela inclut les instructions, les paramètres de sortie et les autres champs de l'agent.
- **Partir d'un modèle :** la console d'agents propose une option **Créer un agent avec Operator** qui charge un prompt pré-rédigé pour un cas d'usage courant, comme la rédaction, l'analyse de sentiment, le routage de parcours ou l'enrichissement de catalogue. Sélectionnez une catégorie, et Operator vous aide à rédiger un agent que vous pouvez affiner. Pour la liste complète des modèles, consultez [Modèles d'agents créés avec Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).
- **Affiner un agent existant :** lorsque vous modifiez un agent, sélectionnez **Générer avec Operator** ou **Affiner avec Operator** près du champ d'instructions de l'agent pour obtenir l'aide d'Operator dans la rédaction ou la révision du prompt et des paramètres de sortie de l'agent.

## Contenu et création {#content-and-creative}

Operator peut générer et vérifier le contenu de vos messages, y compris le texte, le HTML des messages, le Liquid et les images, et applique automatiquement vos directives de marque partout où elles sont configurées. Vous pouvez également demander de l'aide à Operator depuis la bibliothèque de modèles et les pages d'aperçu. Par exemple, vous pouvez créer ou mettre à jour des [modèles d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates) ou des Content Blocks depuis leurs pages de liste, planifier du travail sur le [calendrier de contenu]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/campaign_calendar), créer des [modèles de profils de couleurs pour les messages in-app]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles), ou configurer des [emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements).

### Appliquer les directives de marque {#apply-brand-guidelines}

Operator utilise les directives de marque configurées dans votre espace de travail afin que le texte, les modèles et les images générés correspondent à la voix, au ton et au style de votre marque. Pour configurer les directives de marque, accédez à **Contenu** > **Directives de marque**. Pour en savoir plus, consultez [Directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) et [Appliquer les directives de marque]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines) dans le guide d'utilisation d'Operator.

### Générer du texte {#generate-copy}

Vous pouvez utiliser Operator pour réfléchir ou générer du texte depuis n'importe où, mais vous obtiendrez la meilleure expérience en l'utilisant directement dans l'éditeur de messages, où il peut travailler à vos côtés sur le message que vous construisez. Décrivez votre produit ou votre Campaign, et Operator renvoie un texte que vous pouvez vérifier et insérer.

Operator améliore le rédacteur autonome de plusieurs façons :

- Il applique automatiquement vos [directives de marque](#apply-brand-guidelines) lorsqu'elles sont configurées.
- Il utilise le [contexte de la page]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), vous n'avez donc pas besoin de re-décrire le canal ou le message sur lequel vous travaillez. Grâce à cette connaissance de la page, vous pouvez également l'utiliser pour modifier ou affiner un message existant au lieu d'en générer un de zéro.
- Il peut consulter vos [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) et événements, ce qui vous permet de lui demander de personnaliser les recommandations de texte avec du vrai Liquid.
- Vous pouvez animer la conversation et itérer. Par exemple, demandez un ton différent, une version plus courte ou une traduction.

#### Tons {#generate-copy-tones}

Le ton du texte généré est déterminé par votre prompt. Décrivez le style souhaité et Operator ajuste sa production en conséquence. Par exemple, demandez un ton formel, décontracté, urgent ou accrocheur. Vous pouvez également affiner le ton dans des prompts de suivi, par exemple en demandant une version plus détendue ou plus soignée. Lorsque les directives de marque sont configurées, Operator les applique automatiquement pour que le texte reste cohérent avec la voix de votre marque.

### Générer des messages {#generate-messages}

Operator peut générer un design de message complet pour tout canal ou éditeur disposant d'un mode HTML, notamment :

- E-mail
- SMS/MMS/RCS
- Message in-app
- Content Card
- Bannière
- Notification push
- Webhook

Les éditeurs par glisser-déposer ne prennent pas en charge la génération directe de design, bien qu'Operator puisse toujours vous aider avec le texte ou d'autres contenus que vous ajoutez manuellement. Décrivez le message souhaité en langage naturel, vérifiez le résultat et insérez-le dans votre éditeur. Animez la conversation pour affiner le résultat. Par exemple, vous pouvez demander une mise en page différente, un texte plus court ou un style de bouton mis à jour avant d'insérer le HTML dans l'éditeur.

Vous obtiendrez les meilleurs résultats en utilisant Operator dans l'éditeur que vous êtes en train d'utiliser, où il dispose du [contexte de la page]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context) pour le canal et le type de message. Lorsque les directives de marque sont configurées, Operator les applique automatiquement.

### Créer des Content Blocks {#create-content-blocks}

Operator peut vous aider à créer des [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), les éléments de contenu réutilisables que vous insérez dans vos messages. Décrivez le bloc souhaité, et Operator rédige son contenu pour que vous le vérifiiez avant de l'enregistrer. Comme les Content Blocks sont partagés, la mise à jour de l'un met à jour chaque message qui le référence.

Operator crée les Content Blocks un par un dans le tableau de bord. Pour créer des Content Blocks en masse, utilisez l'endpoint [Create Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) avec une clé API disposant de la permission `content_blocks.create`.

### Créer des modèles de messages {#create-message-templates}

Operator peut vous aider à créer des [modèles de messages]({{site.baseurl}}/user_guide/messaging/templates) réutilisables que vous pouvez appliquer à vos Campaigns. Décrivez le modèle souhaité, et Operator le rédige pour que vous le vérifiiez avant de l'enregistrer. Vous pouvez commencer depuis n'importe où dans Braze. La génération d'un modèle fonctionne de manière similaire à la génération d'un message, consultez donc [Générer des messages](#generate-messages) pour les canaux et éditeurs pris en charge.

### Générer du Liquid {#generate-liquid}

Operator est très performant avec la [syntaxe Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Il peut générer une logique Liquid complexe basée sur les données de votre espace de travail, y compris la consultation des données d'attributs, d'événements et de [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs) pour trouver des exemples de valeurs. Il peut également vérifier et expliquer le Liquid existant dans vos Campaigns.

Comme pour la rédaction, vous pouvez demander à Operator de générer du Liquid depuis n'importe où, et cela fonctionne sur tous les canaux et éditeurs de messages. Vous obtiendrez les meilleurs résultats depuis un éditeur de messages, où Operator dispose du contexte complet du message que vous construisez.

{% details Bonnes pratiques pour les prompts Liquid %}

#### Donnez du contexte {#generate-liquid-give-context}

Fournir du contexte aide Operator à comprendre la vue d'ensemble de votre projet. Il est utile d'inclure des informations telles que :

- Le nom et le secteur d'activité de votre entreprise
- La Campaign sur laquelle vous travaillez, comme le Black Friday ou les soldes de fin d'année
- Votre objectif, comme augmenter votre taux de clics
- Les attributs personnalisés spécifiques que vous souhaitez inclure dans votre message

Inclure du contexte dans votre prompt aide Operator à adapter ses réponses pour mieux répondre à vos besoins. Vous pouvez également inclure des détails de votre Campaign, de votre brief de message ou de votre document de brainstorming pour mettre Operator au courant.

#### Soyez précis {#generate-liquid-be-specific}

Operator peut poser des questions de suivi, mais fournir des détails dès le départ peut conduire à des résultats plus précis plus rapidement. Pensez à inclure des détails tels que :

- Toute préférence ou exigence connue pour le message
- Des instructions sur la façon de gérer certaines situations, comme l'absence de réponse du destinataire du message ou les options de message de secours
- Des valeurs exactes ou similaires pour les attributs personnalisés que vous souhaitez utiliser, ce qui aide Operator à générer et tester une logique plus précise
- Lorsque vous demandez du Liquid utilisant du contenu connecté, la documentation de l'endpoint API, un exemple de réponse API, ou les deux

#### Faites preuve de créativité {#generate-liquid-get-creative}

Essayez différents prompts pour voir comment Operator peut améliorer vos messages. Expérimentez avec différents prompts et idées, car la créativité peut conduire à des résultats plus engageants.

{% enddetails %}

### Générer des images {#generate-images}

Operator génère des images à l'aide de [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), un système d'IA d'OpenAI, fournisseur tiers de Braze. Cela vous permet de créer des images réalistes et des illustrations à partir d'une description en langage naturel.

Dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), sélectionnez **Générer avec Operator** dans le panneau **Charger des ressources**. Décrivez l'image souhaitée, et Operator la génère et l'enregistre directement dans votre bibliothèque multimédia.

#### Conseils pour les prompts {#generate-images-prompt-tips}

- Décrivez le sujet, le style, l'ambiance et les couleurs de manière précise. Plus vous incluez de détails, meilleur sera le résultat. Le chargement d'une image de référence n'est pas pris en charge.
- Lorsque vous appliquez les [directives de marque](#apply-brand-guidelines) comme contexte dans votre prompt Operator, celui-ci les applique directement à l'image générée, de sorte que le résultat reflète le style visuel de votre marque.
- Les générations d'images sont comptabilisées dans la limite d'utilisation quotidienne d'Operator à l'échelle de l'entreprise, au même titre que les autres actions Operator. Pour en savoir plus, consultez [Limitations](#limitations).

### Vérifier la qualité du contenu {#review-content-quality}

Dans l'onglet **Test** pour les SMS, les notifications push Android, les notifications push iOS et les messages in-app traditionnels, sélectionnez **Vérifier avec Operator** pour vérifier votre contenu avant l'envoi. Par défaut, Operator vérifie votre Campaign pour les erreurs d'orthographe et de grammaire, le ton inapproprié ou hors marque, le langage offensant, ainsi que tout code résiduel, contenu de test ou Liquid non rendu, et recommande comment corriger ce qu'il trouve. Vous pouvez également demander à Operator d'adapter la façon dont il vérifie votre contenu directement dans votre prompt.

Au-delà de sa vérification par défaut, vous pouvez orienter Operator vers des contrôles spécifiques. Pensez à lui demander de vérifier l'un des éléments suivants :

- **Orthographe et grammaire :** relire l'orthographe et la grammaire et suggérer des corrections qui améliorent la précision de votre contenu.
- **Ton :** évaluer si le ton correspond au style de communication souhaité et signaler tout ce qui pourrait être mal interprété.
- **Langage offensant :** rechercher un langage potentiellement offensant ou inapproprié afin que vous puissiez le réviser et garder vos messages respectueux.
- **Contenu accidentel :** détecter le code résiduel, le balisage ou les messages de test ajoutés involontairement, y compris le Liquid qui ne s'est pas rendu pour un utilisateur test.
- **Autres langues :** vérifier du contenu rédigé dans une autre langue. La prise en charge du contenu non anglophone peut varier, vérifiez donc les résultats attentivement.

#### Bonnes pratiques {#review-content-quality-best-practices}

Tenez compte des éléments suivants pour tirer le meilleur parti de la vérification de contenu :

- **Relisez votre message :** bien que la vérification de contenu puisse aider à identifier les erreurs, il est toujours essentiel de relire votre contenu manuellement. Appuyez-vous sur les suggestions générées par l'IA comme guide utile, mais utilisez votre jugement pour garantir la précision.
- **Comprenez l'analyse du ton :** les résultats de l'analyse du ton sont subjectifs et basés sur la compréhension du modèle d'IA. Bien qu'ils puissent fournir des informations utiles, tenez compte de votre ton souhaité et du contexte de la conversation pour effectuer les ajustements appropriés.
- **Vérifiez le langage offensant signalé :** la détection du langage offensant est conçue pour être robuste, mais elle peut occasionnellement signaler des faux positifs. Examinez attentivement les sections signalées et apportez les modifications nécessaires.

## Automatisation des données et recherche {#data-automation-and-lookup}

Operator peut servir de référence pour les données de votre espace de travail et la documentation Braze, écrire du SQL lorsque vous devez interroger ces données directement, et générer le code qui transforme les données entrantes, comme un payload webhook, dans un format utilisable par Braze.

### Ce qu'Operator peut rechercher {#what-operator-can-look-up}

Operator peut consulter les éléments suivants pour répondre à des questions ou enrichir le contenu qu'il génère, notamment :

- Documentation Braze
- [Segments]({{site.baseurl}}/user_guide/audience/segments)
- [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) et [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- Données de [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs)
- Configuration de [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) et de [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) existants, comme les paramètres de ciblage et de distribution
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)
- Réponses de [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Agents]({{site.baseurl}}/user_guide/brazeai/agents)

Demandez directement à Operator si vous n'êtes pas sûr qu'il puisse rechercher une information spécifique.


### Analyser les données de performance {#analyze-performance-data}

Posez à Operator des questions en langage naturel sur les performances de vos Campaigns et Canvas, et il vous renvoie des graphiques, des comparaisons et de courtes analyses tirées des données de votre espace de travail. Contrairement aux fonctionnalités contextuelles d'Operator, qui s'appuient sur la page où vous vous trouvez, la fonction Analyze répond depuis n'importe quel endroit du tableau de bord. Pour en savoir plus, consultez [Operator Analyze]({{site.baseurl}}/user_guide/brazeai/operator/analyze).

### Créer des rapports et des tableaux de bord {#build-reports-and-dashboards}

Operator peut vous aider à créer des rapports dans le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder) et des tableaux de bord dans le [générateur de tableaux de bord]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder) à partir d'une description en langage naturel. Décrivez les indicateurs, les canaux et la plage de dates souhaités, et Operator prépare le rapport ou le tableau de bord pour que vous le vérifiiez avant de l'enregistrer.

Par exemple, demandez : « Crée-moi un rapport qui montre l'engagement SMS de mon espace de travail au cours des 30 derniers jours. »

### Créer des prédictions {#create-predictions}

Operator peut vous aider à consulter et à créer des prédictions de [prédiction du taux d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) et des [recommandations d'articles par IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai). Décrivez le résultat souhaité, et Operator propose la prédiction ou la recommandation pour que vous la vérifiiez.

### Écrire des requêtes SQL {#write-sql-queries}

Operator peut vous aider à écrire du SQL pour les [extensions de segments](#campaigns-and-audiences) et pour les [modèles de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) du générateur de requêtes. Décrivez la requête souhaitée en langage naturel, et Operator génère le SQL pour que vous le vérifiiez avant de l'exécuter.

### Générer du code de transformation des données {#generate-data-transformation-code}

Dans l'éditeur de [transformation des données]({{site.baseurl}}/user_guide/data/unification/data_transformation), sélectionnez **Insérer le code** pour générer du code de transformation qui convertit un payload webhook entrant en requêtes API Braze valides. Pour des instructions étape par étape sur la création d'une transformation, consultez [Créer une transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

## Paramètres de l'espace de travail {#workspace-settings}

Operator peut examiner et mettre à jour les paramètres sur plusieurs pages de configuration de l'espace de travail. Décrivez le changement souhaité, et Operator le propose sous forme de carte d'action que vous examinez avant qu'il ne soit enregistré. Les pages de paramètres prises en charge incluent, sans s'y limiter :

- [Heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- [Paramètres push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings)
- [Limites de débit des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)
- [Workflows d'approbation]({{site.baseurl}}/user_guide/messaging/governance/approvals), y compris les [règles de messaging]({{site.baseurl}}/user_guide/messaging/governance/approvals/messaging_rules) et l'approbation permanente
- [API et identifiants]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers), y compris les [autres identifiants]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers#other-identifiers), les limites d'API et les [alertes d'utilisation de l'API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts)
- [Coordonnées des paramètres d'administration]({{site.baseurl}}/user_guide/administer/global/admin_settings/contact_information)
- [Paramètres de sécurité]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings) et [provisionnement SCIM]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning)
- [Rôles]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role) et [ensembles de permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set)
- [Journal des exportations]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/exports_log)
- Catégories de priorisation des messages

{% alert note %}
La couverture des pages de paramètres par Operator s'étend régulièrement. **Demandez directement à Operator** pour obtenir la réponse la plus à jour sur ce qu'il peut configurer.
{% endalert %}

## Limitations {#limitations}

{% alert note %}
La couverture d'Operator évolue fréquemment. Si vous n'êtes pas sûr qu'un écran ou un flux de travail spécifique soit pris en charge, demandez directement à Operator.
{% endalert %}

La prise en charge d'Operator dans le tableau de bord est large, mais elle a des limites.

- **Canvas :** Operator peut [créer et modifier des Canvas](#canvases) dans l'éditeur Canvas actuel. Il ne prend pas en charge l'[éditeur Canvas d'origine]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), le démarrage d'un Canvas depuis la page de sélection de modèles, ni l'utilisation de **Prévisualiser en tant qu'utilisateur** lors de la création de Canvas. Operator peut toutefois consulter la configuration d'un Canvas existant, comme les paramètres de ciblage et de distribution, pour répondre à des questions et enrichir ses résultats.
- **Duplication de Campaign :** Operator ne peut pas dupliquer une Campaign existante depuis la vue de liste des Campaigns. Pour créer une campagne similaire, demandez à Operator d'en créer une nouvelle à partir de zéro, ou dupliquez la campagne manuellement depuis le menu **Plus d'actions** de la vue de liste.
- **Éditeurs par glisser-déposer :** Operator ne peut pas générer ni insérer un design de message directement dans un éditeur par glisser-déposer, comme ceux pour les [e-mails]({{site.baseurl}}/user_guide/channels/email/drag_and_drop), les [Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner) et les [messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop). Passez à l'éditeur HTML correspondant pour utiliser Operator, ou demandez à Operator de générer du contenu, comme du texte, que vous pouvez coller manuellement. Consultez [Générer des messages](#generate-messages) pour les canaux et éditeurs pris en charge.
- **Visibilité de l'écran :** Operator utilise le contexte de la page pour comprendre ce que vous regardez, y compris le contenu dans les aperçus et éditeurs pris en charge. Lorsqu'une partie de la page échappe à ce qu'Operator peut lire, il vous le signale au lieu de deviner, afin que vous sachiez décrire ce contenu vous-même.
- **Limites d'utilisation :** Operator dispose d'une limite d'utilisation quotidienne à l'échelle de l'entreprise qui se réinitialise toutes les 24 heures. Toutes les actions d'Operator sont comptabilisées dans cette limite, et la consommation varie en fonction de la quantité de données qu'Operator doit lire et produire. Poser des questions, rechercher des informations et [créer un ticket d'assistance]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets) consomment moins de ressources. Créer ou modifier des objets tels que des campagnes et des Segments consomme davantage. Les [générations d'images](#generate-images) sont également comptabilisées dans cette limite. Si la limite est atteinte, un message « Limite quotidienne atteinte » apparaît et Operator ne traite plus de requêtes jusqu'à la réinitialisation de la limite. Pour les étapes de résolution des problèmes, consultez [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting).

## Anciens assistants {#legacy-assistants}

Avant Operator, plusieurs fonctionnalités d'IA existaient en tant qu'assistants autonomes distincts : AI Copywriter, AI Liquid Assistant, AI Image Generator, AI SQL Generator, le Data Transformations AI Copilot et la vérification de contenu. Tous leurs points d'entrée restent en place et redirigent vers Operator, vos flux de travail existants ne sont donc pas affectés. Pour savoir ce qu'ils font aujourd'hui, consultez [Contenu et création](#content-and-creative) et [Automatisation des données et recherche](#data-automation-and-lookup).

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Confidentialité et sécurité des données {#data-privacy-and-security}

Operator s'intègre à OpenAI pour générer des résultats. Pour en savoir plus sur les informations que Braze envoie à OpenAI, la façon dont ces données sont utilisées et vos droits de propriété intellectuelle, consultez [Comment les données sont utilisées avec OpenAI]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security).

## Étapes suivantes {#next-steps}

- [Premiers pas avec Operator]({{site.baseurl}}/user_guide/brazeai/operator) : accédez à Operator et utilisez-le
- [Bibliothèque de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library) : parcourez des exemples de prompts prêts à l'emploi
- [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) : vérifiez et approuvez les modifications proposées par Operator
- [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting) : consultez les problèmes courants et leurs solutions