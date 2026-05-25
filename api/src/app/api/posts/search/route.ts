import { NextRequest, NextResponse } from 'next/server';
import { POSTS_DATA } from '@/lib/posts-data';

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

  const results = POSTS_DATA
    .filter(post => !post.draft)
    .filter(post =>
      post.title.toLowerCase().includes(q) ||
      post.description?.toLowerCase().includes(q) ||
      post.tags.some(tag => tag.toLowerCase().includes(q)) ||
      post.content?.toLowerCase().includes(q)
    )
    .map(post => ({
      slug: post.slug,
      title: post.title,
      description: post.description,
      tags: post.tags,
      date: post.date,
      match_reasons: [
        post.title.toLowerCase().includes(q) && '标题匹配',
        post.description?.toLowerCase().includes(q) && '描述匹配',
        post.tags.some(tag => tag.toLowerCase().includes(q)) && '标签匹配'
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
