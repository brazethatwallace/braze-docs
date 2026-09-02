---
nav_title: Acessibilidade
article_title: Acessibilidade
platform: Web
page_order: 22
page_type: reference
description: "Este artigo descreve como a Braze suporta acessibilidade."

---

# Acessibilidade {#accessibility}

> Este artigo fornece uma visão geral de como a Braze suporta acessibilidade na sua integração.

O SDK or kit de desenvolvimento de software Web da Braze suporta os padrões fornecidos pelas [Diretrizes de Acessibilidade para Conteúdo da Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Mantemos uma [pontuação de 100/100 no Lighthouse](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) para Content Cards e mensagens no app em todas as nossas novas versões para manter nosso padrão de acessibilidade.

## Pré-requisitos {#prerequisites}

A versão mínima do SDK or kit de desenvolvimento de software que atende à WCAG 2.1 é próxima da v3.4.0. No entanto, recomendamos a atualização para pelo menos a v6.0.0 para correções importantes de tags de imagem.

### Correções notáveis de acessibilidade {#notable-accessibility-fixes}

| Versão | Tipo | Principais mudanças |
|---------|------|-------------|
| **6.0.0** | **Major** | Imagens como tags `<img>`, campos `imageAltText` ou `language`, melhorias gerais de acessibilidade da interface |
| **3.5.0** | Minor | Melhorias de acessibilidade de texto rolável |
| **3.4.0** | Fix | Correção do papel `article` para Content Cards |
| **3.2.0** | Minor | Alvos de toque mínimos de 45x45px para botões |
| **3.1.2** | Minor | Texto alternativo padrão para imagens |
| **2.4.1** | **Major** | HTML semântico (`h1` ou `button`), atributos ARIA, navegação por teclado, gerenciamento de foco |
| **2.0.5** | Minor | Gerenciamento de foco, navegação por teclado, rótulos |
{: .reset-td-br-1, .reset-td-br-2 aria-label="Correções notáveis de acessibilidade" }

## Recursos de acessibilidade suportados {#supported-accessibility-features}

Suportamos esses recursos para Content Cards e mensagens no app:

- Funções e rótulos ARIA
- Suporte à navegação por teclado
- Gerenciamento de foco
- Anúncios para leitores de tela
- Suporte a texto alternativo para imagens

## Diretrizes de acessibilidade para integrações de SDK or kit de desenvolvimento de software {#accessibility-guidelines-for-sdk-integrations}

Consulte [Crie mensagens acessíveis na Braze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) para diretrizes gerais de acessibilidade. Este guia fornece dicas e boas práticas para máxima acessibilidade ao integrar o SDK or kit de desenvolvimento de software Web da Braze em sua aplicação web.

### Content Cards

#### Definindo uma altura máxima {#setting-a-maximum-height}

Para evitar que os Content Cards ocupem muito espaço vertical e melhorar a acessibilidade, você pode definir uma altura máxima no contêiner do feed, como neste exemplo:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Considerações sobre a viewport {#viewport-considerations}

Para Content Cards exibidos em linha, considere as restrições da viewport, como neste exemplo.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### Mensagens no app {#in-app-messages}

{% alert warning %}
Não coloque informações importantes em mensagens no app do tipo slide up, pois elas não são acessíveis para leitores de tela.
{% endalert %}

### Considerações para dispositivos móveis {#mobile-considerations}

#### Design responsivo {#responsive-design}

O SDK or kit de desenvolvimento de software inclui pontos de interrupção responsivos. Confirme que suas personalizações funcionam em diferentes tamanhos de tela, como neste exemplo:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }

  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Testando acessibilidade {#testing-accessibility}

#### Lista de verificação de teste manual {#manual-test-checklist}

Teste manualmente a acessibilidade completando estas tarefas:

- Navegue pelos Content Cards e mensagens no app apenas com o teclado (Tab, Enter, Espaço)
- Teste com leitor de tela (NVDA, JAWS, VoiceOver)
- Verifique se todas as imagens têm texto alternativo
- Verifique as proporções de contraste de cores (use ferramentas como o WebAIM Contrast Checker)
- Teste em dispositivos móveis com toque
- Verifique se os indicadores de foco estão visíveis
- Teste a captura de foco de mensagens modais
- Verifique se todos os elementos interativos são acessíveis pelo teclado

### Problemas comuns de acessibilidade {#common-accessibility-issues}

Para evitar problemas comuns de acessibilidade, faça o seguinte:

1. **Mantenha os estilos de foco:** Os indicadores de foco do SDK or kit de desenvolvimento de software são essenciais para usuários de teclado.
2. **Use `display: none` apenas em elementos não interativos:** Use `visibility: hidden` ou `opacity: 0` para ocultar elementos interativos.
3. **Não substitua atributos ARIA:** O SDK or kit de desenvolvimento de software define funções e rótulos ARIA apropriados.
4. **Use atributos `tabindex`:** Eles controlam a ordem de navegação pelo teclado.
5. **Forneça rolagem se você definir `overflow: hidden`:** Confirme que o conteúdo rolável permanece acessível.
6. **Não interfira nos manipuladores de teclado integrados:** Confirme que a navegação existente pelo teclado funciona.