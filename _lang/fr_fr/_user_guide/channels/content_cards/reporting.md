---
nav_title: Rapports
article_title: Rapports sur les cartes de contenu
page_order: 21
description: "Cet article de référence offre un aperçu des différents indicateurs et options d'analytique disponibles pour les cartes de contenu dans le tableau de bord de Braze."
channel:
  - content cards
tool:
  - Reports

---

# Rapports sur les cartes de contenu {#content-card-reporting}

> Cet article de référence offre un aperçu des différents indicateurs et options d'analytique disponibles pour les cartes de contenu dans le tableau de bord de Braze.

## Quand les envois sont enregistrés {#when-sends-are-logged}

Le moment où un événement _Envoyé_ est enregistré pour les Content Cards dépend du type de distribution et du paramètre **Création de la carte**.

### Livraison planifiée {#scheduled-delivery}

Pour les Content Cards planifiées, le moment de l'événement _Envoyé_ dépend du paramètre **Création de la carte** :

- **Au lancement de la campagne :** l'envoi est enregistré à l'heure d'envoi planifiée, lorsque la carte est inscrite dans le flux de l'utilisateur. Cela se produit que l'utilisateur ait ouvert l'application ou consulté la carte ou non.
- **À la première impression :** l'envoi est enregistré la première fois que l'application demande la carte après l'heure d'envoi planifiée, lorsque la carte est créée à la demande.

Si votre campagne est configurée pour utiliser **À la première impression** (recommandé), le nombre d'_Envoyés_ dans l'analytique de la campagne augmente progressivement à mesure que les applications demandent la carte. Si l'application ne demande jamais la carte (par exemple, si l'utilisateur n'ouvre jamais l'application) avant son expiration, aucun envoi n'est enregistré et la carte n'est jamais distribuée. Si votre campagne est configurée pour utiliser **Au lancement de la campagne**, le nombre d'_Envoyés_ dans l'analytique de la campagne augmente brusquement à l'heure planifiée.

### Livraison par événement {#action-based-delivery}

Pour les Content Cards déclenchées par une action, l'envoi est enregistré peu après que l'utilisateur a effectué l'action déclencheuse, lorsque la carte est inscrite dans son flux. Cela se produit que l'utilisateur ait consulté la carte ou non.

### Filtres Campaigns reçues et reciblage {#campaigns-received-and-retargeting-filters}

Quel que soit le type de distribution ou le paramètre **Création de la carte**, une campagne de cartes de contenu n'apparaît dans le profil de l'utilisateur sous **Campaigns reçues** qu'après que celui-ci a effectivement consulté la carte dans l'application. Les filtres de reciblage **Dernier message reçu** et **Dernière campagne reçue** sont mis à jour au moment de la consultation pour la même raison.

{% multi_lang_include analytics/campaign_analytics.md channel="Content Card" %}