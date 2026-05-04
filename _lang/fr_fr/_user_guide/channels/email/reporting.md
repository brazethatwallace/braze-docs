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

# Rapports e-mail

> Cet article présente les différents composants de vos rapports e-mail et indique où les trouver dans le tableau de bord.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Résolution des problèmes

### E-mails rejetés (bounces)

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy :** Essayez une autre adresse, réengagez le contact sur un autre canal ou supprimez l'adresse de la liste de suppression uniquement pour vos propres adresses de test. Évitez de retirer les suppressions d'utilisateurs réels, car cela peut nuire à votre réputation.
- **Boîte pleine / compte invalide :** Il s'agit souvent d'un signal lié à la qualité de votre liste. Priorisez les utilisateurs ayant récemment ouvert ou cliqué (par exemple, au cours des 30 à 60 derniers jours) pendant que vous nettoyez les adresses inactives ou invalides.

### Domaines invalides

Des erreurs telles que `unable to get mx info` signifient souvent que de nombreux destinataires utilisent des domaines incorrects (par exemple, des fautes de frappe). Segmentez, exportez, corrigez et réimportez ces profils.

### IP limitées (throttling)

Si un serveur destinataire limite le débit de votre IP, réduisez le volume d'envoi vers ce domaine, améliorez l'engagement et contactez l'assistance livrabilité si la limitation persiste.