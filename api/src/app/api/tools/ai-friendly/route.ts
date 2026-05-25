import { NextRequest, NextResponse } from 'next/server';
import { TOOLS_DATA } from '@/lib/tools-data';
import { Tool, AIFriendlyTool } from '@/lib/tools-registry';

function convertToAIFriendly(tool: Tool): AIFriendlyTool {
  return {
    id: tool.id,
    name: tool.name,
    description: tool.descriptionForAI,
    usage_example: tool.metadata.examples[0] || `使用 ${tool.name} 完成任务`,
    capabilities: tool.capabilities,
    registration_required: tool.auth.type !== 'none',
    free_tier: tool.pricing.hasFreeTier,
    openclaw_config: tool.openclaw.configTemplate || {}
  };
}

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  
  const q = searchParams.get('q')?.toLowerCase() || '';
  const category = searchParams.get('category')?.toLowerCase();
  const freeOnly = searchParams.get('free') === 'true';
  const maxResults = parseInt(searchParams.get('limit') || '10');

  let filteredTools = [...TOOLS_DATA];

  // 搜索过滤
  if (q) {
    filteredTools = filteredTools.filter(tool =>
      tool.name.toLowerCase().includes(q) ||
      tool.descriptionForAI.toLowerCase().includes(q) ||
      tool.metadata.tags.some(tag => tag.toLowerCase().includes(q)) ||
      tool.capabilities.some(cap => cap.toLowerCase().includes(q))
    );
  }

  // 分类过滤
  if (category) {
    filteredTools = filteredTools.filter(tool => 
      tool.category.toLowerCase().includes(category)
    );
  }

  // 免费过滤
  if (freeOnly) {
    filteredTools = filteredTools.filter(tool => tool.pricing.hasFreeTier);
  }

  // 排序
  filteredTools.sort((a, b) => (b.stats?.popularity || 0) - (a.stats?.popularity || 0));

  // 限制结果
  const limitedTools = filteredTools.slice(0, maxResults);

  const aiFriendlyTools = limitedTools.map(convertToAIFriendly);

  return NextResponse.json({
    tools: aiFriendlyTools,
    count: aiFriendlyTools.length,
    purpose: '提供给AI Agent使用的Python工具列表，可直接用于工具调用和配置',
    format_version: '1.0'
  }, {
    headers: {
      'Cache-Control': 'public, max-age=3600',
      'Content-Type': 'application/json'
    }
  });
}
