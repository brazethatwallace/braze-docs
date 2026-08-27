---
nav_title: Diretrizes da marca
article_title: Diretrizes da marca
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como criar, gerenciar e usar diretrizes da marca que o Operator aplica ao gerar textos, modelos e imagens."
---

# Diretrizes da marca {#brand-guidelines}

> Adapte o estilo do seu texto gerado por IA para que corresponda à voz, ao tom e à personalidade da sua marca com diretrizes personalizadas da marca.

Crie e gerencie as diretrizes da marca acessando **Conteúdo** > **Diretrizes da marca**.

## Criando diretrizes da marca {#creating-brand-guidelines}

### Etapa 1: Criar uma diretriz da marca {#step-1-create-a-brand-guideline}

Na página **Brand Guidelines**, selecione **Create new**. Se quiser que essa diretriz da marca seja a padrão para o espaço de trabalho, selecione **Use as default brand guideline**. Você pode ter uma diretriz padrão por espaço de trabalho.

### Etapa 2: Descrever a personalidade da sua marca {#step-2-describe-your-brand-personality}

Em **Brand personality**, pense no que torna sua marca única. Inclua traços, valores, voz e quaisquer arquétipos que definam sua marca. Mantenha esse campo com 10.000 caracteres ou menos. Se você gerar esse texto com um LLM, inclua esse limite de caracteres no seu prompt para que a saída caiba no campo.

Aqui estão algumas características a serem consideradas:

| Característica           | Definição                                                                            | Exemplo                                                            |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputação                | Como você quer que sua marca seja percebida no mercado.                              | Somos conhecidos por ser a marca mais confiável e focada no cliente do nosso setor. |
| Traços de personalidade  | Características humanas que descrevem o caráter da sua marca.                        | Nossa marca é amigável, acessível e sempre animada.                |
| Valores                  | Valores essenciais que orientam as ações e decisões da sua marca.                    | Valorizamos sustentabilidade, transparência e comunidade.          |
| Diferenciação            | Qualidades únicas que diferenciam sua marca dos concorrentes.                        | Nos destacamos por oferecer um atendimento ao cliente personalizado que vai além. |
| Voz da marca             | O tom e o estilo de comunicação que sua marca utiliza.                                | Nossa voz é casual, mas informativa, garantindo clareza sem ser formal demais. |
| Arquétipo da marca       | O arquétipo que representa a persona da sua marca (O Herói, O Criador e assim por diante). | Incorporamos o arquétipo do "Explorador", sempre buscando novos desafios e aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 2: Descrever a personalidade da sua marca" }

### Etapa 3: Definir linguagem que deve ser evitada (opcional) {#step-3-define-language-that-should-be-avoided-optional}

Em **Exclusions**, liste qualquer linguagem ou estilo que não esteja alinhado com sua marca. Por exemplo, você pode querer evitar "sarcasmo", "atitudes negativas" ou tons "condescendentes". Mantenha esse campo com 300 caracteres ou menos.

![A janela "Create brand guideline" com campos para inserir o nome, a descrição, a personalidade, as exclusões e o tom.]({% image_buster /assets/img/guidelines_create.png %})

### Etapa 4: Testar suas diretrizes {#step-4-test-your-guidelines}

Teste suas diretrizes para ver como elas funcionam. Expanda **Test your guidelines** para gerar exemplos de texto e ajuste conforme necessário.

### Etapa 5: Salvar suas diretrizes {#step-5-save-your-guidelines}

Quando estiver satisfeito com suas diretrizes, selecione **Save brand guideline**. Suas diretrizes são salvas no seu espaço de trabalho para uso futuro.

{% alert important %}
Você pode alterar o idioma de saída independentemente do idioma do seu texto, mas nem a Braze nem a OpenAI garantem a qualidade da tradução. Sempre teste e verifique as traduções antes de usá-las.
{% endalert %}

## Gerenciando diretrizes da marca {#managing-brand-guidelines}

Você pode editar diretrizes da marca selecionando-as na página **Brand Guidelines**. Arquive uma diretriz da marca para torná-la inativa e indisponível nos criadores de mensagem. Para torná-la ativa e selecionável novamente, você pode filtrar por diretrizes da marca arquivadas e então desarquivá-la.

## Usando diretrizes da marca {#using-brand-guidelines}

Ao compor uma mensagem, abra o Operator para [gerar textos]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) e selecione sua diretriz da marca no menu suspenso **Apply brand guideline**. Se você designar uma diretriz da marca específica como padrão, a Braze a seleciona automaticamente no menu suspenso, mas você pode escolher uma diretriz diferente.

![Operator com "Important Alerts!!" selecionado como a diretriz da marca.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}