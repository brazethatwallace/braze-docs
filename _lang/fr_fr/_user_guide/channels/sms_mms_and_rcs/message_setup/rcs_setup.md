---
nav_title: "Configuration RCS"
article_title: "Configuration RCS"
page_order: 1
alias: /rcs_setup/
description: "Cet article de référence couvre les conditions requises pour mettre en place et lancer le RCS."
page_type: reference
channel:
  - RCS
---

# Configurer le RCS {#set-up-rcs}

> Cet article couvre les conditions requises pour mettre en place et lancer votre canal RCS.

La configuration du RCS est aussi simple que celle du SMS. Poursuivez votre lecture pour découvrir comment vous pouvez commencer à envoyer des messages riches et interactifs.

## Étape 1 : Remplir les critères d'éligibilité {#step-1-meet-the-eligibility-criteria}

Pour être éligible à l'envoi de RCS avec Braze, votre entreprise doit remplir trois critères au préalable :

1. Votre contrat Braze actuel doit inclure des crédits de messages ou d'actions.
2. Vous devez envoyer vos messages RCS vers l'un des pays pris en charge par Braze suivants :
- États-Unis
- Royaume-Uni
- Allemagne
- Mexique
- Suède
- Espagne
- Singapour
- Brésil
- France
- Italie
- Colombie
3. Vous devez disposer d'une ou plusieurs unités de gestion des stocks (SKU) RCS dans votre contrat.

## Étape 2 : Enregistrer un expéditeur vérifié RCS {#step-2-register-an-rcs-verified-sender}

Avant de pouvoir envoyer des messages RCS, vous devez enregistrer un expéditeur vérifié RCS. Il s'agit de la représentation de votre marque que les utilisateurs voient sur leurs appareils mobiles, qui inclut le nom de votre marque, votre logo, un badge de vérification et un slogan optionnel. L'expéditeur vérifié RCS renforce la confiance des clients et confirme que vos messages proviennent d'une source authentifiée.

![Un exemple d'expéditeur vérifié RCS dans un message RCS appelé « Cat Failz Cafe ».]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Après avoir ajouté la ou les unités de gestion des stocks RCS à votre bon de commande, Braze est notifié et vous contacte avec les informations d'enregistrement de l'expéditeur RCS. Le format de ces informations dépend des pays vers lesquels vous souhaitez envoyer des messages RCS.

Lorsque vous avez soumis vos formulaires complétés à Braze, Braze finalise le processus d'enregistrement en votre nom.

### Étape 2.1 : Configurer les solutions de repli SMS pour les groupes d'abonnement RCS {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Étant donné que la couverture actuelle des opérateurs varie selon les pays, et que le matériel et les logiciels des utilisateurs varient d'un individu à l'autre, la solution de repli SMS est un composant clé pour avoir un programme RCS performant aujourd'hui. Nous vous recommandons de configurer la solution de repli SMS. Si un opérateur ne prend pas en charge le RCS ou si l'appareil d'un utilisateur ne peut pas recevoir de messages RCS, la solution de repli SMS envoie votre message quoi qu'il arrive, afin que vous ne manquiez jamais un moment important avec vos utilisateurs.

Nous vous recommandons vivement de revoir votre expérience actuelle d'abonnement SMS, vos groupes d'abonnement et la segmentation de votre audience avant de déployer votre première Campaign RCS. Si nécessaire, votre gestionnaire du succès des clients est toujours disponible pour vous fournir des conseils et vous aider à naviguer dans le processus de configuration.

#### Comment la solution de repli SMS fonctionne avec les événements et la segmentation {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab Comportement des événements %}

Lorsque vous utilisez la solution de repli SMS avec le RCS, le comportement des événements dépend de si le message est envoyé avec succès via RCS ou s'il bascule vers le SMS :

- **Si l'envoi RCS réussit :** vous recevez un événement d'envoi RCS et un événement de réception RCS.
- **Si l'envoi RCS bascule vers le SMS :** vous recevez un événement d'envoi RCS, un événement de rejet RCS et un événement de réception SMS. L'événement de réception SMS a `IS_SMS_FALLBACK=TRUE`.

{% endtab %}
{% tab Comportement de la segmentation %}

Pour le SMS et le RCS, les [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) de messages reçus (tels que [A reçu un message d'une Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) et [A reçu un message d'une étape Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step)) sont évalués au moment de l'envoi du message, et non lorsqu'il atteint l'appareil de l'utilisateur. Avec la solution de repli SMS activée, les utilisateurs peuvent toujours correspondre à ces filtres si un message RCS est rejeté et bascule vers le SMS, ou si le SMS de repli n'est pas distribué sur l'appareil de l'utilisateur.

{% endtab %}
{% endtabs %}

### Délai d'approbation par les opérateurs {#timeline-for-carrier-approval}

Le délai d'approbation par les opérateurs varie selon les pays et peut également varier au sein d'un même pays. Gardez à l'esprit que le marché du RCS en est encore à ses débuts, de sorte que les processus des opérateurs et des agrégateurs évoluent rapidement. Aux États-Unis, Braze estime que le délai d'approbation par les opérateurs pour un expéditeur vérifié RCS se situe généralement dans une fourchette de 4 à 6 semaines, un expéditeur de test étant généralement approuvé en une semaine.

Lorsque votre expéditeur vérifié RCS est approuvé, notre équipe opérationnelle met à jour vos groupes d'abonnement selon les besoins pour confirmer qu'ils incluent bien l'expéditeur RCS.

## Étape 3 : Configurer les groupes d'abonnement {#step-3-set-up-subscription-groups}

Selon votre intégration, Braze peut ajouter des expéditeurs vérifiés RCS à vos groupes d'abonnement SMS existants ou en configurer de nouveaux. Pour des instructions de configuration détaillées, consultez [Groupes d'abonnement SMS et RCS]({{site.baseurl}}/sms_rcs_subscription_groups).

## Migrer le trafic SMS vers RCS {#migrating-sms-traffic-to-rcs}

Si vous disposez de groupes d'abonnement SMS et RCS distincts, vous pouvez migrer les utilisateurs de SMS vers RCS à l'aide d'un Canvas en une seule étape. Pour des instructions détaillées, consultez [Migrer le trafic SMS vers RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#migrate-sms-traffic-to-rcs).