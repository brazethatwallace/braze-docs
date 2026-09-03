## 법적 고지 사항 {#legal-disclaimer}
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

### 지시 및 응답 처리 방식 {#how-instructions-and-responses-are-handled}

Braze MCP 서버는 Claude, ChatGPT, Copilot, Gemini CLI, Codex 또는 Cursor와 같은 서드파티 공급자 MCP 클라이언트로부터 해당 공급자의 기본 AI 모델이 생성한 그대로의 지시를 수신합니다. 사용자가 자연어로 요청을 입력하면, AI 모델이 해당 요청을 해석하여 Braze에 대한 하나 이상의 특정 도구 호출로 변환합니다. Braze는 전송된 도구 호출을 그대로 수신하고 실행합니다. Braze는 사용자의 원래 자연어 프롬프트를 확인할 수 없으며, 생성된 도구 호출이 사용자의 의도한 요청을 완전하고 정확하게 반영하는지 검증할 수 없습니다.

Braze가 데이터 또는 결과를 반환하면, 해당 응답은 서드파티 공급자 MCP 클라이언트로 다시 전송되며, 클라이언트가 이를 해석하고 형식을 지정하여 사용자에게 표시합니다. Braze는 AI 모델이 반환된 정보를 표시, 요약 또는 설명하는 방식을 제어하지 않습니다.

Braze는 서드파티 공급자 MCP 클라이언트에 의해 생성된 지시 또는 전달된 응답에 대해 책임을 지지 않습니다. 서드파티 공급자 MCP 클라이언트가 자동 작업 구현을 위한 "자동 모드"를 제공하는 경우, 이를 사용하지 않는 것을 권장합니다. AI가 생성한 요약은 Braze 대시보드의 원본 데이터와 대조하여 검토하고, AI가 제안한 모든 작업은 서드파티 공급자 MCP 클라이언트를 통해 구현하기 전에 반드시 검토해 주세요.