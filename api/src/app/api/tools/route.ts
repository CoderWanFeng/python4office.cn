import { NextRequest, NextResponse } from 'next/server';
import { TOOLS_DATA } from '@/lib/tools-data';
import { ToolCategory } from '@/lib/tools-registry';

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  
  const query = searchParams.get('query')?.toLowerCase() || '';
  const category = searchParams.get('category') as ToolCategory | null;
  const capabilities = searchParams.get('capabilities')?.split(',').filter(Boolean) || [];
  const freeOnly = searchParams.get('freeOnly') === 'true';
  const page = parseInt(searchParams.get('page') || '1');
  const limit = parseInt(searchParams.get('limit') || '20');

  let filteredTools = [...TOOLS_DATA];

  // 搜索过滤
  if (query) {
    filteredTools = filteredTools.filter(tool =>
      tool.name.toLowerCase().includes(query) ||
      tool.description.toLowerCase().includes(query) ||
      tool.metadata.tags.some(tag => tag.toLowerCase().includes(query))
    );
  }

  // 分类过滤
  if (category) {
    filteredTools = filteredTools.filter(tool => tool.category === category);
  }

  // 能力过滤
  if (capabilities.length > 0) {
    filteredTools = filteredTools.filter(tool =>
      capabilities.every(cap => tool.capabilities.includes(cap))
    );
  }

  // 免费过滤
  if (freeOnly) {
    filteredTools = filteredTools.filter(tool => tool.pricing.hasFreeTier);
  }

  // 排序
  filteredTools.sort((a, b) => (b.stats?.popularity || 0) - (a.stats?.popularity || 0));

  // 分页
  const total = filteredTools.length;
  const totalPages = Math.ceil(total / limit);
  const startIndex = (page - 1) * limit;
  const paginatedTools = filteredTools.slice(startIndex, startIndex + limit);

  return NextResponse.json({
    success: true,
    data: {
      tools: paginatedTools,
      total,
      page,
      perPage: limit,
      totalPages
    },
    meta: {
      generatedAt: new Date().toISOString(),
      cacheTTL: 3600,
      version: '1.0.0'
    }
  });
}
