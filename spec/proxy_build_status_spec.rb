# frozen_string_literal: true

RSpec.describe 'dev_build_status_enabled gating' do
  def enabled?(rack_env:, sse_flag: '1')
    return false if rack_env == 'production'
    return false if sse_flag == '0'

    true
  end

  it 'is enabled in development by default' do
    expect(enabled?(rack_env: 'development')).to be(true)
  end

  it 'is disabled in production' do
    expect(enabled?(rack_env: 'production')).to be(false)
  end

  it 'is disabled when BRAZE_DOCS_BUILD_STATUS_SSE=0' do
    expect(enabled?(rack_env: 'development', sse_flag: '0')).to be(false)
  end
end
