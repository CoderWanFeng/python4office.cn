import { NextRequest, NextResponse } from 'next/server';
import { POSTS_DATA } from '@/lib/posts-data';

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ slug: string }> }
) {
  const { slug } = await params;
  const post = POSTS_DATA.find(p => p.slug === slug);

  if (!post) {
    return NextResponse.json({
      success: false,
      error: {
        code: 'POST_NOT_FOUND',
        message: `Post with slug '${slug}' not found`
      }
    }, { status: 404 });
  }

  // 获取相关文章
  const related = POSTS_DATA
    .filter(p => p.slug !== slug && 
      (p.tags.some(tag => post.tags.includes(tag)) ||
       p.categories?.some(cat => post.categories?.includes(cat)))
    )
    .slice(0, 5)
    .map(({ content, ...p }) => p);

  return NextResponse.json({
    success: true,
    data: post,
    related,
    meta: {
      generatedAt: new Date().toISOString()
    }
  });
}
