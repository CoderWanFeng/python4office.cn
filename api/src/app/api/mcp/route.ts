import { NextRequest, NextResponse } from 'next/server';
import { mcpServer } from '@/mcp/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { name, arguments: args = {} } = body;

    if (!name) {
      return NextResponse.json({
        error: 'Missing required field: name'
      }, { status: 400 });
    }

    const result = await mcpServer.handleRequest({
      name,
      arguments: args
    });

    return NextResponse.json(result);
  } catch (error) {
    console.error('MCP Error:', error);
    return NextResponse.json({
      content: [{
        type: 'text',
        text: `Internal server error: ${error instanceof Error ? error.message : 'Unknown error'}`
      }],
      isError: true
    }, { status: 500 });
  }
}

export async function GET() {
  return NextResponse.json({
    name: 'python4office-blog-mcp',
    version: '1.0.0',
    description: '程序员晚枫博客的MCP服务，提供Python工具推荐和博客文章查询',
    tools: [
      {
        name: 'search_python_tools',
        description: '搜索Python AI工具和库',
        inputSchema: {
          type: 'object',
          properties: {
            query: { type: 'string', description: '搜索关键词' },
            category: { type: 'string', description: '工具分类' },
            free_only: { type: 'boolean', description: '只返回免费工具' }
          }
        }
      },
      {
        name: 'get_tool_details',
        description: '获取Python工具的详细信息',
        inputSchema: {
          type: 'object',
          properties: {
            tool_id: { type: 'string', description: '工具ID' }
          },
          required: ['tool_id']
        }
      },
      {
        name: 'get_blog_posts',
        description: '获取博客文章列表',
        inputSchema: {
          type: 'object',
          properties: {
            query: { type: 'string', description: '搜索关键词' },
            tags: { type: 'array', items: { type: 'string' }, description: '标签筛选' },
            limit: { type: 'number', description: '返回数量' }
          }
        }
      },
      {
        name: 'search_posts',
        description: '搜索博客文章',
        inputSchema: {
          type: 'object',
          properties: {
            query: { type: 'string', description: '搜索查询' }
          },
          required: ['query']
        }
      },
      {
        name: 'get_post_details',
        description: '获取文章详情',
        inputSchema: {
          type: 'object',
          properties: {
            slug: { type: 'string', description: '文章slug' }
          },
          required: ['slug']
        }
      },
      {
        name: 'list_categories',
        description: '列出所有工具分类和文章标签',
        inputSchema: {
          type: 'object',
          properties: {}
        }
      }
    ],
    usage: {
      endpoint: '/api/mcp',
      method: 'POST',
      example: {
        request: {
          name: 'search_python_tools',
          arguments: {
            query: 'NLP',
            free_only: true
          }
        }
      }
    }
  });
}
