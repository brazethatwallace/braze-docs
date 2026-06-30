---
nav_title: Consentement et collecte d'adresses
article_title: Consentement et collecte d'adresses
page_order: 6
page_type: reference
description: "Cet article de référence présente les bonnes pratiques pour recueillir le consentement et les adresses e-mail des utilisateurs, et définit les différents états d'abonnement possibles."
channel: email

---

# Consentement et collecte d'adresses {#consent-and-address-collection}

> Avant d'envoyer vos premiers e-mails, il est important d'obtenir d'abord la permission de vos clients. C'est une question de courtoisie, et cela fait des merveilles pour vos taux d'ouverture !

## États des abonnés {#subscriber-states}

Il existe trois états d'abonnement e-mail pour un utilisateur : **abonné**, **inscrit** et **désabonné**. Pour modifier l'état d'abonnement d'un utilisateur, consultez notre article sur la [modification des abonnements]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-subscriptions) ou utilisez nos [API d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status).

| État de l'abonné | Description |
|---|---|
| Abonné | Ces clients ont cliqué sur le lien dans un e-mail de confirmation et ont activement choisi de recevoir vos messages. |
| Inscrit | Par défaut, les utilisateurs sont inscrits aux e-mails tant qu'une adresse e-mail valide est enregistrée dans leur profil. Les utilisateurs restent inscrits jusqu'à ce qu'ils se désabonnent ou qu'ils choisissent de s'abonner. |
| Désabonné | Pour être marqué comme désabonné, un client s'est soit explicitement désabonné de vos e-mails, soit a signalé un e-mail comme spam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États des abonnés" }

## Méthodes de collecte des adresses {#address-collection-methods}

En plus d'obtenir la permission de vos utilisateurs avant de leur envoyer des messages, il existe plusieurs méthodes pour collecter ces adresses e-mail, et chacune peut avoir un impact sur votre livrabilité.

### Listes d'adresses achetées {#purchased-address-lists}

L'envoi d'e-mails à des listes achetées ou louées constitue une violation de votre contrat avec Braze ! Si vous achetez des adresses e-mail, vous envoyez des messages totalement non sollicités et vous vous exposez à des problèmes de livrabilité.

### Co-inscription {#co-registration}

La co-inscription désigne un accord entre entreprises pour collecter des informations sur les utilisateurs. Il s'agit d'une méthode de collecte risquée. Elle inscrit les utilisateurs à la réception d'e-mails de tiers, parfois sans que le client en ait connaissance ou ait donné son accord. Si vous optez pour cette approche, veillez à fournir des mentions claires et à offrir la possibilité de se désabonner au moment de la collecte.

### Abonnement pré-coché ou forcé {#pre-selected-or-forced-opt-in}

L'abonnement pré-coché est une méthode d'inscription par e-mail dans laquelle la case d'inscription est déjà cochée pour que les utilisateurs reçoivent vos e-mails. En laissant la case cochée, les utilisateurs donnent leur consentement à recevoir vos e-mails. Cette méthode a tendance à agacer les gens (elle est également illégale pour les e-mails envoyés vers ou au sein du Canada). Vous pourriez obtenir une liste d'e-mails de taille respectable, mais vous ne pouvez pas vraiment être sûr que ces utilisateurs souhaitent recevoir vos e-mails marketing.

### Abonnement simple {#single-opt-in}

L'abonnement simple se produit lorsque des utilisateurs s'inscrivent via un formulaire et sont immédiatement ajoutés à votre liste d'e-mails. Avec cette méthode, les utilisateurs effectuent une seule action pour s'abonner, comme saisir leur adresse e-mail dans un champ de collecte ou cocher une case dans le cadre d'une transaction.

### Abonnement confirmé {#confirmed-opt-in}

Un abonnement confirmé se produit lorsqu'un utilisateur coche une case demandant à recevoir des communications par e-mail, et qu'un message de confirmation lui est envoyé en retour. Cette méthode permet aux utilisateurs de choisir le type et la fréquence du contenu, ce qui améliore l'engagement.

Pour vous assurer de cibler uniquement les utilisateurs les plus engagés, vous pouvez également utiliser la méthode du double abonnement confirmé. Cette approche ajoute une étape supplémentaire dans laquelle l'utilisateur doit cliquer sur un bouton ou un lien dans l'e-mail de confirmation pour être ajouté à la liste d'e-mails.