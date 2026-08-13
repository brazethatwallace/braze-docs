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

Avant de pouvoir envoyer des messages RCS, vous devez enregistrer un expéditeur vérifié RCS. Il s'agit de la représentation de votre marque que les utilisateurs verront sur leurs appareils mobiles, comprenant le nom de votre marque, votre logo, un badge de vérification et un slogan optionnel. L'expéditeur vérifié RCS renforce la confiance des clients et confirme que vos messages proviennent d'une source authentifiée.

![Un exemple d'expéditeur vérifié RCS dans un message RCS appelé « Cat Failz Cafe ».]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Après avoir ajouté la ou les unités de gestion des stocks RCS à votre bon de commande, Braze sera notifié et vous contactera avec les informations d'enregistrement de l'expéditeur RCS. Le format de ces informations dépendra des pays vers lesquels vous souhaitez envoyer des messages RCS.

Lorsque vous aurez soumis vos formulaires complétés à Braze, nous finaliserons le processus d'enregistrement en votre nom.

### Étape 2.1 : Configurer les solutions de repli SMS pour les groupes d'abonnement RCS {#step-21-set-up-sms-fallbacks-for-rcs-subscription-groups}

Étant donné que la couverture actuelle des opérateurs varie selon les pays, et que le matériel et les logiciels des utilisateurs varient d'un individu à l'autre, la solution de repli SMS est un élément clé pour un programme RCS réussi aujourd'hui. Nous vous recommandons de configurer la solution de repli SMS. Si un opérateur ne prend pas en charge le RCS ou si l'appareil d'un utilisateur ne peut pas recevoir de messages RCS, la solution de repli SMS enverra votre message quoi qu'il arrive, afin que vous ne manquiez jamais un moment important avec vos utilisateurs.

Nous vous recommandons vivement de revoir votre expérience actuelle d'abonnement SMS, vos groupes d'abonnement et la segmentation de votre audience avant de déployer votre première Campaign RCS. Si nécessaire, votre gestionnaire du succès des clients est toujours disponible pour vous fournir des conseils et vous aider à naviguer dans le processus de configuration.

#### Comment la solution de repli SMS fonctionne avec les événements et la segmentation {#how-sms-fallback-works-with-events-and-segmentation}

{% tabs %}
{% tab Comportement des événements %}

Lorsque vous utilisez la solution de repli SMS avec le RCS, le comportement des événements dépend de si le message est envoyé avec succès via RCS ou s'il bascule vers le SMS :

- **Si l'envoi RCS réussit :** Vous recevez un événement d'envoi RCS et un événement de réception RCS.
- **Si l'envoi RCS bascule vers le SMS :** Vous recevez un événement d'envoi RCS, un événement de rejet RCS et un événement de réception SMS. L'événement de réception SMS a `IS_SMS_FALLBACK=TRUE`.

{% endtab %}
{% tab Comportement de la segmentation %}

Pour le SMS et le RCS, les [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) de messages reçus (tels que [Message reçu d'une Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) et [Message reçu d'une étape Canvas]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step)) sont évalués au moment de l'envoi du message, et non lorsqu'il atteint l'appareil de l'utilisateur. Avec la solution de repli SMS activée, les utilisateurs peuvent toujours correspondre à ces filtres si un message RCS est rejeté et bascule vers le SMS, ou si le SMS de repli n'est pas distribué sur l'appareil de l'utilisateur.

{% endtab %}
{% endtabs %}

### Délai d'approbation par les opérateurs {#timeline-for-carrier-approval}

Le délai d'approbation par les opérateurs varie selon les pays et peut également varier au sein d'un même pays. Gardez à l'esprit que le marché du RCS en est encore à ses débuts, de sorte que les processus des opérateurs et des agrégateurs évoluent rapidement. Aux États-Unis, Braze estime que le délai d'approbation par les opérateurs pour un expéditeur vérifié RCS se situe généralement dans une fourchette de 4 à 6 semaines, un expéditeur de test étant généralement approuvé en une semaine.

Lorsque votre expéditeur vérifié RCS est approuvé, notre équipe opérationnelle mettra à jour vos groupes d'abonnement si nécessaire pour confirmer qu'ils incluent bien l'expéditeur RCS.

## Étape 3 : Configurer les groupes d'abonnement {#step-3-set-up-subscription-groups}

Selon votre intégration, Braze peut ajouter des expéditeurs vérifiés RCS à vos groupes d'abonnement SMS existants ou en configurer de nouveaux. Pour des instructions de configuration détaillées, consultez [Groupes d'abonnement SMS et RCS]({{site.baseurl}}/sms_rcs_subscription_groups).

## Migration du trafic SMS vers le RCS {#migrating-sms-traffic-to-rcs}

Si vous disposez de groupes d'abonnement SMS et RCS distincts, vous pouvez migrer les utilisateurs du SMS vers le RCS à l'aide d'un Canvas en une seule étape.

Braze recommande de tester l'envoi de messages RCS à un volume réduit d'utilisateurs dans un premier temps, puis de migrer progressivement davantage d'utilisateurs vers le groupe d'abonnement RCS. Par exemple, si vous avez 1 000 000 d'utilisateurs abonnés à un groupe d'abonnement SMS, vous pourriez d'abord migrer tous les utilisateurs vers le nouveau groupe d'abonnement, puis segmenter une audience plus restreinte de 50 000 à 100 000 (5 à 10 %) pour tester les messages RCS.

### Étape 1 : Créer un Canvas et remplir la planification d'entrée {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Créez un Canvas et donnez-lui un nom facilement identifiable (par exemple « Transfert d'utilisateurs du groupe d'abonnement SMS vers RCS »). Ensuite, planifiez la Campaign au moment qui vous convient.

### Étape 2 : Définir votre audience {#step-2-define-your-audience}

Définissez votre audience en utilisant l'une des méthodes suivantes. Ensuite, accédez à l'étape **Paramètres d'envoi** et sélectionnez **Utilisateurs abonnés ou ayant accepté l'abonnement**.

| Méthode                          | Description                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Créer un Segment**         | Créez un Segment qui inclut tous les utilisateurs d'un groupe d'abonnement ou un sous-ensemble à l'aide de filtres de segmentation (par exemple, un échantillon aléatoire de 5 à 10 %). Les Segments se mettent à jour avant chaque envoi pour refléter votre base d'utilisateurs actuelle.        |
| **Appliquer des filtres de Campaign ou de Canvas** | Affinez l'audience à l'étape **Audience cible** de votre Campaign ou Canvas. Ajustez les options de ciblage sans quitter la page pour plus de flexibilité.                                         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Définir votre audience" }

### Étape 3 : Configurer une étape de mise à jour utilisateur {#step-3-configure-a-user-update-step}

Ajoutez une étape de mise à jour utilisateur à votre Canvas. Dans cette étape, ouvrez l'**éditeur JSON avancé** et saisissez le code suivant (pour le champ d'identifiant utilisateur unique, nous recommandons d'utiliser le champ `braze_id`) :

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

{% alert important %}
Lorsque vous utilisez `use_double_opt_in_logic`, un profil utilisateur doit déjà exister pour que l'état d'abonnement puisse être mis à jour. Si aucun profil utilisateur n'est associé à l'identifiant fourni, l'état d'abonnement n'est pas mis à jour.
{% endalert %}

![Objet de mise à jour utilisateur contenant le code JSON mentionné précédemment.]({% image_buster /assets/img/sms/user_update_object.png %})

### Étape 4 : Tester le Canvas {#step-4-test-the-canvas}

Nous vous recommandons vivement de [tester votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) pour confirmer qu'il fonctionne comme prévu avant de l'envoyer à votre audience plus large.

### Étape 5 : Lancer votre Canvas {#step-5-launch-your-canvas}

Après avoir testé votre Canvas avec succès, lancez-le pour votre sous-ensemble d'utilisateurs !

Pour confirmer que vos utilisateurs ont été migrés avec succès, nous vous recommandons de vérifier quelques profils utilisateur individuels qui ont été mis à jour. Dans l'onglet **Engagement**, recherchez **Paramètres de contact** et faites défiler pour afficher les groupes d'abonnement auxquels l'utilisateur est abonné. Le bouton du groupe d'abonnement RCS devrait maintenant être activé.