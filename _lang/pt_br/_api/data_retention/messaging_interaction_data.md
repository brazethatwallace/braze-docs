---
nav_title: "Dados de interação de mensagens"
article_title: "Dados de interação de mensagens"
alias: "/messaging_interaction_data/"
page_order: 1
description: "Este artigo de referência aborda os dados de interação de Campaigns e Canvas e sua disponibilidade."
page_type: reference
---

# Sobre a disponibilidade dos dados de interação de mensagens {#about-messaging-interaction-data-availability}

> Saiba mais sobre os dados de interação de mensagens para Campaigns e Canvas, incluindo por quanto tempo a Braze os mantém e quais recursos os utilizam para redirecionamento.

### O que são dados de interação de mensagens? {#what-is-messaging-interaction-data}

Os dados de interação de mensagens referem-se a como um usuário interage com uma Campaign ou um Canvas que recebeu (por exemplo, quando um usuário abre a Campaign A ou um usuário recebe a variante A). Esses dados são usados para redirecionamento.

### Quando os dados de interação de mensagens ficam disponíveis? {#when-is-messaging-interaction-data-available}

Os dados de interação estão sempre disponíveis. Para Campaigns e Canvas ativos, os dados de interação estão sempre disponíveis em tempo real.

Para Campaigns e Canvas interrompidos, seus dados de interação expiram após três meses, a menos que sejam usados em filtros de redirecionamento por Campaigns ou Canvas ativos. Os dados de interação expirados são movidos para armazenamento de longo prazo e não ficam disponíveis para uso, a menos que sejam restaurados usando o processo descrito abaixo.

Os dados de interação expirados nunca são excluídos e podem ser restaurados a qualquer momento.

#### Recursos que usam dados de interação {#features-that-use-interaction-data}

Os seguintes recursos usam dados de interação de mensagens:

- Filtros de redirecionamento que redirecionam com base em uma Campaign ou Canvas específico
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- Filtros de redirecionamento que redirecionam com base em Campaigns ou Canvas de uma determinada tag
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- Listas **Campaigns Received** e **Canvas Messages Received** no perfil de usuário
- Endpoint `/users/export`
- Exportações CSV de **User Data** nas páginas de resumo de Campaigns e Canvas

Esses recursos não incluem dados de interação expirados em seus resultados. Para incluir dados de interação expirados nos resultados desses recursos, restaure a Campaign ou o Canvas com dados expirados.

Por exemplo, Canvas não podem ser lançados se os dados de interação estiverem expirados, o que significa que uma edição como adicionar uma equipe ao Canvas não pode ser salva.

#### Recursos que não usam dados de interação {#features-that-dont-use-interaction-data}

Os seguintes recursos **não** usam dados de interação de mensagens, o que significa que esses recursos não são afetados pela expiração dos dados de interação de mensagens:

- Configuração de Campaigns e Canvas
- Análise de dados de Campaigns e Canvas
- Relatórios de análise de dados (como Criador de relatórios, Criador de consultas e Relatórios de engajamento)
- Currents
- Snowflake Data Share
- Extensões de segmento
- Pontos de dados
- Os seguintes filtros de redirecionamento:
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

### Como restaurar dados de interação de mensagens? {#how-do-i-restore-messaging-interaction-data}

Para restaurar seus dados de interação, siga estas etapas:

1. Acesse a Campaign ou o Canvas expirado.
2. No topo da página inicial da Campaign ou do Canvas, selecione **Restore interaction data** no banner.

Você também pode restaurar dados de interação para múltiplas Campaigns na página **Campaigns**, selecionando as Campaigns e depois selecionando **Restore interaction data**.

O tempo para restaurar os dados de interação pode variar, mas na maioria dos casos, esse processo pode levar de 5 a 15 minutos. Após a conclusão da restauração, você receberá um e-mail.

#### Restauração por tag {#restoring-by-tag}

Você também pode restaurar dados de interação para Campaigns ou Canvas expirados com uma determinada tag.

1. Acesse a página **Campaigns** ou **Canvas** e pesquise pela tag relevante.
2. Selecione suas Campaigns ou Canvas.
3. Selecione **Restore interaction data** para restaurar os dados dessas Campaigns ou Canvas.

Após mais três meses de inatividade, essas Campaigns ou Canvas expiram novamente.

#### Redirecionamento por tag {#retargeting-by-tag}

Campaigns que usam filtros de redirecionamento que redirecionam por tag não estão isentas da expiração. Os filtros de redirecionamento que redirecionam por tag incluem:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

### Quando os dados de interação de mensagens estiveram disponíveis no passado? {#when-was-messaging-interaction-data-available-in-the-past}

Anteriormente, os dados de interação de mensagens eram excluídos quando uma Campaign ou Canvas:

- Não havia enviado mensagens em 25 meses corridos, E
- Não era usado para redirecionamento em nenhuma Campaign, Canvas ou Content Cards ativo.

Campaigns e Canvas com dados de interação de mensagens excluídos anteriormente não podem ser usados em filtros de redirecionamento para Campaigns, Canvas e Segments.