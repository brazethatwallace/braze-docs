---
nav_title: Personalizar landing pages
article_title: Personalizar landing pages
description: "Este artigo aborda como personalizar landing pages da Braze com o editor de arrastar e soltar."
page_order: 4
---

# Personalizar landing pages {#personalize-landing-pages}

> Use a personalização com Liquid em landing pages para adaptar dinamicamente o conteúdo com dados do perfil de usuário. Por exemplo, você pode personalizar títulos com base em diferentes atributos de usuário sem precisar gerenciar várias landing pages estáticas.

{% alert important %}
A personalização com Liquid para landing pages está disponível apenas no plano Pro de landing pages. Atualmente, [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [multi-idioma]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings) e [códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) não são compatíveis com a personalização Liquid em landing pages.
{% endalert %}

## Inserindo Liquid {#inserting-liquid}

No editor de arrastar e soltar, você pode inserir personalização com Liquid tanto no editor quanto nas configurações da página ou do bloco no painel à direita. Para instruções sobre como implementar Liquid, confira nossa [documentação dedicada sobre Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#using-liquid).

![Editor de landing page com personalização Liquid adicionada.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Pré-visualização e teste {#previewing-and-testing}

Ao pré-visualizar uma landing page no editor, você pode visualizar a página como um usuário aleatório, um usuário existente ou um usuário personalizado.

No entanto, ao pré-visualizar a landing page a partir da tabela de dados ou da página **Detalhes da landing page**, você só poderá visualizá-la como um usuário aleatório.

## Considerações sobre personalização {#personalization-considerations}

Para manter o desempenho ideal com landing pages personalizadas, observe os seguintes limites de tamanho:

- **Salvar uma landing page:** Se o tamanho exceder 500&nbsp;KB, você poderá receber uma mensagem de alerta indicando que a página excedeu nossos limites de tamanho, o que pode impedir sua publicação.
- **Renderização com personalização Liquid:** O tamanho total não deve exceder 1&nbsp;MB. Caso contrário, a página poderá ser automaticamente despublicada pela Braze.

### Evitar a despublicação de landing pages {#avoid-unpublishing-landing-pages}

Se sua página exceder esses limites de tamanho, você receberá um e-mail informando que ela poderá ser despublicada caso continue excedendo o limite. Quando o limite for atingido, a página será automaticamente despublicada e você receberá uma notificação.

Para evitar que sua página exceda os limites de tamanho ou tenha tempos de carregamento lentos, certifique-se de usar personalização Liquid que:

- Não faça loops contínuos nem referencie grandes conjuntos de dados.
- Não dependa de lógica matemática ou condicional extensa dentro do bloco Liquid.

Além disso, evite incorporar scripts grandes, folhas de estilo e ativos codificados em base64 diretamente no código da sua landing page. Esses ativos inline contam para o limite de tamanho da página e podem tornar a renderização mais lenta. Em vez disso, faça upload de fontes, imagens, folhas de estilo e scripts para a [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Os ativos servidos a partir da biblioteca de mídia são hospedados na CDN da Braze, portanto não são processados para renderização Liquid e não contam para o limite de tamanho da página.

### Usar Liquid para usuários identificados e anônimos {#use-liquid-for-identified-and-anonymous-users}

O Liquid pode personalizar a experiência da landing page tanto para visitantes identificados quanto anônimos.

- **Usuários identificados:** Vincule a landing page a partir de uma mensagem da Braze e inclua a [Liquid tag de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users#using-landing-page-liquid-tags). Isso associa o usuário ao seu perfil na Braze e personaliza a experiência da página.
- **Visitantes anônimos:** Use Liquid para conteúdo contextual não baseado em perfil, como um número aleatório ou uma saudação baseada no horário do dia.

### Pré-preencher campos de formulário {#pre-fill-form-fields}

Se um campo de formulário da landing page estiver mapeado para um atributo do perfil de usuário, você pode pré-preencher esse campo para usuários recorrentes. Isso ajuda a reduzir o atrito no formulário e melhora as taxas de conclusão para visitantes conhecidos.

Para usar campos de formulário pré-preenchidos:

1. Selecione o campo do formulário no editor de arrastar e soltar.
2. No painel de configurações à direita, mapeie o campo para o atributo de perfil apropriado.
3. Selecione **Pré-preencher a partir do perfil de usuário**.

![Configurações do campo de formulário da landing page mostrando a opção de pré-preencher a partir dos dados do perfil de usuário.]({% image_buster /assets/img/landing_pages/pre-fill-checkbox.png %}){: style="max-width:70%;"}

O pré-preenchimento funciona apenas para [usuários identificados](#use-liquid-for-identified-and-anonymous-users). Para visitantes anônimos, os campos do formulário mantêm seu estado padrão:

- **Campos de entrada:** Exibem o texto de placeholder.
- **Caixas de seleção, botões de opção e controles semelhantes:** Permanecem desmarcados até que o usuário interaja com eles.

{% alert warning %}
Se um usuário encaminhar um link de landing page (de um e-mail, SMS ou outra mensagem) para outra pessoa, o destinatário verá os dados pré-preenchidos destinados ao usuário original. Essa é a mesma consideração de segurança que se aplica a links de cancelamento de inscrição e links da Central de Preferências. Considere a sensibilidade dos dados que você está pré-preenchendo e o comportamento de compartilhamento do seu público ao usar esse recurso.
{% endalert %}

## Buscar dados externos com código personalizado {#fetching-external-data-with-custom-code}

Você pode usar um bloco de **Código personalizado** para buscar dados de endpoints externos e exibi-los na sua landing page. Essa abordagem faz a requisição no lado do cliente (no navegador do usuário), então a página carrega rapidamente sem atrasos de renderização no servidor.

{% alert warning %}
Ao buscar dados externos, você é responsável pela segurança da sua implementação. Identificadores externos usados em chamadas de API devem ser UUIDs ou usar um esquema de nomenclatura equivalentemente seguro. Consulte as [práticas recomendadas de nomenclatura de ID do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).
{% endalert %}

### Caso de uso {#use-case}

Esse padrão é útil quando você precisa exibir dados específicos do usuário que não estão armazenados na Braze. Exemplos incluem inventário em tempo real, recomendações personalizadas ou outros dados que sua organização gerencia em sistemas separados.

### Exemplo de implementação {#example-implementation}

Este exemplo mostra como buscar dados de usuário de uma API externa. Substitua o endpoint da API pelo seu próprio endpoint seguro e use um identificador seguro.

{% raw %}
```html
<script>
window.onload = () => {
  // Use Liquid to template the user's external ID
  const userId = "{{${user_id}}}";

  const loadUserData = async () => {
    try {
      // Replace with your own secure API endpoint
      const response = await fetch(`https://your-api.example.com/user/${userId}`);

      if (!response.ok) {
        throw new Error('Failed to load data');
      }

      const data = await response.json();

      // Update the page with the fetched data
      document.querySelector("#user-data").textContent = JSON.stringify(data, null, 2);
      document.querySelector("#user-name").textContent = data.name || "User";
    } catch (error) {
      // Handle errors gracefully
      document.querySelector("#user-data").textContent = "Unable to load data at this time.";
    }
  };

  loadUserData();
};
</script>

<!-- Display area for fetched data -->
<p>Welcome, <span id="user-name">Loading...</span></p>
<pre id="user-data">Loading your information...</pre>
```
{% endraw %}

### Considerações {#considerations}

Ao buscar dados externos em landing pages:

- **Estados de carregamento:** Os usuários verão um texto de placeholder até que o endpoint responda. Considere adicionar um indicador de carregamento ou uma tela esqueleto.
- **Tratamento de erros:** Se o endpoint falhar ou demorar para responder, a página pode parecer quebrada. Implemente mensagens de erro e fallbacks apropriados.
- **Desempenho:** A página carrega imediatamente, mas os dados aparecem após a conclusão da requisição externa. Mantenha as respostas da sua API rápidas para a melhor experiência do usuário.
- **Segurança:** Certifique-se de que seu endpoint de API valide o identificador e retorne apenas dados que o usuário está autorizado a ver. Implemente limite de frequência para evitar abusos. Para orientações sobre como escolher identificadores seguros, consulte as [práticas recomendadas de nomenclatura de ID do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).

## Páginas de fallback {#fallback-pages}

Se seus usuários tentarem acessar uma página que foi despublicada, eles verão uma mensagem indicando que a página não pode ser carregada no momento. Os motivos para uma página ter sido despublicada incluem:

- Liquid complexo ou com erros, que pode causar longos tempos de renderização
- Problemas de rede do usuário
- Exceder os limites máximos de tamanho da landing page