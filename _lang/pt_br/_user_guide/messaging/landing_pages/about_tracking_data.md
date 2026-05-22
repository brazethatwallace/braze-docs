---
nav_title: Sobre o rastreamento de dados
article_title: Sobre o rastreamento de dados de landing pages
description: "Saiba mais sobre rastreamento e dados anonimizados para landing pages na Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Sobre o rastreamento de dados de landing pages {#about-landing-page-tracking-data}

> Saiba mais sobre rastreamento e dados anonimizados para landing pages na Braze.

## Métodos de rastreamento {#tracking-methods}

### SDK para web {#web-sdk}

O SDK para web da Braze é inicializado quando um usuário envia um formulário em uma landing page. Antes do envio do formulário, nenhum dado pessoal é coletado e o SDK não rastreia ativamente os usuários. Após a conclusão da inicialização, o SDK não armazena nenhum dado no navegador (como cookies, armazenamento local ou outros).

O SDK para web da Braze é inicializado imediatamente quando um usuário navega até a landing page por meio de um link gerado por uma {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag em uma mensagem da Braze.

Quando um formulário é enviado, o SDK coleta os seguintes dados:

- Evento de envio de formulário (nome do evento e horário do envio)
- Dados especificados pela sua equipe no formulário (como nome, e-mail e número de telefone)
- Horário de início da sessão
- ID do dispositivo (um ID único que é gerado, mas não armazenado, para o dispositivo)
- País determinado pelo endereço IP

### Dados anonimizados {#anonymized-data}

Antes de um usuário enviar um formulário, os dados rastreados em uma landing page consistem apenas em informações anonimizadas e não identificáveis. Isso inclui métricas agregadas padrão de sites, como o número de visualizações de página (impressões) e cliques que uma landing page recebe.

Como esses dados não estão vinculados a usuários identificáveis, eles não podem ser usados para redirecionar ou rastrear o comportamento individual de usuários.

## Mesclando perfis de usuário duplicados {#merging-duplicate-user-profiles}

A Braze não mescla automaticamente usuários com base em atributos, como e-mail ou telefone, quando um formulário de landing page é enviado. Se um formulário for enviado com um e-mail ou número de telefone que corresponda a um perfil de usuário existente, a Braze cria um perfil de usuário separado.

Para mesclar perfis de usuário duplicados, você pode:

- Acionar o [endpoint `/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) quando um formulário de landing page for enviado para mesclar o novo perfil com um perfil existente.
- Programar a [mesclagem em massa]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#bulk-merging) para mesclar periodicamente perfis duplicados com base em identificadores correspondentes.