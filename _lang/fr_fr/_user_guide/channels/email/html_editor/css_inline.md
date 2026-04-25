---
nav_title: Inclusion CSS
article_title: Inclusion CSS
page_order: 5.1
description: "Cet article de référence explique comment activer l'inclusion CSS et présente quelques bonnes pratiques."
channel:
  - email

---

# Inclusion CSS

> L'inclusion CSS est une forme de prétraitement des e-mails qui déplace les styles d'une feuille de style CSS dans le corps d'un e-mail HTML. Le terme « inlining » désigne le fait que les styles sont appliqués « inline » aux éléments HTML individuels.

Pour certains clients de messagerie, l'insertion CSS peut améliorer le rendu des e-mails et vous aider à confirmer que vos e-mails s'affichent comme prévu. Si la majorité de votre CSS est déjà insérée en ligne ou si vous êtes certain que votre HTML et votre CSS sont compatibles avec les exigences de la plupart des clients de messagerie, il n'est peut-être pas nécessaire d'activer cette fonctionnalité. Les styles incorporés dynamiquement peuvent entrer en conflit avec vos styles en ligne existants et modifier le rendu attendu de la prévisualisation et de l'e-mail.

## Utilisation de l'inclusion CSS

Vous pouvez activer ou désactiver l'insertion CSS pour n'importe quel e-mail à l'aide de la bascule **Activer l'insertion CSS** dans l'onglet **Informations d'envoi** de l'éditeur HTML.

![Case à cocher pour gérer l'insertion CSS dans le compositeur HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### État d'insertion par défaut

Vous pouvez définir un état par défaut (activé ou désactivé) de manière globale depuis **Paramètres** > **Préférences des e-mails**. Recherchez le paramètre **Insertion CSS**. Ce paramètre détermine la valeur par défaut avec laquelle tous les nouveaux e-mails sont créés. Notez que la modification de ce paramètre n'affectera aucun de vos e-mails existants. Vous pouvez également remplacer cette valeur par défaut à tout moment lors de la rédaction de vos e-mails.

![Option d'insertion CSS par défaut pour les nouveaux e-mails, située dans les paramètres des e-mails.]({% image_buster /assets/img_archive/css-inline1.png %})