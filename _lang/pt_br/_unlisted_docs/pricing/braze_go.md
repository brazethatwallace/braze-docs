---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> O Braze Go oferece acesso simplificado à plataforma de engajamento com clientes da Braze para ajudar suas equipes de marketing a começar de qualquer lugar e chegar a todos os lugares. Projetado para simplicidade e eficiência, o Braze Go é feito sob medida para mercados emergentes selecionados.

{% alert important %}
O Braze Go não está disponível em todos os mercados. Se você tiver interesse em saber mais sobre o Braze Go, entre em contato com seu gerente de conta.
{% endalert %}

O Braze Go oferece todas as mesmas funcionalidades da Braze, com as seguintes alterações específicas nos recursos:

- Você pode ter até 30 campanhas ativas.
- Você pode ter até 20 Canvas ativos.
- O limite de frequência padrão total da REST or transferir estado representacional API or interface de programação do aplicativo (API) é de 50.000 por hora, por espaço de trabalho.
    - Para uso fora do Braze Go, saiba mais sobre [limites da REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_limits#rate-limits-by-request-type).
- A retenção de dados de interação de campanhas e Canvas é de 2 meses, sem restauração.
    - Para uso fora do Braze Go, saiba mais sobre [disponibilidade de dados de interação de mensagens]({{site.baseurl}}/messaging_interaction_data).

{% alert note %}
Os dados de interação para campanhas e Canvas são diferentes dos dados do Snowflake e não têm nenhum efeito sobre eles.
{% endalert %}

- Webhooks da Braze para a Braze não são compatíveis.
- Filtros relacionados a tags não são compatíveis, especificamente os seguintes filtros:
    - Clicou ou abriu campanha ou Canvas com tag
    - Última mensagem recebida de campanha ou Canvas com tag
    - Recebeu campanha ou Canvas com tag
- A Braze também pode implementar uma política de retenção de dados para eventos de perfil de usuário e dados de compra que remove eventos, compras ou ambos com mais de 1 ano que não tenham sido realizados novamente em 1 ano. No entanto, esses dados ainda estariam disponíveis em extensões de Segment or segmento or segmento SQL por 2 anos.

Se alguma funcionalidade descrita neste artigo for atualizada, isso será refletido neste artigo e registrado em nossas [notas de versão]({{site.baseurl}}/help/release_notes#most-recent-braze-release-notes).