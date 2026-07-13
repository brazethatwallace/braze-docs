---
nav_title: DataGrail
article_title: DataGrail
description: "Cet article de référence décrit le partenariat entre Braze et DataGrail, une plateforme de gestion de la confidentialité, qui vous permet de détecter les données des consommateurs collectées et stockées dans Braze pour traiter rapidement les DSR."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), une plateforme de gestion de la confidentialité, aide à renforcer la confiance des consommateurs et à éliminer les risques commerciaux. Grâce à la détection continue des systèmes et au traitement automatisé des requêtes de droits des personnes concernées (DSR), DataGrail alimente les programmes de confidentialité, garantissant la conformité aux lois et réglementations sur la confidentialité en constante évolution, comme le RGPD, la CCPA et la CPRA.

_Cette intégration est maintenue par DataGrail._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et DataGrail vous permet de détecter les données des consommateurs collectées et stockées dans Braze pour traiter rapidement les DSR (requêtes d'accès, de suppression et de non-vente). Braze sera ajouté à un plan précis de l'endroit où les données des consommateurs se trouvent dans votre organisation grâce à un mappage de données automatisé — plus besoin d'enquêtes ou de feuilles de calcul pour maintenir un cadre de confidentialité ou produire un registre des activités de traitement (RoPA).

## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Compte DataGrail | Un compte DataGrail est nécessaire pour profiter de ce partenariat.<br>Contactez votre administrateur ou envoyez un e-mail à support@datagrail.io pour toute question ou problème concernant l'intégration. |
| Clé API de Braze | Une clé API REST de Braze avec les autorisations `events.list`, `users.export.ids`, `users.delete` et `users.track`.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu des API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration {#integration}

Connectez-vous au portail DataGrail et sélectionnez **Connect** sur la page d'intégration de Braze. Saisissez ensuite votre instance et votre clé API Braze, puis sélectionnez **Connect Braze**.

S'il y a des comptes Braze supplémentaires à intégrer :
1. Sélectionnez **Edit Connection** sur la page d'intégration de Braze.
2. Dans la liste déroulante, sélectionnez **+Add New Connection**.
3. Sous **Connection Name**, saisissez un nouveau nom pour identifier ce compte distinct (par exemple, Braze Training Account).
4. Saisissez une instance Braze distincte et une clé API pour ce nouveau compte.
5. Sélectionnez **Connect**.

Envoyez un e-mail à DataGrail à l'adresse support@datagrail.io pour toute question ou problème concernant votre intégration.