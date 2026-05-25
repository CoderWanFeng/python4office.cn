import { NextRequest, NextResponse } from 'next/server';
import { POSTS_DATA } from '@/lib/posts-data';
import { Post } from '@/lib/posts-types';

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  
  const query = searchParams.get('query')?.toLowerCase() || '';
  const tags = searchParams.get('tags')?.split(',').filter(Boolean) || [];
  const categories = searchParams.get('categories')?.split(',').filter(Boolean) || [];
  const featured = searchParams.get('featured') === 'true';
  const page = parseInt(searchParams.get('page') || '1');
  const limit = parseInt(searchParams.get('limit') || '20');
  const sortBy = searchParams.get('sortBy') || 'date';

  let filteredPosts = [...POSTS_DATA].filter(post => !post.draft);

  // 搜索过滤
  if (query) {
    filteredPosts = filteredPosts.filter(post =>
      post.title.toLowerCase().includes(query) ||
      post.description?.toLowerCase().includes(query) ||
      post.tags.some(tag => tag.toLowerCase().includes(query)) ||
      post.content?.toLowerCase().includes(query)
    );
  }

  // 标签过滤
  if (tags.length > 0) {
    filteredPosts = filteredPosts.filter(post =>
      tags.some(tag => post.tags.includes(tag))
    );
  }

  // 分类过滤
  if (categories.length > 0) {
    filteredPosts = filteredPosts.filter(post =>
      categories.some(cat => post.categories?.includes(cat))
    );
  }

  // 精选过滤
  if (featured) {
    filteredPosts = filteredPosts.filter(post => post.featured);
  }

  // 排序
  switch (sortBy) {
    case 'title':
      filteredPosts.sort((a, b) => a.title.localeCompare(b.title));
      break;
    case 'updated':
      filteredPosts.sort((a, b) => {
        const aDate = a.updated || a.date;
        const bDate = b.updated || b.date;
        return new Date(bDate).getTime() - new Date(aDate).getTime();
      });
      break;
    case 'date':
    default:
      filteredPosts.sort((a, b) => 
        new Date(b.date).getTime() - new Date(a.date).getTime()
      );
  }

  // 分页
  const total = filteredPosts.length;
  const totalPages = Math.ceil(total / limit);
  const startIndex = (page - 1) * limit;
  const paginatedPosts = filteredPosts.slice(startIndex, startIndex + limit);

  // 移除详细内容
  const postsWithoutContent = paginatedPosts.map(({ content, ...post }) => post);

  return NextResponse.json({
    success: true,
    data: {
      posts: postsWithoutContent,
      total,
      page,
      perPage: limit,
      totalPages
    },
    meta: {
      generatedAt: new Date().toISOString()
    }
  });
}
