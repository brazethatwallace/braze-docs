---
page_order: 6
nav_title: Invites de poussée douce
article_title: Invites de poussée douce pour le Web
description: "Découvrez comment configurer les invites de poussée douce pour le SDK Web de Braze avant l'invite native d'autorisation de notifications du navigateur."
channel:
  - push notifications
---

# Invites de poussée douce pour le Web {#soft-push-prompts-for-web}

> Les invites de poussée douce sont des messages personnalisés que vous affichez avant l'invite native d'autorisation de notifications du navigateur. Elles expliquent pourquoi les utilisateurs devraient activer les notifications push et peuvent améliorer les taux d'abonnement par rapport à l'affichage de l'invite système dès la première visite. Ce guide explique comment implémenter les invites de poussée douce avec le SDK Web de Braze, notamment quand déclencher l'invite, comment personnaliser le contenu du message et les bonnes pratiques pour planifier la demande après que les utilisateurs ont compris la valeur des notifications push.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/soft_push_prompts.md %}
{% endsdktab %}
{% endsdktabs %}

## Questions fréquentes {#frequently-asked-questions}

### Qu'est-ce qu'une invite de poussée douce ? {#what-is-a-soft-push-prompt}

Une invite de poussée douce est un message in-app ou sur site personnalisé que vous affichez avant la boîte de dialogue native d'autorisation de notifications du navigateur. Elle explique la valeur des notifications push afin que les utilisateurs soient plus susceptibles d'accepter lorsque l'invite système apparaît.

### Quand dois-je afficher une invite de poussée douce ? {#when-should-i-show-a-soft-push-prompt}

Affichez une invite de poussée douce après que les utilisateurs ont compris la valeur de votre produit — par exemple, après l'onboarding ou une action significative dans l'application — et non au premier chargement de page. Consultez les étapes du SDK Web dans ce guide pour les détails de déploiement.