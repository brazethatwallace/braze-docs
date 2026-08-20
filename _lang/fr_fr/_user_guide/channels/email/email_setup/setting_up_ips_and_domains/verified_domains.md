---
nav_title: Domaines vérifiés
article_title: Domaines vérifiés
page_order: 0
page_type: tutorial
channel: email
description: "Cet article explique comment configurer des domaines vérifiés afin que Braze puisse gérer le DNS pour l'envoi d'e-mails et le suivi des clics HTTPS."
toc_headers: h2
---

# Domaines vérifiés {#verified-domains}

> Les domaines vérifiés vous permettent d'accorder à Braze le contrôle d'un sous-domaine spécifique pour automatiser la configuration des e-mails et le suivi HTTPS. Grâce à la délégation de domaine DNS, Braze gère les enregistrements DNS nécessaires à l'envoi d'e-mails et au suivi des clics. Par exemple, si votre sous-domaine est « mail.example.com », vous pouvez le déléguer à Braze pour configurer vos domaines d'envoi et de suivi.

{% alert important %}
Les domaines vérifiés ne prennent actuellement en charge qu'Amazon SES. Si vous utilisez SendGrid ou SparkPost, cette fonctionnalité n'est pas disponible.<br><br>Les domaines vérifiés sont pris en charge uniquement pour les e-mails. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

## Avantages {#benefits}

- Onboarding plus rapide : l'automatisation de ces étapes réduit le temps d'onboarding pour les e-mails.
- Moins de coordination : vous n'avez plus besoin de travailler avec le support Braze pour les tâches de configuration de domaine, ce qui vous rapproche d'une expérience entièrement en libre-service.
- Gestion SSL automatisée : Braze gère la création et le renouvellement des certificats SSL, ce qui élimine un point de défaillance courant et une charge manuelle. Sécuriser vos liens avec SSL est une bonne pratique standard : les destinataires sont plus susceptibles de faire confiance aux liens sécurisés, et la couche d'authentification supplémentaire contribue à protéger vos données.
- Moins d'erreurs de configuration : les flux d'onboarding guidés et la validation automatisée remplacent la configuration DNS manuelle sujette aux erreurs, ce qui réduit les risques de mauvaise configuration des enregistrements et de dysfonctionnement de la configuration e-mail.
- Surveillance proactive : Braze surveille vos enregistrements DNS et vous avertit lorsqu'il détecte des problèmes, au lieu d'attendre que les défaillances se manifestent.

## Considérations {#considerations}

Avant de commencer, gardez les points suivants à l'esprit :

- Choisissez un sous-domaine dédié. Une fois la délégation de domaine terminée, Braze gère tous les enregistrements DNS de ce sous-domaine. Braze recommande de déléguer un sous-domaine plutôt que le domaine parent de votre marque, car déléguer un domaine parent signifie que vous perdez la visibilité et le contrôle sur celui-ci. Si vous souhaitez utiliser un domaine parent, utilisez-en un qui n'est pas utilisé ailleurs.
- La délégation NS (serveur de noms) est requise pour que Braze puisse gérer les enregistrements DNS de votre sous-domaine, tels que SPF, DKIM et le suivi HTTPS, sans que vous ayez à configurer chacun d'entre eux manuellement.

{% alert note %}
La délégation CNAME n'est pas prise en charge. {% multi_lang_include product_feedback_cta.md context="gap" feature="CNAME delegation for verified domains" %}
{% endalert %}

- Prévoyez un sous-domaine d'envoi d'au moins trois niveaux. Étant donné que Braze crée un sous-domaine sous votre domaine délégué (tel que « mail.example.com »), votre domaine d'envoi doit comporter au moins trois niveaux. Par exemple : « e.mail.example.com ».
- Braze gère vos enregistrements DNS. Une fois la délégation terminée, Braze est responsable des enregistrements DNS sur le sous-domaine délégué. Ne modifiez pas ces enregistrements vous-même, car cela pourrait entraîner un problème avec l'envoi de vos e-mails.
- La permission « Edit Domain Settings » est requise pour configurer les domaines vérifiés.

## Étape 1 : Ajouter le domaine vérifié {#step-1-add-the-verified-domain}

1. Accédez à **Paramètres** > **Domaines vérifiés** > **Ajouter un domaine vérifié**.
2. Saisissez le sous-domaine et le nom racine. Par exemple, si vous déléguez le sous-domaine « mail.example.com » à Braze, le nom racine est « example.com » et le sous-domaine est « mail ».
3. Confirmez que le sous-domaine choisi n'est pas utilisé ailleurs et qu'il n'a pas d'enregistrements DNS en conflit.
4. Sélectionnez **Ajouter** pour recevoir les enregistrements TXT et NS.

## Étape 2 : Configurer les enregistrements DNS {#step-2-configure-dns-records}

Après avoir soumis le domaine vérifié, Braze génère les enregistrements DNS requis que vous devez ajouter à votre fournisseur DNS. Cette étape peut nécessiter une coordination avec votre équipe informatique ou DNS. Vous disposez de 30 jours pour que les enregistrements soient vérifiés avant qu'ils n'expirent. Passé ce délai, vous devrez recommencer la configuration.

{% alert tip %}
Confirmez que les quatre enregistrements NS sont explicitement présents à l'aide de la commande `dig` et que le domaine est validé dans le tableau de bord avant de considérer la configuration comme terminée. La vérification DNS expire après 30 jours.
{% endalert %}

## Étape 3 : Vérifier le domaine {#step-3-verify-the-domain}

Une fois les enregistrements DNS propagés, Braze vérifie que les enregistrements sont présents et correctement configurés dans un délai de 24 heures. En cas de vérification réussie :

- Le statut du domaine passe à **Vérifié**.
- Braze envoie un e-mail vous informant que le domaine est prêt.
- Le domaine apparaît comme actif dans la liste des **Domaines vérifiés**.

Une fois qu'un sous-domaine a été délégué avec succès, créez des domaines e-mail tels que vos domaines d'envoi et de suivi en accédant à **Ajouter un domaine personnalisé**. Vous serez ensuite redirigé vers la page **Vérification de l'expéditeur** pour terminer votre configuration. Pour les étapes détaillées, consultez [Configuration e-mail en libre-service]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve).