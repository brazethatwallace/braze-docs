# Création d'agents décisionnels basés sur l'intelligence artificielle {#building-ai-decisioning-agents}

> Découvrez comment créer un agent pour BrazeAI Decisioning Studio™, afin d'automatiser les expérimentations personnalisées et d'optimiser les résultats tels que les conversions, la fidélisation ou le chiffre d'affaires, sans tests A/B manuels.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## À propos des agents {#about-agents}

Un agent de décision IA est une configuration personnalisée du moteur de décision BrazeAI<sup>TM</sup>, conçue sur mesure pour répondre à un objectif métier spécifique.

Par exemple, vous pourriez créer un agent d'achat récurrent pour augmenter les conversions de suivi après une première vente. Vous définissez l'audience et le message dans Braze, tandis que votre agent de décision exécute des expérimentations quotidiennes et teste automatiquement différentes combinaisons d'offres de produits, de timing de message et de fréquence pour chaque client. Au fil du temps, BrazeAI<sup>TM</sup> apprend ce qui fonctionne le mieux et orchestre des envois personnalisés via Braze pour maximiser les taux de réachat.

Pour créer un bon agent, vous devrez :

- Choisir une métrique de succès que BrazeAI<sup>TM</sup> devra optimiser, comme le chiffre d'affaires, les conversions ou l'ARPU.
- Définir les dimensions à tester, comme l'offre, la ligne d'objet, le visuel, le canal ou l'heure d'envoi.
- Sélectionner les options pour chaque dimension, comme e-mail versus SMS, ou fréquence quotidienne versus hebdomadaire.

![Exemple de diagramme d'un agent Decisioning Studio pour les e-mails de recommandation.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Exemples d'agents {#sample-agents}

Voici quelques exemples d'agents que vous pouvez créer avec BrazeAI<sup>TM</sup> Decisioning Studio. Vos agents de décision IA apprendront de chaque interaction client et appliqueront ces informations aux actions du lendemain.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Créer un agent {#building-an-agent}

### Prérequis {#prerequisites}

Avant de pouvoir créer un agent, vous devez [intégrer BrazeAI Decisioning Studio™]({{site.baseurl}}/developer_guide/decisioning_studio/integration).

### Étape 1 : Contacter l'équipe AI Expert Services {#step-1-contact-ai-expert-services}

L'équipe AI Expert Services travaillera étroitement avec vous pour cadrer, concevoir et créer votre agent de décision. Si ce n'est pas déjà fait, [contactez-nous](https://www.braze.com/get-started/) pour commencer.

Vous réaliserez ensemble les étapes suivantes pour créer un agent personnalisé adapté à vos besoins.

### Étape 2 : Concevoir votre agent {#step-2-design-your-agent}

En collaboration avec l'équipe AI Expert Services, vous définirez :

- une audience cible,
- la métrique métier à optimiser,
- les actions de l'agent de décision BrazeAI<sup>TM</sup>, et
- toute donnée client first-party que l'agent doit exploiter pour atteindre vos résultats métier.

Une fois la conception finalisée, l'équipe travaillera avec vous pour identifier et compléter toute exigence d'intégration supplémentaire.

### Étape 3 : Configurer votre plateforme de distribution {#step-3-set-up-your-delivery-platform}

Ensuite, l'équipe AI Expert Services vous aidera à configurer votre plateforme d'engagement client. Bien que Decisioning Studio fonctionne de manière optimale avec Braze, plusieurs autres plateformes sont prises en charge — contactez votre équipe AI Expert Services pour obtenir des ressources complémentaires.

{% tabs local %}
{% tab Braze %}
Pour configurer Braze :

1. Créez une [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) ou un [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=api-triggered%20delivery#step-12-determine-your-canvas-entry-schedule). BrazeAI Decisioning Studio™ utilisera cette méthode de distribution pour envoyer des événements d'activation personnalisés 1:1 aux utilisateurs de votre audience définie.
2. Veillez à ne pas inclure de [groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) Braze, afin que BrazeAI<sup>TM</sup> puisse servir de groupe de contrôle dédié à la place.
3. En fonction de vos dimensions, vous pouvez configurer des étiquettes Liquid dans votre contenu créatif pour remplir dynamiquement vos messages avec les recommandations de BrazeAI<sup>TM</sup>. BrazeAI<sup>TM</sup> transmettra du contenu spécifique à chaque client aux étiquettes Liquid de vos modèles via l'API Braze.
{% endtab %}
{% endtabs %}

### Étape 4 : Lancer et surveiller {#step-4-launch-and-monitor}

Après le lancement de votre agent, votre équipe AI Expert Services continuera à le surveiller et à l'ajuster conformément à la conception convenue. Elle vous aidera également à apporter des ajustements, des extensions ou des modifications à l'agent, si nécessaire.