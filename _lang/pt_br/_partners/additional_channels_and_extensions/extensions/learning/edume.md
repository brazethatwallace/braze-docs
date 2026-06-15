---
nav_title: EduMe
article_title: EduMe
description: "Este artigo de referência descreve a parceria entre a Braze e a eduMe, uma ferramenta de treinamento baseada em dispositivos móveis que permite aproveitar o Conteúdo conectado da Braze para dar aos seus usuários acesso aos cursos e lições da eduMe em suas campanhas Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# EduMe

> [A eduMe](https://edume.com) é uma ferramenta de treinamento baseada em dispositivos móveis que oferece à sua força de trabalho o conhecimento de que ela precisa para ter sucesso, quando precisar, onde quer que esteja.

_Essa integração é mantida pela eduMe._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a eduMe aproveita o [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) da Braze para dar aos seus usuários acesso aos cursos e lições da eduMe em suas campanhas Braze. O progresso individual e do grupo pode então ser rastreado pela funcionalidade de relatórios da eduMe.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta eduMe | É necessário ter uma conta eduMe para aproveitar essa parceria. |
| Chave de API da eduMe | Você deve solicitar uma chave de API ao seu contato de sucesso do cliente da eduMe. Essa chave é usada na sua chamada de Conteúdo conectado da Braze. |
| Segredo de assinatura de link da eduMe | Você deve solicitar ao seu contato de sucesso do cliente na eduMe a configuração de um segredo de assinatura de link para sua organização. Esse segredo é usado para ativar links contínuos no Conteúdo conectado. Você não precisa fazer nada com esse segredo. |
| IDs de grupo e conteúdo da eduMe | Esses identificadores são necessários para configurar suas chamadas de Conteúdo conectado. Entre em contato com o atendimento ao cliente da eduMe para obter ajuda na obtenção desses identificadores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Crie sua chamada de Conteúdo conectado {#create-your-connected-content-call}

Para dar a um usuário acesso a um curso, lição ou pesquisa eNPS e rastrear o progresso dele em relação ao seu ID de usuário interno na eduMe, siga a chamada de API mostrada neste exemplo:

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

1. Substitua `YOUR-EDUME-API-KEY` pela sua chave de API da eduMe.<br><br>
2. Substitua `EDUME-CONTENT-LINK-AND-CONTENT-ID` pela string de link de conteúdo correspondente e pelo identificador de módulo, lição ou pesquisa. Esses identificadores podem ser encontrados na sua conta eduMe.
  - Curso: `getCourseLink?moduleId=12087`
  - Lição: `getLessonLink?lessonId=25805`
  - Pesquisa eNPS: `getSurveyLink?surveyId=654`<br><br>
3. Os usuários que chegam à eduMe por meio desse link são adicionados a uma equipe ou grupo da eduMe de sua escolha. Substitua `groupId` pelo ID da equipe relevante ou pelo ID do grupo da eduMe. Normalmente, usa-se o ID da equipe, exceto para cursos que exigem inscrição, caso em que se deve usar o ID do grupo.<br><br>
4. Inclua um campo apropriado para mapear o campo `externalUserId`. O exemplo de chamada de Conteúdo conectado usa `driver_id`, embora seu campo provavelmente seja diferente. Esse ID está disponível nos relatórios da eduMe, permitindo que você os correlacione com seus sistemas.<br><br>
5. Por fim, personalize e teste sua mensagem conforme necessário. Recomendamos que você envie pelo menos uma mensagem de teste, acesse o conteúdo da eduMe, conclua a lição ou o curso e verifique se a análise de dados da eduMe está sendo registrada.