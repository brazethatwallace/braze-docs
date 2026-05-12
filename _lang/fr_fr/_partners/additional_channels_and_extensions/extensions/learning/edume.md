---
nav_title: eduMe
article_title: eduMe
description: "Cet article de référence présente le partenariat entre Braze et eduMe, un outil de formation mobile qui vous permet de tirer parti du Contenu connecté de Braze pour donner à vos utilisateurs un accès aux cours et leçons d'eduMe dans vos Campaigns Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com) est un outil de formation pour appareils mobiles qui fournit à tout moment et en tout lieu à votre personnel les connaissances dont il a besoin pour réussir.

_Cette intégration est maintenue par eduMe._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et eduMe s'appuie sur le [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) de Braze pour permettre à vos utilisateurs d'accéder aux cours et leçons d'eduMe dans vos Campaigns Braze. Les progrès individuels et collectifs peuvent ensuite être suivis grâce à la fonctionnalité de reporting d'eduMe.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte eduMe | Un compte eduMe est nécessaire pour bénéficier de ce partenariat. |
| Clé API eduMe | Vous devez demander une clé API à votre contact de satisfaction client eduMe. Cette clé est utilisée dans votre appel de Contenu connecté Braze. |
| Secret de signature de lien eduMe | Vous devez demander à votre contact de satisfaction client chez eduMe de mettre en place un secret de signature de lien pour votre organisation. Ce secret est utilisé pour activer les liens fluides dans le Contenu connecté. Vous n'avez rien à faire avec ce secret. |
| ID de groupe et de contenu eduMe | Ces identifiants sont nécessaires pour configurer vos appels de Contenu connecté. Contactez votre contact de service client eduMe pour obtenir ces identifiants. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

### Créer votre appel de Contenu connecté {#create-your-connected-content-call}

Pour donner à un utilisateur l'accès à un cours, une leçon ou une enquête eNPS, et pour suivre ses progrès par rapport à votre ID utilisateur interne dans eduMe, suivez l'appel API présenté dans cet exemple :

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Remplacez `YOUR-EDUME-API-KEY` par votre clé API eduMe.<br><br>
2. Remplacez `EDUME-CONTENT-LINK-AND-CONTENT-ID` par la chaîne de caractères du lien de contenu et l'identifiant du module, de la leçon ou de l'enquête correspondants. Ces identifiants se trouvent dans votre compte eduMe.
  - Cours : `getCourseLink?moduleId=12087`
  - Leçon : `getLessonLink?lessonId=25805`
  - Enquête eNPS : `getSurveyLink?surveyId=654`<br><br>
3. Les utilisateurs qui arrivent sur eduMe par ce lien sont ajoutés à une équipe ou un groupe eduMe de votre choix. Remplacez `groupId` par l'ID de l'équipe ou du groupe eduMe concerné. Vous utilisez généralement l'ID de l'équipe, sauf pour les cours qui requièrent une inscription, auquel cas vous devez utiliser l'ID du groupe.<br><br>
4. Incluez un champ approprié pour mapper le champ `externalUserId`. L'exemple d'appel de Contenu connecté utilise `driver_id`, mais votre champ sera probablement différent. Cet ID est disponible dans les rapports eduMe, ce qui vous permet de les mettre en corrélation avec vos systèmes.<br><br>
5. Enfin, personnalisez et testez votre message si nécessaire. Nous vous recommandons d'envoyer au moins un message de test, d'accéder au contenu eduMe, de terminer la leçon ou le cours et de vérifier que les analyses eduMe sont bien enregistrées.