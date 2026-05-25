import { NextRequest, NextResponse } from 'next/server';
import { POSTS_DATA } from '@/lib/posts-data';
import { Post, AIFriendlyPost } from '@/lib/posts-types';

function convertToAIFriendly(post: Post): AIFriendlyPost {
  return {
    slug: post.slug,
    title: post.title,
    summary: post.description || `关于 ${post.title} 的文章`,
    tags: post.tags,
    date: post.date,
    url: `https://www.python4office.cn/${post.slug}`,
    reading_time_minutes: post.readingTime || Math.ceil((post.wordCount || 1000) / 200)
  };
}

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  
  const q = searchParams.get('q')?.toLowerCase() || '';
  const tags = searchParams.get('tags')?.split(',').filter(Boolean) || [];
  const maxResults = parseInt(searchParams.get('limit') || '10');

  let filteredPosts = [...POSTS_DATA].filter(post => !post.draft);

  // 搜索过滤
  if (q) {
    filteredPosts = filteredPosts.filter(post =>
      post.title.toLowerCase().includes(q) ||
      post.description?.toLowerCase().includes(q) ||
      post.tags.some(tag => tag.toLowerCase().includes(q)) ||
      post.content?.toLowerCase().includes(q)
    );
  }

  // 标签过滤
  if (tags.length > 0) {
    filteredPosts = filteredPosts.filter(post =>
      tags.some(tag => post.tags.includes(tag))
    );
  }

  // 排序
  filteredPosts.sort((a, b) => 
    new Date(b.date).getTime() - new Date(a.date).getTime()
  );

  // 限制结果
  const limitedPosts = filteredPosts.slice(0, maxResults);

  const aiFriendlyPosts = limitedPosts.map(convertToAIFriendly);

  return NextResponse.json({
    posts: aiFriendlyPosts,
    count: aiFriendlyPosts.length,
    purpose: '提供给AI Agent使用的文章列表，可用于问答和内容推荐',
    format_version: '1.0'
  }, {
    headers: {
      'Cache-Control': 'public, max-age=3600',
      'Content-Type': 'application/json'
    }
  });
}
