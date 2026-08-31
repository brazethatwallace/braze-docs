---
nav_title: "Autorisations géographiques"
article_title: "Autorisations géographiques"
description: "Cet article présente la liste de pays autorisés pour les autorisations géographiques, qui vous permet de choisir vers quels pays les SMS, MMS et RCS peuvent être envoyés."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# Autorisations géographiques {#geographic-permissions}

> Les autorisations géographiques renforcent la sécurité et protègent contre le trafic frauduleux de SMS, MMS et RCS en appliquant des contrôles sur les pays vers lesquels vous pouvez envoyer des messages. Vous pouvez spécifier une liste de pays autorisés pour vous assurer que les messages SMS, MMS et RCS ne sont envoyés que vers des régions approuvées. Les messages ne sont envoyés qu'aux numéros de téléphone correspondant aux indicatifs téléphoniques de ces pays.<br><br> Seuls les administrateurs peuvent modifier la liste de pays autorisés. Les utilisateurs non administrateurs ont accès à une version en lecture seule de la liste qui indique vers quels pays un groupe d'abonnement peut envoyer des messages.

Si vous êtes administrateur, vous pouvez configurer les pays figurant sur la liste autorisée. La liste de pays autorisés est configurée au niveau du [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups). Vous pouvez y accéder en allant dans **Audience** > **Gestion des groupes d'abonnement** et en sélectionnant un groupe d'abonnement SMS, MMS ou RCS. La liste autorisée se trouve sous **Autorisations géographiques**.

![La section modifiable des autorisations géographiques pour un administrateur, avec plusieurs pays sélectionnés dans la « liste de pays autorisés ».]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## Sélection des pays {#selecting-countries}

Ajoutez des pays à la liste autorisée à l'aide du menu déroulant. Les pays les plus courants pour les SMS, MMS et RCS apparaissent en haut, les autres étant affichés dans la section suivante. Vous pouvez également rechercher des pays en saisissant du texte dans le champ de recherche.

![Le menu déroulant « Liste autorisée des pays » avec les pays les plus courants affichés en haut.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Supprimez les pays précédemment sélectionnés en décochant les cases correspondantes.

### Enregistrer vos modifications {#saving-your-changes}

Les modifications prennent effet après l'enregistrement. Retirer des pays de votre liste autorisée empêche l'envoi de tous les messages SMS, MMS et RCS vers les numéros de téléphone utilisant les indicatifs téléphoniques de ces pays.

![Fenêtre modale d'avertissement confirmant les pays qui seront supprimés de la liste autorisée.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Pays à risque élevé de fraude {#high-fraud-risk-countries}

Certains pays présentent un risque plus élevé de trafic artificiellement gonflé (traffic pumping) par SMS, MMS et RCS. Ces pays sont identifiés par une étiquette **High Fraud Risk** dans le menu déroulant des pays.

![Le menu déroulant des pays avec l'Azerbaïdjan affichant une étiquette « High Fraud Risk ».]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Si vous autorisez l'envoi vers ces pays, vous devez d'abord reconnaître le risque associé avant que le pays ne soit ajouté à votre liste autorisée.

{% alert note %}
Limitez les pays de votre liste autorisée à ceux strictement nécessaires pour répondre à vos besoins commerciaux. Cela réduit votre exposition au trafic frauduleux. Pour plus de conseils sur la prévention du trafic artificiellement gonflé par SMS, MMS et RCS, consultez la [FAQ sur la fraude par traffic pumping SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud).
{% endalert %}

## Visibilité des envois en dehors de la liste autorisée {#visibility-of-sends-outside-the-allowlist}

Les tentatives d'envoi vers des pays qui ne figurent pas sur votre liste de pays autorisés seront abandonnées. Les messages abandonnés seront consignés dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) et dans l'[événement d'engagement lié aux messages SMS abandonnés]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

Les messages abandonnés pour les destinataires situés dans des pays ne figurant pas sur votre liste autorisée apparaissent en tant qu'**Aborted Message Errors** et contiennent le message « The recipient's phone number is in a blocked country ».

![Journal d'abandon montrant plusieurs envois SMS, MMS et RCS abandonnés parce que le pays du numéro de téléphone ne figure pas sur la liste de pays autorisés.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## Avis important concernant les pays à haut risque de fraude et la fraude par gonflement de trafic {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### Qu'est-ce que le gonflement de trafic SMS, MMS et RCS ? {#what-is-sms-mms-and-rcs-traffic-pumping}

Le gonflement de trafic SMS, MMS et RCS (également connu sous le nom de trafic artificiellement gonflé) est un schéma de fraude en pleine expansion qui peut entraîner une exposition financière significative pour les clients. Les fraudeurs peuvent exploiter vos formulaires web publics non protégés, vos flux d'authentification ou vos endpoints d'API pour déclencher l'envoi de volumes importants de SMS, MMS et RCS (tels que des confirmations d'abonnement, des mots de passe à usage unique ou des notifications) vers des numéros de téléphone qu'ils contrôlent ou influencent. Les attaquants perçoivent ensuite une part des revenus auprès de réseaux mobiles complices ou non informés pour avoir généré ce trafic artificiel. L'impact en aval entraîne une exposition financière significative.

### Quels sont les pays à haut risque de fraude ? {#what-are-high-fraud-risk-countries}

Un pays ou territoire est désigné comme étant à haut risque de fraude s'il présente une densité anormalement élevée de petits opérateurs locaux à tarification premium en itinérance, ou s'il ne dispose pas d'une surveillance réglementaire stricte. Les acteurs malveillants ciblent systématiquement ces réseaux d'opérateurs à tarifs élevés, car ils maximisent la part de revenus par message généré.

De plus, les restrictions de routage système sont appliquées en fonction des indicatifs de pays de destination plutôt que de la localisation physique réelle du destinataire. Cela signifie que si vous avez des clients qui voyagent fréquemment, vous n'avez pas besoin d'ajouter leurs destinations de voyage à votre liste d'autorisation de pays, car les messages seront acheminés en fonction de l'indicatif du pays de destination d'origine, et non de leur localisation physique actuelle. Par exemple, les territoires partageant un indicatif de pays avec des régions à moindre risque (comme Jersey ou Guernesey qui partagent l'indicatif +44 avec le Royaume-Uni) présentent tout de même une exposition élevée aux tarifs des opérateurs et sont gérés selon les mêmes conditions du cadre de haut risque de fraude.

### Responsabilité du client et responsabilité financière {#customer-responsibility-and-financial-liability}

Le client est responsable de tous les messages mobiles envoyés par le biais des Services en son nom, y compris les messages résultant du gonflement de trafic SMS, MMS et RCS, et sera facturé en conséquence. Les mesures de protection de la plateforme, telles que la liste d'autorisation de pays, vous aident à restreindre la distribution aux régions de confiance. En définitive, cependant, la sécurisation de vos endpoints exposés et la prévention de dommages financiers dévastateurs restent de la seule responsabilité du client.

### Comment prévenir le gonflement de trafic {#how-to-prevent-traffic-pumping}

Ne pas limiter strictement la distribution de vos messages aux régions géographiques où résident vos clients réels crée une vulnérabilité immédiate à la fraude et un préjudice financier grave. Pour protéger votre entreprise, vous devez restreindre de manière proactive vos régions de distribution en utilisant la liste d'autorisation de pays. De plus, et surtout, vous devez sécuriser tout formulaire en ligne de demande de numéro de téléphone ou endpoint d'API qui déclenche des envois SMS, MMS et RCS, conformément aux bonnes pratiques du secteur, comme décrit dans [Comprendre et prévenir la fraude par gonflement de trafic SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud).