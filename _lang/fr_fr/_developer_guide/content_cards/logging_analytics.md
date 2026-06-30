---
nav_title: Enregistrer les analyses
article_title: Enregistrer les analyses
page_order: 1
description: "Cet article explique comment enregistrer manuellement les impressions, les clics, les rejets et gérer le comportement au clic pour vos Content Cards personnalisées."
toc_headers: "h2"

---

# Enregistrer les analyses {#log-analytics}

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Rejets uniques supérieurs aux impressions uniques {#unique-dismissals-higher-than-unique-impressions}

Si les *rejets uniques* dépassent les *impressions uniques*, votre intégration personnalisée de Content Cards a enregistré des rejets sans enregistrer les impressions pour ces mêmes cartes. L'interface par défaut des Content Cards de Braze enregistre les deux automatiquement, ce décalage n'apparaît donc que lorsque vous utilisez une interface personnalisée.

Enregistrez une impression chaque fois que vous affichez une carte, et enregistrez un rejet lorsque l'utilisateur la ferme. Pour les noms de méthodes et des exemples, consultez les sections par plateforme ci-dessous.

## Analyses manquantes pour les Content Cards {#missing-content-cards-analytics}

Si les Content Cards s'affichent correctement dans votre application mais que vous ne recevez systématiquement aucune donnée analytique (impressions, clics, etc.), il s'agit probablement d'un problème d'intégration SDK.

- **Vues personnalisées de Content Cards (Android, iOS, Web) :** L'interface par défaut de Braze enregistre automatiquement les impressions et les clics sur toutes les plateformes. Si vous utilisez une vue ou une implémentation personnalisée de Content Cards, vous devez appeler explicitement les méthodes d'enregistrement appropriées dans votre application. Consultez [Enregistrer les analyses]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) pour votre plateforme. Pour les implémentations Web personnalisées en particulier, vérifiez que le SDK Web de Braze est chargé, consultez la console du navigateur pour détecter d'éventuelles erreurs et assurez-vous que les données des cartes sont bien reçues.
- **Initialisation du SDK et identification de l'utilisateur :** Assurez-vous que le SDK est entièrement initialisé avant d'afficher les cartes. Les événements sont silencieusement ignorés (et non mis en file d'attente) si le SDK n'est pas initialisé, s'il est en mode d'initialisation différée ou s'il est désactivé pour le RGPD. Le SDK enregistre bien les analyses pour les utilisateurs anonymes, mais les indicateurs du tableau de bord comme « impressions quotidiennes uniques » nécessitent une identité utilisateur résolue. Appelez donc `changeUser` avant l'affichage des cartes dans la mesure du possible.

## ID de Content Card {#content-card-id}

Chaque envoi d'une Campaign à un destinataire génère un nouvel ID de Content Card. Si le même utilisateur reçoit la Campaign à nouveau lors d'un envoi ultérieur, Braze attribue un nouvel ID. Référencez l'`id` de la carte lorsque vous enregistrez les impressions, les clics et les rejets dans vos implémentations personnalisées.