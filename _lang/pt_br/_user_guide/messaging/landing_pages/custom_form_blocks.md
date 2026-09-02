---
nav_title: Criar blocos de formulário personalizados
article_title: Criar blocos de formulário personalizados em landing pages
page_order: 6
page_type: reference
description: "Saiba como criar entradas de formulário interativas personalizadas em landing pages da Braze para que seus valores sejam validados e enviados junto com os blocos de formulário padrão."
---

# Criar blocos de formulário personalizados em landing pages {#create-custom-form-blocks-on-landing-pages}

> Os [blocos de formulário]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) de landing pages da Braze capturam entradas padrão, como campos de texto, caixas de seleção e menus suspensos. Os blocos de formulário personalizados ampliam as possibilidades, permitindo que você crie seus próprios elementos interativos, como uma avaliação por estrelas, um seletor de sentimento com emojis ou um cartão de raspadinha.

Quando um visitante envia o formulário personalizado, o valor selecionado é validado e salvo junto com os campos padrão, e então enviado à Braze como um atributo personalizado de usuário. Isso permite coletar dados mais ricos e envolventes sem sair do editor de landing pages.

Você cria blocos de formulário personalizados com um único auxiliar JavaScript, `window.brazeHelpers.forms.registerFormInput`, que é chamado a partir de um bloco de **Custom Code** na landing page.

{% alert note %}
Pesquisas e mensagens no app têm seus próprios blocos de formulário, mas `registerFormInput` — a API JavaScript para conectar uma interface personalizada a um bloco de formulário — está disponível apenas em landing pages.
{% endalert %}

## Como funciona {#how-it-works}

Uma entrada de formulário personalizada é qualquer elemento na sua landing page cujo valor você deseja capturar e enviar com o formulário. Você conecta esse elemento ao sistema de formulários da Braze registrando-o. O registro informa à Braze qual elemento monitorar, como ler seu valor atual e o que fazer com esse valor quando o formulário for enviado.

1. Crie sua interface personalizada dentro de um bloco de **Custom Code** na landing page e atribua a ela um seletor CSS estável, como um `id`.
2. Registre o elemento chamando `window.brazeHelpers.forms.registerFormInput` com um objeto de configuração.
3. A Braze chama sua função `getValue` para ler o valor atual quando necessário.
4. Se o campo for obrigatório, ou se você fornecer uma função `onValidate`, a Braze bloqueia o envio até que o valor seja aprovado e marca o elemento inválido com uma classe CSS que você pode estilizar. Consulte [Validação e campos obrigatórios](#validation-and-required-fields).
5. Quando o formulário é enviado e a validação é aprovada, a Braze chama sua função `onSubmit`, onde você pode usar o SDK da Braze para registrar informações como um atributo personalizado de usuário.

Como você fornece as funções que leem, validam e enviam o valor, essa abordagem funciona com praticamente qualquer elemento de formulário personalizado, sem se limitar aos tipos de campo padrão do editor.

## Estrutura básica {#basic-framework}

O registro mais simples direciona um elemento, trata-o como obrigatório, lê seu valor a partir de um atributo de dados e grava esse valor em um atributo personalizado de usuário quando o formulário é enviado. Envolva a chamada em um listener `DOMContentLoaded`, como nos exemplos desta página, para que o elemento exista antes de `registerFormInput` ser executado:

```js
document.addEventListener("DOMContentLoaded", () => {
  window.brazeHelpers.forms.registerFormInput({
    selector: "#my-custom-input",
    isRequired: true,
    getValue: (element) => element.dataset.value ?? null,
    onSubmit: (value) => {
      window.brazeBridge.getUser().setCustomUserAttribute("my_attribute", value);
    },
  });
});
```

Chame `registerFormInput` uma vez para cada entrada personalizada na página. Os campos de formulário padrão inseridos pelo editor de landing pages não precisam ser registrados; o registro é necessário apenas para as entradas personalizadas que você cria em um bloco de **Custom Code**.

## Referência de configuração {#configuration-reference}

`registerFormInput` aceita um único objeto de configuração. Expressa como assinatura de função, a estrutura completa é:

```js
window.brazeHelpers.forms.registerFormInput({
  // Provide exactly one of `selector` or `element` to identify the input.
  selector?: string,
  element?: HTMLElement,
  isRequired?: boolean | Promise<boolean>,
  getValue: (element: HTMLElement) => value,
  onValidate?: (value, element: HTMLElement) => boolean | Promise<boolean>,
  onSubmit?: (value, element: HTMLElement) => void | Promise<void>,
});
```

No mínimo, você deve fornecer uma forma de localizar o elemento (`selector` ou `element`) e uma função `getValue`. Todo o restante é opcional.

| Propriedade | Tipo | Obrigatória | Descrição |
| --- | --- | --- | --- |
| `selector` | `string` | Sim (ou `element`) | Um seletor CSS que corresponde ao seu elemento personalizado, por exemplo `"#scratch-card"`. A Braze o resolve de forma lazy com `querySelector` no momento da validação e do envio, então ele pode corresponder a um elemento adicionado ao DOM após a execução de `registerFormInput`. |
| `element` | `HTMLElement` | Sim (ou `selector`) | Uma referência direta ao elemento, usada no lugar de `selector`. É utilizada apenas enquanto o elemento permanece anexado à página, e tem precedência sobre `selector` quando ambos são fornecidos. |
| `isRequired` | `boolean \| Promise<boolean>` | Não | Quando `true`, o formulário não pode ser enviado até que a entrada tenha um valor não vazio — `null`, `undefined`, strings vazias (incluindo strings apenas com espaços em branco) e arrays vazios são considerados vazios. Também pode ser uma promise que resolve para um booleano, que a Braze reavalia cada vez que a entrada é validada, permitindo que você defina o estado de obrigatoriedade em tempo de execução. O padrão é `false`. Consulte [Validação e campos obrigatórios](#validation-and-required-fields) para a ordem completa de validação. |
| `getValue` | `function` | Sim | Retorna o valor atual da entrada. A Braze passa o elemento correspondente como argumento, para que você possa ler o valor do DOM, por exemplo `element.dataset.sentiment`, ou de uma variável no seu próprio código. Retorne `null` quando ainda não houver valor. |
| `onValidate` | `function` | Não | Recebe o valor atual e o elemento correspondente, e deve retornar `boolean \| Promise<boolean>` — o mesmo tipo de retorno que `isRequired` — onde `true` significa que o valor é válido e `false` significa que não é. Use para aplicar regras além de simplesmente ter um valor, por exemplo, que o valor pertença a um conjunto permitido. Se omitido, apenas `isRequired` e a validação nativa de restrições são aplicadas. |
| `onSubmit` | `function` | Não | Executada quando o formulário é enviado e a validação é aprovada. Recebe o valor atual e o elemento correspondente. É aqui que você registra o valor na Braze, normalmente com `setCustomUserAttribute`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Referência de configuração" }

### Agir sobre o valor em onSubmit {#act-on-the-value-in-onsubmit}

`onSubmit` é um callback JavaScript simples, então você pode agir sobre o valor capturado da forma que sua integração precisar. Como `onSubmit` é executado como parte do envio do formulário, as chamadas `brazeBridge` feitas dentro dele funcionam como esperado, mesmo para um visitante que abriu a landing page anonimamente. Consulte [Disponibilidade do bridge]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#bridge-availability) para a outra situação em que as chamadas do bridge funcionam.

O padrão mais comum é gravar o valor capturado no perfil do usuário com o [bridge JavaScript da Braze]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) disponível em landing pages:

```js
window.brazeBridge.getUser().setCustomUserAttribute("attribute_name", value);
```

Use um nome de atributo personalizado que já exista, ou um que você queira criar, no seu espaço de trabalho. O valor que você passa é armazenado no perfil do usuário e pode então ser usado para segmentação, personalização e disparo de mensagens de acompanhamento.

Você não está limitado a atributos personalizados. A partir do mesmo callback, você pode chamar qualquer [método `brazeBridge.getUser()`]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#supported-methods). Por exemplo, para adicionar o usuário a um grupo de inscrições, definir um atributo padrão, registrar um evento personalizado ou enviar o valor para o endpoint da sua própria API.

{% alert note %}
Você não precisa chamar `requestImmediateDataFlush` dentro de `onSubmit`. O processo de envio do formulário automaticamente envia todos os dados para a Braze após a conclusão do seu callback `onSubmit`.
{% endalert %}

## Exemplos {#examples}

Os exemplos a seguir são completos e independentes. Cada um é um bloco único contendo marcação, uma tag `<script>` e uma tag `<style>` que você cola em um bloco de **Custom Code** (HTML) na sua landing page. A chamada `registerFormInput` próxima ao final de cada script conecta a entrada personalizada ao formulário da Braze. Passe o mouse sobre um exemplo de código e selecione o ícone de cópia para copiá-lo.

{% alert important %}
Esses exemplos são executados inteiramente no navegador do visitante. No exemplo da raspadinha, o "prêmio" é escolhido por JavaScript no navegador do visitante, então um visitante tecnicamente habilidoso poderia modificar esse código para obter o resultado que quiser. Não confie nesse padrão para recompensas, descontos ou outros resultados que exijam aplicação rigorosa por visitante. Valide qualquer coisa sensível à segurança ou à receita nos seus próprios servidores.
{% endalert %}

<div class="scrollable-code-examples" markdown="1">

{% tabs local %}
{% tab Seletor de sentimento %}

**Objetivo:** O visitante seleciona um rosto feliz ou triste, e a escolha é gravada em um atributo personalizado de string chamado `feedback_sentiment`.

Cole o seguinte em um único bloco de **Custom Code** (HTML):

```html
<div id="sentiment-picker" class="sentiment-picker">
  <button type="button" data-sentiment="positive" aria-label="Happy">🙂</button>
  <button type="button" data-sentiment="negative" aria-label="Unhappy">🙁</button>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const picker = document.getElementById("sentiment-picker");

    picker.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => {
        picker.dataset.sentiment = button.dataset.sentiment;
        picker.querySelectorAll("button").forEach((b) => b.classList.remove("selected"));
        button.classList.add("selected");
      });
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#sentiment-picker",
      isRequired: true,
      getValue: (element) => element.dataset.sentiment ?? null,
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("feedback_sentiment", value);
      },
    });
  });
</script>

<style>
  .sentiment-picker {
    display: flex;
    gap: 16px;
    justify-content: center;
    font-size: 40px;
  }

  .sentiment-picker button {
    background: none;
    border: 2px solid transparent;
    border-radius: 12px;
    cursor: pointer;
    line-height: 1;
    padding: 8px;
  }

  .sentiment-picker button.selected {
    border-color: #1f2933;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .sentiment-picker.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**Como funciona:** Selecionar um botão armazena seu valor `data-sentiment` no elemento contêiner. `getValue` lê esse valor de volta do elemento contêiner que a Braze passa. Como `isRequired` é `true`, o formulário não é enviado até que o visitante escolha um rosto, e o contêiner é marcado com a classe `bz-validation-error` enquanto estiver vazio. No envio, o valor escolhido (`"positive"` ou `"negative"`) é gravado em `feedback_sentiment`.

{% endtab %}
{% tab Raspadinha %}

**Objetivo:** O visitante raspa um cartão para revelar um dos três descontos (10% Off, 20% Off ou 25% Off), e o desconto é gravado em um atributo personalizado de string chamado `scratch_off_reward`.

Este exemplo desenha um cartão de raspadinha em um Canvas HTML. Uma recompensa é escolhida aleatoriamente quando a página carrega e fica escondida sob uma camada opaca que o visitante raspa. Você pode substituir a abordagem com Canvas por qualquer widget de raspadinha que preferir; apenas a chamada `registerFormInput` o conecta à Braze. Cole o seguinte em um único bloco de **Custom Code** (HTML):

```html
<div id="scratch-card" class="scratch-card" data-reward="">
  <span class="scratch-card__reward"></span>
  <canvas class="scratch-card__surface" width="300" height="150"></canvas>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const rewards = ["10% Off", "20% Off", "25% Off"];

    const card = document.getElementById("scratch-card");
    const label = card.querySelector(".scratch-card__reward");
    const canvas = card.querySelector(".scratch-card__surface");
    const ctx = canvas.getContext("2d");

    // Randomly assign which reward this visitor will reveal.
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    label.textContent = reward;

    // Paint the opaque scratch layer over the reward.
    ctx.fillStyle = "#b3b3b3";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = "destination-out";

    let isScratching = false;

    function scratchAt(event) {
      const rect = canvas.getBoundingClientRect();
      ctx.beginPath();
      ctx.arc(event.clientX - rect.left, event.clientY - rect.top, 18, 0, Math.PI * 2);
      ctx.fill();
    }

    canvas.addEventListener("pointerdown", () => { isScratching = true; });
    canvas.addEventListener("pointermove", (event) => {
      if (isScratching) scratchAt(event);
    });
    canvas.addEventListener("pointerup", () => {
      isScratching = false;
      // The visitor has scratched the card, so record the revealed reward.
      card.dataset.reward = reward;
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#scratch-card",
      isRequired: true,
      getValue: (element) => element.dataset.reward || null,
      onValidate: (value) => rewards.includes(value),
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("scratch_off_reward", value);
      },
    });
  });
</script>

<style>
  .scratch-card {
    position: relative;
    width: 300px;
    height: 150px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }

  /* The reward sits underneath and is revealed as the canvas is scratched away. */
  .scratch-card__reward {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    color: #1f2933;
  }

  .scratch-card__surface {
    position: absolute;
    inset: 0;
    border-radius: 12px;
    cursor: pointer;
    touch-action: none;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .scratch-card.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**Como funciona:** Quando a página carrega, o script escolhe aleatoriamente uma das três recompensas e pinta uma camada opaca sobre ela no Canvas. Conforme o visitante arrasta pelo Canvas, o modo de composição `"destination-out"` apaga essa camada e revela a recompensa por baixo. No `pointerup`, a recompensa revelada é gravada no atributo `data-reward` do cartão. `getValue` lê o valor de lá, `onValidate` confirma que é uma das três recompensas definidas, e `isRequired` impede o envio até que o cartão tenha sido raspado. No envio, o desconto revelado (por exemplo, `"20% Off"`) é gravado em `scratch_off_reward`.

{% endtab %}
{% tab Atribuição de Campaign %}

**Objetivo:** Capturar a Campaign que direcionou o visitante à landing page e registrá-la como uma propriedade de evento personalizado para relatórios e atribuição downstream.

Este exemplo demonstra como atribuir o envio de um formulário de landing page a uma Campaign específica. Ao adicionar uma variável Liquid como {% raw %}`{{campaign.${api_id}}}`{% endraw %} à URL da sua landing page em mensagens de e-mail, SMS ou WhatsApp, você pode passar o identificador da Campaign para a landing page. O bloco de formulário personalizado então lê esse parâmetro da URL e o registra como um evento personalizado com o API ID da Campaign como propriedade do evento, facilitando o rastreamento de quais Campaigns estão gerando envios de formulário.

Cole o seguinte em um único bloco de **Custom Code** (HTML):

```html
<input type="hidden" id="campaign-attribution" value="" />

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const hiddenInput = document.getElementById("campaign-attribution");
    const campaignApiId = new URLSearchParams(window.location.search).get("campaign_api_id");

    if (campaignApiId) {
      hiddenInput.value = campaignApiId;
    }

    window.brazeHelpers.forms.registerFormInput({
      selector: "#campaign-attribution",
      isRequired: false,
      getValue: (element) => element.value || null,
      onSubmit: async (value) => {
        if (!value) {
          return;
        }

        await window.brazeBridge.logCustomEvent("landing_page_form_submitted", {
          campaign_api_id: value,
        });
      },
    });
  });
</script>
```

**Como funciona:** Quando você cria uma mensagem de e-mail, SMS ou WhatsApp com link para sua landing page, adicione o identificador da Campaign à URL usando templates Liquid: {% raw %}`https://your-landing-page.com?campaign_api_id={{campaign.${api_id}}}`{% endraw %}. Quando um visitante chega à landing page a partir dessa mensagem, o script lê o parâmetro `campaign_api_id` da URL e o armazena em um campo de entrada oculto. No envio do formulário, se um ID de Campaign estiver presente, o callback `onSubmit` registra um evento personalizado chamado `landing_page_form_submitted` com o API ID da Campaign como propriedade do evento. Esse evento aparece no Currents e pode ser usado para relatórios, segmentação e análise de atribuição.

{% alert tip %}
Você pode estender esse padrão para capturar parâmetros de URL adicionais, como variação de mensagem, etapa do Canvas ou qualquer outra variável Liquid que você queira passar para a landing page para fins de atribuição.
{% endalert %}

{% endtab %}
{% endtabs %}

</div>

## Validação e campos obrigatórios {#validation-and-required-fields}

Uma entrada deve passar por todas as camadas a seguir que se aplicam a ela antes que o formulário possa ser enviado:

1. **`isRequired`** condiciona o envio à presença de um valor não vazio. Retorne `null` de `getValue` quando a entrada ainda não tiver valor, para que a Braze possa identificar que está vazia. Strings vazias (incluindo strings apenas com espaços em branco) e arrays vazios também são tratados como vazios, enquanto `0` e `false` contam como valores presentes. `isRequired` pode ser um booleano ou uma promise que resolve para um, e é reavaliado cada vez que a entrada é validada.
2. **Validação nativa de restrições.** Se o elemento correspondente suportar a API padrão HTML `checkValidity()`, por exemplo um `<input>` nativo com `required`, `pattern`, `min` ou `max`, a Braze a executa e bloqueia o envio quando falha. Para elementos totalmente personalizados e não nativos (um `div`, um `canvas`, etc.), essa verificação sempre passa, então nunca interfere na sua própria lógica.
3. **`onValidate`** condiciona o envio às suas próprias regras. Recebe o valor atual e o elemento correspondente, e deve retornar `boolean \| Promise<boolean>` — o mesmo tipo de retorno que `isRequired` — onde `true` significa que o valor é válido e `false` significa que não é. Use para verificações de valores permitidos, verificações de formato, intervalos ou qualquer lógica que você possa expressar em JavaScript.

### Estilização de erros {#error-styling}

Sempre que uma entrada falha na validação, a Braze adiciona a classe CSS `bz-validation-error` ao elemento correspondente ao seu `selector` ou `element`, e remove a classe quando a entrada se torna válida novamente. Estilize o estado inválido como preferir, por exemplo com um contorno ou borda que chame atenção para a entrada com problema, adicionando uma regra que direcione seu elemento combinado com a classe `bz-validation-error`:

```css
#my-custom-input.bz-validation-error {
  outline: 3px solid #f94144;
  outline-offset: 4px;
}
```

Estilizar o estado de erro é opcional, mas recomendado, para que os visitantes possam ver qual entrada personalizada está bloqueando o envio. Cada [exemplo](#examples) nesta página inclui uma regra `bz-validation-error`.

## Práticas recomendadas {#best-practices}

- Use um seletor estável e único. Um `id` é a escolha mais segura. Evite seletores que possam corresponder a mais de um elemento.
- Retorne `null`, não uma string vazia ou `undefined`, quando não houver valor, para que as verificações de obrigatoriedade se comportem de forma previsível. Strings vazias e arrays vazios também são tratados como vazios, mas `null` é o sinal mais claro de "sem valor".
- Mantenha `getValue` leve e síncrono. A Braze pode chamá-lo mais de uma vez, então ele deve ler e retornar o valor atual em vez de realizar trabalho pesado.
- Estilize o estado `bz-validation-error` para que os visitantes possam ver qual entrada personalizada está bloqueando o envio.
- Defina os nomes dos seus atributos personalizados com antecedência e mantenha-os consistentes para que você possa segmentar os dados de forma confiável posteriormente.
- Teste o envio completo. Confirme que o atributo aparece no perfil do usuário após o envio e que as regras de obrigatoriedade e validação bloqueiam o envio conforme esperado.

## Solução de problemas {#troubleshooting}

### O formulário é enviado mesmo sem nada selecionado {#the-form-submits-even-though-nothing-was-selected}
Certifique-se de que `isRequired` está definido como `true`. A Braze trata `null`, `undefined`, strings vazias (incluindo strings apenas com espaços em branco) e arrays vazios como ausência de valor — se `getValue` estiver retornando algo diferente (por exemplo, um valor padrão não vazio ou um placeholder) quando nada foi selecionado, a verificação de obrigatoriedade não vai detectar.

### O valor não aparece no perfil {#the-value-doesnt-appear-on-the-profile}
Confirme que `onSubmit` chama `window.brazeBridge.getUser().setCustomUserAttribute` com o nome correto do atributo, e que o bloco de **Custom Code** está na mesma landing page que o formulário.

### O registro parece não fazer nada {#registration-seems-to-do-nothing}
Verifique se o seletor corresponde a um elemento que existe no DOM quando `registerFormInput` é executado, e se o script é executado após esse elemento ser renderizado. Em seguida, abra o console de desenvolvedor do seu navegador: `registerFormInput` valida sua configuração e, quando algo está errado (por exemplo, um `getValue` ausente, um seletor que não é um seletor CSS válido ou uma propriedade do tipo errado), ignora o registro e exibe um aviso prefixado com `[brazeHelpers.forms.registerFormInput]` descrevendo o que estava inválido.

## Conteúdo relacionado {#related-content}

- [Bridge JavaScript para landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) cobre a referência completa do `brazeBridge` usado em `onSubmit`.
- [Criar landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)