---
nav_title: E-mail
article_title: E-mail
page_order: 3
page_type: landing
description: "Créez des campagnes e-mail personnalisées dans Braze avec les éditeurs par glisser-déposer et HTML, la gestion des abonnements, et bien plus encore."
channel:
  - email
search_rank: 2
---

# E-mail {#email}

> Avec l'e-mail de Braze, vous créez des messages e-mail personnalisés dans des Campaigns ou des Canvas qui atteignent vos utilisateurs en dehors de votre application ou de votre site web. Ce hub couvre la configuration des e-mails, les éditeurs par glisser-déposer et HTML, la gestion des abonnements, les modèles et les tests afin que vous puissiez lancer des programmes e-mail conformes et fidèles à votre marque. Utilisez les modèles d'e-mail de Braze ou du HTML personnalisé pour refléter le ton et la mise en page de votre marque. Commencez par la [configuration des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup) si vous configurez un nouveau domaine d'envoi. Pour consulter des exemples de campagnes e-mail, reportez-vous aux [études de cas](https://www.braze.com/customers/) de Braze.

## Prérequis {#prerequisites}

Avant de pouvoir envoyer des e-mails avec Braze, vous devez configurer vos IP dédiées, vos domaines, l'authentification des e-mails et l'IP warming. Pour une procédure complète, consultez la section [Configuration des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Personnalisez vos e-mails {#customize-your-emails}

Vous pouvez personnaliser vos communications par e-mail de différentes manières, notamment :

- [Modèles d'e-mails Braze]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [Modèles HTML personnalisés]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [Blocs de l'éditeur (e-mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [Abonnements des utilisateurs]({{site.baseurl}}/user_guide/channels/email/subscriptions)
- [Groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)

## Testez vos e-mails {#test-your-emails}

Les [groupes initiateurs]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) envoient automatiquement des copies de vos campagnes e-mail aux utilisateurs internes à des fins d'assurance qualité. Les e-mails initiateurs incluent `[SEED]` ajouté au début de la ligne d'objet pour vous aider à les identifier.

## Cas d'usage {#use-cases}

| Cas d'usage | Explication |
| --- | --- |
| Réengagement | Contactez les utilisateurs en dehors de votre application, y compris ceux qui n'ont pas installé l'application. |
| Onboarding | Accueillez et encouragez les nouveaux utilisateurs à activer les notifications push ou à partager l'application sur les réseaux sociaux. |
| Messages enrichis | Permettez l'envoi de messages HTML riches et dynamiques. |
| Contenu multimédia | Facilitez l'intégration de contenu multimédia engageant pour les utilisateurs, comme des vidéos et des images. |
| Newsletters | Envoyez facilement des newsletters mensuelles ou hebdomadaires pour maintenir l'engagement des utilisateurs. |
| Transactions | Informez les utilisateurs de leurs achats récents et transmettez des informations importantes sur les produits et la livraison grâce aux [e-mails transactionnels]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'usage" }

## Services e-mail {#email-services}

Si vous avez besoin d'une assistance supplémentaire pour votre programme e-mail, Braze propose des services ponctuels et récurrents moyennant un coût additionnel. Pour plus d'informations, contactez votre gestionnaire de compte Braze.

### Services de livrabilité des e-mails {#email-deliverability-services}

Braze propose deux niveaux d'assistance e-mail récurrente :
1. Deluxe
2. Standard

Ces services peuvent inclure :

- Un audit des pratiques d'envoi d'e-mails historiques et actuelles, avec une analyse du ciblage, de la cadence et des stratégies d'envoi de messages
- Une configuration en marque blanche et un plan de réchauffement d'adresses IP personnalisé, créés par un expert en livrabilité des e-mails
  - Des appels de suivi réguliers pendant votre premier mois (trois fois par semaine pour Deluxe et une fois par semaine pour Standard)
- Des appels réguliers avec un expert en livrabilité (deux fois par mois pour Deluxe et une fois par mois pour Standard) pour :
  - Suivre les performances de livrabilité par domaine
  - Formuler des recommandations pour améliorer les performances et les résultats de votre programme e-mail en s'appuyant sur les données et les bonnes pratiques établies
- Atténuer et résoudre les situations de crise liées à des événements entraînant des problèmes tels qu'une mise en liste de blocage affectant la livrabilité

## Questions fréquemment posées {#frequently-asked-questions}

### Comment configurer l'envoi d'e-mails dans Braze ? {#how-do-i-set-up-email-sending-in-braze}

Configurez des IP dédiées, des domaines, l'authentification et l'IP warming avant votre premier envoi. Consultez la [Configuration des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup) pour la liste complète des étapes.

### Quelle est la différence entre les abonnements utilisateur et les groupes d'abonnement ? {#what-is-the-difference-between-user-subscriptions-and-subscription-groups}

Les abonnements utilisateur contrôlent le statut d'abonnement global pour un canal (par exemple, abonné ou désabonné aux e-mails). Les groupes d'abonnement permettent aux utilisateurs de choisir des catégories de messages spécifiques au sein de ce canal. Consultez [Abonnements utilisateur]({{site.baseurl}}/user_guide/channels/email/subscriptions) et [Groupes d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

### Comment puis-je tester un e-mail avant d'envoyer une campagne ? {#how-can-i-test-an-email-before-i-send-a-campaign}

Utilisez les [groupes initiateurs]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) pour envoyer des copies d'aperçu à des réviseurs internes et vérifier le rendu sur différents clients de messagerie.

## Prochaines étapes {#next-steps}

- [Configuration des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup)
- [Créer un e-mail avec l'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)
- [Créer un e-mail avec l'éditeur HTML]({{site.baseurl}}/user_guide/channels/email/html_editor)