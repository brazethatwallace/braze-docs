---
nav_title: Centro de Entregabilidade
article_title: Centro de Entregabilidade
alias: "/deliverability_center/"
page_order: 4
description: "Este artigo de referência explica como configurar o Centro de Entregabilidade, um recurso que permite que profissionais de marketing visualizem a reputação dos domínios de envio de e-mail e dos IPs, além de entender a entregabilidade dos seus e-mails."
channel:
  - email

---

# Centro de Entregabilidade {#deliverability-center}

> O Centro de Entregabilidade oferece mais insights sobre o desempenho dos seus e-mails, com suporte ao uso do [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para rastrear dados de e-mails enviados e coletar informações sobre o seu domínio de envio.

A entregabilidade de e-mail é o ponto central do sucesso de uma campanha. Usando o Centro de Entregabilidade no dashboard da Braze, você pode visualizar seus domínios por **IP Reputation** ou **Delivery Errors** para identificar e solucionar possíveis problemas de entregabilidade de e-mail.

Para acessar o Centro de Entregabilidade, você precisa das [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) listadas no dropdown a seguir para o seu espaço de trabalho.

{% details Permissões de usuário para o Centro de Entregabilidade %}

- View Campaigns
- Edit Campaigns
- Archive Campaigns
- View Canvases
- Edit Canvases
- Archive Canvases
- View Frequency Capping Rules
- Edit Frequency Capping Rules
- View Message Prioritization
- Edit Message Prioritization
- View Content Blocks
- View Feature Flags
- Edit Feature Flags
- Archive Feature Flags
- View Segments
- Edit Segments
- View IAM Templates
- Edit IAM Templates
- Archive IAM Templates
- View Email Templates
- Edit Email Templates
- Archive Email Templates
- View Webhook Templates
- Edit Webhook Templates
- Archive Webhook Templates
- View Email Link Templates
- Edit Email Link Templates
- View Media Library Assets
- Edit Media Library Assets
- Delete Media Library Assets
- View Locations
- Edit Locations
- Archive Locations
- View Promotion Codes
- Edit Promotion Codes
- Export Promotion Codes
- View Preference Centers
- Edit Preference Centers
- View Reports
- Edit Reports
- View Usage Data

{% enddetails %}

## Configure sua conta do Google Postmaster {#set-up-your-google-postmaster-account}

Antes de conectar à Central de Entregabilidade, você precisará configurar uma conta do Google Postmaster Tools. Você pode usar uma conta do Gmail pessoal ou de trabalho para configurar seu Google Postmaster.

1. Acesse o [dashboard do Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. Na parte inferior da página, selecione <i class="fas fa-plus-circle"></i> **Add domain**.
3. Insira seu domínio raiz (pai) para autenticar seu e-mail. Certifique-se de que o registro TXT esteja vinculado a esse domínio raiz (pai), **não** ao subdomínio que você está usando pela Braze. Verificar o domínio raiz (pai) permite que você adicione subdomínios posteriormente no Postmaster Tools sem criar registros TXT adicionais. Por exemplo, ao verificar `braze.com`, você pode adicionar `demo.braze.com` como um subdomínio separado no Postmaster Tools para visualizar métricas no nível do subdomínio.
4. O Google gera um registro TXT que pode ser adicionado diretamente ao DNS do seu domínio. Geralmente, isso é gerenciado por quem administra seu DNS. Para informações e orientações sobre como atualizar seu DNS específico, confira [Verificar seu domínio (etapas específicas por host)](https://support.google.com/a/topic/1409901).
5. Selecione **Next**. <br>![Um exemplo de domínio "demo.braze.com" para autenticar um e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Depois que o registro TXT for adicionado ao DNS, retorne ao dashboard do Google Postmaster Tools e selecione **Verify**. Essa etapa confirma que você é proprietário do domínio, para que possa acessar as métricas de entregabilidade do Gmail na sua conta do Postmaster. <br>![Um prompt para verificar a propriedade do domínio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})
7. Após verificar o domínio raiz (pai), adicione seus subdomínios de envio ao Google Postmaster.

{% alert note %}
Se seus subdomínios não estiverem incluídos na Central de Entregabilidade para o Google Postmaster, isso pode ser resultado de ter adicionado apenas o domínio raiz (pai) ao Google Postmaster. Depois que os domínios raiz forem verificados no Google Postmaster, você pode adicionar seus subdomínios, que são verificados automaticamente. Esse processo permite que o Google retorne métricas no nível do subdomínio, que podem então ser importadas para a Central de Entregabilidade da Braze.
{% endalert %}

## Integrar o Google Postmaster {#integrating-google-postmaster}

{% alert important %}
**Migração do Google Postmaster Tools v2**<br>
O Google está descontinuando a versão antiga do Postmaster Tools (v1) e lançou uma versão de nova geração (v2) com uma interface moderna e novos dashboards, incluindo um dashboard de conformidade para ajudar a monitorar a aderência às diretrizes de remetente do Gmail. Todos os usuários devem migrar para a v2 até 31 de outubro de 2026.<br><br>
Para reautorizar sua conexão com o Google Postmaster Tools, acesse **Integrações de parceiros** > **Parceiros de tecnologia**, abra **Google Postmaster** e selecione **Change Account** para reautenticar com as novas permissões da v2. Ao concluir, você será atualizado para a v2 e terá acesso aos novos dashboards e dados.<br><br>
Para saber mais, consulte o [anúncio do Google sobre o novo Postmaster Tools](https://support.google.com/mail/answer/16594218?hl=en).
{% endalert %}

Antes de configurar o Centro de Entregabilidade, verifique se seus domínios foram [adicionados ao Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Siga estas etapas para integrar com o Google Postmaster e configurar o Centro de Entregabilidade:

1. Acesse **Analytics** > **Email Performance**.
2. Selecione a guia **Deliverability Center**. <br>![Um Centro de Entregabilidade com o Google Postmaster desconectado.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecione **Connect with Google Postmaster**.
4. Selecione sua conta do Google e depois selecione **Allow** para permitir que a Braze visualize as métricas de tráfego de e-mail dos domínios registrados no Postmaster Tools.

Seus domínios verificados serão exibidos no Centro de Entregabilidade.

![Dois domínios verificados no Google Postmaster com reputação média e baixa.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Você também pode acessar o Google Postmaster no dashboard da Braze em **Integrações de parceiros** > **Parceiros de tecnologia** > **Google Postmaster**. Após a integração, a Braze importa dados de reputação e erros dos últimos 30 dias. Os dados podem não estar disponíveis imediatamente e podem levar alguns minutos para serem carregados.

### Autorização inválida ou expirada {#invalid-or-expired-authorization}

Se você receber um alerta informando que as credenciais de autorização do Google Postmaster Tools são inválidas, o envio de e-mails pela Braze **não** é afetado. Apenas a conexão entre a Braze e o Google Postmaster é interrompida, o que impede a sincronização dos dados de reputação e erros do Gmail com o Centro de Entregabilidade até que você reconecte.

Para restaurar a integração, acesse **Integrações de parceiros** > **Parceiros de tecnologia**, abra **Google Postmaster**, selecione **Disconnect** e depois refaça o fluxo de conexão (mesmas etapas de [Integrar o Google Postmaster](#integrating-google-postmaster)).

### Métricas e definições {#metrics-and-definitions}

As métricas e definições a seguir se aplicam ao Google Postmaster Tools.

#### Reputação de IP {#ip-reputation}

Para entender as classificações de reputação de IP, consulte esta tabela:

| Classificação de reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de gerar poucas reclamações de SPAM (como usuários clicando no botão "spam"). |
| Média/Razoável | Conhecido por gerar engajamento positivo, mas ocasionalmente recebe reclamações de SPAM. A maioria dos e-mails deste domínio é entregue na caixa de entrada, exceto quando as reclamações de SPAM aumentam. |
| Baixa | Conhecido por receber taxas elevadas de reclamações de SPAM regularmente. E-mails deste remetente provavelmente serão filtrados para a pasta de SPAM. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de SPAM. E-mails deste domínio quase sempre são rejeitados no momento da conexão ou filtrados para a pasta de SPAM. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reputação de IP" }

{% alert important %}
Os dados de reclamações de SPAM exibidos na Braze são baseados em relatórios de feedback loop (FBL) de provedores de e-mail que os compartilham, como Microsoft, Yahoo e Comcast. Quando os usuários desses provedores reportam um e-mail como SPAM, essas reclamações são enviadas de volta para a Braze.<br><br>
No entanto, o Gmail e o iCloud não operam feedback loops tradicionais e não reportam reclamações de SPAM de volta para a Braze. Isso significa:<br>
- Reclamações de SPAM de usuários do Gmail não são incluídas nas métricas da Braze nem estão disponíveis nos dados do Snowflake ou Currents.<br>
- Você pode visualizar dados de SPAM do Gmail apenas como porcentagens agregadas no [Gmail Postmaster Tools](https://www.gmail.com/postmaster/), não como endereços individuais.<br>
- Se você observar altas taxas de SPAM no Gmail Postmaster Tools, esses números não correspondem às métricas de reclamação de SPAM da Braze, porque o Gmail não compartilha esses dados com os remetentes.
{% endalert %}

#### Reputação do domínio {#domain-reputation}

Use a tabela a seguir para monitorar e entender as classificações de reputação do seu domínio e evitar que seus e-mails sejam filtrados para a pasta de SPAM.

| Classificação de reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de reclamações de SPAM muito baixas. Está em conformidade com as diretrizes de remetente do Gmail. E-mails raramente são filtrados para a pasta de SPAM. Tem um bom histórico de taxa de SPAM muito baixa. Está em conformidade com as [diretrizes de remetente do Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Média/Razoável | Conhecido por gerar engajamento positivo, mas ocasionalmente recebe um baixo volume de reclamações de SPAM. A maioria dos e-mails deste domínio chega à caixa de entrada (exceto quando há um aumento notável nos níveis de SPAM). |
| Baixa | Conhecido por receber reclamações de SPAM regularmente. E-mails deste remetente provavelmente serão filtrados para a pasta de SPAM. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de SPAM. E-mails deste domínio quase sempre são rejeitados no momento da conexão ou filtrados para a pasta de SPAM. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reputação do domínio" }

#### Autenticação {#authentication}

Use o dashboard de autenticação para verificar a porcentagem de e-mails que passaram pelo Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) e Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Tipo de gráfico | Definição |
| ----- | ---------- |
| SPF | Mostra a porcentagem de e-mails que passaram pelo SPF em relação a todos os e-mails do domínio que tentaram o SPF. Isso exclui qualquer e-mail falsificado. |
| DKIM | Mostra a porcentagem de e-mails que passaram pelo DKIM em relação a todos os e-mails do domínio que tentaram o DKIM. |
| DMARC | Mostra a porcentagem de e-mails que passaram pelo alinhamento DMARC em relação a todos os e-mails recebidos do domínio que passaram pelo SPF ou DKIM. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Autenticação" }

#### Criptografia {#encryption}

Consulte esta tabela para entender qual porcentagem do seu tráfego de entrada e saída é criptografada.

| Termo | Definição |
| ----- | ---------- |
| TLS de entrada | Mostra a porcentagem de e-mails recebidos (para o Gmail) que passaram pelo TLS em relação a todos os e-mails recebidos daquele domínio. |
| TLS de saída | Mostra a porcentagem de e-mails enviados (do Gmail) aceitos via TLS em relação a todos os e-mails enviados para aquele domínio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Criptografia" }

Para mais ideias sobre como melhorar a entregabilidade, leia [Armadilhas de entregabilidade e spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps). Consulte também nossas [Práticas recomendadas de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices) para verificar o que deve ser revisado antes de enviar uma campanha de e-mail.

## Configurar o Microsoft Smart Network Data Services (SNDS) {#set-up-microsoft-smart-network-data-services-snds}

Se a Microsoft é seu principal provedor de caixa de entrada, você pode visualizar os dados do Microsoft SNDS no Deliverability Center. Isso inclui IPs de envio dedicados para espaços de trabalho que usam Amazon SES, SendGrid ou SparkPost. Use esses dados para monitorar a integridade do IP e entender como os provedores de caixa de entrada da Microsoft estão avaliando seus envios.

O Microsoft SNDS fornece dados em nível de IP sobre reclamações de SPAM e volume de envio, conforme relatado por provedores de caixa de entrada da Microsoft, como Outlook, Hotmail e Live.

{% alert important %}
Se você não encontrar seus dados no Deliverability Center, entre em contato com o [Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) com uma lista dos seus endereços IP.
{% endalert %}

### Amazon SES

Para espaços de trabalho que enviam e-mail pelo Amazon SES, o Deliverability Center exibe métricas do Microsoft SNDS para seus IPs de envio dedicados. A Braze preenche retroativamente até 90 dias de dados históricos do SNDS quando esse recurso é ativado para o seu espaço de trabalho.

![Um exemplo de resultados do Microsoft SNDS, incluindo IPs de amostra, destinatários, comandos RCPT, comandos DATA, resultado do filtro e taxa de reclamação.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas e definições

As métricas a seguir se aplicam ao Microsoft SNDS.

#### Destinatários {#recipients}

Essa métrica se refere ao número de destinatários nas mensagens transmitidas pelo IP.

#### Comandos DATA {#data-commands}

Essa métrica rastreia o número de comandos DATA enviados pelo IP. Os comandos DATA fazem parte do protocolo SMTP usado para enviar e-mails.

#### Resultados do filtro {#filter-results}

Consulte esta tabela para entender os resultados do filtro

| Resultado | Definição |
| ----- | ---------- |
| Verde | Considerado SPAM pelo filtro de SPAM da Microsoft em até 10% do período determinado. |
| Amarelo | Considerado SPAM pelo filtro de SPAM da Microsoft entre 10% e 90% do período determinado. |
| Vermelho | Considerado SPAM pelo filtro de SPAM da Microsoft em mais de 90% do período determinado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Resultados do filtro" }

#### Taxa de reclamação {#complaint-rate}

Essa é a fração do tempo em que uma mensagem recebida do IP é reportada como indesejada por um usuário do Hotmail ou Windows Live durante o período de atividade. Os usuários têm a opção de reportar quase todas as mensagens como lixo eletrônico pela interface web.

Para calcular a taxa de reclamação, divida o número de reclamações pelo número de destinatários da mensagem.

| Resultado | Definição |
| ----- | ---------- |
| Menos de 0,3% | A taxa de reclamação ideal. |
| Mais de 0,3% | Revise seu processo de inscrição e verifique se o link de cancelamento de inscrição está funcionando. Considere também se o e-mail poderia ser mais personalizado para o seu público. |
| Mais de 100% | O SNDS exibe as reclamações referentes ao dia em que foram reportadas, e não retroativamente ao dia em que o e-mail reclamado foi entregue. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Taxa de reclamação" }

#### Hits de spam trap e período de mensagens de trap {#spam-trap-hits-and-trap-message-period}

{% alert important %}
A Microsoft não inclui mais contagens de hits de spam trap nem dados de período de mensagens de trap nos relatórios do SNDS. Para saber mais, consulte o [anúncio do SNDS da Microsoft](https://substrate.office.com/ip-domain-management-snds/snds).
{% endalert %}

Os hits de spam trap eram o número de mensagens enviadas para "contas de trap", que são contas mantidas pelo Outlook.com que não solicitam nenhum e-mail.

As colunas de início e fim do período de mensagens de trap mostravam quando as primeiras e últimas mensagens enviadas para contas de trap foram recebidas do IP durante o período de atividade.

{% alert tip %}
Se você está procurando registros relacionados a um dos seus domínios verificados na Braze, observe que o Deliverability Center lista seus dados do Google Postmaster ou do Microsoft SNDS, o que significa que é possível que uma dessas plataformas não tenha dados para compartilhar com a Braze. Como alternativa, tente manter uma entrega de e-mail consistente, pois isso pode levar a uma reputação mais alta.
{% endalert %}

## Reclamações de SPAM e loops de feedback {#spam-complaints-and-feedback-loops}

Um loop de feedback de e-mail (FBL) permite que remetentes de e-mail recebam relatórios quando destinatários marcam mensagens como SPAM. No entanto, o Gmail e o iCloud não oferecem loops de feedback tradicionais, o que significa que a Braze (por meio do SparkPost ou SendGrid) não recebe dados de reclamações de SPAM desses provedores.

Como os dados de reclamações de SPAM não estão disponíveis no Gmail e no iCloud, é importante usar outras ferramentas para monitorar a integridade e a reputação do seu e-mail com esses grandes provedores:

- Use o [Google Postmaster Tools](https://www.gmail.com/postmaster/) para monitorar a reputação do domínio e do IP, as taxas de SPAM e o engajamento dos usuários. Você pode integrar o Google Postmaster com a Braze conforme descrito em [Integrar o Google Postmaster](#integrating-google-postmaster).
- A Apple não oferece uma ferramenta pública de Postmaster equivalente à do Google. Concentre-se em manter métricas de engajamento sólidas e seguir as práticas recomendadas de e-mail.

Para manter uma boa entregabilidade com todos os provedores, implemente uma [política de sunset]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) para parar automaticamente de enviar e-mails a usuários não engajados. Isso ajuda a evitar que seus e-mails sejam marcados como SPAM e protege a reputação do remetente.