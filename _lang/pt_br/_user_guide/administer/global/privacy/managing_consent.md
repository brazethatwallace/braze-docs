---
nav_title: Gerenciar consentimento
article_title: Gerenciar consentimento
page_order: 1
page_type: reference
description: "Este artigo de referência fornece dicas sobre como gerenciar o consentimento usando a Braze."
---

# Gerenciar consentimento {#manage-consent}

> Este artigo de referência fornece dicas sobre como gerenciar o consentimento dos seus usuários usando a Braze.

A Braze não pode fornecer conselhos específicos sobre a interpretação de leis e regulamentos nem oferecer orientação sobre como lidar com o gerenciamento de consentimento, pois isso dependerá da interpretação da lei pela sua equipe jurídica. No entanto, oferecemos uma série de ferramentas de apoio à inscrição e ao gerenciamento de consentimento.

Sua abordagem deve depender do rigor exigido pela sua equipe jurídica com base na interpretação da lei. Aqui estão algumas opções a serem consideradas, listadas da mais rigorosa para a menos rigorosa:

- **Equipes:** Use [as equipes da Braze]({{site.baseurl}}/user_guide/administer/global/user_management/teams) para fazer uma verdadeira governança. Isso envolve adicionar um atributo personalizado a todos os perfis de usuário para indicar o status de consentimento, a data de consentimento ou ambos. Em seguida, é necessário migrar todas as Campaigns e Canvas para a equipe designada e ajustar as permissões de usuário no dashboard de acordo.
- **Atributo de perfil de usuário:** Adicione um atributo de consentimento a todos os perfis de usuário. Esse atributo indicará se um usuário deu consentimento ou não. No futuro, você poderá incluir um Segment or segmento or segmento de usuários que consentiram (por exemplo, `consent = true`) em todas as suas Campaigns e Canvas.
- **Grupos de inscrições específicos por canal:** Manipule os grupos de inscrições de canais específicos (notificações por push, e-mail, etc.) para gerenciar o consentimento. Inicialmente, marque os usuários como cancelados desses canais e só os marque como inscritos após terem dado consentimento.

{% alert important %}
Consulte sua equipe jurídica para determinar a abordagem adequada para a conformidade da sua organização com os requisitos de gerenciamento de consentimento.
{% endalert %}