---
nav_title: Double abonnement
article_title: Double abonnement
description: "Cet article de référence couvre la fonctionnalité de double abonnement et explique comment activer cette fonctionnalité, sélectionner les mots-clés d'abonnement et les messages de réponse, et faire entrer les utilisateurs dans le flux de double abonnement via des mises à jour d'abonnement effectuées par la REST API, le SDK et les mises à jour du centre de préférences."
page_type: reference
page_order: 1
channel:
  - SMS
  - MMS
  - RCS
---

# Double abonnement {#double-opt-in}

> La fonctionnalité de double abonnement exige que les utilisateurs confirment explicitement leur intention d'abonnement avant de pouvoir recevoir des messages SMS, MMS ou RCS. Cela concentre l'envoi de messages sur les utilisateurs engagés et soutient les bonnes pratiques de conformité.

Lorsque le double abonnement est activé, les utilisateurs reçoivent un message leur demandant leur consentement explicite avant de pouvoir être contactés par vos Campaigns ou Canvas.

Bien que ce ne soit pas une exigence explicite du Telephone Consumer Protection Act de 1991 (TCPA), Braze recommande de configurer le double abonnement pour confirmer que les utilisateurs sont informés et consentent à faire partie de votre programme SMS, MMS ou RCS. Pour plus d'informations sur la conformité, consultez [Lois, réglementations et prévention des abus pour les SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).

## Flux de double abonnement {#double-opt-in-workflows}

Le double abonnement vous permet d'obtenir un consentement explicite via des campagnes d'abonnement entrantes et sortantes.

### Sortant {#outbound}

Lorsqu'un utilisateur fournit son numéro de téléphone, il reçoit un message lui demandant son consentement.

![Capture d'écran d'un message SMS sortant où la marque envoie « Bienvenue aux mises à jour texte de MARQUE ! 1 msg par semaine pour les dernières offres. Répondez Y pour vous abonner. », l'utilisateur répond « Y », et la marque répond « Merci ! Vous êtes maintenant abonné aux alertes MARQUE. Voici un code promo SMS10 pour 10 % de réduction sur votre premier achat ! »]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Entrant {#inbound}

Lorsqu'un utilisateur envoie un message contenant un mot-clé d'abonnement, il reçoit un message lui demandant son consentement.

![Capture d'écran d'un message SMS entrant où un utilisateur envoie « JOIN » et reçoit la réponse « Répondez Y pour confirmer que vous souhaitez rejoindre notre programme SMS. 3 msg/semaine, envoyez STOP à tout moment pour STOP », puis répond « Y ».]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Activer le double abonnement {#enabling-double-opt-in}

Pour activer le double abonnement, accédez au tableau **Global Keywords** dans le groupe d'abonnement concerné, puis cliquez sur **Edit** dans la catégorie **Opt-In Keyword Category**. Ensuite, sélectionnez votre méthode d'abonnement (**Opt-In** ou **Double Opt-In**). Sélectionner **Double Opt-In** développera la page pour afficher des [champs configurables](#configurable-fields) supplémentaires.

![La section Méthode d'abonnement propose deux méthodes au choix : Opt-In et Double Opt-In.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Champs configurables {#configurable-fields}

| Catégorie | Champs | Description
| ----------- |----------- |----------------
| Demande d'abonnement | Mots-clés | Ce sont les mots-clés qu'un utilisateur peut envoyer par SMS pour indiquer son intention d'abonnement. `START` est un mot-clé obligatoire. Cette demande d'abonnement sera également envoyée à l'utilisateur lorsque son statut d'abonnement est mis à jour par les sources listées dans la section [Sources d'abonnement](#subscription-sources).
| | Message de réponse | C'est la réponse initiale qu'un utilisateur recevra après avoir envoyé un mot-clé d'abonnement (par exemple, « Répondez Y pour confirmer que vous souhaitez recevoir des messages de ce numéro. Des frais de messages et données peuvent s'appliquer. »)
| Confirmation de double abonnement | Mots-clés | Ce sont les mots-clés avec lesquels un utilisateur peut répondre pour confirmer son intention d'abonnement. Au moins un mot-clé est requis. Ces mots-clés doivent être spécifiés dans le champ **Message de réponse de la demande d'abonnement**.
| | Message de réponse | C'est la réponse de confirmation qu'un utilisateur recevra après avoir explicitement confirmé son abonnement et être désormais joignable par message. Le statut du groupe d'abonnement de l'utilisateur sera défini sur `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurable fields #configurable-fields" }

Lorsqu'un utilisateur reçoit une demande d'abonnement, il dispose de 30 jours pour confirmer son intention d'abonnement. Si un utilisateur souhaite s'abonner après cette fenêtre de 30 jours, il doit envoyer un mot-clé d'abonnement pour relancer le flux de double abonnement.

![Les champs configurables comportent deux sections, Demande d'abonnement et Confirmation de double abonnement, chacune avec les champs Mots-clés et Message de réponse.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Statut du groupe d'abonnement {#subscription-group-status}

Ce n'est qu'après avoir complété le flux de double abonnement que le [statut du groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) de l'utilisateur est mis à jour sur `Subscribed`. Si l'utilisateur commence le flux mais ne le termine pas, il reste `Unsubscribed` et ne peut pas recevoir de messages de ce groupe d'abonnement.

Les utilisateurs peuvent également entrer dans le flux de double abonnement s'ils sont [abonnés depuis d'autres sources]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) (par exemple, REST API, SDK).

## Sources d'abonnement {#subscription-sources}

Les utilisateurs peuvent également entrer dans le flux de double abonnement via des mises à jour d'abonnement effectuées en dehors des messages entrants. Ces sources incluent les mises à jour provenant de la REST API, du SDK et du centre de préférences. Lorsqu'un utilisateur entre dans le flux de double abonnement via ces sources, il reçoit le **message de réponse de la demande d'abonnement**.

{% alert important %}
Lorsque les utilisateurs entrent dans le flux de double abonnement via des sources autres que les messages entrants, ils reçoivent au maximum un message de réponse de demande d'abonnement sur une période glissante de 24 heures, quel que soit le nombre de fois où ils entrent dans ce flux.
{% endalert %}

Chaque source d'abonnement a un comportement d'inscription différent, comme décrit dans le tableau suivant.

| Source | Comportement d'inscription au double abonnement
| ----------- | -----------
| SDK | Les utilisateurs entreront automatiquement dans le flux de double abonnement lorsqu'ils s'abonnent via le SDK Braze.
| REST API | Les utilisateurs peuvent entrer dans le flux lorsque le statut d'abonnement est défini via `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` et que le paramètre facultatif `use_double_opt_in_logic` est passé avec la valeur `true` (par exemple, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Si ce paramètre est omis, les utilisateurs n'entreront pas dans le flux de double abonnement.
| Shopify | Les utilisateurs n'entreront pas dans le flux de double abonnement lorsque leur statut d'abonnement est défini par notre intégration Shopify.
| Importation d'utilisateurs | Les utilisateurs n'entreront pas dans le flux de double abonnement lorsque leur statut d'abonnement est défini par l'importation d'utilisateurs.
| [Centre de préférences]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/) | Les utilisateurs entreront automatiquement dans le flux de double abonnement lorsqu'ils s'abonnent via un centre de préférences.
| Étape de mise à jour utilisateur | Les utilisateurs peuvent entrer dans le flux de double abonnement lorsque leur statut d'abonnement est défini via l'étape de mise à jour utilisateur et que le paramètre facultatif `use_double_opt_in_logic` est passé avec la valeur `true`. Si ce paramètre est omis, les utilisateurs n'entreront pas dans le flux de double abonnement.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription sources #subscription-sources" }

## Prise en charge multilingue {#multi-language-support}
Pour les messages entrants, le double abonnement est pris en charge pour toutes les langues définies dans le groupe d'abonnement. Cela signifie que vous pouvez définir vos réponses automatiques dans différentes langues et Braze enverra la réponse automatique associée à une langue spécifique lorsqu'un mot-clé correspondant est reçu.

Les utilisateurs qui entrent dans le flux de double abonnement via des mises à jour d'abonnement effectuées en dehors des messages entrants (par exemple, SDK, REST API, Shopify) recevront uniquement les mots-clés en anglais.