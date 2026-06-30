---
nav_title: Rapports
article_title: Rapports e-mail
page_order: 21
description: "Cet article de référence présente les différents composants des rapports e-mail et indique où les trouver dans le tableau de bord."
tool:
  - Reports
channel:
  - email

---

# Rapports e-mail {#email-reporting}

> Cet article présente les différents composants de vos rapports e-mail et indique où les trouver dans le tableau de bord.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Résolution des problèmes {#troubleshooting}

### E-mails rejetés (bounces) {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy :** Essayez une autre adresse, réengagez le contact sur un autre canal ou supprimez l'adresse de la liste de suppression uniquement pour vos propres adresses de test. Évitez de retirer les suppressions d'utilisateurs réels, car cela peut nuire à votre réputation.
- **Boîte pleine / compte invalide :** Il s'agit souvent d'un signal lié à la qualité de votre liste. Priorisez les utilisateurs ayant récemment ouvert ou cliqué (par exemple, au cours des 30 à 60 derniers jours) pendant que vous nettoyez les adresses inactives ou invalides.

### Domaines invalides {#invalid-domains}

Des erreurs telles que `unable to get mx info` signifient souvent que de nombreux destinataires utilisent des domaines incorrects (par exemple, des fautes de frappe). Segmentez, exportez, corrigez et réimportez ces profils.

### IP limitées (throttling) {#throttled-ips}

Le message `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` peut apparaître dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) lorsqu'un fournisseur de messagerie ralentit ou bloque temporairement la réception depuis votre IP en raison du volume, de la réputation, ou des deux. Braze retente automatiquement l'envoi des messages différés ; si les reports se concentrent sur ce motif, vous observerez souvent une hausse des échecs provisoires d'envoi en parallèle.

Ce schéma signifie généralement que vous envoyez plus vite que ce que le fournisseur de messagerie accepte compte tenu de votre réputation actuelle. En plus d'améliorer l'engagement et la qualité de votre liste, utilisez la [limitation du débit de réception]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) pour plafonner la vitesse à laquelle les messages quittent Braze pour une campagne ou un Canvas. Cela contribue à réduire le throttling pendant que vous travaillez avec votre équipe livrabilité sur des correctifs à plus long terme.

Si la limitation persiste pour des domaines spécifiques, réduisez le volume d'envoi vers ces domaines et contactez l'assistance livrabilité de Braze pour obtenir des recommandations.