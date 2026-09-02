---
nav_title: Sobre o Audience Sync
article_title: Sobre o Audience Sync
alias: /partners/about_audience_sync/
description: "Este artigo de referência aborda como usar o Audience Sync da Braze para o Facebook, para veicular anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 0
tool:
  - Canvas
---

# Sobre o Audience Sync {#about-audience-sync}

> O recurso de Audience Sync da Braze ajuda você a expandir o alcance das suas campanhas para muitas das principais tecnologias sociais e de publicidade. Por meio do [BRAZE CANVAS]({{site.baseurl}}/user_guide/messaging/canvas), as marcas podem sincronizar dinamicamente e com segurança os dados de usuários de primeira parte no ecossistema de publicidade para impulsionar a eficiência de marketing e operacional.

## Disponibilidade do recurso {#feature-availability}

Todos os clientes da Braze têm acesso imediato ao Audience Sync para Google e Facebook, mas clientes com Action Credits podem acessar todos os parceiros do Audience Sync. Para desbloquear destinos adicionais do Audience Sync para clientes que não possuem Action Credits, adquira o Audience Sync Pro. Entre em contato com seu gerente de conta da Braze para mais detalhes.

## Casos de uso {#use-cases}

- Direcionar usuários de alto valor usando canais próprios e pagos para impulsionar compras ou engajamento incrementais.
- Criar públicos semelhantes aos seus usuários de alto valor para otimizar custos de aquisição e conversões de novos usuários.
- Redirecionar usuários com anúncios que são menos responsivos a outros canais de marketing.
- Criar públicos de supressão para evitar que usuários recebam anúncios quando já são consumidores fiéis da sua marca.

## Visão geral {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| Destino | Tempo para o destino corresponder membros do público | Limite de frequência | Lookalike ou actalike | Dicas |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | Até 24 horas | 250.000 solicitações por minuto. Agrupadas a cada 5 segundos com nova tentativa automática. | Sim | {::nomarkdown}<ul><li>O Criteo suporta até 1.000 públicos de anúncios.</li><li>O tamanho mínimo do público é 500, e o recomendado é acima de 20.000.</li></ul>{:/} |
| [Facebook ou Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | Até 24 horas | 190.000 contas de anúncios por hora | Sim | {::nomarkdown}<ul><li>O Facebook suporta até 500 públicos de anúncios.</li><li>O Facebook exige que os públicos tenham pelo menos 1.000 usuários.</li></ul>{:/} |
| [Google Ads ou YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | Entre 6 e 12 horas | Agrupadas a cada 5 segundos com nova tentativa automática baseada no feedback do Google | Não | {::nomarkdown}<ul><li><b>Correspondência de clientes:</b> Use ID de anúncio para dispositivos móveis, ou endereço de e-mail ou número de telefone.</li><li>Os públicos do Google exigem pelo menos 5.000 usuários para começar a veicular anúncios.</li><li>O tamanho do público será exibido como zero até que haja pelo menos 1.000 usuários.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 48 horas | O LinkedIn processa 10 consultas por segundo e 100.000 usuários por solicitação. A Braze agrupa os usuários a cada 5 segundos. | Públicos preditivos com IA | {::nomarkdown}<ul><li>O tamanho mínimo do público é de 300 membros, com o direcionamento por local levado em consideração.</li><li>O LinkedIn exibe a taxa de correspondência no dashboard da Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | Entre 24 e 48 horas | O Pinterest processa 7 consultas por segundo e 1.900 usuários por solicitação. A Braze agrupa os usuários a cada 5 segundos. | Sim | Os públicos do Pinterest exigem pelo menos 100 usuários. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/D | O Snapchat processa 10 consultas por segundo e 100.000 usuários por solicitação. A Braze agrupa os usuários a cada 5 segundos. | Sim | O Snapchat suporta até 1.000 públicos de anúncios. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | Até 24 horas | N/D | Sim | {::nomarkdown}<ul><li>Não há tamanho mínimo de público para públicos de CRM no The Trade Desk.</li><li>Não há limite para a quantidade de públicos que o The Trade Desk suporta.</li><li>Se você sincronizar com um público cuja região esteja definida como UE, o número de telefone não é suportado.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | Entre 24 e 48 horas | O TikTok processa 50 consultas por segundo e 10.000 usuários por solicitação. A Braze agrupa os usuários a cada 5 segundos. | Sim | {::nomarkdown}<ul><li>O TikTok suporta até 400 públicos de anúncios.</li><li>Os públicos do TikTok exigem pelo menos 1.000 usuários para começar a veicular anúncios.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Visão geral" }
<sup>Quando o limite de frequência é atingido, a Braze tenta novamente as sincronizações por 13 horas.</sup>

## Como funciona {#how-it-works}

Para usar o Audience Sync com o Google ou Facebook, conecte sua conta de anúncios pesquisando o parceiro na página **Technology Partners**.

![Parceira de tecnologia Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Parceira de tecnologia Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Após conectar sua conta de anúncios, você pode criar um Canvas com uma etapa de Audience Sync.

![Menu de componentes do Canvas para adicionar a etapa Audience Sync à jornada do usuário.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Em seguida, selecione o parceiro para sincronizar os públicos.

![Opção para selecionar o parceiro de sincronização de público na etapa Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Para cada parceiro, você precisará configurar o seguinte como parte da sua etapa de Audience Sync:

- Conta de anúncios
- Público
- Ação para adicionar ou remover usuários
- Campos para correspondência

Tenha em mente que a Braze sincroniza os usuários assim que eles entram na etapa de Audience Sync dentro do seu Canvas.

Para cada destino de Audience Sync, o parceiro pode ter requisitos diferentes em relação aos campos que a Braze pode enviar. Consulte a documentação específica do parceiro para mais detalhes.

### Audience Sync Pro

Para usar um parceiro Audience Sync Pro, incluindo TikTok, Pinterest, Snapchat ou Criteo, você pode selecionar seus parceiros com base nas alocações da sua compra de Audience Sync Pro na seção **Audience Sync Pro** da página **Technology Partners**.

![Audience Sync Pro sem parceiros selecionados ainda.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Primeiro, selecione os parceiros que você pretende usar. Cada compra de Audience Sync Pro oferece 3 destinos alocados de Audience Sync Pro, que estão disponíveis em cada um dos seus espaços de trabalho no dashboard.

![Opção para selecionar até três parceiros para conectar à Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Após selecionar seus destinos de Audience Sync Pro, conecte a conta de anúncios do parceiro selecionado clicando no bloco do parceiro.

![Exemplo de Snapchat e TikTok selecionados como parceiros para Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Configurações do Audience Sync para Snapchat com a mensagem: "Você conectou 1 conta do Snapchat com sucesso".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Por último, crie sua etapa de Audience Sync no Canvas usando esse destino de Audience Sync Pro.

### Lotes e latência {#batching-and-latency}

Quando os usuários entram em uma etapa de Audience Sync no Canvas, a Braze os coloca em um sistema de lotes que agrega as atualizações de usuários antes de enviá-las à API or interface de programação do aplicativo (API) do parceiro. Um lote é enviado quando uma das seguintes condições ocorre:

- **O lote atinge seu limite de tamanho.** Isso varia por parceiro:
  - O padrão suporta até 2.000 usuários
  - Google Ads suporta até 10.000 usuários
  - Facebook e TikTok suportam até 2.000 usuários
- **O temporizador de latência do lote expira.** O padrão é uma hora, mas isso é configurável por parceiro. Por exemplo, o The Trade Desk usa 10 minutos.

Canvas de alto volume podem despachar mais cedo porque os lotes são preenchidos mais rapidamente. Canvas de baixo volume aguardam até o temporizador de latência expirar. A Braze não garante um horário fixo de despacho; o tempo depende do tamanho do lote e da janela de latência configurada.

A Braze registra a atividade de despacho em logs internos para monitoramento e solução de problemas, mas esses timestamps não são expostos como campos consultáveis. Após a Braze despachar um lote para a API or interface de programação do aplicativo (API) do parceiro, o parceiro processa a atualização do público de acordo com seus próprios Acordos de Nível de Serviço — normalmente de 6 a 48 horas.

A Braze não recebe confirmação dos parceiros de que usuários individuais foram correspondidos ou sincronizados. As respostas dos parceiros são confirmações HTTP de recebimento, não confirmações de correspondência. Para verificar se um público foi preenchido, verifique a plataforma de anúncios do parceiro (como o Google Ads Audience Manager ou o Meta Business Manager).

### E-mails de erro do Audience Sync {#audience-sync-error-emails}

Se o erro estiver relacionado à integração geral do parceiro (como um problema de autorização), um e-mail é enviado ao usuário que conectou a integração. Se esse usuário não existir mais, os administradores recebem os e-mails.

Se o erro estiver relacionado a problemas com o componente de Audience Sync (como "Público não existe") no Canvas, um e-mail é enviado ao usuário que configurou o Canvas. Se esse usuário não existir mais, o e-mail é encaminhado ao administrador da empresa.

Para configurar quem recebe esses e-mails, entre em contato com seu gerente de sucesso do cliente para adicionar destinatários em **Notification Preferences**. Essa preferência cobre tanto erros de integração quanto erros do componente de Audience Sync. Os destinatários que você adicionar recebem esses e-mails além do usuário associado ao erro.

## Considerações sobre privacidade de dados {#data-privacy-considerations}

{% alert important %}
Esta documentação não se destina a fornecer, nem pode ser considerada como, aconselhamento jurídico. O uso do Audience Sync está sujeito a requisitos legais específicos. Para garantir que você está usando o recurso em conformidade com todas as leis aplicáveis, procure orientação do seu departamento jurídico.
{% endalert %}

Ao criar públicos para rastreamento de anúncios, você pode querer incluir ou excluir determinados usuários com base em suas preferências e em conformidade com leis de privacidade, como o direito de "Não vender ou compartilhar" previsto na [CCPA](https://oag.ca.gov/privacy/ccpa). Profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canvas. As opções a seguir podem ajudar.

Se você coletou o [IDFA do iOS por meio do SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations), poderá usar o filtro "Ads Tracking Enabled". Selecione o valor como `true` para enviar usuários apenas para destinos do Audience Sync nos quais eles aceitaram participar.

![Um Canvas com um público de entrada configurado com "Ad Tracking Enabled é true".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Se você está coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, inclua-os nos critérios de entrada do Canvas como filtro:

![Um Canvas com um público de entrada configurado com "opted_in_marketing igual a true".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Para saber mais sobre como estar em conformidade com essas leis de proteção de dados na plataforma da Braze, consulte [Assistência técnica para proteção de dados]({{site.baseurl}}/dp-technical-assistance).

## Gerenciamento de consentimento para direcionamento de anúncios {#managing-consent-for-ad-targeting}

Como anunciante, é sua responsabilidade gerenciar o consentimento para rastreamento ou direcionamento de anúncios dos seus usuários.

Para enviar anúncios aos seus usuários, você deve cumprir todas as leis e regulamentações aplicáveis, bem como as políticas e requisitos da plataforma de anúncios. Use a Braze apenas para direcionar e sincronizar usuários para os quais você obteve consentimento.

Para manter suas listas de público atualizadas nessas plataformas de anúncios e remover usuários que revogaram o consentimento, configure um Canvas para remover usuários dessas listas de público existentes usando uma etapa de Audience Sync.