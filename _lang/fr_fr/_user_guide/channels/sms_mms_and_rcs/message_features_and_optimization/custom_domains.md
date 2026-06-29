---
nav_title: Domaines personnalisés en libre-service
article_title: Domaines personnalisés en libre-service
page_order: 2
description: "Cette page explique comment utiliser des domaines personnalisés avec le raccourcissement de liens pour personnaliser l'apparence de vos URL raccourcies."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Domaines personnalisés en libre-service {#self-serve-custom-domains}

> Cette page explique comment configurer vos propres domaines personnalisés dans le tableau de bord de Braze. Les domaines personnalisés vous permettent d'utiliser un lien raccourci de marque qui reflète l'identité de votre marque au lieu d'un lien raccourci générique ou du domaine Braze (`brz.ai`), améliorant ainsi la confiance des utilisateurs et l'engagement des campagnes avec les liens SMS.

Les domaines personnalisés en libre-service vous permettent de configurer et de gérer vos propres domaines personnalisés pour les SMS, le RCS et WhatsApp, directement depuis votre tableau de bord de Braze. Vous pouvez facilement ajouter, surveiller et gérer jusqu'à 10 domaines personnalisés en un seul endroit.

## Avantages des domaines personnalisés en libre-service {#benefits-of-self-serve-custom-domains}

- **Configuration simplifiée :** Configurez vos domaines sur la page **Paramètres de l'entreprise**, réduisant ainsi le temps de configuration.
- **Transparence accrue :** Recevez des mises à jour en temps réel sur l'état de configuration de votre domaine grâce à des bannières dans le tableau de bord.
- **Notifications proactives :** Recevez des alertes immédiates lorsque votre domaine personnalisé est connecté ou si des erreurs de configuration surviennent.

## Exigences relatives aux domaines {#domain-requirements}

- Les domaines doivent être achetés, détenus et gérés par vous. Cela peut être fait via un registraire de domaines, tel que GoDaddy, Amazon Route 53 ou Google Domains.
- Le domaine utilisé pour cette fonctionnalité doit être :
  - Unique (différent de votre domaine de site web)
  - Ne peut pas être utilisé pour héberger du contenu web
    - Vous pouvez également utiliser des sous-domaines uniques. Par exemple, le domaine `braze.com` pourrait avoir des sous-domaines tels que `sms.braze.com` ou `whatsapp.braze.com`.

## Délégation de votre domaine personnalisé {#delegating-your-custom-domain}

Nous vous demandons de déléguer votre domaine personnalisé à Braze afin que nous puissions faciliter le routage approprié et la compatibilité de l'infrastructure avec nos services de raccourcissement de liens et de suivi des clics. Lorsque vous déléguez votre domaine à Braze, nous gérons automatiquement le renouvellement du certificat pour éviter toute interruption de service.

## Ajout d'un domaine personnalisé {#adding-a-custom-domain}

1. Dans Braze, accédez à **Paramètres de l'entreprise** > **Domaines SMS/RCS et applications de messagerie**.
![Page « Domaines SMS/RCS et applications de messagerie » avec plusieurs domaines répertoriés.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. Sélectionnez **Add Domain** pour commencer la configuration d'un nouveau domaine personnalisé.
3. Saisissez le domaine personnalisé que vous avez acheté dans le champ de saisie de l'application, qui utilise notre logique de validation existante pour un formatage correct, puis sélectionnez **Next** et **Submit**.

![Bouton « Add Domain » sur la page « Domaines SMS/RCS et applications de messagerie ».]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. Demandez à votre équipe technique (comme l'ingénierie ou l'informatique) de mettre à jour votre configuration DNS avec les détails de l'enregistrement DNS Cloudflare affichés. Votre équipe technique doit mettre à jour vos enregistrements DNS avec ces détails dans un délai de 45 jours.
  - Si vous avez besoin de plus de temps pour mettre à jour vos enregistrements DNS, vous pouvez relancer le processus et générer un nouvel ensemble d'enregistrements DNS pour votre domaine.

Braze interrogera votre configuration DNS environ toutes les 30 minutes pour vérifier les mises à jour.

![Section « Enregistrement DNS » avec 3 étapes à compléter pour terminer la configuration de votre domaine.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
La progression de votre domaine est enregistrée automatiquement. Si vous devez quitter en cours de processus, vous pouvez reprendre plus tard en sélectionnant l'entrée de domaine en attente sur la page **Domaines SMS/RCS et applications de messagerie**.
{% endalert %}

### Gestion et utilisation continues {#ongoing-management-and-usage}

Une fois votre domaine vérifié, vos domaines personnalisés apparaîtront dans le tableau de la page **Domaines SMS/RCS et applications de messagerie** avec des indicateurs d'état. Vous pouvez immédiatement utiliser les domaines connectés sur plusieurs groupes d'abonnement, espaces de travail, et sur les canaux SMS, RCS et WhatsApp.

![Liste des domaines personnalisés et de leurs états.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

La surveillance en temps réel vous alertera dans le tableau de bord de Braze si l'un de vos domaines actifs rencontre un problème, afin que vos liens personnalisés restent utilisables. Si vous rencontrez des problèmes, consultez les détails de l'erreur dans l'application ou contactez l'[assistance]({{site.baseurl}}/braze_support/) Braze pour obtenir de l'aide.

## Attribution de domaines personnalisés aux groupes d'abonnement {#assigning-custom-domains-to-subscription-groups}

Une fois configurés, les domaines personnalisés peuvent être attribués à un ou plusieurs groupes d'abonnement SMS, RCS et WhatsApp.

1. Accédez à **Audience** > **Gestion des groupes d'abonnement**.
2. Recherchez et sélectionnez votre groupe d'abonnement dans la liste.
3. Sous **Détails du groupe d'abonnement**, sélectionnez votre domaine personnalisé dans le menu déroulant **Link Shortening Domain**.

Les campagnes envoyées avec le raccourcissement de liens activé utiliseront le domaine attribué associé à votre groupe d'abonnement SMS, RCS ou WhatsApp.

![Aperçu du compositeur de messages SMS avec un domaine de lien raccourci différent du domaine dans la zone « Message ».]({% image_buster /assets/img/custom_domain2.png %})

## Questions fréquentes {#frequently-asked-questions}

### Les domaines délégués peuvent-ils être partagés entre plusieurs groupes d'abonnement ? {#can-delegated-domains-be-shared-across-multiple-subscription-groups}

Oui. Un seul domaine peut être utilisé avec plusieurs groupes d'abonnement. Pour ce faire, sélectionnez le domaine pour chaque groupe d'abonnement auquel il doit être associé.

### Les domaines délégués peuvent-ils être partagés entre plusieurs espaces de travail ? {#can-delegated-domains-be-shared-across-multiple-workspaces}

Oui. Les domaines peuvent être associés à des groupes d'abonnement dans plusieurs espaces de travail, à condition que les espaces de travail soient contenus dans la même entreprise.

### Combien de domaines personnalisés puis-je ajouter ? {#how-many-custom-domains-can-i-add}

Vous pouvez ajouter jusqu'à 10 domaines personnalisés par tableau de bord.

### Que se passe-t-il si je ne mets pas à jour mes enregistrements DNS dans les 45 jours ? {#what-happens-if-i-dont-update-my-dns-records-within-45-days}

Bien que les détails de votre enregistrement DNS Cloudflare expirent après 45 jours, vous pouvez relancer le processus de configuration avec le même domaine et Braze générera un nouvel ensemble d'enregistrements DNS pour prolonger votre fenêtre de configuration.

### Serai-je notifié en cas d'erreur lors du processus de mise à jour DNS ? {#will-i-be-notified-if-there-is-an-error-during-the-dns-update-process}

Oui. En cas d'erreur, vous recevrez une bannière dans le tableau de bord de Braze détaillant le problème ainsi que les étapes pour le résoudre.

### Puis-je utiliser un domaine personnalisé sur plusieurs canaux ? {#can-i-use-a-custom-domain-across-multiple-channels}

Oui. Une fois qu'un domaine personnalisé est vérifié, il peut être utilisé dans tous les groupes d'abonnement SMS, RCS et WhatsApp sur tous les espaces de travail au sein d'un tableau de bord.

### Et si j'ai des questions ou besoin d'une assistance supplémentaire ? {#what-if-i-have-questions-or-need-further-support}

Pour des conseils plus détaillés sur la configuration et la gestion des domaines personnalisés, y compris les étapes de résolution des problèmes et les exigences techniques, [contactez l'assistance]({{site.baseurl}}/braze_support/).