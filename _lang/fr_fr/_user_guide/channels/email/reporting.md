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

### E-mails rejetés {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy :** Essayez une autre adresse, réengagez sur un autre canal ou retirez l'adresse de la liste de suppression uniquement pour vos propres adresses de test. Évitez de supprimer les suppressions d'utilisateurs réels, car cela peut nuire à la réputation.
- **Mailbox full / invalid account :** Il s'agit souvent d'un signal de qualité de liste. Priorisez les utilisateurs qui ont récemment ouvert ou cliqué (par exemple, au cours des 30 à 60 derniers jours) pendant que vous nettoyez les adresses inactives ou invalides.

#### Comportement de réessai en cas d'échec provisoire d'envoi {#soft-bounce-retry-behavior}

Lorsqu'un e-mail subit un échec provisoire d'envoi en raison de problèmes temporaires (tels qu'une boîte de réception pleine, un serveur temporairement indisponible ou d'autres défaillances de livrabilité transitoires), Braze retente automatiquement la livraison pendant un maximum de 72 heures. Le nombre de tentatives de réessai varie selon le destinataire.

Si l'e-mail n'est pas livré avec succès après la période de réessai, Braze enregistre un événement d'échec provisoire d'envoi pour cet envoi de Campaign. Ces échecs provisoires d'envoi n'apparaissent pas dans les analyses de la campagne, mais vous pouvez :
- Les surveiller dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) pour consulter les raisons du rejet
- Utiliser le [filtre de Segment « Échec provisoire d'envoi »]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced) pour exclure ces utilisateurs des envois futurs

En raison de cette période de réessai, les indicateurs de livraison des e-mails (livraisons, rejets et taux de spam) peuvent ne pas totaliser 100 % pour les Campaigns où les e-mails ayant subi un échec provisoire d'envoi ne parviennent finalement pas à être livrés.

Pour plus d'informations sur les échecs provisoires d'envoi, consultez le [Glossaire d'analyse des e-mails]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Domaines invalides {#invalid-domains}

Des erreurs telles que `unable to get mx info` signifient souvent que de nombreuses cibles utilisent des domaines incorrects (par exemple, des fautes de frappe). Segmentez, exportez, corrigez et réimportez ces profils.

### IP limitées en débit {#throttled-ips}

Vous pouvez voir le message `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) si un fournisseur de messagerie ralentit ou bloque temporairement la livraison depuis votre IP en raison du volume, de la réputation, ou des deux. Braze retente les messages différés ; si les reports se concentrent à partir de ce phénomène, vous observerez souvent des échecs provisoires d'envoi élevés en parallèle.

Ce schéma signifie généralement que vous envoyez plus vite que ce que le fournisseur de messagerie accepte pour votre réputation actuelle. En plus d'améliorer l'engagement et la qualité de la liste, utilisez la [limitation du débit de livraison]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) pour plafonner la vitesse à laquelle les messages quittent Braze pour une Campaign ou un Canvas. Cela contribue à réduire la limitation de débit pendant que vous travaillez avec votre équipe de livrabilité sur des correctifs à plus long terme.

Si la limitation de débit persiste pour des domaines spécifiques, réduisez le volume vers ces domaines et contactez le support livrabilité de Braze pour obtenir des conseils.

### Statut de réputation IP inconnu {#unknown-ip-reputation-status}

Si votre rapport de performance des e-mails affiche une valeur « inconnu » pour la réputation IP, cela peut être lié à une panne de Google Postmaster Tools. Google Postmaster Tools fournit des données de réputation pour la livrabilité Gmail, et des interruptions de service temporaires peuvent entraîner des valeurs de réputation manquantes ou inconnues.

Si vous constatez un statut de réputation inconnu et avez des questions sur la livrabilité de vos e-mails, contactez le [support Braze]({{site.baseurl}}/support_contact).