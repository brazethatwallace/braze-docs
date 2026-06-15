---
nav_title: "A2P 10DLC"
article_title: "A2P 10DLC"
page_order: 2.9
description: "Cet article traite de l'A2P 10DLC, explique pourquoi l'enregistrement 10DLC est nécessaire pour les clients utilisant des codes longs aux États-Unis, fournit des informations utiles sur les coûts et le débit, et explique comment démarrer le processus d'enregistrement."
page_type: reference
channel:
  - SMS

---

# Application-to-Person 10-Digit Long Codes (codes longs à 10 chiffres) {#application-to-person-10-digit-long-codes}

> L'A2P 10DLC désigne un système aux États-Unis qui permet aux entreprises d'envoyer des messages de type Application-to-Person (A2P) via un numéro de téléphone standard à code long de 10 chiffres (10DLC). Ces codes longs enregistrés bénéficient d'un débit plus élevé, d'une meilleure livrabilité et d'une conformité améliorée par rapport aux codes longs standard.

{% alert important %}
Tous les clients qui possèdent et/ou utilisent actuellement des codes longs américains pour envoyer des messages à des clients aux États-Unis sont tenus d'enregistrer leurs codes longs pour le 10DLC ; ceux qui ne le font pas verront l'ensemble de leurs messages fortement filtrés. Ce processus de demande prend 4 à 6 semaines.
{% endalert %}

## Pourquoi c'est nécessaire {#why-its-necessary}

Le service 10DLC a été créé spécifiquement pour faciliter l'envoi de messages A2P via des codes longs. Historiquement, les codes longs étaient destinés à la messagerie Person-to-Person (P2P), mais lorsqu'ils étaient utilisés à des fins marketing, les entreprises se retrouvaient limitées par un débit restreint et un filtrage accru.

Le 10DLC contribue à résoudre ces problèmes en offrant :
- **Un débit plus élevé** : les numéros 10DLC prennent en charge un volume de messages plus important que les codes longs classiques.
- **Une meilleure livrabilité** : les numéros 10DLC sont désignés pour le trafic A2P, de sorte que les messages envoyés avec ces numéros ont plus de chances d'atteindre le destinataire et sont moins susceptibles d'être filtrés ou rejetés par l'opérateur que les messages envoyés via des codes longs locaux classiques.
- **Une conformité améliorée** : l'utilisation d'un code long local pour l'envoi de messages commerciaux est contraire aux directives de la [CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Les numéros 10DLC ont été conçus pour l'envoi de messages en masse et permettent aux marques de se conformer aux réglementations du secteur sans dépendre des codes courts.
- **Un coût avantageux** : le 10DLC est une excellente option pour les entreprises qui souhaitent commencer à envoyer des SMS ou qui envoient des SMS en faibles volumes. Pour les marques envoyant des volumes de messages plus importants, supérieurs à 100 000 messages par jour, nous recommandons l'utilisation d'un code court.

Depuis 2019, les opérateurs ont commencé à adopter le 10DLC pour la messagerie commerciale, Verizon et AT&T prenant actuellement en charge le 10DLC, et nous nous attendons à ce que tous les principaux opérateurs suivent prochainement. Bien que cela puisse entraîner des désagréments à court terme, à long terme, les clients bénéficieront de meilleurs taux de livrabilité tout en protégeant leurs consommateurs contre les messages indésirables.

## Ce que vous devez savoir {#what-you-need-to-know}

### Accès {#access}

L'enregistrement des codes longs avec l'A2P 10DLC prend 4 à 6 semaines.

### Coûts {#costs}

L'enregistrement auprès de l'A2P 10DLC peut inclure plusieurs types de frais :

| Type de frais | Description |
| -------- | ---------- |
| Frais d'enregistrement | Frais nominaux appliqués lors de l'enregistrement de votre marque et de votre cas d'utilisation sur l'ensemble des principaux réseaux américains. |
| Frais de vérification secondaire | Les marques peuvent contester leur [score de confiance](#trust-score) et demander un processus de vérification secondaire pour améliorer leur débit global ; des frais sont associés à ce processus. |
| Frais d'opérateur | Frais facturés par les opérateurs pour les SMS et MMS sortants envoyés aux utilisateurs après l'enregistrement 10DLC. À compter du 1er octobre 2021, les frais d'opérateur seront plus élevés pour le trafic non enregistré (codes longs standard) que pour le trafic enregistré (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Coûts" }

Consultez l'article Twilio sur le 10DLC pour vérifier les [estimations de frais](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) mises à jour.

### Débit {#throughput}

Le débit de messages pour votre 10DLC dépend de plusieurs facteurs, notamment le score de confiance de la marque, les limites quotidiennes de messages et vos cas d'utilisation de messagerie.

#### Score de confiance de la marque {#trust-score}

Le Campaign Registry (TCR) est un organisme tiers qui utilise un algorithme de réputation pour examiner des critères spécifiques relatifs à votre entreprise et attribuer un score de confiance qui détermine le débit de messagerie pour chaque marque. Ce score de confiance est attribué lorsqu'un client s'enregistre pour la messagerie 10DLC aux États-Unis. Plus le score de confiance est élevé, meilleur sera le nombre de messages par seconde (MPS) que vous obtiendrez.

|     | Score de confiance | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Élevé | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Moyen | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Faible | 1-49 | 4 MPS | 4 MPS | 4 MPS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Score de confiance de la marque" }

{% alert tip %}
Les entreprises figurant dans l'indice Russell 3000 se verront accorder un débit élevé et un score de confiance de marque élevé après l'enregistrement et l'examen 10DLC.
{% endalert %}

#### Limites quotidiennes de messages {#daily-message-limits}

Les limites quotidiennes varient de 2 000 à 200 000 messages en fonction de votre score de confiance de marque et s'appliquent à l'ensemble des codes longs. Bien que des scores de confiance élevés offrent un débit de 60 messages par seconde, les limites quotidiennes de messages fixées par l'opérateur restent applicables. Cela signifie que les codes courts seraient une meilleure option si le pic quotidien de messages d'une marque dépasse la limite quotidienne imposée.

#### Cas d'utilisation de messagerie {#messaging-use-cases}

Le débit est également affecté par le type de cas d'utilisation de messagerie que vous choisissez. La plupart des clients relèvent du cas d'utilisation marketing standard ou marketing mixte. D'autres cas d'utilisation moins courants seront soumis à des valeurs de débit différentes.

Selon votre cas d'utilisation, le score de confiance nécessaire pour atteindre le débit maximum variera. Les tableaux suivants présentent les cas d'utilisation standard et les plages courantes de scores de confiance. Pour les cas d'utilisation spéciaux tels que les services d'urgence ou les œuvres caritatives, consultez la [documentation Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Cas d'utilisation standard | Description |
| ------------------ | ----------- |
| Marketing | Contenu promotionnel tel que les soldes et les offres à durée limitée. |
| Mixte | Campagne couvrant plusieurs cas d'utilisation, comme le service client. |
| Enseignement supérieur | Campagnes destinées aux établissements d'enseignement supérieur. |
| Sondages et votes | Sondages et votes non politiques, tels que les enquêtes clients. |
| Annonces d'intérêt public | Annonces d'intérêt public visant à sensibiliser sur un sujet donné. |
| Service client | Assistance, gestion de compte et autres interactions client. |
| Notifications de livraison | Messages sur l'état de la livraison. |
| Notifications de compte | Notifications sur l'état d'un compte. |
| 2FA | Toute authentification ou vérification de compte, comme les OTP. |
| Alertes de sécurité | Notification d'un système compromis. |
| Alertes de fraude | Messages concernant une activité potentiellement frauduleuse. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation de messagerie" }

{% tabs %}
{% tab Cas d'utilisation déclaré %}
Un cas d'utilisation déclaré signifie que vous avez choisi un cas d'utilisation spécifique non marketing (par exemple, 2FA ou notifications de compte).

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Cas d'utilisation de messagerie" }

{% endtab %}
{% tab Cas d'utilisation marketing mixte %}

Les cas d'utilisation marketing mixte peuvent être enregistrés pour les clients qui souhaitent envoyer des messages pour plusieurs cas d'utilisation à partir du même ensemble de numéros ou à des fins marketing.

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Cas d'utilisation de messagerie" }

{% endtab %}
{% endtabs %}

Consultez l'article Twilio sur le 10DLC pour vérifier les [estimations de débit](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) mises à jour.

## Étapes suivantes {#next-steps}

Les clients qui ne se sont pas encore enregistrés pour le 10DLC doivent travailler avec leur gestionnaire de la satisfaction client pour enregistrer leurs codes longs. **Si les clients n'enregistrent pas leurs codes longs, à compter du 1er octobre 2021, tout expéditeur A2P utilisant des codes longs verra l'ensemble de ses messages fortement filtrés.** Contactez votre gestionnaire de la satisfaction client pour démarrer votre enregistrement 10DLC.