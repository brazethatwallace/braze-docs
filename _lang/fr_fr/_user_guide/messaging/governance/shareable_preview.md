---
nav_title: Aperçu partageable
article_title: Partager un aperçu de message avec les parties prenantes
page_order: 5
page_type: reference
description: "Cet article de référence explique comment générer et partager un lien d'aperçu pour un message ou un contenu, afin que les parties prenantes sans accès au tableau de bord puissent le consulter avant son envoi."
---

# Partager un aperçu de message avec les parties prenantes {#share-a-message-preview-with-stakeholders}

> L'aperçu partageable vous permet de générer un lien vers un aperçu de votre message ou contenu et de le partager avec des réviseurs, tels que des parties prenantes, des équipes juridiques ou des équipes de conformité, qui n'ont pas accès à votre tableau de bord de Braze. Les destinataires peuvent consulter l'aperçu dans leur navigateur sans se connecter à Braze.

## Canaux pris en charge {#supported-channels}

Vous pouvez générer un lien d'aperçu partageable pour les canaux et types de contenu suivants :

- Bannières
- Content Blocks
- Content Cards
- E-mail et pied de page d'e-mail
- Pages de destination
- LINE
- Notifications push
- Pages d'abonnement
- SMS et RCS
- WhatsApp

{% alert note %}
L'aperçu partageable est déployé progressivement et peut ne pas encore être disponible pour chaque canal dans votre espace de travail. Contactez votre gestionnaire de compte Braze si vous ne voyez pas l'option pour un canal répertorié dans cette section.
{% endalert %}

## Fonctionnement de l'aperçu partageable {#how-shareable-preview-works}

Le comportement suivant est cohérent pour tous les canaux pris en charge.

### Générer un lien {#generating-a-link}

Lors de la composition de votre message ou contenu, sélectionnez **Copier le lien d'aperçu** pour générer un lien partageable. Braze copie automatiquement le lien dans votre presse-papiers.

- Le lien ouvre un instantané statique en lecture seule de votre message tel qu'il apparaissait au moment où vous avez généré le lien. Il ne se met pas à jour automatiquement lorsque vous continuez à modifier. Générez un nouveau lien pour capturer vos dernières modifications.
- Si votre message inclut de la personnalisation, comme du Liquid ou du contenu connecté qui se résout par rapport à un utilisateur test, un profil utilisateur personnalisé ou un utilisateur aléatoire, l'aperçu reflète cette même personnalisation, correspondant à ce que vous voyez dans **Aperçu et test**.
- Sélectionner **Régénérer le lien** crée un nouvel instantané avec sa propre date d'expiration. Cela n'invalide pas le lien précédent. Les deux liens continuent de fonctionner indépendamment jusqu'à leur expiration respective.

### Consulter le lien {#viewing-the-link}

Toute personne disposant du lien peut consulter l'aperçu. Aucune connexion à Braze ni aucune autorisation du tableau de bord n'est requise.

{% alert important %}
Traitez un lien comme tout autre document partageable : envoyez-le uniquement aux personnes auxquelles vous souhaitez donner accès, et évitez de le publier dans un espace public.
{% endalert %}

### Expiration du lien {#link-expiration}

- Chaque lien d'aperçu partageable expire sept jours après sa génération.
- Lorsqu'un lien expire, il ne s'ouvre plus. Générez un nouveau lien depuis le compositeur pour en obtenir un nouveau.
- Il n'est pas possible de révoquer ou de désactiver manuellement un lien avant son expiration. Régénérer un lien ne révoque pas le précédent ; chaque lien expire simplement selon son propre calendrier de sept jours.

## Particularités par canal {#per-channel-nuances}

Bien que l'expérience de base soit la même partout, quelques canaux présentent de petites différences à connaître.

{% alert note %}
L'aperçu partageable n'est pas disponible pour les messages in-app.
{% endalert %}

| Canal | Ce qui diffère |
|---|---|
| E-mail | L'aperçu inclut les champs À, De et ligne d'objet du message, en plus du corps du message. <br><br>Si vous personnalisez en tant qu'utilisateur personnalisé, les valeurs saisies comme propriétés de déclenchement API ou propriétés d'événement peuvent ne pas apparaître dans l'aperçu, même si elles s'affichent correctement dans **Aperçu et test**. Les attributs personnalisés, les utilisateurs test et les utilisateurs aléatoires ne sont pas affectés. |
| Bannière (éditeur par glisser-déposer) | L'aperçu reflète le contenu tel qu'il était la dernière fois que vous avez ouvert l'onglet **Aperçu** dans le compositeur, pas nécessairement vos modifications les plus récentes. <br><br>Ouvrez à nouveau **Aperçu** avant de générer ou de régénérer un lien pour vous assurer qu'il est à jour. |
| SMS et RCS | Ces deux canaux sont régis par la même fonctionnalité d'aperçu partageable, mais chacun génère son propre lien indépendant. |
| WhatsApp | L'aperçu partageable est disponible séparément pour les messages de modèle WhatsApp et les messages de réponse WhatsApp. |
| Content Blocks, pieds de page d'e-mail et pages d'abonnement | Ceux-ci génèrent un aperçu du contenu autonome, indépendamment de toute campagne ou de tout Canvas spécifique dans lequel il est utilisé. |
| Pages de destination | L'aperçu se comporte différemment pour les pages de destination que pour les autres canaux. Consultez [Prévisualiser la page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-5-preview-the-page) pour plus de détails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Particularités par canal" }

## Questions fréquentes {#frequently-asked-questions}

{% details Le destinataire a-t-il besoin d'un compte Braze pour consulter l'aperçu ? %}
Non. Toute personne disposant du lien peut consulter l'aperçu dans son navigateur sans se connecter.
{% enddetails %}

{% details L'aperçu se met-il à jour si je continue à modifier mon message ? %}
Non. Un lien d'aperçu partageable est un instantané au moment de sa création. Sélectionnez **Régénérer le lien** pour capturer vos dernières modifications et obtenir un nouveau lien.
{% enddetails %}

{% details Combien de temps le lien reste-t-il actif ? %}
Sept jours à compter de sa génération. Si vous régénérez le lien, le nouveau lien obtient sa propre expiration de sept jours, indépendante du précédent.
{% enddetails %}

{% details Puis-je révoquer un lien de manière anticipée ? %}
Non, vous ne pouvez pas révoquer un lien. Régénérer le lien n'invalide pas le précédent. Tous les liens fonctionnent jusqu'à leur expiration après sept jours.
{% enddetails %}