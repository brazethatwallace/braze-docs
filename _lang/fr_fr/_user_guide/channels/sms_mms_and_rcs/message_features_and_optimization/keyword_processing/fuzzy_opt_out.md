---
nav_title: Désabonnement approximatif
article_title: Désabonnement approximatif
description: "Cet article de référence explique comment configurer le désabonnement approximatif, un paramètre qui tente de reconnaître lorsqu'un message entrant ne correspond pas à un mot-clé de désabonnement."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 4

---

# Désabonnement approximatif {#fuzzy-opt-out}

![Conversation de messages iOS montrant des messages sortants de désabonnement en réponse au désabonnement approximatif entrant « Please stopppp ».]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Les utilisateurs qui envoient des SMS, MMS et RCS avec Braze doivent respecter les lois, réglementations et normes du secteur applicables. En matière de désabonnement, des lois telles que le TCPA stipulent que lorsqu'un utilisateur envoie un message constituant une révocation raisonnable du consentement (y compris des mots-clés de désabonnement reconnus tels que « STOP », « STOPALL », « UNSUBSCRIBE », « CANCEL », « END » ou « QUIT »), tous les messages ultérieurs liés à ce programme de communication doivent être interrompus. Braze traite automatiquement les mots-clés de désabonnement reconnus et désabonne l'utilisateur.<br><br> Le désabonnement approximatif étend cette fonctionnalité en tentant de reconnaître les messages entrants qui ne correspondent à aucun **mot-clé de désabonnement** configuré pour la catégorie **Opt-out** du groupe d'abonnement (c'est-à-dire tout [mot-clé de désabonnement par défaut]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) ou [mot-clé de désabonnement personnalisé]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling)) mais qui indiquent tout de même une intention de désabonnement — par exemple, un message comme « goodbye » ou « leave me alone ».

Le désabonnement approximatif est désactivé par défaut. Si le désabonnement approximatif est activé et qu'un message entrant est jugé « approximatif », vous pouvez configurer Braze pour désabonner automatiquement l'utilisateur ou envoyer un message lui indiquant comment se désabonner manuellement. Pour les marques américaines, le désabonnement automatique de l'utilisateur est fortement recommandé afin de respecter les exigences du TCPA.

{% alert note %}
Actuellement, seuls les mots-clés de désabonnement (par défaut et personnalisés) créés avec l'anglais comme [langue locale]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling#multi-language-support) sont pris en charge.
{% endalert %}

## Qu'est-ce qui est considéré comme approximatif ? {#what-is-deemed-as-fuzzy}

Les critères pour qu'une réponse entrante soit considérée comme « approximative » sont les suivants (les comparaisons utilisent chaque mot-clé de la catégorie **Opt-out**, y compris les mots-clés par défaut et personnalisés) :
- Si le remplacement d'une lettre par une touche adjacente sur un clavier QWERTY produit un mot-clé de désabonnement correspondant.
- Si une sous-chaîne du message correspond à un mot-clé de désabonnement.

Par exemple, « Stpo » ou « Please stopppp » seront considérés comme approximatifs, et une réponse de désabonnement approximatif sera envoyée. Si l'utilisateur répond ensuite avec un mot-clé de désabonnement, un événement de désabonnement sera déclenché.

## Configurer le désabonnement approximatif {#configure-fuzzy-opt-out}

Pour configurer le désabonnement approximatif, accédez à la page de gestion des mots-clés du groupe d'abonnement.

1. Accédez à **Audience** > **Subscription Group Management** et sélectionnez un groupe d'abonnement **SMS/MMS/RCS**.
2. Dans **Global Keywords**, trouvez la catégorie **Opt-out** et sélectionnez l'icône de crayon.
3. Basculez **Fuzzy Opt-Out** sur **On**.
4. Sélectionnez votre option préférée pour la **Fuzzy Opt-Out Logic** :
   - **Automatically unsubscribe :** Lorsqu'un utilisateur envoie un message similaire à un mot-clé de désabonnement, il est immédiatement désabonné sans être invité à confirmer. Le message de confirmation de désabonnement standard est alors envoyé.
   - **Send opt-out instructions :** Lorsqu'un utilisateur envoie un message similaire à un mot-clé de désabonnement, Braze envoie une réponse personnalisée (le **Opt-out instruction message**) expliquant comment se désabonner.
5. Si vous avez sélectionné **Send opt-out instructions**, saisissez votre texte personnalisé dans le champ **Opt-out instruction message**. Ce champ est requis pour ce paramètre.
6. Sélectionnez **Save**.

![Section pour modifier les mots-clés de désabonnement et fournir un message d'instructions de désabonnement.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Bonnes pratiques pour les messages de désabonnement approximatif {#best-practices-for-fuzzy-opt-out-messages}

Pour garantir une expérience claire, conforme et positive pour vos utilisateurs abonnés, il est essentiel de configurer votre message de désabonnement approximatif de manière réfléchie. L'objectif principal du message de désabonnement approximatif est de **guider les utilisateurs qui envoient un message similaire, mais pas exactement identique, à votre mot-clé de désabonnement désigné**. Le message indique aux utilisateurs comment se désabonner avec succès.

### Considérations essentielles {#critical-considerations}

{% alert warning %}
Si vous avez sélectionné **Send opt-out instructions**, **ne configurez pas** votre message de désabonnement approximatif pour confirmer un désabonnement. Votre message de désabonnement approximatif ne doit pas contenir de formulation impliquant que l'utilisateur s'est déjà désabonné avec succès. Par exemple, **n'utilisez pas** « Vous avez été désabonné », « Vous ne recevrez plus de messages de ce numéro » ou « Vous êtes maintenant désabonné ».
{% endalert %}

Le message de désabonnement approximatif est envoyé avant que l'utilisateur ne se soit effectivement désabonné. Utiliser un langage de confirmation (tel que « Vous avez été désabonné ») induit l'utilisateur abonné en erreur en lui faisant croire qu'il est désabonné alors qu'il ne l'est pas, ce qui entraîne la poursuite de messages non souhaités, la frustration de l'utilisateur abonné et des risques de conformité importants.

Pour désabonner immédiatement les utilisateurs lors d'une correspondance approximative, utilisez plutôt le paramètre **Automatically unsubscribe**.

{% alert warning %}
**NE CONFIGUREZ PAS** votre message de désabonnement approximatif pour qu'il soit identique ou similaire à votre mot-clé de désabonnement exact.
{% endalert %}

Si votre message approximatif est identique ou trop proche de votre mot-clé de désabonnement exact (par exemple, si « STOP » est votre mot-clé exact et que votre message approximatif est « Envoyez STOP pour vous désabonner »), cela peut créer une confusion quant à savoir si le message initial de l'utilisateur a effectivement entraîné un désabonnement ou s'il doit effectuer une autre action. Le message approximatif doit toujours clarifier l'action que l'utilisateur doit entreprendre.

### Exemples de messages de désabonnement approximatif {#examples-of-fuzzy-opt-out-messages}

Si vous choisissez **Send opt-out instructions**, concentrez votre message sur l'accompagnement de l'utilisateur. Par exemple, si votre mot-clé de désabonnement est « STOP », voici de bons et de mauvais exemples de messages de désabonnement approximatif que vous pourriez créer :

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>« Pour vous désabonner de tous les messages, veuillez répondre avec le mot STOP. »</td>
      <td>« Vous avez été désabonné avec succès. Vous ne recevrez plus de messages de ce numéro. Répondez START pour vous réabonner. » (Il s'agit d'une confirmation directe de désabonnement, ce qui est trompeur dans un scénario de désabonnement approximatif.)</td>
    </tr>
    <tr>
      <td>« Nous avons bien reçu votre message. Si vous souhaitez ne plus recevoir de SMS, veuillez envoyer STOP. »</td>
      <td>« STOP. » (Il s'agit simplement du mot-clé exact lui-même, ce qui ne guide pas l'utilisateur.)</td>
    </tr>
    <tr>
      <td>« Souhaitiez-vous vous désabonner ? Répondez STOP pour ne plus recevoir de messages. »</td>
      <td>« Envoyez STOP pour vous désabonner. » (Si « STOP » est également votre mot-clé exact, cela est redondant et ne clarifie pas l'action si le message initial était approximatif.)</td>
    </tr>
  </tbody>
</table>