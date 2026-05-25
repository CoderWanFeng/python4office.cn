import { NextRequest, NextResponse } from 'next/server';
import { TOOLS_DATA } from '@/lib/tools-data';

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params;
  const tool = TOOLS_DATA.find(t => t.id === id);

  if (!tool) {
    return NextResponse.json({
      success: false,
      error: {
        code: 'TOOL_NOT_FOUND',
        message: `Tool with id '${id}' not found`
      }
    }, { status: 404 });
  }

  const related = TOOLS_DATA
    .filter(t => t.id !== id && t.category === tool.category)
    .slice(0, 3);

  return NextResponse.json({
    success: true,
    data: tool,
    related,
    meta: {
      generatedAt: new Date().toISOString()
    }
  });
}
