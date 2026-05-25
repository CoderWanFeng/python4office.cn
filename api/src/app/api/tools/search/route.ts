import { NextRequest, NextResponse } from 'next/server';
import { TOOLS_DATA } from '@/lib/tools-data';

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const q = searchParams.get('q')?.toLowerCase() || '';

  if (!q || q.length < 2) {
    return NextResponse.json({
      success: false,
      error: {
        code: 'INVALID_QUERY',
        message: 'Query must be at least 2 characters'
      }
    }, { status: 400 });
  }

  const results = TOOLS_DATA
    .filter(tool =>
      tool.name.toLowerCase().includes(q) ||
      tool.description.toLowerCase().includes(q) ||
      tool.metadata.tags.some(tag => tag.toLowerCase().includes(q)) ||
      tool.capabilities.some(cap => cap.toLowerCase().includes(q))
    )
    .map(tool => ({
      id: tool.id,
      name: tool.name,
      description: tool.description,
      category: tool.category,
      openclaw_compatible: tool.openclaw.compatible,
      has_free_tier: tool.pricing.hasFreeTier,
      registration_url: tool.auth.registrationUrl,
      match_reasons: [
        tool.name.toLowerCase().includes(q) && '名称匹配',
        tool.description.toLowerCase().includes(q) && '描述匹配',
        tool.metadata.tags.some(tag => tag.toLowerCase().includes(q)) && '标签匹配',
        tool.capabilities.some(cap => cap.toLowerCase().includes(q)) && '功能匹配'
      ].filter(Boolean)
    }))
    .sort((a, b) => b.match_reasons.length - a.match_reasons.length)
    .slice(0, 20);

  return NextResponse.json({
    success: true,
    query: q,
    results,
    total: results.length,
    meta: {
      generatedAt: new Date().toISOString()
    }
  });
}
