---
nav_title: Outubro
page_order: 3
noindex: true
page_type: update
description: "Este artigo contém notas de versão de outubro de 2016."
---

# Outubro de 2016 {#october-2016}

## Novas configurações de segurança {#new-security-settings}
Adicionamos recursos de segurança aprimorados à Braze, incluindo regras de expiração de senha, regras de comprimento de senha, regras de complexidade de senha, lista de permissões de login de IP no dashboard e autenticação de dois fatores.

> Atualização: As **Configurações de segurança** da Braze, acessadas na página **Configurações da empresa**, também incluem regras para reutilização e expiração de senhas.

## Baixar CSV após a importação {#csv-download-after-import}
Os usuários da empresa agora podem baixar CSVs de usuários importados recentemente. Isso oferece mais visibilidade na sincronização de dados dos seus sistemas. Saiba mais sobre a [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/).

## Filtro de aniversário {#anniversary-filter}
Além do [filtro de aniversário de nascimento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/), a Braze agora oferece um filtro de aniversário que permite direcionar os usuários com base em uma data do calendário para marcos de fidelidade, avisos de recarga e muito mais! Acesse esse recurso selecionando o filtro "Date of Custom Attribute" na página Segments. Saiba mais sobre [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Atualizações do limite de frequência {#frequency-capping-updates}
Anteriormente, uma Campaign ou um Canvas que ignorasse as restrições de limite de frequência ainda contaria para os limites de frequência. Alteramos o comportamento para que, por padrão, novas Campaigns e Canvas que não obedeçam aos limites de frequência também não sejam contabilizados para esses limites. Isso é configurável para cada Campaign e Canvas. Saiba mais sobre o [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## Perfis de cores de mensagens no app {#in-app-message-color-profiles}
Adicionamos [perfis de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) para mensagens no app, permitindo que os clientes reutilizem esquemas de cores da marca ao criar novas mensagens na Braze.