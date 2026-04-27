import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.any().default('Untitled'),
    date: z.any().default(new Date()),
    tags: z.any().optional(),
    categories: z.any().optional(),
    description: z.any().optional(),
    author: z.any().optional(),
  }).passthrough(),
});

export const collections = { blog };
